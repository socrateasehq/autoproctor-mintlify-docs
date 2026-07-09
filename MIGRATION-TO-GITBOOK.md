# Mintlify → GitBook Migration Guide

This document contains everything needed to migrate the AutoProctor Help Center from Mintlify to GitBook. The site has ~75 articles × 3 languages (EN, ES, PT) = ~225 MDX files.

---

## Current Architecture

### File Structure
```
autoproctor-mintlify-docs/
├── docs.json                    # Navigation, redirects, theme, analytics config
├── custom.css                   # 123 lines of CSS overrides
├── custom.js                    # 137 lines — language selector widget
├── index.mdx                    # EN homepage
├── CLAUDE.md                    # Article style guide (keep for reference, do not migrate)
├── images/                      # Shared image assets
├── videos/                      # Shared video assets
├── tests-results/
│   ├── create/                  # 12 articles
│   ├── results/                 # 7 articles
│   ├── access-limits/           # 6 articles
│   └── issues/                  # 13 articles
├── candidate-guide/
│   └── attempting/              # 7 articles
├── understanding/
│   ├── getting-started/         # 4 articles
│   └── how-proctoring-works/    # 3 articles
├── socratease/
│   ├── create-questions/        # 6 articles
│   └── settings/                # 5 articles
├── pricing-account/
│   ├── plans-credits/           # 5 articles
│   ├── billing-teams/           # 5 articles
│   └── support/                 # 2 articles
├── es/                          # Spanish — mirrors the EN structure above
└── pt/                          # Portuguese — mirrors the EN structure above
```

### Key Config Files
- **`docs.json`** (~656 lines): Navigation tree for EN/ES/PT, 90 redirect rules, theme colors, logos, fonts, analytics IDs, SEO metadata, footer links.
- **`custom.css`** (123 lines): Content area widening, container query image sizing (`cqi` units), `<Frame>` shrink-wrapping (`width: fit-content`), H3 left-border indentation, Related Resources section styling, sidebar logo sizing, Mintlify branding removal.
- **`custom.js`** (137 lines): Custom language selector (globe icon + dropdown in sidebar) using MutationObserver to inject DOM elements on client-side navigation.

### Mintlify Components Used

These are the JSX/MDX components used across articles that need conversion:

| Component | Approximate Count (EN only) | Example |
|---|---|---|
| `<Tip>...</Tip>` | ~10 | Green callout for TL;DR / shortcuts |
| `<Note>...</Note>` | ~40 | Blue callout for supplementary context |
| `<Warning>...</Warning>` | ~25 | Amber callout for things that can go wrong |
| `<Steps>/<Step title="...">` | ~20 files | Numbered procedure steps |
| `<Frame caption="...">` | ~80 usages | Image/video container with optional caption |
| `<CardGroup cols={N}>/<Card>` | ~5 files (~20 cards) | Grid of linked cards (homepage, overview pages) |

### JSX Attributes on Images

Many `<img>` tags have JSX-style attributes that are NOT valid in standard markdown:

```jsx
// These patterns appear throughout the codebase:
<img style={{maxWidth: "56cqi"}} src="/images/..." alt="..." />
<img style={{maxWidth: "49cqi"}} src="/images/..." alt="..." />
<img className="border rounded-xl" src="/images/..." alt="..." />
<img style={{transform: "scale(1.008)"}} src="/images/..." alt="..." />
```

All of these must be stripped. GitBook does not support inline styles or className on images.

### Frontmatter

Every article has YAML frontmatter with `title` and `description`. GitBook supports this — it transfers directly.

```yaml
---
title: "Your First Proctored Test"
description: "A step-by-step guide to creating, configuring, and sharing your first proctored test."
---
```

---

## GitBook Target Architecture

### Multilingual Setup

GitBook uses **variants** (separate "spaces") for each language, linked to a single published site. This replaces Mintlify's folder-prefix model.

