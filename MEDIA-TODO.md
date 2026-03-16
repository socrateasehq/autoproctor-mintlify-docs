# Media TODO Checklist

Consolidated list of all screenshots, videos, GIFs, and diagrams needed across EN articles.
ES and PT articles mirror the same TODOs — once EN media is added, duplicate to `es/` and `pt/` folders.

**Total: 173 items** (152 screenshots/diagrams, 14 videos, 7 GIFs)

---

## Getting Started (22 items)

### quickstart.mdx
- [ ] Video walkthrough of the complete quickstart flow <!-- skip -->

<!-- video will cover the below points -->
- [x] Screenshot of the AutoProctor dashboard for a new user <!-- getting-started/new-user-dashboard.png -->
- [x] Screenshot of the quiz provider selection screen <!-- creating-tests/all-test-types.png -->
- [x] Screenshot of the test settings page with key sections highlighted <!-- getting-started/configure-test-settings.png -->
- [ ] GIF showing the demo test experience <!-- skip. -->
- [x] Screenshot showing where to copy the test link <!-- getting-started/copy-test-link.gif -->
- [x] Screenshot of the results page with sample data <!-- getting-started/sample-results.png -->

### what-gets-tracked.mdx
- [x] Screenshot of a sample proctoring report showing flagged violations <!-- getting-started/sample-proctoring-report.png -->
- [x] Screenshot of violation evidence cards in a proctoring report <!-- skip -->
<!-- Have added a video for the below 3 points: videos/getting-started/configure-proctor-settings.mp4 -->
- [x] Screenshot of the test dashboard with the Settings button highlighted
- [x] Screenshot of the Proctoring Settings tab
- [x] Screenshot of proctoring feature toggles

### trust-score.mdx
- [ ] Diagram or infographic illustrating how the three factors combine into the Trust Score <!-- ignoring this for now -->
- [x] Screenshot of the results list showing Trust Score column <!-- videos/getting-started/trustscore-column.mp4 -->
- [ ] Screenshot of results list sorted by Trust Score <!-- don't need this -->
- [ ] Screenshot of an individual proctoring report with violation evidence <!-- we can skip this as well -->

### device-compatibility.mdx
- [ ] Screenshot of the demo test landing page <!-- skip -->
- [x] Screenshot of the browser permission prompt for camera/microphone <!-- getting-started/video-permission.png + getting-started/audio-permission.png -->
- [ ] Screenshot of a successful demo test completion screen <!-- skip -->

### video-recording.mdx
- [ ] Diagram comparing traditional video-based proctoring vs. AutoProctor's on-device monitoring approach <!-- ignoring this for now -->
- [ ] Illustration of the smoke detector analogy -- on-device monitoring with alert-only output <!-- skip -->
- [x] Screenshot of a proctoring report showing different types of violation evidence <!-- getting-started/sample-proctoring-report.png -->

### best-practices-for-teachers.mdx
- [ ] Video walkthrough of the complete test administration workflow <!-- will be a lot to cover in a video, we should skip -->
- [ ] Screenshot of the demo test landing page <!-- skip -->
- [x] Screenshot of the account credits/balance display <!-- getting-started/display-credits.gif -->
- [x] Screenshot of the dashboard during an active test session showing real-time submissions <!-- getting-started/sample-results.png -->
- [ ] Screenshot of the results page with Trust Score column highlighted <!-- i think we should skip as we are linking to trust scores doc and that already has the video highlighting trust score column  -->

---

## Creating Tests (16 items)

### quiz-providers.mdx
<!-- Added one video and one image to cover all points: videos/creating-tests/all-test-types.mp4 + creating-tests/all-test-types.png -->
- [ ] Screenshot of the quiz provider selection screen <!-- skip -->
- [x] Screenshot of Socratease quiz creation interface <!-- covered by video -->
- [x] Video walkthrough of creating a Socratease quiz <!-- videos/creating-tests/all-test-types.mp4 -->
- [x] Screenshot of the AutoProctor Google Forms add-on <!-- covered by video -->
- [x] Video walkthrough of using AutoProctor with Google Forms <!-- covered by video -->
- [x] Screenshot of a Microsoft Forms test in AutoProctor <!-- covered by video -->
- [x] Video walkthrough of using AutoProctor with Microsoft Forms <!-- covered by video -->
- [x] Screenshot of the IFrame/Other provider configuration <!-- covered by video -->
- [x] Video walkthrough of using AutoProctor with IFrame/Other providers <!-- covered by video -->

