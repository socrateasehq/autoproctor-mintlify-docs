---
title: "Export Results to Excel"
description: "Download your AutoProctor test results as an Excel spreadsheet for record-keeping, sharing with colleagues, and audit purposes."
---

AutoProctor lets you export your test results to an Excel spreadsheet. This is useful for sharing results with colleagues, maintaining audit records, or storing documentation for your institution.

## What the Export Includes

The exported spreadsheet contains a summary of all candidate results:

| Column | Description |
|---|---|
| **Candidate name** | Name of the test taker |
| **Email address** | Email used to take the test |
| **Test start time** | When the candidate started the test |
| **Submit time** | When the candidate submitted the test |
| **Trust Score** | Proctoring integrity score (if proctoring is enabled) |
| **Quiz score** | Candidate's score (for Socratease Quizzes only) |

![Results table on the AutoProctor dashboard with export option](images/results/export-results-table.png)
*Results table with Export to Excel button*

You can view a [sample exported spreadsheet](https://docs.google.com/spreadsheets/d/1lvkt7n7ZkOushCFYd0ZrTv5YgBAex4CJV78LG88mLx4/edit#gid=0) to see the exact format.

## How to Export

![GIF showing how to export results to Excel from the AutoProctor dashboard](images/results/export-results-to-excel.gif)
*Exporting results to Excel*

{% stepper %}
{% step %}
### Open the results page
Navigate to your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) and click **Results** for the test you want to export.
{% endstep %}
{% step %}
### Click the Export button
Click the **Export to Excel** button at the top of the results table. The file downloads automatically to your device.
{% endstep %}
{% step %}
### Open the file
Open the downloaded `.xlsx` file in Microsoft Excel, Google Sheets, or any compatible spreadsheet application.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
For automatic, ongoing exports without manual downloads, consider setting up the [Google Sheets integration](tests-results/results/google-sheets-integration.md) instead.
{% endhint %}

## Related Resources

- [Google Sheets Integration](tests-results/results/google-sheets-integration.md) -- Automatically write results to a Google Sheet
- [Where Can I See My Quiz Results?](tests-results/results/how-to-see-results.md) -- Overview of quiz results vs. proctoring results
- [Sharing Test Results](tests-results/results/sharing-test-results.md) -- Grant other users access to test results
- [Where Can I See Proctoring Results?](tests-results/results/proctoring-results.md) -- View detailed proctoring reports
