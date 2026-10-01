# AI drama production pipeline

Use this reference for a full episode or production workflow. The storyboard and prompt rules remain in `architecture-v3.md`; this file covers the work before and after them. Do not present an ungenerated plan as a finished episode.

## Handoff map

```text
Series / episode brief
  -> approved script and beat sheet
  -> visual asset manifest
  -> Scene State and Shot Cards
  -> generation job manifest
  -> generated takes and footage QC
  -> edit decision list and timeline
  -> episode review and delivery
```

Keep one stable `episode_id` and `shot_id` across these records. Give every approved script, asset, prompt, model profile, and take its own version or immutable file reference. A change to one record invalidates only dependent jobs and reviews; preserve accepted work elsewhere.

## 1. Series and episode brief

Before directing a full episode, record only the story decisions needed to judge the edit:

For new or rewritten scripts, use `story-development.md` to create and review the beat sheet before the script is approved. Preserve any locked source material.

```text
series_id / episode_id:
format and target runtime:
audience and release format, if supplied:
series premise and character arcs:
episode goal and main conflict:
opening hook:
turning points:
ending payoff or cliffhanger:
non-negotiable dialogue, events, relationships, and tested timing:
source script version and approval status:
```

Map every scene to a dramatic function and each shot to a beat. A scene that has attractive shots but no causal contribution is a script or pacing issue, not a prompt issue. Do not invent episode-level hooks or rewrite locked story facts when the user supplied only a single scene. Mark unknown fields `not supplied`.

Handoff gate: the beat order, dialogue, character motivation, and timing are approved or explicitly marked provisional before expensive generation begins.

## 2. Visual asset manifest

Create reusable asset IDs for characters, outfits, locations, props, and visual style. For each asset, record:

Use `visual-prompt-bible.md` to draft character and scene identity cards, plate prompts, and composite key frames. The manifest records approved files; prompt text alone does not make an asset approved.

```text
asset_id / type / version:
canonical description and invariant features:
source and rights or use status:
actual file path or URL, or `missing`:
available views: front / side / back / expression / full-body, as applicable:
scene or shot usage:
known variation allowed:
approved reference version:
```

For characters, distinguish identity from costume, pose, emotion, and lighting. For locations, pair reference images with a simple top-down orientation or landmark map, entrances, exits, camera axis, and target anchors. For props, record owner, hand, position, and continuity state where it matters. A textual Scene State defines geography; it does not substitute for reference media when visual identity must persist across shots or episodes.

Do not claim a reference is locked until the actual asset exists and its version is recorded. If a model supports only some reference types or a limited number of inputs, choose the minimum set that preserves identity and geography; record the omitted references as risks.

Handoff gate: every continuity-critical character, location, and prop has an approved asset version or an explicit missing-asset blocker.

## 3. Generation job manifest

Convert approved Shot Cards into executable jobs without copying the entire card into the prompt. A job is one model invocation; one job may contain multiple internal shots only when the selected model supports it and the timing has been tested. Split jobs according to model capability and observed results, not a universal duration rule.

For dialogue-heavy jobs, attach the `timing-performance.md` ledger with a test status and measured audio or animatic paths when they exist.

```text
job_id / episode_id / source_shot_ids:
script_version / shot_card_version / compiler_version:
model and model_version / supported duration / aspect ratio / reference modes:
duration / resolution / frame rate, if selectable:
prompt_version and exact prompt text or file path:
reference asset_ids and versions / first frame / last frame, if supported:
seed and control parameters, if supported:
required first state / required final state / reveal timing:
expected dialogue and audio responsibilities:
candidate count / retry limit / cost estimate or actual cost:
status: planned | blocked | ready | generated | reviewed | accepted | rejected:
output take_ids and file paths:
```

The model profile is a measured capability record, not a promise: supported input types, durations, audio behavior, output formats, and known limitations. Check the selected model's current documentation or actual account settings before creating executable jobs. If the model cannot reliably create dialogue, lip sync, or layered sound, route those to the later sound pass and keep their timing markers in the job.

Use a bounded retry loop. Before retrying, identify whether the failure belongs to the script, asset, Shot Card, compiler, prompt, or model output. Change the smallest relevant input, save the new version, and retain the prior accepted take. Never spend generation credits or invoke an external model unless the task authorizes it and the required access is available.

Handoff gate: the job has real asset references, a supported model configuration, and an expected result that can be checked in footage. If dialogue or action timing is still estimated, state that risk in the job; missing critical references or unsupported settings keep it `blocked` or `planned`.

## 4. Footage review and acceptance

Text checks validate the plan. Footage QC validates the generated take. Review the actual video and listen to its actual audio, using frame or timecode evidence for failures:

```text
take_id / job_id / file path / reviewed_at:
reviewer and review method:
identity and costume consistency:
scene geography, screen direction, and target anchor:
action phases and result state:
performance, dialogue, timing, and lip sync when present:
reveal timing and environment motion:
audio presence, sync, and defects when present:
visual artifacts and unwanted text or objects:
first frame / last frame compatibility with neighboring shots:
verdict: accepted | fixable_in_edit | regenerate | blocked:
evidence: timecodes or frame references:
failure_id / owner layer / next action:
```

Reject or repair a take when a story-critical invariant fails: wrong character, broken geography, missing action completion, wrong dialogue, or premature reveal. Less important defects can be accepted only with an explicit edit fix and owner. A prompt passing the Output Lock does not make its video pass QC. Record the candidate that was selected and why; do not call generated takes "validated" without inspecting the media.

Handoff gate: every shot used in the edit has an accepted take or a documented edit fix. Unreviewed takes remain unapproved.

## 5. Edit decision list and timeline

Assemble accepted takes into a story sequence. Preserve source identity and the exact in/out points:

```text
episode_id / timeline_version / target format and runtime:
ordered shot_id -> take_id -> source in/out -> timeline in/out:
cut or transition reason and continuity bridge:
dialogue, sound, music, and subtitle cue IDs, if available:
missing shot or pickup requirement:
opening hook and ending payoff check:
final review status and export path, when rendered:
```

Check the joins in the timeline: matching screen direction, action phase, eyeline, character/prop state, ambience, and audio lead or tail. Trim or reorder only when the story beat and tested timing still work. If the edit exposes a missing connective image, create a pickup job tied to that gap and review it like any other take. Keep a reviewable rough cut before treating the episode as delivered.

Handoff gate: the assembled timeline has no unresolved critical continuity failure, required dialogue is present, the episode goal and ending land, and the target format is verified on the rendered export. A written edit decision list is a plan, not evidence of a rendered export.

## Output by request scope

- Storyboard request: use the existing Shot Card and prompt outputs; no production manifest is required.
- Production plan without access to assets or models: deliver the brief, asset inventory with missing fields, planned jobs, QC criteria, and edit outline. Mark generation, footage QC, and export as pending.
- Production with authorized access: retain concrete file paths, versions, takes, QC evidence, selected edit, and export status. Stop at the first missing approval or technical dependency and report it precisely.

## RT-001 boundary

The mountain-road scene's tested 10-second story rhythm, exact dialogue, character formation, and late pavilion reveal remain fixed. Asset binding and model job setup may be added around that case, but an untested job split or model change cannot be described as preserving the validated result. See `rt-001-mountain-road.md` for its concrete production handoff.
