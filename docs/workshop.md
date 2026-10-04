# Lab guide

## The hour

| Minutes | Activity |
| --- | --- |
| 0–20 | Explanation, loading walkthrough and live example |
| 20–23 | Clone, open the root and check Copilot |
| 23–35 | Build your first skill |
| 35–47 | Test activation and output |
| 47–55 | Swap with a partner and improve |
| 55–60 | Show two results and name a next step |

## Choose a small workflow

Developers can draft PR summaries using `examples/developer-change.md`.
Infrastructure colleagues can review a proposed change using `examples/infrastructure-change.tf`, without applying it.
Either group can adapt an incident handoff to a different audience.
You can use another recurring task if its input and output fit this session.

**Finish line:** one discovered skill, a useful output, a positive activation test, a paraphrase test, an unrelated request test and a missing-input test. Record evidence, including a failure and your improvement if one occurs.

## Build: 23–35 minutes

1. Choose a workflow you currently explain repeatedly to a colleague or to Copilot.
2. Copy `templates/my-skill/SKILL.md` to `.github/skills/<your-name>/SKILL.md`. Use a lowercase hyphenated name, matching the directory.
3. Write the description first. Specify the outcome, task language and relevant boundary.
4. Replace the body with your input requirements, workflow and expected output. Give it task-specific guidance rather than generic instructions to be helpful.
5. Save it and check discovery in the client. Start a fresh chat if the current session does not reflect your changes.

Copilot drafting prompt:

```text
Help me create a skill for [my recurring task] in .github/skills/[my-name]/SKILL.md.
Use templates/my-skill/SKILL.md as a starting point.
My input is [example]. A useful result is [format and success criteria].
The skill should apply to [requests], and should leave [nearby tasks] to another workflow.
Ask about missing task details before inventing our team's rules.
Keep the first version short. Explain why you chose the description.
```

## Test: 35–47 minutes

Use [the test prompts](test-prompts.md). Run each automatic activation test in a fresh chat without naming the skill or attaching `SKILL.md`. Keep the input explicit. Inspect tool activity for the skill file and resources where your client exposes it.

Check the result against your expected format and facts. The agent saying “I used the skill” or reproducing a marker is weaker evidence than an actual load/read event. Some clients inject skill instructions without a visible file read. If you cannot see loading, record that limitation separately from output quality.

Suggested record:

| Request | Expected activation | Observed loading evidence | Output result | Improvement |
| --- | --- | --- | --- | --- |
| Direct task | Yes | | | |
| Paraphrase | Yes | | | |
| Unrelated task | No | | | |
| Missing input | Yes, then clarify | | | |

## Pair review: 47–55 minutes

Ask a partner to try their own wording in a fresh chat. Have them assess whether the output would be useful in their work. Change the description for routing failures and the body or reference for execution failures. Repeat the failing test.

## Stretch track

Add one resource only when it improves your workflow:

- A reference with a concrete rubric that applies to one task variant.
- An asset with the desired output format.
- A deterministic local script, with documented inputs and failure behavior.

Link the resource from `SKILL.md` and say when to use it. Check whether the relevant resource loads or runs on the matching request. Do not connect to live systems for this exercise.

## Share: 55–60 minutes

Show your description, one output and a test that taught you something. Name where you would maintain the skill, who would review changes and which representative test you would keep.