**Required structure:**
- Create 3 GitBook spaces: `AutoProctor Help (EN)`, `AutoProctor Help (ES)`, `AutoProctor Help (PT)`
- Link all 3 spaces to one docs site with language variants
- GitBook provides a built-in language switcher (replaces `custom.js`)

For Git Sync, you can either:
1. Use 3 separate repos (one per language), OR
2. Use one repo with 3 root directories configured in `.gitbook.yaml`

**Recommended approach:** Single repo with this structure:
```
autoproctor-gitbook-docs/
├── en/
│   ├── .gitbook.yaml
│   ├── SUMMARY.md
│   ├── README.md              # Homepage
│   ├── images/                # Shared (or symlinked)
│   ├── videos/
│   └── tests-results/
│       ├── create/
│       │   ├── your-first-proctored-test.md
│       │   └── ...
│       └── ...
├── es/
│   ├── .gitbook.yaml
│   ├── SUMMARY.md
│   ├── README.md
│   └── ... (same structure)
└── pt/
    ├── .gitbook.yaml
    ├── SUMMARY.md
    ├── README.md
    └── ... (same structure)
```

### Navigation: SUMMARY.md

GitBook uses `SUMMARY.md` instead of `docs.json`. One `SUMMARY.md` per language space.

**EN SUMMARY.md** (convert from `docs.json` navigation → EN section):

