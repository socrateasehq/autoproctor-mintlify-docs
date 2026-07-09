---
title: "Missing Random Photos in Report"
description: "Understand why random photos may not appear in a candidate's proctoring report and how the random photo capture system works during tests."
---

Random photos are captured at unpredictable moments during a test to provide unbiased evidence of the candidate's environment and behavior. If you do not see random photos in a proctoring report, the candidate likely submitted the test before the system had a chance to capture them.

## Why Random Photos Matter

Random photos serve as an independent verification tool. Unlike violation-triggered photos (which are taken when an anomaly is detected), random photos capture the candidate at arbitrary moments. This helps you verify that the candidate was present, alone, and following test rules throughout the entire session -- not just when a violation occurred.

## Why Random Photos Are Missing

AutoProctor schedules random photo captures at unpredictable times throughout the test duration. If a candidate submits the test before any of the scheduled capture times, no random photos will be recorded.

**Example:** For a test with a 5-minute duration, the system might schedule photo captures at 2:00, 4:15, and 4:45. If the candidate submits the test at 1:30, the system has not yet reached any of the scheduled capture times, so no random photos appear in the report.

{% hint style="info" %}
Random photos only appear if the candidate was actively taking the test at the time the system scheduled the capture. If the test was submitted before any scheduled captures, no random photos will be available.
{% endhint %}

## How to Reduce the Chance of Missing Random Photos

If random photos are important for your proctoring workflow, consider the following approaches:

| Approach | How It Helps |
|---|---|
| Set a minimum test duration | Longer tests give the system more opportunities to capture random photos |
| Add more questions to your test | More questions typically mean longer test-taking times |
| Require candidates to use the full time | Discourages early submission before photos can be captured |

## Related Resources

- [What Gets Tracked](understanding/how-proctoring-works/what-gets-tracked.md) -- All events AutoProctor monitors during a test
- [Proctoring Results](tests-results/results/proctoring-results.md) -- How to review proctoring reports
- [Missing Violation Evidence](tests-results/issues/missing-violation-evidence.md) -- Why violation evidence may be absent
- [Missing Images and Recordings](tests-results/issues/missing-images-and-recordings.md) -- Other causes of missing media
- [Proctoring Settings](tests-results/create/proctoring-settings.md) -- Configure proctoring options for your test
- [Contact Us](pricing-account/support/contact-us.md) -- Reach out if you need further help
