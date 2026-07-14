#!/usr/bin/env python3
"""
flatten-urls.py - Flatten nested MDX file paths to a single-level URL structure.

This script:
1. Moves MDX files from nested directories to flat structure using git mv
2. Updates docs.json navigation and redirects
3. Updates all cross-references in all MDX files (EN, ES, PT)
4. Creates a crisp-redirect-map.json file for the CloudFront Function
5. Cleans up empty directories
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent

MAPPING = {
    "tests-results/create/your-first-proctored-test": "create-proctored-exam",
    "tests-results/create/quiz-providers": "supported-quiz-providers",
    "tests-results/create/proctoring-settings": "proctoring-settings",
    "tests-results/create/enhanced-proctoring": "enhanced-proctoring",
    "tests-results/create/timer-settings": "timer-settings",
    "tests-results/create/advanced-settings": "advanced-exam-settings",
    "tests-results/create/resuming-test-attempts": "resume-exam-attempts",
    "tests-results/create/resuming-google-forms": "resume-google-forms-exam",
    "tests-results/create/instructions-page-for-candidates": "candidate-instructions-page",
    "tests-results/create/archiving-and-deleting-tests": "archive-and-delete-exams",
    "tests-results/create/iframe-query-arguments": "iframe-query-arguments",
    "tests-results/create/add-on-error": "google-forms-addon-error",
    "tests-results/results/how-to-see-results": "where-to-find-quiz-results",
    "tests-results/results/proctoring-results": "where-to-find-proctoring-results",
    "tests-results/results/individual-submissions": "access-candidate-responses",
    "tests-results/results/unsubmitted-tests": "view-unsubmitted-exams",
    "tests-results/results/export-to-excel": "export-results-to-excel",
    "tests-results/results/google-sheets-integration": "write-results-to-google-sheets",
    "tests-results/results/sharing-test-results": "share-exam-results",
    "tests-results/access-limits/restricting-by-email": "restrict-access-by-email",
    "tests-results/access-limits/restricting-to-some-users": "restrict-access-to-candidates",
    "tests-results/access-limits/inviting-candidates-via-email": "invite-candidates-via-email",
    "tests-results/access-limits/maximum-attempts": "maximum-exam-attempts",
    "tests-results/access-limits/concurrency": "max-simultaneous-candidates",
    "tests-results/access-limits/adding-collaborators": "add-collaborators",
    "tests-results/issues/loading-screen": "test-stuck-at-loading-screen",
    "tests-results/issues/blank-page-grey-screen": "blank-screen-during-test",
    "tests-results/issues/slow-and-laggy": "test-slow-and-laggy",
    "tests-results/issues/cannot-click-answer": "cannot-click-answers-during-test",
    "tests-results/issues/google-forms-questions-not-visible": "google-forms-questions-not-visible",
    "tests-results/issues/false-app-switch": "false-app-switch-alert",
    "tests-results/issues/no-face-or-multiple-faces": "no-face-or-multiple-faces-detected",
    "tests-results/issues/missing-violation-evidence": "missing-violation-evidence",
    "tests-results/issues/missing-random-photos": "missing-random-photos",
    "tests-results/issues/missing-images-and-recordings": "missing-images-and-recordings",
    "tests-results/issues/went-offline-meaning": "what-does-went-offline-mean",
    "tests-results/issues/incorrect-student-name": "incorrect-candidate-name-in-results",
    "tests-results/issues/google-forms-response-not-visible": "google-forms-response-not-visible",
    "candidate-guide/attempting/proctored-test-instructions": "take-proctored-exam",
    "candidate-guide/attempting/timed-test-instructions": "take-timed-exam",
    "candidate-guide/attempting/proctored-socratease-instructions": "take-proctored-socratease-quiz",
    "candidate-guide/attempting/timed-socratease-instructions": "take-timed-socratease-quiz",
    "candidate-guide/attempting/submit-button": "how-to-submit-quiz",
    "candidate-guide/attempting/candidate-login-methods": "candidate-login-methods",
    "candidate-guide/attempting/how-to-logout": "how-to-logout",
    "understanding/getting-started/things-you-need-to-know": "before-you-get-started",
    "understanding/getting-started/device-compatibility": "device-compatibility",
    "understanding/getting-started/best-practices-for-teachers": "best-practices-for-exam-creators",
    "understanding/getting-started/faqs": "faqs",
    "understanding/how-proctoring-works/what-gets-tracked": "what-gets-tracked-during-proctoring",
    "understanding/how-proctoring-works/trust-score": "what-is-trust-score",
    "understanding/how-proctoring-works/video-recording": "does-autoproctor-record-video",
    "socratease/create-questions/why-socratease": "why-socratease",
    "socratease/create-questions/creating-a-quiz": "create-socratease-quiz",
    "socratease/create-questions/question-types": "socratease-question-types",
    "socratease/create-questions/question-type-availability": "question-type-availability",
    "socratease/create-questions/bulk-import-from-excel": "import-questions-from-excel",
    "socratease/create-questions/question-banks": "question-banks",
    "socratease/settings/quiz-settings": "socratease-quiz-settings",
    "socratease/settings/question-display-mode": "question-display-mode",
    "socratease/settings/showing-results-to-candidates": "show-results-to-candidates",
    "socratease/settings/using-tags": "using-tags",
    "socratease/settings/latex-math-equations": "latex-math-equations",
    "pricing-account/plans-credits/payments-and-credits": "payments-and-credits",
    "pricing-account/plans-credits/feature-comparison": "feature-comparison",
    "pricing-account/plans-credits/elite-features": "elite-plan-features",
    "pricing-account/plans-credits/one-time-subscription": "one-time-subscription",
    "pricing-account/plans-credits/cancel-subscription": "cancel-subscription",
    "pricing-account/billing-teams/teams": "what-is-a-team",
    "pricing-account/billing-teams/purchased-packs-not-visible": "purchased-packs-not-showing",
    "pricing-account/billing-teams/track-test-pack-usage": "track-credit-usage",
    "pricing-account/billing-teams/invoices": "invoices-and-receipts",
    "pricing-account/billing-teams/billing-information": "edit-billing-information",
    "pricing-account/support/contact-us": "contact-us",
    "pricing-account/support/booking-a-demo": "book-a-demo",
}

CRISP_MAPPING = {
    "how-to-see-details-of-unsubmitted-tests-7bwfjp": "view-unsubmitted-exams",
    "where-do-i-find-the-answers-of-an-autoproctor-test-1vcyp8w": "access-candidate-responses",
    "how-to-restrict-autoproctor-to-only-some-users-1i0clwv": "restrict-access-to-candidates",
    "autoproctor-test-settings-124fmjb": "create-proctored-exam",
    "using-tags-on-autoproctor-up8wkk": "using-tags",
    "inviting-candidates-via-email-i98t6m": "invite-candidates-via-email",
    "5-faqs-about-autoproctor-dczd4d": "faqs",
    "what-gets-tracked-and-recorded-during-proctoring-kn393g": "what-gets-tracked-during-proctoring",
    "do-you-record-the-video-of-the-candidate-where-can-i-download-the-video-1077c2w": "does-autoproctor-record-video",
    "using-latex-for-math-equations-1k4u522": "latex-math-equations",
    "instructions-for-taking-a-timed-test-1k26zu3": "take-timed-exam",
    "trust-score-what-is-it-how-it-is-calculated-what-is-a-good-score-1yajx7t": "what-is-trust-score",
    "cannot-see-response-in-google-form-154hg24": "google-forms-response-not-visible",
    "i-cannot-see-the-questions-on-google-forms-1ydsjqq": "google-forms-questions-not-visible",
    "socratease-quiz-settings-yd3vuf": "socratease-quiz-settings",
    "test-loads-but-cannot-click-on-answer-1rcl1q6": "cannot-click-answers-during-test",
    "why-do-some-violations-have-missing-evidence-19rjxbi": "missing-violation-evidence",
    "what-is-export-to-excel-1hdze8z": "export-results-to-excel",
    "i-purchased-test-packs-but-i-cannot-see-them-in-my-account-1meybkn": "purchased-packs-not-showing",
    "why-no-face-or-multiple-faces-detected-even-though-clearly-there-is-only-one-face-aqm7fq": "no-face-or-multiple-faces-detected",
    "why-do-i-not-see-random-photos-in-the-report-n08f91": "missing-random-photos",
    "things-you-need-to-know-8dk1as": "before-you-get-started",
    "instructions-page-for-candidates-1tazm6g": "candidate-instructions-page",
    "quiz-providers-on-autoproctor-13n5455": "supported-quiz-providers",
    "socratease-vs-other-quizzes-submit-button-1ria8bw": "how-to-submit-quiz",
    "test-stuck-at-loading-screen-ihjzg3": "test-stuck-at-loading-screen",
    "candidate-login-methods-pkwoun": "candidate-login-methods",
    "invoices-for-payments-irkqxy": "invoices-and-receipts",
    "how-can-i-purchase-a-one-time-subscription-of-autoproctor-and-not-a-recurring-subscription-wkx36g": "one-time-subscription",
    "maximum-attempts-for-a-test-w7bk1o": "maximum-exam-attempts",
    "switched-to-different-application-falsely-showing-in-the-report-1a0supo": "false-app-switch-alert",
    "student-name-is-incorrect-in-results-page-or-excel-i3huzq": "incorrect-candidate-name-in-results",
    "unable-to-see-images-and-recordings-in-students-test-report-540oww": "missing-images-and-recordings",
    "how-to-add-query-arguments-to-iframes-on-autoproctor-6s0lv9": "iframe-query-arguments",
    "best-practices-for-teachers-1pc2pil": "best-practices-for-exam-creators",
    "archiving-and-deleting-tests-1gsrt5z": "archive-and-delete-exams",
    "test-loads-but-is-very-slow-and-laggy-1n8lqs3": "test-slow-and-laggy",
    "how-to-see-results-on-autoproctor-m6jiyu": "where-to-find-quiz-results",
    "where-can-i-see-proctoring-results-1s5ru8g": "where-to-find-proctoring-results",
    "test-is-showing-a-blank-page-or-grey-screen-1p5gs18": "blank-screen-during-test",
    "how-to-cancel-your-autoproctor-subscription-16zl78f": "cancel-subscription",
    "instructions-for-taking-a-proctored-test-enr9pf": "take-proctored-exam",
    "question-display-mode-187yci9": "question-display-mode",
    "how-to-allow-other-users-to-access-test-results-3okzzs": "share-exam-results",
    "question-banks-dwvaft": "question-banks",
    "why-we-recommend-equip-for-hiring-1jkgl7x": "",
    "error-using-autoproctor-add-on-tn9ynj": "google-forms-addon-error",
    "booking-a-demo-7qhuis": "book-a-demo",
    "socratease-question-type-availability-based-on-plan-ya5rw6": "question-type-availability",
    "payments-and-credits-explained-1y7iwvu": "payments-and-credits",
    "contact-us-k2vxnm": "contact-us",
    "how-to-logout-of-autoproctor-1y33j9y": "how-to-logout",
    "resuming-test-attempts-1amghab": "resume-exam-attempts",
    "what-is-a-team-on-autoproctor-1rfhqaa": "what-is-a-team",
    "editing-your-card-and-billing-information-lbzogr": "edit-billing-information",
    "restricting-the-test-based-on-email-id-19hbpn0": "restrict-access-by-email",
    "checking-individual-submissions-on-autoproctor-wm8jed": "access-candidate-responses",
    "how-to-track-test-pack-usage-1xmghzb": "track-credit-usage",
    "concurrency-maximum-simultaneous-candidates-yqte35": "max-simultaneous-candidates",
    "socratease-quiz-question-types-geexzf": "socratease-question-types",
    "instructions-for-taking-a-timed-socratease-quiz-1czty9p": "take-timed-socratease-quiz",
    "automatically-write-test-results-to-google-sheets-1nhzg4u": "write-results-to-google-sheets",
    "what-does-went-offline-in-the-proctoring-report-mean-pxpbzv": "what-does-went-offline-mean",
    "what-devices-are-compatible-with-autoproctors-proctoring-1bcwsde": "device-compatibility",
    "bulk-import-questions-from-excel-r4vs7a": "import-questions-from-excel",
    "resuming-google-forms-tests-1qb0lxe": "resume-google-forms-exam",
    "how-to-create-a-socratease-quiz-1w48uag": "create-socratease-quiz",
    "showing-results-to-candidates-1x9hsrj": "show-results-to-candidates",
    "why-socratease-quiz-1i82ch9": "why-socratease",
    "adding-collaborators-to-your-tests-1jf4dkj": "add-collaborators",
    "instructions-for-taking-a-proctored-socratease-quiz-16tp1s5": "take-proctored-socratease-quiz",
    "elite-features-1872ame": "elite-plan-features",
}

# Language prefixes: EN is at root, ES and PT are in subdirectories
LANG_PREFIXES = ["", "es/", "pt/"]


# ---------------------------------------------------------------------------
# Step 1: Move files with git mv
# ---------------------------------------------------------------------------

def move_files():
    """Move MDX files from nested directories to flat structure using git mv."""
    moved = 0
    skipped = 0

    for old_path, new_slug in MAPPING.items():
        for prefix in LANG_PREFIXES:
            src = ROOT / f"{prefix}{old_path}.mdx"
            dst = ROOT / f"{prefix}{new_slug}.mdx"

            if not src.exists():
                skipped += 1
                continue

            if dst.exists():
                print(f"  SKIP (dst exists): {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
                skipped += 1
                continue

            # Ensure destination directory exists
            dst.parent.mkdir(parents=True, exist_ok=True)

            result = subprocess.run(
                ["git", "mv", str(src), str(dst)],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(f"  ERROR: git mv {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}: {result.stderr.strip()}")
                skipped += 1
            else:
                moved += 1

    return moved, skipped


# ---------------------------------------------------------------------------
# Step 2: Update docs.json
# ---------------------------------------------------------------------------

def update_docs_json():
    """Update navigation paths and redirects in docs.json."""
    docs_path = ROOT / "docs.json"
    with open(docs_path, "r") as f:
        docs = json.load(f)

    nav_updates = 0
    redirect_updates = 0

    # Sort by longest old path first to avoid partial matches
    sorted_mapping = sorted(MAPPING.items(), key=lambda x: len(x[0]), reverse=True)

    # --- 2a: Update navigation page references ---
    def update_pages(pages, lang_prefix=""):
        """Recursively update page references in navigation groups."""
        nonlocal nav_updates
        updated = []
        for item in pages:
            if isinstance(item, str):
                new_item = item
                for old_path, new_slug in sorted_mapping:
                    old_with_prefix = f"{lang_prefix}{old_path}" if lang_prefix else old_path
                    if item == old_with_prefix:
                        new_item = f"{lang_prefix}{new_slug}" if lang_prefix else new_slug
                        nav_updates += 1
                        break
                updated.append(new_item)
            elif isinstance(item, dict) and "pages" in item:
                item["pages"] = update_pages(item["pages"], lang_prefix)
                updated.append(item)
            else:
                updated.append(item)
        return updated

    # Process each language in navigation
    nav = docs.get("navigation", {})
    languages = nav.get("languages", [])
    for lang_entry in languages:
        lang = lang_entry.get("language", "en")
        lang_prefix = "" if lang == "en" else f"{lang}/"
        groups = lang_entry.get("groups", [])
        for group in groups:
            if "pages" in group:
                group["pages"] = update_pages(group["pages"], lang_prefix)

    # --- 2b: Update redirect destinations to use new flat slugs ---
    redirects = docs.get("redirects", [])
    for redirect in redirects:
        dest = redirect.get("destination", "")
        for old_path, new_slug in sorted_mapping:
            if dest == f"/{old_path}":
                redirect["destination"] = f"/{new_slug}"
                redirect_updates += 1
                break
            matched = False
            for prefix in ["es/", "pt/"]:
                if dest == f"/{prefix}{old_path}":
                    redirect["destination"] = f"/{prefix}{new_slug}"
                    redirect_updates += 1
                    matched = True
                    break
            if matched:
                break

    # --- 2c: Add new redirects from old nested paths to new flat paths ---
    existing_sources = {r["source"] for r in redirects}
    new_redirects = []

    for old_path, new_slug in MAPPING.items():
        # EN redirect
        source = f"/{old_path}"
        if source not in existing_sources:
            new_redirects.append({
                "source": source,
                "destination": f"/{new_slug}",
            })

        # ES redirect
        source_es = f"/es/{old_path}"
        if source_es not in existing_sources:
            new_redirects.append({
                "source": source_es,
                "destination": f"/es/{new_slug}",
            })

        # PT redirect
        source_pt = f"/pt/{old_path}"
        if source_pt not in existing_sources:
            new_redirects.append({
                "source": source_pt,
                "destination": f"/pt/{new_slug}",
            })

    if new_redirects:
        redirects.extend(new_redirects)
        docs["redirects"] = redirects

    # Write back
    with open(docs_path, "w") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return nav_updates, redirect_updates, len(new_redirects)


# ---------------------------------------------------------------------------
# Step 3: Update cross-references in MDX files
# ---------------------------------------------------------------------------

def update_cross_references():
    """Update internal links in all MDX files across EN, ES, PT."""
    # Sort by longest path first to avoid partial matches
    sorted_mapping = sorted(MAPPING.items(), key=lambda x: len(x[0]), reverse=True)

    ref_updates = 0
    files_updated = 0

    # Collect all MDX files
    mdx_files = []
    for prefix in LANG_PREFIXES:
        search_dir = ROOT / prefix.rstrip("/") if prefix else ROOT
        if search_dir.exists():
            for mdx_file in search_dir.glob("**/*.mdx"):
                mdx_files.append(mdx_file)

    for mdx_file in mdx_files:
        with open(mdx_file, "r") as f:
            content = f.read()

        original = content

        for old_path, new_slug in sorted_mapping:
            # Pattern 1: Markdown links  ](/old/nested/path)  ](/old/nested/path#anchor)
            # Matches: ](/ followed by old_path followed by ) or # or " or whitespace before )
            pattern = re.compile(
                r'(\]\(/)' + re.escape(old_path) + r'(\s*[)#"])',
                re.MULTILINE,
            )
            content = pattern.sub(r'\g<1>' + new_slug + r'\2', content)

            # Pattern 2: href="/old/path" in JSX components (exact match)
            pattern_href = re.compile(
                r'(href="/)' + re.escape(old_path) + r'(")',
                re.MULTILINE,
            )
            content = pattern_href.sub(r'\g<1>' + new_slug + r'\2', content)

            # Pattern 3: href="/old/path#anchor" in JSX
            pattern_prop = re.compile(
                r'(href="/)' + re.escape(old_path) + r'(#[^"]*")',
                re.MULTILINE,
            )
            content = pattern_prop.sub(r'\g<1>' + new_slug + r'\2', content)

            # Pattern 4: Links with language prefix in es/pt MDX files
            for lang_prefix in ["es/", "pt/"]:
                pattern_lang = re.compile(
                    r'(\]\(/)' + re.escape(lang_prefix + old_path) + r'(\s*[)#"])',
                    re.MULTILINE,
                )
                content = pattern_lang.sub(
                    r'\g<1>' + lang_prefix + new_slug + r'\2', content
                )

        if content != original:
            with open(mdx_file, "w") as f:
                f.write(content)
            files_updated += 1
            ref_updates += sum(
                1 for a, b in zip(original.splitlines(), content.splitlines()) if a != b
            )

    return files_updated, ref_updates


# ---------------------------------------------------------------------------
# Step 4: Create crisp-redirect-map.json
# ---------------------------------------------------------------------------

def create_crisp_redirect_map():
    """Create crisp-redirect-map.json for CloudFront Function."""
    redirect_map = {
        "en-us": {},
        "es": {},
        "pt-br": {},
        "_fallback": "/",
    }

    for crisp_slug, new_slug in sorted(CRISP_MAPPING.items()):
        if new_slug == "":
            # Empty target -> redirect to home
            redirect_map["en-us"][crisp_slug] = "/"
            redirect_map["es"][crisp_slug] = "/es"
            redirect_map["pt-br"][crisp_slug] = "/pt"
        else:
            redirect_map["en-us"][crisp_slug] = f"/{new_slug}"
            redirect_map["es"][crisp_slug] = f"/es/{new_slug}"
            redirect_map["pt-br"][crisp_slug] = f"/pt/{new_slug}"

    output_path = ROOT / "crisp-redirect-map.json"
    with open(output_path, "w") as f:
        json.dump(redirect_map, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return len(CRISP_MAPPING)


# ---------------------------------------------------------------------------
# Step 5: Clean up empty directories
# ---------------------------------------------------------------------------

def cleanup_empty_dirs():
    """Remove empty directories left behind after moving files."""
    removed = 0
    candidate_dirs = [
        "tests-results", "candidate-guide", "understanding",
        "socratease", "pricing-account",
    ]

    for prefix in LANG_PREFIXES:
        for dir_name in candidate_dirs:
            dir_path = ROOT / f"{prefix}{dir_name}" if prefix else ROOT / dir_name
            if dir_path.exists() and dir_path.is_dir():
                # Walk bottom-up to remove empty subdirectories first
                for dirpath, dirnames, filenames in os.walk(str(dir_path), topdown=False):
                    dp = Path(dirpath)
                    remaining = list(dp.iterdir())
                    if not remaining:
                        result = subprocess.run(
                            ["git", "rm", "-r", str(dp)],
                            cwd=str(ROOT),
                            capture_output=True,
                            text=True,
                        )
                        if result.returncode != 0:
                            try:
                                dp.rmdir()
                                removed += 1
                            except OSError:
                                pass
                        else:
                            removed += 1

                # Check if the top-level dir is now empty
                if dir_path.exists():
                    remaining = list(dir_path.iterdir())
                    if not remaining:
                        try:
                            dir_path.rmdir()
                            removed += 1
                        except OSError:
                            pass

    return removed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("flatten-urls.py - Flatten nested MDX file paths")
    print("=" * 60)
    print()

    # Step 1: Move files
    print("[Step 1] Moving MDX files with git mv...")
    moved, skipped = move_files()
    print(f"  Files moved: {moved}")
    print(f"  Files skipped (already flat or missing): {skipped}")
    print()

    # Step 2: Update docs.json
    print("[Step 2] Updating docs.json navigation and redirects...")
    nav_updates, redirect_dest_updates, new_redirects = update_docs_json()
    print(f"  Navigation references updated: {nav_updates}")
    print(f"  Redirect destinations updated: {redirect_dest_updates}")
    print(f"  New redirects added (old->new): {new_redirects}")
    print()

    # Step 3: Update cross-references
    print("[Step 3] Updating cross-references in MDX files...")
    files_updated, ref_updates = update_cross_references()
    print(f"  MDX files modified: {files_updated}")
    print(f"  References updated: {ref_updates}")
    print()

    # Step 4: Create crisp-redirect-map.json
    print("[Step 4] Creating crisp-redirect-map.json...")
    crisp_entries = create_crisp_redirect_map()
    print(f"  Crisp redirect entries: {crisp_entries}")
    print()

    # Step 5: Clean up empty directories
    print("[Step 5] Cleaning up empty directories...")
    dirs_removed = cleanup_empty_dirs()
    print(f"  Empty directories removed: {dirs_removed}")
    print()

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Files moved:               {moved}")
    print(f"  Navigation updates:        {nav_updates}")
    print(f"  Redirect dest updates:     {redirect_dest_updates}")
    print(f"  New redirects added:       {new_redirects}")
    print(f"  MDX files with ref updates:{files_updated}")
    print(f"  Cross-references updated:  {ref_updates}")
    print(f"  Crisp redirect entries:    {crisp_entries}")
    print(f"  Empty dirs removed:        {dirs_removed}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
