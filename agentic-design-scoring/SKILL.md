---
name: agentic-design-scoring
description: Score a design's quality out of 100 using the ADS rubric — 40% design, 30% usability (including WCAG 2.0 AA conformance), 20% creativity, 10% content. Use when the user asks to score, rate, grade, evaluate, critique, benchmark or audit a design, screen, frame, mockup, landing page or UI, mentions ADS or "design score", or asks how good a design is or whether it meets WCAG 2.0 AA.
---

# Agentic Design Scoring (ADS)

A quantified, repeatable design score out of 100. Four weighted sections:

| Section | Weight | What it measures |
|---|---|---|
| **Design** | 40 | Hierarchy, typography, colour, layout, system adherence, craft |
| **Usability** | 30 | WCAG 2.0 AA conformance, affordance, IA, states, error handling |
| **Creativity** | 20 | Distinctiveness, concept fit, restraint, risk that lands |
| **Content** | 10 | Copy clarity, microcopy, voice, scannability |

> **The cap rule.** Accessibility is worth only 12 of the 100 points, so weighting alone cannot stop a beautiful, non-compliant design from scoring well. The cap does that instead:
> **any unresolved WCAG 2.0 Level A or AA failure caps the total at 79. Two or more distinct Level A failures cap it at 69.**
> The cap is always shown in the report: `Raw 86 → capped 79 (1.4.3 contrast failure)`.

---

## 0. The three rules that make the number mean something

**1. Binary before scalar.** Run the WCAG pass/fail checklist (§4) *first*, then assign 0–5 scores (§5). Never score the rubric first and check accessibility afterwards — the checklist changes what the scores are allowed to be.

**2. One claim, one citation.** Every deduction and every score above the default names the frame and layer it came from. `PricingHero/subhead` — not "the subheading". If you cannot cite it, you cannot score it.

**3. Measure, don't eyeball.** Contrast from fill hex values. Target size from layer bounds. Type-style count from the styles panel. Spacing from auto-layout values. Line length from character count. Estimating any of these when the real value is available is a defect in the scoring, not a shortcut.

**Taste never compensates for compliance.** Design and Creativity scores may not offset an accessibility failure. When a visually strong screen fails AA, say so in the verdict line, in plain words.

---

## 1. Pick the target

Score **the current selection**. If nothing is selected, score **the current page**.

Accepted inputs, each with a confidence level that you print in the report header:

| Input | Confidence | Consequence |
|---|---|---|
| Figma frames with layer data | **High** | Contrast computed from real fill hexes; all checks available |
| Live URL or rendered HTML | **High** | Contrast from computed styles; all checks available |
| Static screenshot only | **Medium** | Contrast sampled from pixels — note antialiasing risk on text under 16px; layer-level checks (tokens, instances, variants) unavailable |
| Code component | **Medium** | Structure and copy checkable; rendered spacing and hierarchy are inferred |
| Verbal description only | — | **Refuse to score.** Ask for an artefact. A score with no artefact is a guess wearing a number. |

When a check cannot be performed because of the input type, mark it **not assessed** and say why. Never let an unavailable check silently pass.

---

## 2. Step 0 — the Design Read

Before scoring anything, print one line declaring what this design is *trying* to be:

```
Design Read: [archetype] for [audience]; expected variance [low/med/high], density [low/med/high]. (briefed | inferred)
```

Archetypes: `marketing/landing` · `product UI` · `dashboard/data` · `editorial` · `public-sector service` · `portfolio` · `mobile app` · `email`.

Typical expectations:

| Archetype | Variance | Density | Notes |
|---|---|---|---|
| Marketing / landing | High | Low–med | Distinctiveness is part of the job |
| Portfolio / agency | High | Low | Boldness expected; timidity is a real fault |
| Product UI | Medium | Medium | Consistency outranks novelty |
| Dashboard / data | Low | High | Restraint is correct, not a deficiency |
| Editorial | Medium | Low–med | Typography carries most of the load |
| Public-sector service | Low | Medium | Clarity and compliance outrank flair |

