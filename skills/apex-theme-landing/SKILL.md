---
name: apex-theme-landing
description: Restyle an Oracle APEX app to look like the Setproduct Figma Landing Pages kit (colourful, trendy landing blocks: violet, sunshine yellow, mint on bright colour-block sections) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Figma Landing Pages theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct Figma Landing Pages -> Oracle APEX

**Category:** Landing pages  |  **Kit:** https://www.setproduct.com/templates/landing  |  **Modes:** light (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Figma Landing Pages.

## The look
- Bold colour-block sections (violet, sunshine yellow, mint) with white cards on top.
- Chunky headings, rounded 12-20px cards, tag-style labels.

**Fonts:** body `Poppins`, headings `Poppins` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Figma Landing Pages signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#6C5CE4` |
| `--sp-accent` | `#FCCC6C` |
| `--sp-success` | `#04B494` |
| `--sp-warning` | `#FCCC6C` |
| `--sp-danger` | `#F0506E` |
| `--sp-info` | `#54ECC4` |
| `--sp-bg` | `#FFFFFF` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#ECEAF7` |
| `--sp-text` | `#1E1A33` |
| `--sp-text-muted` | `#6D6887` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#EEEBFD` |
| `--sp-radius-md` | `12px` |
| `--sp-radius-lg` | `20px` |
| `--sp-btn-radius` | `10px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Colour-block sections | Static Content regions with CSS class `sp-block-violet` / `sp-block-yellow` / `sp-block-mint` |
| Hero | Hero region template |
| Feature tiles | Cards region (Layout = Grid) with Icon/Media slot |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): `sp-block-mint`, `sp-block-violet`, `sp-block-yellow`

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#6C5CE4", "#FCCC6C", "#04B494", "#54ECC4", "#A49CFC", "#F0506E", "#FCECAC", "#2B2340" ];
    return options;
}
```

## Dark / light
This kit is light-only; no second style is needed.

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/landing and nudge tokens, not selectors.
