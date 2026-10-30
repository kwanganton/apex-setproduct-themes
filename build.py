"""Generate every theme skill from src/themes.py + src/base.css.

    python build.py

Writes, for each theme:
  skills/apex-theme-<slug>/SKILL.md
  skills/apex-theme-<slug>/theme-<mode>.css   (self-contained: fonts + tokens + base + signature)
and refreshes:
  skills/apex-setproduct-themes/assets/base.css
  the theme tables in skills/apex-setproduct-themes/SKILL.md and README.md
  docs/index.html  (swatch gallery, GitHub Pages ready)
"""
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from themes import THEMES  # noqa: E402

SKILLS = ROOT / "skills"
CORE = SKILLS / "apex-setproduct-themes"
BASE_CSS = (ROOT / "src" / "base.css").read_text(encoding="utf-8")

SHADOWS = {
    "soft": ("0 1px 2px rgba(16,24,40,.05), 0 1px 3px rgba(16,24,40,.07)",
             "0 4px 12px rgba(16,24,40,.08)",
             "0 16px 40px rgba(16,24,40,.12)"),
    "flat": ("none", "0 1px 2px rgba(0,0,0,.08)", "0 8px 24px rgba(0,0,0,.12)"),
    "tinted": ("0 2px 8px color-mix(in srgb, var(--sp-primary) 8%, transparent)",
               "0 8px 24px color-mix(in srgb, var(--sp-primary) 12%, transparent)",
               "0 24px 48px color-mix(in srgb, var(--sp-primary) 16%, transparent)"),
    "elevated": ("0 1px 3px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.24)",
                 "0 3px 6px rgba(0,0,0,.16), 0 3px 6px rgba(0,0,0,.23)",
                 "0 10px 20px rgba(0,0,0,.19), 0 6px 6px rgba(0,0,0,.23)"),
    "dark": ("0 1px 2px rgba(0,0,0,.5)", "0 6px 18px rgba(0,0,0,.45)", "0 20px 50px rgba(0,0,0,.6)"),
    "glow": ("0 0 0 1px rgba(255,255,255,.03)",
             "0 8px 24px rgba(0,0,0,.45)",
             "0 24px 60px rgba(0,0,0,.55), 0 0 48px color-mix(in srgb, var(--sp-primary) 18%, transparent)"),
    "clay": ("6px 6px 0 rgba(116,52,28,.10), inset -3px -3px 0 rgba(0,0,0,.04), inset 3px 3px 0 rgba(255,255,255,.75)",
             "10px 10px 0 rgba(116,52,28,.12), inset -4px -4px 0 rgba(0,0,0,.05), inset 4px 4px 0 rgba(255,255,255,.8)",
             "16px 16px 0 rgba(116,52,28,.14), inset -5px -5px 0 rgba(0,0,0,.05), inset 5px 5px 0 rgba(255,255,255,.8)"),
}

# Tokens a theme may leave out; values are CSS so they follow the other tokens.
DEFAULTS = {
    "primary-contrast": "#FFFFFF",
    "primary-shade": "color-mix(in srgb, var(--sp-primary) 14%, transparent)",
    "accent-contrast": "#FFFFFF",
    "accent-shade": "color-mix(in srgb, var(--sp-accent) 16%, transparent)",
    "surface-2": "color-mix(in srgb, var(--sp-text) 3%, var(--sp-surface))",
    "highlight": "color-mix(in srgb, var(--sp-primary) 10%, var(--sp-surface))",
    "field-bg": "var(--sp-surface)",
    "field-border": "var(--sp-border)",
    "header-bg": "var(--sp-surface)",
    "header-text": "var(--sp-text)",
    "nav-bg": "var(--sp-surface)",
    "nav-text": "var(--sp-text-muted)",
    "nav-hover-bg": "color-mix(in srgb, var(--sp-nav-active-text) 8%, transparent)",
    "nav-active-bg": "color-mix(in srgb, var(--sp-primary) 12%, var(--sp-nav-bg))",
    "nav-active-text": "var(--sp-primary)",
    "radius-pill": "999px",
}

