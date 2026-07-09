---
title: "Write Results to Google Sheets"
description: "Set up automatic export of AutoProctor test results to Google Sheets so data flows in real time without manual downloads."
---

Instead of manually downloading Excel files after each test, you can configure AutoProctor to automatically write test results to a Google Sheet. Results appear in the sheet as candidates complete their tests, keeping your data current without any extra effort.

{% hint style="info" %}
This is a **Premium Feature** and requires a Premium or Elite subscription. See [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) for plan details.
{% endhint %}

## Setup Instructions

![GIF showing how to set up Google Sheets integration in AutoProctor](images/settings/write-to-gsheet.gif)
*Setting up Google Sheets integration*

{% stepper %}
{% step %}
### Open test settings
Visit the **Test Settings** for a new or existing test on your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Find the Google Sheets ID field
Scroll down to the **Advanced Settings** section and locate the **Google Sheets ID** field.
{% endstep %}
{% step %}
### Create a blank Google Sheet
Create an empty Google Sheet in your Google Drive. You will use this sheet to receive AutoProctor results.
{% endstep %}
{% step %}
### Grant write access
Share the Google Sheet with `hello@autoproctor.co` and grant **Editor** permissions. This allows AutoProctor to write data to the sheet.

{% hint style="warning" %}
If you do not share the sheet with `hello@autoproctor.co` as an Editor, AutoProctor cannot write results to it. Make sure you grant Editor access, not just Viewer.
{% endhint %}
{% endstep %}
{% step %}
### Paste the Google Sheet URL
Copy the URL of your Google Sheet and paste it into the **Google Sheets ID** field in AutoProctor's test settings.
{% endstep %}
{% step %}
### Save the test
Click **Create** or **Update** to save your test configuration.
{% endstep %}
{% step %}
### Verify the integration
Complete a test attempt. A new sheet tab labeled **AutoProctor** automatically appears in your Google Sheet with the results data.
{% endstep %}
{% endstepper %}

Subsequent test attempts automatically populate the same Google Sheet without any additional setup.

## Socratease Quiz Integration

For Socratease Quizzes, the system writes both proctoring scores and quiz scores to the sheet. However, individual questions and answers are not included -- only aggregate scoring data appears.

{% hint style="info" %}
If you need detailed question-level data for Socratease Quizzes, use the [individual submissions](tests-results/results/individual-submissions.md) view on the [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) instead.
{% endhint %}

## Related Resources

- [Export to Excel](tests-results/results/export-to-excel.md) -- Manually download results as a spreadsheet
- [Access Answers and Candidate Responses](tests-results/results/individual-submissions.md) -- View detailed per-candidate responses
- [Where Can I See My Quiz Results?](tests-results/results/how-to-see-results.md) -- Overview of quiz results vs. proctoring results
- [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) -- Plan details and feature availability
- [Sharing Test Results](tests-results/results/sharing-test-results.md) -- Grant other users access to test results
