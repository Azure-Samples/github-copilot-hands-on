# Hands-on Labs Overview

The labs are designed to be mixed and matched. Start with a fundamentals lab, then move to APIs, tests, agentic workflows, or MCP depending on the audience.

## Labs in this workshop

| Area | Lab | Language / tools | Typical use |
| --- | --- | --- | --- |
| Fundamentals | [HTML Image Gallery](html-gallery.md) | HTML, CSS, JavaScript | First Copilot experience, prompt iteration, UI preview. |
| Fundamentals | [Rock Paper Scissors](rock_paper_scissors.md) | Python | Generate game logic, tests, comments, and simplifications. |
| APIs | [Star Wars API in Python](starwars-api-python.md) | Python, pytest | Data classes, abstract base classes, HTTP calls, tests. |
| APIs | [Star Wars API in Java](starwars-api.md) | Java, Maven | DTOs, interfaces, implementations, and unit tests. |
| Agentic / MCP | [HTML Image Gallery with MCP](gh-gallery-mcp.md) | GitHub MCP, Playwright MCP | Create issues, implement from requirements, and test with tools. |
| Agentic / MCP | [Build Your Own MCP Server](mcp-server-starter.md) | Python, Java, TypeScript options | Build a weather MCP server and connect it to Copilot. |
| Agentic / MCP | [Four in a Row MCP Game](mcp-fiar.md) | Java, Spring Boot, MCP | Interact with a custom MCP server through Copilot Chat. |
| Extended | [Other Labs](other-labs.md) | Multiple | External labs for additional languages and customer scenarios. |

## How to use these labs

Each lab includes:

1. A scenario and expected outcome.
2. Prompts or prompt patterns for Copilot.
3. Checkpoints to review generated output.
4. Validation steps such as running tests, previewing a page, or inspecting a diff.

## Choosing the right lab

| Audience | Suggested path |
| --- | --- |
| New to Copilot | HTML Image Gallery or Rock Paper Scissors. |
| Backend / API developers | Star Wars API in Python or Java. |
| Developers interested in agents | HTML Image Gallery with MCP. |
| Platform or tooling audience | Build Your Own MCP Server. |
| Mixed customer workshop | Start with one fundamentals lab, then offer a language-specific breakout. |

## Trainer guidance

- Treat generated code as a draft that requires review.
- Prefer small prompt iterations over one large request.
- Explain tool approval before running MCP labs.
- Use Auto model selection where possible and only choose a specific model when a lab needs a capability such as visual input or deeper reasoning.
