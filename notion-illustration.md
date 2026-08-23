# Monochrome Hand-Drawn Icon Style Guide

Reference: [Ultimate Notion Icons by Vectorly Space](https://dribbble.com/shots/23073767-Ultimate-Notion-Icons)

This guide describes the collection's broad visual principles so an image model can create new, original icons with a compatible look. Use the reference for art direction, not to reproduce any existing icon exactly.

## One-sentence style summary

Minimal black-and-white spot illustrations that combine slightly imperfect hand-drawn outlines, simple geometric construction, selective solid-black fills, playful perspective, and a small grounding shadow on a clean white background.

## Visual DNA

### Colour

- Strict monochrome: pure black artwork on pure white or transparent background.
- No greys, colour accents, gradients, lighting effects, or texture overlays.
- Black is used in two ways: as an outline and as one or two bold filled shapes.
- Aim for roughly 15–30% black coverage. Most of the image should remain white.

### Line quality

- Use confident, medium-to-bold black outlines.
- Lines should feel hand-drawn rather than mechanically perfect.
- Allow subtle variation in curvature, angle, and spacing, but keep the result clean.
- Prefer rounded joins and ends where possible.
- Do not use sketchy repeated strokes, pencil shading, cross-hatching, or distressed ink.
- Keep internal detail lines slightly lighter or visually quieter than the outer contour.
- At a 512 × 512 px canvas, a useful starting point is an outer stroke around 8–12 px and detail strokes around 5–8 px.

### Shapes and construction

- Reduce the subject to a few recognisable geometric masses.
- Use mildly exaggerated proportions so the object reads instantly at small size.
- Straight objects may be slightly skewed or bowed; circles may be a little irregular.
- Combine clean geometry with a friendly doodle-like finish.
- Avoid tiny realistic components. Retain only details that identify the subject.
- Objects can use a simple three-quarter view, shallow perspective, or a slight tilt.
- Perspective may be intentionally imperfect; visual charm is more important than technical precision.

### Black fills

- Add one dominant solid-black area to create weight and recognisability.
- Good locations include a side plane, rear plane, opening, screen, liquid, shadowed underside, or cast shadow.
- A smaller secondary black accent is acceptable, but avoid filling every enclosed shape.
- Keep large white areas inside the subject so it does not become a solid silhouette.

### Grounding and depth

- Most objects should have a small, simple grounding device:
  - an irregular black oval;
  - a flat black wedge;
  - a short horizontal baseline; or
  - a detached geometric cast shadow.
- The shadow is graphic, not realistic: hard-edged, flat, and fully black.
- Shadows may sit slightly off-centre to reinforce the playful perspective.
- Use overlap and a single dark side plane instead of realistic light and shade.

### Energy marks

- Add two to six short accent marks only when they improve the idea.
- Examples: motion lines, impact ticks, sparkle rays, steam curls, vibration arcs, or tiny dots.
- Marks should be asymmetrical, sparse, and placed near the active part of the object.
- They should communicate action, emphasis, heat, sound, movement, or success—not merely decorate empty space.

## Composition

- One main subject per icon.
- Centre the overall visual weight, while allowing the object itself to lean or point diagonally.
- Use a square canvas with generous white space.
- The subject should occupy about 55–70% of the canvas width and height.
- Keep a safe margin of at least 12–15% on every edge.
- Use a front or three-quarter angle; avoid dramatic camera angles.
- Build a compact, readable silhouette with no background scene.
- If several objects are necessary, overlap them into one unified cluster rather than scattering them.
- Do not add borders, rounded-square containers, labels, or captions unless they are requested separately for a UI layout.

## Subject simplification recipe

Before writing a prompt, reduce the idea to four layers:

1. **Primary silhouette** — the largest, instantly recognisable shape.
2. **Identity details** — two to four features that distinguish the object.
3. **Black mass** — one filled area that adds contrast and depth.
4. **Gesture** — a tilt, overlap, motion mark, or grounding shadow that gives the icon personality.

For example, a watering can could be reduced to: rounded can body + top handle and long spout + black side plane + three droplets and a small floor shadow.

## Master prompt

Replace the bracketed text while keeping the rest of the prompt stable.

> Create one original monochrome spot icon of **[SUBJECT AND ACTION]**. Minimal black ink illustration on a pure white background, slightly imperfect hand-drawn vector outline, bold clean outer contour, sparse internal detail, simplified geometric construction, friendly playful proportions, subtle three-quarter perspective, one strong solid-black fill area, and a small hard-edged black grounding shadow. Add only **[2–5 RELEVANT MOTION OR EMPHASIS MARKS]** near the active part of the object. Compact centred silhouette, generous empty space, immediately readable at small size. No text, no border, no surrounding scene. Square composition, crisp high-resolution vector-like finish.

## Prompt formula

Use this order for consistent generations:

```text
[subject + action],
single monochrome spot icon,
slightly imperfect hand-drawn black vector outline,
simplified geometric forms and playful proportions,
one bold solid-black side plane or accent,
small flat black grounding shadow,
sparse purposeful motion marks,
centred compact silhouette with generous white space,
pure white or transparent background,
crisp, minimal, readable at 32 px,
no text, no border, no scene
```

## Example prompts

### AI assistant icon

> Create one original monochrome spot icon of a small friendly desktop robot organising three floating note cards. Minimal black ink illustration on a pure white background, slightly imperfect hand-drawn vector outline, bold clean outer contour, sparse internal detail, simplified geometric forms, and playful proportions. Show the robot in a subtle three-quarter view. Fill one side of its body and one card overlap in solid black. Add a small irregular black oval shadow below and four short motion ticks around the moving cards. Compact centred silhouette, generous white space, instantly readable at small size. No words, letters, logo, border, interface, background scene, grey, colour, gradient, or realistic shading.

### Cloud backup icon

> Create one original monochrome spot icon of a cloud lifting a document upward. Use confident, slightly uneven hand-drawn black outlines with rounded joins, simple geometric construction, and very few internal lines. The cloud stays mostly white; use a solid-black upward arrow and a small black shadow wedge beneath the document. Add three short upward motion lines. Square canvas, centred compact composition, generous empty white space, crisp vector-like finish, no text, no border, no extra objects, no colour, no gradient, no 3D rendering.

### Focus timer icon

> Create one original monochrome spot icon of a round kitchen timer with a small sprouting leaf, suggesting focused work and healthy time management. Draw it with a bold, slightly imperfect black vector contour, playful proportions, sparse dial marks, and a gentle three-quarter tilt. Use a solid-black side plane and a short black grounding shadow. Add two tiny vibration arcs near the bell. Keep the silhouette compact and centred on pure white, readable at 32 px. No typography, border, scene, grey tones, soft shadow, gradients, photorealism, or excessive detail.

## Negative prompt

Use this as a reusable negative prompt when the model supports one:

```text
colour, grey, gradients, soft shadows, realistic lighting, photorealism,
3D render, glossy plastic, clay style, isometric scene, detailed background,
multiple disconnected subjects, complex composition, thin technical line art,
perfect CAD geometry, ruler-straight sterile lines, rough pencil sketch,
charcoal, cross-hatching, stippling, distressed texture, halftone,
heavy black silhouette, excessive fill, tiny details, ornamental decoration,
thick comic-book inking, kawaii face unless requested, text, letters,
numbers, caption, watermark, logo, border, badge, app-icon container,
cropped object, off-canvas elements
```

## Consistency rules for a full icon set

Lock these choices before generating a batch:

- Canvas: 1:1 square.
- Background: pure white or transparent.
- Subject scale: approximately 60–65% of canvas.
- View: front or mild three-quarter perspective.
- Outer stroke: one consistent weight across the set.
- Detail stroke: about 65–75% of outer-stroke weight.
- Corner character: mostly rounded, never sharp everywhere.
- Black mass: one dominant filled area per icon.
- Grounding: choose either oval/wedge shadows or short baselines and use that system consistently.
- Energy marks: maximum six; omit them for static ideas.
- Detail budget: two to four identifying features per subject.
- Tone: smart, practical, optimistic, and lightly playful—not childish.

When using a model with seed or reference controls, keep the same seed, aspect ratio, reference strength, and style prompt for the entire batch. Change only the subject/action phrase.

## Batch prompt template

```text
Generate a coherent set of [NUMBER] separate icons. Each icon contains one
[SUBJECT LIST] rendered with the exact same visual system: black and white only,
slightly imperfect hand-drawn vector contours, consistent medium-bold outer
stroke, sparse internal detail, simplified playful geometry, one solid-black
accent plane, and one small hard-edged grounding shadow. Use a mild front or
three-quarter view, a compact centred silhouette, and generous white space.
Keep every icon equally scaled and readable at 32 px. Do not combine the icons
into scenes. No text, borders, gradients, grey, colour, realistic shading, or 3D.
```

For production work, generating each icon separately usually gives more consistent cropping and cleaner editable assets than asking for a large contact sheet.

## Quality-control checklist

An icon belongs in the set only if all of these are true:

- [ ] The subject is recognisable at 32–48 px.
- [ ] The silhouette is compact and not cropped.
- [ ] The image contains only black and white pixels, except anti-aliasing at edges.
- [ ] The outer contour feels bold and slightly human, not mechanically perfect.
- [ ] Internal detail is sparse and supports recognition.
- [ ] There is one clear solid-black area rather than many unrelated black patches.
- [ ] The shadow is flat and graphic, not blurred or realistic.
- [ ] Perspective is simple and does not distort the subject beyond recognition.
- [ ] Accent lines explain action or emphasis.
- [ ] There is no accidental text, pseudo-lettering, watermark, or logo.
- [ ] White space and subject scale match the rest of the set.
- [ ] The icon still works when converted to a one-colour SVG.

## Common failure modes and corrections

| Failure | Correction to add to the next prompt |
| --- | --- |
| Looks too polished or corporate | “slightly irregular hand-drawn contour; subtle human variation in curves and angles” |
| Looks messy or sketchy | “single clean contour per edge; no repeated sketch strokes; crisp vector-like finish” |
| Looks like generic thin line art | “medium-bold outer outline; one large solid-black accent plane; strong graphic contrast” |
| Looks like a heavy silhouette | “mostly white interior; black fill limited to one side plane and the small cast shadow” |
| Looks flat or static | “mild three-quarter tilt; one overlapping plane; three purposeful motion ticks” |
| Looks like a 3D render | “flat black ink shapes only; no realistic lighting, material, gradient, bevel, or soft shadow” |
| Too much background | “isolated single subject; pure white background; no room, landscape, interface, or decorative props” |
| Inconsistent within a set | Repeat the same complete style block and change only the subject phrase |
| Unusable at small size | “maximum four identifying details; simplified compact silhouette; readable at 32 px” |

## Suggested generation workflow

1. Generate four variations of one representative subject.
2. Choose the version with the best silhouette and black/white balance.
3. Use that chosen image as the visual reference for every later icon.
4. Keep the master prompt unchanged and swap only the subject/action.
5. Regenerate outliers instead of accepting inconsistent line weight or scale.
6. Remove the white background if transparent assets are needed.
7. Vectorise only after the full raster set is visually consistent.
8. Clean the vector paths, unify stroke widths, and manually correct malformed details.
9. Test every icon at 32, 48, 64, and 128 px before export.

## Export targets

- Master canvas: 1024 × 1024 px or larger.
- Working background: white for generation; transparent after cleanup if required.
- Raster: PNG or WebP at 1×, 2×, and 4×.
- Vector: SVG with expanded strokes when cross-application consistency matters.
- Keep each icon optically centred rather than relying only on mathematical bounds.
- Preserve a consistent viewBox and padding across the entire set.

## Short prompt for tools with limited prompt length

> Original black-and-white hand-drawn vector spot icon of **[SUBJECT]**: bold slightly irregular outline, simplified playful geometry, sparse detail, one solid-black accent plane, small flat black grounding shadow, a few purposeful motion ticks, compact centred silhouette, generous white space, readable at 32 px. No text, border, colour, grey, gradients, realistic shading, 3D, background scene, or cropping.
