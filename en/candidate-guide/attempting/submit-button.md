---
title: "Submit Button: Socratease vs Other Quizzes"
description: "Understand the key differences in how submission works between Socratease quizzes and other quiz types on AutoProctor, and why Socratease eliminates the risk of lost answers."
---

The submission process differs depending on which quiz provider you use. Socratease quizzes use a single submit button, which eliminates the risk of answer loss. Other quiz types (Google Forms, Microsoft Forms, etc.) require two submit buttons clicked in the correct order.

## Non-Socratease Quizzes (Google Forms, Microsoft Forms, etc.)

When AutoProctor embeds external forms, you must **submit twice** because privacy restrictions prevent external platforms from notifying AutoProctor when a submission occurs:

{% stepper %}
{% step %}
### Click the purple submit button first
Click the **purple submit button** at the bottom of the form to save your quiz answers to the quiz provider (Google Forms, Microsoft Forms, etc.).
{% endstep %}
{% step %}
### Click the green submit button second
Click the **green submit button** at the top of the page to submit the proctoring or timed session to AutoProctor.
{% endstep %}
{% endstepper %}

![Proctored test requiring candidates to click two separate submit buttons](images/taking-tests/submit-buttons-proctored.png)
*Other platforms: dual submit buttons*

{% hint style="warning" %}
If you do not submit the quiz answers **first** (purple button), all your answers will be lost. This cannot be recovered. Due to privacy restrictions, Google and Microsoft do not allow AutoProctor to detect whether the purple submit button was clicked, so AutoProctor cannot enforce this step automatically.
{% endhint %}

## Socratease Quizzes

Socratease quizzes use a **single submit button**. One click submits both your answers and the proctoring session -- no confusion, no risk of answer loss.

![Socratease quiz showing a single Submit button at the bottom](images/taking-tests/soc-submit-button.png)
*Socratease: single submit button*

{% hint style="info" %}
Socratease Quizzes are available on **all plans**, including the free trial. See [Why Socratease?](socratease/create-questions/why-socratease.md) for more benefits.
{% endhint %}

## Comparison

| Feature | Non-Socratease (Google Forms, etc.) | Socratease |
|---|---|---|
| Number of submit buttons | 2 (purple then green) | 1 |
| Risk of lost answers | Yes, if buttons clicked in wrong order | None |
| Why two buttons? | Privacy restrictions prevent external platforms from notifying AutoProctor | Not applicable -- Socratease is built into AutoProctor |

## Related Resources

- [Proctored Test Instructions](candidate-guide/attempting/proctored-test-instructions.md) -- Full guide for proctored tests
- [Timed Test Instructions](candidate-guide/attempting/timed-test-instructions.md) -- Full guide for timed tests
- [Proctored Socratease Instructions](candidate-guide/attempting/proctored-socratease-instructions.md) -- Simpler guide for Socratease
- [Google Forms Response Not Visible](tests-results/issues/google-forms-response-not-visible.md) -- Troubleshoot missing submissions
- [Why Socratease?](socratease/create-questions/why-socratease.md) -- Benefits of using Socratease over Google Forms
