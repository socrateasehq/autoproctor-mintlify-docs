---
title: Restrict Test Access by Email Address
description: >-
  Limit who can take your test by restricting access to specific email domains
  or individual email addresses using Login Restrictions.
---

# Restrict Test Access by Email Address

Login Restrictions let you control exactly who can take your test by filtering candidates based on their email address. This prevents unauthorized access even if someone shares or discovers your test link.

### How to Set Up Email Restrictions

{% stepper %}
{% step %}
#### Open your test settings

Navigate to the test on your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/) and click the **Settings** button.
{% endstep %}

{% step %}
#### Go to Advanced Settings

Scroll down to the **Advanced Settings** section and locate the **Login Restrictions** fields.
{% endstep %}

{% step %}
#### Add domain or email restrictions

Enter the email domains or specific email addresses you want to allow. You can combine both types of restrictions in a single field (see examples below).
{% endstep %}

{% step %}
#### Save the test

Click **Create** or **Update** to apply the restrictions.
{% endstep %}
{% endstepper %}

### Domain-Based Restrictions

You can restrict access to candidates whose email addresses end with specific domains. For example, entering `@abc.com` and `@xyz.com` allows only candidates with those email domains to take the test.

![Login Restrictions field showing domain-based restrictions with @abc.com and @xyz.com entered](../../.gitbook/assets/login-restrictions-domain.png)

### Specific Email Restrictions

You can also permit individual email addresses alongside domain restrictions. This is useful when most candidates share a domain but a few external participants need access.

For example, you can allow all users whose email ends with `@abc.com` plus specific individual email addresses like `guest@gmail.com`.

![Login Restrictions field showing a combination of domain and individual email restrictions](../../.gitbook/assets/login-restrictions-email.png)

{% hint style="info" %}
Email restrictions work in conjunction with the candidate's [login method](candidate-guide/attempting/candidate-login-methods.md). The candidate must sign in with an email address that matches one of the allowed domains or addresses you specified.
{% endhint %}

### Related Resources

* [Candidate Login Methods](candidate-guide/attempting/candidate-login-methods.md) -- Understand available authentication options for candidates
* [Restricting to Specific Users](tests-results/access-limits/restricting-to-some-users.md) -- Other methods for limiting test access
* [Inviting Candidates via Email](tests-results/access-limits/inviting-candidates-via-email.md) -- Generate unique per-candidate test links
* [Advanced Settings](tests-results/create/advanced-settings.md) -- Configure Login Restrictions and other advanced test options
* [Best Practices for Test Creators](understanding/getting-started/best-practices-for-teachers.md) -- Tips for smooth test administration
