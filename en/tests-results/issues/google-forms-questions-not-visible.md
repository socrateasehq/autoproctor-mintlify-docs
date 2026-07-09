---
title: "Cannot See Questions on Google Forms"
description: "Understand why questions may not be visible on a Google Form loaded through AutoProctor and how to resolve access restriction errors."
---

AutoProctor loads your Google Form within its own site for proctoring. If the Google Form has an access restriction or other error, that same error message appears inside the AutoProctor interface. AutoProctor cannot control or modify anything inside the Google Form due to privacy restrictions.

## Why Questions Are Not Visible

Google Forms can restrict access based on organization, email domain, or specific accounts. When you are signed in with an account that does not meet these restrictions, Google blocks the form content and shows an error message instead.


![Google Form displaying access restricted error inside AutoProctor interface](images/candidate-issues/google-forms-access-restricted.png)
*Google Form showing an access restriction message within AutoProctor*

## How to Fix It

{% stepper %}
{% step %}
### Check the error message
Read the error message displayed on the form. It typically explains whether the form is restricted to certain users or an organization.
{% endstep %}
{% step %}
### Sign in with the correct account
Log out of your current Google account at [accounts.google.com/Logout](https://accounts.google.com/Logout), then sign in with the account that has access to the form.
{% endstep %}
{% step %}
### Contact the form creator if needed
If you are unsure which account to use or believe you should have access, contact the person who created the test. They may need to update the form's sharing settings.
{% endstep %}
{% endstepper %}

## Why AutoProctor Cannot Fix This

Due to privacy restrictions, Google does not allow AutoProctor to access or modify anything inside a Google Form. AutoProctor can only load the form -- it cannot control the form's content, access settings, or error messages. If you encounter a form access issue, only the form creator can resolve it.

{% hint style="info" %}
AutoProctor embeds Google Forms similarly to how websites embed YouTube videos. If a YouTube video shows an error on an external site, the issue is with YouTube, not the embedding site. The same applies to Google Forms on AutoProctor -- any errors you see originate from Google, not from AutoProctor.
{% endhint %}

## Related Resources

- [Cannot See Response in Google Form](tests-results/issues/google-forms-response-not-visible.md) -- Missing responses after submission
- [Cannot Click on Answer](tests-results/issues/cannot-click-answer.md) -- Form loads but is not interactive
- [Blank Page or Grey Screen](tests-results/issues/blank-page-grey-screen.md) -- Form does not load at all
- [Instructions for Taking a Proctored Test](candidate-guide/attempting/proctored-test-instructions.md) -- Setup guide with Google Account section
- [How to Logout](candidate-guide/attempting/how-to-logout.md) -- Steps to switch accounts
- [Contact Us](pricing-account/support/contact-us.md) -- Reach out if you need further help
