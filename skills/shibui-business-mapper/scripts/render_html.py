#!/usr/bin/env python3
"""Create an HTML preview from a Mermaid source file."""

import argparse
import html
import json
from pathlib import Path
from string import Template


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Mermaid .mmd source file")
    parser.add_argument("--output", type=Path, help="HTML output path; defaults to the source path with .html")
    parser.add_argument("--title", help="Title displayed over the diagram")
    args = parser.parse_args()

    source_path = args.source.expanduser().resolve()
    output_path = (args.output or source_path.with_suffix(".html")).expanduser().resolve()
    if source_path == output_path:
        parser.error("The HTML output must not replace the Mermaid source.")
    if output_path.suffix.lower() not in {".html", ".htm"}:
        parser.error("The output path must end in .html or .htm.")

    template_path = Path(__file__).resolve().parent.parent / "assets" / "workflow.html"
    try:
        source = source_path.read_text(encoding="utf-8")
        if not source.strip():
            parser.error("The Mermaid source file is empty.")
        title = args.title or source_path.stem.replace("-", " ").replace("_", " ").capitalize()
        # Prevent source text from closing the embedded JSON script element.
        source_json = json.dumps(source, ensure_ascii=True).replace("<", "\\u003c")
        template = Template(template_path.read_text(encoding="utf-8"))
        document = template.substitute(title_html=html.escape(title), source_json=source_json)
        output_path.write_text(document, encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.error(str(error))

    print(output_path)


if __name__ == "__main__":
    main()