```markdown
# Table of contents

## Tests & Results

* [Create](tests-results/create/README.md)
  * [Your First Proctored Test](tests-results/create/your-first-proctored-test.md)
  * [Quiz Providers](tests-results/create/quiz-providers.md)
  * [Proctoring Settings](tests-results/create/proctoring-settings.md)
  * [Enhanced Proctoring](tests-results/create/enhanced-proctoring.md)
  * [Timer Settings](tests-results/create/timer-settings.md)
  * [Advanced Settings](tests-results/create/advanced-settings.md)
  * [Resuming Test Attempts](tests-results/create/resuming-test-attempts.md)
  * [Resuming Google Forms Tests](tests-results/create/resuming-google-forms.md)
  * [Instructions Page for Candidates](tests-results/create/instructions-page-for-candidates.md)
  * [Archiving and Deleting Tests](tests-results/create/archiving-and-deleting-tests.md)
  * [IFrame Query Arguments](tests-results/create/iframe-query-arguments.md)
  * [AutoProctor Add-On Error](tests-results/create/add-on-error.md)
* [Results](tests-results/results/README.md)
  * [Where Can I See My Quiz Results?](tests-results/results/how-to-see-results.md)
  * [Where Can I See Proctoring Results?](tests-results/results/proctoring-results.md)
  * [Access Answers and Candidate Responses](tests-results/results/individual-submissions.md)
  * [Export to Excel](tests-results/results/export-to-excel.md)
  * [Google Sheets Integration](tests-results/results/google-sheets-integration.md)
  * [Sharing Test Results](tests-results/results/sharing-test-results.md)
  * [Unsubmitted Tests](tests-results/results/unsubmitted-tests.md)
* [Access & Limits](tests-results/access-limits/README.md)
  * [Maximum Attempts](tests-results/access-limits/maximum-attempts.md)
  * [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md)
  * [Restricting by Email](tests-results/access-limits/restricting-by-email.md)
  * [Restricting to Some Users](tests-results/access-limits/restricting-to-some-users.md)
  * [Adding Collaborators](tests-results/access-limits/adding-collaborators.md)
  * [Concurrency](tests-results/access-limits/concurrency.md)
* [Issues](tests-results/issues/README.md)
  * [Loading Screen](tests-results/issues/loading-screen.md)
  * [Blank Page / Grey Screen](tests-results/issues/blank-page-grey-screen.md)
  * [Slow and Laggy](tests-results/issues/slow-and-laggy.md)
  * [Cannot Click Answer](tests-results/issues/cannot-click-answer.md)
  * [False App Switch](tests-results/issues/false-app-switch.md)
  * [No Face or Multiple Faces](tests-results/issues/no-face-or-multiple-faces.md)
  * [Incorrect Student Name](tests-results/issues/incorrect-student-name.md)
  * [Missing Images and Recordings](tests-results/issues/missing-images-and-recordings.md)
  * [Missing Random Photos](tests-results/issues/missing-random-photos.md)
  * [Missing Violation Evidence](tests-results/issues/missing-violation-evidence.md)
  * [Went Offline Meaning](tests-results/issues/went-offline-meaning.md)
  * [Google Forms Questions Not Visible](tests-results/issues/google-forms-questions-not-visible.md)
  * [Google Forms Response Not Visible](tests-results/issues/google-forms-response-not-visible.md)

## Candidate Guide

* [Attempting Tests](candidate-guide/attempting/README.md)
  * [Proctored Test Instructions](candidate-guide/attempting/proctored-test-instructions.md)
  * [Proctored Socratease Instructions](candidate-guide/attempting/proctored-socratease-instructions.md)
  * [Timed Test Instructions](candidate-guide/attempting/timed-test-instructions.md)
  * [Timed Socratease Instructions](candidate-guide/attempting/timed-socratease-instructions.md)
  * [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md)
  * [How to Logout](candidate-guide/attempting/how-to-logout.md)
  * [Submit Button](candidate-guide/attempting/submit-button.md)

## Understanding AutoProctor

* [Getting Started](understanding/getting-started/README.md)
  * [FAQs](understanding/getting-started/faqs.md)
  * [Device Compatibility](understanding/getting-started/device-compatibility.md)
  * [Best Practices for Test Creators](understanding/getting-started/best-practices-for-teachers.md)
  * [Things You Need to Know](understanding/getting-started/things-you-need-to-know.md)
* [How Proctoring Works](understanding/how-proctoring-works/README.md)
  * [What Gets Tracked](understanding/how-proctoring-works/what-gets-tracked.md)
  * [Trust Score](understanding/how-proctoring-works/trust-score.md)
  * [Video Recording](understanding/how-proctoring-works/video-recording.md)

## Socratease Quizzes

* [Create & Questions](socratease/create-questions/README.md)
  * [Why Socratease?](socratease/create-questions/why-socratease.md)
  * [Creating a Quiz](socratease/create-questions/creating-a-quiz.md)
  * [Question Types](socratease/create-questions/question-types.md)
  * [Question Type Availability](socratease/create-questions/question-type-availability.md)
  * [Question Banks](socratease/create-questions/question-banks.md)
  * [Bulk Import from Excel](socratease/create-questions/bulk-import-from-excel.md)
* [Settings](socratease/settings/README.md)
  * [Quiz Settings](socratease/settings/quiz-settings.md)
  * [Question Display Mode](socratease/settings/question-display-mode.md)
  * [Showing Results to Candidates](socratease/settings/showing-results-to-candidates.md)
  * [Using Tags](socratease/settings/using-tags.md)
  * [LaTeX Math Equations](socratease/settings/latex-math-equations.md)

## Pricing & Account

* [Plans & Credits](pricing-account/plans-credits/README.md)
  * [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md)
  * [Feature Comparison](pricing-account/plans-credits/feature-comparison.md)
  * [Elite Features](pricing-account/plans-credits/elite-features.md)
  * [One-Time Subscription](pricing-account/plans-credits/one-time-subscription.md)
  * [Cancel Subscription](pricing-account/plans-credits/cancel-subscription.md)
* [Billing & Teams](pricing-account/billing-teams/README.md)
  * [Billing Information](pricing-account/billing-teams/billing-information.md)
  * [Teams](pricing-account/billing-teams/teams.md)
  * [Invoices](pricing-account/billing-teams/invoices.md)
  * [Track Test Pack Usage](pricing-account/billing-teams/track-test-pack-usage.md)
  * [Purchased Packs Not Visible](pricing-account/billing-teams/purchased-packs-not-visible.md)
* [Support](pricing-account/support/README.md)
  * [Booking a Demo](pricing-account/support/booking-a-demo.md)
  * [Contact Us](pricing-account/support/contact-us.md)
```

