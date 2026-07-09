---
title: "Missing Images and Recordings in Report"
description: "Understand why images or audio recordings may not appear in a candidate's test report despite violations being listed, and how to fix it."
---

If you can see violations listed in a candidate's test report but cannot see the supporting evidence (images or audio recordings), there are two possible scenarios, each with a different cause and resolution.

## Scenario 1: No Images or Recordings at All

If no images or recordings appear despite violations being listed, the evidence recording feature was likely disabled in your test settings.

{% stepper %}
{% step %}
### Check your test settings
Navigate to your test's proctoring configuration in the [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) and verify that evidence recording is enabled. See [Proctoring Settings](tests-results/create/proctoring-settings.md) for details on each option.
{% endstep %}
{% step %}
### Enable evidence recording for future tests
If evidence recording was disabled, enable it for future tests. Note that this change will not retroactively add evidence to tests that have already been taken.
{% endstep %}
{% endstepper %}


## Scenario 2: Some Violations Have Evidence, Others Do Not

If some violations show evidence files while others do not, this is expected behavior. AutoProctor stores a fixed number (approximately 20) of images and audio files per test attempt. When violations exceed this limit, not every violation will have an associated evidence file.

| What You See | What It Means |
|---|---|
| No evidence files at all | Evidence recording is likely disabled in test settings |
| Some violations have files, others do not | Storage limit reached -- normal behavior |

{% hint style="warning" %}
**All violations are tracked and affect the Trust Score**, even when evidence files are not stored for viewing. The evidence files are a subset -- they exist so you can review what happened, but the Trust Score calculation considers every detected violation regardless of whether evidence was stored.
{% endhint %}

## Related Resources

- [Proctoring Settings](tests-results/create/proctoring-settings.md) -- Configure evidence storage and proctoring options
- [Missing Violation Evidence](tests-results/issues/missing-violation-evidence.md) -- Detailed explanation of evidence storage limits
- [Missing Random Photos](tests-results/issues/missing-random-photos.md) -- Why random photos may be absent
- [Proctoring Results](tests-results/results/proctoring-results.md) -- How to review proctoring reports
- [Understanding Trust Score](understanding/how-proctoring-works/trust-score.md) -- How Trust Scores are calculated
- [Contact Us](pricing-account/support/contact-us.md) -- Reach out if you need further help
