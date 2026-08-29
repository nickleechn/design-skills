#!/usr/bin/env python3
"""
Agent Mark - code review through Muse Spark 1.2 Contributor on the Vercel AI Gateway.

Usage:
    agent_mark.py FILE [FILE ...]          review whole files
    agent_mark.py --diff [GIT_ARGS]        review a git diff (default: HEAD)
    agent_mark.py --stdin                  review code piped in
    agent_mark.py FILE --focus "security"  steer the review
    agent_mark.py FILE --effort xhigh      change how hard the model thinks

The contributor tier trains on what you send it, so the script refuses to run
on a non-public repo unless you pass --yes. See PRIVACY below.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

GATEWAY = "https://ai-gateway.vercel.sh/v1/chat/completions"
MODEL = "meta/muse-spark-1.2-contributor"

# This model is reasoning-heavy: a 20k-token file routinely burns 6-8k tokens
# thinking before it emits a single visible character. Too small a budget and
# the response comes back finish_reason=length with content="" - a silent empty
# review. Start high and grow on retry rather than guessing low.
DEFAULT_MAX_TOKENS = 32000

# The gateway validates reasoning.effort against this set - a bad value is a
# 400, not a silent ignore, so the flag is genuinely wired through to the model.
# Measured caveat: 'minimal' visibly suppresses thinking, but low/high/xhigh sat
# in the same token band on a sample workload, so treat 'high' as a sensible
# default rather than a proven quality win over the model's own default.
EFFORT_CHOICES = ("none", "minimal", "low", "medium", "high", "xhigh", "max")
DEFAULT_EFFORT = "high"

PRIVACY = """\
NOTE: %s is a 'contributor' tier model. Vercel's own model listing states your
inputs and outputs are used to train Meta's models (zdr: none, no_training: none).
Only send code you are willing to make public.""" % MODEL


def load_key():
    """$AI_GATEWAY_API_KEY wins; otherwise read VERCELAIGATEWAY from the apikeys store."""
    key = os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("VERCELAIGATEWAY")
    if key:
        return key.strip()

    store = os.environ.get("APIKEYS_ENV_FILE")
    if not store:
        base = os.environ.get("XDG_CONFIG_HOME") or os.path.join(
            os.path.expanduser("~"), ".config")
        store = os.path.join(base, "apikeys", ".env")
    if not os.path.exists(store):
        die("no API key: set $AI_GATEWAY_API_KEY, or store VERCELAIGATEWAY in %s" % store)

    for line in open(store, encoding="utf-8"):
        line = line.strip()
        if line.startswith("VERCELAIGATEWAY="):
            raw = line.split("=", 1)[1].strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
                raw = raw[1:-1]
            if raw:
                return raw
    die("VERCELAIGATEWAY not found (or empty) in %s" % store)


def die(message, code=1):
    sys.stderr.write("agent-mark: %s\n" % message)
    raise SystemExit(code)


def repo_is_public():
    """True/False/None - None when we genuinely cannot tell."""
    try:
        out = subprocess.run(["gh", "repo", "view", "--json", "visibility", "-q", ".visibility"],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                             universal_newlines=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return out.stdout.strip().lower() == "public"


def gather(args):
    """Return (label, code) for whatever the user asked to review."""
    if args.stdin:
        return "stdin", sys.stdin.read()
    if args.diff:
        cmd = ["git", "diff"] + (args.diff_args or ["HEAD"])
        out = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
        if out.returncode != 0:
            die("git diff failed")
        if not out.stdout.strip():
            die("the diff is empty - nothing to review")
        return " ".join(cmd), out.stdout
    chunks = []
    for path in args.files:
        if not os.path.isfile(path):
            die("not a file: %s" % path)
        with open(path, encoding="utf-8", errors="replace") as handle:
            chunks.append("----- %s -----\n%s" % (path, handle.read()))
    return ", ".join(args.files), "\n\n".join(chunks)


def build_prompt(label, code, focus):
    steer = ("\nWeight the review toward: %s\n" % focus) if focus else ""
    return (
        "You are reviewing code. Report real defects, not style preferences, and "
        "skip praise entirely.\n\n"
        "Before reporting a finding, satisfy yourself that it survives the code as "
        "written. The most common way a review like this goes wrong is asserting "
        "that a guard, fallback or ordering constraint is missing when it is "
        "actually present a few lines away - so for each finding, first locate the "
        "place the fix would go and read what is already there.\n\n"
        "Evidence requirement: quote the exact line(s) your finding rests on, "
        "verbatim from the source, and give the line numbers. If you cannot quote "
        "the code that proves the defect, do not report it. A finding whose "
        "quotation turns out to contradict the claim is worse than no finding, "
        "because someone will spend an hour chasing it.\n\n"
        "For each finding give: severity (critical/high/medium/low), the function "
        "and line numbers, the verbatim quote, what concretely goes wrong (the "
        "inputs or conditions that trigger it), and a specific fix.\n"
        "State your confidence. If you are unsure whether something is a real bug, "
        "say so plainly rather than rounding up to certainty - a hedged finding is "
        "useful, a confident wrong one is not.\n"
        "Reserve critical/high for defects you can prove from the quoted code. "
        "Order findings by severity, worst first.\n"
        "%s\nSubject: %s\n\n```\n%s\n```" % (steer, label, code)
    )


def call(key, model, prompt, max_tokens, timeout, effort=DEFAULT_EFFORT):
    payload = {"model": model,
               "messages": [{"role": "user", "content": prompt}],
               "temperature": 0.2,
               "max_tokens": max_tokens}
    if effort:
        payload["reasoning"] = {"effort": effort}
    req = urllib.request.Request(
        GATEWAY, data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": "Bearer " + key,
                 "Content-Type": "application/json",
                 "User-Agent": "agent-mark"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()[:400]
        if exc.code == 401:
            die("gateway rejected the key (401). Check VERCELAIGATEWAY.\n  %s" % body)
        if exc.code in (402, 429):
            die("gateway says out of credit or rate limited (%d).\n  %s" % (exc.code, body))
        die("gateway HTTP %d\n  %s" % (exc.code, body))
    except Exception as exc:
        die("request failed: %s" % exc)


def main():
    parser = argparse.ArgumentParser(description="Code review via Muse Spark Contributor.")
    parser.add_argument("files", nargs="*", help="files to review")
    parser.add_argument("--diff", action="store_true", help="review a git diff instead")
    parser.add_argument("--diff-args", nargs="*", help="args for git diff (default: HEAD)")
    parser.add_argument("--stdin", action="store_true", help="read code from stdin")
    parser.add_argument("--focus", help="steer the review, e.g. 'security' or 'concurrency'")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--effort", choices=EFFORT_CHOICES, default=DEFAULT_EFFORT,
                        help="reasoning effort (default: %s)" % DEFAULT_EFFORT)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--json", action="store_true", help="emit the raw API response")
    parser.add_argument("-y", "--yes", action="store_true",
                        help="skip the training-data confirmation")
    args = parser.parse_args()

    if not (args.files or args.diff or args.stdin):
        parser.error("give one or more FILEs, or --diff, or --stdin")

    label, code = gather(args)
    if not code.strip():
        die("nothing to review")

    # The privacy gate is the point of this script, so make it hard to skip by
    # accident but trivial to skip on purpose.
    sys.stderr.write(PRIVACY + "\n")
    public = repo_is_public()
    if not args.yes and public is not True:
        where = "could not determine repo visibility" if public is None else "this repo is PRIVATE"
        if sys.stdin.isatty():
            answer = input("agent-mark: %s. Send anyway? [y/N]: " % where).strip().lower()
            if answer not in ("y", "yes"):
                die("aborted - nothing was sent", 2)
        else:
            die("%s; refusing to send. Pass --yes to override." % where, 2)

    key = load_key()
    budget = args.max_tokens
    for attempt in (1, 2):
        data = call(key, args.model, build_prompt(label, code, args.focus), budget,
                    args.timeout, args.effort)
        if args.json:
            print(json.dumps(data, indent=2))
            return 0
        choice = data["choices"][0]
        content = (choice.get("message") or {}).get("content") or ""
        usage = data.get("usage", {})
        detail = usage.get("completion_tokens_details", {}) or {}
        if content.strip():
            print(content)
            sys.stderr.write(
                "\n--- %s | effort %s | in %s tok, out %s tok (%s reasoning) | $%.4f ---\n"
                % (data.get("model", args.model), args.effort, usage.get("prompt_tokens"),
                   usage.get("completion_tokens"), detail.get("reasoning_tokens", "?"),
                   float(usage.get("cost", 0) or 0)))
            return 0
        if choice.get("finish_reason") == "length" and attempt == 1:
            budget *= 2
            sys.stderr.write(
                "agent-mark: the model spent its whole %d-token budget reasoning and "
                "returned nothing. Retrying with %d.\n" % (args.max_tokens, budget))
            continue
        die("empty review (finish_reason=%s). Try a larger --max-tokens."
            % choice.get("finish_reason"))
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
