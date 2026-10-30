---
name: apex-setproduct-themes
description: Catalog and shared method for making an Oracle APEX app look like a Setproduct (setproduct.com) UI kit - Eclipse, Panda, Rome, Neolex, Xela, Material You, Material X, Material, Nocra, Orion, Charts, Hyper Charts, Nucleus, Mobile X, Appka iOS, Android, Zeus, Landing, Website, Claylo, Levitate, React UI kit. Native Universal Theme components restyled with a drop-in CSS file and Theme Style. Use when the user wants to theme/restyle/reskin an APEX app, match a Setproduct kit, or asks which look to use.
---

# Setproduct kits -> Oracle APEX (native-first)

Every theme here keeps the app on **Universal Theme 42** with stock templates, Template Options and
template components. The kit's look comes from one CSS file per mode that maps `--sp-*` design tokens onto
Universal Theme's own CSS variables (verified against APEX 24.1/24.2), plus a few selector overrides where
Vita hard-codes colours (side menu) and optional utility classes you add through *CSS Classes*.

## Pick a theme
<!-- THEMES:START -->
| Theme | Category | Modes | Look |
|---|---|---|---|
| [Eclipse](../apex-theme-eclipse/SKILL.md) | Dashboard | dark, light | dark-first data dashboard: near-black canvas, electric violet and cyan, gradient KPI cards |
| [Panda](../apex-theme-panda/SKILL.md) | Dashboard | light, dark | clean modern web-app dashboard: white cards, dark navy sidebar, confident blue |
| [Rome](../apex-theme-rome/SKILL.md) | Dashboard | light | airy light dashboard: periwinkle blue, peach and pink accents, soft tinted shadows |
| [Neolex](../apex-theme-neolex/SKILL.md) | Dashboard | light, dark | 8dp-grid responsive dashboard: bright azure, orange and purple accents, crisp light greys |
| [React UI kit (Blueprint)](../apex-theme-react-ui-kit/SKILL.md) | Dashboard | light, dark | data-dense Blueprint.js-style desktop UI: tight spacing, 3px radii, inset borders |
| [Xela](../apex-theme-xela/SKILL.md) | Dashboard | light, dark | cross-platform (React/Swift/Android/Flutter) system: royal blue, crisp white, easy dark toggle |
| [Material You](../apex-theme-material-you/SKILL.md) | Material | light, dark | Material Design 3 with Tailwind palette and Readex Pro: tonal surfaces, pill buttons |
| [Material X](../apex-theme-material-x/SKILL.md) | Material | light | Material beyond Material: Manrope type, deep indigo + teal, top-notch rounded shapes |
| [Material Design System](../apex-theme-material/SKILL.md) | Material | light, dark | classic Material Design (material.io): Roboto + Red Hat Display, elevation shadows, 4px radii |
| [Nocra](../apex-theme-nocra/SKILL.md) | AI product | dark, light | AI-product design system: deep midnight navy, mint CTAs, prompt inputs, thinking-state motion |
| [Orion](../apex-theme-orion/SKILL.md) | Data visualization | dark, light | space-themed dataviz: deep indigo night, neon violet/cyan, glowing maps, hexagons and bubbles |
| [Figma Charts](../apex-theme-charts/SKILL.md) | Data visualization | light, dark | component-driven chart library: pastel-bright violet/blue/mint/peach series on clean white cards |
| [Hyper Charts](../apex-theme-hyper-charts/SKILL.md) | Data visualization | light, dark | 1000+ chart blocks: indigo and fresh green on lavender-tinted cards, rounded and airy |
| [Nucleus UI](../apex-theme-nucleus/SKILL.md) | Mobile | light, dark | 1000+ component mobile system: vivid violet, sunshine-yellow highlights, rounded friendly UI |
| [Mobile X](../apex-theme-mobile-x/SKILL.md) | Mobile | light, dark | iOS/Android cross-platform kit: clear blue, lime highlight, 8dp grid, toggleable dark variants |
| [Appka iOS](../apex-theme-appka-ios/SKILL.md) | Mobile | light, dark | Apple-spec iOS system: grouped inset lists, SF-style type, system blue-violet, true-black dark |
| [Android UI kit](../apex-theme-android/SKILL.md) | Mobile | light | Android app templates: indigo-blue, amber accents, Roboto, elevation cards |
| [Zeus](../apex-theme-zeus/SKILL.md) | Landing pages | light | landing-page system: teal + violet on white, dark hero bands, pill CTAs, 630+ web blocks |
| [Figma Landing Pages](../apex-theme-landing/SKILL.md) | Landing pages | light | colourful, trendy landing blocks: violet, sunshine yellow, mint on bright colour-block sections |
| [Figma Website templates](../apex-theme-website/SKILL.md) | Landing pages | light, dark | 140+ dark & light website blocks: trustworthy blue, coral accent, mixable light/dark sections |
| [Claylo](../apex-theme-claylo/SKILL.md) | Landing pages | light | claymorphism: warm cream canvas, puffy pastel clay cards, chunky 3D push buttons, Fredoka |
| [Levitate](../apex-theme-levitate/SKILL.md) | Landing pages | dark | 3D scene presentation style: jet-black stage, neon sky/green/violet, glassy floating panels |
<!-- THEMES:END -->

