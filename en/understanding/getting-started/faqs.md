---
title: "Frequently Asked Questions"
description: "Answers to the most common questions about AutoProctor's proctoring platform, pricing, and capabilities."
---

Find answers to the most frequently asked questions about AutoProctor below. If your question is not covered here, [contact our support team](pricing-account/support/contact-us.md).

<AccordionGroup>
  <Accordion title="How does AutoProctor ensure the integrity of online tests?">
    AutoProctor uses on-device AI monitoring that accesses cameras, microphones, and screens (with the candidate's permission) to detect problematic behaviors. These include unauthorized persons in the frame, background noise, and attempts to navigate away from the test screen. Each incident generates a detailed violation report with evidence for you to review.

    Learn more about [what gets tracked](understanding/how-proctoring-works/what-gets-tracked.md) during proctoring.
  </Accordion>

  <Accordion title="How do I create and manage tests on AutoProctor?">
    You create a proctored test in five steps:

{% stepper %}
{% step %}
### Create a quiz
Build your quiz using Google Forms, Microsoft Forms, or [Socratease](socratease/create-questions/why-socratease.md).
{% endstep %}
{% step %}
### Register the test on AutoProctor
Sign in to AutoProctor and register your quiz URL, or create a Socratease quiz directly on the platform.
{% endstep %}
{% step %}
### Configure your proctoring settings
Set up camera tracking, microphone monitoring, screen sharing, and other options in your [proctoring settings](tests-results/create/proctoring-settings.md).
{% endstep %}
{% step %}
### Share the test link with candidates
Distribute the unique AutoProctor test link to your candidates via email, LMS, or any messaging tool.
{% endstep %}
{% step %}
### Review violation reports
After the test, review [proctoring results](tests-results/results/proctoring-results.md) and [Trust Scores](understanding/how-proctoring-works/trust-score.md) for each candidate.
{% endstep %}
{% endstepper %}

    For a full walkthrough, see the [Quickstart guide](tests-results/create/your-first-proctored-test.md).
  </Accordion>

  <Accordion title="What are the pricing plans for AutoProctor?">
    AutoProctor offers three subscription tiers:

    | Plan | What You Get |
    |---|---|
    | **Standard** | 150 proctored credits per billing cycle, plus unlimited timer-only attempts |
    | **Premium** | Standard features plus team collaboration capabilities |
    | **Elite** | Premium features plus advanced question types, question banks, and API/SDK access |

    All plans include a **10-credit free trial** with no credit card required. You can cancel anytime.

    Visit the [pricing page](https://www.autoproctor.co/pricing/) for current rates, or see [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) for details on how credits work.
  </Accordion>

  <Accordion title="How many candidates can take a proctored test simultaneously?">
    AutoProctor supports up to **5,000 concurrent candidates** on a single test.

{% hint style="info" %}
If you anticipate more than 5,000 candidates taking a test at the same time, [contact us](pricing-account/support/contact-us.md) at least two business days in advance so we can prepare our infrastructure.
{% endhint %}

    Learn more about [concurrency limits](tests-results/access-limits/concurrency.md).
  </Accordion>

  <Accordion title="How does AutoProctor protect user privacy and data?">
    AutoProctor collects names, email addresses, images, and audio recordings exclusively for test integrity purposes. The company does not sell personal information or share it with third parties beyond necessary subprocessors.

    Key privacy facts:
    - All AI monitoring happens **on the candidate's device** -- no full video recordings are uploaded to servers
    - Data is used solely for generating proctoring reports
    - Candidates under 18 require parental or guardian consent

{% hint style="info" %}
AutoProctor does not record full video. See [Does AutoProctor Record Video?](understanding/how-proctoring-works/video-recording.md) for details on how the on-device monitoring approach protects candidate privacy.
{% endhint %}
  </Accordion>

  <Accordion title="What quiz platforms does AutoProctor support?">
    AutoProctor works with the following quiz platforms:

    - **Google Forms**
    - **Microsoft Forms**
    - **Socratease** (AutoProctor's built-in quiz platform)
    - **Any web-based quiz** via iframe embedding

    See [Quiz Providers](tests-results/create/quiz-providers.md) for setup instructions for each platform.
  </Accordion>

  <Accordion title="Can I restrict who can take my test?">
    Yes. AutoProctor offers several access control options:

    - **[Restrict by email domain](tests-results/access-limits/restricting-by-email.md)** -- Allow only candidates with specific email domains (e.g., @university.edu)
    - **[Restrict to specific users](tests-results/access-limits/restricting-to-some-users.md)** -- Allow only a pre-approved list of email addresses
    - **[Invite candidates via email](tests-results/access-limits/inviting-candidates-via-email.md)** -- Send direct invitations to specific candidates

    You configure these options in your [advanced settings](tests-results/create/advanced-settings.md).
  </Accordion>
</AccordionGroup>

## Related Resources

- [Quickstart](tests-results/create/your-first-proctored-test.md) -- Create your first proctored test in under 5 minutes
- [What Gets Tracked](understanding/how-proctoring-works/what-gets-tracked.md) -- All monitoring capabilities available
- [Trust Score](understanding/how-proctoring-works/trust-score.md) -- How AutoProctor scores candidate integrity
- [Device Compatibility](understanding/getting-started/device-compatibility.md) -- Supported browsers and devices
- [Contact Us](pricing-account/support/contact-us.md) -- Get help from the AutoProctor support team
- [Book a Demo](pricing-account/support/booking-a-demo.md) -- Schedule a live walkthrough of AutoProctor