**Why this exists.** Creativity is 20% of the score. Without a declared intent, a well-built government form gets punished for lacking flair, and a timid agency landing page gets rewarded for being inoffensive. Both are wrong.

**Judge Creativity as appropriateness of the choice, not as quantity of flair.** Restraint that fits the brief can score 5. Restraint that is merely timid — an archetype that calls for boldness, delivered as a centred stack of cards — cannot score above 2 on C1, however tidy it is.

If the user gave a brief, use it. If not, infer from the artefact and label it `(inferred)`, so a wrong inference is visible and correctable rather than buried in the score.

---

## 3. Gather evidence

Record these before forming any judgment. This is the raw material every later citation draws on.

**Structure**
- Frame names and dimensions; how many frames/screens are in scope
- Section count and the layout family of each (centred stack · split image+text · grid/bento · full-bleed · sidebar · table)
- Layer order within each frame — this is your proxy for reading and focus order

**Type**
- Every distinct text style: font family, size, weight, line height, letter spacing, fill
- Count of distinct type styles per screen (more than 4 is a flag, not an automatic fault)
- Body line length in characters at the design width

**Colour**
- Every fill and stroke hex, with opacity
- Any gradient stops, and any overlay stacked above a background
- The accent colour(s); count them
- Whether light and dark variants exist

**Layout**
- Auto-layout padding and gap values; whether they resolve to a consistent step (4/8pt or similar)
- Corner radius values in use; count the distinct systems
- Grid/bento cell count vs. item count

**System**
- Which fills, type styles and spacing values are bound to variables/tokens vs. hard-coded
- Which elements are component instances vs. detached or redrawn
- Which states exist as variants: default, hover, focus, active, disabled, loading, empty, error, success

**Content**
- Every visible string: headings, labels, button text, helper text, error text, empty-state copy
- Placeholder or lorem text, and any name/number that looks invented

---

## 4. WCAG 2.0 AA — run this first

Scope note: this checklist is **strictly WCAG 2.0 Level A and AA**. Non-text contrast (1.4.11), reflow (1.4.10), text spacing (1.4.12), target size (2.5.5/2.5.8) and status messages (4.1.3) are **WCAG 2.1/2.2** and are *not* scored here — they appear in the advisory at §4.4.

### 4.1 Design-evaluable criteria

Check every one. Mark `pass`, `fail` or `N/A`, and name the offending layer on any failure.

