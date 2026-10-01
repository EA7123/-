"""Structural gates for storyboard-director prompt packages.

The supervisor still judges story and visual quality; this script rejects missing
handoffs, broken timing, and prompt sections without traceable shot evidence.
"""

import argparse
import json
import math
import sys
from pathlib import Path


METHODS = {f"D{i:02d}" for i in range(17)}
SHOT_FIELDS = (
    "id", "beat_id", "function", "method_impact", "camera", "blocking",
    "performance", "lighting_color", "sound", "cut_reason",
    "start_state", "end_state",
)
TRACE_FIELDS = (
    "function", "method", "camera", "blocking", "performance",
    "lighting_color", "sound", "transition",
)


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def check_text(container, key, path, errors):
    value = container.get(key) if isinstance(container, dict) else None
    if not has_text(value):
        errors.append(f"{path}.{key}: required nonempty text")
    return value


def check_role(roles, name, errors, allow_na=False):
    role = roles.get(name, {}) if isinstance(roles, dict) else {}
    status = role.get("status")
    allowed = {"pass", "not_applicable"} if allow_na else {"pass"}
    if status not in allowed:
        errors.append(f"roles.{name}.status: expected {sorted(allowed)}")
    check_text(role, "evidence", f"roles.{name}", errors)
    return status


def check_review(manifest, gate, errors):
    reviews = manifest.get("supervisor_reviews", {})
    review = reviews.get(gate, {}) if isinstance(reviews, dict) else {}
    if review.get("verdict") != "pass":
        errors.append(f"supervisor_reviews.{gate}.verdict: expected pass")
    check_text(review, "evidence", f"supervisor_reviews.{gate}", errors)


