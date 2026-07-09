---
title: "Restrict Test Access to Specific Candidates"
description: "Limit test participation to specific candidates on AutoProctor using link distribution, email restrictions, unique invitation links, or platform access controls."
---

By default, anyone with your test link can take the test. AutoProctor gives you several methods to lock down access so only the candidates you choose can participate.

## Method 1: Selective Link Distribution

The simplest approach is to share the test link only with the candidates who should take the test.

{% stepper %}
{% step %}
### Identify eligible candidates
Determine which candidates should have access to the test.
{% endstep %}
{% step %}
### Share the link privately
Send the test link only to those candidates via email, your learning management system, or another private channel. Avoid posting the link publicly.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
This method relies on candidates not sharing the link with others. If you need stronger access control, use one of the methods below.
{% endhint %}

## Method 2: Email-Based Restrictions

Use AutoProctor's built-in **Login Restrictions** to allow only specific email domains or individual email addresses. You configure this in the Advanced Settings section of your test.

{% stepper %}
{% step %}
### Open Advanced Settings
Navigate to your test settings and scroll to the **Advanced Settings** section.
{% endstep %}
{% step %}
### Enter Login Restrictions
Add the email domains (e.g., `@yourschool.edu`) or specific email addresses you want to allow.
{% endstep %}
{% step %}
### Save the test
Click **Create** or **Update** to apply the restrictions.
{% endstep %}
{% endstepper %}

![Login Restrictions field with domain and email restrictions](images/settings/login-restrictions-email.png)
*Login Restrictions field with domain and email restrictions*

See [Restrict Test Access by Email Address](tests-results/access-limits/restricting-by-email.md) for full setup instructions and examples.

## Method 3: Unique Invitation Links

Generate unique per-candidate URLs tied to specific email addresses. Each candidate receives their own link with email verification, so only the intended recipient can use it.

{% embed url="videos/settings/unique-invitation-links.mp4" %}
Unique invitation links setup
{% endembed %}

{% stepper %}
{% step %}
### Enable Unique URL
Open your test settings and enable the **Unique URL** option.
{% endstep %}
{% step %}
### Upload email addresses
Upload candidate email addresses via a CSV file (up to 1,000 at once).
{% endstep %}
{% step %}
### Generate the unique links
AutoProctor outputs a unique link for each email address as comma-separated pairs.
{% endstep %}
{% step %}
### Format the data
Paste the output into a spreadsheet application and split on the comma separator to organize email addresses and links into separate columns.
{% endstep %}
{% step %}
### Distribute unique links
Send each candidate their unique link individually using the spreadsheet you created.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Unique invitation links are available only on the **Elite Plan** and work with Socratease Quizzes and IFrame Tests. See [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) for plan details.
{% endhint %}

See [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md) for the complete setup process.

## Method 4: Google Forms Access Restrictions

If you use Google Forms, you can restrict access at the Google Forms level instead of (or in addition to) AutoProctor restrictions. Candidates can still open the AutoProctor link, but they cannot proceed if Google Forms blocks their access.

{% stepper %}
{% step %}
### Open your Google Form settings
In Google Forms, click the **Settings** gear icon.
{% endstep %}
{% step %}
### Restrict to your organization
Enable the option to restrict responses to users in your organization. This limits access to candidates with email addresses under your Google Workspace domain.

![Google Forms access restriction settings](images/settings/google-form-restriction.png)
*Google Forms access restriction settings*
{% endstep %}
{% endstepper %}

For more details, refer to [Google's guide on restricting form access](https://www.bettercloud.com/monitor/the-academy/restrict-access-to-google-forms/).

## Comparison of Access Control Methods

| Method | Strength | Works With | Plan Required |
|---|---|---|---|
| Selective link distribution | Low -- relies on trust | All test types | Any |
| Email-based restrictions | Medium -- blocks wrong domains | All test types | Any |
| Unique invitation links | High -- per-candidate verification | Socratease Quizzes, IFrame Tests | Elite |
| Google Forms restrictions | Medium -- organization-level | Google Forms only | Any |

## Related Resources

- [Restrict Test Access by Email Address](tests-results/access-limits/restricting-by-email.md) -- Set up domain and email-based restrictions
- [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md) -- Generate unique per-candidate test links
- [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md) -- Understand available authentication options
- [Advanced Settings](tests-results/create/advanced-settings.md) -- Configure Login Restrictions and other advanced options
- [Best Practices for Test Creators](understanding/getting-started/best-practices-for-teachers.md) -- Tips for smooth test administration
