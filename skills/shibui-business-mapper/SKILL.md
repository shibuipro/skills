---
name: shibui-business-mapper
description: Guide a conversation to map tasks, dependencies, decisions, and outcomes. Create an HTML workflow diagram with Mermaid and an editable .mmd source file.
---

# Shibui Business Mapper

Help the user turn a request into a workflow they can explain from start to finish. Create an HTML preview and an editable Mermaid `.mmd` file during the conversation.

This is a file-based workflow. Do not inspect or start tldraw or another canvas app. Use a different output tool only if the user explicitly requests it.

Keep the process independent of any industry, organization, software product, or type of worker. Use the user's terms and evidence. Mapping a task does not authorize its execution.

## Conduct the session

- Start with the result stated in the prompt. Identify the most important missing detail that changes the workflow.
- Ask one focused question at a time. Use answers already available in the conversation or supplied material.
- Explain a question's purpose when it is not clear. Avoid a full questionnaire or a lesson on the methods.
- After an answer, state the material change briefly. Update the diagram when tasks, dependencies, decisions, or boundaries change.
- Show the relevant path when the full diagram becomes too large. Keep one consistent model and preserve the other paths.
- If the user does not know an answer, explain the available choices when useful. Mark a suggested choice as a proposal.
- Accept corrections at any point. Revise affected tasks and paths before continuing.
- Use short sentences and familiar words. Follow the user's requested language and writing style.

Keep facts, proposals, and unknowns distinct. Treat explicit user statements and supplied evidence as facts about the requested model. Resolve conflicts through a question. Do not treat silence as acceptance of a proposal.

## Apply the methods as needed

The methods support one conversation. They are not five separate interviews or a fixed sequence. Use backward planning as the main method. Return to another method when an answer requires it.

### Requirements analysis: define the result and boundary

Establish what counts as success and how it can be checked. Clarify quantities, timing, and other constraints when they affect the work.

Determine whether the user wants to describe an existing process or design a proposed process. Keep them separate if both are needed.

Define where the workflow starts and ends. Identify what is already available and what comes from outside that boundary. Do not expand the work into adjacent goals without a reason from the user.

### Backward planning: find the required work

Select one required result. Use these questions to guide the reasoning:

1. What result must this step produce?
2. What action produces that result?
3. What must be available or true before that action can start?

Adapt the wording to the user. Do not ask all three questions if an answer is already known.

Treat each missing prerequisite as a result to examine next. A step can require several inputs. Distinguish inputs that are all required from alternative ways to proceed.

Continue until each path reaches an available input, an agreed external input, or the agreed starting condition. Keep an unknown prerequisite visible; it is not a completed path.

### Functional decomposition: make a task clear enough to use

Divide a task when it hides a handoff, decision, dependency, or separate result that affects the workflow. Stop when a responsible person can understand the task and check its completion.

For each task, establish the action, required inputs or conditions, responsible person or system, output, and completion check. Gather these details during the conversation. Do not present them as a repeated form.

Examine the remaining results in the same way. Share a task across paths only when its work and requirements match. Similar names alone do not establish shared work.

### Process modeling: connect the work

Establish what starts a run and which tasks depend on others. Show decisions with labeled outcomes. Distinguish choices from work that can occur at the same time.

Add repeated work, waiting, and handoffs when they apply. Distinguish the end of one run from the event that starts the next run.

### State modeling: define meaningful changes

Identify the states needed to explain whether work can proceed or is complete. Establish the action or event that changes each state.

Keep actions and states distinct. A task being attempted does not prove that its intended result exists.

Include states in the workflow when that is clear. Add a separate Mermaid state diagram only when it materially clarifies the process.

## Build the Mermaid diagram