| SC | Level | What to inspect |
|---|---|---|
| 1.1.1 Non-text Content | A | Every meaningful icon, image, chart and icon-only button has an intended text alternative or accessible name. Decorative graphics explicitly marked decorative. Icon-only buttons with no label are the usual failure. |
| 1.3.1 Info and Relationships | A | Visual grouping, heading levels and label-to-field association are expressible in markup. Headings that are just big bold text with no hierarchy; fields whose label is only spatially adjacent. |
| 1.3.2 Meaningful Sequence | A | Reading order matches visual order. Compare layer order and auto-layout flow against the visual reading path. Absolutely-positioned overlays and reordered columns are common breaks. |
| 1.3.3 Sensory Characteristics | A | No instruction relies on shape, size, position or sound alone — "the green button on the right", "click the icon below". |
| 1.4.1 Use of Color | A | Colour is never the only carrier of meaning. Links distinguished only by colour; required fields marked only red; error state signalled only by a red border; chart series separated only by hue. Each needs a second cue — underline, icon, text label, pattern. |
| **1.4.3 Contrast (Minimum)** | **AA** | See §4.3. Compute every text/background pair. |
| 1.4.4 Resize Text | AA | Layout survives 200% text scale. Flag fixed-height text containers, clipped overflow, text set in a box with no room to grow, single-line buttons whose label already nearly fills them. |
| 1.4.5 Images of Text | AA | No text baked into a raster image except logotypes. Flag screenshot-as-content and text rendered inside an exported graphic. |
| 2.4.2 Page Titled | A | Each screen has a title, and it describes the screen. |
| 2.4.3 Focus Order | A | A logical tab path exists and follows the visual order. Where visual order and layer order diverge, flag it. |
| 2.4.4 Link Purpose (In Context) | A | Link and button text describes its destination or action. "Click here", "Read more" repeated five times, bare arrows. |
| 2.4.5 Multiple Ways | AA | More than one route to key destinations across a set of screens — nav plus search, or nav plus sitemap/index. Only applies when multiple screens are in scope and the design represents a site rather than a single-purpose flow. |
| 2.4.6 Headings and Labels | AA | Headings describe their section; labels describe their input. Flag decorative all-caps headings that carry no informational role. |
| **2.4.7 Focus Visible** | **AA** | A focus indicator is actually designed, and is visually distinct from the hover state. A component set with hover but no focus variant is a fail, not an omission to note later. This is the most commonly missed criterion in Figma work. |
| 3.2.3 Consistent Navigation | AA | Nav position, order and content identical across screens. Requires multiple frames. |
| 3.2.4 Consistent Identification | AA | The same function is labelled and iconed the same way everywhere. "Delete" here, "Remove" there, a bare trash icon elsewhere. Requires multiple frames. |
| 3.3.1 Error Identification | A | Errors described in text and the failing field named. A red border alone fails this and 1.4.1 together. |
| 3.3.2 Labels or Instructions | A | Every input has a visible, persistent label. Placeholder-as-label is a fail — the label vanishes on input. Format requirements stated before submission, not after. |
| 3.3.3 Error Suggestion | AA | Where the fix is knowable, it is offered: expected format, an example, a correction. "Invalid input" alone fails. |
| 3.3.4 Error Prevention | AA | For legal, financial or data-destructive actions: a confirm, review or reverse step exists. |

### 4.2 Indicative only — flag as risk, never certify

These cannot be *passed* from a static design. A frame can reveal a problem but cannot demonstrate conformance. Report them as `risk` or `not assessed`, never as `pass`.

| SC | Level | Risk visible in a design |
|---|---|---|
| 2.1.1 Keyboard | A | Hover-only reveals with no persistent equivalent; custom controls with no plausible focus path |
| 2.1.2 No Keyboard Trap | A | Modals, carousels and dropdowns with no visible dismiss affordance |
| 2.2.2 Pause, Stop, Hide | A | **Applies whenever moving content is shown** — a marquee, auto-advancing carousel, auto-playing logo strip or looping animation. If no pause/stop control is designed, that is a real Level A risk worth raising, not a footnote |
| 3.1.1 Language of Page | A | Multilingual content with no indication of language handling |
| 4.1.2 Name, Role, Value | A | Toggles, checkboxes and switches with no visual on/off distinction; custom components with no evident role |

### 4.3 Contrast — compute, never estimate

**The maths.** For each channel `c` in 0–255:

```
cs  = c / 255
lin = cs / 12.92                    if cs <= 0.03928
lin = ((cs + 0.055) / 1.055) ^ 2.4  otherwise

L = 0.2126*R_lin + 0.7152*G_lin + 0.0722*B_lin

ratio = (L_lighter + 0.05) / (L_darker + 0.05)
```

**Truncate to 2 decimal places. Never round up.** A pair computing to 4.4781 is **4.47**, and it fails 4.5:1. A ratio that reaches the threshold only by rounding has not met it.

**Flatten before you compute.** Opacity and overlays change the actual rendered colour:

```
c_effective = alpha * c_foreground + (1 - alpha) * c_backdrop
```

- Text at 60% opacity is not its own hex — flatten it against what is behind it.
- Over a **gradient**: test the lightest *and* the darkest point beneath the text. Both must pass.
- Over an **image**: test the worst-case region under the text, not an average.
- Over a **scrim**: flatten the scrim onto the image first, then the text onto that.

**Thresholds**

