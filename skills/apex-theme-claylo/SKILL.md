---
name: apex-theme-claylo
description: Restyle an Oracle APEX app to look like the Setproduct Claylo kit (claymorphism: warm cream canvas, puffy pastel clay cards, chunky 3D push buttons, Fredoka) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Claylo theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct Claylo -> Oracle APEX

**Category:** Landing pages  |  **Kit:** https://www.setproduct.com/templates/claylo  |  **Modes:** light (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Claylo.

## The look
- Claymorphism: soft, puffy surfaces with inner highlights and offset drop shadows.
- Warm cream canvas; pastel mint, lavender, butter and tangerine; brown ink text.
- Fredoka display + Plus Jakarta Sans body; chunky pill buttons that 'press' down.

**Fonts:** body `Plus Jakarta Sans`, headings `Fredoka` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Claylo signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#F49444` |
| `--sp-accent` | `#ACE4C4` |
| `--sp-success` | `#3FAF7A` |
| `--sp-warning` | `#F4DC84` |
| `--sp-danger` | `#E8604C` |
| `--sp-info` | `#C4BCF4` |
| `--sp-bg` | `#FCF4EC` |
| `--sp-surface` | `#FFFDF9` |
| `--sp-border` | `#F0DCC8` |
| `--sp-text` | `#4A2A1C` |
| `--sp-text-muted` | `#8C6B5C` |
| `--sp-nav-bg` | `#FCF4EC` |
| `--sp-nav-active-bg` | `#FFE2C4` |
| `--sp-radius-md` | `20px` |
| `--sp-radius-lg` | `32px` |
| `--sp-btn-radius` | `999px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Clay cards | Cards / Static Content regions; colour variants with CSS class `sp-clay-mint`, `sp-clay-lavender`, `sp-clay-butter` |
| Chunky CTA | Button, Hot, Template Option `Large` - press effect is automatic |
| Icon tiles linked by dashes | Cards region, Icon slot, Layout Grid 3; CSS class `sp-dashed-links` on the region |
| Testimonials with stars | Cards region + Star Rating item (read-only) or `fa-star` icons |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): `sp-clay-butter`, `sp-clay-lavender`, `sp-clay-mint`, `sp-dashed-links`

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#F49444", "#ACE4C4", "#C4BCF4", "#F4DC84", "#E8604C", "#74341C", "#3FAF7A", "#ECCCB4" ];
    return options;
}
```

## Dark / light
This kit is light-only; no second style is needed.

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/claylo and nudge tokens, not selectors.
