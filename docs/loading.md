# Skill loading in this workshop

The common client is VS Code with GitHub Copilot in Agent mode. Optional controls are client features rather than guarantees of the portable Agent Skills format.

## Where skills live

VS Code reads skills from folders on your laptop, so it does not matter whether you push to GitHub or GitLab.

- **Project skills**, shared with your team through the repository: `.github/skills/<name>/SKILL.md`. VS Code also reads `.agents/skills` and `.claude/skills`. This starter uses `.github/skills`.
- **Personal skills**, only for you and available in every repository you open: `~/.copilot/skills/<name>/SKILL.md` (also `~/.agents/skills` and `~/.claude/skills`).

The folder name must match the `name` field, and the file must be called `SKILL.md`.

## How a skill loads: three moments in one chat

1. **Chat starts:** Copilot gets a short catalog with the name and description of every skill, about 50 to 100 tokens each.
2. **Your question matches:** the model compares your question with the descriptions and decides; there is no keyword rule. It then loads the full `SKILL.md` into the chat. Typing `/skill-name` loads it on purpose. Keep `SKILL.md` under about 500 lines.
3. **A step needs a file:** only when a step points to a reference, template or script does Copilot read or run it.

The other skills stay one line each the whole time.
Once loaded, a skill stays in that chat; a new chat starts again from moment 1.
That is why every test uses a fresh chat, and why a vague description means the skill is never loaded.
Loading adds instructions to the task. It does not retrain the model or grant system access.

## Current VS Code controls

- Default: automatic selection and slash invocation are both available.
- `user-invocable: false`: hide the slash entry while allowing automatic selection.
- `disable-model-invocation: true`: require explicit slash invocation.
- Both options together disable both routes. Leave them out for the core lab.
- `context: fork` is an experimental VS Code option. It uses a separate subagent context and requires the documented skill-tool setting. The core lab uses the default inline context.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Skill absent in discovery | Repository root, supported path, exact `SKILL.md` case, valid YAML, matching folder and name |
| Explicit invocation works but automatic selection fails | Description, realistic task vocabulary, competing skills, fresh chat |
| Skill loads but output is poor | Input contract, missing-information behavior, workflow and output example |
| Reference or script is unused | Link/path, when-to-use instruction, available tools and interpreter |
| Old behavior after saving | New chat, reload the client if needed, correct workspace root |
| No load event is visible | Inspect client-supported customization diagnostics/tool traces. Record the evidence limitation. |

Sources checked on 5 October 2026:

- [GitHub overview](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [VS Code loading, slash commands and controls](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Portable format](https://agentskills.io/specification)
- [Agent implementation model](https://agentskills.io/client-implementation/adding-skills-support)
