# GIO Promo Film Style

A reusable guide for short product films that show off a website or design system: one continuous camera, soft "morning fog" light, typography that moves with the music, and UI that feels touchable. Written from a 45-second, 1080p60 launch film for the GIO website redesign.

## Style in one sentence

One unbroken camera glides into a single detail, lets it become the next scene, and pulls back to reveal the whole, all in soft fogged light, with text that arrives grey and fills in on the beat.

## References

- **Zeller POS launch:** pacing, frosted product surfaces.
- **Tesla "Model Y in 60 seconds":** one macro detail and one small caption per beat.
- **Zeller App:** word-by-word text animation.
- **Feel:** Apple and Tesla product films: calm, confident, nothing shouting.

## Core principles

### 1. Every transition is a continuous shot

- **No cuts, no dissolves, no wipes.** Each scene hands over to the next through the camera.
- **Two moves only:**
  - **Zoom in** to an element until it fills the frame and *becomes* the next scene. Examples: the "O" in the logo turns into white fog; the counter of a letter "a" opens onto the next typeface; a slider thumb swells into a colour card; that colour *is* the "Get a quote" button.
  - **Focus on one part of the UI, then pull back** to reveal the page, the device, then every page.
- **Plan the hand-off object first.** Each scene must end on something that can grow into the next one.
- **Fixed focal point on zooms.** Zoom geometrically (interpolate the log of the frame width), and move the centre in proportion to the width change. A linear centre with a geometric zoom drifts off the subject.

### 2. Rhythm: one feature every 3–5 seconds

- Cut the film to the music's phrase, not to the second: at 124 bpm, an 8-beat loop is about 3.9 s, and each feature gets one loop.
- Land camera moves, word reveals and number counts on beats. Keep a beat grid (`B(n) = phase + n × 60/bpm`) and time everything in beats.
- Use the track's structure:
  - Silent beats are for the biggest zoom-through.
  - A breakdown is for slow anticipation, such as a cursor drifting to a button.
  - The drop is for the click that pulls the camera back.
- **Open fast.** The first 5 seconds must already be moving, with no slow fade-up.

### 3. Morning fog light

- **Background:** a pale blue-white field with a large, soft, warm radial glow (peach to GIO orange `#eb5c25` at low alpha) rising from one corner, plus a white bloom.
- **Surfaces:** frosted glass, i.e. a white linear gradient at 72→42% alpha, `backdrop-filter: blur(36px) saturate(1.5)` and a hairline inner highlight.
- **Progressive blur** at screen edges: four stacked layers (2, 6, 14, 30 px) with offset gradient masks, so focus falls off smoothly.
- **Entrances come out of fog**, not out of nothing: opacity 0→1, y +34→0, blur 24→0 px, expo-out, about 1.1 s. Exits go back into fog: blur up, drift up, ease in-out, about 0.65 s.
- **No drop shadows on flat graphic content** such as colour palettes and type specimens. Depth comes from blur and scale, not shadow. Device frames may keep a soft ambient shadow.

### 4. Typography

- **Figtree everywhere possible:** captions, UI, numbers and display lines.
- **Serif (Newsreader) only upright.** Never italic, in any weight.
- **Display:** Figtree 400–500, tight tracking (−0.02 to −0.035 em), line height about 1.06.
- **Labels and eyebrows:** Figtree 600, 15–21 px at 1080p, uppercase, tracking +0.12 to +0.16 em, slate `#64748b`.
- **Small HUD captions** name the feature on screen in two to four words, in a frosted pill. They fog in from above and leave before the next feature.
- **Weight as motion:** variable-weight specimens can sweep 300→900 to show a type family's range.

### 5. Text that animates

- **Word-by-word reveal:** each word fogs in (y +22→0, blur 12→0, expo, about 0.8 s), staggered 0.10–0.16 s. It arrives grey (`#94a3b8`), a blue highlight passes through it (`#3b82f6`), and it settles on its final colour (`#020617`; key words end on brand blue `#2563eb`). On dark backgrounds use grey `#8da2c0` → light blue `#93c5fd` → white.
- **Odometer numbers:** ratings and counts roll vertically, digit by digit, following a continuous value with quint-out easing. Examples: 0.0 → 4.6/5, 1,000 → 2,516 reviews. Higher digits only roll when the lower one wraps.
- **Slot reveal for codes:** characters such as hex values scroll through a few random glyphs and land, staggered about 0.05 s.
- **Star ratings** pop in one by one with a slight overshoot (back-out easing).

### 6. Camera and easing

| Use | Easing |
|---|---|
| Entrances, word reveals | expo-out |
| Camera moves between frames | cubic in-out; quint-out for the "click pulls back" move |
| Slow drift while holding a shot | linear scale 1.00 → 1.03–1.05 over the hold, so the frame never freezes |
| Long page scrolls | quintic in-out |
| Things that land (cards, stars, illustrations) | back-out (overshoot about 1.4) |
| Zoom-through exits | cubic-in, with blur 0 → 26 px |