Each group section (e.g., `## Tests & Results`) needs a `README.md` in its folder — this is the group landing page. If one doesn't exist, create a minimal one with the group title.

---

## Component Conversion Reference

### Callouts

**Mintlify `<Tip>` → GitBook `{% hint style="success" %}`**
```markdown
<!-- Mintlify -->
<Tip>
Create a proctored test, share the link with candidates, and view results — all in under 5 minutes.
</Tip>

<!-- GitBook -->
{% hint style="success" %}
Create a proctored test, share the link with candidates, and view results — all in under 5 minutes.
{% endhint %}
```

**Mintlify `<Note>` → GitBook `{% hint style="info" %}`**
```markdown
<!-- Mintlify -->
<Note>
**Customize Message** is a Premium feature.
</Note>

<!-- GitBook -->
{% hint style="info" %}
**Customize Message** is a Premium feature.
{% endhint %}
```

**Mintlify `<Warning>` → GitBook `{% hint style="warning" %}` or `{% hint style="danger" %}`**
```markdown
<!-- Mintlify -->
<Warning>
You must check the **Enable Proctor** checkbox for any of these settings to apply.
</Warning>

<!-- GitBook -->
{% hint style="warning" %}
You must check the **Enable Proctor** checkbox for any of these settings to apply.
{% endhint %}
```

Use `"warning"` for cautions and `"danger"` for critical/destructive warnings.

### Steps

**Mintlify `<Steps>/<Step>` → GitBook `{% stepper %}`**
```markdown
<!-- Mintlify -->
<Steps>
  <Step title="Log in to AutoProctor">
    Go to autoproctor.co and sign in with your **Google** or **Microsoft** account.
  </Step>
  <Step title="Create a new test">
    Click **Create Test** on your dashboard.
  </Step>
</Steps>

<!-- GitBook -->
{% stepper %}
{% step %}
### Log in to AutoProctor
Go to autoproctor.co and sign in with your **Google** or **Microsoft** account.
{% endstep %}
{% step %}
### Create a new test
Click **Create Test** on your dashboard.
{% endstep %}
{% endstepper %}
```

Note: The step title becomes an `### H3` heading inside the step block.

### Images (replacing `<Frame>`)

**Mintlify `<Frame>` with `<img>` → GitBook plain markdown image**

```markdown
<!-- Mintlify -->
<Frame caption="AutoProctor dashboard for a new user">
  <img style={{maxWidth: "56cqi"}} src="/images/getting-started/new-user-dashboard.png" alt="AutoProctor dashboard for a new user" />
</Frame>

<!-- GitBook -->
![AutoProctor dashboard for a new user](images/getting-started/new-user-dashboard.png)
```

**What is lost:**
- Caption text (GitBook does not have a native image caption block — use a line of italic text below the image as a workaround: `*AutoProctor dashboard for a new user*`)
- Responsive sizing (`cqi` units) — images render at default size
- `className` attributes — no custom CSS classes
- Shrink-wrapped frame container with background — images render inline

**For videos:**
```markdown
<!-- Mintlify -->
<Frame caption="How to create a test">
  <video controls className="rounded-xl" src="/videos/creating-tests/all-test-types.mp4"></video>
</Frame>

<!-- GitBook — embed or link -->
{% embed url="/videos/creating-tests/all-test-types.mp4" %}
How to create a test
{% endembed %}
```

Note: GitBook supports `{% embed %}` for videos. Self-hosted video files may need to be uploaded to GitBook's asset storage or an external host.

### Cards (replacing `<CardGroup>/<Card>`)

**Mintlify `<CardGroup>/<Card>` → GitBook cards (HTML table)**

