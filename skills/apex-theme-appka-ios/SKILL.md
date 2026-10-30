---
name: apex-theme-appka-ios
description: "Restyle an Oracle APEX app to look like the Setproduct Appka iOS kit (Apple-spec iOS system: grouped inset lists, SF-style type, system blue-violet, true-black dark) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the Appka iOS theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct Appka iOS -> Oracle APEX

**Category:** Mobile  |  **Kit:** https://www.setproduct.com/templates/appka-ios-ui-kit  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to Appka iOS.

## The look
- Apple HIG: grouped inset lists on #F2F2F7, hairline separators, 10-14px radii.
- System-font stack (SF Pro where available), blue-violet tint, true-black dark mode.
- 4100+ variants for 28 components, 280+ layouts across 14 categories.

**Fonts:** body `-apple-system, BlinkMacSystemFont, "SF Pro Text", Inter`, headings `-apple-system, BlinkMacSystemFont, "SF Pro Display", Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + Appka iOS signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#4444E4` |
| `--sp-accent` | `#FCC444` |
| `--sp-success` | `#34C759` |
| `--sp-warning` | `#FF9500` |
| `--sp-danger` | `#EC042C` |
| `--sp-info` | `#7474EC` |
| `--sp-bg` | `#F2F2F7` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#E5E5EA` |
| `--sp-text` | `#000000` |
| `--sp-text-muted` | `#8E8E93` |
| `--sp-nav-bg` | `#F2F2F7` |
| `--sp-nav-active-bg` | `#FFFFFF` |
| `--sp-radius-md` | `10px` |
| `--sp-radius-lg` | `14px` |
| `--sp-btn-radius` | `12px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Grouped inset table view | Content Row template component or Classic Report (Template = Standard) + region CSS class `sp-inset-group` |
| Segmented control | Radio Group, Template Option `Display as Pill Button` |
| Action sheet | Inline Drawer region or Modal Dialog (Drawer page template) |
| Switches | Switch item (native) - green ON via --sp-success |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): `sp-inset-group`

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#4444E4", "#FCC444", "#34C759", "#FF9500", "#EC042C", "#7474EC", "#5AC8FA", "#AF52DE" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/appka-ios-ui-kit and nudge tokens, not selectors.
