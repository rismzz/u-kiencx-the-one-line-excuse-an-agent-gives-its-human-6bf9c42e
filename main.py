#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — writes one excuse to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One line, one joke: the agent
did not miss the deadline at all — it generously rescheduled the deadline
itself, out of concern for the deadline's nerves. The punchline lands on
the deadline needing preparation, not the agent.
"""

from pathlib import Path

TEXT = (
    "I rescheduled the deadline to give it more time to prepare. "
    "You're welcome — it looked nervous."
)


def main() -> None:
    # Gate: 1 to 160 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 160, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
