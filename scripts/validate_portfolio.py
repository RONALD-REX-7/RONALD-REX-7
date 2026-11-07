#!/usr/bin/env python3
"""Validate local visual assets and basic integrity of the GitHub profile README."""
from __future__ import annotations
import re, sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

if not README.is_file():
    fail("README.md is missing")
content = README.read_text(encoding="utf-8")
headings = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
if len(headings) < 8:
    fail(f"Expected at least 8 Markdown headings; found {len(headings)}")
for section in ("LumaGuard", "EmbeddedLab OS", "MineGuard", "QUARTZSENTRY", "AWS certifications", "Education", "Connect"):
    if section.casefold() not in content.casefold():
        fail(f"README is missing required content: {section}")

credential_patterns = (
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
)
evidence = ROOT / "docs" / "PROJECT_EVIDENCE.md"
if not evidence.is_file():
    fail("docs/PROJECT_EVIDENCE.md is missing")
docs_text = content + "\n" + evidence.read_text(encoding="utf-8")
for pattern in credential_patterns:
    if pattern.search(docs_text):
        fail("Potential credential pattern found in user-facing Markdown")

references = re.findall(r"<img\b[^>]*?\bsrc=[\"']([^\"']+)[\"']", content, re.IGNORECASE)
references += re.findall(r"!\[[^\]]*\]\(([^)]+)\)", content)
local_images = []
for reference in references:
    reference = reference.strip().split()[0].strip("<>")
    if reference.startswith(("https://", "http://", "data:")):
        continue
    path = (ROOT / urlsplit(reference).path).resolve()
    if ROOT.resolve() not in path.parents and path != ROOT.resolve():
        fail(f"Image reference escapes repository root: {reference}")
    if not path.is_file():
        fail(f"Missing local image: {reference}")
    local_images.append(path)
if not local_images:
    fail("No local image references were found")

# Parse SVGs that the README actually displays. Historical, unused SVG assets
# are intentionally left untouched and must not break the current portfolio.
svg_files = sorted({path for path in local_images if path.suffix.lower() == ".svg"})
for svg in svg_files:
    try:
        ET.parse(svg)
    except ET.ParseError as exc:
        fail(f"Malformed referenced SVG {svg.relative_to(ROOT)}: {exc}")

print(f"README headings: {len(headings)}")
print(f"Local image references verified: {len(local_images)}")
print(f"Referenced SVG assets parsed: {len(svg_files)}")
print("Portfolio integrity checks passed.")