```markdown
<!-- Mintlify -->
<CardGroup cols={2}>
  <Card title="Your First Proctored Test" icon="rocket" href="/tests-results/create/your-first-proctored-test">
    Step-by-step quickstart guide
  </Card>
  <Card title="Quiz Providers" icon="list" href="/tests-results/create/quiz-providers">
    Supported quiz platforms
  </Card>
</CardGroup>

<!-- GitBook -->
<table data-view="cards">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th data-hidden data-card-target data-type="content-ref"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Your First Proctored Test</strong></td>
      <td>Step-by-step quickstart guide</td>
      <td><a href="tests-results/create/your-first-proctored-test.md">link</a></td>
    </tr>
    <tr>
      <td><strong>Quiz Providers</strong></td>
      <td>Supported quiz platforms</td>
      <td><a href="tests-results/create/quiz-providers.md">link</a></td>
    </tr>
  </tbody>
</table>
```

**What is lost:** Icons (`icon="rocket"`) — GitBook cards support cover images but not inline icons.

---

## Redirects

The current `docs.json` contains 90 redirect rules mapping old Crisp helpdesk URLs to the new structure. These need to be recreated in GitBook.

**Options:**
1. **GitBook dashboard**: Settings → Domain & redirects → Add redirect (one by one — tedious for 90)
2. **GitBook API**: `POST /docs-sites/{siteId}/redirects` — scriptable for bulk import
3. **`.gitbook.yaml` redirects section** (if supported for the site)

**Full redirect list** (extract from `docs.json`):

