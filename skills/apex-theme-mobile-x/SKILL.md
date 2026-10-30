---
name: apex-theme-mobile-x
description: "Restyle an Oracle APEX app to look like the Setproduct Mobile X kit (iOS/Android cross-platform kit: clear blue, lime highlight, 8dp grid, toggleable dark variants) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Mobile X theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Mobile X -> Oracle APEX

**Category:** Mobile  |  **Kit:** https://www.setproduct.com/templates/mobile-x  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Mobile X.

## The look
- Clear blue primary with a lime-green highlight and blush-pink tags.
- iOS specs adopted to the Android 8dp grid; every component has a dark variant.

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Mobile X signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#4474FC` |
| `--sp-accent` | `#B4EC5C` |
| `--sp-success` | `#3DBE6B` |
| `--sp-warning` | `#FFB020` |
| `--sp-danger` | `#FF5C5C` |
| `--sp-info` | `#3454AC` |
| `--sp-bg` | `#F5F6FA` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E5E7EF` |
| `--sp-text` | `#121726` |
| `--sp-text-muted` | `#6A7186` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `#E8EEFF` |
| `--sp-radius-md` | `10px` |
| `--sp-radius-lg` | `16px` |
| `--sp-btn-radius` | `10px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| App bars | Header + Breadcrumb Bar region; Back button = Button with `t-Button--noUI` icon |
| Sheets | Inline Drawer region |
| PIN / register inputs | Text Field items with Template `Optional - Floating` |
| Settings toggles | Switch item; group with Content Row |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#4474FC", "#B4EC5C", "#FCC4C4", "#3454AC", "#8CACFC", "#FF5C5C", "#FFB020", "#24346C" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/mobile-x and nudge tokens, not selectors.
