# APEX Setproduct Themes

Claude Code skills that make an **Oracle APEX** app look like one of the [Setproduct](https://www.setproduct.com/all)
UI kits, while staying on **native Universal Theme 42** components.

- One skill per kit (`skills/apex-theme-<kit>/`) with a ready-to-upload CSS file per light/dark mode,
  the kit's tokens, a kit-pattern -> native-component recipe table and a chart palette.
- One router skill (`skills/apex-setproduct-themes/`) with the shared method, install guide,
  full component map and the verified Universal Theme variable list.
- A generator (`build.py`) so every theme comes from one data file (`src/themes.py`) and one bridge
  stylesheet (`src/base.css`).
- A swatch gallery at `docs/index.html` (works as GitHub Pages).

## How it works
```
src/themes.py  --tokens-->  --sp-* variables
src/base.css   --maps-->    --ut-* / --a-* Universal Theme variables (verified on APEX 24.1/24.2)
                            + side-menu selector overrides (Vita hard-codes those)
                            + optional sp-* utility classes per kit
build.py       --writes-->  skills/apex-theme-<kit>/theme-<mode>.css + SKILL.md
```
In APEX you upload one CSS file, save a Theme Style from **Vita** / **Vita - Dark** that references it,
and build pages with stock regions, template components and Template Options.

## Themes
<!-- THEMES:START -->
| Theme | Category | Modes | Look |
|---|---|---|---|
| [Eclipse](skills/apex-theme-eclipse/SKILL.md) | Dashboard | dark, light | dark-first data dashboard: near-black canvas, electric violet and cyan, gradient KPI cards |
| [Panda](skills/apex-theme-panda/SKILL.md) | Dashboard | light, dark | clean modern web-app dashboard: white cards, dark navy sidebar, confident blue |
| [Rome](skills/apex-theme-rome/SKILL.md) | Dashboard | light | airy light dashboard: periwinkle blue, peach and pink accents, soft tinted shadows |
| [Neolex](skills/apex-theme-neolex/SKILL.md) | Dashboard | light, dark | 8dp-grid responsive dashboard: bright azure, orange and purple accents, crisp light greys |
| [React UI kit (Blueprint)](skills/apex-theme-react-ui-kit/SKILL.md) | Dashboard | light, dark | data-dense Blueprint.js-style desktop UI: tight spacing, 3px radii, inset borders |
| [Xela](skills/apex-theme-xela/SKILL.md) | Dashboard | light, dark | cross-platform (React/Swift/Android/Flutter) system: royal blue, crisp white, easy dark toggle |
| [Material You](skills/apex-theme-material-you/SKILL.md) | Material | light, dark | Material Design 3 with Tailwind palette and Readex Pro: tonal surfaces, pill buttons |
| [Material X](skills/apex-theme-material-x/SKILL.md) | Material | light | Material beyond Material: Manrope type, deep indigo + teal, top-notch rounded shapes |
| [Material Design System](skills/apex-theme-material/SKILL.md) | Material | light, dark | classic Material Design (material.io): Roboto + Red Hat Display, elevation shadows, 4px radii |
| [Nocra](skills/apex-theme-nocra/SKILL.md) | AI product | dark, light | AI-product design system: deep midnight navy, mint CTAs, prompt inputs, thinking-state motion |
| [Orion](skills/apex-theme-orion/SKILL.md) | Data visualization | dark, light | space-themed dataviz: deep indigo night, neon violet/cyan, glowing maps, hexagons and bubbles |
| [Figma Charts](skills/apex-theme-charts/SKILL.md) | Data visualization | light, dark | component-driven chart library: pastel-bright violet/blue/mint/peach series on clean white cards |
| [Hyper Charts](skills/apex-theme-hyper-charts/SKILL.md) | Data visualization | light, dark | 1000+ chart blocks: indigo and fresh green on lavender-tinted cards, rounded and airy |
| [Nucleus UI](skills/apex-theme-nucleus/SKILL.md) | Mobile | light, dark | 1000+ component mobile system: vivid violet, sunshine-yellow highlights, rounded friendly UI |
| [Mobile X](skills/apex-theme-mobile-x/SKILL.md) | Mobile | light, dark | iOS/Android cross-platform kit: clear blue, lime highlight, 8dp grid, toggleable dark variants |
| [Appka iOS](skills/apex-theme-appka-ios/SKILL.md) | Mobile | light, dark | Apple-spec iOS system: grouped inset lists, SF-style type, system blue-violet, true-black dark |
| [Android UI kit](skills/apex-theme-android/SKILL.md) | Mobile | light | Android app templates: indigo-blue, amber accents, Roboto, elevation cards |
| [Zeus](skills/apex-theme-zeus/SKILL.md) | Landing pages | light | landing-page system: teal + violet on white, dark hero bands, pill CTAs, 630+ web blocks |
| [Figma Landing Pages](skills/apex-theme-landing/SKILL.md) | Landing pages | light | colourful, trendy landing blocks: violet, sunshine yellow, mint on bright colour-block sections |
| [Figma Website templates](skills/apex-theme-website/SKILL.md) | Landing pages | light, dark | 140+ dark & light website blocks: trustworthy blue, coral accent, mixable light/dark sections |
| [Claylo](skills/apex-theme-claylo/SKILL.md) | Landing pages | light | claymorphism: warm cream canvas, puffy pastel clay cards, chunky 3D push buttons, Fredoka |
| [Levitate](skills/apex-theme-levitate/SKILL.md) | Landing pages | dark | 3D scene presentation style: jet-black stage, neon sky/green/violet, glassy floating panels |
<!-- THEMES:END -->

## Install the skills (Claude Code)
Windows:
```powershell
./install.ps1
```
macOS / Linux:
```bash
./install.sh
```
Both copy `skills/*` into `~/.claude/skills/`. Then ask Claude, for example:
"apply the Panda theme to app 127" or "which Setproduct look suits an analytics app?".

## Apply a theme by hand (no Claude)
1. Upload `skills/apex-theme-<kit>/theme-<mode>.css` to **Static Application Files** (`setproduct/<kit>-<mode>.css`).
2. Theme Roller: pick **Vita** (light) or **Vita - Dark** (dark), **Save As** a new style.
3. Shared Components > Themes > Theme Styles > your style: **CSS File URLs** = `#APP_FILES#setproduct/<kit>-<mode>.css`, **Is Current**.
4. Build pages with native components - see the kit's SKILL.md recipe table.

Full guide: [`skills/apex-setproduct-themes/references/install.md`](skills/apex-setproduct-themes/references/install.md).

## Edit or add themes
```bash
python build.py
```
Change tokens in `src/themes.py` or the bridge in `src/base.css`, rebuild, re-upload. Adding a kit:
[`references/new-theme.md`](skills/apex-setproduct-themes/references/new-theme.md).

## Notes
- Colours are approximations sampled from Setproduct's public preview images; fonts come from the kit
  descriptions where stated. This repo contains **no Setproduct assets**. For exact values, buy the kit
  and copy its tokens into `src/themes.py`.
- Setproduct and the kit names are trademarks of their owners; this project is unaffiliated.
- Requires browsers with CSS `color-mix()` (all evergreen browsers since 2023).