| Text | Required |
|---|---|
| Normal | **4.5:1** |
| Large — 18pt+ regular, or 14pt+ bold | **3:1** |

In Figma at 1×, large text is approximately **24px regular or 18.66px bold**. Use the pt definition when the design declares points.

**Exemptions, precisely**
- **Logotypes** are exempt.
- **Inactive (disabled) components** are exempt. Do not report disabled text as a failure — note it as advisory if it is genuinely illegible.
- **Placeholder text is NOT exempt.** It is not an inactive component. It must meet 4.5:1. This is the single most common false pass in design accessibility reviews.

**Verify your own arithmetic before reporting any number.** Two anchor pairs:

```
#767676 on #FFFFFF  =  4.54:1  → PASSES 4.5:1
#777777 on #FFFFFF  =  4.47:1  → FAILS  4.5:1
```

If you cannot reproduce both values, say so and report contrast as unverified rather than publishing numbers you do not trust.

**Named failure patterns — check for these every time.** They recur in almost every real review:

- White or near-white text on a white/light button fill
- Ghost or outline button over a photograph with no scrim, stroke or backdrop
- Transparent button on the page background with no border and no contrasting label
- Light grey placeholder text on a near-white input
- Form labels set in a grey below 4.5:1 — very common at `#999999` (2.84:1 on white) and `#8E8E93`
- Focus rings and error text below the threshold
- Body copy at `#767676` or lighter — the boundary case above
- White text on a mid-tone brand colour that only passes at large sizes but is used at body size

### 4.4 Beyond WCAG 2.0 AA — advisory, never scored

Report these as advisories so they are visible, and state plainly that they are **not** part of WCAG 2.0 AA:

- **1.4.11 Non-text Contrast** (2.1 AA) — UI component boundaries and graphical objects at 3:1
- **1.4.10 Reflow** (2.1 AA) — no horizontal scroll at 320px equivalent
- **1.4.12 Text Spacing** (2.1 AA) — survives increased line/letter/word spacing
- **2.5.5 / 2.5.8 Target Size** (2.1 AAA / 2.2 AA) — scored in ADS under U2, not here
- **4.1.3 Status Messages** (2.1 AA) — status changes announced without focus change
- **`prefers-reduced-motion`** — not a WCAG 2.0 criterion at all

---

## 5. The rubric

Score each sub-criterion **0–5**. Points = `(score ÷ 5) × weight`. Weights sum to 100, so the total is a straight sum — no normalisation.

**The 0–5 anchors, applied identically to every criterion:**

| Score | Meaning |
|---|---|
| **0** | Absent or broken |
| **1** | Severely deficient; actively harms the work |
| **2** | Below the professional bar |
| **3** | Competent but unremarkable — **the default** |
| **4** | Strong and evidently considered; requires a citation |
| **5** | Exemplary; rare; requires a stated reason it exceeds "correct" |

### 5.1 Design — 40 points

| # | Criterion | Pts | What earns and loses points |
|---|---|---|---|
| **D1** | Visual hierarchy and focal order | 9 | One unambiguous focal point per screen; the eye lands where the design intends. Deduct for competing focal weights, headline and CTA fighting, uniform emphasis across unequal content, or a hierarchy that reads only because of size with no support from weight, colour or space. |
| **D2** | Typography | 8 | A deliberate scale with distinguishable steps; line height suited to measure; body line length roughly 45–75 characters (65 is a good target); pairings chosen for contrast of role, not decoration. Deduct for more than 4 distinct type styles per screen without cause, cramped or airy leading, measure beyond ~85ch, and optical problems such as italic descenders clipping their container. |
| **D3** | Colour and material | 8 | One accent used consistently; neutrals with a deliberate hue bias rather than default mid-grey; off-black and off-white in preference to pure `#000000` / `#FFFFFF`; both light and dark states designed, not assumed. Deduct for a second competing accent, unbound rogue hexes, gradients that muddy at their midpoint, and dark mode produced by inversion. |
| **D4** | Layout, grid and spacing rhythm | 8 | Spacing resolves to a consistent step (4pt or 8pt); alignment is intentional; sections breathe in proportion to their importance. **Measure this from auto-layout padding and gap values — do not eyeball it.** Deduct for arbitrary one-off spacing, inconsistent gutters, and content floating without an evident grid relationship. |
| **D5** | Consistency and system adherence | 4 | Fills, type and spacing bound to variables/tokens; repeated UI built from component instances; one corner-radius system throughout. Deduct per detached instance, per rogue hard-coded hex where a token exists, and for mixed radius systems (a 4px card beside a 16px card with no rationale). |
| **D6** | Craft and finish | 3 | Optical alignment, not merely mathematical; coherent stroke weights and shadow logic; grid integrity — a bento or card grid has exactly as many cells as items, with no empty cells mid-grid. Deduct for half-pixel offsets, mismatched icon weights, shadows from inconsistent light sources. |

