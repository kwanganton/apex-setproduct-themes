# Kit pattern -> native APEX component

Use the native component first, then Template Options, then the theme's `sp-*` CSS classes. Names are
Universal Theme 42 (APEX 23.2+ for the template components marked *TC*).

## Shell and navigation
| Kit pattern | Native APEX | Notes |
|---|---|---|
| Sidebar navigation | Navigation Menu, Position Side, *Side Navigation Menu* | Active pill/inset comes from `--sp-nav-*` tokens |
| Collapsed icon rail | Same, Template Option *Collapsed by default*; give every list entry an icon | |
| Top app bar | Page template *Standard*; Navigation Bar list for user/avatar/notifications | Colour = `--sp-header-bg` |
| Top tabs / menubar | Navigation Menu Position Top (*Top Navigation Tabs* / *Top Navigation Menu*) | |
| Breadcrumbs + page title | Breadcrumb region, template *Title Bar* | |
| Footer | Page template footer; Static Content in *Footer* position | |
| Command palette | Not native - use the *Search* region / Smart Filters, or a Popup LOV in the header | |

## Content containers
| Kit pattern | Native APEX | Notes |
|---|---|---|
| Card / panel | Region template *Standard* | Radius/shadow from tokens |
| Card without header | *Standard* + Template Option *Hidden but accessible* header | |
| KPI / stat tiles | **Cards** region (Layout Grid, N columns) or **Badge** TC | Put deltas in Badge slot |
| Gradient / coloured hero card | Static Content + theme class (`sp-kpi-gradient`, `sp-glow`, `sp-clay-*`) | |
| List items / settings rows | **Content Row** TC | |
| Feed / news | **Media List** TC | |
| Activity log | **Timeline** TC | |
| Avatars, user chips | **Avatar** TC; Cards Initials slot | |
| Accordions | Region template *Collapsible* | |
| Tabs | *Tabs Container* region, or Region Display Selector | |
| Hero / landing header | Region template *Hero* | |
| Empty state | Region "No Data Found" message + Hero-style icon | |
| Kanban (read-only) | One Cards region per column, side by side | Drag-drop needs a plug-in |

## Data
| Kit pattern | Native APEX | Notes |
|---|---|---|
| Data table (editable) | Interactive Grid | `--a-gv-*` vars |
| Data table (user reports) | Interactive Report | |
| Simple / styled table | Classic Report, template *Standard* or *Value Attribute Pairs* | |
| Filters / chips | Faceted Search, Smart Filters | Chip radius = pill |
| Charts (bar, line, area, donut, radar, funnel, gauge, bubble, polar, stock) | Chart region (Oracle JET) | Series colours via init function |
| Maps | Map region | |
| Calendar | Calendar region | |
| Tree / file explorer | Tree region | `--a-treeview-*` |
| Progress / percent | Status Meter Gauge chart; *Percent Graph* column format | |

## Forms and controls
| Kit pattern | Native APEX | Notes |
|---|---|---|
| Text inputs (label above) | Item template *Optional - Above* | Dashboard kits |
| Filled / floating inputs | Item template *Optional - Floating* | Material kits |
| Select / dropdown | Select List; Popup LOV; Combobox (24.1+, multi-value chips) | |
| Segmented control / chips | Radio Group or Checkbox Group, Template Option *Pill Button* | |
| Toggle | Switch item | |
| Date / time picker | Date Picker item (Display As Inline for calendar cards) | |
| File drop zone | File Upload, Display As *Drop Zone* | `--a-filedrop-*` |
| Rich text | Rich Text Editor | |
| Rating | Star Rating item | |
| Stepper / wizard | *Wizard Progress* list + Wizard Container region | |
| Search bar | Text Field with icon + Hot icon button; or Search region | |

## Actions and feedback
| Kit pattern | Native APEX | Notes |
|---|---|---|
| Primary button | Button template *Text*, Template Option **Hot** | `--sp-primary` |
| Secondary / outline | Template Option *Style = Simple* | |
| Ghost / text button | Template Option *Remove UI Decoration* (`t-Button--noUI`) | |
| Icon button | Button template *Icon* | |
| Button group | Template Option *Button Set* (First/Inner/Last) | |
| Dropdown menu | Menu Popup list template, or Actions menu | `--a-menu-*` |
| Modal | Modal Dialog page, or Inline Dialog region | |
| Drawer / sheet | *Drawer* page template, or Inline Drawer region | |
| Toast / snackbar | `apex.message.showPageSuccess()` | |
| Alert / callout | Region template *Alert* (Type + Style options) | Palette tokens |
| Badge / status pill | Badge TC; `u-success`/`u-danger` etc. helper classes | |
| Tooltip | Item/Button *Title* attribute | |
| Loader | `apex.util.showSpinner()`; theme `sp-thinking` for AI kits | |
| AI chat | Dynamic Action **Show AI Assistant** (24.1+); `APEX_AI` package server-side | `--a-chat-*` vars |