```json
[
  { "source": "/getting-started/quickstart", "destination": "/tests-results/create/your-first-proctored-test" },
  { "source": "/creating-tests/quiz-providers", "destination": "/tests-results/create/quiz-providers" },
  { "source": "/settings/proctoring-settings", "destination": "/tests-results/create/proctoring-settings" },
  { "source": "/settings/enhanced-proctoring", "destination": "/tests-results/create/enhanced-proctoring" },
  { "source": "/settings/timer-settings", "destination": "/tests-results/create/timer-settings" },
  { "source": "/settings/advanced-settings", "destination": "/tests-results/create/advanced-settings" },
  { "source": "/settings/resuming-test-attempts", "destination": "/tests-results/create/resuming-test-attempts" },
  { "source": "/settings/resuming-google-forms", "destination": "/tests-results/create/resuming-google-forms" },
  { "source": "/creating-tests/archiving-and-deleting-tests", "destination": "/tests-results/create/archiving-and-deleting-tests" },
  { "source": "/creating-tests/iframe-query-arguments", "destination": "/tests-results/create/iframe-query-arguments" },
  { "source": "/creating-tests/add-on-error", "destination": "/tests-results/create/add-on-error" },
  { "source": "/results/how-to-see-results", "destination": "/tests-results/results/how-to-see-results" },
  { "source": "/results/proctoring-results", "destination": "/tests-results/results/proctoring-results" },
  { "source": "/results/individual-submissions", "destination": "/tests-results/results/individual-submissions" },
  { "source": "/results/export-to-excel", "destination": "/tests-results/results/export-to-excel" },
  { "source": "/results/google-sheets-integration", "destination": "/tests-results/results/google-sheets-integration" },
  { "source": "/results/sharing-test-results", "destination": "/tests-results/results/sharing-test-results" },
  { "source": "/results/unsubmitted-tests", "destination": "/tests-results/results/unsubmitted-tests" },
  { "source": "/settings/maximum-attempts", "destination": "/tests-results/access-limits/maximum-attempts" },
  { "source": "/settings/inviting-candidates-via-email", "destination": "/tests-results/access-limits/inviting-candidates-via-email" },
  { "source": "/settings/restricting-by-email", "destination": "/tests-results/access-limits/restricting-by-email" },
  { "source": "/settings/restricting-to-some-users", "destination": "/tests-results/access-limits/restricting-to-some-users" },
  { "source": "/creating-tests/adding-collaborators", "destination": "/tests-results/access-limits/adding-collaborators" },
  { "source": "/settings/concurrency", "destination": "/tests-results/access-limits/concurrency" },
  { "source": "/candidate-issues/loading-screen", "destination": "/tests-results/issues/loading-screen" },
  { "source": "/candidate-issues/blank-page-grey-screen", "destination": "/tests-results/issues/blank-page-grey-screen" },
  { "source": "/candidate-issues/slow-and-laggy", "destination": "/tests-results/issues/slow-and-laggy" },
  { "source": "/candidate-issues/cannot-click-answer", "destination": "/tests-results/issues/cannot-click-answer" },
  { "source": "/candidate-issues/false-app-switch", "destination": "/tests-results/issues/false-app-switch" },
  { "source": "/candidate-issues/no-face-or-multiple-faces", "destination": "/tests-results/issues/no-face-or-multiple-faces" },
  { "source": "/candidate-issues/incorrect-student-name", "destination": "/tests-results/issues/incorrect-student-name" },
  { "source": "/candidate-issues/missing-images-and-recordings", "destination": "/tests-results/issues/missing-images-and-recordings" },
  { "source": "/candidate-issues/missing-random-photos", "destination": "/tests-results/issues/missing-random-photos" },
  { "source": "/candidate-issues/missing-violation-evidence", "destination": "/tests-results/issues/missing-violation-evidence" },
  { "source": "/candidate-issues/went-offline-meaning", "destination": "/tests-results/issues/went-offline-meaning" },
  { "source": "/candidate-issues/google-forms-questions-not-visible", "destination": "/tests-results/issues/google-forms-questions-not-visible" },
  { "source": "/candidate-issues/google-forms-response-not-visible", "destination": "/tests-results/issues/google-forms-response-not-visible" },
  { "source": "/taking-tests/proctored-test-instructions", "destination": "/candidate-guide/attempting/proctored-test-instructions" },
  { "source": "/taking-tests/proctored-socratease-instructions", "destination": "/candidate-guide/attempting/proctored-socratease-instructions" },
  { "source": "/taking-tests/timed-test-instructions", "destination": "/candidate-guide/attempting/timed-test-instructions" },
  { "source": "/taking-tests/timed-socratease-instructions", "destination": "/candidate-guide/attempting/timed-socratease-instructions" },
  { "source": "/taking-tests/candidate-login-methods", "destination": "/candidate-guide/attempting/candidate-login-methods" },
  { "source": "/taking-tests/how-to-logout", "destination": "/candidate-guide/attempting/how-to-logout" },
  { "source": "/taking-tests/submit-button", "destination": "/candidate-guide/attempting/submit-button" },
  { "source": "/taking-tests/instructions-page-for-candidates", "destination": "/tests-results/create/instructions-page-for-candidates" },
  { "source": "/getting-started/faqs", "destination": "/understanding/getting-started/faqs" },
  { "source": "/getting-started/device-compatibility", "destination": "/understanding/getting-started/device-compatibility" },
  { "source": "/getting-started/best-practices-for-teachers", "destination": "/understanding/getting-started/best-practices-for-teachers" },
  { "source": "/results/things-you-need-to-know", "destination": "/understanding/getting-started/things-you-need-to-know" },
  { "source": "/getting-started/what-gets-tracked", "destination": "/understanding/how-proctoring-works/what-gets-tracked" },
  { "source": "/getting-started/trust-score", "destination": "/understanding/how-proctoring-works/trust-score" },
  { "source": "/getting-started/video-recording", "destination": "/understanding/how-proctoring-works/video-recording" },
  { "source": "/socratease/why-socratease", "destination": "/socratease/create-questions/why-socratease" },
  { "source": "/socratease/creating-a-quiz", "destination": "/socratease/create-questions/creating-a-quiz" },
  { "source": "/socratease/question-types", "destination": "/socratease/create-questions/question-types" },
  { "source": "/socratease/question-type-availability", "destination": "/socratease/create-questions/question-type-availability" },
  { "source": "/socratease/question-banks", "destination": "/socratease/create-questions/question-banks" },
  { "source": "/socratease/bulk-import-from-excel", "destination": "/socratease/create-questions/bulk-import-from-excel" },
  { "source": "/socratease/quiz-settings", "destination": "/socratease/settings/quiz-settings" },
  { "source": "/socratease/question-display-mode", "destination": "/socratease/settings/question-display-mode" },
  { "source": "/socratease/showing-results-to-candidates", "destination": "/socratease/settings/showing-results-to-candidates" },
  { "source": "/socratease/using-tags", "destination": "/socratease/settings/using-tags" },
  { "source": "/socratease/latex-math-equations", "destination": "/socratease/settings/latex-math-equations" },
  { "source": "/pricing/payments-and-credits", "destination": "/pricing-account/plans-credits/payments-and-credits" },
  { "source": "/pricing/feature-comparison", "destination": "/pricing-account/plans-credits/feature-comparison" },
  { "source": "/pricing/elite-features", "destination": "/pricing-account/plans-credits/elite-features" },
  { "source": "/pricing/one-time-subscription", "destination": "/pricing-account/plans-credits/one-time-subscription" },
  { "source": "/pricing/cancel-subscription", "destination": "/pricing-account/plans-credits/cancel-subscription" },
  { "source": "/pricing/billing-information", "destination": "/pricing-account/billing-teams/billing-information" },
  { "source": "/pricing/teams", "destination": "/pricing-account/billing-teams/teams" },
  { "source": "/pricing/invoices", "destination": "/pricing-account/billing-teams/invoices" },
  { "source": "/pricing/track-test-pack-usage", "destination": "/pricing-account/billing-teams/track-test-pack-usage" },
  { "source": "/pricing/purchased-packs-not-visible", "destination": "/pricing-account/billing-teams/purchased-packs-not-visible" },
  { "source": "/support/booking-a-demo", "destination": "/pricing-account/support/booking-a-demo" },
  { "source": "/support/contact-us", "destination": "/pricing-account/support/contact-us" }
]
```

