---
name: apex-theme-charts
description: "Restyle an Oracle APEX app to look like the Setproduct Figma Charts kit (component-driven chart library: pastel-bright violet/blue/mint/peach series on clean white cards) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Figma Charts theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Figma Charts -> Oracle APEX

**Category:** Data visualization  |  **Kit:** https://www.setproduct.com/templates/charts  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Figma Charts.

## The look
- Clean white chart cards; violet, sky blue, mint and peach series with pastel fills.
- 150+ templates across desktop/tablet/mobile; every chart cloned into dark mode.

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Figma Charts signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#845CF4` |
| `--sp-accent` | `#54A4FC` |
| `--sp-success` | `#1CD4A4` |
| `--sp-warning` | `#FCBC7C` |
| `--sp-danger` | `#F87171` |
| `--sp-info` | `#54A4FC` |
| `--sp-bg` | `#F7F7FC` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#ECECF4` |
| `--sp-text` | `#2C2C34` |
| `--sp-text-muted` | `#7C7C8A` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#F1ECFE` |
| `--sp-radius-md` | `8px` |
| `--sp-radius-lg` | `12px` |
| `--sp-btn-radius` | `8px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Any of the 25+ chart types | Chart region (Oracle JET): bar, line, area, combo, pie/donut, funnel, pyramid, radar, polar, range, stock, gauge |
| Chart card with header metric | Chart region in Standard template; put the metric in Region Header via a Display Only item or the region's `Sub Title` |
| Infographic progress | Percent Graph / Status Meter Gauge chart |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#845CF4", "#54A4FC", "#1CD4A4", "#FCBC7C", "#F87171", "#CCBCFC", "#BCF4E4", "#FACC15" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/charts and nudge tokens, not selectors.
