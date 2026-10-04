# Codewing: creating skills with GitHub Copilot

A one-hour workshop for CM developers and infrastructure colleagues, facilitated by **Nick Geerts and Tom Heyvaert**.

By the end, you will have created a skill and tested both when it activates and what it produces. Everything in the sample inputs is fictional.

## Before the workshop

- Install a current VS Code release and Git.
- Sign in to GitHub Copilot and confirm that agent mode is available under your organization's policy.
- Optional: Python 3.10+ for the example's local checker and repository validator. You can complete the workshop without Python.
- Use sample data or your own invented examples. Keep CM member information, credentials and internal production details out of this public repository.

## Start here

```sh
git clone https://github.com/N1ckG/codewing-skills-workshop-starter.git
cd codewing-skills-workshop-starter
code .
```

Open Copilot Chat in agent mode. Open the repository root, rather than a child folder. Type `/` and look for `incident-handoff`. You can also inspect skills through Configure Chat or `/skills` in current VS Code releases.

Try this explicit invocation:

```text
/incident-handoff Use examples/infra-incident.json. Draft the handoff in chat.
```

If your client does not expose the slash command, ask it to use the `incident-handoff` skill by name and inspect its tool activity. Do not silently replace the loading exercise with pasting the skill file into chat.

## What is included?

| Path | Purpose |
| --- | --- |
| `.github/skills/incident-handoff/` | A complete, discoverable example with a reference, an output template and an optional Python checker |
| `templates/my-skill/SKILL.md` | A scaffold outside discovery locations, so it cannot accidentally compete with your skill |
| `demo/security-review/` | The skill from the live demo, kept outside discovery locations until you copy it in |
| `examples/` | Fictional incidents, a code change, a Terraform snippet and intentionally insecure demo code |
| `docs/workshop.md` | Lab steps, two tracks and completion criteria |
| `docs/test-prompts.md` | Activation and output tests |
| `docs/loading.md` | The loading model and troubleshooting |
| `scripts/validate_skills.py` | A lightweight check for the simple frontmatter and local links used here |

## Demo skill

`demo/security-review/` is the skill from the live demo.
It sits outside `.github/skills/` on purpose, so the first run in the demo uses no skill.
To try it, copy the folder to `.github/skills/security-review/`, start a new chat and ask: "Check the code in this repo for security vulnerabilities."
`examples/security/orders_api.py` is fictional, intentionally insecure code for that demo. Do not run or reuse it.

## Your skill

Create `.github/skills/<your-skill-name>/SKILL.md` using the scaffold, or ask Copilot to help you draft it. Keep the folder name and `name` identical. Good topics include a pull request summary, an infrastructure change review or an incident handoff.

Read [the lab guide](docs/workshop.md). Test with fresh chats before claiming that automatic activation works. Mentioning a skill's name or opening its file changes the test.

Optional checks:

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

On Windows, use `py -3` if `python3` is unavailable. These checks validate files and the checker. They do not test Copilot's behavior.

## Documentation

The workshop uses VS Code with GitHub Copilot as its common client. Check the installed client before the session, because UI controls and optional fields change.

- [GitHub: agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [GitHub: adding skills](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills)
- [VS Code: skill loading and invocation](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Agent Skills format](https://agentskills.io/specification)

Documentation checked on 4 October 2026. This is a workshop example, not an official CM operational procedure.