Quick picks: internal dashboards -> Panda, Eclipse (dark) or Neolex; data-dense admin tools -> React UI kit;
analytics/BI -> Orion, Charts, Hyper Charts; AI features -> Nocra; Material shops -> Material You;
mobile/PWA -> Appka iOS, Nucleus, Mobile X; public marketing pages -> Zeus, Website, Claylo.

## Native-first rules (follow in this order)
1. **Theme Style variables** - the generated CSS sets `--ut-*` / `--a-*` variables; most of the look comes from these.
2. **Template Options and templates** - choose the right stock template (Cards, Content Row, Badge, Avatar,
   Media List, Timeline, Hero, Collapsible, Tabs Container, Inline Drawer, Login) before writing CSS.
3. **Utility CSS classes** - each theme ships a few `sp-*` classes; add them in *Appearance > CSS Classes*.
4. **Selector overrides** - only where Vita hard-codes values (side menu). Never copy/edit theme templates;
   never subscribe-break the theme. Never use jQuery UI widgets or plug-ins just for looks.
5. When native truly can't do it (drag-and-drop kanban, hexagon grids), say so and offer a declarative
   **template component plug-in** before custom JavaScript.

## Apply a theme (summary - full steps in `references/install.md`)
1. Copy `apex-theme-<slug>/theme-<mode>.css` to **Shared Components > Static Application Files** (e.g. `setproduct/eclipse-dark.css`).
2. Theme Roller: start from **Vita** (light file) or **Vita - Dark** (dark file), **Save As** `Setproduct <Name> <Mode>`.
3. Shared Components > Themes > Universal Theme > **Theme Styles** > that style: put
   `#APP_FILES#setproduct/eclipse-dark.css` in its **CSS File URLs**; set **Is Current**.
4. Two modes? Repeat for the other file, make both **Is Public**, and enable end users to choose the theme style.
5. Navigation: User Interface Attributes > Navigation Menu = **Side** (dashboard kits) or **Top** (landing kits).
6. Charts: paste the theme's chart-palette Initialization JavaScript Function into each chart.
7. Verify with the checklist in the theme's SKILL.md.

Do not set colours with Theme Roller's pickers on a Setproduct style - they compete with the file. Tweak by
overriding `--sp-*` variables in Theme Roller's **Custom CSS** box instead.

## References
- `references/install.md` - step-by-step install, fonts/CSP, Workspace Files for many apps, troubleshooting load order
- `references/component-map.md` - kit pattern -> native APEX component + template options (all kits)
- `references/ut-variables.md` - the Universal Theme variables the bridge sets, and how to inspect more
- `references/new-theme.md` - add another Setproduct kit (or any design) as a new theme skill
- `assets/base.css` - the shared bridge layer (already inlined into every theme file)

## Honesty notes
- Tokens are approximations sampled from public preview images on setproduct.com, not the licensed Figma
  files. For pixel-exact work, buy the kit and copy real values into `src/themes.py`.
- Do not ship kit illustrations, icons or 3D assets in an app unless the user owns a licence.
- All 131 variables the bridge sets exist in APEX 24.2 and 26.2 Vita/Core CSS. Panda (light) and Eclipse (dark)
  were rendered on Oracle's live Universal Theme reference app (APEX 26.2, Vita / Vita - Dark): shell, side
  menu, regions and Interactive Report all pick up the tokens. Other themes share the same bridge but were only
  checked in the swatch gallery (`docs/index.html`).
- Variables were verified against APEX 24.1/24.2/26.2 Vita. On older versions (22.x/23.x), check names in DevTools
  (`references/ut-variables.md`) - a missing variable is silently ignored, so nothing breaks, it just doesn't apply.
