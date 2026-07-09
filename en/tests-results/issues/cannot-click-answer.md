---
title: "Cannot Click on Answers in Test Form"
description: "Fix the issue where your test form loads but you cannot click on questions or select answers. Usually caused by being signed into the wrong Google account."
---

If you can see the test form but cannot click on questions or select answers, you are most likely signed into a Google account that does not have permission to interact with the form.

## Why This Happens

When a Google Form is restricted to specific email addresses, it loads in a read-only preview mode for unauthorized accounts. You can see the questions but cannot interact with them. Since AutoProctor embeds the Google Form within its interface, this restriction appears inside the AutoProctor test window.

![Google Form in AutoProctor that cannot be clicked because the wrong Google account is active](images/candidate-issues/cannot-click-form.png)
*Test form loaded in read-only mode due to incorrect Google account*

## How to Fix It

{% stepper %}
{% step %}
### Log out of all Google accounts
Visit [accounts.google.com/Logout](https://accounts.google.com/Logout) and sign out of all your accounts.
{% endstep %}
{% step %}
### Sign in with the correct account
Sign back in with the Google account that has been granted access to the test. Check with your test administrator if you are unsure which account to use.
{% endstep %}
{% step %}
### Reload the test
Navigate back to the test link and load it again. You should now be able to click on questions and select answers.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you are unsure which Google account has access, contact your test administrator. They can confirm the email address that was granted permission to take the test.
{% endhint %}

## Related Resources

- [Blank Page or Grey Screen](tests-results/issues/blank-page-grey-screen.md) -- Similar issue caused by wrong Google account
- [Cannot See Questions on Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Google Form access restrictions
- [How to Logout](candidate-guide/attempting/how-to-logout.md) -- Steps to switch accounts
- [Instructions for Taking a Proctored Test](candidate-guide/attempting/proctored-test-instructions.md) -- Setup guide with Google Account section
- [Device Compatibility](understanding/getting-started/device-compatibility.md) -- Check supported browsers and devices
- [Contact Us](pricing-account/support/contact-us.md) -- Reach out if you need further help
