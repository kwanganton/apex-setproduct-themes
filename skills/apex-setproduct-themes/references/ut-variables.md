# Universal Theme variables used by the bridge

Source: `Vita.min.css` and `Core.min.css` for APEX 24.1 and 24.2 from Oracle's CDN
(`https://static.oracle.com/cdn/apex/24.2.0/themes/theme_42/24.2/css/`). Vita defines ~860 custom
properties; the bridge (`assets/base.css`) sets the ones below from `--sp-*` tokens.

| Area | Variables |
|---|---|
| Type | `--a-base-font-family`, `--a-base-font-weight-semibold`, `--ut-alternate-heading-font-family`, `--ut-hero-region-title-font-family` |
| Palette | `--ut-palette-{primary,primary-alt,success,warning,danger,info}` + `-contrast`, `-shade`, `-text` |
| Links / focus | `--ut-link-text-color`, `--a-base-link-text-color`, `--ut-focus-outline-color` |
| Shape / depth | `--ut-border-radius{,-sm,-md,-lg}`, `--ut-shadow-{sm,md,lg}` |
| Shell | `--ut-body-{background,text}-color`, `--ut-body-title-*`, `--ut-header-{background-color,text-color,border-color,box-shadow}`, `--ut-body-nav-{background-color,text-color,border-color}`, `--ut-body-sidebar-background-color`, `--ut-footer-*` |
| Components | `--ut-component-{background-color,text-default-color,text-title-color,text-subtitle-color,text-muted-color,border-color,inner-border-color,border-radius,box-shadow,highlight-background-color,toolbar-background-color,icon-*,badge-*}` |
| Regions | `--ut-region-{background-color,text-color,header-background-color,header-text-color,header-border-color,box-shadow,border-width}` |
| Buttons | `--a-button-{border-radius,font-size,padding-y,padding-x}` (plus `-hover-*`, `-active-*`, `-focus-*` if needed) |
| Fields | `--a-field-input-{border-radius,background-color,border-color,text-color,focus-border-color,focus-background-color}`, `--ut-field-label-text-color`, `--a-checkbox-*`, `--a-switch-*`, `--a-chip-border-radius` |
| Cards | `--a-cv-{background-color,border-color,border-radius,shadow,hover-shadow,title-font-size,icon-*,initials-*,badge-border-radius}` |
| Reports | `--a-gv-{background-color,header-background-color,cell-border-color,header-cell-border-color,row-hover-background-color}`, `--ut-report-{header-background-color,cell-border-color,cell-hover-background-color,cell-alt-background-color}`, `--a-toolbar-*` |
| Menus / dates / tabs | `--a-menu-{background-color,border-color,border-radius}`, `--a-datepicker-*`, `--ut-tabs-item-*`, `--ut-navtabs-*` |
| Login / hero | `--ut-login-page-background-color`, `--ut-login-region-{background-color,box-shadow}`, `--ut-hero-region-*` |
| AI chat (24.1+) | `--a-chat-user-{primary,secondary}-{message-background-color,text-color}` |

## Hard-coded in Vita (needs selectors)
The side menu (`.t-TreeNav .a-TreeView-*`) row/hover/selected colours are literal hex values in Vita and
Vita - Dark, so the bridge overrides them by selector. Everything else above is variable-driven.

## Inspecting your version
In the running app: DevTools > Elements > select `<html>` > Styles > filter `--ut-` or `--a-`. Or:

```javascript
[...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch { return []; } })
  .filter(r => r.selectorText === ':root')
  .flatMap(r => [...r.style]).filter(p => p.startsWith('--ut-') || p.startsWith('--a-')).sort();
```

Re-download the CDN CSS for another version by swapping `24.2.0`/`24.2` in the URL, then
`grep -o '\-\-[a-z][a-z0-9-]*:' Vita.min.css | sort -u`.