- Use the file path or folder supplied by the user. Otherwise, save `<workflow-name>.mmd` and `<workflow-name>.html` in the current project folder or working directory. Ask for a folder only when no location is available.
- Choose a short, descriptive filename. Check an existing file before editing it. Reuse it only if it belongs to this workflow.
- Save plain Mermaid source in the file, without Markdown code fences. Keep the saved file as the main diagram source.
- Start with confirmed results. Expand the diagram as the conversation establishes the work. An early diagram can be small and incomplete.
- Create both files as soon as the prompt supplies a result to map. Save each diagram change to the `.mmd` file and regenerate its HTML preview.
- Show the HTML preview link and source path after the first save and at session end. Read existing files before later edits so user changes are preserved.
- Use `flowchart TD` for the main workflow unless the user requests another direction. Show execution from top to bottom, even though discovery proceeds backward.
- Use stable node IDs and short, quoted labels. Label actions with a verb and an object. Label states as conditions.
- Make choices, parallel paths, and points that require all inputs explicit. Do not imply a sequence between independent tasks.
- Mark unresolved parts and proposals in text labels. Do not rely on color alone.
- Keep detailed task notes outside the diagram when they would make it difficult to read.
- If file tools are unavailable, provide the complete HTML in a code block. State that no file was saved. Do not start a canvas app as a fallback.

## Generate the HTML preview

Use [the HTML template](assets/workflow.html) to keep the preview consistent. It embeds the diagram source and loads Mermaid 12.0.0 from jsDelivr:

`https://cdn.jsdelivr.net/npm/mermaid@12.0.0/dist/mermaid.esm.min.mjs`

When Python is available, run [the generation script](scripts/render_html.py):

```sh
python3 <skill-directory>/scripts/render_html.py <workflow-path>.mmd --title "Workflow title"
```

The script writes an `.html` file beside the source. Use `--output <path>.html` when the user specifies a different HTML path. It uses only the Python standard library.

If Python is unavailable, generate equivalent HTML from the template. Encode the source as a JSON string. Escape `<` as `\u003c` in that string and HTML-escape the title. Do not insert raw source into JavaScript template literals.

Keep these properties:

- Embed the source in the HTML. Opening the file must not require a local server or a request to read the adjacent `.mmd` file.
- Load the library from the pinned CDN URL. Tell the user once that the preview needs internet access.
- Let the diagram viewport fill the browser's available width and height. Do not place it inside a centered card or a page with large margins.
- Show a compact title and zoom controls over the diagram. Include zoom in, zoom out, actual size, and fit-to-view. Do not add a footer, library credits, version text, or a success message.
- Support normal mouse-wheel and trackpad scrolling, mouse dragging to pan, and Control plus mouse wheel to zoom. Preserve the viewed point when zooming.
- Keep labels large and readable. Start at actual size or fit the width when needed. Use the Fit control to show the complete diagram.
- Keep Mermaid's strict security setting. Show a load or render error inside the diagram area if needed.
- Regenerate the same HTML file after source changes. Preserve user changes to the preview design when updating an existing file.

When a browser tool is available, open the first preview and refresh it after updates. Otherwise, provide the HTML link and tell the user to open or refresh it. Do not install a browser or start a service for this step.

## Check the model with the user

Walk forward through one representative case. Check that each required input exists before its task starts and that the path reaches the agreed result.

Then examine the failure cases that matter for this workflow. Ask about missing inputs, failed actions, rejected decisions, or repeat attempts only where they apply. Establish the response and stopping condition for each agreed case.

Check that each result has a path, each decision has defined outcomes, and each wait has a release condition. Check loops and handoffs for paths that cannot finish.

Inspect Mermaid syntax and diagram consistency. When browser access is available, check rendering, zoom controls, scrolling, and dragging. Check that labels remain readable and that the diagram uses the available viewport. Report a tool check only if it was performed. Valid syntax does not prove that the workflow is correct.

Save the complete Mermaid source and regenerate the HTML preview. Provide both file links, the agreed start and end, and any unresolved details. Ask for corrections to the model as a whole.

Call the workflow complete only within the agreed scope and level of detail. Required paths must have defined inputs, responsibilities, outputs, and completion checks. Applicable decisions, repeated work, and agreed failure responses must be resolved.

If the user stops earlier, save both files and identify the workflow as a draft. Include the file links, unresolved details, and the next question needed to continue.
