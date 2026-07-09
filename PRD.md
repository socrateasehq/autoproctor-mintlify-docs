# AutoProctor Help Center — Setup & Handoff PRD

## Overview

This repo contains the AutoProctor Help Center documentation, built with [Mintlify](https://mintlify.com). It has been migrated from the original Crisp helpdesk at [helpdesk.autoproctor.co](https://helpdesk.autoproctor.co).

**GitHub repo:** `socrateasehq/autoproctor-mintlify-docs`

---

## What's Already Done

### Content Migration (Complete)
- **72 helpdesk articles** migrated from Crisp to Mintlify MDX format
- **59+ images** downloaded from Crisp CDN to local `/images/` directories
- **5 YouTube video embeds** added to relevant articles
- **AutoProctor branding** applied (logo SVGs, favicon, color scheme)

### Repo Structure
```
autoproctor-mintlify-docs/
├── docs.json                    # Mintlify configuration (nav, theme, branding)
├── index.mdx                    # Landing page with CardGroup links
├── favicon.svg                  # Blue "A" favicon
├── logo/
│   ├── light.svg                # Light-mode logo (blue "Auto" + dark "Proctor")
│   └── dark.svg                 # Dark-mode logo (light blue "Auto" + white "Proctor")
├── images/                      # All images organized by section
│   ├── getting-started/         # 3 images
│   ├── creating-tests/          # 9 images
│   ├── socratease/              # 23 images
│   ├── taking-tests/            # 6 images
│   ├── results/                 # 19 images
│   ├── candidate-issues/        # 7 images
│   └── pricing/                 # 8 images
├── getting-started/             # 8 articles
├── creating-tests/              # 6 articles
├── socratease/                  # 11 articles
├── taking-tests/                # 8 articles
├── results/                     # 17 articles
├── candidate-issues/            # 13 articles
└── pricing/                     # 9 articles
```

### Navigation (7 groups, defined in `docs.json`)
1. **Getting Started** (8 articles) — What gets tracked, device compatibility, FAQs, trust score, etc.
2. **Creating Tests** (6 articles) — Test settings, quiz providers, collaborators, archiving
3. **Socratease Quizzes** (11 articles) — Creating quizzes, question types, settings, banks, LaTeX
4. **Taking Tests** (8 articles) — Proctored/timed instructions, submit button, login/logout
5. **Results & Reports** (17 articles) — Viewing results, exports, restrictions, resuming, best practices
6. **Candidate Issues** (13 articles) — Loading screen, blank page, false violations, troubleshooting
7. **Pricing & Account** (9 articles) — Payments, teams, subscriptions, invoices, billing

---

## What You Need To Set Up

### 1. Connect the GitHub Repo to Mintlify

Mintlify auto-deploys docs when you push to the connected branch. You need to connect the repo in the Mintlify dashboard.

1. Go to [dashboard.mintlify.com](https://dashboard.mintlify.com)
2. Log in with the account that owns the `socrateasehq` organization (or create one)
3. Create a new project or connect to an existing one
4. Connect the GitHub repo: `socrateasehq/autoproctor-mintlify-docs`
5. Set the branch to `main`
6. Set the subdirectory to `/` (root)
7. Once connected, Mintlify will auto-deploy on every push to `main`

**Docs reference:** https://mintlify.com/docs/quickstart#github-repository

### 2. Configure Custom Domain (Optional)

If you want docs hosted at e.g. `docs.autoproctor.co`:

1. In the Mintlify dashboard, go to **Settings > Custom Domain**
2. Enter your desired subdomain (e.g., `docs.autoproctor.co`)
3. Add a CNAME record in your DNS provider pointing to `cname.mintlify.com`
4. Wait for DNS propagation (can take up to 48 hours, usually much faster)

**Docs reference:** https://mintlify.com/docs/settings/custom-domain

### 3. Local Development (For Previewing Changes)

To preview docs locally before pushing:

```bash
# Clone the repo
git clone https://github.com/socrateasehq/autoproctor-mintlify-docs.git
cd autoproctor-mintlify-docs

# Install and run Mintlify dev server
npx mintlify@latest dev
```

This starts a dev server at `http://localhost:3000` with hot-reload.

**Requirements:**
- Node.js 18+ (recommended: use `nvm` or `volta` to manage versions)
- No other global installs needed — `npx` handles the Mintlify CLI

### 4. Replace Placeholder Logo (Recommended)

The current logo is a simple text SVG. For a more polished look, replace with the actual AutoProctor logo:

- `logo/light.svg` — Logo for light backgrounds
- `logo/dark.svg` — Logo for dark backgrounds
- `favicon.svg` — Browser tab icon

You can export logos from Figma/Illustrator as SVG, or use a PNG/JPG by updating the file extensions in `docs.json` under the `"logo"` key.

---

## Key Configuration File: `docs.json`

This is the main Mintlify config file. Key sections:

| Section | What It Controls |
|---|---|
| `name` | Site name shown in browser tab ("AutoProctor Help Center") |
| `colors` | Primary blue (#2563EB), light (#3B82F6), dark (#1D4ED8) |
| `navigation.tabs[0].groups` | Sidebar navigation structure — all 7 groups and their pages |
| `navigation.global.anchors` | Global anchors in the sidebar (currently links to autoproctor.co) |
| `logo` | Path to light/dark logo SVGs |
| `navbar` | Top nav links (Support email, "Go to AutoProctor" button) |
| `footer.socials` | Social links (X/Twitter, LinkedIn) |

### Adding a New Article

1. Create a new `.mdx` file in the appropriate directory (e.g., `getting-started/new-article.mdx`)
2. Add frontmatter at the top:
   ```mdx
   ---
   title: "Your Article Title"
   description: "Brief description for SEO and previews."
   ---

   Your content here in markdown...
   ```
3. Add the file path to `docs.json` under the correct navigation group:
   ```json
   {
     "group": "Getting Started",
     "pages": [
       "getting-started/existing-article",
       "getting-started/new-article"    // <-- add here
     ]
   }
   ```
4. Push to `main` — Mintlify auto-deploys.

### Mintlify Components Used in the Docs

The articles use these Mintlify components (no imports needed — they're built in):

| Component | Usage |
|---|---|
| `<Frame>` | Wraps images for consistent styling |
| `<Note>` | Blue info callout box |
| `<Warning>` | Yellow/orange warning callout box |
| `<Steps>` + `<Step>` | Numbered step-by-step instructions |
| `<CardGroup>` + `<Card>` | Grid of clickable cards (used on landing page) |
| `<AccordionGroup>` + `<Accordion>` | Expandable FAQ-style sections |
| `<iframe>` | YouTube video embeds |

**Full component reference:** https://mintlify.com/docs/components

---

## Known Remaining Items

### Must Do
- [ ] **Connect repo to Mintlify dashboard** — docs won't auto-deploy until this is done
- [ ] **Verify all images render** — spot-check articles in each section after deploy
- [ ] **Verify YouTube embeds play** — check `creating-tests/quiz-providers`, `socratease/creating-a-quiz`, `taking-tests/proctored-socratease-instructions`, `taking-tests/timed-socratease-instructions`

### Nice To Have
- [ ] **Replace text logo SVGs** with actual AutoProctor brand logo
- [ ] **Set up custom domain** (e.g., `docs.autoproctor.co`)
- [ ] **Add analytics** — Mintlify supports PostHog, Google Analytics, etc. via `docs.json` `analytics` key
- [ ] **Add search** — Mintlify provides built-in search, but you can also configure Algolia
- [ ] **Review social links** in footer — verify X and LinkedIn URLs in `docs.json` are correct
- [ ] **Add OpenGraph/meta images** — for better social media previews when docs links are shared
- [ ] **Remove `download-socratease-images.sh`** — leftover script from migration, not needed

### Content Improvements (Optional)
- [ ] Review all 72 articles for accuracy against current AutoProctor product
- [ ] Add more cross-links between related articles
- [ ] Consider adding a "What's New" / changelog section
- [ ] Add screenshots of the latest AutoProctor UI where images are outdated

---

## Useful Links

| Resource | URL |
|---|---|
| GitHub Repo | https://github.com/socrateasehq/autoproctor-mintlify-docs |
| Mintlify Docs | https://mintlify.com/docs |
| Mintlify Dashboard | https://dashboard.mintlify.com |
| Mintlify Components | https://mintlify.com/docs/components |
| Original Crisp Helpdesk | https://helpdesk.autoproctor.co |
| AutoProctor | https://www.autoproctor.co |

---

## Contacts

- **Support email** (configured in navbar): support@autoproctor.co
- **Mintlify support**: https://mintlify.com/docs/support
