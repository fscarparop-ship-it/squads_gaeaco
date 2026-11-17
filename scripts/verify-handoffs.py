#!/usr/bin/env python3
"""Verify every field named in the cross-squad handoff contracts actually exists.

The contracts in brand-squad/data/cross-squad-handoffs.yaml name the outputs a
sending task produces and the input fields a receiving task consumes. Nothing
enforces that those names match the task files, so a contract can silently
reference a field that was never declared — the handoff then looks wired up
while nothing can receive it.

Run: python3 scripts/verify-handoffs.py
Exits non-zero and lists every unresolved reference.
"""

import os
import re
import sys

import yaml

CONTRACTS = "brand-squad/data/cross-squad-handoffs.yaml"
SQUADS = ["brand-squad", "copy-squad", "design-squad", "storytelling", "traffic-masters"]


def locate(filename):
    for squad in SQUADS:
        for subdir in ("tasks", "workflows"):
            path = os.path.join(squad, subdir, filename)
            if os.path.exists(path):
                return path
    return None


def declares(text, name):
    # Task frontmatter uses "campo:", workflow input blocks use "field:".
    pattern = r"(?:campo|field):\s*" + re.escape(name) + r"\s*$"
    return re.search(pattern, text, re.M) is not None


def main():
    contracts = yaml.safe_load(open(CONTRACTS))
    failures = []

    for name, handoff in contracts["handoffs"].items():
        for output in handoff.get("source_outputs", []):
            path = locate(output["from_task"])
            if path is None:
                failures.append(f"{name}: sending file not found — {output['from_task']}")
            elif not declares(open(path).read(), output["name"]):
                failures.append(
                    f"{name}: {output['from_task']} does not declare output '{output['name']}'"
                )

        for target in handoff.get("target_inputs", []):
            ref = target.get("task") or target.get("workflow")
            path = locate(ref)
            if path is None:
                failures.append(f"{name}: target file not found — {ref}")
            elif not declares(open(path).read(), target["field"]):
                failures.append(
                    f"{name}: {ref} does not declare input '{target['field']}'"
                )

    for failure in failures:
        print(failure)

    if failures:
        print(f"\n{len(failures)} unresolved handoff reference(s)")
        return 1

    print("All handoff references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
