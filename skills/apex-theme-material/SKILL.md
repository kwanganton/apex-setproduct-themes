---
name: apex-theme-material
description: "Restyle an Oracle APEX app to look like the Setproduct Material Design System kit (classic Material Design (material.io): Roboto + Red Hat Display, elevation shadows, 4px radii) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Material Design System theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Material Design System -> Oracle APEX

**Category:** Material  |  **Kit:** https://www.setproduct.com/templates/material  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Material Design System.

## The look
- 100% material.io guidelines: elevation shadows, 4px radii, uppercase text buttons.
- Roboto body with Red Hat Display headings.
- Light and dark themes per the Material dark-theme spec (#121212 surfaces).

**Fonts:** body `Roboto`, headings `Red Hat Display` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Material Design System signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#3D7FF0` |
| `--sp-accent` | `#FC7C2C` |
| `--sp-success` | `#34A853` |
| `--sp-warning` | `#FBBC05` |
| `--sp-danger` | `#EA4335` |
| `--sp-info` | `#3D7FF0` |
| `--sp-bg` | `#F5F5F5` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E0E0E0` |
| `--sp-text` | `#212121` |
| `--sp-text-muted` | `#757575` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `rgba(61,127,240,.12)` |
| `--sp-radius-md` | `4px` |
| `--sp-radius-lg` | `8px` |
| `--sp-btn-radius` | `4px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| App bar | Header = coloured (header-bg token = primary) |
| Text / contained / outlined buttons | Button templates Text (Hot = contained), Template Options `Style = Simple` = outlined, `Style = Remove UI Decoration` = text |
| Snackbar | apex.message.showPageSuccess() (native success message) - styled by palette |
| FAB | Icon button + CSS class `sp-fab` |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): `sp-fab`

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#3D7FF0", "#EA4335", "#FBBC05", "#34A853", "#FC7C2C", "#AB47BC", "#00ACC1", "#94B4EC" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/material and nudge tokens, not selectors.
