# AutoProctor Help Center — Article Style Guide

## 10 Principles for Every Article

1. **TL;DR only when it earns its place** — Add a `<Tip>` at the top only when the article is detailed and the title poses a question worth answering upfront. The TL;DR lets the reader decide whether to read further. Skip it for straightforward how-to or settings pages where the title already says enough.

2. **One visual element per section** — Every H2 section must contain at least one non-text element: screenshot, video, table, callout, or code block. Never let more than 3-4 paragraphs stack without a visual break.

3. **Bold the key terms** — Within body text, bold the critical concept or feature name on first mention. This makes skimming possible ("If you want to show only a **subset** of questions...").

4. **Short paragraphs (3 sentences max)** — Break long paragraphs. Each paragraph expresses one idea. Critical for a global audience where English may not be the first language.

5. **Use callouts for intent, not decoration** — `<Tip>` = summary/shortcut, `<Note>` = supplementary context, `<Warning>` = things that can go wrong. Each callout type has a specific purpose.

6. **Tables for comparisons, not prose** — Whenever comparing 2+ options, features, or plans, use a table. Never describe comparisons in paragraph form.

7. **Steps for procedures, prose for concepts** — Use `<Steps>` for sequences of actions. Use prose paragraphs for explaining why something works. Don't mix the two.

8. **H2 for major sections, H3 for sub-topics** — H2 headings are scannable section labels (nouns or short phrases). H3 subdivides within an H2. Never skip from H2 to H4.

9. **Related Resources are an appendix** — The Related Resources section at the bottom is navigation, not content. It is visually demarcated with a border and muted styling via CSS.

10. **Front-load the action** — The first H2 should be the primary thing the user came to do. Conceptual background comes after. People searching help docs want to do something, not learn theory first.

## Image & Video Sizing

The `<Frame>` container shrinks to wrap the image (`width: fit-content`) and is centered in the content area. Images default to **70% of content-area width** via CSS (`custom.css`) using container query units (`cqi`).

- **Default (no action needed):** Images render at `70cqi` (70% of `#content-area` width). The frame wraps tightly with its padding/background.
- **Override per image:** Add an inline `style` with a `cqi` value. Use `cqi` (not `%`) so the size is always relative to the content area, not the fit-content parent:
  ```jsx
  <img style={{maxWidth: "56cqi"}} src="/images/..." alt="..." />
  ```
- **Sizing by information density:** Choose size based on how much detail the reader needs to parse:

  | Density | Examples | Size |
  |---|---|---|
  | Low | Single button, icon, simple dialog, toggle | `40cqi`–`50cqi` |
  | Medium | Settings panel, form, single dashboard card | `56cqi` |
  | High (default) | Full-page screenshot, multi-column layout, table-heavy UI | `70cqi` |
  | Very high | Dense data table, side-by-side comparison, wide workflow | `80cqi`–`90cqi` |

  The test: if the reader would need to squint or zoom to read text in the image, size up.

- **Videos and iframes:** YouTube embeds and other iframes inside `<Frame>` default to `70cqi` via CSS. No inline override needed. Iframes outside a `<Frame>` should use `className="w-full aspect-video"`.
- Images should always have `alt` text for accessibility.

## URL Structure

URLs follow the navigation hierarchy: `/section/subsection/article-slug`. The folder structure IS the URL — renaming a folder changes all URLs under it. `docs.json` references must match file paths.

## Multilingual

All articles exist in 3 languages: EN (root), ES (`es/`), PT (`pt/`). Changes to structure or content should be applied to all 3.

## Mintlify Components

- `<Tip>` — Green callout for TL;DR and shortcuts
- `<Note>` — Blue callout for supplementary context
- `<Warning>` — Yellow/red callout for things that can go wrong
- `<Steps>` / `<Step>` — Numbered procedure steps
- `<Frame>` — Image/video container with optional caption
- `<CardGroup>` / `<Card>` — Grid of linked cards (used on homepage)

## Writing Conventions

- **No em-dashes.** Use a single hyphen `-` instead of `—` (em-dash) or `--` (double hyphen) everywhere: prose, callouts, list items, Related Resources. Mintlify renders `--` as an em-dash, which looks like AI-generated text. A single `-` stays as-is.

## Product Context

- AutoProctor is an AI proctoring platform. Users bring their own quiz (Google Forms, Microsoft Forms, etc.) or use AutoProctor's native quiz tool (Socratease).
- Two quiz paths: (1) Socratease — questions configured inside AutoProctor, (2) External providers — questions stay on that platform, AutoProctor only adds proctoring.
- Four user roles: test creator, candidate (test taker), learner (understanding AutoProctor), admin (pricing/billing).
- Global audience: students in developing countries through professors at elite institutions. Simple, clear language.
