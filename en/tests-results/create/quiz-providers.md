---
title: "Quiz Providers"
description: "Learn about the quiz platforms you can use with AutoProctor for proctored online tests."
---

{% hint style="success" %}
AutoProctor adds proctoring to your quiz — you choose the quiz platform. Use **Socratease** to build quizzes inside AutoProctor, or bring your own from Google Forms, Microsoft Forms, or any other platform.
{% endhint %}

## Choosing a Quiz Provider

{% embed url="../../videos/creating-tests/all-test-types.mp4" %}
How to create a test with different quiz providers in AutoProctor. You can only select one provider per test
{% endembed %}

{% stepper %}
{% step %}
### Create a New Test
Go to your [**Dashboard**](https://www.autoproctor.co/test-admin/home/) and click **Create Test**.
{% endstep %}
{% step %}
### Select a Quiz Provider
Choose one of the available providers: **Socratease Quizzes**, **Google Forms**, **Microsoft Forms**, or **IFrame/Other**.
{% endstep %}
{% step %}
### Configure Proctoring
Set up [timer](tests-results/create/timer-settings.md) and [proctoring](tests-results/create/proctoring-settings.md) settings. If you chose Socratease, you also configure your questions and grading within AutoProctor. For external providers, your quiz content stays on that platform.
{% endstep %}
{% endstepper %}

## Available Quiz Providers

| Provider | Best For | Key Advantage |
|---|---|---|
| **Socratease Quizzes** | Full-featured assessments | Native integration with auto-submit protection |
| **Google Forms** | Existing Google Forms users | Dedicated add-on for automatic test creation |
| **Microsoft Forms** | Microsoft ecosystem organizations | Seamless integration for enterprise evaluations |
| **IFrame/Other** | TypeForm, ProProfs, ClassMarker, etc. | Adds proctoring to any web-based quiz platform |

### Socratease Quizzes

Socratease is AutoProctor's **native quizzing tool**. It provides the tightest integration and the best candidate experience:

- **Single submit button** — prevents answer loss from incorrect sequencing
- **Auto-submit protection** — saves answers before the test closes
- **Multiple question types** — MCQs, essays, voice responses, coding, and more
- **Excel bulk import** and **question banks** for fast quiz assembly

### Google Forms

Google Forms is the most widely-used quizzing platform. AutoProctor offers a dedicated [**Google Forms add-on**](https://workspace.google.com/marketplace/app/timer_+_proctor_google_forms_autoproctor/691377974459) that creates a proctored test directly from within your Google Form.

{% hint style="info" %}
With external providers like Google Forms, your questions, points, and grading stay on that platform. AutoProctor only adds the proctoring layer.
{% endhint %}

### Microsoft Forms

Microsoft Forms is the second most-used platform, especially within organizations that rely on the **Microsoft ecosystem** for internal evaluations and hiring assessments.

### IFrame/Other Providers

Hundreds of quiz platforms exist, including TypeForm, ProProfs, and ClassMarker. You can add AutoProctor's proctoring to any of them by selecting **IFrame/Other**. AutoProctor embeds your quiz inside a proctored browser window.

{% hint style="info" %}
When using IFrame/Other providers, you can customize the embedded URL using [query arguments](tests-results/create/iframe-query-arguments.md).
{% endhint %}

## Related Resources

- [Why Socratease?](socratease/create-questions/why-socratease.md) -- Benefits of using AutoProctor's native quiz tool
- [How to Create a Socratease Quiz](socratease/create-questions/creating-a-quiz.md) -- Step-by-step creation guide
- [Timer Settings](tests-results/create/timer-settings.md) -- Configure test duration and time windows
- [Proctoring Settings](tests-results/create/proctoring-settings.md) -- Camera, microphone, and tab-switching options
- [IFrame Query Arguments](tests-results/create/iframe-query-arguments.md) -- Customize embedded quiz URLs
- [Advanced Settings](tests-results/create/advanced-settings.md) -- Login providers, collaborators, and more
