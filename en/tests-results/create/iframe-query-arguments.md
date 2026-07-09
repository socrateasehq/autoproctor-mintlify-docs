---
title: "IFrame Query Arguments"
description: "Append query parameters to iframe URLs in AutoProctor's Advanced Settings to customize embedded content."
---

When you use the **IFrame/Other** quiz provider, you can append query parameters to your embedded quiz URL through AutoProctor's **Advanced Settings**. This lets you customize how the embedded content behaves -- for example, forcing a specific language or enabling embedded mode -- without modifying the original URL.

## How It Works

AutoProctor constructs the final URL by appending your query arguments to the original quiz URL. You provide only the parameters; AutoProctor adds the `?` prefix automatically.

{% embed url="videos/settings/query-arguments.mp4" %}
How to use query arguments in AutoProctor's Advanced Settings
{% endembed %}

{% stepper %}
{% step %}
### Open Advanced Settings
Navigate to your test and open the **Advanced Settings** section.
{% endstep %}
{% step %}
### Enter Your Query Arguments
Type your parameters in the **Query Arguments** field. Use the format `key1=val1&key2=val2`.
{% endstep %}
{% step %}
### Save Settings
Save your test settings. AutoProctor appends your parameters to the quiz URL when rendering the iframe.
{% endstep %}
{% endstepper %}

### Example

If your original URL is:

```
www.website.com
```

And you enter the following in the **Query Arguments** field:

```
key1=val1&key2=val2
```

AutoProctor renders the iframe as:

```
www.website.com?key1=val1&key2=val2
```

{% hint style="info" %}
Do not include the `?` prefix in your query arguments. AutoProctor adds it automatically when constructing the URL.
{% endhint %}

## Common Parameters

| Parameter | Purpose | Example Use Case |
|---|---|---|
| `hl=en` | Set the language to English | Render a Google Form in English for international candidates |
| `hl=fr` | Set the language to French | Render a Google Form in French |
| `embedded=true` | Force embedded mode | Ensure certain platforms display correctly inside the iframe |

## Related Resources

- [Quiz Providers](tests-results/create/quiz-providers.md) -- All supported quiz platforms
- [Advanced Settings](tests-results/create/advanced-settings.md) -- Login providers, collaborators, and other advanced options
- [Timer Settings](tests-results/create/timer-settings.md) -- Configure test duration and time windows
- [Proctoring Settings](tests-results/create/proctoring-settings.md) -- Camera, microphone, and tab-switching options