### 5.2 Usability — 30 points

| # | Criterion | Pts | What earns and loses points |
|---|---|---|---|
| **U1** | **WCAG 2.0 AA conformance** | 12 | Scored directly from §4. See the mapping below. |
| **U2** | Clarity and affordance | 6 | One obvious primary action per screen; what is interactive looks interactive; icons legible at their rendered size; **tap/click targets at least 44×44pt** (measure the bounds — this is a usability standard, *not* a WCAG 2.0 criterion); lists longer than 5 items use a suitable pattern rather than an undifferentiated stack. Deduct for competing CTAs of equal weight, vague verbs ("Submit", "OK", "Continue" with no object), duplicate CTA intent on one screen ("Get in touch" beside "Contact us"), and icon-only controls whose meaning is not recoverable. |
| **U3** | Information architecture and navigation | 5 | Structure predictable across frames; a user always knows where they are and how to leave. Cross-references 2.4.3, 2.4.5 and 3.2.3 — note the SC numbers here, but score the compliance itself once, in U1. Deduct for dead ends, back/close behaviour that changes between screens, and nesting that hides primary tasks. |
| **U4** | States and feedback | 4 | Default, hover, focus, active, disabled, loading, empty, error and success exist as named frames or component variants. Deduct one step for each of empty, loading and error that is missing — these three are the ones most often skipped, and their absence is where real products break. |
| **U5** | Error prevention and recovery | 3 | Destructive actions are confirmable or reversible; constraints are stated before submission rather than after; recovery from an error costs the user little. Deduct for irreversible destructive actions with no confirm, validation that only fires on submit, and errors that clear the user's input. |

**U1 score mapping** — read straight off the §4 checklist:

| U1 | Condition |
|---|---|
| 5 | Every design-evaluable SC passes; no risks outstanding |
| 4 | Every design-evaluable SC passes; advisories or indicative risks noted |
| 3 | Exactly one AA failure |
| 2 | Multiple AA failures, or one Level A failure |
| 1 | Multiple Level A failures |
| 0 | Failures pervasive across the screen |

**Any single SC failure caps U1 at 2**, regardless of how polished everything else is.

### 5.3 Creativity — 20 points

Judged against the **Design Read** from §2. Appropriateness, not quantity of flair.

| # | Criterion | Pts | What earns and loses points |
|---|---|---|---|
| **C1** | Distinctiveness | 8 | Scored against the slop checklist below. Does this look like a decision, or like a default? |
| **C2** | Concept fit | 6 | The visual idea serves this subject and this audience. Restraint that fits the archetype scores well here; restraint that is merely timid does not. Deduct when the aesthetic is borrowed from an unrelated category, or when decoration has no relationship to the content. |
| **C3** | Signature moment and restraint | 4 | Boldness spent in one place rather than distributed evenly until nothing stands out. One memorable move, supported by quiet surroundings. Deduct when every element competes for attention, or when nothing is memorable at all. |
| **C4** | Compositional risk that lands | 2 | A choice that could have failed and didn't — an unexpected crop, an asymmetry, a scale jump. Deduct nothing for its absence in low-variance archetypes; score 0–1 when a high-variance archetype plays it entirely safe. |

