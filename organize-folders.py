#!/usr/bin/env python3
"""
Organize flat MDX files into section folders while preserving URL slugs via frontmatter.

This script:
1. Creates folders for each section in root, es/, and pt/
2. Moves files with `git mv`
3. Adds `slug` frontmatter to preserve flat URLs
4. Updates docs.json navigation references
5. Prints a summary
"""

import json
import os
import re
import subprocess
import sys

BASE_DIR = "/Users/jayanth/projects/autoproctor-mintlify-docs"

FOLDER_MAP = {
    "create": [
        "create-proctored-exam",
        "supported-quiz-providers",
        "proctoring-settings",
        "enhanced-proctoring",
        "timer-settings",
        "advanced-exam-settings",
        "resume-exam-attempts",
        "resume-google-forms-exam",
        "candidate-instructions-page",
        "archive-and-delete-exams",
        "iframe-query-arguments",
        "google-forms-addon-error",
    ],
    "results": [
        "where-to-find-quiz-results",
        "where-to-find-proctoring-results",
        "access-candidate-responses",
        "view-unsubmitted-exams",
        "export-results-to-excel",
        "write-results-to-google-sheets",
        "share-exam-results",
    ],
    "access": [
        "restrict-access-by-email",
        "restrict-access-to-candidates",
        "invite-candidates-via-email",
        "maximum-exam-attempts",
        "max-simultaneous-candidates",
        "add-collaborators",
    ],
    "issues": [
        "test-stuck-at-loading-screen",
        "blank-screen-during-test",
        "test-slow-and-laggy",
        "cannot-click-answers-during-test",
        "google-forms-questions-not-visible",
        "false-app-switch-alert",
        "no-face-or-multiple-faces-detected",
        "missing-violation-evidence",
        "missing-random-photos",
        "missing-images-and-recordings",
        "what-does-went-offline-mean",
        "incorrect-candidate-name-in-results",
        "google-forms-response-not-visible",
    ],
    "candidate": [
        "take-proctored-exam",
        "take-timed-exam",
        "take-proctored-socratease-quiz",
        "take-timed-socratease-quiz",
        "how-to-submit-quiz",
        "candidate-login-methods",
        "how-to-logout",
    ],
    "understanding": [
        "before-you-get-started",
        "device-compatibility",
        "best-practices-for-exam-creators",
        "faqs",
        "what-gets-tracked-during-proctoring",
        "what-is-trust-score",
        "does-autoproctor-record-video",
    ],
    "socratease": [
        "why-socratease",
        "create-socratease-quiz",
        "socratease-question-types",
        "question-type-availability",
        "import-questions-from-excel",
        "question-banks",
        "socratease-quiz-settings",
        "question-display-mode",
        "show-results-to-candidates",
        "using-tags",
        "latex-math-equations",
    ],
    "pricing": [
        "payments-and-credits",
        "feature-comparison",
        "elite-plan-features",
        "one-time-subscription",
        "cancel-subscription",
        "what-is-a-team",
        "purchased-packs-not-showing",
        "track-credit-usage",
        "invoices-and-receipts",
        "edit-billing-information",
        "contact-us",
        "book-a-demo",
    ],
}

# Language prefixes: root (empty string), es/, pt/
LANG_PREFIXES = ["", "es/", "pt/"]


def create_folders():
    """Step 1: Create folders for each section in root, es/, and pt/."""
    created = []
    for folder in FOLDER_MAP:
        for prefix in LANG_PREFIXES:
            dir_path = os.path.join(BASE_DIR, prefix, folder)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                created.append(dir_path)
                print(f"  Created: {prefix}{folder}/")
    return created


def move_files():
    """Step 2: Move files with git mv."""
    moved = []
    errors = []
    for folder, slugs in FOLDER_MAP.items():
        for slug in slugs:
            for prefix in LANG_PREFIXES:
                src = os.path.join(BASE_DIR, prefix, f"{slug}.mdx")
                dst = os.path.join(BASE_DIR, prefix, folder, f"{slug}.mdx")

                if not os.path.exists(src):
                    errors.append(f"  SKIP (not found): {prefix}{slug}.mdx")
                    continue
                if os.path.exists(dst):
                    errors.append(f"  SKIP (already exists): {prefix}{folder}/{slug}.mdx")
                    continue

                result = subprocess.run(
                    ["git", "mv", src, dst],
                    capture_output=True,
                    text=True,
                    cwd=BASE_DIR,
                )
                if result.returncode != 0:
                    errors.append(f"  ERROR moving {prefix}{slug}.mdx: {result.stderr.strip()}")
                else:
                    moved.append(f"{prefix}{slug}.mdx -> {prefix}{folder}/{slug}.mdx")
                    print(f"  Moved: {prefix}{slug}.mdx -> {prefix}{folder}/{slug}.mdx")

    if errors:
        print("\n  Warnings/Errors during move:")
        for e in errors:
            print(e)

    return moved


