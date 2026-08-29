---
name: agent-mark
description: Run a second-opinion code review through "Agent Mark", an external reviewer powered by Meta's Muse Spark 1.2 Contributor model on the Vercel AI Gateway. Use this whenever the user asks for Agent Mark by name, or asks for a review, audit, or second opinion from Muse Spark / Vercel AI Gateway / an outside or independent model — and also when they want a review from something other than Claude, want their code checked by a different model, or want a cross-check on findings Claude already produced. Covers whole files, git diffs, and piped snippets.
---

# Agent Mark

Agent Mark is a code reviewer that runs on `meta/muse-spark-1.2-contributor`
via the Vercel AI Gateway. It exists to give a genuinely independent read on
code — a different model, with no memory of the conversation that produced the
code, which is exactly what makes a second opinion worth having.

It is not a subagent. Claude Code subagents run Claude models only, so Agent
Mark is a script that calls the gateway directly.

## Running it

`scripts/agent_mark.py` handles auth, the request, and the failure modes.

```bash
python3 ~/.claude/skills/agent-mark/scripts/agent_mark.py path/to/file.py
python3 ~/.claude/skills/agent-mark/scripts/agent_mark.py --diff
python3 ~/.claude/skills/agent-mark/scripts/agent_mark.py src/*.ts --focus "auth and session handling"
git show HEAD:file.js | python3 ~/.claude/skills/agent-mark/scripts/agent_mark.py --stdin
```

The review goes to stdout; the model, token counts and dollar cost go to
stderr, so `> review.md` captures just the review.

Auth comes from `$AI_GATEWAY_API_KEY`, falling back to `VERCELAIGATEWAY` in the
apikeys store (`~/.config/apikeys/.env`). If neither exists the script says so
rather than failing obscurely.

## The privacy rule — this is the important part

The contributor tier is cheap because **Vercel's model listing states inputs and
outputs are used to train Meta's models** (`zdr: none`, `no_training: none`).
Anything sent to Agent Mark should be treated as published.

The script enforces this: it checks `gh repo view` and refuses to send when the
repo is private or visibility can't be determined, unless the user passes
`--yes` or confirms at the prompt. Do not reach for `--yes` to make a refusal go
away — surface it to the user and let them decide, because they are the only one
who knows whether that code can leave the building. For private code, review it
with Claude instead.

## Cost and the empty-review trap

Pricing is roughly $0.10 per million input tokens and $0.20 per million output,
so a 20k-token file costs well under a cent. Check the user's balance if it
might be low: `curl -s -H "Authorization: Bearer $KEY" https://ai-gateway.vercel.sh/v1/credits`

This model is heavily reasoning-based and will happily spend 7,000 tokens
thinking before writing anything. If `max_tokens` is too small the response
comes back `finish_reason: length` with **empty content** — a silent non-answer
that looks like a bug. The script defaults to 32,000 tokens and automatically
retries at double the budget if it still comes back empty, so you normally never
see this. If you call the gateway by hand, budget generously.

## Reporting findings back to the user

Agent Mark is another model, not an oracle, and it has none of the context you
have about the codebase. Treat its output as a set of claims to check, not
results to relay.

This is not hypothetical. On its first real run against a 1,800-line userscript,
both findings Agent Mark rated **critical** were false: it reported a missing
MutationObserver fallback that was present in the very function it cited, and a
missing `storageReady` gate on a call that was already inside `storageReady.then()`.
The three findings that held up were the medium-severity ones. Expect roughly this
shape - plausible reasoning about code it has half-read, with confidence inversely
related to accuracy - and budget time for checking rather than for reading.

Before presenting findings, open the file and verify each one against the actual
code. Report what you confirmed, drop what turned out to be wrong, and say
plainly which is which — "Agent Mark flagged X; I checked and it's real / it
misread the code because Y". Passing along an unverified finding wastes the
user's time chasing a bug that isn't there, and quietly deleting a wrong one
hides that the reviewer was unreliable. Both matter.

Where Agent Mark and your own reading disagree, say so and explain the
disagreement rather than silently picking a side.

## Suggested structure

Group by severity, worst first. For each finding: where it is, what concretely
breaks, the fix, and your verification verdict. A short "what Agent Mark got
wrong" section at the end is worth including when it applies — it tells the user
how much weight to give the next review.
