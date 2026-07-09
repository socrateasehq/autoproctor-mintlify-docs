---
title: "Trust Score"
description: "Understand how AutoProctor's Trust Score works, how it is calculated, and what constitutes a good score."
---

AutoProctor assigns a Trust Score (0--100%) to every proctoring report. The score gives you a quick summary of how likely it is that a candidate maintained test integrity, so you can focus your review time on the attempts that need it most.

![Trust Score display showing a percentage at the top of an AutoProctor proctoring report](images/getting-started/trustscore.png)
*Trust Score displayed at the top of a proctoring report*

A lower Trust Score means AutoProctor detected more suspicious behavior during the test.

{% hint style="warning" %}
Always review the supporting evidence before drawing conclusions. **Do not** rely solely on the Trust Score -- review the actual violation photos, screenshots, and audio recordings to determine whether misconduct occurred.
{% endhint %}

## How the Trust Score Is Calculated

AutoProctor monitors candidates in real time across multiple channels (depending on your [proctoring settings](tests-results/create/proctoring-settings.md)):

- Camera feed
- Microphone feed
- Screen activity

The algorithm evaluates violations based on three factors:

| Factor | How It Affects the Score |
|---|---|
| **Type of violation** | Different violations carry different weights. Tab switching impacts the score more heavily than noise detection. |
| **Frequency of violations** | More incidents result in a lower score. |
| **Duration of violations** | Extended violations reduce the score more significantly than brief ones. |


## What Is a Good Trust Score?

As a general guideline, review the evidence for any candidate with a Trust Score **below 85%**. This threshold is meant for review, not as proof of misconduct.

{% hint style="info" %}
Environmental factors can significantly impact scoring. For example, a candidate in a noisy room near traffic could receive a 0% Trust Score even when no actual cheating occurred. The microphone picks up ambient noise and the system cannot always distinguish between human speech and background sound. Always check the evidence before making a determination.
{% endhint %}

## How to Review a Trust Score

{% stepper %}
{% step %}
### Open your test results
Go to your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/), select a test, and click **Results**. You see a list of all candidates with their Trust Scores.
{% endstep %}
{% step %}
### Identify candidates for review
Sort by Trust Score and focus on candidates scoring **below 85%**. These attempts are the most likely to contain violations worth reviewing.

{% embed url="videos/getting-started/trustscore-column.mp4" %}
Results list showing the Trust Score column
{% endembed %}
{% endstep %}
{% step %}
### Review the violation evidence
Click **View Report** on a candidate's row to see the detailed breakdown: flagged photos, screenshots, audio clips, and a timeline of detected violations.


{% endstep %}
{% step %}
### Make your determination
Use the evidence to decide whether the violations indicate actual misconduct or are false positives caused by environmental factors.
{% endstep %}
{% endstepper %}

## Related Resources

- [What Gets Tracked](understanding/how-proctoring-works/what-gets-tracked.md) -- All monitoring capabilities available
- [Proctoring Results](tests-results/results/proctoring-results.md) -- How to view violation evidence and reports
- [Access Answers and Candidate Responses](tests-results/results/individual-submissions.md) -- Reviewing a single candidate's report in detail
- [No Face or Multiple Faces Detected](tests-results/issues/no-face-or-multiple-faces.md) -- Why face detection may flag false positives
- [False App Switch Violation](tests-results/issues/false-app-switch.md) -- Understanding false violation flags
- [Best Practices for Test Creators](understanding/getting-started/best-practices-for-teachers.md) -- Tips for running effective proctored tests
