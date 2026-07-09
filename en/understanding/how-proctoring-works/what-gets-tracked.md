---
title: "What Gets Tracked During Proctoring"
description: "Learn about the data feeds, detection capabilities, and evidence recording available in AutoProctor's proctoring system."
---

AutoProctor monitors candidates in real time using on-device AI and captures evidence only when it detects a violation. This means you review flagged incidents rather than hours of footage.

<Frame caption="A sample proctoring report showing the Trust Score, violation counts, and flagged events with evidence">
  ![Sample proctoring report](../../images/getting-started/sample-proctoring-report.png)
</Frame>

[View sample proctoring results](https://www.autoproctor.co/sample-dashboard/) to explore a live report.

## Data Feeds

AutoProctor can access the following feeds on the candidate's device:

| Feed | What It Does |
|---|---|
| **Camera feed** | Monitors the candidate's face and surroundings |
| **Microphone feed** | Detects background noise and audio cues |
| **Screen share feed** | Captures screen activity during the test |
| **Auxiliary device camera feed** | Monitors via a paired secondary device (e.g., phone) |

{% hint style="info" %}
Which feeds AutoProctor accesses depends entirely on how you configure each test. You enable or disable each feed in your [proctoring settings](tests-results/create/proctoring-settings.md).
{% endhint %}

## What AutoProctor Detects and Records

Unlike traditional proctoring platforms that record full video and audio sessions, AutoProctor detects violations and shows you evidence of only those violations -- so you do not spend hours reviewing each candidate's attempt.

| Detection Feature | What It Does |
|---|---|
| **Background audio detection** | Records noise and audio cues from the microphone feed |
| **Face detection** | Captures photos when no face or multiple faces appear on camera |
| **Tab/app switching** | Captures screenshots when candidates switch tabs or applications |
| **Random photos** | Takes photos at random intervals throughout the exam |
| **Multiple monitor detection** | Identifies when additional screens are connected to the device |
| **Pre-test face capture** | Takes a photo of the candidate's face before the test starts |
| **Full-screen enforcement** | Ensures the test runs in full-screen mode and flags exits |
| **Session action recording** | Logs mouse clicks and keyboard activity throughout the test |
| **Auxiliary device pairing** | Monitors via a paired phone to detect keyboard usage, ensuring candidates are not using ChatGPT or other tools to cheat |

{% hint style="info" %}
All tracking features are configurable per test. Enable only what you need in your [proctoring settings](tests-results/create/proctoring-settings.md).
{% endhint %}

## How to Configure Tracking

{% embed url="../../videos/getting-started/configure-proctor-settings.mp4" %}
How to Configure Tracking Settings
{% endembed %}

{% stepper %}
{% step %}
### Open your test settings
Go to your [AutoProctor dashboard](https://www.autoproctor.co/test-admin/home/), select a test, and click **Settings**.


{% endstep %}
{% step %}
### Navigate to Proctoring Settings
Click the **Proctoring Settings** tab to see all available tracking options.


{% endstep %}
{% step %}
### Enable the features you need
Toggle each tracking feature on or off depending on your requirements. For example, you might enable camera monitoring and tab-switching detection but leave microphone monitoring off.


{% endstep %}
{% step %}
### Save your settings
Click **Save** to apply your changes. These settings take effect immediately for all future test attempts.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Enabling more tracking features increases the processing load on the candidate's device. If your candidates use older hardware, consider enabling only the features you need most. See [Device Compatibility](understanding/getting-started/device-compatibility.md) for minimum requirements.
{% endhint %}

## Related Resources

- [Trust Score](understanding/how-proctoring-works/trust-score.md) -- How AutoProctor scores candidate integrity
- [Proctoring Settings](tests-results/create/proctoring-settings.md) -- Configure which proctoring features to enable
- [Enhanced Proctoring](tests-results/create/enhanced-proctoring.md) -- Advanced monitoring options for higher security
- [Proctoring Results](tests-results/results/proctoring-results.md) -- View violation evidence and reports
- [Video Recording](understanding/how-proctoring-works/video-recording.md) -- Why AutoProctor does not record full video
- [Device Compatibility](understanding/getting-started/device-compatibility.md) -- Supported browsers and devices
