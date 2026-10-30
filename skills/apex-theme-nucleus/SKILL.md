---
name: apex-theme-nucleus
description: Restyle an Oracle APEX app to look like the Setproduct Nucleus UI kit (1000+ component mobile system: vivid violet, sunshine-yellow highlights, rounded friendly UI) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Nucleus UI theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct Nucleus UI -> Oracle APEX

**Category:** Mobile  |  **Kit:** https://www.setproduct.com/templates/nucleus-ui  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Nucleus UI.

## The look
- Vivid violet primary with sunshine-yellow highlight chips; deep indigo for dark surfaces.
- Friendly rounded components (16px+) and large touch targets; 500+ mobile screens.
- Sector themes: events, food delivery, healthcare, finance, travel, NFT, e-commerce.

**Fonts:** body `Poppins`, headings `Poppins` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Nucleus UI signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#7454FC` |
| `--sp-accent` | `#FCDC4C` |
| `--sp-success` | `#22C55E` |
| `--sp-warning` | `#FCDC4C` |
| `--sp-danger` | `#F43F5E` |
| `--sp-info` | `#2414AC` |
| `--sp-bg` | `#F7F6FF` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#ECE9FB` |
| `--sp-text` | `#1A1433` |
| `--sp-text-muted` | `#7B7596` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#EFEAFF` |
| `--sp-radius-md` | `14px` |
| `--sp-radius-lg` | `22px` |
| `--sp-btn-radius` | `14px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Mobile app shell | Enable Progressive Web App (Shared Components > PWA) + page template `Standard`; Navigation Menu = Side Menu collapsed by default, or Top Navigation Tabs |
| List screens | Content Row / Media List template components |
| Bottom sheets | Inline Drawer region (native) or Modal Dialog with `Drawer` page template |
| Big CTA button | Button Template Options `Stretch` + `Large`, Hot |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#7454FC", "#FCDC4C", "#2414AC", "#22C55E", "#F43F5E", "#9CBCEC", "#CCC4FC", "#FB923C" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/nucleus-ui and nudge tokens, not selectors.
