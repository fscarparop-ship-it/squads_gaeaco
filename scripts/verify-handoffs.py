#!/usr/bin/env python3
"""Verify brand-squad handoff contracts and workflow outputs resolve to real fields.

1. Handoff contracts. brand-squad/data/cross-squad-handoffs.yaml names the
   outputs a sending task produces and the input fields a receiving task
   consumes. Nothing enforces that those names match the task files, so a
   contract can silently reference a field that was never declared.

2. brand-squad workflow outputs. Every output a brand-squad workflow step
   names for a brand-squad task must be declared in that task's Saida or
   Entrada. Scoped to brand-squad: the other squads use workflow outputs for
   granular deliverables and have not adopted this convention.

Run: python3 scripts/verify-handoffs.py
Exits non-zero and lists every unresolved reference.
"""

import glob
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


def workflow_steps(data):
    for phase in data.get("phases", []):
        yield phase.get("task"), phase.get("outputs", [])
        for step in phase.get("steps", []):
            yield step.get("task"), step.get("outputs", [])


def check_brand_workflows(failures):
    for path in sorted(glob.glob("brand-squad/workflows/*.yaml")):
        data = yaml.safe_load(open(path))
        for task, outputs in workflow_steps(data):
            if not task or not outputs:
                continue
            task_path = os.path.join("brand-squad", "tasks", task)
            if not os.path.exists(task_path):
                failures.append(f"{path}: task not found — {task}")
                continue
            text = open(task_path).read()
            for output in outputs:
                name = list(output)[0] if isinstance(output, dict) else output
                if not declares(text, name):
                    failures.append(f"{path}: {task} does not declare output '{name}'")


def main():
    contracts = yaml.safe_load(open(CONTRACTS))
    failures = []

    check_brand_workflows(failures)

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
