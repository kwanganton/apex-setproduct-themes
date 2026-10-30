---
name: apex-theme-neolex
description: "Restyle an Oracle APEX app to look like the Setproduct Neolex kit (8dp-grid responsive dashboard: bright azure, orange and purple accents, crisp light greys) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Neolex theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Neolex -> Oracle APEX

**Category:** Dashboard  |  **Kit:** https://www.setproduct.com/templates/neolex-dashboard  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Neolex.

## The look
- Strict 8dp spacing rhythm; light grey canvas with white panels and thin borders.
- Bright azure primary; orange and purple used for charts and highlights.
- Shopping, CRM, tasks, planner, kanban, news and table layouts.

**Fonts:** body `Nunito Sans`, headings `Nunito Sans` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Neolex signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#047CFC` |
| `--sp-accent` | `#FC8C34` |
| `--sp-success` | `#22B07D` |
| `--sp-warning` | `#FC8C34` |
| `--sp-danger` | `#F0445A` |
| `--sp-info` | `#9C54E4` |
| `--sp-bg` | `#F4F4F4` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E4E4E4` |
| `--sp-text` | `#1F2430` |
| `--sp-text-muted` | `#6F7787` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#E6F2FF` |
| `--sp-radius-md` | `8px` |
| `--sp-radius-lg` | `8px` |
| `--sp-btn-radius` | `8px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Task / planner lists | Content Row template component with checkbox via Cards/Content Row actions |
| Shopping product grid | Cards region, Media Source = Image, Layout = Grid, 3-4 columns |
| Stats tiles | Cards region (Layout = Grid); or Badge template component for single numbers |
| News feed | Media List template component |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#047CFC", "#FC8C34", "#9C54E4", "#4CA4FC", "#22B07D", "#94C4FC", "#F0445A", "#FFC542" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/neolex-dashboard and nudge tokens, not selectors.
