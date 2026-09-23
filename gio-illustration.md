# GIO Illustration Style

A reusable guide for producing clean, friendly GIO illustrations with enough detail to feel considered while remaining simple and immediately readable.

## Visual references

### Coffee shop

![Front-facing GIO-style coffee shop storefront](gio-illustrations/assets/gio-coffee-shop-storefront.png)

### Armchair and standing lamp

![GIO-style armchair with standing lamp](gio-illustrations/assets/gio-armchair-standing-lamp.png)

## Style summary

Create crisp flat-vector illustrations from rounded geometric shapes, using GIO blue as the dominant colour, pale blue for secondary surfaces, white for breathing room and a restrained GIO red accent. Subjects should be complete, comfortably padded and easy to recognise, with a little practical detail but no texture or visual clutter.

## Visual system

### Shape and finish

- Use clean, solid, opaque vector-like fills with crisp edges.
- Build objects from simple rounded geometry and gently softened corners.
- Add enough definition to explain construction: seams, panels, window frames, handles, shelves and a few recognisable accessories.
- Keep the result slightly more detailed than an icon, but much simpler than an editorial scene.
- Avoid outlines where overlapping colour blocks can define the form.
- Do not use grain, noise, speckling, paper texture, a sandpaper effect, a grey wash or distressed edges.
- Do not use photorealism, 3D materials, bevels, glossy highlights or realistic shadows.

### Composition

- Show the entire subject. Nothing important may touch or cross the canvas edge.
- Keep generous clear space around the artwork, with at least 10–15% padding on every side.
- Use a clean white background by default.
- Keep the visual weight centred and balanced.
- Use a straight-on front view for buildings, rooms and storefronts unless another view is explicitly requested.
- Use a simple front or gentle three-quarter view for freestanding objects.
- Do not use isometric perspective unless explicitly requested.
- Start every new brief as a fresh composition; do not carry over objects from a previous illustration.

### Colour palette

| Role | Colour | Hex |
| --- | --- | --- |
| Dominant structure | GIO blue | `#005296` |
| Dark definition | Deep GIO blue | `#014A73` |
| Mid-tone variation | Sky blue | `#B1C6DF` |
| Secondary surfaces | Pale blue | `#D6E5EF` |
| Light surfaces | Light blue | `#F0F5F9` |
| Background and highlights | White | `#FFFFFF` |
| Small accent only | GIO red | `#E3001B` |

Use blue, pale blue and white for most of the image. Red should be a small point of emphasis rather than a large colour field. Avoid unrelated greens, browns, yellows, purples and greys.

## Subject guidance

### Objects and interiors

- Preserve a strong, recognisable primary silhouette.
- Add three to six useful identity details rather than decorative micro-detail.
- Let adjacent blue values and overlap create depth.
- Keep furniture soft and welcoming through rounded cushions and broad, simple forms.
- Use only a subtle flat grounding shape when the object needs visual weight.

### Architecture and storefronts

- Use a front-facing elevation with clean verticals and horizontals.
- Show the complete facade, roofline or awning, entrance and base.
- Add a small number of readable interior cues through the windows.
- Use signage as a simple pictogram or abstract brand-free symbol.
- Do not generate words, logos, addresses or pseudo-lettering.

### People

- Use simplified, elongated proportions and an expressive pose.
- Include minimal friendly facial features when a face is visible: small eyes, a simple nose or mouth and uncomplicated hair shapes.
- Keep features subtle so the figure remains part of the same flat visual system.
- Use clean colour blocks for clothing and anatomy, with no realistic skin texture or shading.
- Vary pose and posture between illustrations rather than reusing the same figure.

## Master prompt

```text
Create one original GIO-style flat-vector illustration of [SUBJECT].

Use clean solid geometric shapes, softly rounded corners and crisp edges. Use GIO blue
#005296 as the dominant colour, deep blue #014A73 for definition, pale blues #B1C6DF,
#D6E5EF and #F0F5F9 for secondary surfaces, pure white #FFFFFF for the background and
highlights, and GIO red #E3001B only as a small accent. Add a modest amount of useful
detail so the subject feels considered and recognisable without becoming busy.

Show the complete subject with generous 10–15% clear space on every side. Keep the
composition centred and balanced. Use a straight-on front view for architecture and a
front or gentle three-quarter view for individual objects. Use a clean white background.

No text, logos or pseudo-lettering. No cropping, isometric view, photorealism, 3D,
gradients, glossy lighting, bevels, realistic shadows, noise, grain, speckles, paper
texture, sandpaper effect, grey wash, haze or distressed edges. Do not reuse objects or
motifs from earlier illustration requests unless they are explicitly requested.
```

## Example subject briefs

### Coffee shop

```text
A complete front-facing neighbourhood coffee-shop storefront. Include a blue structural
frame, striped awning, large pale-blue display windows and a centred entrance. Through
the windows, show only a few simplified cues: an espresso machine, stacked cups and a
small bistro table with chairs. Use a simple cup-and-steam pictogram as the sign. Keep the
whole facade fully inside the frame with comfortable white space around it.
```

### Armchair and standing lamp

```text
A welcoming upholstered armchair beside a slender standing lamp. Use broad rounded
cushions, visible arms, short feet, one small scatter cushion and a simple curved lamp
shade. Add restrained seam details and overlapping blue shapes for depth. Keep both
objects complete and fully inside the frame on a pure white background.
```

## Negative prompt

```text
cropped subject, cut-off object, edge collision, isometric scene, side-view building,
photorealism, 3D render, gradients, bevels, glossy materials, realistic lighting,
heavy shadows, blur, noise, grain, speckling, stippling, paper texture, sandpaper effect,
grey wash, haze, faded colour, distressed edges, clutter, excessive detail, thin line art,
unrelated props from earlier scenes, text, letters, numbers, logo, watermark
```

## Quality checklist

- [ ] The entire subject is visible with generous padding.
- [ ] The chosen view is appropriate and architecture is front-facing.
- [ ] GIO blue is dominant and red is only a small accent.
- [ ] The background is clean white unless another background was requested.
- [ ] Details improve recognition without creating clutter.
- [ ] People, when used, have subtle facial features and a distinct pose.
- [ ] Fills are crisp, solid and free of texture, noise or grey wash.
- [ ] There is no accidental text, logo, watermark or pseudo-lettering.
- [ ] No visual elements have leaked in from a previous request.

