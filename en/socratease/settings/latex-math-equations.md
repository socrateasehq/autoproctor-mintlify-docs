---
title: "Using LaTeX for Math Equations"
description: "Add mathematical equations to your Socratease quizzes using LaTeX syntax."
---

Socratease supports LaTeX, the global standard for writing mathematical equations used in academic publications, textbooks, and research papers worldwide. Instead of inserting equation images or using simplified text notation like `a^2` or `3/4`, you can write properly formatted equations directly in your quiz questions.

{% hint style="info" %}
LaTeX equation support is exclusive to AutoProctor's **Socratease Quizzes**. It is not available when using other quiz providers.
{% endhint %}

## How to Write LaTeX Equations

To include a LaTeX equation in your quiz, enclose the equation between `\(` and `\)` delimiters.

**Example:**

```
\(a^2 + b^2 = c^2\)
```

This renders as the familiar Pythagorean theorem: a squared plus b squared equals c squared.


## What LaTeX Supports

LaTeX can render any mathematical notation, including:

| Notation | LaTeX Syntax | Description |
|---|---|---|
| Basic arithmetic | `\(a + b = c\)` | Addition, subtraction, multiplication, division |
| Exponents | `\(x^2\)` | Superscripts and powers |
| Subscripts | `\(a_n\)` | Subscript notation |
| Fractions | `\(\frac{a}{b}\)` | Fraction notation |
| Square roots | `\(\sqrt{x}\)` | Square and nth roots |
| Integrals | `\(\int_0^1 x^2 dx\)` | Definite and indefinite integrals |
| Summations | `\(\sum_{i=1}^{n} i\)` | Summation notation |
| Greek letters | `\(\alpha, \beta, \gamma\)` | All Greek letter symbols |

You can also use any other standard LaTeX mathematical notation beyond the examples listed above.

## Enabling LaTeX

{% embed url="../../videos/socratease/using-latex.mp4" %}
How to enable and use LaTeX in Socratease
{% endembed %}

{% stepper %}
{% step %}
### Open Your Quiz
Open your Socratease Quiz on AutoProctor.
{% endstep %}
{% step %}
### Go to Settings
Click the **Settings** icon (gear) in the quiz editor toolbar.
{% endstep %}
{% step %}
### Enable LaTeX Support
Toggle on the **LaTeX Support** setting. This activates LaTeX rendering for all questions in the quiz.


{% endstep %}
{% step %}
### Write Your Equations
Write your equations in question text using the `\(` and `\)` delimiters. The equations render as formatted math when candidates view the quiz.


{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Make sure you enable the LaTeX Support toggle in quiz settings **before** sharing the test. If LaTeX is not enabled, candidates will see the raw LaTeX syntax instead of rendered equations.
{% endhint %}

## Try It Out

You can see a sample quiz demonstrating LaTeX equation rendering at:
[autoproctor.co/tests/jVRBZGRMNU/load](https://www.autoproctor.co/tests/jVRBZGRMNU/load/)


## Related Resources

- [Quiz Settings](socratease/settings/quiz-settings.md) -- All Socratease quiz configuration options
- [Question Types](socratease/create-questions/question-types.md) -- Available question formats
- [How to Create a Socratease Quiz](socratease/create-questions/creating-a-quiz.md) -- Step-by-step creation guide
- [Why Socratease?](socratease/create-questions/why-socratease.md) -- Benefits of using Socratease over other platforms