def validate(manifest, stage):
    errors = []
    if not isinstance(manifest, dict):
        return ["manifest: expected JSON object"]

    check_text(manifest, "case_id", "manifest", errors)
    source = manifest.get("source", {})
    source = source if isinstance(source, dict) else {}
    duration = source.get("duration_sec")
    if not isinstance(duration, (int, float)) or isinstance(duration, bool) or not math.isfinite(duration) or duration <= 0:
        errors.append("source.duration_sec: expected positive finite number")
        duration = None
    dialogue = source.get("dialogue")
    if not isinstance(dialogue, list):
        errors.append("source.dialogue: expected list, possibly empty")
        dialogue = []
    dialogue_ids = set()
    for index, line in enumerate(dialogue):
        path = f"source.dialogue[{index}]"
        line = line if isinstance(line, dict) else {}
        line_id = check_text(line, "id", path, errors)
        check_text(line, "speaker", path, errors)
        check_text(line, "text", path, errors)
        if line_id in dialogue_ids:
            errors.append(f"{path}.id: duplicate")
        dialogue_ids.add(line_id)

    direction = manifest.get("direction", {})
    direction = direction if isinstance(direction, dict) else {}
    dominant = direction.get("dominant_method")
    if dominant not in METHODS:
        errors.append("direction.dominant_method: expected D00-D16")
    supporting = direction.get("supporting_method")
    if supporting is not None and (supporting not in METHODS or supporting == dominant):
        errors.append("direction.supporting_method: expected distinct D00-D16 or null")
    check_text(direction, "reason", "direction", errors)
    consequences = direction.get("shot_consequences")
    if not isinstance(consequences, list) or len(consequences) < 2 or not all(has_text(item) for item in consequences):
        errors.append("direction.shot_consequences: expected at least two concrete decisions")

    roles = manifest.get("roles", {})
    for role in ("editor", "director", "drama", "art"):
        check_role(roles, role, errors)
    action_required = source.get("action_required")
    if not isinstance(action_required, bool):
        errors.append("source.action_required: expected boolean")
    action_status = check_role(roles, "action", errors, allow_na=True)
    if action_required is True and action_status != "pass":
        errors.append("roles.action: physical action requires a passed action-director handoff")
    if action_required is False and action_status != "not_applicable":
        errors.append("roles.action: no physical action requires a reasoned not_applicable status")
    check_review(manifest, "gate1", errors)
    if stage == 1:
        return errors

    check_role(roles, "storyboard", errors)
    shots = manifest.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("shots: expected nonempty list")
        shots = []
    seen_shots = set()
    referenced_lines = set()
    previous_end = None
    previous_state = None
    for index, shot in enumerate(shots):
        path = f"shots[{index}]"
        shot = shot if isinstance(shot, dict) else {}
        for key in SHOT_FIELDS:
            check_text(shot, key, path, errors)
        shot_id = shot.get("id")
        if shot_id in seen_shots:
            errors.append(f"{path}.id: duplicate")
        seen_shots.add(shot_id)
        start, end = shot.get("start_sec"), shot.get("end_sec")
        valid_time = all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in (start, end))
        if not valid_time or start < 0 or end <= start:
            errors.append(f"{path}: invalid start_sec/end_sec")
        elif previous_end is None and abs(start) > 0.05:
            errors.append(f"{path}.start_sec: first shot must start at 0")
        elif previous_end is not None and abs(start - previous_end) > 0.05:
            errors.append(f"{path}.start_sec: gap or overlap with previous shot")
        if valid_time:
            previous_end = end
        if previous_state is not None and shot.get("start_state") != previous_state:
            if not has_text(shot.get("transition_event")):
                errors.append(f"{path}.start_state: previous end_state differs without transition_event")
        previous_state = shot.get("end_state")
        ids = shot.get("dialogue_ids", [])
        if not isinstance(ids, list):
            errors.append(f"{path}.dialogue_ids: expected list")
        else:
            for line_id in ids:
                if line_id not in dialogue_ids:
                    errors.append(f"{path}.dialogue_ids: unknown {line_id}")
                referenced_lines.add(line_id)
    if duration is not None and previous_end is not None and abs(previous_end - duration) > 0.05:
        errors.append("shots: final end_sec must match source.duration_sec")
    for line_id in dialogue_ids - referenced_lines:
        errors.append(f"shots: locked dialogue {line_id} is not assigned")
    check_review(manifest, "gate2", errors)
    if stage == 2:
        return errors

    check_role(roles, "compiler", errors)
    outputs = manifest.get("outputs", {})
    outputs = outputs if isinstance(outputs, dict) else {}
    for group in ("character_prompts", "scene_prompts"):
        items = outputs.get(group)
        if not isinstance(items, list) or not items or not all(has_text(item) for item in items):
            errors.append(f"outputs.{group}: expected nonempty prompt texts")
    video = outputs.get("video_prompts")
    if not isinstance(video, list) or not video:
        errors.append("outputs.video_prompts: expected shot-linked prompt sections")
        video = []
    covered = set()
    all_video_text = []
    for index, section in enumerate(video):
        path = f"outputs.video_prompts[{index}]"
        section = section if isinstance(section, dict) else {}
        shot_id = section.get("shot_id")
        if shot_id not in seen_shots:
            errors.append(f"{path}.shot_id: no matching Shot Card")
        if shot_id in covered:
            errors.append(f"{path}.shot_id: duplicate")
        covered.add(shot_id)
        prompt = check_text(section, "text", path, errors)
        prompt = prompt if has_text(prompt) else ""
        all_video_text.append(prompt)
        evidence = section.get("evidence")
        evidence = evidence if isinstance(evidence, dict) else {}
        for field in TRACE_FIELDS:
            phrase = evidence.get(field)
            if not has_text(phrase) or phrase not in prompt:
                errors.append(f"{path}.evidence.{field}: quote an exact phrase retained in text")
    for shot_id in seen_shots - covered:
        errors.append(f"outputs.video_prompts: missing section for {shot_id}")
    compiled = "\n".join(all_video_text)
    for line in dialogue:
        if isinstance(line, dict) and has_text(line.get("text")) and line["text"] not in compiled:
            errors.append(f"outputs.video_prompts: locked dialogue {line.get('id')} missing verbatim")
    check_review(manifest, "gate3", errors)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="JSON role/shot/prompt manifest")
    parser.add_argument("--stage", type=int, choices=(1, 2, 3), required=True)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        print(json.dumps({"stage": args.stage, "pass": False, "failures": [str(exc)]}))
        return 2
    errors = validate(manifest, args.stage)
    print(json.dumps({"stage": args.stage, "pass": not errors, "failures": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
