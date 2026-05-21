#!/usr/bin/env python3
"""Write a downstream R agent prompt to a Markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


def write_prompt(input_prompt: Path, output_md: Path, title: str) -> None:
    """Write a prompt text file as a standalone Markdown document."""
    prompt = input_prompt.read_text(encoding="utf-8").strip()
    output_md.parent.mkdir(parents=True, exist_ok=True)

    content = "\n".join(
        [
            f"# {title}",
            "",
            "```text",
            prompt,
            "```",
            "",
        ]
    )
    output_md.write_text(content, encoding="utf-8")


def main() -> None:
    """Parse arguments and write the Markdown prompt file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_prompt", type=Path, help="Plain text prompt file.")
    parser.add_argument("output_md", type=Path, help="Output Markdown prompt file.")
    parser.add_argument("--title", default="R Agent Prompt", help="Markdown title.")
    args = parser.parse_args()

    write_prompt(args.input_prompt, args.output_md, args.title)


if __name__ == "__main__":
    main()
