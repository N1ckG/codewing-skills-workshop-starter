# Lab guide

This guide follows the hands-on slide "Build one skill: start here".
The hands-on takes the rest of the hour after the talk and the mini demo.
No Copilot or Wi-Fi? Pair up with your neighbour.
Stuck? Ask your table first, then raise your hand.

## 1. Get started

1. Clone or download this repository: `github.com/N1ckG/codewing-skills-workshop-starter`.
2. Open the repository root in VS Code, not a subfolder, and switch Copilot Chat to Agent mode.
3. Type `/skills` in the chat. You should see `incident-handoff`.

If nothing shows up, check that the root folder is open and that the chat is in Agent mode.

## 2. Pick a task

Pick something you explained twice this month.
Small, frequent, and you recognise a good result.

| Idea | Sample input in this repo |
| --- | --- |
| Merge request description | `examples/developer-change.md` |
| Terraform change review | `examples/infrastructure-change.tf` |
| Incident handoff | `.github/skills/incident-handoff/` is a complete example to read and copy from |
| Commit message in your team's format | |
| Runbook or release checklist | |
| Explain a script or module to a newcomer | |

You can also bring your own task.
Keep private work in its own repository: this repository is public.

### Should it be a skill?

Answer four questions.
Four times yes: write the skill.

1. Do you repeat it? If not, just ask in chat.
2. Is it for one kind of task? If it should apply to every chat, use custom instructions instead.
3. Can you say what good looks like (format, steps, checks)? If not, clarify the task first.
4. Is it safe to write down? Secrets, credentials and member data never go in a skill.

## 3. Draft it

1. Type `/create-skill` in the chat and describe your task, or copy `templates/my-skill/SKILL.md` to `.github/skills/<your-skill-name>/SKILL.md`.
2. Write the description first: what the skill does and when to use it, in the words people actually type.
3. Keep the folder name and the `name` field identical: lowercase letters, numbers and hyphens.
4. Write the steps in plain Markdown, the way you would brief a colleague.
5. Read every line Copilot drafted and remove team rules it invented.

Drafting prompt, if you prefer to ask in your own words:

```text
Help me create a skill for [my recurring task] in .github/skills/[my-name]/SKILL.md.
Use templates/my-skill/SKILL.md as a starting point.
My input is [example]. A useful result is [format and success criteria].
The skill should apply to [requests], and should leave [nearby tasks] to another workflow.
Ask about missing task details before inventing our team's rules.
Keep the first version short.
```

## 4. Test it

1. Open a new chat.
2. Ask your question normally, without naming the skill or attaching `SKILL.md`.
3. Look for `SKILL.md` in the references or tool activity of the answer.
4. Not picked? Sharpen the description and try again in a new chat.
5. Picked, but the result is off? Improve the steps, or add a template or checklist next to `SKILL.md` and link it from a step.

[The test prompts](test-prompts.md) show the same tests for `incident-handoff`.

## Checkpoints

- About a third of the way in: a first `SKILL.md` is saved. If not, make the task smaller.
- About two thirds in: everyone tests in a fresh chat, without naming the skill.
- A few minutes before the share-back: get your phone ready.

## Done early?

- Add a checklist or template and make a step point to it.
- Test a question that should not trigger your skill.
- Move the skill to your own team repository and try it on real work.

## Share-back

Scan the QR code on the share-back slide and type, in two or three words, which task your skill handles.
The answers appear as a live word cloud.

## After the workshop

- Share the skill with your team through your team's folder in the CM APM marketplace (the link is on the slides). The CodeWing team reviews the pull request.
- Keep it alive: rerun your test question after every change, update `SKILL.md` when the result is off, and run `apm update` to get the latest version of shared skills.
