---
title: "Inviting Candidates via Email"
description: "Generate unique invitation links tied to specific email addresses for controlled test access with email verification on AutoProctor."
---

Unique invitation links let you generate a distinct test URL for each candidate, tied to their email address. When a candidate opens their link, AutoProctor sends a one-time verification code to confirm their identity before granting access to the test.

{% hint style="info" %}
This feature is available only on the **Elite Plan** and works exclusively with **Socratease Quizzes** and **IFrame Tests**. It is not compatible with Google Forms or Microsoft Forms, as those require platform-specific sign-in. See [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) for plan details.
{% endhint %}

## How to Set Up Unique Invitation Links

{% embed url="../../videos/settings/unique-invitation-links.mp4" %}
How to set up unique invitation links in AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Enable Unique URL
Open your test settings and enable the **Unique URL** option.


{% endstep %}
{% step %}
### Upload email addresses
Upload candidate email addresses via a CSV file. You can upload a maximum of 1,000 email addresses at once.


{% endstep %}
{% step %}
### Get the generated links
AutoProctor generates a text output containing email addresses and their corresponding unique test links as comma-separated columns.


{% endstep %}
{% step %}
### Format the data
Paste the output into a spreadsheet application and split on the comma separator to organize email addresses and links into separate columns.
{% endstep %}
{% step %}
### Distribute links
Send the unique links to your candidates via email, your learning management system, or another distribution method.
{% endstep %}
{% endstepper %}

## How Verification Works

When a candidate clicks their unique link, AutoProctor sends a one-time verification code to the email address associated with that link. The candidate must enter this code to access the test. This ensures only the intended recipient can use each link.


## Important Limitations

| Limitation | Details |
|---|---|
| Standard URL disabled | Once you enable this feature, the standard shared test URL stops working. Only the unique per-candidate URLs grant access. |
| No revocation | You cannot invalidate sent invitations after they are generated. |
| No free trial | This feature cannot be tested before purchasing the Elite Plan. |
| Batch limit | You can upload a maximum of 1,000 email addresses at once. |

{% hint style="warning" %}
After enabling unique URLs, the common test link stops working immediately. Make sure you are ready to distribute the individual links before enabling this feature.
{% endhint %}

## Bulk Email Service

For large-scale campaigns exceeding 5,000 candidates, AutoProctor offers an email distribution service at $100 per 5,000 messages. This requires sufficient account balance and submission of your CSV file and email content to the AutoProctor team. [Contact us](pricing-account/support/contact-us.md) for details.

## Related Resources

- [Restrict Test Access by Email Address](tests-results/access-limits/restricting-by-email.md) -- Alternative method using email domain restrictions
- [Restricting to Specific Candidates](tests-results/access-limits/restricting-to-some-users.md) -- Overview of all access control methods
- [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md) -- Understand authentication options
- [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) -- Plan details and Elite Plan features
- [Elite Features](pricing-account/plans-credits/elite-features.md) -- All features available on the Elite Plan
