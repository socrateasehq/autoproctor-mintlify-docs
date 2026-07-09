---
title: "Question Display Mode"
description: "Control how questions are displayed to candidates -- all at once, one-by-one with navigation, or one-by-one without navigation."
---

The Question Display Mode setting controls how questions appear to your test takers. You can choose between three display options, each with different implications for navigation, timing, and test security.

{% hint style="info" %}
Question Display Mode is a **Premium** feature. See [Payments and Credits](pricing-account/plans-credits/payments-and-credits.md) for plan details.
{% endhint %}

## Display Modes

![Question display mode settings panel showing the three available options](images/socratease/question-display-mode.png)
*Question display mode setting in quiz settings*

### 1. All-at-once (Google Forms style)

Candidates see all the questions at the same time, one below the other, like a Google Form. The timer applies to the **entire test**. Candidates can scroll freely between questions and answer them in any order.

![Candidate view of all-at-once display mode showing all questions on one page](images/socratease/all-at-once.png)
*All-at-once display mode*

### 2. One-by-one with navigation (Typeform style)

Candidates see one question at a time and can navigate back and forth between questions. The timer applies to the **entire test**, not to individual questions. Candidates can revisit and change their answers at any point before submitting.

![Candidate view of one-by-one with navigation display mode showing a single question with Next and Previous buttons](images/socratease/one-by-one-like-typeform.png)
*One-by-one with navigation*

### 3. One-by-one without navigation

Candidates see one question at a time. Once they submit a question (by attempting or skipping it), they **cannot go back to it**. The timer is set **per question**, not for the entire test.

![Candidate view of one-by-one without navigation display mode showing a single question with Submit and Skip buttons](images/socratease/one-by-one.png)
*One-by-one without navigation*

## Key Differences

| Feature | All-at-once | One-by-one with nav | One-by-one without nav |
|---|:---:|:---:|:---:|
| Timer scope | Entire test | Entire test | Per question |
| Can go back to previous questions | Yes | Yes | No |
| Custom instructions | Yes | No | No |

## When to Use One-by-one Without Navigation

The no-navigation option is especially useful for test security. Candidates can view only one question at a time for a limited duration, which significantly reduces the opportunity to cheat. Each question has its own timer, so candidates cannot spend extra time on difficult questions by rushing through easier ones.

## How Timer Settings Change

{% hint style="warning" %}
When you use **one-by-one without navigation**, certain test-level timer settings become unavailable. The timer behavior shifts to the question level:

- **Duration**: You set the duration per question, not for the entire test
- **Auto-Submit**: Each question auto-submits when its individual timer expires
- **Must Submit By**: This test-level setting is replaced by **Cannot Start After** at the test level
{% endhint %}

For more information on timer configuration, see [Timer Settings](tests-results/create/timer-settings.md).

## How to Set the Display Mode

{% embed url="videos/socratease/question-display-mode.mp4" %}
How to set the question display mode
{% endembed %}

{% stepper %}
{% step %}
### Open Your Quiz
Open the Socratease Quiz you want to configure from your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Go to Settings
Click the **Settings** icon (gear) in the quiz editor toolbar.
{% endstep %}
{% step %}
### Select Display Mode
Choose your preferred display mode from the **Question Display Mode** dropdown. The default is "All-at-once."


{% endstep %}
{% endstepper %}

## Related Resources

- [Quiz Settings](socratease/settings/quiz-settings.md) -- All Socratease quiz configuration options
- [Timer Settings](tests-results/create/timer-settings.md) -- Configure test-level and question-level timers
- [How to Create a Socratease Quiz](socratease/create-questions/creating-a-quiz.md) -- Step-by-step creation guide
- [Showing Results to Candidates](socratease/settings/showing-results-to-candidates.md) -- Control result visibility