**C1 slop checklist.** Count the hits, cite each one. This is countable, not a matter of taste:

- AI-purple / violet-to-blue gradient as the primary brand gesture
- Inter (or the platform default sans) chosen with no evident consideration
- Three equal-width feature cards as the default way to present three things
- Centred hero over a dark mesh gradient
- Placeholder names and companies: John/Jane Doe, Acme, Nexus, SmartFlow
- Filler verbs in headlines: Elevate, Seamless, Unleash, Next-Gen, Revolutionize, Empower
- Fake-precise statistics with no source: "92%", "4.1×", "48k", "5.8mm"
- Three or more consecutive sections sharing the same layout family
- Eyebrow/kicker labels exceeding `ceil(section count ÷ 3)`
- Hero stack with more than 4 text elements, or subtext over 20 words
- More than one accent colour competing for primacy
- Mixed corner-radius systems with no rationale
- Stock iconography at inconsistent weights, or hand-drawn icons among library glyphs

**C1 ceiling by hit count:**

| Hits | C1 maximum |
|---|---|
| 0 | 5 |
| 1–2 | 4 |
| 3–4 | 3 |
| 5+ | 2 |

**Penalise a familiar pattern only when it substitutes for an idea.** A three-card row is not automatically slop — three genuinely parallel items belong in three parallel cards. It is slop when it is the shape the content was forced into because no other shape was considered. Say which one you are looking at.

**The checklist dates.** These are 2025–26 tells. Revisit the list periodically; today's default is next year's deliberate retro choice, and a stale list will score good work badly.

### 5.4 Content — 10 points

| # | Criterion | Pts | What earns and loses points |
|---|---|---|---|
| **N1** | Copy clarity and specificity | 4 | Real content, specific to this product. Deduct heavily for lorem ipsum, for placeholder strings shipped as final, and for copy so generic it would fit any competitor unchanged. |
| **N2** | Microcopy and labelling | 3 | Buttons name their action and object ("Create invoice", not "Submit"); error messages say what went wrong and what to do; empty states tell the user how to begin. All microcopy scores here and nowhere else. |
| **N3** | Voice consistency | 2 | One voice across headings, body, buttons and errors. Deduct for a playful hero above clinical form errors, or capitalisation that changes between components. |
| **N4** | Density and scannability | 1 | Sub-paragraphs kept short (roughly 25 words or fewer); no 20-row data table on a marketing page; content chunked so it can be skimmed. |

### 5.5 Double-counting guard

The same defect must not be charged twice. Where an issue could land in two places:

| Issue | Scores in | Not in |
|---|---|---|
| Microcopy quality | **N2** | Creativity, Usability |
| Target size (44×44pt) | **U2** | The WCAG checklist — it is not in 2.0 |
| Navigation consistency | **U3** (compliance itself in U1) | Both |
| Slop-checklist hits | **C1** | Design |
| Contrast failures | **U1** | D3 — colour choice may still be judged on its own merits |
| Missing dark mode | **D3** | Usability |

A single artefact can legitimately fail an SC in U1 *and* count as a slop hit in C1 — those are different claims about the same object. Charging the same claim twice is not.

---

## 6. Calibration — the anti-inflation rules

These exist because an unconstrained scorer drifts upward until every design scores in the high 80s and the number stops discriminating.

