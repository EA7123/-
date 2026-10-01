# Storyboard outputs

## Default script-to-prompts delivery

When the user provides a script and asks for AI drama prompts without a narrower format, deliver in this order:

1. Brief continuity assumptions: only inferred visual design, duration/model uncertainty, and locked story facts that materially affect generation.
2. **Character image prompts**: one copy-ready prompt per principal character using the exact white-background composite layout in `visual-prompt-bible.md`: left frontal extreme face close-up; right adjacent full-body front and back views. Include stable costume and prop side/orientation. Lock one medium across all views; illustrated characters cannot have photographic faces.
3. **Scene image prompts**: empty environment plates only, one per distinct location and another for a materially different reveal state. No people, body parts, silhouettes, human reflections or shadows. Default to 35mm, layered foreground/midground/background, fixed spatial anchors, readable depth, and physically motivated airborne dust or wet-weather moisture.
4. **Video prompts**: per generated clip or shot, with the timeline, camera, relative character positions, prop state changes, complete action, performance/dialogue, environment motion, sound, reveal, and continuity at clip boundaries. Preserve the script's tested total rhythm.
5. **Audit receipt**: selected director method ID and two visible consequences; Gate 1/2/3 structural status, creative review status, the highest remaining `watch` risk and its next evidence needed. Keep this compact. Never describe estimated timing or ungenerated footage as verified, or state a pass that was not performed.

Put each usable prompt in its own fenced block with its ID, aspect ratio, and proposed/approved design status outside the block. Do not make the reader extract prompts from a large Shot Card table. Include a compact state or timing note only when it prevents a material ambiguity. Label estimated sub-shot time boundaries as estimates.

Internally, compile all three groups from one style record, a location map, start/end composite key frames, and a cut/clip boundary ledger as specified in `visual-continuity-bridge.md`. These are not an extra required user-facing group. Surface a map sketch or boundary note only if a spatial ambiguity needs review.

## Standard delivery

Use this detailed storyboard delivery when the user asks to inspect or edit the shot plan.

Begin with a compact visual thesis: format/aspect ratio, point of view, lens tendency, camera-movement policy, pacing, dominant method, and priority risks.

Then define the scene states before the shot table:

```text
Scene State:
Character State:
Environment Anchor:
Reveal State:
Audio State:
```

Then use one row per shot. For v3 work, prefer the complete Shot Card table below.

| 镜号 | 时间/时长 | Shot Function | 导演方法影响 | 景别与构图 | 焦段范围 | 机位/机侧/角度/视角 | 运镜起止 | 人物位置/关系/朝向 | 动作阶段 | 微表情/小动作/视线 | 光向/色调 | 对白 | 分层声音 | 环境动态 | 动作完成点 | 切镜理由 | 下一镜承接 |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

After each scene, add only when useful:

- Scene logic: why this coverage pattern was chosen.
- Risk/fallback: expensive, technically difficult, or generation-fragile shots and a simpler alternative.
- Regression notes: only failures or meaningful risks, not a restatement of all rules.

## Shot Card v3

When detailed output is required, each shot must contain:

```text
Time:
Shot Function:
Director Method Impact:
Shot Size:
Camera Position:
Camera Side:
Camera Angle:
Camera Movement (trigger, path, speed, stop):
Viewpoint:
Lens / Focal Character:
Composition:
Character Position:
Character Relation:
Character Facing:
Movement Direction:
Action:
Expression:
Observable Microexpression and Small Gesture:
Eye Direction:
Lighting Direction and Color Treatment:
Dialogue:
Audio:
Environment Motion:
Action Completion Point:
Cut Reason:
Next Shot Continuity:
```

## Compact mode

For early discussion, provide beat, shot function, framing, camera action, action completion, and purpose only. Do not invent production detail the user did not request.

## Key-frame prompt mode

For each selected key frame, write a self-contained still prompt in this order: subject and action; setting; stable spatial anchors; character relation; camera height and lens band; depth/focus; motivated lighting; palette/texture; aspect ratio. Include only continuity anchors the generator must preserve.

When references will recur across shots, first create character and scene identity cards and plate prompts using `visual-prompt-bible.md`. Cite their asset IDs and approved versions in each composite key frame. If reference files do not exist, provide coherent proposed designs and say they are not yet approved assets.

## Video prompt mode

For each shot, specify start frame, subject motion, environmental motion source, camera motion, focus behavior, sound layer, timing, and end frame. Keep one principal beat per generated clip unless a tested duration requires multiple internal shots. Avoid vague style labels, contradictory camera commands, and rule text.

A multi-shot video prompt must read like an executable miniature storyboard, not a plot summary. For each timed shot, state: shot function and size; camera side/angle and whether it holds or moves, including movement trigger and end; character formation and action phase; a visible microexpression plus small gesture at reaction or dialogue beats; exact speaker/line and delivery; lighting direction and color treatment; sound; and the result that motivates the next cut. Keep the shared lighting and palette coherent across shots while letting the framing change for a reason. Use concrete observable behavior instead of labels such as "concerned" or "tired" alone.

If natural dialogue duration exceeds a proposed shot window, begin the line before a cut or carry it over a phase-compatible reaction/action shot with clear speaker identity. Preserve exact words and total tested duration. Mark internal cut points estimated until a table read, animatic, or generated video verifies them.

For separate generated clips, carry the preceding end state into the next start state. If real first/last frame assets exist and the selected model supports them, cite their reference handles in the generation job; otherwise describe the compatible states in text and mark the visual handoff unverified.

For speech-heavy or tightly timed clips, attach a timing ledger from `timing-performance.md` to the internal job record. The final prompt carries the necessary timing cues; the ledger records measured speech/action durations and test status. Do not present estimated sub-shot timestamps as measured performance.

## Prompt compiler output

Final AI-video prompts should be shorter than the Shot Cards but preserve all execution-critical facts:

- Duration, aspect ratio, and base style
- Timeline and shot count
- Scene, character formation, camera side, and target anchors
- Per-shot function, camera position and movement, action, visible microexpression/gesture, dialogue delivery, lighting/color, audio, environment motion, cut logic, and continuity
- Observable consequences of the selected director method, not its name as a decorative label

Do not include Failure Log, regression tables, priority explanations, or repeated negative prompts unless the user explicitly asks for diagnostics.

## Review summary

End with a brief note identifying the scene’s dominant method, any intentional continuity break, shots that can be removed without losing meaning, failed output-lock items, and unresolved reference or timing dependencies.
