# Shibui Skills

Skills for AI assistants. Install the skills you need, one at a time.

## Ask your assistant to install a skill

Copy this prompt into your assistant:

```text
Install only shibui-business-mapper from https://github.com/shibuipro/skills. Follow https://raw.githubusercontent.com/shibuipro/skills/main/INSTALL.md, then start the skill.
```

Replace `shibui-business-mapper` with another skill name from the list below when needed. The assistant handles setup when its app permits skill installation. If installation is unavailable, it must explain the limit before using the skill for the current conversation.

## Available skills

| Skill | Purpose | Download |
| --- | --- | --- |
| [shibui-business-mapper](skills/shibui-business-mapper/SKILL.md) | Develop a workflow through a conversation. Save Mermaid source and an HTML diagram with zoom and pan controls. | [Skill ZIP](https://github.com/shibuipro/skills/releases/latest/download/shibui-business-mapper.zip) |

Each ZIP contains one complete skill, including its templates and scripts.

## QR code

The [Business Mapper QR code](qr/shibui-business-mapper.png) contains the installation prompt above. Scan it with a QR reader, copy the text, and send it to your assistant.

[PNG](qr/shibui-business-mapper.png) · [SVG](qr/shibui-business-mapper.svg) · [Prompt text](qr/shibui-business-mapper.txt)

## Install with the Skills CLI

Requires Node.js and npm. List the available skills without installing them:

```sh
npx --yes skills@1.7.0 add shibuipro/skills --list
```

Install one selected skill. The command asks which supported assistant to use:

```sh
npx --yes skills@1.7.0 add shibuipro/skills --skill shibui-business-mapper --global
```

For installation by an assistant, follow [INSTALL.md](INSTALL.md). These commands use the [Skills CLI](https://github.com/vercel-labs/skills).

## Repository structure

```text
skills/
  shibui-business-mapper/
    SKILL.md
    agents/openai.yaml
    assets/workflow.html
    scripts/render_html.py
INSTALL.md
qr/
```

Each folder under `skills/` is an independent skill. Its folder name must match the `name` in its `SKILL.md` file. Keep all resources needed by that skill inside its folder.

## Add another skill

1. Add `skills/<skill-name>/SKILL.md` with a name, description, and instructions.
2. Add the required templates, scripts, or references inside that folder.
3. Check the skill and add it to the table above.
4. Create a ZIP with `<skill-name>/` as its top folder. Attach it to the latest release. Keep the other skill ZIPs available in that release.

To package one skill, run this command from `skills/` and replace the example name as needed:

```sh
python3 -m zipfile -c ../shibui-business-mapper.zip shibui-business-mapper
```

## Output requirements

Shibui Business Mapper uses Python 3 when available to create its HTML file. The script needs no Python packages. The skill includes a template-based alternative when Python is unavailable.

Open the generated HTML in a browser. Internet access is required to load Mermaid from jsDelivr. The diagram source is embedded in the HTML.