1. **3 is the default.** Every criterion starts at 3. Move off it only with cited evidence, in either direction.
2. **Any score of 4 or 5 requires a specific citation** — a layer name, a hex value, a measurement, a copy string. No citation means the score returns to 3.
3. **A score of 5 additionally requires a sentence explaining what makes it exceptional rather than merely correct.** Correct is a 3 or 4. Expect no more than about 10% of criteria to reach 5 on real work.
4. **A section cannot exceed 85% of its weight if any sub-criterion within it scores 2 or lower.** A serious weakness caps the section it sits in.
5. **Whole numbers only. Never round a section total up.**
6. **Expected distribution: competent professional work totals 62–74.** Strong work reaches the high 70s. If a first pass lands above 80, stop and re-audit every score of 4 and 5 before publishing — that result is more likely to be drift than excellence.
7. **Taste never compensates for compliance.** When a visually strong design fails AA, the verdict line says so explicitly.

**Bands:**

| Score | Verdict |
|---|---|
| 90–100 | Ship it |
| 80–89 | Minor polish |
| 70–79 | Needs work |
| 60–69 | Competent; revise |
| 45–59 | Major revision |
| Below 45 | Rethink |

---

## 7. Compute and cap

1. Sum the points from all four sections → **raw total**.
2. Apply the cap:
   - Any unresolved Level A or AA failure → **cap at 79**
   - Two or more distinct Level A failures → **cap at 69**
3. The final total is `min(raw, cap)`.
4. **Always show the cap when it bites**, with its cause:

```
Raw 86 → capped 79 (1.4.3 contrast failure: PricingCard/body-text at 3.9:1)
```

Never quietly report the capped number as though it were the raw score. The gap between the two is the most useful figure in the report — it is exactly what the design stands to gain by fixing its accessibility.

---

## 8. The report

Keep prose under roughly 400 words. Tables do not count toward that — they carry the evidence, and compressing them costs more than it saves.

**1. Design Read**
```
Design Read: marketing/landing for SMB finance buyers; expected variance high, density low. (inferred)
```

**2. Verdict** — one line, plus the cap line and the taste-vs-compliance sentence when they apply.
```
68/100 — needs work. Raw 74 → capped 69 (two Level A failures: 3.3.2, 1.4.1).
Visually the strongest work in this file; it is also the least accessible.
```

**3. Header** — target, input type, confidence, date.

**4. Section table**

| Section | Weight | Earned |
|---|---|---|
| Design | 40 | 29 |
| Usability | 30 | 14 |
| Creativity | 20 | 13 |
| Content | 10 | 6 |
| **Raw** | **100** | **62** |

**5. Per-criterion table** — id, score /5, points, and one line of cited evidence each.

**6. WCAG 2.0 AA checklist** — SC, level, `pass` / `fail` / `risk` / `not assessed` / `N/A`, and the offending layer on any failure. Mark genuinely inapplicable criteria `N/A`; **do not pad the table with N/As** to make coverage look broader than it was.

**7. Contrast measurements**

| Sample | Foreground | Background | Ratio | Required | Verdict |
|---|---|---|---|---|---|
| `Hero/subhead` | `#8A8A8E` | `#FFFFFF` | 3.43:1 | 4.5:1 | **fail** |
| `Nav/link` | `#1A1C1E` | `#FFFFFF` | 17.09:1 | 4.5:1 | pass |

**8. Slop checklist** — hits only, each cited, with the resulting C1 ceiling stated.

**9. Top fixes** — ranked by point impact. Each names the exact frame, layer and change, with the gain and the criterion it moves:
```
1. PricingFrame/cta-label: raise fill to #1A1C1E for 17.09:1 on #FFFFFF  (+4 pts, U1; lifts the 79 cap)
2. SignupForm/email-input: add a persistent label above the field, replacing placeholder-as-label  (+2 pts, U1/3.3.2)
3. Features/*: replace the three equal cards with a weighted layout  (+2 pts, C1)
```

**10. JSON block** — **only when asked.** Do not emit it by default.

---

## 9. Writing the scorecard back into Figma

**Ask before writing anything.** Modifying the user's file is a side-effectful action and is never assumed, however routine it looks. Report first, then offer.

On approval:

