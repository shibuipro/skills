# Install a Shibui skill

These instructions are for an assistant whose user has asked it to install a skill from `https://github.com/shibuipro/skills`.

## Select the skill

1. Use the skill name in the user's request.
2. Check the [skill list](https://github.com/shibuipro/skills#available-skills). Match the name to one folder under `skills/`.
3. If no skill is named, show the available names and short descriptions. Ask which skill the user wants.
4. Read the selected `SKILL.md` and inspect its bundled scripts before installation. Download the complete folder, including its assets and scripts. Do not install other skills.

Never use `--all`, `--skill '*'`, or `--agent '*'` for a request to install one skill. Do not treat a folder inside the current chat's temporary workspace as a permanent installation.

## Install when the app permits it

Use an available native skill installer when it accepts a GitHub folder URL:

```text
https://github.com/shibuipro/skills/tree/main/skills/<skill-name>
```

Otherwise, if you have local shell access and Node.js, use the Skills CLI. Identify the current assistant from your environment. Do not install for other assistants on the same computer.

Before installation, check for an existing skill with the same name. Keep an identical installation. If its content differs, explain the difference and ask before replacing it.

For Codex, replace `<skill-name>` and run:

```sh
npx --yes skills@1.7.0 add shibuipro/skills --skill <skill-name> --agent codex --global --yes
```

For Claude Code, replace `<skill-name>` and run:

```sh
npx --yes skills@1.7.0 add shibuipro/skills --skill <skill-name> --agent claude-code --global --yes
```

These commands install for the current user. Use project scope instead when the user requests it. For another supported assistant, use its documented agent identifier. If the environment does not identify the target app, ask one short question.

If Node.js is unavailable, use the app's documented skill directory. Download the repository to a temporary directory, then copy only `skills/<skill-name>/` into that directory. Preserve every file and relative path. Do not guess an installation directory or install a new runtime just for setup.

## If installation is unavailable

State the specific limit. Do not claim that reading these instructions installed the skill.

- If the app requires a manual upload, give the user the selected ZIP link: `https://github.com/shibuipro/skills/releases/latest/download/<skill-name>.zip`. Explain the app's upload step only when needed.
- If the user wants to proceed in the current conversation, load the selected skill instructions and the resources required for its output. State that this use does not persist as an installed skill.
- If a link cannot be read, report that failure and request the selected ZIP or required files. Do not invent the missing instructions or template.

Do not bypass app permissions or workspace restrictions.

## Verify and start

1. Confirm that the installed `SKILL.md` has the requested name.
2. Compare the installed files with the selected source folder. Confirm that required assets and scripts are present.
3. Check the app's skill list when available. If the app requires a reload, report it. Distinguish files copied from a skill that the app has loaded.
4. Report the skill name and installation location briefly.
5. Start the selected skill if the user asked you to start it. For Shibui Business Mapper, ask: "What process do you want to map?" Use any process the user already supplied.

## Sources

- [Skills CLI: selected skills, agents, and installation scope](https://github.com/vercel-labs/skills)
- [Codex: local skills and installation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code: skill locations](https://code.claude.com/docs/en/skills)
- [Claude: custom skill uploads](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [ChatGPT: skill availability and uploads](https://help.openai.com/en/articles/20001066)
