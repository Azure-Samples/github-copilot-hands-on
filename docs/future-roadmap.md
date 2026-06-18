# Keeping the Workshop Current

GitHub Copilot changes too quickly for a static workshop to maintain a reliable product roadmap. Instead of predicting future features, this page gives trainers and maintainers a repeatable way to keep the workshop aligned with the current Copilot experience.

## What to review before each delivery

| Area | What to check |
| --- | --- |
| Copilot UI | Mode names, chat controls, tool approval prompts, and screenshot accuracy. |
| Models | Current model names, Auto behavior, visual-input support, and organization policy. |
| MCP | VS Code MCP configuration, server startup UX, and tool enablement screens. |
| Lab code | Dependencies, APIs, build commands, tests, and runtime versions. |
| External labs | Repository availability, instructions, QR codes, and prerequisites. |
| Security guidance | Token handling, generated-code review, dependency review, and customer data boundaries. |

## Current capability areas to watch

- **Agentic coding workflows**: multi-file changes, terminal commands, tests, and tool use with review.
- **MCP servers**: bringing external tools and data sources into Copilot Chat.
- **Model selection**: Auto model selection, specialized reasoning models, and visual input support.
- **Enterprise controls**: policy, auditability, content exclusion, and organization-level model availability.
- **Repository context**: how Copilot uses open files, selections, workspace search, issues, pull requests, and docs.

## Recommended maintenance workflow

1. Review the official Copilot docs and changelog.
2. Run the selected labs from a clean clone.
3. Update prompts and screenshots when the product UX changes.
4. Replace hard-coded model names with task-based guidance unless a lab requires a specific model.
5. Build the MkDocs site and fix broken links or assets.
6. Commit changes in the fork and open a pull request to the Azure-Samples repository.

## Official sources

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [AI model comparison for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [GitHub Changelog](https://github.blog/changelog/)
- [VS Code AI documentation](https://code.visualstudio.com/docs/ai/overview)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)

## Guidance for trainers

When a participant sees a slightly different UI, treat it as normal. Copilot capabilities can vary by plan, organization policy, extension version, IDE, and rollout status. Focus on durable practices: provide context, ask for small iterations, inspect diffs, run tests, and keep humans in control of accepted changes.