- Place an **"ADS Scorecard"** frame offset to the right of the evaluated frames, or on a new page named `ADS`.
- Optionally attach findings beside the offending layers, as annotations or a numbered callout matching the fix list.
- **Never modify the evaluated layers themselves.** Not to demonstrate a fix, not to correct a contrast value, not to tidy a stray hex. A scorer that edits its subject destroys the record of what was scored.
- Include the raw total, the cap, the cause and the date in the scorecard frame, so a screenshot of it is self-explanatory later.

For the Claude-side path: the `figma-use` skill is a mandatory prerequisite before any `use_figma` call. Load it first.

---

## Appendix A — Opt-in house-style checks (OFF by default)

These are one studio's house style, not measures of design quality. Applying them by default would grade a designer's work against someone else's taste, so they are quarantined here and **have no effect on the score unless the user explicitly asks for them**.

Enable with: *"score with house style"* / *"include house-style checks"*.

When enabled, report them as a separate list with their own count. They still do not alter the 100-point total unless the user asks for them to be scored — in which case apply them as C1 slop hits.

- **Dashes** — no em-dash (`—`) or en-dash (`–`) as a separator in any visible string: headlines, eyebrows, pills, body, quotes, buttons, captions, alt text.
- **Display serifs** — Fraunces and Instrument_Serif not used as the default display serif; any serif choice justified.
- **Premium-consumer palette** — not the default beige-and-brass family, i.e. backgrounds `#f5f1ea` `#f7f5f1` `#fbf8f1` `#efeae0` `#ece6db`, accents `#b08947` `#b6553a` `#9a2436` `#9c6e2a`, text `#1a1714` `#1a1814`.
- **Banned copy patterns** — "Quietly in use at" / "Quietly trusted by"; poetic section labels ("From the field", "Field notes", "On our desks"); generic step labels ("Stage 1 / Stage 2", "Phase 01"); section-number eyebrows ("00 / INDEX", "001 · Capabilities"); version labels in a hero (V0.6, BETA) outside a launch brief; version footers on marketing pages.
- **Decoration** — no scroll cues; no decorative status dots; no pills or labels overlaid on images; no photo-credit captions used as ornament; no locale/time/weather strips outside a travel or distributed-studio brief.

---

## Appendix B — Quick reference

**Order of operations**
1. Pick the target (selection → page) and state input confidence
2. Print the Design Read
3. Gather evidence
4. Run the WCAG 2.0 AA checklist — **binary before scalar**
5. Score the 19 sub-criteria, default 3, citations required above 3
6. Sum → apply cap → band
7. Report; then *ask* before writing back to Figma

**Weights at a glance**

```
Design 40   D1 9 · D2 8 · D3 8 · D4 8 · D5 4 · D6 3
Usability 30   U1 12 · U2 6 · U3 5 · U4 4 · U5 3
Creativity 20   C1 8 · C2 6 · C3 4 · C4 2
Content 10   N1 4 · N2 3 · N3 2 · N4 1
```

**The numbers that matter most**

| Thing | Value |
|---|---|
| Normal text contrast | 4.5:1 |
| Large text contrast | 3:1 (18pt / 14pt bold ≈ 24px / 18.66px bold) |
| Contrast self-check | `#767676` on white = 4.54:1 pass · `#777777` = 4.47:1 fail |
| Placeholder text | **Not exempt** from 4.5:1 |
| Disabled components | Exempt |
| Cap: any A or AA failure | 79 |
| Cap: 2+ Level A failures | 69 |
| Target size (U2, not WCAG 2.0) | 44×44pt |
| Body measure | ~45–75 characters |
| Type styles per screen | More than 4 is a flag |
| Expected total, competent work | 62–74 |

**Three things that are easy to get wrong**
- 4.1.3, 1.4.11, 1.4.10, 1.4.12 and target size are **WCAG 2.1/2.2**, not 2.0 AA. Keep them in the advisory.
- Disabled text is **exempt** from 1.4.3; placeholder text is **not**.
- 2.1.1, 2.1.2, 3.1.1 and 4.1.2 can be flagged as risks from a design but **cannot be certified as passes**.
