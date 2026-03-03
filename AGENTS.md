# AutoProctor Help Center — Documentation Standards

## About this project

- This is the AutoProctor Help Center, built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Run `npx mintlify@latest dev` to preview locally
- Run `npx mintlify@latest broken-links` to check links
- Mintlify auto-generates `/llms.txt` and `/llms-full.txt` for AI ingestion on deployment

## Terminology

- Use **"candidates"** for people taking tests (not "students", "test-takers", or "users")
- Use **"test creators"** or **"administrators"** for people setting up tests
- Use **"quiz"** only when referring to Socratease quizzes; use **"test"** for everything else
- Use **"AutoProctor"** (never "Auto Proctor" or "autoproctor")
- Use **"Trust Score"** (capitalized as a product name)
- Use **"credits"** when referring to billing units (not "attempts")
- Use **"Socratease"** (capitalized, one word)

## Style preferences

- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**, select **Create Test**
- Code formatting for file names, commands, paths, and code references
- Short paragraphs (1-3 sentences maximum)
- Action-oriented imperatives in procedures: "Click", "Select", "Enable"

## Article template

Every article should follow this structure:

1. **Frontmatter**: `title` (50-60 chars) + `description` (150-160 chars)
2. **Intro paragraph**: 1-2 sentences providing context
3. **Note/Warning** (if applicable): Feature availability or critical caveats
4. **Main content**: H2 sections, H3 subsections, sequential heading hierarchy
5. **Related Resources**: Internal links to related articles at the bottom

## Component rules

- Wrap ALL images in `<Frame>` — no bare `<img>` tags
- Use `<Steps>` for any procedural/how-to content
- Use `<Note>` for supplementary information and tips
- Use `<Warning>` for critical caveats (max 1-2 per article, never duplicate)
- Use `<AccordionGroup>` for FAQ-style content
- Use `<CardGroup>` for feature comparisons and navigation grids

## Content boundaries

- Document features available to test creators and candidates
- Do not document internal admin or engineering features
- Do not include pricing dollar amounts (link to the pricing page instead)
- Keep troubleshooting articles focused: Problem, Why, Fix, Related Resources
