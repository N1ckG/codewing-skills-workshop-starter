# Skill loading in this workshop

The common client is VS Code with GitHub Copilot agent mode. Optional controls are client features rather than guarantees of the portable Agent Skills format.

## What happens

1. **Discovery:** the client finds `SKILL.md` in supported skill directories and exposes names and descriptions to the model. For this workshop, use `.github/skills/<name>/SKILL.md` at the repository root.
2. **Selection:** the request and description help Copilot choose a skill. Automatic selection depends on the model and context. Discovery alone does not establish selection.
3. **Instructions:** activation brings the skill body into the agent's context. An explicit slash command is the baseline for this exercise.
4. **Resources:** the workflow directs file reads and local script execution as needed. An unreferenced file does not automatically become part of the instructions. A script result can enter context without the full script source being read.
5. **Result:** the agent combines the loaded workflow with the request, relevant context and tool results. Loading adds instructions to this task. It does not retrain the model or grant system access.

The portable specification describes metadata, instructions and resources as separate loading tiers. Exact caching, refresh and trace presentation vary by client. Use a fresh chat for fair routing tests and after edits when refresh is unclear.

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

Sources checked on 4 October 2026:

- [GitHub overview](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [VS Code loading, slash commands and controls](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Portable format](https://agentskills.io/specification)
- [Agent implementation model](https://agentskills.io/client-implementation/adding-skills-support)