TOKEN_ORDER = [
    "font", "font-heading",
    "primary", "primary-contrast", "primary-shade", "accent", "accent-contrast", "accent-shade",
    "success", "warning", "danger", "info",
    "bg", "surface", "surface-2", "border", "text", "text-muted", "highlight",
    "field-bg", "field-border", "header-bg", "header-text", "header-shadow",
    "nav-bg", "nav-text", "nav-border", "nav-hover-bg", "nav-active-bg", "nav-active-text",
    "nav-item-radius", "nav-item-inset", "login-bg",
    "radius-sm", "radius-md", "radius-lg", "radius-pill", "btn-radius", "field-radius", "border-width",
    "btn-padding-y", "btn-padding-x", "btn-font-size", "btn-weight", "btn-transform", "btn-hot-shadow", "btn-hot-bg",
    "weight-semibold", "heading-tracking",
    "shadow-sm", "shadow-md", "shadow-lg",
]

SYSTEM_STACK = 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif'


def font_value(name):
    if "," in name:
        return f"{name}, {SYSTEM_STACK}"
    return f'"{name}", {SYSTEM_STACK}'


def tokens_for(theme, mode):
    t = dict(DEFAULTS)
    t.update(theme["base"])
    t.update(theme[mode])
    t["font"] = font_value(theme["fonts"]["body"])
    t["font-heading"] = font_value(theme["fonts"]["heading"])
    sm, md, lg = SHADOWS[theme["shadow"][mode]]
    t.setdefault("shadow-sm", sm)
    t.setdefault("shadow-md", md)
    t.setdefault("shadow-lg", lg)
    missing = [k for k in ("primary", "accent", "bg", "surface", "border", "text", "text-muted") if k not in t]
    if missing:
        raise SystemExit(f"{theme['slug']}/{mode}: missing tokens {missing}")
    ordered = [k for k in TOKEN_ORDER if k in t] + sorted(k for k in t if k not in TOKEN_ORDER)
    return [(k, t[k]) for k in ordered]


def google_import(theme):
    fams = "&".join(f"family={f}" for f in theme["fonts"]["google"])
    return f"https://fonts.googleapis.com/css2?{fams}&display=swap"


def css_for(theme, mode):
    toks = tokens_for(theme, mode)
    lines = [
        f"@import url(\"{google_import(theme)}\");",
        "/* " + "=" * 74,
        f"   Setproduct {theme['name']} for Oracle APEX - {mode} mode",
        f"   Kit: {theme['url']}",
        f"   Base Theme Style: {'Vita - Dark' if mode == 'dark' else 'Vita'}   (generated by build.py - edit src/, not this file)",
        "   " + "=" * 74 + " */",
        "",
        ":root {",
    ]
    if mode == "dark":
        lines.append("  color-scheme: dark;")
    lines += [f"  --sp-{k}: {v};" for k, v in toks]
    lines += ["}", "", BASE_CSS.strip(), ""]
    sig = theme.get("signature", "").strip()
    if sig:
        lines += ["/* ---- " + theme["name"] + " signature utilities (add via CSS Classes) ---- */", sig, ""]
    return "\n".join(lines)


def chart_js(theme):
    colors = ", ".join(f'"{c}"' for c in theme["chart"])
    return (
        "function( options ) {\n"
        "    options.styleDefaults = options.styleDefaults || {};\n"
        f"    options.styleDefaults.colors = [ {colors} ];\n"
        "    return options;\n"
        "}"
    )