### adding-collaborators.mdx
- [x] Screenshot of the Advanced Settings section with the collaborators area visible
- [x] Screenshot of the collaborate link button
<!-- Have added a video to cover all points: videos/creating-tests/collaborators.mp4 -->

### archiving-and-deleting-tests.mdx
<!-- Added three videos to cover all points: videos/creating-tests/archive-test.mp4, delete-test.mp4, restore-test.mp4 -->
- [x] Screenshot of the Dashboard with the Settings button highlighted <!-- covered by archive-test.mp4 -->
- [x] Screenshot of the Archive Test button in test settings <!-- covered by archive-test.mp4 -->
- [x] Screenshot of the Archived Tests section in the left sidebar <!-- covered by archive-test.mp4 -->
- [x] Screenshot of the Restore button in the Archived Tests section <!-- covered by restore-test.mp4 -->

### iframe-query-arguments.mdx
<!-- Added one video to cover both points: videos/settings/query-arguments.mp4 -->
- [x] Screenshot of Advanced Settings with the Query Arguments field visible <!-- covered by query-arguments.mp4 -->
- [x] Screenshot showing the Query Arguments field with an example value entered <!-- covered by query-arguments.mp4 -->

### add-on-error.mdx 
<!-- We can skip this entirely -->
- [ ] Screenshot of the add-on showing only the Help option
- [ ] Screenshot of the add-on working correctly in Incognito mode
- [ ] Screenshot of the AutoProctor add-on in the Google Workspace Marketplace

---

## Settings (33 items)

### timer-settings.mdx
- [ ] Screenshot of the Timer Settings section in the test settings page <!-- skip -->
- [x] A video walkthrough of how to configure timer settings <!-- videos/settings/config-timer-settings.mp4 -->
- [ ] GIF showing the timer countdown experience from the candidate's perspective <!-- i dont think this is needed -->

### proctoring-settings.mdx
- [x] Screenshot of the full Proctoring Settings section <!-- creating-tests/proctoring-settings.png + creating-tests/enhanced-proctoring.png + settings/communication-settings.png -->
- [ ] GIF showing the candidate experience when Photo Before Test Start is enabled <!-- i dont think this is needed -->
- [ ] Video walkthrough of the 360-degree auxiliary device pairing process <!-- we can add the youtube video that we have on features page here, it is a little long, but it covers everything. -->

### enhanced-proctoring.mdx
- [x] Screenshot of the enhanced proctoring settings panel <!-- creating-tests/enhanced-proctoring.png (already embedded at top of article) -->
- [x] Screenshot of the ID card upload screen from the candidate's perspective <!-- taking-tests/id-verification.png -->
- [x] Screenshot of an impersonation detection alert in the proctoring report <!-- taking-tests/impersonation-detected.png -->
- [x] Screenshot of auxiliary device in the proctoring report <!-- taking-tests/aux-device-evidence.png -->
- [x] Screenshot of auxiliary device from the candidate's perspective <!-- taking-tests/aux-device.png -->
- [ ] Video walkthrough of the auxiliary device pairing and 360° proctoring setup <!-- we can add the youtube video here, it is a little long, but it covers everything. -->

- [ ] Screenshot of a session recording playback in the results page <!-- we can either link them to /session-recording-demo/ or the loom we have for that -->

### advanced-settings.mdx
- [x] Screenshot of the Advanced Settings panel <!-- creating-tests/advanced-settings.png (already embedded at top of article) -->
- [ ] Screenshot showing the login provider selection options <!-- skip -->
- [ ] Screenshot showing login restriction configuration <!-- skip -->
- [ ] Screenshot showing the Gather Additional Details configuration <!-- skip -->
- [ ] Screenshot showing the Additional Instructions field and how it appears to candidates <!-- skip -->

### restricting-by-email.mdx
- [ ] Screenshot of the test dashboard showing the Settings button <!-- skip -->
- [ ] Screenshot of the Advanced Settings section with Login Restrictions fields visible <!-- skip -->
- [x] Screenshot of Login Restrictions field showing domain-based restrictions with @abc.com and @xyz.com <!-- settings/login-restrictions-domain.png -->
- [x] Screenshot of Login Restrictions field showing a combination of domain and individual email restrictions <!-- settings/login-restrictions-email.png -->

