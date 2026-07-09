---
title: "Blank Page or Grey Screen During Test"
description: "Resolve blank page or grey screen issues when loading a proctored test. Usually caused by being signed into the wrong Google account."
---

If your test displays a blank page or grey screen instead of loading the questions, the most common cause is that you are signed into a Google account that does not have access to the test form.

## Why This Happens

When a test administrator restricts access to specific email addresses, Google Forms blocks anyone signed in with a different account. AutoProctor loads the Google Form within its own interface, so you see a blank or grey screen instead of the form's own error message.


![Blank page displayed when the wrong Google account is active in AutoProctor](images/candidate-issues/blank-page-google-account.png)
*Blank page caused by being signed into the wrong Google account*

## How to Fix It

{% stepper %}
{% step %}
### Log out of all Google accounts
Visit [accounts.google.com/Logout](https://accounts.google.com/Logout) to sign out of all your Google accounts.
{% endstep %}
{% step %}
### Sign back in with the correct account
Sign in with the Google account that has been granted access to the test. This is usually the email address your test administrator provided instructions for.
{% endstep %}
{% step %}
### Reload the test
Navigate back to the test link and load it again. The form should now display correctly.
{% endstep %}
{% step %}
### Try using Incognito mode
If the page is still blank, open the test link in an **Incognito window** (`Ctrl+Shift+N` on Windows or `Cmd+Shift+N` on Mac). Incognito starts a fresh session without cached accounts or permissions, which often resolves the issue.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
For detailed setup instructions before taking a test, see:
- [Instructions for Taking a Proctored Test](candidate-guide/attempting/proctored-test-instructions.md) -- Google Account Setup section
- [Instructions for Taking a Timed Test](candidate-guide/attempting/timed-test-instructions.md) -- Google Account Setup section
{% endhint %}

## Related Resources

- [Cannot Click on Answer](tests-results/issues/cannot-click-answer.md) -- Similar issue caused by wrong Google account
- [Cannot See Questions on Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Google Form access issues
- [Test Stuck at Loading Screen](tests-results/issues/loading-screen.md) -- Other loading issues
- [How to Logout](candidate-guide/attempting/how-to-logout.md) -- Steps to switch accounts
- [Device Compatibility](understanding/getting-started/device-compatibility.md) -- Check supported browsers and devices
- [Contact Us](pricing-account/support/contact-us.md) -- Reach out if you need further help
