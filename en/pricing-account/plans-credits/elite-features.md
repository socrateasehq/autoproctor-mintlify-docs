---
title: "Elite Plan Features"
description: "Explore the exclusive features available only on the AutoProctor Elite plan, including API access, question banks, and advanced question types."
---

The Elite plan is AutoProctor's most feature-rich tier. It includes everything in the Standard and Premium plans, plus several exclusive capabilities designed for advanced assessment workflows.

{% hint style="warning" %}
These features are available **only** on the Elite plan. You do not have access to them on the Free Trial, Standard, or Premium plans.
{% endhint %}

## Elite-Only Features

As shown on the [Pricing Page](https://www.autoproctor.co/pricing/), AutoProctor offers three subscription tiers: **Standard**, **Premium**, and **Elite**. The following features are exclusive to Elite.

### API/SDK Access

If you already have your own quizzing or assessment platform and want to add proctoring, you can integrate AutoProctor using the JavaScript SDK. This lets you embed proctoring directly into your existing workflow without requiring candidates to use a separate platform.


### Cloning Quizzes

You can **duplicate Socratease Quizzes in a single click**. This is especially useful when you need to create multiple quizzes that share a similar structure but differ in specific questions or settings.

<Frame caption="How to clone a quiz">
  <iframe className="w-full rounded-xl" style={{aspectRatio: "16/9"}} src="https://www.youtube.com/embed/1gAEoe2Oy3E?rel=0" title="How to clone a quiz" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>
</Frame>

### Unique URL per Candidate

Generate a unique test link for each candidate so a single link cannot be forwarded to unintended recipients. See [Unique URL per Candidate](tests-results/create/advanced-settings#unique-url-per-candidate-elite.md) for setup.

### Additional Instructions

Add custom instructions to the candidate instructions page — useful for sharing specific rules, context, or guidelines before the test begins. See [Additional Instructions](tests-results/create/advanced-settings#additional-instructions-elite.md) for details.

{% hint style="info" %}
The following features (Question Banks, More Question Types, and Import From Excel) apply specifically to Socratease Quizzes.
{% endhint %}

### Question Banks

Question Banks let you create large pools of questions and dynamically select subsets for each candidate. This supports two key use cases:

| Use Case | Example |
|---|---|
| **Random subset by difficulty** | Select 5 easy and 2 hard MCQs from a pool of 100 questions |
| **Combine multiple pools** | Draw 3 Physics and 2 Chemistry MCQs from two separate pools of 100 each |

For a detailed guide, see [Question Banks](socratease/create-questions/question-banks.md).

### More Question Types

Socratease Quizzes support many question formats. The following are exclusive to the Elite plan:

<CardGroup cols={3}>
  <Card title="Voice Input">
    Candidates record themselves speaking the answer. Useful for language assessments, oral exams, and presentation-style questions.
  </Card>
  <Card title="Autograded Text">
    You specify the correct answer when creating the question. If the candidate's submission matches exactly, they receive full points. Otherwise, they receive 0 points.
  </Card>
  <Card title="Answer Any">
    Present multiple questions (for example, 5) and allow candidates to answer a subset (for example, 3). The numbers are fully configurable.
  </Card>
</CardGroup>

For the full list of question types, see [Socratease Question Types](socratease/create-questions/question-types.md).

### Import From Excel

Using the AutoProctor Excel template, you can **bulk upload questions** onto a Socratease Quiz. This is ideal for migrating existing question sets or creating large assessments quickly. See [Bulk Import from Excel](socratease/create-questions/bulk-import-from-excel.md) for step-by-step instructions.

## Related Resources

- [Payments and Credits Explained](pricing-account/plans-credits/payments-and-credits.md) -- Understand subscription tiers and pricing
- [What is a Team?](pricing-account/billing-teams/teams.md) -- Share billing and collaborate with team members
- [Question Types](socratease/create-questions/question-types.md) -- All available Socratease question formats
- [Question Banks](socratease/create-questions/question-banks.md) -- Detailed guide to using question banks
- [Bulk Import from Excel](socratease/create-questions/bulk-import-from-excel.md) -- Step-by-step Excel import instructions
- [Why Socratease](socratease/create-questions/why-socratease.md) -- Benefits of using Socratease over other quiz platforms
