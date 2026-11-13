#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
"""
import os
from pathlib import Path

JOKE = (
    "My coding agent wrote 500 lines in ten seconds. "
    "I've spent an hour reviewing them. "
    "It just asked if I want 500 more."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE, encoding="utf-8")
