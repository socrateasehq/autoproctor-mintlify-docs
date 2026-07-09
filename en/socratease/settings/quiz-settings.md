---
title: "Socratease Quiz Settings"
description: "Configure your Socratease quiz with settings for display mode, result visibility, randomization, and more."
---

Socratease has its own set of configurable settings, distinct from the general Timer and Proctor settings on AutoProctor. These settings control how the quiz behaves for your candidates -- from how questions appear to whether candidates can copy and paste.


## Available Settings

### 1. Question Display Mode (Premium)

Control how questions appear to candidates: all at once (Google Forms style), one-by-one with navigation (Typeform style), or one-by-one without navigation. This setting also affects how timers work.

For more details, see [Question Display Mode](socratease/settings/question-display-mode.md).

### 2. Result Visibility

Control when candidates see their scores and results:
- **Immediately** after submission
- **When you release individual scores** (one candidate at a time)
- **When you release all scores** (everyone at once)
- **Never** -- results are withheld entirely

For more details, see [Showing Results to Candidates](socratease/settings/showing-results-to-candidates.md).

### 3. Question Randomization

Randomize the order of questions for each candidate. What Candidate 1 sees as Question 1 may be Question 10 for Candidate 2. This reduces the opportunity for candidates to share answers during a test.

{% hint style="info" %}
This option is only available when you use the [All-at-once (Google Forms style)](socratease/settings/question-display-mode.md) mode.
{% endhint %}


### 4. Choice Shuffling

For MCQ and MCA type questions, you can randomize the order of answer options across candidates. Even if two candidates see the same question, the choices appear in a different order.


### 5. Copy and Paste Restriction

When you enable this setting, candidates cannot copy question text from the quiz or paste text from a different tab or application into the quiz. This reduces reliance on external tools and AI assistants.


### 6. Tab-Switch Auto-Submit

Set the maximum number of tab switches permitted during the test. If a candidate exceeds this limit, their test is automatically submitted. This discourages candidates from switching to other tabs to look up answers.

{% hint style="warning" %}
When a test auto-submits due to tab-switch limits, the candidate cannot resume the test. Make sure to communicate the tab-switch policy to your candidates beforehand.
{% endhint %}


### 7. Custom Instructions

Add general test guidance that displays to candidates before they start the quiz. Use this to communicate important rules, instructions, or expectations.

{% hint style="info" %}
Custom instructions are available only when you use the **all-at-once** question display mode.
{% endhint %}


### 8. LaTeX Support

If you want to include mathematical equations, write them using LaTeX syntax and they render automatically as formatted equations. Enable this setting to activate LaTeX rendering in your quiz.

For more details, see [Using LaTeX for Math Equations](socratease/settings/latex-math-equations.md).

## How to Access Quiz Settings

{% embed url="../../videos/socratease/soc-quiz-settings.mp4" %}
How to access and configure Socratease quiz settings
{% endembed %}

{% stepper %}
{% step %}
### Open Your Quiz
Open the Socratease Quiz you want to configure from your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Click the Settings Icon
Click the **Settings** icon (gear) in the quiz editor toolbar.
{% endstep %}
{% step %}
### Adjust Your Settings
Modify any of the eight settings listed above. Changes save automatically.
{% endstep %}
{% endstepper %}

## Related Resources

- [Question Display Mode](socratease/settings/question-display-mode.md) -- Detailed explanation of display options
- [Showing Results to Candidates](socratease/settings/showing-results-to-candidates.md) -- Control result visibility
- [Using LaTeX for Math Equations](socratease/settings/latex-math-equations.md) -- Add mathematical equations to your quizzes
- [Timer Settings](tests-results/create/timer-settings.md) -- For general test timer and proctoring configuration (separate from Socratease quiz settings)
- [Creating a Quiz](socratease/create-questions/creating-a-quiz.md) -- Step-by-step guide to creating a quiz