### restricting-to-some-users.mdx
- [x] Screenshot of Login Restrictions field for Method 2 <!-- settings/login-restrictions-email.png -->
- [x] Video walkthrough of unique invitation links for Method 3 <!-- videos/settings/unique-invitation-links.mp4 -->
- [x] Screenshot of Google Forms settings showing the organization restriction toggle <!-- settings/google-form-restriction.png -->

### inviting-candidates-via-email.mdx
<!-- covered by videos/settings/unique-invitation-links.mp4 -->
- [x] Screenshot of the Unique URL toggle in test settings
- [x] Screenshot of the CSV upload interface for email addresses
- [x] Screenshot of the generated output showing email-link pairs
- [x] Screenshot of the verification code entry screen candidates see

### maximum-attempts.mdx
<!-- videos/settings/max-attempts-settings.mp4 -->
- [x] Screenshot of the test dashboard showing the Settings button
- [x] Screenshot of the Max Attempts field in Main Settings
- [x] Screenshot of the restriction message candidates see when attempts are exhausted <!-- settings/max-attempts-blocked.png -->

### concurrency.mdx
- [ ] Screenshot of the staggering countdown button candidates see <!-- skip -->

### resuming-test-attempts.mdx
- [ ] Screenshot of the test dashboard showing the Settings button <!-- skip -->
- [x] Screenshot of the Enable Auto Resume toggle in test settings <!-- settings/enable-auto-resume.png -->

### resuming-google-forms.mdx
- [x] Screenshot of Google Forms test settings showing Disable Autosave toggled OFF <!-- settings/gforms-autosave-enabled.png -->
- [x] Screenshot of AutoProctor test settings showing Enable Auto-resume toggled ON <!-- settings/gforms-autoresume-enabled.png -->
- [x] Screenshot of Google Forms test settings showing Disable Autosave toggled ON <!-- settings/gforms-autosave-disabled.png -->
- [x] Screenshot of AutoProctor test settings showing Resume Unsubmitted Test toggled OFF <!-- settings/gforms-autoresume-disabled.png -->

---

## Socratease Quizzes (34 items)

### why-socratease.mdx
- [x] Screenshot of Socratease single submit button vs dual submit on other platforms <!-- taking-tests/soc-submit-button.png + taking-tests/submit-buttons-proctored.png -->
- [x] Screenshot of copy-paste restriction setting <!-- videos/socratease/disable-copy-paste.mp4 -->
- [ ] Screenshot of AutoProctor unified dashboard <!-- skip -->

### creating-a-quiz.mdx
- [x] Video walkthrough of creating a Socratease quiz <!-- videos/socratease/create-soc-test.mp4 -->
- [ ] Screenshot of AutoProctor login page <!-- skip -->
- [ ] Screenshot of quiz provider selection screen <!-- skip -->
- [ ] Screenshot of question editor interface <!-- skip -->
- [ ] Screenshot of quiz settings panel <!-- skip -->
- [ ] Screenshot of test link sharing interface <!-- skip -->
- [x] Screenshot of results dashboard <!-- images/getting-started/sample-results.png -->

### question-display-mode.mdx
- [x] Screenshot of the question display mode setting in quiz settings <!-- socratease/question-display-mode.png -->
- [ ] Screenshot of all-at-once display mode from the candidate view <!-- skip -->
- [ ] Screenshot of one-by-one with navigation from the candidate view <!-- skip -->
- [ ] Screenshot of one-by-one without navigation from the candidate view <!-- skip -->
- [x] Screenshot of question display mode dropdown selection <!-- videos/socratease/question-display-mode.mp4 -->

### quiz-settings.mdx
- [x] Screenshot of the Socratease quiz settings panel <!-- videos/socratease/soc-quiz-settings.mp4 -->
- [ ] Screenshot of question randomization toggle <!-- skip -->
- [ ] Screenshot of choice shuffling toggle <!-- skip -->
- [ ] Screenshot of copy-paste restriction toggle <!-- skip -->
- [ ] Screenshot of tab-switch auto-submit configuration <!-- skip -->
- [ ] Screenshot of custom instructions field <!-- skip -->
- [x] Screenshot of the settings icon location in the quiz editor <!-- videos/socratease/soc-quiz-settings.mp4 -->

### showing-results-to-candidates.mdx
<!-- videos/socratease/release-method.mp4 -->
- [x] Screenshot of settings icon in quiz editor
- [x] Screenshot of result visibility dropdown selection

