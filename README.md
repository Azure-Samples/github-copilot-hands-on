# GitHub Copilot Hands-on Labs

This repository contains a GitHub Copilot workshop created by Microsoft Germany Cloud Solution Architects. It helps customers get hands-on experience with Copilot across everyday coding, test generation, API clients, agentic workflows, and Model Context Protocol (MCP) scenarios.

## What is in this repo?

| Path | Purpose |
| --- | --- |
| `docs/` | Published MkDocs workshop content. Start here when delivering or previewing the workshop. |
| `labs/` | Starter code, sample projects, and supporting lab instructions. |
| `mkdocs.yml` | MkDocs Material site configuration and navigation. |
| `.github/workflows/deploy-mkdocs.yml` | GitHub Pages deployment workflow for the docs site. |

## Workshop content

The workshop is designed to be flexible. Trainers can run a short introduction with one or two fundamentals labs, or a longer session that includes agentic and MCP scenarios.

| Area | Labs |
| --- | --- |
| Fundamentals | HTML Image Gallery, Rock Paper Scissors |
| API clients | Star Wars API in Python, Star Wars API in Java |
| Agentic workflows and MCP | HTML Image Gallery with MCP, Build Your Own MCP Server, Four in a Row MCP Game |
| Extended resources | External labs linked from the "Other Labs" page |

## Prerequisites

Participants need:

- A GitHub account with GitHub Copilot access.
- [Visual Studio Code](https://code.visualstudio.com/) with the GitHub Copilot extension enabled.
- Git installed locally, or access to GitHub Codespaces.
- Runtime dependencies for the selected lab, for example Python, Java and Maven, Node.js, Docker, or .NET.

Some MCP labs also require a GitHub personal access token and explicit tool approval in Copilot Chat.

## Preview the workshop locally

Install MkDocs Material and start the local preview server:

```bash
python -m pip install mkdocs-material
mkdocs serve
```

Then open the local URL printed by MkDocs. Before publishing documentation changes, run:

```bash
mkdocs build --strict
```

## Working from a fork

Use your fork for changes and target the Azure-Samples repository when opening a pull request.

```bash
git remote add upstream https://github.com/Azure-Samples/github-copilot-hands-on.git
git fetch upstream
git checkout -b <your-branch> upstream/main
# make changes
git push origin <your-branch>
```

Open the pull request with:

- **Base repository**: `Azure-Samples/github-copilot-hands-on`
- **Base branch**: `main`
- **Head repository**: your fork
- **Compare branch**: your feature branch

## Keeping the workshop current

GitHub Copilot changes quickly. Keep volatile topics link-first: explain how to choose a model, mode, or tool at a high level, then link to the official documentation for the latest details.

Useful references:

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [AI model comparison for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [GitHub Changelog](https://github.blog/changelog/)
- [VS Code AI documentation](https://code.visualstudio.com/docs/ai/overview)