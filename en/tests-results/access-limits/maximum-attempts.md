---
title: "Maximum Attempts for a Test"
description: "Configure how many times candidates can attempt a test on AutoProctor and understand how attempt tracking works across login methods."
---

The **Max Attempts** setting lets you control how many times each candidate can take a specific test. Once a candidate reaches the limit, AutoProctor blocks further attempts and displays a notification.

## How to Configure Maximum Attempts

{% embed url="videos/settings/max-attempts-settings.mp4" %}
How to configure maximum attempts in AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Open test settings
Navigate to your test on the [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) and click the **Settings** button.
{% endstep %}
{% step %}
### Set the Max Attempts value
In the **Main Settings** section, locate the **Max Attempts** field and enter the number of allowed attempts.
{% endstep %}
{% step %}
### Save the test
Click **Create** or **Update** to apply the setting.
{% endstep %}
{% endstepper %}

When a candidate exceeds their allowed attempts, they see a restriction message and cannot proceed.


![Restriction message shown to candidates](images/settings/max-attempts-blocked.png)
*Restriction message shown to candidates*

## Recommended Configuration

| Test Type | Recommended Max Attempts | Reason |
|---|---|---|
| Google Forms | 1 | AutoProctor [automatically resumes](tests-results/create/resuming-test-attempts.md) these tests if candidates reload or revisit the link |
| Socratease Quiz | 1 | AutoProctor [automatically resumes](tests-results/create/resuming-test-attempts.md) these tests if candidates reload or revisit the link |
| Microsoft Forms | Based on your needs | Each visit creates a new attempt; resumption is not supported |
| IFrame Tests | Based on your needs | Configurable resume behavior; adjust attempts accordingly |

{% hint style="info" %}
For Google Forms and Socratease Quizzes, set **Max Attempts** to **1**. AutoProctor automatically [resumes these tests](tests-results/create/resuming-test-attempts.md) if candidates reload the page or revisit the link, so multiple attempts are not needed for resumption.
{% endhint %}

## How Attempts Are Tracked

AutoProctor tracks attempts by the email address used to sign in. This means:

- Each unique email address counts as a separate candidate, regardless of who is behind it.
- If a candidate signs in with different email addresses across attempts (for example, using **Sign in with Google** once and **Sign in with Email** another time with a different address), each email counts separately, effectively bypassing the attempt limit.

{% hint style="warning" %}
If a candidate uses different login methods that resolve to different email addresses, each one counts as a separate candidate. This can allow them to bypass the maximum attempts limit.
{% endhint %}

## Preventing Attempt Limit Bypass

To prevent candidates from circumventing the maximum attempts setting:

- **Restrict login methods** -- Choose a test type that supports only one sign-in option. Google Forms restricts candidates to Google sign-in only, and Microsoft Forms restricts to Microsoft sign-in only. See [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md).
- **Use email restrictions** -- Limit access to specific email domains or addresses so candidates cannot use alternative accounts. See [Restrict Test Access by Email Address](tests-results/access-limits/restricting-by-email.md).
- **Use unique invitation links** -- Generate per-candidate URLs that enforce email verification. See [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md).

## Related Resources

- [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md) -- How login methods affect attempt tracking
- [Resuming Test Attempts](tests-results/create/resuming-test-attempts.md) -- How test resumption works across test types
- [Restrict Test Access by Email Address](tests-results/access-limits/restricting-by-email.md) -- Limit access by email domain or address
- [Timer Settings](tests-results/create/timer-settings.md) -- Configure test duration and time windows
- [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md) -- Send unique test links to candidates
