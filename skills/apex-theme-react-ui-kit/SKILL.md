---
name: apex-theme-react-ui-kit
description: "Restyle an Oracle APEX app to look like the Setproduct React UI kit (Blueprint) (data-dense Blueprint.js-style desktop UI: tight spacing, 3px radii, inset borders) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the React UI kit (Blueprint) theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog."
---

# Setproduct React UI kit (Blueprint) -> Oracle APEX

**Category:** Dashboard  |  **Kit:** https://www.setproduct.com/templates/react-ui-kit  |  **Modes:** light, dark (default light)

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to React UI kit (Blueprint).

## The look
- Built on Blueprint.js styling: compact controls, 3-4px radii, subtle inset borders.
- Neutral greys with Blueprint blue/green/orange/red intents.
- Optimised for complex, data-dense desktop tools (tables, trees, toolbars).

**Fonts:** body `Inter`, headings `Inter` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
- `theme-light.css` - light mode; create the Theme Style from **Vita** (default)
- `theme-dark.css` - dark mode; create the Theme Style from **Vita - Dark**

Each file is self-contained (font import + `--sp-*` tokens + base bridge + React UI kit (Blueprint) signature rules).

## Key tokens (light)
| Token | Value |
|---|---|
| `--sp-primary` | `#2D72D2` |
| `--sp-accent` | `#7961DB` |
| `--sp-success` | `#238551` |
| `--sp-warning` | `#C87619` |
| `--sp-danger` | `#CD4246` |
| `--sp-info` | `#2D72D2` |
| `--sp-bg` | `#F6F7F9` |
| `--sp-surface` | `#FFFFFF` |
| `--sp-border` | `#DCE0E5` |
| `--sp-text` | `#1C2127` |
| `--sp-text-muted` | `#5F6B7C` |
| `--sp-nav-bg` | `#FFFFFF` |
| `--sp-nav-active-bg` | `rgba(45,114,210,.12)` |
| `--sp-radius-md` | `3px` |
| `--sp-radius-lg` | `4px` |
| `--sp-btn-radius` | `3px` |

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
| Dense tables | Interactive Grid; Template Options on the region: `Remove Body Padding`; IG attributes: Fixed Row Height |
| Tree / file explorer | Tree region (native, uses --a-treeview-* vars) |
| Toolbars + button groups | Buttons in Region `Edit`/`Next` positions; Button Template Options `Button Set = Inner/First/Last` |
| Callouts | Alert region template, Template Options `Alert Type` + `Horizontal` |
| Segmented tabs | Radio Group item with Template Option `Display as Pill Button` |

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): none - the base layer covers this kit

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
function( options ) {
    options.styleDefaults = options.styleDefaults || {};
    options.styleDefaults.colors = [ "#2D72D2", "#238551", "#C87619", "#CD4246", "#7961DB", "#147EB3", "#D1980B", "#D13913" ];
    return options;
}
```

## Dark / light
Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch from the runtime *Customize* dialog (see `references/install.md` step 3).

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at https://www.setproduct.com/templates/react-ui-kit and nudge tokens, not selectors.
