#!/usr/bin/env python3
"""Validate the bundled paper catalog using only the Python standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path

WEIGHTS = {"topic_match": 35, "method_value": 20, "source_quality": 15, "cross_lane_bridge": 10, "applied_value": 10, "archival_value": 10}
STATUSES = {"peer_reviewed", "workshop_peer_reviewed", "preprint", "metadata_only"}


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1] / "references" / "paper-catalog.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        fail("schema_version must be 1.0")
    papers = data.get("papers")
    if not isinstance(papers, list) or not papers:
        fail("papers must be a non-empty list")
    seen = {"id": set(), "title": set(), "doi": set(), "url": set()}
    for index, paper in enumerate(papers, 1):
        prefix = f"paper[{index}]"
        required = ("id", "title", "year", "lane", "venue", "status", "url", "why", "how", "what", "transfer", "limitation", "scores", "total")
        for key in required:
            if key not in paper:
                fail(f"{prefix}: missing {key}")
        if not isinstance(paper["year"], int) or not 2000 <= paper["year"] <= 2100:
            fail(f"{prefix}: invalid year")
        if paper["status"] not in STATUSES:
            fail(f"{prefix}: invalid status {paper['status']}")
        if not str(paper["url"]).startswith("https://"):
            fail(f"{prefix}: URL must use https")
        scores = paper["scores"]
        if set(scores) != set(WEIGHTS):
            fail(f"{prefix}: score keys differ from rubric")
        for key, cap in WEIGHTS.items():
            value = scores[key]
            if not isinstance(value, int) or not 0 <= value <= cap:
                fail(f"{prefix}: {key}={value!r} outside 0..{cap}")
        if paper["status"] == "preprint" and scores["source_quality"] > 9:
            fail(f"{prefix}: preprint source_quality exceeds 9")
        if sum(scores.values()) != paper["total"]:
            fail(f"{prefix}: total does not equal score sum")
        for key in ("id", "title", "url"):
            normalized = str(paper[key]).strip().lower()
            if normalized in seen[key]:
                fail(f"{prefix}: duplicate {key}: {paper[key]}")
            seen[key].add(normalized)
        doi = str(paper.get("doi") or "").removeprefix("https://doi.org/").lower()
        if doi:
            if doi in seen["doi"]:
                fail(f"{prefix}: duplicate DOI: {doi}")
            seen["doi"].add(doi)
    print(f"OK: {len(papers)} papers validated from {path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