- **Device moments:** give device frames a gentle 3D tilt (rotateX 3–4°, rotateY ±9°) when they enter, then settle flat. Add a slow float while held.
- **Show, don't list:** use the real pages. Hero, hover and press states, a click, scrolling into a comparison table, desktop and phone navigating together.
- **Multi-page shots show only the top of each page** (header and hero), never mid-page or the footer.

### 7. Colour

| Role | Value |
|---|---|
| Ink | `#020617`, `#0f172a` |
| Brand blue / accent blue | `#2563eb` / `#3b82f6` |
| Light blue (on dark) | `#93c5fd` |
| Slate text and labels | `#64748b`, `#475569`, `#94a3b8` |
| Warm accent (sparingly) | GIO orange `#eb5c25`, `#f5763a`; tag pill `#ffe3d1` on `#ad3210` |
| Fog / paper | `#f8fafc`, `#e2e8f0` |

Keep orange to one or two moments: the sunrise glow, a "Most popular" tag. Blue carries the film.

### 8. Illustration

Brand illustrations use the [GIO Marshmallow style](gio-illustration.md). In film, an illustration can lift off a card on the page, be joined by friends that arrive with back-out easing, and form a carousel around it before the camera moves on.

### 9. Sound

- **Music** drives the edit. Pick a track with a clear 8-beat loop, a breakdown and a drop.
- **Whooshes are sparse:** about one per major camera move. Thirteen in 45 s was the upper limit ("slightly more, don't overdo it"). Pitch-shift them slightly so repeats don't sound identical, and keep them 20–27 dB under the music.
- **One distinct sound per action, fired by the real animation event:**
  - **Stars:** one rising, glassy note per star, on the 16th-note grid.
  - **Counters:** woody ticks on actual digit changes, slowing as the number settles, then a two-note chime on landing.
  - **Click:** a short, crisp click on the drop.
  - **Arrivals:** a soft pop.
- **Musical sounds stay in key.** Synthesised notes use only notes from the track's key (for a track in G: G, A, D). Use sound-effect generation only for textures: whoosh, click, pop, riser.
- **Level each effect against the music**, measuring each raw file's RMS or peak. Generated clips vary widely in loudness.

### 10. Structure of the 45-second film

| Beats | Scene | Hand-off |
|---|---|---|
| 0–8 | Real footage (city in fog) with a white display question; the logo assembles | Dive into the white "O"; it becomes fog |
| 8–16 | Typography: Figtree specimen, weight sweep, Newsreader specimen | Zoom through the counter of the "a"; the slider thumb swells |
| 16–24 | Colour: one colour card, then the full ramps | Dive into the brand blue |
| 24–64 | One camera over real pages: hero button, hover and click (drop at 32), page pull-back, reviews counting, desktop and phone, comparison table | Race down into the illustration on a card |
| 64–72 | Illustration lifts off the page; friends arrive; carousel forms | Pull back |
| 72–85 | A gently tilted wall of page heads drifting in alternate rows; brand line reveals word by word | Fade to white |
| 85+ | Logo assembles; a single closing line | End: nothing under it, no credits |

## Production technique

- **Build the film as one HTML page** with a deterministic timeline: every property is a pure function of `t`, exposed as `seek(t)`. There are no CSS transitions and no requestAnimationFrame-driven state.
- **Render frame by frame** in headless Chrome over the DevTools protocol (JPEG q97). Run several instances in parallel, then encode with ffmpeg (libx264, CRF 15) and mix the audio separately.
- **Render twice and diff.** Chrome occasionally drops a raster tile, about 1 frame in 1000. Re-render the frames that differ and arbitrate with a third pass.
- **Text stutters under slow transforms**, because Chrome snaps baselines to whole pixels. Fix this with `will-change: transform` on the moving text and its animated children. Switch it off around big zooms, or the layer keeps its old raster scale and goes blurry.
- **`filter` on a child of a `background-clip: text` parent** makes the text vanish.
- **Odometers:** don't vertically centre the digit strip with flex `align-items: center`; it shifts by half its height.
- **For macro shots**, export UI from Figma at 4×. Exports cap at 16384 px.

## Checklist

- [ ] Every scene ends on an object that becomes the next scene (no cuts or dissolves).
- [ ] One feature per 3–5 s, and the key moves land on beats.
- [ ] Entrances fog in (blur + drift); nothing pops from nothing except deliberate overshoots.
- [ ] Figtree first; serif upright only; no italics anywhere.
- [ ] Text reveals word by word (grey → highlight → final); numbers roll.
- [ ] No drop shadows on flat graphics.
- [ ] Page montages show only the header and hero.
- [ ] Whooshes are sparse, each action has its own sound, and musical sounds stay in key.
- [ ] Ends on a single brand line with nothing under it.
