# Train the Trainer Guide

Use this guide to prepare and deliver a GitHub Copilot workshop with consistent messaging, realistic demos, and enough flexibility for different customer audiences.

## Trainer checklist

### Before the workshop

- Confirm every participant has GitHub Copilot access.
- Decide whether participants use local VS Code or GitHub Codespaces.
- Pick labs that match the audience language stack and available time.
- Test the selected labs from a clean clone.
- For MCP labs, prepare the required tokens, server setup, and tool approval explanation.

### Opening

- Introduce the workshop goals and agenda.
- Explain that Copilot is an assistant, not an autopilot replacement for engineering judgment.
- Set expectations: generated output is non-deterministic and must be reviewed, tested, and committed like any other code.

### Core concepts to explain

- **Completions**: suggestions while typing.
- **Ask-style help**: read-only chat for explanations, snippets, and learning.
- **Agentic workflows**: Copilot can propose and apply changes, use tools, and run commands with user approval.
- **Models**: start with Auto when available; choose a specialized model only when a task needs it.
- **Context**: better context usually leads to better output.
- **Validation**: tests, builds, diffs, and human review remain mandatory.

### Suggested flow

| Phase | Goal |
| --- | --- |
| Welcome and setup | Verify accounts, IDE, extension, and repository access. |
| Fundamentals demo | Show completions, chat, context, and prompt iteration. |
| First lab | Run a small lab such as HTML Image Gallery or Rock Paper Scissors. |
| Review checkpoint | Compare generated output, discuss mistakes, and run tests or preview. |
| Advanced lab | Use an API, agentic workflow, or MCP lab depending on the audience. |
| Wrap-up | Discuss adoption, governance, security, and next steps. |

## Trainer tips

1. Keep prompts visible so participants can compare prompt quality and output.
2. Encourage small iterations instead of one huge prompt.
3. Pause after generated changes and inspect the diff together.
4. Use failures as teaching moments: ask Copilot to explain an error, then validate the fix.
5. Avoid promising deterministic output. Labs should describe expected outcomes, not exact generated code.
6. Have a fallback path for participants who cannot run a specific runtime locally.

## Resources for trainers

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center/)
- [AI model comparison for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [VS Code AI documentation](https://code.visualstudio.com/docs/ai/overview)
- [GitHub Changelog](https://github.blog/changelog/)