def skill_md(theme):
    slug, name = theme["slug"], theme["name"]
    modes = theme["modes"]
    default = modes[0]
    toks = dict(tokens_for(theme, default))
    files = "\n".join(
        f"- `theme-{m}.css` - {m} mode; create the Theme Style from **{'Vita - Dark' if m == 'dark' else 'Vita'}**"
        + (" (default)" if m == default else "")
        for m in modes
    )
    swatches = "\n".join(
        f"| `--sp-{k}` | `{toks[k]}` |"
        for k in ("primary", "accent", "success", "warning", "danger", "info", "bg", "surface", "border",
                  "text", "text-muted", "nav-bg", "nav-active-bg", "radius-md", "radius-lg", "btn-radius")
        if k in toks
    )
    look = "\n".join(f"- {x}" for x in theme["look"])
    recipes = "\n".join(f"| {a} | {b} |" for a, b in theme["recipes"])
    sig_classes = sorted(set(re.findall(r"\.(sp-[a-z0-9-]+)", theme.get("signature", ""))))
    sig = ", ".join(f"`{c}`" for c in sig_classes) if sig_classes else "none - the base layer covers this kit"
    dark_note = (
        "Both modes ship. Create one Theme Style per mode, mark both **Is Public = Yes**, and in "
        "Shared Components > User Interface Attributes enable end users to choose the theme style, so users can switch "
        "from the runtime *Customize* dialog (see `references/install.md` step 3)."
        if len(modes) > 1 else
        f"This kit is {default}-only; no second style is needed."
    )
    return f"""---
name: apex-theme-{slug}
description: Restyle an Oracle APEX app to look like the Setproduct {name} kit ({theme['summary']}) using native Universal Theme components plus a drop-in CSS file. Use when the user asks for the {name} theme/look/style in APEX, or picks it from the apex-setproduct-themes catalog.
---

# Setproduct {name} -> Oracle APEX

**Category:** {theme['category']}  |  **Kit:** {theme['url']}  |  **Modes:** {', '.join(modes)} (default {default})

Read `../apex-setproduct-themes/SKILL.md` first for the shared method (native-first rules, install steps,
component map). This file only holds what is specific to {name}.

## The look
{look}

**Fonts:** body `{theme['fonts']['body']}`, headings `{theme['fonts']['heading']}` (loaded from Google Fonts by the CSS `@import`;
self-host them as Static Application Files if the app's CSP blocks fonts.googleapis.com).

## Files
{files}

Each file is self-contained (font import + `--sp-*` tokens + base bridge + {name} signature rules).

## Key tokens ({default})
| Token | Value |
|---|---|
{swatches}

To re-tint, change tokens in `src/themes.py` and run `python build.py` - or override just the `--sp-*`
variables in Theme Roller's **Custom CSS** box, which loads after the file.

## Build it with native components
| Kit element | Native APEX implementation |
|---|---|
{recipes}

Everything else follows the shared component map (`../apex-setproduct-themes/references/component-map.md`).

**Signature utility classes** (put in a region's or item's *Appearance > CSS Classes*): {sig}

## Charts
Paste into each Chart region's **Attributes > Advanced > Initialization JavaScript Function**:

```javascript
{chart_js(theme)}
```

## Dark / light
{dark_note}

## Verify
1. Run a page with a Side Menu, a Cards region, an Interactive Report, a form with Floating labels and a Hot button.
2. Check the side menu's current item, focus rings (Tab key), Hot button contrast, and the IR header in both modes.
3. Check the Login page (page template *Login*) and a Modal Dialog.
4. Compare side by side with the kit preview at {theme['url']} and nudge tokens, not selectors.
"""


def theme_table(link_prefix):
    rows = ["| Theme | Category | Modes | Look |", "|---|---|---|---|"]
    for t in THEMES:
        rows.append(
            f"| [{t['name']}]({link_prefix}apex-theme-{t['slug']}/SKILL.md) | {t['category']} | "
            f"{', '.join(t['modes'])} | {t['summary']} |"
        )
    return "\n".join(rows)


def replace_block(path, body):
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- THEMES:START -->\n).*?(\n<!-- THEMES:END -->)",
                 lambda m: m.group(1) + body + m.group(2), text, flags=re.S)
    path.write_text(new, encoding="utf-8")


def gallery():
    cards = []
    for t in THEMES:
        m = t["modes"][0]
        tk = dict(tokens_for(t, m))
        chips = "".join(f'<span style="background:{c}" title="{c}"></span>' for c in t["chart"])
        style = "; ".join(f"--sp-{k}: {v}" for k, v in tk.items())
        cards.append(f"""
<article class="card" style="{html.escape(style)}">
  <div class="mock">
    <aside><i></i><i class="on"></i><i></i><i></i></aside>
    <main>
      <div class="panel"><b>Revenue</b><strong>$42,180</strong><div class="chips">{chips}</div></div>
      <div class="row"><button class="hot">Primary</button><button>Secondary</button></div>
    </main>
  </div>
  <h2>{html.escape(t['name'])}</h2>
  <p>{html.escape(t['summary'])}</p>
  <small>{html.escape(t['category'])} &middot; {', '.join(t['modes'])} &middot; <a href="{t['url']}">kit</a></small>
</article>""")
    fonts = sorted({f for t in THEMES for f in t["fonts"]["google"]})
    font_url = "https://fonts.googleapis.com/css2?" + "&".join(f"family={f}" for f in fonts) + "&display=swap"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>APEX Setproduct Themes</title>
