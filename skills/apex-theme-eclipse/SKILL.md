---
name: apex-theme-eclipse
description: Restyle an Oracle APEX app to look like the Setproduct Eclipse kit (dark-first data dashboard: near-black canvas, electric violet and cyan, gradient KPI cards) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Eclipse theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct Eclipse -> Oracle APEX

**Category:** Dashboard  |  **Kit:** https://www.setproduct.com/templates/eclipse  |  **Modes:** dark, light (default dark)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Eclipse.

## The look
- Near-black canvas with slightly lifted navy panels; content floats on 12px-radius cards.
- Electric violet primary, cyan/green/red for data; gradient (violet to blue) hero KPI cards.
- Dense numeric typography: large tabular figures, small muted labels.

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark** (default)
- `theme-light.css` - light mode; create the Theme Style from **Vita**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Eclipse signature rules).

## Key tokens (dark)
| Token | Value |
|---|---|
| `--sp-primary` | `#5B2EF0` |
| `--sp-accent` | `#04BCF4` |
| `--sp-success` | `#14BC3C` |
| `--sp-warning` | `#F5A524` |
| `--sp-danger` | `#DC3434` |
| `--sp-info` | `#0B4CEC` |
| `--sp-bg` | `#08080F` |
| `--sp-surface` | `#12121C` |
| `--sp-border` | `#262638` |
| `--sp-text` | `#F4F4FA` |
| `--sp-text-muted` | `#9A9AB5` |
| `--sp-nav-bg` | `#0C0C14` |
| `--sp-nav-active-bg` | `#5B2EF0` |
| `--sp-radius-md` | `8px` |
| `--sp-radius-lg` | `14px` |
| `--sp-btn-radius` | `8px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Gradient KPI card | Cards region (or Static Content region, template Standard) + CSS class `sp-kpi-gradient` |
| Stat tiles row | Cards region, Layout = Grid, Grid Columns = 4; use the Badge/Icon slots for deltas |
| Line/area/wave charts | Chart region (JET), Line with Area; apply the chart palette init function |
| Transactions table | Classic Report (Template = Standard, Stretch) or Interactive Report |
| Bank card widget | Static Content region + CSS class `sp-kpi-gradient` with Display Image / Icon |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): `sp-kpi-gradient`, `sp-num`

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#5B2EF0", "#04BCF4", "#14BC3C", "#F5A524", "#DC3434", "#A78BFA", "#0B4CEC", "#F472B6" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/eclipse and nudge tokens, not selectors.
