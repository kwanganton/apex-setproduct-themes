"""Source of truth for every Setproduct kit -> APEX theme.

Tokens are approximations of each kit's public preview imagery on
setproduct.com (palette sampled from the product pages, fonts taken from the
kit descriptions where stated). They are a starting point, not the kit's
licensed design files. Edit here, then run `python build.py`.

Per theme:
  modes      first entry is the default mode; "dark" files sit on Vita - Dark
  base       tokens shared by every mode (palette, shape, fonts)
  light/dark per-mode tokens; any base token can be overridden per mode
  shadow     preset name per mode (see SHADOWS in build.py)
  recipes    kit element -> native APEX component (+ template options / CSS class)
  signature  extra CSS: utility classes you add via a region/button "CSS Classes"
"""

THEMES = [
    # ------------------------------------------------------------------ dashboards
    {
        "slug": "eclipse", "name": "Eclipse", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/eclipse",
        "summary": "dark-first data dashboard: near-black canvas, electric violet and cyan, gradient KPI cards",
        "look": [
            "Near-black canvas with slightly lifted navy panels; content floats on 12px-radius cards.",
            "Electric violet primary, cyan/green/red for data; gradient (violet to blue) hero KPI cards.",
            "Dense numeric typography: large tabular figures, small muted labels.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["dark", "light"],
        "base": {
            "primary": "#5B2EF0", "accent": "#04BCF4", "success": "#14BC3C", "warning": "#F5A524",
            "danger": "#DC3434", "info": "#0B4CEC",
            "radius-sm": "6px", "radius-md": "8px", "radius-lg": "14px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px", "nav-item-inset": "8px",
        },
        "dark": {"bg": "#08080F", "surface": "#12121C", "surface-2": "#1A1A28", "border": "#262638",
                 "text": "#F4F4FA", "text-muted": "#9A9AB5", "nav-bg": "#0C0C14", "header-bg": "#08080F",
                 "nav-text": "#B3B3CC", "nav-active-bg": "#5B2EF0", "nav-active-text": "#FFFFFF"},
        "light": {"bg": "#F4F4F8", "surface": "#FFFFFF", "surface-2": "#F7F7FB", "border": "#E4E4EE",
                  "text": "#14142B", "text-muted": "#6E6E8F", "nav-bg": "#14142B", "nav-text": "#B3B3CC",
                  "nav-active-bg": "#5B2EF0", "nav-active-text": "#FFFFFF", "nav-border": "#14142B"},
        "shadow": {"dark": "glow", "light": "soft"},
        "chart": ["#5B2EF0", "#04BCF4", "#14BC3C", "#F5A524", "#DC3434", "#A78BFA", "#0B4CEC", "#F472B6"],
        "recipes": [
            ("Gradient KPI card", "Cards region (or Static Content region, template Standard) + CSS class `sp-kpi-gradient`"),
            ("Stat tiles row", "Cards region, Layout = Grid, Grid Columns = 4; use the Badge/Icon slots for deltas"),
            ("Line/area/wave charts", "Chart region (JET), Line with Area; apply the chart palette init function"),
            ("Transactions table", "Classic Report (Template = Standard, Stretch) or Interactive Report"),
            ("Bank card widget", "Static Content region + CSS class `sp-kpi-gradient` with Display Image / Icon"),
        ],
        "signature": """
.sp-kpi-gradient { background: linear-gradient(135deg, var(--sp-primary) 0%, var(--sp-info) 100%) !important; color: #fff; border: 0 !important; }
.sp-kpi-gradient .t-Region-title, .sp-kpi-gradient .a-CardView-title, .sp-kpi-gradient .t-Region-body { color: #fff; }
.sp-num { font-variant-numeric: tabular-nums; font-weight: 700; font-size: 1.75rem; letter-spacing: -0.02em; }
""",
    },
    {
        "slug": "panda", "name": "Panda", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/panda",
        "summary": "clean modern web-app dashboard: white cards, dark navy sidebar, confident blue",
        "look": [
            "White content cards on a cool light-grey canvas; dark navy side navigation.",
            "Confident blue primary with green/yellow accents for statuses.",
            "Kanban, calendar, invoice, profile and data-table patterns; 1920px layouts.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#3C84F4", "accent": "#24C45C", "success": "#24C45C", "warning": "#ECB40C",
            "danger": "#F04438", "info": "#2C5C9C",
            "radius-sm": "6px", "radius-md": "8px", "radius-lg": "12px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px", "nav-item-inset": "10px",
        },
        "light": {"bg": "#F5F7FB", "surface": "#FFFFFF", "surface-2": "#F8FAFC", "border": "#E6EAF0",
                  "text": "#0C141C", "text-muted": "#6B7785", "nav-bg": "#0C141C", "nav-text": "#A9B4C2",
                  "nav-active-bg": "rgba(60,132,244,.22)", "nav-active-text": "#FFFFFF", "nav-border": "#0C141C",
                  "nav-hover-bg": "rgba(255,255,255,.06)"},
        "dark": {"bg": "#0C141C", "surface": "#131D28", "surface-2": "#1A2633", "border": "#24313F",
                 "text": "#EEF2F7", "text-muted": "#8A97A8", "nav-bg": "#09111A", "nav-text": "#A9B4C2",
                 "nav-active-bg": "rgba(60,132,244,.22)", "nav-active-text": "#FFFFFF", "header-bg": "#0C141C",
                 "nav-hover-bg": "rgba(255,255,255,.05)"},
        "shadow": {"light": "soft", "dark": "dark"},
        "chart": ["#3C84F4", "#24C45C", "#ECB40C", "#F04438", "#6C9CF4", "#2C5C9C", "#9B8AFB", "#14B8A6"],
        "recipes": [
            ("Kanban board", "one Cards region per status laid side by side (Layout Column Span 3 each), cards ordered by priority; drag-and-drop needs a plug-in"),
            ("Calendar", "Calendar region (native); colours follow --ut-palette-*"),
            ("Invoice / checkout", "Form region (Template = Standard) + Classic Report (Template = Value Attribute Pairs - Row)"),
            ("Profile widget", "Avatar + Content Row template components"),
            ("Data tables", "Interactive Grid / Interactive Report"),
        ],
        "signature": """
.t-Body-nav .t-TreeNav { padding-top: .5rem; }
""",
    },
    {
        "slug": "rome", "name": "Rome", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/rome",
        "summary": "airy light dashboard: periwinkle blue, peach and pink accents, soft tinted shadows",
        "look": [
            "Very light lavender canvas, pure white cards with generous 20px radius.",
            "Periwinkle-blue primary, peach and pink secondary accents.",
            "Soft blue-tinted shadows instead of borders; rounded pill controls and switches.",
        ],
        "fonts": {"body": "DM Sans", "heading": "DM Sans", "google": ["DM+Sans:wght@400;500;600;700"]},
        "modes": ["light"],
        "base": {
            "primary": "#4C74FC", "accent": "#FCA44C", "success": "#2FB67C", "warning": "#FCA44C",
            "danger": "#F2617A", "info": "#8CA4FC",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "20px", "btn-radius": "12px", "field-radius": "12px",
            "nav-item-radius": "12px", "nav-item-inset": "12px", "border-width": "0px",
        },
        "light": {"bg": "#F4F5FC", "surface": "#FFFFFF", "surface-2": "#F7F8FE", "border": "#E7EAF7",
                  "text": "#1B1F3B", "text-muted": "#7A80A6", "highlight": "#EEF2FF",
                  "nav-bg": "#FFFFFF", "nav-text": "#5D6488", "nav-active-bg": "#EEF2FF", "nav-active-text": "#4C74FC"},
        "shadow": {"light": "tinted"},
        "chart": ["#4C74FC", "#FCA44C", "#FC8CA4", "#8CA4FC", "#2FB67C", "#BCCCFC", "#FCDCB4", "#A78BFA"],
        "recipes": [
            ("Calendar picker card", "Date Picker item, Display As = Inline; region template Standard"),
            ("Pill tabs", "Region Display Selector or Tabs Container with Template Options `Style = Pill`"),
            ("Sliders / switches", "Number Field with range is not native: use Switch item; for ranges use two Number Fields"),
            ("Profile card", "Cards region with Initials/Avatar slot, centered body"),
        ],
        "signature": """
.t-Region, .a-CardView-item { border: 0 !important; }
""",
    },
    {
        "slug": "neolex", "name": "Neolex", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/neolex-dashboard",
        "summary": "8dp-grid responsive dashboard: bright azure, orange and purple accents, crisp light greys",
        "look": [
            "Strict 8dp spacing rhythm; light grey canvas with white panels and thin borders.",
            "Bright azure primary; orange and purple used for charts and highlights.",
            "Shopping, CRM, tasks, planner, kanban, news and table layouts.",
        ],
        "fonts": {"body": "Nunito Sans", "heading": "Nunito Sans", "google": ["Nunito+Sans:wght@400;600;700;800"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#047CFC", "accent": "#FC8C34", "success": "#22B07D", "warning": "#FC8C34",
            "danger": "#F0445A", "info": "#9C54E4",
            "radius-sm": "4px", "radius-md": "8px", "radius-lg": "8px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px", "nav-item-inset": "8px",
        },
        "light": {"bg": "#F4F4F4", "surface": "#FFFFFF", "surface-2": "#FAFAFA", "border": "#E4E4E4",
                  "text": "#1F2430", "text-muted": "#6F7787", "highlight": "#E6F2FF",
                  "nav-bg": "#FFFFFF", "nav-text": "#4A5263", "nav-active-bg": "#E6F2FF", "nav-active-text": "#047CFC"},
        "dark": {"bg": "#121418", "surface": "#1B1E24", "surface-2": "#22262E", "border": "#2E333D",
                 "text": "#F1F3F7", "text-muted": "#9AA2B1", "nav-bg": "#16191E", "header-bg": "#16191E",
                 "nav-text": "#B4BBC8", "nav-active-bg": "rgba(4,124,252,.18)", "nav-active-text": "#4CA4FC"},
        "shadow": {"light": "flat", "dark": "dark"},
        "chart": ["#047CFC", "#FC8C34", "#9C54E4", "#4CA4FC", "#22B07D", "#94C4FC", "#F0445A", "#FFC542"],
        "recipes": [
            ("Task / planner lists", "Content Row template component with checkbox via Cards/Content Row actions"),
            ("Shopping product grid", "Cards region, Media Source = Image, Layout = Grid, 3-4 columns"),
            ("Stats tiles", "Cards region (Layout = Grid); or Badge template component for single numbers"),
            ("News feed", "Media List template component"),
        ],
        "signature": "",
    },
    {
        "slug": "react-ui-kit", "name": "React UI kit (Blueprint)", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/react-ui-kit",
        "summary": "data-dense Blueprint.js-style desktop UI: tight spacing, 3px radii, inset borders",
        "look": [
            "Built on Blueprint.js styling: compact controls, 3-4px radii, subtle inset borders.",
            "Neutral greys with Blueprint blue/green/orange/red intents.",
            "Optimised for complex, data-dense desktop tools (tables, trees, toolbars).",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#2D72D2", "accent": "#7961DB", "success": "#238551", "warning": "#C87619",
            "danger": "#CD4246", "info": "#2D72D2",
            "radius-sm": "2px", "radius-md": "3px", "radius-lg": "4px", "btn-radius": "3px", "field-radius": "3px",
            "nav-item-radius": "3px", "btn-padding-y": ".3125rem", "btn-padding-x": ".625rem",
            "btn-font-size": ".8125rem", "btn-weight": "500",
        },
        "light": {"bg": "#F6F7F9", "surface": "#FFFFFF", "surface-2": "#F6F7F9", "border": "#DCE0E5",
                  "text": "#1C2127", "text-muted": "#5F6B7C", "highlight": "rgba(45,114,210,.1)",
                  "nav-bg": "#FFFFFF", "nav-text": "#404854", "nav-active-bg": "rgba(45,114,210,.12)",
                  "nav-active-text": "#215DB0"},
        "dark": {"bg": "#1C2127", "surface": "#252A31", "surface-2": "#2F343C", "border": "#404854",
                 "text": "#F6F7F9", "text-muted": "#ABB3BF", "highlight": "rgba(76,144,240,.15)",
                 "nav-bg": "#252A31", "header-bg": "#2F343C", "nav-text": "#D3D8DE",
                 "nav-active-bg": "rgba(76,144,240,.2)", "nav-active-text": "#8ABBFF", "primary": "#4C90F0"},
        "shadow": {"light": "flat", "dark": "dark"},
        "chart": ["#2D72D2", "#238551", "#C87619", "#CD4246", "#7961DB", "#147EB3", "#D1980B", "#D13913"],
        "recipes": [
            ("Dense tables", "Interactive Grid; Template Options on the region: `Remove Body Padding`; IG attributes: Fixed Row Height"),
            ("Tree / file explorer", "Tree region (native, uses --a-treeview-* vars)"),
            ("Toolbars + button groups", "Buttons in Region `Edit`/`Next` positions; Button Template Options `Button Set = Inner/First/Last`"),
            ("Callouts", "Alert region template, Template Options `Alert Type` + `Horizontal`"),
            ("Segmented tabs", "Radio Group item with Template Option `Display as Pill Button`"),
        ],
        "signature": """
.t-Button:not(.t-Button--hot):not(.t-Button--noUI) { box-shadow: inset 0 0 0 1px rgba(17,20,24,.2), 0 1px 2px rgba(17,20,24,.1); }
""",
    },
    {
        "slug": "xela", "name": "Xela", "category": "Dashboard",
        "url": "https://www.setproduct.com/templates/xela-react",
        "summary": "cross-platform (React/Swift/Android/Flutter) system: royal blue, crisp white, easy dark toggle",
        "look": [
            "Royal-blue primary on crisp white; soft blue-grey neutrals; peach accent.",
            "Rounded 10px controls, clear focus rings; built to swap dark and light with no hassle.",
            "Same kit ships for React, Swift, Android and Flutter; this theme covers the web look.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#3464FC", "accent": "#FC9C6C", "success": "#1DB98A", "warning": "#FFB020",
            "danger": "#F0445A", "info": "#043CEC",
            "radius-sm": "6px", "radius-md": "10px", "radius-lg": "16px", "btn-radius": "10px", "field-radius": "10px",
            "nav-item-radius": "10px", "nav-item-inset": "10px",
        },
        "light": {"bg": "#F4F6FB", "surface": "#FFFFFF", "surface-2": "#F8FAFE", "border": "#E5E9F2",
                  "text": "#0E1A3B", "text-muted": "#6B7593", "highlight": "#EBF0FF",
                  "nav-bg": "#FFFFFF", "nav-text": "#4A5578", "nav-active-bg": "#EBF0FF", "nav-active-text": "#3464FC"},
        "dark": {"bg": "#0B1020", "surface": "#121A30", "surface-2": "#18223D", "border": "#24304F",
                 "text": "#EEF2FF", "text-muted": "#93A0C4", "nav-bg": "#0E1428", "header-bg": "#0E1428",
                 "nav-text": "#B6C1E0", "nav-active-bg": "rgba(52,100,252,.22)", "nav-active-text": "#94ACFC"},
        "shadow": {"light": "soft", "dark": "dark"},
        "chart": ["#3464FC", "#FC9C6C", "#1DB98A", "#94ACFC", "#FFB020", "#F0445A", "#5C84FC", "#C4D4FC"],
        "recipes": [
            ("Accordions", "Collapsible region template, or Region Display Selector"),
            ("Rating, sliders", "Star Rating item (native); range = two Number Field items"),
            ("Steppers", "Wizard Progress list (Steps navigation) + Wizard Container region"),
            ("Pagination", "Report pagination; Classic Report Pagination Type = Row Ranges X to Y"),
        ],
        "signature": "",
    },
    # ------------------------------------------------------------------ material family
    {
        "slug": "material-you", "name": "Material You", "category": "Material",
        "url": "https://www.setproduct.com/templates/material-you",
        "summary": "Material Design 3 with Tailwind palette and Readex Pro: tonal surfaces, pill buttons",
        "look": [
            "Material Design 3: tonal (tinted) surfaces instead of heavy shadows.",
            "Tailwind blue/indigo palette, pill-shaped buttons and navigation indicators.",
            "Readex Pro type; large 16-28px container radii; dialogs with icon headers.",
        ],
        "fonts": {"body": "Readex Pro", "heading": "Readex Pro", "google": ["Readex+Pro:wght@300;400;500;600"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#3B82F6", "accent": "#4F46E5", "success": "#22C55E", "warning": "#F59E0B",
            "danger": "#EF4444", "info": "#0EA5E9",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "16px", "btn-radius": "999px", "field-radius": "12px",
            "nav-item-radius": "999px", "nav-item-inset": "12px", "weight-semibold": "500",
            "btn-padding-x": "1.5rem", "btn-padding-y": ".625rem",
        },
        "light": {"bg": "#F8FAFF", "surface": "#FFFFFF", "surface-2": "#EEF4FE", "border": "#E2E8F0",
                  "text": "#0F172A", "text-muted": "#64748B", "highlight": "#E0ECFF",
                  "nav-bg": "#EEF4FE", "nav-text": "#334155", "nav-active-bg": "#D3E3FD",
                  "nav-active-text": "#0F172A", "header-bg": "#F8FAFF", "nav-border": "transparent",
                  "field-bg": "#EEF4FE", "field-border": "transparent"},
        "dark": {"bg": "#0B1220", "surface": "#111A2E", "surface-2": "#1C2C54", "border": "#26365E",
                 "text": "#E5ECF8", "text-muted": "#94A3B8", "highlight": "rgba(59,130,246,.18)",
                 "nav-bg": "#111A2E", "header-bg": "#0B1220", "nav-text": "#C7D2E6",
                 "nav-active-bg": "#1C2C54", "nav-active-text": "#FFFFFF", "nav-border": "transparent",
                 "field-bg": "#1C2C54", "field-border": "transparent", "primary": "#60A5FA",
                 "primary-contrast": "#0B1220"},
        "shadow": {"light": "flat", "dark": "dark"},
        "chart": ["#3B82F6", "#4F46E5", "#22C55E", "#F59E0B", "#EF4444", "#0EA5E9", "#A855F7", "#14B8A6"],
        "recipes": [
            ("Filled text fields", "Page Items with Template `Optional - Floating`; tonal fill comes from --sp-field-bg"),
            ("Navigation rail / drawer", "Navigation Menu = Side Menu; pill active indicator comes from nav tokens"),
            ("FAB", "Button, Template = Icon, Template Options `Hot` + CSS class `sp-fab`; position via Region `Floating` or page-level button"),
            ("Dialogs with icon header", "Modal Dialog page; Hero region at top with icon"),
            ("Chips / filters", "Faceted Search or Smart Filters region (native chips)"),
            ("Segmented button", "Radio Group, Template Option `Display as Pill Button`"),
        ],
        "signature": """
.sp-fab.t-Button { width: 56px; height: 56px; border-radius: 16px !important; box-shadow: 0 6px 16px rgba(0,0,0,.18); }
.t-Form-fieldContainer--floatingLabel .apex-item-text, .t-Form-fieldContainer--floatingLabel .apex-item-select, .t-Form-fieldContainer--floatingLabel .apex-item-textarea { border-bottom: 2px solid transparent; }
.t-Form-fieldContainer--floatingLabel.is-active .apex-item-text { border-bottom-color: var(--sp-primary); }
""",
    },
    {
        "slug": "material-x", "name": "Material X", "category": "Material",
        "url": "https://www.setproduct.com/templates/material-x",
        "summary": "Material beyond Material: Manrope type, deep indigo + teal, top-notch rounded shapes",
        "look": [
            "Material foundations with bolder shapes: 16-24px radii and asymmetric 'notch' corners on hero cards.",
            "Deep indigo primary, teal accent, white surfaces on a cool off-white canvas.",
            "Manrope typeface throughout; 40 desktop/tablet/mobile app templates (Angular port exists).",
        ],
        "fonts": {"body": "Manrope", "heading": "Manrope", "google": ["Manrope:wght@400;500;600;700;800"]},
        "modes": ["light"],
        "base": {
            "primary": "#24348C", "accent": "#5CC4B4", "success": "#248C24", "warning": "#F2A93B",
            "danger": "#D6455D", "info": "#5464A4",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "20px", "btn-radius": "12px", "field-radius": "12px",
            "nav-item-radius": "999px", "nav-item-inset": "12px", "weight-semibold": "700",
        },
        "light": {"bg": "#F7F8FC", "surface": "#FFFFFF", "surface-2": "#F2F4FA", "border": "#E3E6F0",
                  "text": "#141A33", "text-muted": "#626A86", "highlight": "#E8EBF7",
                  "nav-bg": "#FFFFFF", "nav-text": "#3D4466", "nav-active-bg": "#DDE3FA", "nav-active-text": "#24348C"},
        "shadow": {"light": "soft"},
        "chart": ["#24348C", "#5CC4B4", "#5464A4", "#9CDCD4", "#F2A93B", "#D6455D", "#248C24", "#ACFCF4"],
        "recipes": [
            ("Notched hero card", "Static Content / Cards region + CSS class `sp-notch`"),
            ("Steppers / counters", "Number Field + two Icon buttons (Template Option `Button Set`)"),
            ("Top app bar", "Page template Standard with Navigation Menu Position = Top (Top Navigation Menu list)"),
            ("Data cards", "Cards region (Layout = Grid) with Icon/Media slot"),
        ],
        "signature": """
.sp-notch { border-radius: 28px 6px 28px 6px !important; }
""",
    },
    {
        "slug": "material", "name": "Material Design System", "category": "Material",
        "url": "https://www.setproduct.com/templates/material",
        "summary": "classic Material Design (material.io): Roboto + Red Hat Display, elevation shadows, 4px radii",
        "look": [
            "100% material.io guidelines: elevation shadows, 4px radii, uppercase text buttons.",
            "Roboto body with Red Hat Display headings.",
            "Light and dark themes per the Material dark-theme spec (#121212 surfaces).",
        ],
        "fonts": {"body": "Roboto", "heading": "Red Hat Display",
                  "google": ["Roboto:wght@400;500;700", "Red+Hat+Display:wght@500;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#3D7FF0", "accent": "#FC7C2C", "success": "#34A853", "warning": "#FBBC05",
            "danger": "#EA4335", "info": "#3D7FF0",
            "radius-sm": "4px", "radius-md": "4px", "radius-lg": "8px", "btn-radius": "4px", "field-radius": "4px",
            "nav-item-radius": "0 999px 999px 0", "weight-semibold": "500",
            "btn-transform": "uppercase", "btn-weight": "500", "heading-tracking": "0",
            "header-shadow": "0 2px 4px rgba(0,0,0,.2)",
        },
        "light": {"bg": "#F5F5F5", "surface": "#FFFFFF", "surface-2": "#FAFAFA", "border": "#E0E0E0",
                  "text": "#212121", "text-muted": "#757575", "header-bg": "#3D7FF0", "header-text": "#FFFFFF",
                  "nav-bg": "#FFFFFF", "nav-text": "#424242", "nav-active-bg": "rgba(61,127,240,.12)",
                  "nav-active-text": "#3D7FF0"},
        "dark": {"bg": "#121212", "surface": "#1E1E1E", "surface-2": "#2C2C2C", "border": "#333333",
                 "text": "#E0E0E0", "text-muted": "#A0A0A0", "header-bg": "#1E1E1E", "header-text": "#FFFFFF",
                 "nav-bg": "#1E1E1E", "nav-text": "#CFCFCF", "nav-active-bg": "rgba(148,180,236,.16)",
                 "nav-active-text": "#94B4EC", "primary": "#94B4EC", "primary-contrast": "#121212"},
        "shadow": {"light": "elevated", "dark": "dark"},
        "chart": ["#3D7FF0", "#EA4335", "#FBBC05", "#34A853", "#FC7C2C", "#AB47BC", "#00ACC1", "#94B4EC"],
        "recipes": [
            ("App bar", "Header = coloured (header-bg token = primary)"),
            ("Text / contained / outlined buttons", "Button templates Text (Hot = contained), Template Options `Style = Simple` = outlined, `Style = Remove UI Decoration` = text"),
            ("Snackbar", "apex.message.showPageSuccess() (native success message) - styled by palette"),
            ("FAB", "Icon button + CSS class `sp-fab`"),
        ],
        "signature": """
.sp-fab.t-Button { width: 56px; height: 56px; border-radius: 50% !important; box-shadow: 0 3px 5px -1px rgba(0,0,0,.2), 0 6px 10px rgba(0,0,0,.14); }
.t-Button { letter-spacing: .04em; }
""",
    },
    # ------------------------------------------------------------------ AI product
    {
        "slug": "nocra", "name": "Nocra", "category": "AI product",
        "url": "https://www.setproduct.com/templates/nocra",
        "summary": "AI-product design system: deep midnight navy, mint CTAs, prompt inputs, thinking-state motion",
        "look": [
            "Deep midnight-navy canvas with soft glows; mint-green primary actions.",
            "Large rounded prompt inputs, prompt-history lists, AI status panels, style selectors.",
            "Microinteractions: loaders, thinking shimmer, success/error motion.",
        ],
        "fonts": {"body": "Geist", "heading": "Geist", "google": ["Geist:wght@400;500;600;700"]},
        "modes": ["dark", "light"],
        "base": {
            "success": "#2ECC8F", "warning": "#F5B544", "danger": "#F40C04", "info": "#C4DCFC",
            "accent": "#CCFCBC", "accent-contrast": "#0C0C44",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "20px", "btn-radius": "12px", "field-radius": "16px",
            "nav-item-radius": "10px", "nav-item-inset": "10px",
        },
        "dark": {"primary": "#CCFCBC", "primary-contrast": "#0C0C44",
                 "bg": "#07071F", "surface": "#0F0F33", "surface-2": "#16163F", "border": "#24245A",
                 "text": "#F2F2FF", "text-muted": "#9B9BC9", "highlight": "rgba(204,252,188,.08)",
                 "nav-bg": "#0A0A26", "header-bg": "#07071F", "nav-text": "#B9B9DD",
                 "nav-active-bg": "rgba(204,252,188,.12)", "nav-active-text": "#CCFCBC",
                 "field-bg": "#16163F", "field-border": "#2B2B66"},
        "light": {"primary": "#1C1C7C", "primary-contrast": "#FFFFFF",
                  "bg": "#F7F7FB", "surface": "#FFFFFF", "surface-2": "#F1F1F8", "border": "#E4E4F0",
                  "text": "#0C0C44", "text-muted": "#66668F", "nav-bg": "#FFFFFF", "nav-text": "#3A3A6E",
                  "nav-active-bg": "#ECECFB", "nav-active-text": "#1C1C7C"},
        "shadow": {"dark": "glow", "light": "soft"},
        "chart": ["#CCFCBC", "#C4DCFC", "#8E8EFF", "#2ECC8F", "#F5B544", "#FF7A7A", "#5EEAD4", "#E9D5FF"],
        "recipes": [
            ("AI chat / assistant", "Dynamic Action `Show AI Assistant` (APEX 24.1+, native) - styled via --a-chat-* vars"),
            ("Prompt input", "Textarea item, Template `Optional`, CSS class `sp-prompt` on the item (Advanced > CSS Classes) + Hot icon button"),
            ("Prompt history", "Content Row or Media List template component"),
            ("Style / model selector", "Radio Group, Template Option `Display as Pill Button`, or Cards region with selectable cards"),
            ("Generation status panel", "Badge template component + CSS class `sp-thinking` while running"),
            ("Server call", "APEX_AI.GENERATE (24.1+) in a PL/SQL process or Ajax callback"),
        ],
        "signature": """
.sp-prompt, .sp-prompt.apex-item-textarea { border-radius: var(--sp-radius-lg) !important; min-height: 6rem; padding: 1rem 1.125rem; box-shadow: 0 0 0 1px var(--sp-border), 0 0 32px color-mix(in srgb, var(--sp-primary) 10%, transparent); }
.sp-prompt:focus { box-shadow: 0 0 0 2px var(--sp-primary), 0 0 40px color-mix(in srgb, var(--sp-primary) 22%, transparent); }
.sp-thinking { background: linear-gradient(90deg, var(--sp-text-muted) 0%, var(--sp-primary) 50%, var(--sp-text-muted) 100%); background-size: 200% 100%; -webkit-background-clip: text; background-clip: text; color: transparent !important; animation: sp-shimmer 1.6s linear infinite; }
@keyframes sp-shimmer { to { background-position: -200% 0; } }
@media (prefers-reduced-motion: reduce) { .sp-thinking { animation: none; color: var(--sp-text-muted) !important; } }
""",
    },
    # ------------------------------------------------------------------ data viz
    {
        "slug": "orion", "name": "Orion", "category": "Data visualization",
        "url": "https://www.setproduct.com/templates/orion",
        "summary": "space-themed dataviz: deep indigo night, neon violet/cyan, glowing maps, hexagons and bubbles",
        "look": [
            "Deep indigo 'night sky' canvas; neon violet, electric blue and cyan series.",
            "Full-width chart templates: world maps, bubble, heat maps, hexagon grids, connection graphs.",
            "Glows and radial gradients behind hero numbers; light variant on lavender-white.",
        ],
        "fonts": {"body": "Inter", "heading": "Space Grotesk",
                  "google": ["Inter:wght@400;500;600", "Space+Grotesk:wght@500;700"]},
        "modes": ["dark", "light"],
        "base": {
            "primary": "#8474FC", "accent": "#04F4E4", "accent-contrast": "#05051A", "success": "#2EE6A8",
            "warning": "#FFB547", "danger": "#FF4D8D", "info": "#043CFC",
            "radius-sm": "6px", "radius-md": "10px", "radius-lg": "16px", "btn-radius": "10px", "field-radius": "10px",
            "nav-item-radius": "10px", "nav-item-inset": "8px",
        },
        "dark": {"bg": "#05051A", "surface": "#0E0E2A", "surface-2": "#16163A", "border": "#23234D",
                 "text": "#F2F2FF", "text-muted": "#8D8DB8", "nav-bg": "#08081F", "header-bg": "#05051A",
                 "nav-text": "#B5B5DA", "nav-active-bg": "rgba(132,116,252,.2)", "nav-active-text": "#FFFFFF"},
        "light": {"bg": "#F4F4FC", "surface": "#FFFFFF", "surface-2": "#F7F6FF", "border": "#E4E2F7",
                  "text": "#1C1C54", "text-muted": "#6E6E99", "nav-bg": "#FFFFFF", "nav-text": "#3F3F75",
                  "nav-active-bg": "#EEEBFF", "nav-active-text": "#5B4AE6"},
        "shadow": {"dark": "glow", "light": "tinted"},
        "chart": ["#8474FC", "#04F4E4", "#043CFC", "#FF4D8D", "#FFB547", "#2EE6A8", "#BCB4FC", "#5B8CFF"],
        "recipes": [
            ("World map / continent data", "Map region (native, APEX 21.1+) with Choropleth or Bubbles layer; colour layers from the chart palette"),
            ("Bubble, heat map, polar charts", "Chart region: Bubble, Polar, or Status Meter Gauge; hexagons need a Treemap or custom SVG"),
            ("Connection graphs", "not native - use Treemap/Sunburst charts, or Oracle's Graph Visualization plug-in"),
            ("Hero metric with glow", "Static Content + CSS class `sp-glow`"),
        ],
        "signature": """
.sp-glow { background: radial-gradient(120% 90% at 20% 0%, color-mix(in srgb, var(--sp-primary) 28%, transparent) 0%, transparent 60%), radial-gradient(90% 80% at 100% 100%, color-mix(in srgb, var(--sp-accent) 18%, transparent) 0%, transparent 55%), var(--sp-surface) !important; }
""",
    },
    {
        "slug": "charts", "name": "Figma Charts", "category": "Data visualization",
        "url": "https://www.setproduct.com/templates/charts",
        "summary": "component-driven chart library: pastel-bright violet/blue/mint/peach series on clean white cards",
        "look": [
            "Clean white chart cards; violet, sky blue, mint and peach series with pastel fills.",
            "150+ templates across desktop/tablet/mobile; every chart cloned into dark mode.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#845CF4", "accent": "#54A4FC", "success": "#1CD4A4", "warning": "#FCBC7C",
            "danger": "#F87171", "info": "#54A4FC",
            "radius-sm": "6px", "radius-md": "8px", "radius-lg": "12px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px", "nav-item-inset": "8px",
        },
        "light": {"bg": "#F7F7FC", "surface": "#FFFFFF", "surface-2": "#FAFAFE", "border": "#ECECF4",
                  "text": "#2C2C34", "text-muted": "#7C7C8A", "nav-bg": "#FFFFFF", "nav-text": "#4A4A57",
                  "nav-active-bg": "#F1ECFE", "nav-active-text": "#845CF4"},
        "dark": {"bg": "#16161D", "surface": "#1F1F28", "surface-2": "#272732", "border": "#33333F",
                 "text": "#F2F2F7", "text-muted": "#9D9DAD", "nav-bg": "#1A1A22", "header-bg": "#16161D",
                 "nav-text": "#C2C2D0", "nav-active-bg": "rgba(132,92,244,.22)", "nav-active-text": "#CCBCFC"},
        "shadow": {"light": "soft", "dark": "dark"},
        "chart": ["#845CF4", "#54A4FC", "#1CD4A4", "#FCBC7C", "#F87171", "#CCBCFC", "#BCF4E4", "#FACC15"],
        "recipes": [
            ("Any of the 25+ chart types", "Chart region (Oracle JET): bar, line, area, combo, pie/donut, funnel, pyramid, radar, polar, range, stock, gauge"),
            ("Chart card with header metric", "Chart region in Standard template; put the metric in Region Header via a Display Only item or the region's `Sub Title`"),
            ("Infographic progress", "Percent Graph / Status Meter Gauge chart"),
        ],
        "signature": "",
    },
    {
        "slug": "hyper-charts", "name": "Hyper Charts", "category": "Data visualization",
        "url": "https://www.setproduct.com/templates/hyper-charts",
        "summary": "1000+ chart blocks: indigo and fresh green on lavender-tinted cards, rounded and airy",
        "look": [
            "Indigo + fresh green series, sky and lavender supporting colours.",
            "Chart cards with big rounded corners and dollar-figure headlines; full dark mode.",
        ],
        "fonts": {"body": "Outfit", "heading": "Outfit", "google": ["Outfit:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#6C74E4", "accent": "#4CDC6C", "success": "#4CDC6C", "warning": "#FFB86B",
            "danger": "#FC6C6C", "info": "#5CD4FC",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "20px", "btn-radius": "12px", "field-radius": "12px",
            "nav-item-radius": "12px", "nav-item-inset": "10px",
        },
        "light": {"bg": "#F6F5FF", "surface": "#FFFFFF", "surface-2": "#F8F7FF", "border": "#E9E7FA",
                  "text": "#1E1F3A", "text-muted": "#727497", "nav-bg": "#FFFFFF", "nav-text": "#46486E",
                  "nav-active-bg": "#ECEDFC", "nav-active-text": "#6C74E4"},
        "dark": {"bg": "#0A0A10", "surface": "#15151F", "surface-2": "#1D1D2A", "border": "#2A2A3B",
                 "text": "#F1F1FA", "text-muted": "#9A9BB8", "nav-bg": "#101018", "header-bg": "#0A0A10",
                 "nav-text": "#C0C1DB", "nav-active-bg": "rgba(108,116,228,.22)", "nav-active-text": "#ACB4F4"},
        "shadow": {"light": "tinted", "dark": "dark"},
        "chart": ["#6C74E4", "#4CDC6C", "#5CD4FC", "#DCC4FC", "#FFB86B", "#FC6C6C", "#ACB4F4", "#FCECC4"],
        "recipes": [
            ("Chart blocks", "Chart region per block; group 2-4 per row with Column Span in Layout"),
            ("Headline figure + delta", "Cards region with the Badge slot for the delta"),
        ],
        "signature": "",
    },
    # ------------------------------------------------------------------ mobile
    {
        "slug": "nucleus", "name": "Nucleus UI", "category": "Mobile",
        "url": "https://www.setproduct.com/templates/nucleus-ui",
        "summary": "1000+ component mobile system: vivid violet, sunshine-yellow highlights, rounded friendly UI",
        "look": [
            "Vivid violet primary with sunshine-yellow highlight chips; deep indigo for dark surfaces.",
            "Friendly rounded components (16px+) and large touch targets; 500+ mobile screens.",
            "Sector themes: events, food delivery, healthcare, finance, travel, NFT, e-commerce.",
        ],
        "fonts": {"body": "Poppins", "heading": "Poppins", "google": ["Poppins:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#7454FC", "accent": "#FCDC4C", "accent-contrast": "#1A1433", "success": "#22C55E",
            "warning": "#FCDC4C", "danger": "#F43F5E", "info": "#2414AC",
            "radius-sm": "10px", "radius-md": "14px", "radius-lg": "22px", "btn-radius": "14px", "field-radius": "14px",
            "nav-item-radius": "14px", "nav-item-inset": "10px",
            "btn-padding-y": ".75rem", "btn-padding-x": "1.25rem", "btn-font-size": ".875rem",
        },
        "light": {"bg": "#F7F6FF", "surface": "#FFFFFF", "surface-2": "#F4F2FF", "border": "#ECE9FB",
                  "text": "#1A1433", "text-muted": "#7B7596", "nav-bg": "#FFFFFF", "nav-text": "#4B4566",
                  "nav-active-bg": "#EFEAFF", "nav-active-text": "#7454FC"},
        "dark": {"bg": "#0F0B24", "surface": "#1A1438", "surface-2": "#221B47", "border": "#2F2760",
                 "text": "#F5F3FF", "text-muted": "#A39DC4", "nav-bg": "#14102E", "header-bg": "#0F0B24",
                 "nav-text": "#C9C3E8", "nav-active-bg": "rgba(116,84,252,.25)", "nav-active-text": "#FFFFFF",
                 "primary": "#8E73FF"},
        "shadow": {"light": "tinted", "dark": "dark"},
        "chart": ["#7454FC", "#FCDC4C", "#2414AC", "#22C55E", "#F43F5E", "#9CBCEC", "#CCC4FC", "#FB923C"],
        "recipes": [
            ("Mobile app shell", "Enable Progressive Web App (Shared Components > PWA) + page template `Standard`; Navigation Menu = Side Menu collapsed by default, or Top Navigation Tabs"),
            ("List screens", "Content Row / Media List template components"),
            ("Bottom sheets", "Inline Drawer region (native) or Modal Dialog with `Drawer` page template"),
            ("Big CTA button", "Button Template Options `Stretch` + `Large`, Hot"),
        ],
        "signature": "",
    },
    {
        "slug": "mobile-x", "name": "Mobile X", "category": "Mobile",
        "url": "https://www.setproduct.com/templates/mobile-x",
        "summary": "iOS/Android cross-platform kit: clear blue, lime highlight, 8dp grid, toggleable dark variants",
        "look": [
            "Clear blue primary with a lime-green highlight and blush-pink tags.",
            "iOS specs adopted to the Android 8dp grid; every component has a dark variant.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#4474FC", "accent": "#B4EC5C", "accent-contrast": "#1A2410", "success": "#3DBE6B",
            "warning": "#FFB020", "danger": "#FF5C5C", "info": "#3454AC",
            "radius-sm": "6px", "radius-md": "10px", "radius-lg": "16px", "btn-radius": "10px", "field-radius": "10px",
            "nav-item-radius": "10px", "nav-item-inset": "8px",
        },
        "light": {"bg": "#F5F6FA", "surface": "#FFFFFF", "surface-2": "#F8F9FC", "border": "#E5E7EF",
                  "text": "#121726", "text-muted": "#6A7186", "nav-bg": "#FFFFFF", "nav-text": "#3F465A",
                  "nav-active-bg": "#E8EEFF", "nav-active-text": "#4474FC"},
        "dark": {"bg": "#161616", "surface": "#242424", "surface-2": "#2D2D2D", "border": "#3A3A3A",
                 "text": "#F4F4F4", "text-muted": "#A3A3A3", "nav-bg": "#1C1C1C", "header-bg": "#161616",
                 "nav-text": "#CFCFCF", "nav-active-bg": "rgba(68,116,252,.22)", "nav-active-text": "#8CACFC"},
        "shadow": {"light": "soft", "dark": "dark"},
        "chart": ["#4474FC", "#B4EC5C", "#FCC4C4", "#3454AC", "#8CACFC", "#FF5C5C", "#FFB020", "#24346C"],
        "recipes": [
            ("App bars", "Header + Breadcrumb Bar region; Back button = Button with `t-Button--noUI` icon"),
            ("Sheets", "Inline Drawer region"),
            ("PIN / register inputs", "Text Field items with Template `Optional - Floating`"),
            ("Settings toggles", "Switch item; group with Content Row"),
        ],
        "signature": "",
    },
    {
        "slug": "appka-ios", "name": "Appka iOS", "category": "Mobile",
        "url": "https://www.setproduct.com/templates/appka-ios-ui-kit",
        "summary": "Apple-spec iOS system: grouped inset lists, SF-style type, system blue-violet, true-black dark",
        "look": [
            "Apple HIG: grouped inset lists on #F2F2F7, hairline separators, 10-14px radii.",
            "System-font stack (SF Pro where available), blue-violet tint, true-black dark mode.",
            "4100+ variants for 28 components, 280+ layouts across 14 categories.",
        ],
        "fonts": {"body": "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", Inter",
                  "heading": "-apple-system, BlinkMacSystemFont, \"SF Pro Display\", Inter",
                  "google": ["Inter:wght@400;500;600;700"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#4444E4", "accent": "#FCC444", "accent-contrast": "#1C1C1E", "success": "#34C759",
            "warning": "#FF9500", "danger": "#EC042C", "info": "#7474EC",
            "radius-sm": "8px", "radius-md": "10px", "radius-lg": "14px", "btn-radius": "12px", "field-radius": "10px",
            "nav-item-radius": "10px", "nav-item-inset": "8px", "border-width": "0px",
        },
        "light": {"bg": "#F2F2F7", "surface": "#FFFFFF", "surface-2": "#F2F2F7", "border": "#E5E5EA",
                  "text": "#000000", "text-muted": "#8E8E93", "nav-bg": "#F2F2F7", "nav-text": "#3C3C43",
                  "nav-active-bg": "#FFFFFF", "nav-active-text": "#4444E4", "header-bg": "rgba(249,249,249,.94)",
                  "field-bg": "#FFFFFF"},
        "dark": {"bg": "#000000", "surface": "#1C1C1E", "surface-2": "#2C2C2E", "border": "#38383A",
                 "text": "#FFFFFF", "text-muted": "#8E8E93", "nav-bg": "#000000", "header-bg": "rgba(22,22,24,.94)",
                 "nav-text": "#EBEBF5", "nav-active-bg": "#1C1C1E", "nav-active-text": "#7D7DFF",
                 "field-bg": "#1C1C1E", "primary": "#5E5CE6"},
        "shadow": {"light": "flat", "dark": "flat"},
        "chart": ["#4444E4", "#FCC444", "#34C759", "#FF9500", "#EC042C", "#7474EC", "#5AC8FA", "#AF52DE"],
        "recipes": [
            ("Grouped inset table view", "Content Row template component or Classic Report (Template = Standard) + region CSS class `sp-inset-group`"),
            ("Segmented control", "Radio Group, Template Option `Display as Pill Button`"),
            ("Action sheet", "Inline Drawer region or Modal Dialog (Drawer page template)"),
            ("Switches", "Switch item (native) - green ON via --sp-success"),
        ],
        "signature": """
.t-Header { -webkit-backdrop-filter: saturate(180%) blur(20px); backdrop-filter: saturate(180%) blur(20px); border-bottom: .5px solid var(--sp-border); }
.sp-inset-group { border-radius: var(--sp-radius-md) !important; overflow: hidden; }
.sp-inset-group .t-Report-cell, .sp-inset-group .t-ContentRow-item { border-bottom: .5px solid var(--sp-border); }
.a-Switch input:checked + .a-Switch-toggle { background-color: var(--sp-success); }
""",
    },
    {
        "slug": "android", "name": "Android UI kit", "category": "Mobile",
        "url": "https://www.setproduct.com/templates/android-ui-kit",
        "summary": "Android app templates: indigo-blue, amber accents, Roboto, elevation cards",
        "look": [
            "Indigo-blue primary, amber/orange accents, Roboto type.",
            "Elevated photo cards, filters, maps, planners, wishlists - 140 templates.",
        ],
        "fonts": {"body": "Roboto", "heading": "Roboto", "google": ["Roboto:wght@400;500;700"]},
        "modes": ["light"],
        "base": {
            "primary": "#546CFC", "accent": "#FC9C04", "success": "#2EB872", "warning": "#FC9C04",
            "danger": "#F0445A", "info": "#2C7CEC",
            "radius-sm": "4px", "radius-md": "8px", "radius-lg": "12px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px", "nav-item-inset": "8px", "weight-semibold": "500",
        },
        "light": {"bg": "#F7F8FC", "surface": "#FFFFFF", "surface-2": "#F4F6FB", "border": "#E3E6EF",
                  "text": "#1A1D29", "text-muted": "#6B7083", "nav-bg": "#FFFFFF", "nav-text": "#3D4256",
                  "nav-active-bg": "#ECEFFF", "nav-active-text": "#546CFC"},
        "shadow": {"light": "elevated"},
        "chart": ["#546CFC", "#FC9C04", "#2C7CEC", "#74B4DC", "#2EB872", "#F0445A", "#A4CCFC", "#FCECC4"],
        "recipes": [
            ("Photo cards", "Cards region, Media Source = Image, Layout = Grid"),
            ("Filters", "Faceted Search region"),
            ("Maps", "Map region (native)"),
        ],
        "signature": "",
    },
    # ------------------------------------------------------------------ web / landing
    {
        "slug": "zeus", "name": "Zeus", "category": "Landing pages",
        "url": "https://www.setproduct.com/templates/zeus",
        "summary": "landing-page system: teal + violet on white, dark hero bands, pill CTAs, 630+ web blocks",
        "look": [
            "White sections alternating with near-black hero/CTA bands.",
            "Teal and violet accents; pill-shaped CTAs; airy 24px-radius feature cards.",
            "Blocks: hero, features, FAQ, blog, pricing, testimonials, team, footer.",
        ],
        "fonts": {"body": "Plus Jakarta Sans", "heading": "Plus Jakarta Sans",
                  "google": ["Plus+Jakarta+Sans:wght@400;500;600;700;800"]},
        "modes": ["light"],
        "base": {
            "primary": "#845CD4", "accent": "#3CB4AC", "success": "#4CBC7C", "warning": "#F5B544",
            "danger": "#E5484D", "info": "#3CB4AC",
            "radius-sm": "8px", "radius-md": "14px", "radius-lg": "24px", "btn-radius": "999px", "field-radius": "12px",
            "nav-item-radius": "999px", "btn-padding-x": "1.5rem", "btn-padding-y": ".75rem",
        },
        "light": {"bg": "#FFFFFF", "surface": "#FFFFFF", "surface-2": "#F7F7FB", "border": "#ECECF2",
                  "text": "#0C0C14", "text-muted": "#6A6A7C", "nav-bg": "#FFFFFF", "nav-text": "#3A3A4C",
                  "nav-active-bg": "#F2ECFC", "nav-active-text": "#845CD4", "login-bg": "#0C0C14"},
        "shadow": {"light": "soft"},
        "chart": ["#845CD4", "#3CB4AC", "#4CBC7C", "#B4F4FC", "#9484C4", "#F5B544", "#A4B4E4", "#E5484D"],
        "recipes": [
            ("Hero", "Hero region template (set Heading Level to H1) + CSS class `sp-section-dark`"),
            ("Features grid", "Cards region, Layout = Grid, Grid Columns = 3, Icon slot"),
            ("Pricing", "Cards region (one card per plan) with Actions = Button"),
            ("FAQ", "Collapsible regions (Template = Collapsible, Template Option `Remove borders`)"),
            ("Testimonials / team", "Cards region with Initials/Avatar or Media List"),
            ("Page shell", "Public page (Authentication = Public), Page Template `Minimal (No Navigation)`"),
        ],
        "signature": """
.sp-section-dark { background: #0C0C14 !important; color: #FFFFFF; border: 0 !important; border-radius: var(--sp-radius-lg); }
.sp-section-dark .t-HeroRegion-title, .sp-section-dark .t-Region-title, .sp-section-dark .t-HeroRegion-desc { color: #FFFFFF; }
.t-HeroRegion-title { font-weight: 800; letter-spacing: -0.03em; }
""",
    },
    {
        "slug": "landing", "name": "Figma Landing Pages", "category": "Landing pages",
        "url": "https://www.setproduct.com/templates/landing",
        "summary": "colourful, trendy landing blocks: violet, sunshine yellow, mint on bright colour-block sections",
        "look": [
            "Bold colour-block sections (violet, sunshine yellow, mint) with white cards on top.",
            "Chunky headings, rounded 12-20px cards, tag-style labels.",
        ],
        "fonts": {"body": "Poppins", "heading": "Poppins", "google": ["Poppins:wght@400;500;600;700;800"]},
        "modes": ["light"],
        "base": {
            "primary": "#6C5CE4", "accent": "#FCCC6C", "accent-contrast": "#2B2340", "success": "#04B494",
            "warning": "#FCCC6C", "danger": "#F0506E", "info": "#54ECC4",
            "radius-sm": "8px", "radius-md": "12px", "radius-lg": "20px", "btn-radius": "10px", "field-radius": "10px",
            "nav-item-radius": "10px",
        },
        "light": {"bg": "#FFFFFF", "surface": "#FFFFFF", "surface-2": "#F7F6FE", "border": "#ECEAF7",
                  "text": "#1E1A33", "text-muted": "#6D6887", "nav-bg": "#FFFFFF", "nav-text": "#3F3A59",
                  "nav-active-bg": "#EEEBFD", "nav-active-text": "#6C5CE4"},
        "shadow": {"light": "soft"},
        "chart": ["#6C5CE4", "#FCCC6C", "#04B494", "#54ECC4", "#A49CFC", "#F0506E", "#FCECAC", "#2B2340"],
        "recipes": [
            ("Colour-block sections", "Static Content regions with CSS class `sp-block-violet` / `sp-block-yellow` / `sp-block-mint`"),
            ("Hero", "Hero region template"),
            ("Feature tiles", "Cards region (Layout = Grid) with Icon/Media slot"),
        ],
        "signature": """
.sp-block-violet { background: var(--sp-primary) !important; color: #fff; border: 0 !important; }
.sp-block-violet .t-Region-title, .sp-block-violet .t-HeroRegion-title { color: #fff; }
.sp-block-yellow { background: var(--sp-accent) !important; color: #2B2340; border: 0 !important; }
.sp-block-mint { background: #CFF8EC !important; color: #0B3B32; border: 0 !important; }
""",
    },
    {
        "slug": "website", "name": "Figma Website templates", "category": "Landing pages",
        "url": "https://www.setproduct.com/templates/website",
        "summary": "140+ dark & light website blocks: trustworthy blue, coral accent, mixable light/dark sections",
        "look": [
            "Trustworthy blue primary, coral accent; clean light sections mixed with dark ones.",
            "Classic SaaS website blocks: hero, logos, features, stats, blog, footer.",
        ],
        "fonts": {"body": "Inter", "heading": "Inter", "google": ["Inter:wght@400;500;600;700;800"]},
        "modes": ["light", "dark"],
        "base": {
            "primary": "#347CF4", "accent": "#FC5C54", "success": "#22C55E", "warning": "#FCCC6C",
            "danger": "#FC5C54", "info": "#347CF4",
            "radius-sm": "6px", "radius-md": "10px", "radius-lg": "16px", "btn-radius": "8px", "field-radius": "8px",
            "nav-item-radius": "8px",
        },
        "light": {"bg": "#FFFFFF", "surface": "#FFFFFF", "surface-2": "#F5F8FF", "border": "#E6EBF5",
                  "text": "#0F1729", "text-muted": "#64708A", "nav-bg": "#FFFFFF", "nav-text": "#36405A",
                  "nav-active-bg": "#EAF1FF", "nav-active-text": "#347CF4"},
        "dark": {"bg": "#0B111E", "surface": "#121A2B", "surface-2": "#18223A", "border": "#243150",
                 "text": "#EEF3FC", "text-muted": "#93A0BD", "nav-bg": "#0E1525", "header-bg": "#0B111E",
                 "nav-text": "#BCC7DE", "nav-active-bg": "rgba(52,124,244,.2)", "nav-active-text": "#A4C4FC"},
        "shadow": {"light": "soft", "dark": "dark"},
        "chart": ["#347CF4", "#FC5C54", "#22C55E", "#FCCC6C", "#A4C4FC", "#8CEC8C", "#C4ECFC", "#7C5CFC"],
        "recipes": [
            ("Dark section inside light page", "Static Content region + CSS class `sp-section-dark`"),
            ("Stats band", "Cards region, Layout = Grid, plus CSS class `sp-section-dark` if on a dark band"),
            ("Blog list", "Cards region, Media Source = Image"),
        ],
        "signature": """
.sp-section-dark { background: #0B111E !important; color: #EEF3FC; border: 0 !important; }
.sp-section-dark .t-Region-title, .sp-section-dark .t-HeroRegion-title { color: #fff; }
""",
    },
    {
        "slug": "claylo", "name": "Claylo", "category": "Landing pages",
        "url": "https://www.setproduct.com/templates/claylo",
        "summary": "claymorphism: warm cream canvas, puffy pastel clay cards, chunky 3D push buttons, Fredoka",
        "look": [
            "Claymorphism: soft, puffy surfaces with inner highlights and offset drop shadows.",
            "Warm cream canvas; pastel mint, lavender, butter and tangerine; brown ink text.",
            "Fredoka display + Plus Jakarta Sans body; chunky pill buttons that 'press' down.",
        ],
        "fonts": {"body": "Plus Jakarta Sans", "heading": "Fredoka",
                  "google": ["Plus+Jakarta+Sans:wght@400;500;600;700", "Fredoka:wght@500;600;700"]},
        "modes": ["light"],
        "base": {
            "primary": "#F49444", "accent": "#ACE4C4", "accent-contrast": "#24533B", "success": "#3FAF7A",
            "warning": "#F4DC84", "danger": "#E8604C", "info": "#C4BCF4",
            "radius-sm": "14px", "radius-md": "20px", "radius-lg": "32px", "btn-radius": "999px", "field-radius": "16px",
            "nav-item-radius": "999px", "nav-item-inset": "10px", "border-width": "2px",
            "btn-padding-y": ".75rem", "btn-padding-x": "1.5rem", "btn-font-size": ".9375rem", "btn-weight": "700",
            "btn-hot-shadow": "0 5px 0 #C9702A", "heading-tracking": "0",
        },
        "light": {"bg": "#FCF4EC", "surface": "#FFFDF9", "surface-2": "#FFF6EA", "border": "#F0DCC8",
                  "text": "#4A2A1C", "text-muted": "#8C6B5C", "highlight": "#FFEBD6",
                  "nav-bg": "#FCF4EC", "nav-text": "#74341C", "nav-active-bg": "#FFE2C4", "nav-active-text": "#74341C",
                  "field-bg": "#FFFDF9", "header-bg": "#FCF4EC"},
        "shadow": {"light": "clay"},
        "chart": ["#F49444", "#ACE4C4", "#C4BCF4", "#F4DC84", "#E8604C", "#74341C", "#3FAF7A", "#ECCCB4"],
        "recipes": [
            ("Clay cards", "Cards / Static Content regions; colour variants with CSS class `sp-clay-mint`, `sp-clay-lavender`, `sp-clay-butter`"),
            ("Chunky CTA", "Button, Hot, Template Option `Large` - press effect is automatic"),
            ("Icon tiles linked by dashes", "Cards region, Icon slot, Layout Grid 3; CSS class `sp-dashed-links` on the region"),
            ("Testimonials with stars", "Cards region + Star Rating item (read-only) or `fa-star` icons"),
        ],
        "signature": """
.t-Region, .a-CardView-item { border-width: 2px !important; }
.t-Button--hot:active { transform: translateY(4px); box-shadow: 0 1px 0 #C9702A !important; }
.t-Button:not(.t-Button--hot):not(.t-Button--noUI) { box-shadow: 0 4px 0 #E8CDB3; background: #FFFDF9; }
.sp-clay-mint { background: #DDF5E7 !important; border-color: #ACE4C4 !important; }
.sp-clay-lavender { background: #E9E5FC !important; border-color: #C4BCF4 !important; }
.sp-clay-butter { background: #FCF2C9 !important; border-color: #F4DC84 !important; }
.sp-dashed-links .a-CardView-items { background-image: linear-gradient(90deg, #E8CDB3 50%, transparent 50%); background-size: 16px 2px; background-repeat: repeat-x; background-position: 0 50%; }
""",
    },
    {
        "slug": "levitate", "name": "Levitate", "category": "Landing pages",
        "url": "https://www.setproduct.com/templates/levitate",
        "summary": "3D scene presentation style: jet-black stage, neon sky/green/violet, glassy floating panels",
        "look": [
            "Jet-black stage with floating 3D objects; neon sky blue, mint green, violet and pink.",
            "Glassy translucent panels; pill CTAs; bold display headlines.",
            "Made for covers, CTAs and presentations - pair with your own 3D renders as images.",
        ],
        "fonts": {"body": "Inter", "heading": "Sora", "google": ["Inter:wght@400;500;600", "Sora:wght@600;700;800"]},
        "modes": ["dark"],
        "base": {
            "primary": "#44BCFC", "primary-contrast": "#050505", "accent": "#14FC9C", "accent-contrast": "#050505",
            "success": "#14FC9C", "warning": "#FFC857", "danger": "#FC6CC4", "info": "#944CFC",
            "radius-sm": "10px", "radius-md": "16px", "radius-lg": "28px", "btn-radius": "999px", "field-radius": "14px",
            "nav-item-radius": "999px", "nav-item-inset": "10px",
        },
        "dark": {"bg": "#050505", "surface": "rgba(255,255,255,.04)", "surface-2": "rgba(255,255,255,.07)",
                 "border": "rgba(255,255,255,.10)", "text": "#F5F5F7", "text-muted": "#9A9AA3",
                 "highlight": "rgba(68,188,252,.12)", "nav-bg": "#0A0A0B", "header-bg": "rgba(5,5,5,.7)",
                 "nav-text": "#C8C8D0", "nav-active-bg": "rgba(68,188,252,.16)", "nav-active-text": "#FFFFFF",
                 "field-bg": "rgba(255,255,255,.05)", "login-bg": "radial-gradient(80% 60% at 50% 0%, #10233a 0%, #050505 70%)"},
        "shadow": {"dark": "glow"},
        "chart": ["#44BCFC", "#14FC9C", "#944CFC", "#FC6CC4", "#847CF4", "#FFC857", "#04144C", "#A5F3FC"],
        "recipes": [
            ("Glass panels", "Any region + CSS class `sp-glass`"),
            ("3D hero", "Hero region with Display Image = your rendered PNG (Static Application File)"),
            ("Green statement section", "Static Content + CSS class `sp-section-neon`"),
        ],
        "signature": """
.t-Region, .a-CardView-item, .t-Header { -webkit-backdrop-filter: blur(14px); backdrop-filter: blur(14px); }
.sp-glass { background: rgba(255,255,255,.05) !important; border: 1px solid rgba(255,255,255,.12) !important; -webkit-backdrop-filter: blur(18px) saturate(140%); backdrop-filter: blur(18px) saturate(140%); }
.sp-section-neon { background: var(--sp-accent) !important; color: #050505; border: 0 !important; }
.sp-section-neon .t-Region-title, .sp-section-neon .t-HeroRegion-title { color: #050505; }
""",
    },
]