---

## Conversion Scripts

The migration agent should create and run scripts for these bulk operations. All scripts should operate on a NEW directory (do not modify the Mintlify source).

### Script 1: Copy and rename files (.mdx → .md)

```bash
# Copy the EN, ES, PT content directories to a new gitbook target
# Rename all .mdx files to .md
# Exclude: docs.json, custom.css, custom.js, CLAUDE.md, .claude/, .agents/, node_modules/
```

### Script 2: Convert callouts (Tip/Note/Warning)

Regex replacements across all `.md` files:

```
<Tip>\n  →  {% hint style="success" %}\n
</Tip>   →  {% endhint %}

<Note>\n →  {% hint style="info" %}\n
</Note>  →  {% endhint %}

<Warning>\n → {% hint style="warning" %}\n
</Warning>  → {% endhint %}
```

Be careful with:
- Multiline content inside callouts
- Callouts that contain markdown formatting (bold, links, code)
- Nested elements inside callouts (rare but possible)

### Script 3: Convert Steps

```
<Steps>           →  {% stepper %}
<Step title="X">  →  {% step %}\n### X
</Step>           →  {% endstep %}
</Steps>          →  {% endstepper %}
```

Note: Content inside `<Step>` tags (including images, callouts, tables) should be preserved as-is between `{% step %}` and `{% endstep %}`.

### Script 4: Convert Frame/Image tags

```
<Frame caption="X">
  <img ... src="Y" alt="Z" />
</Frame>

→

![Z](Y)
*X*
```

Strip all JSX attributes: `style={{...}}`, `className="..."`, `style={{transform: ...}}`.

For images without a Frame wrapper, convert `<img src="Y" alt="Z" />` → `![Z](Y)`.