### question-banks.mdx
- [x] Screenshot of Question Bank overview screen <!-- socratease/question-bank-overview.png -->
- [x] Screenshot of Question Bank Quiz overview <!-- socratease/question-bank-quiz-overview.png -->
- [x] Screenshot of QBQ creation interface <!-- videos/socratease/add-qbq.mp4 -->
- [ ] Screenshot of adding QBQ to a test <!-- skip -->

### bulk-import-from-excel.mdx
<!-- videos/socratease/import-from-excel.mp4 -->
- [x] Screenshot of template download button in quiz editor
- [x] Screenshot of a filled-in Excel template
- [x] Screenshot of upload button and import confirmation

### using-tags.mdx
<!-- videos/socratease/add-tags.mp4 + videos/socratease/filter-by-tags.mp4 -->
- [x] Screenshot of quiz report showing results grouped by tags
- [x] Screenshot of the three-dot menu with tag input field
- [x] Screenshot of the Group By dropdown with Tags selected
- [x] Screenshot of the Filter by Tag dropdown in action

### latex-math-equations.mdx
<!-- videos/socratease/using-latex.mp4 -->
- [x] Screenshot showing LaTeX equation rendered in a Socratease quiz question
- [x] Screenshot of LaTeX support toggle in quiz settings
- [x] Screenshot of equation being written in the quiz editor
- [x] Screenshot of the sample LaTeX quiz showing rendered equations

---

## Candidate Guide — Instructions (10 items)

### proctored-test-instructions.mdx
- [x] Screenshot of purple and green submit buttons with numbered click order annotations <!-- taking-tests/submit-buttons-proctored.png -->

### timed-test-instructions.mdx
- [x] Screenshot or GIF of submit button sequence for timed tests <!-- taking-tests/submit-buttons-timed.gif -->

### proctored-socratease-instructions.mdx
- [ ] Video guide showing how to take a proctored Socratease quiz on AutoProctor <!-- skip -->

### timed-socratease-instructions.mdx
- [ ] Video guide showing how to take a timed Socratease quiz on AutoProctor <!-- skip -->

### submit-button.mdx
- [x] Screenshot or GIF showing the two-button submission flow for non-Socratease quizzes <!-- taking-tests/submit-buttons-proctored.png -->
- [x] Screenshot or GIF showing the single-button Socratease submission flow <!-- taking-tests/soc-submit-button.png -->

### candidate-login-methods.mdx
- [x] Screenshot of AutoProctor login screen showing Google, Microsoft, and Email sign-in options <!-- taking-tests/login-methods.png -->

### how-to-logout.mdx
<!-- images/taking-tests/how-to-logout.gif -->
- [x] Screenshot of AutoProctor mobile menu with Logout option highlighted
- [x] Screenshot of AutoProctor desktop header with Logout option highlighted

### instructions-page-for-candidates.mdx
- [x] Screenshot of the full AutoProctor instructions page as seen by candidates <!-- getting-started/instructions-page.png -->
- [x] Screenshot of the Additional Instructions field in Advanced Settings <!-- videos/getting-started/additional-instructions-settings.mp4 -->
- [x] Screenshot of the Gather Additional Details feature in Advanced Settings <!-- videos/getting-started/gather-additional-details.mp4 -->

---

## Candidate Guide — Issues (9 items)

### loading-screen.mdx
- [x] Screenshot of AutoProctor loading screen indicating a compatibility issue <!-- candidate-issues/loading-screen-demo.png -->

### blank-page-grey-screen.mdx
- [x] Screenshot of blank page caused by wrong Google account within AutoProctor <!-- candidate-issues/blank-page-google-account.png -->

### cannot-click-answer.mdx
- [x] Screenshot of test form loaded in read-only mode due to incorrect Google account <!-- candidate-issues/cannot-click-form.png -->

### google-forms-questions-not-visible.mdx
- [x] Screenshot of Google Form showing an access restriction message within AutoProctor <!-- candidate-issues/google-forms-access-restricted.png -->

### google-forms-response-not-visible.mdx
- [x] Annotated screenshot showing both submit buttons with numbered click order <!-- taking-tests/submit-buttons-proctored.png -->

### missing-violation-evidence.mdx
- [ ] Screenshot of proctoring settings showing evidence recording toggle <!-- skip -->

### missing-images-and-recordings.mdx
- [ ] Screenshot of proctoring settings showing evidence recording toggle <!-- skip -->

### went-offline-meaning.mdx
- [x] Screenshot of "Went offline" entry shown in a proctoring report <!-- candidate-issues/went-offline-report.png -->

