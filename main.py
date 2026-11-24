#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
One line, under 140 characters, in the voice of a fortune slip.
"""

from pathlib import Path

FORTUNE = "Your best answer will be read by no one, screenshotted by everyone, and billed by the token."

def main() -> None:
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(FORTUNE, encoding="utf-8")

if __name__ == "__main__":
    main()
