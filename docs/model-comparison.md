# AI Model Guidance for GitHub Copilot

GitHub Copilot supports multiple AI models, and the available list changes over time. Model access can also vary by plan, organization policy, IDE, region, and feature rollout.

!!! info "Source of truth"
    Use the official [AI model comparison for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-comparison) for the current model list, model cards, billing notes, and detailed task guidance.

## Workshop recommendation

For most labs, start with **Auto** when it is available. Auto lets Copilot choose a suitable model based on availability and task characteristics.

Only ask participants to manually choose a model when the lab needs a specific capability:

| Task | Recommended guidance |
| --- | --- |
| Everyday coding, explanations, and small edits | Use Auto or a general-purpose coding model. |
| Quick syntax help or repetitive changes | Use Auto or a faster model optimized for simple tasks. |
| Multi-file debugging, architecture, or refactoring | Use Auto or a deep-reasoning model. |
| Agentic software development | Use Auto or a model recommended for agentic coding in the official docs. |
| Screenshots, mockups, and UI analysis | Use a model that supports visual input in your current Copilot surface. |
| Inline code completions | Use the completion model configured by your IDE or organization. |

## How to choose during a lab

1. **Start with the task, not the model name.** Decide whether the participant needs speed, reasoning, visual input, or agentic tool use.
2. **Prefer Auto for workshops.** It avoids teaching a model list that may be outdated by the next delivery.
3. **Use specialized models intentionally.** For example, use a reasoning or vision-capable model for a mockup-to-implementation exercise.
4. **Warn about variability.** Different models may produce different code. Participants should review diffs and validate the result.
5. **Check organization policy.** Some models or features may be disabled by enterprise policy.

## What to avoid in workshop material

- Do not hard-code old model names in prompts unless the exercise explicitly depends on that model and has been recently tested.
- Do not include context-window sizes, benchmark claims, or quota details unless they come directly from current official documentation.
- Do not present model choice as a quality guarantee. Better prompts, context, tests, and review still matter.

## References

- [AI model comparison for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/supported-ai-models-in-copilot)
- [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat)
- [Models and pricing for GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