For videos in Frame:
```
<Frame caption="X">
  <video controls className="..." src="Y"></video>
</Frame>

→

{% embed url="Y" %}
X
{% endembed %}
```

### Script 5: Clean JSX artifacts

Remove across all files:
- `{/* ... */}` JSX comments (or convert to `<!-- ... -->`)
- Any remaining JSX-style attributes
- Orphaned `className`, `style` attributes on HTML tags

### Script 6: Fix internal links

- Change `.mdx` references to `.md` in any explicit file links
- Internal links like `/tests-results/create/quiz-providers` should become relative: `../create/quiz-providers.md` (GitBook prefers relative paths)
- External autoproctor.co links: keep as-is (they already have trailing slashes)

### Script 7: Generate SUMMARY.md files

Parse the navigation sections from `docs.json` and generate:
- `en/SUMMARY.md`
- `es/SUMMARY.md`
- `pt/SUMMARY.md`

### Script 8: Generate .gitbook.yaml files

For each language directory:

```yaml
root: ./

structure:
  readme: ./README.md
  summary: ./SUMMARY.md
```

### Script 9: Create README.md group landing pages

For each subdirectory referenced in SUMMARY.md that doesn't have a `README.md`, create one with minimal content:

```markdown
---
description: Group description from docs.json
---

# Group Title
```

---

## Theme & Branding

The following settings from `docs.json` need to be configured in GitBook's dashboard (Settings → Customization):

| Setting | Current Value | Where in GitBook |
|---|---|---|
| Site name | AutoProctor | Site settings |
| Logo (light) | `/images/brand/logo-light.svg` | Customization → Logo |
| Logo (dark) | `/images/brand/logo-dark.svg` | Customization → Logo |
| Favicon | `/images/brand/favicon.svg` | Customization → Favicon |
| Primary color | `#4A934A` | Customization → Theme |
| Background (light) | `#FFFFFF` | Customization → Theme |
| Background (dark) | Not used (dark mode disabled in Mintlify) | N/A |
| Font (headings) | Inter | Customization → Font |
| Font (body) | Inter | Customization → Font |
| Footer links | LinkedIn, YouTube | Customization → Footer |

**Note:** Dark mode was disabled in Mintlify (`"modeToggle": {"default": "light", "isHidden": true}`). GitBook allows enabling/disabling dark mode in site settings.

---

## What Cannot Be Migrated

These features exist in Mintlify but have no GitBook equivalent:

1. **Container query image sizing** (`cqi` units) — Images will render at GitBook's default sizes
2. **Frame shrink-wrapping** (`width: fit-content` on image containers) — No equivalent
3. **H3 left-border indentation** — GitBook does not support custom heading styles
4. **Content area width override** (`max-width: 64rem`) — GitBook controls layout
5. **Related Resources section styling** (border-top, muted text) — Will render as normal H2 + list
6. **Mintlify branding removal** — GitBook has its own branding (removable on paid plans)
7. **Card icons** — GitBook cards support cover images but not inline icons
8. **`og:site_name` SEO meta tag** — GitBook auto-generates OG tags

---

## Verification Checklist

After migration, verify:

- [ ] All 75 EN articles render correctly
- [ ] All 75 ES articles render correctly
- [ ] All 75 PT articles render correctly
- [ ] Language switcher works between EN/ES/PT
- [ ] Navigation structure matches the current site
- [ ] All images load (check `/images/` path references)
- [ ] All videos load or are properly embedded
- [ ] Internal links between articles work
- [ ] External autoproctor.co links have trailing slashes
- [ ] Callouts render with correct colors (success/info/warning/danger)
- [ ] Steps render as numbered procedures
- [ ] Tables render correctly
- [ ] Homepage cards link to correct articles
- [ ] All 90 redirects are configured and working
- [ ] Custom domain is configured
- [ ] Favicon and logos display correctly
- [ ] Search works across all languages
- [ ] No raw JSX/MDX syntax visible on any page