### incorrect-student-name.mdx
- [x] Screenshot of incorrect candidate name displayed in AutoProctor results page <!-- candidate-issues/incorrect-student-name.png -->

---

## Results & Reports (14 items)

### how-to-see-results.mdx
- [x] Screenshot of the results page <!-- getting-started/sample-results.png -->

### proctoring-results.mdx
- [x] Screenshot of the Results button on the AutoProctor dashboard <!-- results/results-button-dashboard.png -->
- [x] Screenshot of the results table with Trust Score and Quiz Score columns <!-- results/results-table.png -->
- [x] Screenshot of a candidate's proctoring summary page with violations list <!-- results/proctoring-summary.png -->

### individual-submissions.mdx
- [x] Screenshot of the submissions list showing candidate names, scores, and grading status <!-- results/submissions-list.png -->
- [x] Screenshot of an individual submission detail page with responses and scores <!-- results/individual-submission-details.png -->

### unsubmitted-tests.mdx <!-- The images mentioned below were already added. but we should update the doc and then update media as well -->
- [x] Screenshot of the Unsubmitted Tests checkbox on the results page <!-- results/unsubmitted-checkbox.png -->
- [x] Screenshot of the unsubmitted attempts button on a candidate's proctoring report <!-- results/unsubmitted-attempts-button.png -->
- [x] Screenshot of the unsubmitted test details panel <!-- results/unsubmitted-test-details.png -->

### export-to-excel.mdx
- [x] Screenshot of the results page with Export to Excel button highlighted <!-- results/export-results-table.png -->
- [x] GIF showing how to export results to Excel <!-- results/export-results-to-excel.gif -->

### google-sheets-integration.mdx
- [x] Screenshot of the Test Settings page showing Advanced Settings section <!-- settings/write-to-gsheet.gif -->
- [x] Screenshot of the Google Sheets ID field in Advanced Settings <!-- settings/write-to-gsheet.gif -->

### sharing-test-results.mdx
- [x] Screenshot showing the Timer + Proctor add-on within a shared Google Form <!-- videos/settings/timer-proctor-on-gf.mp4 -->

### things-you-need-to-know.mdx
- [ ] Screenshot or GIF showing the two-button submit flow <!-- skip -->

---

## Pricing & Account (13 items)

### payments-and-credits.mdx
- [x] Video of purchasing a subscription <!-- videos/pricing/subscribe.mp4 -->
- [x] GIF of purchasing a Test Pack top-up <!-- pricing/topup.gif -->

### teams.mdx
- [x] Screenshot of the team management page showing member list and join link <!-- pricing/team-management-page.png -->
- [x] Video of creating a team <!-- videos/pricing/create-team.mp4 -->
- [x] Screenshot of join link on the team management page <!-- pricing/join-team.png -->

### elite-features.mdx
- [ ] Screenshot or diagram showing API/SDK integration flow <!-- skip -->
- [x] Screenshot of the Clone Quiz button on the dashboard <!-- YouTube video embed -->

### one-time-subscription.mdx
_(no TODOs)_

### cancel-subscription.mdx
- [x] Screenshot of the Billing link in the left sidebar <!-- pricing/billing-sidebar-link.png -->
- [x] Screenshot of the Manage Subscription button in Plan Details <!-- pricing/manage-subscription-button.png -->
- [x] Screenshot of the Cancel plan button <!-- pricing/cancel-plan-button.png -->

### purchased-packs-not-visible.mdx
- [ ] Screenshot of the Your Account page showing the email address <!-- skip -->

### track-test-pack-usage.mdx
- [x] Screenshot of the Usage link in the sidebar <!-- pricing/usage-sidebar-link.png -->
- [x] Screenshot of the usage table showing per-test credit consumption <!-- pricing/usage-table.png -->
- [x] Screenshot of the team usage table showing per-member credit consumption <!-- pricing/team-usage-table.png -->

### invoices.mdx
- [x] Screenshot of a sample AutoProctor invoice <!-- pricing/sample-invoice.png -->

### billing-information.mdx
- [x] Screenshot of the Billing link in the sidebar <!-- linked to billing page + YouTube video embed -->
- [x] Screenshot of the Manage Subscription button <!-- covered by YouTube video -->

---

## Summary by Type

| Type | Count |
|------|-------|
| Screenshots | 138 |
| Diagrams / Infographics / Illustrations | 4 |
| Videos | 14 |
| GIFs | 7 |
| Screenshot or GIF (either works) | 10 |
| **Total** | **173** |