def add_slug_frontmatter():
    """Step 3: Add slug frontmatter to each moved file."""
    added = []
    skipped = []

    for folder, slugs in FOLDER_MAP.items():
        for slug in slugs:
            for prefix in LANG_PREFIXES:
                file_path = os.path.join(BASE_DIR, prefix, folder, f"{slug}.mdx")

                if not os.path.exists(file_path):
                    continue

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check if slug already exists in frontmatter
                # Frontmatter is between the first two --- lines
                fm_match = re.match(r"^(---\n)(.*?)(---\n)", content, re.DOTALL)
                if not fm_match:
                    skipped.append(f"  SKIP (no frontmatter): {prefix}{folder}/{slug}.mdx")
                    continue

                fm_open = fm_match.group(1)   # "---\n"
                fm_body = fm_match.group(2)   # frontmatter content
                fm_close = fm_match.group(3)  # "---\n"
                rest = content[fm_match.end():]

                if re.search(r"^slug:", fm_body, re.MULTILINE):
                    skipped.append(f"  SKIP (slug exists): {prefix}{folder}/{slug}.mdx")
                    continue

                # Insert slug after description line, or after title line if no description
                slug_line = f'slug: "{slug}"\n'

                if re.search(r'^description:', fm_body, re.MULTILINE):
                    # Insert after the description line
                    new_fm_body = re.sub(
                        r'(^description:.*\n)',
                        r'\1' + slug_line,
                        fm_body,
                        count=1,
                        flags=re.MULTILINE,
                    )
                elif re.search(r'^title:', fm_body, re.MULTILINE):
                    # Insert after the title line
                    new_fm_body = re.sub(
                        r'(^title:.*\n)',
                        r'\1' + slug_line,
                        fm_body,
                        count=1,
                        flags=re.MULTILINE,
                    )
                else:
                    # Just prepend to frontmatter body
                    new_fm_body = slug_line + fm_body

                new_content = fm_open + new_fm_body + fm_close + rest

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                added.append(f"{prefix}{folder}/{slug}.mdx")
                print(f"  Added slug: {prefix}{folder}/{slug}.mdx -> slug: \"{slug}\"")

    if skipped:
        print("\n  Skipped during slug addition:")
        for s in skipped:
            print(s)

    return added


def build_slug_to_folder_map():
    """Build a lookup from slug to folder for nav updates."""
    mapping = {}
    for folder, slugs in FOLDER_MAP.items():
        for slug in slugs:
            mapping[slug] = folder
    return mapping


def update_nav_pages(obj, slug_to_folder):
    """Recursively update page references in navigation structure.
    
    Changes flat slugs to folder/slug paths:
      - "create-proctored-exam" -> "create/create-proctored-exam"
      - "es/create-proctored-exam" -> "es/create/create-proctored-exam"
      - "pt/create-proctored-exam" -> "pt/create/create-proctored-exam"
    """
    updated = []

    if isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str):
                # This is a page reference string
                new_val = _update_page_ref(item, slug_to_folder)
                if new_val != item:
                    obj[i] = new_val
                    updated.append(f"  {item} -> {new_val}")
            elif isinstance(item, dict):
                updated.extend(update_nav_pages(item, slug_to_folder))
    elif isinstance(obj, dict):
        for key, val in obj.items():
            if key == "pages":
                updated.extend(update_nav_pages(val, slug_to_folder))
            elif key in ("groups", "languages", "tabs"):
                updated.extend(update_nav_pages(val, slug_to_folder))
            # Do NOT recurse into "redirects" - those stay as-is
    return updated


def _update_page_ref(page_ref, slug_to_folder):
    """Update a single page reference string."""
    # Check for lang prefix
    for prefix in ["es/", "pt/"]:
        if page_ref.startswith(prefix):
            bare_slug = page_ref[len(prefix):]
            if bare_slug in slug_to_folder:
                folder = slug_to_folder[bare_slug]
                return f"{prefix}{folder}/{bare_slug}"
            return page_ref

    # EN (no prefix)
    if page_ref in slug_to_folder:
        folder = slug_to_folder[page_ref]
        return f"{folder}/{page_ref}"

    return page_ref


def update_docs_json():
    """Step 4: Update docs.json navigation references."""
    docs_path = os.path.join(BASE_DIR, "docs.json")

    with open(docs_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    slug_to_folder = build_slug_to_folder_map()

    # Update only the navigation section, not redirects
    updated = []
    if "navigation" in data:
        updated.extend(update_nav_pages(data["navigation"], slug_to_folder))
    if "tabs" in data:
        updated.extend(update_nav_pages(data["tabs"], slug_to_folder))

    with open(docs_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")  # trailing newline

    for u in updated:
        print(u)

    return updated


def main():
    print("=" * 60)
    print("AutoProctor Docs — Organize Flat Files into Section Folders")
    print("=" * 60)

    # Step 1
    print("\n[Step 1] Creating folders...")
    created = create_folders()
    print(f"  -> {len(created)} folders created")

    # Step 2
    print("\n[Step 2] Moving files with git mv...")
    moved = move_files()
    print(f"  -> {len(moved)} files moved")

    # Step 3
    print("\n[Step 3] Adding slug frontmatter...")
    slugs_added = add_slug_frontmatter()
    print(f"  -> {len(slugs_added)} slugs added")

    # Step 4
    print("\n[Step 4] Updating docs.json navigation...")
    nav_updated = update_docs_json()
    print(f"  -> {len(nav_updated)} nav references updated")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Folders created:       {len(created)}")
    print(f"  Files moved:           {len(moved)}")
    print(f"  Slugs added:           {len(slugs_added)}")
    print(f"  Nav refs updated:      {len(nav_updated)}")
    print("=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
