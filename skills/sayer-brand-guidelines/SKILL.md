---
name: sayer-brand-guidelines
description: "Applies Sayer's official brand — colors, typography, logo, visual identity — to any document, presentation, spreadsheet, PDF, artifact, or web component going to a client or representing Sayer externally. Trigger on brand-specific phrases — 'apply Sayer branding', 'format per brand guidelines', 'brand-check this [artifact]', 'Sayer-branded [artifact]', 'on-brand [artifact]', or any mention of Sayer alongside a document/file type. Read this skill BEFORE generating any client-facing deliverable. Legal documents and contracts require the legal name 'Sayer Strategy Group' — this skill covers when and where to use it."
allowed-tools: Read, Grep, Glob, mcp__claude_ai_Google_Drive__get_file_metadata, mcp__claude_ai_Google_Drive__download_file_content, mcp__claude_ai_Google_Drive__read_file_content, mcp__claude_ai_Google_Drive__search_files
---

# Sayer Brand Guidelines

> Read this skill before generating any client-facing document. For Excel scoping
> workbooks, the canonical implementation of these specs is `scripts/brand_styles.py`
> at the repo root — import styles from there; never hard-code hex values in
> generator scripts.

## Overview

**Brand name:** Sayer
**Legal name:** Sayer Strategy Group

Use "Sayer" everywhere — documents, presentations, proposals, client comms, email signatures.
Use "Sayer Strategy Group" only in formal legal contexts: contracts, MSAs, SOWs, invoices, signature blocks, and any document that requires the full legal entity name.

**Tagline:** "Zero In → Move Fast → Win Big"

Sayer is an AI-native consulting firm. The brand identity is bold, modern, and confident — built around a striking yellow-and-black palette with clean typography. All work products should reflect this identity consistently.

---

## Brand Colors

### Primary Palette

| Role | Color Name | Hex | RGB | Usage |
|------|-----------|-----|-----|-------|
| **Primary Accent** | Yellow | `#FEC700` | (254, 199, 0) | Primary brand color. Headlines, accents, highlights, call-to-action elements, chart emphasis. Pantone Yellow 012 C. |
| **Primary Dark** | Black | `#000000` | (0, 0, 0) | Primary text on light backgrounds, dark backgrounds for slides/covers |
| **Light Neutral** | Cool Grey | `#D6D6D6` | (214, 214, 214) | Light backgrounds, subtle dividers, secondary elements |

### Extended Grey Scale

| Color Name | Hex | RGB | Usage |
|-----------|-----|-----|-------|
| Grey 700 | `#2E2E2E` | (46, 46, 46) | Dark backgrounds (alternative to pure black), dark text |
| Grey 600 | `#7E7E7E` | (126, 126, 126) | Secondary text, captions, metadata |
| Grey 500 | `#BCBCBC` | (188, 188, 188) | Borders, dividers, inactive elements |
| Grey 300 | `#E3E3E3` | (227, 227, 227) | Light fills, table alternating rows |

### Color Application Rules

