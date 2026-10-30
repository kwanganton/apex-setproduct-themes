# Adding a new theme

For another Setproduct kit, a new release, or any design (Dribbble shot, brand guide, Figma file).

1. **Collect the look** from the kit page or files: background, surface, border, text, muted text,
   primary, accent, success/warning/danger/info, nav colours, radii (small/medium/large/button/field),
   shadow style, body and heading fonts (must be on Google Fonts, or self-host), 8 chart colours.
   - From a kit page, sampling preview images is quick: draw each image to a canvas and bucket pixels; the
     most frequent saturated colours are the accents, the most frequent neutrals are bg/surface/text.
   - From Figma: copy the colour/text styles; prefer the kit's tokens over sampling.
2. **Add an entry** to `THEMES` in `src/themes.py` (copy the closest existing theme). Required tokens per
   mode: `primary`, `accent`, `bg`, `surface`, `border`, `text`, `text-muted` (in `base` or the mode).
   Shadow presets: `soft`, `flat`, `tinted`, `elevated`, `dark`, `glow`, `clay`.
3. **Recipes**: list the kit's signature patterns and the native APEX component for each
   (see `component-map.md`). Only add `signature` CSS for things variables can't do, and expose it as
   `sp-*` utility classes rather than global overrides where possible.
4. Run `python build.py` - it writes `skills/apex-theme-<slug>/`, updates both theme tables and the gallery.
5. Run `install.ps1` (or `install.sh`) to copy the skills into `~/.claude/skills`.
6. Test in an app with the checklist in the generated SKILL.md, in both modes.
