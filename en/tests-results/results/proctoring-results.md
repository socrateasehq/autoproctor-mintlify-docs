---
title: "Where Can I See Proctoring Results?"
description: "Access and review proctoring results for your tests on AutoProctor, including Trust Scores, violation details, and candidate-level reports."
---

After candidates complete a proctored test, AutoProctor compiles their monitoring data into a proctoring report. This guide walks you through accessing and interpreting those results.

{% hint style="warning" %}
Proctoring results are only generated when you enable proctoring in your [test settings](tests-results/create/proctoring-settings.md). If you configured your test with only a timer, no proctoring data is available.
{% endhint %}

## Viewing Proctoring Results

{% stepper %}
{% step %}
### Open the results page
Navigate to your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) and click the **Results** button for the test you want to review.

![Results button highlighted on the AutoProctor dashboard](images/results/results-button-dashboard.png)
*Results button on the AutoProctor dashboard*
{% endstep %}
{% step %}
### Review the results table
The results page displays a table listing all submissions. Each row includes:

- Candidate name and email address
- Test start and finish time
- Trust Score (indicating proctoring integrity)
- Quiz score (for Socratease Quizzes only)

![Results table showing candidate submissions with Trust Scores](images/results/results-table.png)
*Results table*
{% endstep %}
{% step %}
### View the proctoring summary
Click on a candidate's **Trust Score** to open their detailed proctoring summary. This page lists all violations detected during the test, including screenshots, timestamps, and evidence.

![Proctoring summary page showing detected violations and evidence](images/results/proctoring-summary.png)
*Proctoring summary page*
{% endstep %}
{% endstepper %}

## What the Proctoring Summary Shows

The proctoring summary for each candidate includes:

| Data Point | Description |
|---|---|
| **Trust Score** | An overall integrity rating based on detected violations |
| **Violations list** | Each violation type with timestamp and evidence |
| **Screenshots** | Random photos captured during the test session |
| **Recordings** | Screen and webcam recordings (if enabled in [enhanced proctoring](tests-results/create/enhanced-proctoring.md)) |
| **Session timeline** | When the candidate started, paused, or submitted the test |

## Related Resources

- [Where Can I See My Quiz Results?](tests-results/results/how-to-see-results.md) -- Overview of quiz results vs. proctoring results
- [Trust Score Explained](understanding/how-proctoring-works/trust-score.md) -- How Trust Scores are calculated
- [What Gets Tracked](understanding/how-proctoring-works/what-gets-tracked.md) -- What AutoProctor monitors during a proctored test
- [Export to Excel](tests-results/results/export-to-excel.md) -- Download proctoring results as a spreadsheet
- [Unsubmitted Tests](tests-results/results/unsubmitted-tests.md) -- View details of tests started but not submitted