- **Dark-on-light:** Black text (#000000) on white or light grey backgrounds. Yellow for accents only.
- **Light-on-dark:** White text (#FFFFFF) on black or Grey 700 backgrounds. Yellow for accents, logo, highlights.
- **Yellow is NEVER used for body text** — only for headlines, accents, decorative elements, and emphasis.
- **Charts and data viz:** Yellow as primary data color, greys for secondary series. No non-brand colors.
- **Tables:** Grey 300 (#E3E3E3) for alternating row fills. Yellow (#FEC700) for header row backgrounds with black text.

---

## Typography

### Font Family: Rethink Sans (Google Font)

| Role | Weight | Size Guidance | Usage |
|------|--------|---------------|-------|
| **Headlines / H1** | Semibold (600) | 24–36pt (presentations), 18–24pt (documents) | Page titles, section headers, slide titles |
| **Subheadings / H2–H3** | Semibold (600) | 16–20pt (presentations), 14–16pt (documents) | Subsections, card titles |
| **Body Text** | Regular (400) | 14–18pt (presentations), 11–12pt (documents) | Paragraphs, descriptions, content |
| **Captions / Small** | Regular (400) | 10–12pt (presentations), 9–10pt (documents) | Footnotes, metadata, labels |
| **Footers / Notes** | Regular Italic (400) | 9–11pt | Footer lines, notes, disclaimers |

### Font Fallbacks

1. **Rethink Sans** (preferred — install from Google Fonts)
2. **Calibri** (common system font, similar feel)
3. **Arial** (universal fallback)

### Typography Rules

- Headlines use Semibold — never bold body text for headlines
- Body text: 1.3–1.5 line spacing
- Left-aligned paragraphs (not justified)
- Sentence case for headlines — not ALL CAPS (except "SAYER" in specific logo contexts)
- Footers and notes use Regular Italic

---

## Logo

### Decision Rule

1. **Background:** Light surface → `-light-` variant. Dark surface → `-dark-` variant.
2. **Layout:** Wide/narrow strip → `horizontal`. Square/tall → `stacked`. Tiny → `mark`.
3. **Color:** Default `fullcolor`. Use `mono` only for print/B&W.

### Logo Asset Index

Read `references/logo-assets.md` (in this skill's directory) for the full Drive ID table. Use the Decision Rule above to select the variant, then fetch by Drive ID via the Google Drive connector.

### Logo Rules (Do NOT Violate)
- Never distort or stretch the logo
- Never change the size relationship between the logomark and wordmark
- Never rotate the logo
- Never use non-approved colors on the logo
- Never outline the logo
- Maintain clear space around the logo (minimum: half the height of the logomark)

---

## Visual Style

### Illustration Style
- **Source:** "Simple Lines" by Alisa Krasnikova (Exactly)
- **Style:** Hand-drawn black line illustrations with minimal detail
- **Themes:** Growth (rockets, charts), Partnership (handshakes), Strategy (puzzle pieces, paths)
- **Usage:** Presentations, proposals — adds approachable, human feel to professional content

### Decorative Elements
- **Yellow dot pattern:** A row/arc of yellow dots used as a decorative border element
- **Usage:** Sparingly — covers and dividers only, not on every page

### Slide/Page Design Patterns

**Cover slides / Title pages:**
- Black or Grey 700 background
- Sayer logo top-left (`sayer-stacked-dark-fullcolor` or `sayer-horizontal-dark-fullcolor`)
- Title in white, subtitle or client name in Yellow (#FEC700)
- Optional: yellow dot pattern as decorative element

**Content slides / Interior pages:**
- White background with black text (default)
- OR Yellow background with black text (emphasis/callout slides)
- OR Black background with white text (data/stats emphasis)
- Small logomark top-right on every interior page (`sayer-mark-light-mono.png` on white slides)

**Data/Stats callout:**
- Large number in black on yellow background
- Supporting text below in regular weight

---

## Format-Specific Application

Apply these brand overrides in whatever tool generates the document:

**Word Documents (docx):** Calibri 11pt (Rethink Sans does not survive Google Docs conversion). H1: Semibold 18pt. H2: 14pt. Body: 1.4 line spacing. Accent lines: Yellow 2pt. Tables: Yellow headers, Grey 300 alt rows. Header logo: horizontal-light-fullcolor (Drive ID `1a7ORUfK2ERRFlnUusmYxTLl4-u64sSqo`). Page numbers: Grey 600, bottom right. Legal docs: use "Sayer Strategy Group" in entity/signature fields.

**Presentations (pptx / Gamma):** Gamma: specify Yellow/Black/grey palette, dark cover, white content slides. Cover: stacked-dark-fullcolor (ID `124V8-Zt6L5ZS7NrcErvKQGNyIxv0ai5v`). Interior: mark-light-mono top-right (ID `1rwnPQyYeQ3KjQGZXhTrrwSsZWqXmr1zf`).

**Spreadsheets (xlsx):** Yellow header rows, Grey 300 alt rows, Grey 500 thin borders. Title: Semibold 14pt. Charts: Yellow primary, greys secondary. Freeze header row. Implementation: import styles from `scripts/brand_styles.py` — see `skills/scope-project/references/excel-formatting.md`.

**PDFs:** Same rules as docx. Cover: Black/Grey 700 bg, white title, yellow subtitle.

**React/HTML:** SVG logo assets should be requested from the operator or generated inline if needed. Font stack: `'Rethink Sans', Calibri, Arial, sans-serif`.
```css
@import url('https://fonts.googleapis.com/css2?family=Rethink+Sans:wght@400;600&display=swap');
--sayer-yellow: #FEC700;
--sayer-black: #000000;
--sayer-grey-700: #2E2E2E;
--sayer-grey-600: #7E7E7E;
--sayer-grey-500: #BCBCBC;
--sayer-grey-300: #E3E3E3;
--sayer-cool-grey: #D6D6D6;
```

---

## Voice & Tone

This skill covers visual identity only — colors, typography, logo, layout.

---

## Quick Reference

```
BRAND NAME:   Sayer
LEGAL NAME:   Sayer Strategy Group (contracts, MSAs, invoices, signature blocks)
TAGLINE:      "Zero In → Move Fast → Win Big"

YELLOW:       #FEC700  — Accents, highlights, headers, charts
BLACK:        #000000  — Primary text, dark backgrounds
GREY 700:     #2E2E2E  — Alt dark backgrounds
GREY 600:     #7E7E7E  — Secondary text
GREY 500:     #BCBCBC  — Borders, dividers
GREY 300:     #E3E3E3  — Light fills, alt rows
COOL GREY:    #D6D6D6  — Light backgrounds

FONT:         Rethink Sans (Google Font)
HEADLINES:    Semibold (600)
BODY:         Regular (400)
NOTES:        Regular Italic (400)
FALLBACK:     Calibri → Arial

LOGO:         Pick by background (light/dark) → layout (horizontal/stacked/mark) → fullcolor default
ASSETS:       Google Drive → Sayer shared drive → sayer-claude-assets/logos/
```

---

## How This Skill Is Used

Pure reference skill — no automatic writes, no data capture, no system mutations.

- **Read by:** `scope-project` (Excel workbooks via `scripts/brand_styles.py`), proposal and SOW generation, and any task producing a client-facing deliverable from this repo.
- **Drift rule:** if this skill and `scripts/brand_styles.py` ever disagree on a hex value or font, fix both in the same commit — `brand_styles.py` is the executable copy of this spec.