<link rel="stylesheet" href="{font_url}">
<style>
:root {{ --page:#f6f6f8; --ink:#16161d; --muted:#6b6b7b; --line:#e4e4ea; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --page:#101014; --ink:#f1f1f5; --muted:#a0a0ad; --line:#2a2a33; }} }}
:root[data-theme="dark"] {{ --page:#101014; --ink:#f1f1f5; --muted:#a0a0ad; --line:#2a2a33; }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--page); color:var(--ink); font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; }}
header {{ max-width:1200px; margin:0 auto; padding:40px 16px 8px }}
header h1 {{ margin:0 0 6px; font-size:28px; letter-spacing:-.02em }}
header p {{ margin:0; color:var(--muted) }}
.grid {{ max-width:1200px; margin:0 auto; padding:24px 16px 64px; display:grid; gap:20px; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)) }}
.card {{ border:1px solid var(--line); border-radius:14px; padding:12px; background:var(--page) }}
.card h2 {{ margin:12px 4px 2px; font-size:17px }} .card p {{ margin:0 4px 6px; color:var(--muted); font-size:13px }}
.card small {{ margin:0 4px; color:var(--muted); font-size:12px }} .card a {{ color:inherit }}
.mock {{ display:flex; height:170px; border-radius:10px; overflow:hidden; background:var(--sp-bg); font-family:var(--sp-font); color:var(--sp-text); border:1px solid var(--sp-border) }}
.mock aside {{ width:52px; background:var(--sp-nav-bg); padding:10px 8px; display:flex; flex-direction:column; gap:7px }}
.mock aside i {{ height:9px; border-radius:var(--sp-nav-item-radius,4px); background:color-mix(in srgb,var(--sp-nav-text) 35%,transparent) }}
.mock aside i.on {{ background:var(--sp-nav-active-bg); outline:1px solid color-mix(in srgb,var(--sp-nav-active-text) 40%,transparent) }}
.mock main {{ flex:1; padding:10px; display:flex; flex-direction:column; gap:9px }}
.panel {{ background:var(--sp-surface); border:1px solid var(--sp-border); border-radius:var(--sp-radius-lg); box-shadow:var(--sp-shadow-sm); padding:10px }}
.panel b {{ display:block; font-size:11px; color:var(--sp-text-muted); font-weight:500 }}
.panel strong {{ font-family:var(--sp-font-heading); font-size:20px; letter-spacing:-.02em }}
.chips {{ display:flex; gap:3px; margin-top:6px }} .chips span {{ flex:1; height:16px; border-radius:3px }}
.row {{ display:flex; gap:6px }}
.row button {{ font:600 11px var(--sp-font); padding:6px 10px; border-radius:var(--sp-btn-radius); border:1px solid var(--sp-border); background:var(--sp-surface); color:var(--sp-text); text-transform:var(--sp-btn-transform,none) }}
.row button.hot {{ background:var(--sp-primary); color:var(--sp-primary-contrast); border-color:transparent; box-shadow:var(--sp-btn-hot-shadow,none) }}
</style></head>
<body><header><h1>APEX Setproduct Themes</h1>
<p>{len(THEMES)} Setproduct kits translated to Oracle APEX Universal Theme. Each card renders that theme's real tokens.</p></header>
<section class="grid">{''.join(cards)}
</section></body></html>
"""


def main():
    CORE.joinpath("assets").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "src" / "base.css", CORE / "assets" / "base.css")
    for t in THEMES:
        d = SKILLS / f"apex-theme-{t['slug']}"
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("theme-*.css"):
            old.unlink()
        for m in t["modes"]:
            (d / f"theme-{m}.css").write_text(css_for(t, m), encoding="utf-8")
        (d / "SKILL.md").write_text(skill_md(t), encoding="utf-8")
    replace_block(CORE / "SKILL.md", theme_table("../"))
    replace_block(ROOT / "README.md", theme_table("skills/"))
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(gallery(), encoding="utf-8")
    print(f"built {len(THEMES)} themes")


if __name__ == "__main__":
    main()
