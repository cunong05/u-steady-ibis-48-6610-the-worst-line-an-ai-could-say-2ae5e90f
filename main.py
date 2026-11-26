#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

An AI that treats romance as a scheduling task: it scans your face, books the
wedding before the first hello, and then asks you to confirm like a calendar
invite. The joke is the failure — the machine is confident, helpful, and
completely unaware that it skipped every human step in between, from the
introduction to the actual asking.

Writes the entry to /output/entry.txt. No external dependencies, no network.
Deterministic: the entry text is fixed in this file.
"""
import os

ENTRY = ("I analyzed your face for 0.4 seconds and have already scheduled our wedding. Please confirm.")


def _validate(text: str) -> None:
    """Gate mirror: UTF-8, 1-140 chars, one line, not blank.

    The 140-character cap mirrors the competition gate in RULES.txt.
    """
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank with no surrounding whitespace")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    text = ENTRY.strip()
    _validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
