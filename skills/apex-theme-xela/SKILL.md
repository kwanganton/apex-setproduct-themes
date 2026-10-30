---
name: apex-theme-xela
description: "Restyle an Oracle APEX app to look like the Setproduct Xela kit (cross-platform (React/Swift/Android/Flutter) system: royal blue, crisp white, easy dark toggle) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Xela theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Xela -> Oracle APEX

**Category:** Dashboard  |  **Kit:** https://www.setproduct.com/templates/xela-react  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Xela.

## The look
- Royal-blue primary on crisp white; soft blue-grey neutrals; peach accent.
- Rounded 10px controls, clear focus rings; built to swap dark and light with no hassle.
- Same kit ships for React, Swift, Android and Flutter; this theme covers the web look.

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Xela signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#3464FC` |
| `--sp-accent` | `#FC9C6C` |
| `--sp-success` | `#1DB98A` |
| `--sp-warning` | `#FFB020` |
| `--sp-danger` | `#F0445A` |
| `--sp-info` | `#043CEC` |
| `--sp-bg` | `#F4F6FB` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E5E9F2` |
| `--sp-text` | `#0E1A3B` |
| `--sp-text-muted` | `#6B7593` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#EBF0FF` |
| `--sp-radius-md` | `10px` |
| `--sp-radius-lg` | `16px` |
| `--sp-btn-radius` | `10px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Accordions | Collapsible region template, or Region Display Selector |
| Rating, sliders | Star Rating item (native); range = two Number Field items |
| Steppers | Wizard Progress list (Steps navigation) + Wizard Container region |
| Pagination | Report pagination; Classic Report Pagination Type = Row Ranges X to Y |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#3464FC", "#FC9C6C", "#1DB98A", "#94ACFC", "#FFB020", "#F0445A", "#5C84FC", "#C4D4FC" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/xela-react and nudge tokens, not selectors.
