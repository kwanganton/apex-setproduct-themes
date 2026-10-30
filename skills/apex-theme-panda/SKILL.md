---
name: apex-theme-panda
description: Restyle an Oracle APEX app to look like the Setproduct Panda kit (clean modern web-app dashboard: white cards, dark navy sidebar, confident blue) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Panda theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct Panda -> Oracle APEX

**Category:** Dashboard  |  **Kit:** https://www.setproduct.com/templates/panda  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Panda.

## The look
- White content cards on a cool light-grey canvas; dark navy side navigation.
- Confident blue primary with green/yellow accents for statuses.
- Kanban, calendar, invoice, profile and data-table patterns; 1920px layouts.

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Panda signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#3C84F4` |
| `--sp-accent` | `#24C45C` |
| `--sp-success` | `#24C45C` |
| `--sp-warning` | `#ECB40C` |
| `--sp-danger` | `#F04438` |
| `--sp-info` | `#2C5C9C` |
| `--sp-bg` | `#F5F7FB` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E6EAF0` |
| `--sp-text` | `#0C141C` |
| `--sp-text-muted` | `#6B7785` |
| `--sp-nav-bg` | `#0C141C` |
| `--sp-nav-active-bg` | `rgba(60,132,244,.22)` |
| `--sp-radius-md` | `8px` |
| `--sp-radius-lg` | `12px` |
| `--sp-btn-radius` | `8px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Kanban board | one Cards region per status laid side by side (Layout Column Span 3 each), cards ordered by priority; drag-and-drop needs a plug-in |
| Calendar | Calendar region (native); colours follow --ut-palette-* |
| Invoice / checkout | Form region (Template = Standard) + Classic Report (Template = Value Attribute Pairs - Row) |
| Profile widget | Avatar + Content Row template components |
| Data tables | Interactive Grid / Interactive Report |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#3C84F4", "#24C45C", "#ECB40C", "#F04438", "#6C9CF4", "#2C5C9C", "#9B8AFB", "#14B8A6" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/panda and nudge tokens, not selectors.
