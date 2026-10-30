# Installing a Setproduct theme in an APEX app

Works on APEX 22.2+ (variables verified on 24.1/24.2). Universal Theme 42 must be the app's theme and
should stay **subscribed** to the master - never copy templates to get a look.

## 1. Upload the CSS
Pick the file(s) from `skills/apex-theme-<slug>/`:

| File | Base Theme Style |
|---|---|
| `theme-light.css` | Vita |
| `theme-dark.css` | Vita - Dark |

Upload options, best first:
1. **Static Application Files** (Shared Components > Static Application Files > Create File). Use a folder:
   `setproduct/<slug>-<mode>.css`. Reference as `#APP_FILES#setproduct/<slug>-<mode>.css`. Exported with the app.
2. **Static Workspace Files** when several apps share one look. Reference as `#WORKSPACE_FILES#setproduct/<slug>-<mode>.css`.
3. **Theme Files** (Shared Components > Themes > Universal Theme 42 > Files) -> `#THEME_FILES#...` (not common).

Scripted alternative (SQLcl / deployment): `apex_application_install` + export with static files,
or create files in a dev workspace and promote by app export.

## 2. Create the Theme Style
1. Run the app > Developer Toolbar > **Customize > Theme Roller**.
2. Choose style **Vita** (for light) or **Vita - Dark** (for dark). Don't change colours.
3. **Save As** `Setproduct <Name> <Mode>`.
4. Builder: Shared Components > Themes > Universal Theme 42 > **Theme Styles** > open the new style.
5. **CSS File URLs**: `#APP_FILES#setproduct/<slug>-<mode>.css`
6. Set **Is Current = Yes** (and **Is Public = Yes** if users may switch).

Simplest alternative for a single-style app: Shared Components > User Interface Attributes >
**Cascading Style Sheets > File URLs** - but a Theme Style keeps light/dark switchable and travels with the theme.

## 3. Light + dark switching (themes with two modes)
- Create one Theme Style per file (step 2 twice), both **Is Public = Yes**.
- User Interface Attributes: enable **end users to choose the theme style**. Users switch in the runtime
  *Customize* dialog; the choice is stored per user.
- To follow the OS setting automatically you need a small Dynamic Action on page 0 that calls
  `apex.theme42.util` / reloads with the other style - only add it if the user asks; it isn't native.

## 4. Navigation and page templates
- Dashboard / mobile kits: User Interface Attributes > Navigation Menu > **Position = Side**, List Template
  **Side Navigation Menu**. Template Options: *Collapsed by default* for mobile kits.
- Landing kits: **Position = Top** (Top Navigation Menu / Tabs) or none; public pages use page template
  **Minimal (No Navigation)** and **Hero** regions.
- Login page: page template **Login**; the CSS styles `.t-Login-region` and the login background.

## 5. Fonts and CSP
Each CSS file starts with a Google Fonts `@import`. If the app (or the ORDS/web server) sends a
Content-Security-Policy that blocks `fonts.googleapis.com` / `fonts.gstatic.com`:
1. Download the `.woff2` files, upload to Static Application Files (`setproduct/fonts/...`).
2. Replace the `@import` line with `@font-face` rules pointing at `#APP_FILES#setproduct/fonts/...`
   (APEX substitutes `#APP_FILES#` only in builder fields, so put the `@font-face` block in the Theme Style's
   **Custom CSS** in Theme Roller, or use relative URLs inside the uploaded CSS: `url(fonts/inter.woff2)`).

## 6. Charts
JET charts don't read CSS variables for series colours. Paste the theme's function into
**Chart region > Attributes > Advanced > Initialization JavaScript Function**. For many charts, put the
function in a static JS file once (e.g. `window.spChart = function(o){...}`) and set each chart's init to
`function(o){ return spChart(o); }`.

## 7. Tweaking
- Change a few colours for one app: Theme Roller > that style > **Custom CSS**:
  `:root { --sp-primary: #0F766E; --sp-radius-lg: 10px; }`
- Change a theme everywhere: edit `src/themes.py`, run `python build.py`, re-upload the CSS.

## Troubleshooting
| Symptom | Cause / fix |
|---|---|
| Nothing changed | Style not current, or file URL typo. DevTools > Network: is the CSS 200? |
| Some colours still Vita | Theme Roller pickers were used on this style - reset style and Save As again, or move values to `--sp-*` |
| Side menu still dark grey | Vita hard-codes TreeNav colours; the theme overrides them by selector. Check no app-level CSS re-overrides `.t-TreeNav` |
| Dark text on dark background | A light file on a *Vita - Dark* style (or vice versa). Match file to base style |
| Fonts fallback to system | CSP blocks Google Fonts - self-host (step 5) |
| `color-mix()` not applied | Very old browser (pre-2023). Replace defaults in `build.py` with hex values |
