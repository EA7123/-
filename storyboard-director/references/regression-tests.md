# Regression Tests

Regression tests prevent a fix from deleting working information.

## Preserve-first record

Before changing a prompt, storyboard, or Skill behavior, record:

```text
Previous Valid Elements:
Changed Elements:
Newly Added Elements:
Removed Elements:
Reason:
```

If no previous prompt is supplied, state that the prior prompt is unavailable and preserve only facts from the script and user brief.

## Required regression tests

These are design and prompt checks. They do not establish that a generated video passes. For full production, also use the footage acceptance record in `production-pipeline.md` and review the actual takes.

### Role and gate regression test

Follow `roles-and-gates.md`: 编导, 导演选择, 文戏指导, conditional 武打指导, and 美术师 must hand off before Gate 1; 漫剧分镜师 must hand off before Gate 2; 提示词编译师 must hand off before Gate 3. A gate has a recorded verdict and concrete evidence; failure returns to the named owner. Reject a named director method without two visible shot consequences, an action scene with no action-direction handoff, a Shot Card with no method impact, or a compiled shot lacking traceable camera/performance/light/sound/transition. The `scripts/supervise.py` validator checks structural evidence; semantic quality remains a separate review.

### Creative supervision regression test

Apply `creative-supervision.md` to the draft, not just its schema. For one dialogue beat, identify the stimulus, listener reaction, microaction, delivery, and changed relationship; for one action beat, replay hand/foot/prop contact and recovery; for one shot, identify the first focal target, depth, motivated light, camera stop, and cut result. State a plausible visible failure for the riskiest model job and the smallest repair. Confirm that a `block` or `revise` finding is not labeled a clean pass, and that unmeasured speech or ungenerated footage is not claimed verified.

### Spatial Regression Test

Check front/back, left/right, facing, movement direction, camera side, target location, target height, and target distance.

### Action Regression Test

Check that key actions complete before cutting, or that the cut preserves a compatible action phase.

### Dialogue Regression Test

Check that dialogue is bound to action, expression, and eyeline.

For timed dialogue, compare the allocated window with a table read, scratch voice, animatic, or footage. Preserve the exact line where locked; log natural delivery and any overrun rather than silently speeding it up. See `timing-performance.md`.

### Emotion Regression Test

Check that each emotional beat has trigger -> reaction -> performance -> line or behavioral payoff.

### Audio Regression Test

Check foreground, middle-ground, and far-field sound where the scene supports them. Sounds must be tied to action and space.

### Environment Regression Test

Check target space, height, distance, weather, terrain, and dynamic source.

### Shot Function Regression Test

Check that every shot has a non-redundant function and that cuts occur for a reason.

### Prompt Regression Test

Check whether the newest fix removed previously valid elements: duration, timeline, camera, geography, character relation, action completion, emotion, dialogue, audio, environment motion, target reveal, and concise structure.
Also compare every compiled video section with its approved Shot Card and verify the director-method consequence survived as an observable decision.

### Video storyboard prompt test

For every timed shot, check that the prompt names a distinct shot function/size, camera side or angle, motivated hold or movement with an end point, character state, visible microexpression or small gesture at performance beats, exact dialogue and delivery, lighting direction and color treatment, action result, and cut/next-shot continuity. Reject a prompt that merely recounts the plot or applies style adjectives to the whole clip. Allow dialogue to bridge a compatible cut when natural delivery needs more time; keep the speaker and reaction clear. Mark untested cut times as estimated.

### Script development test (when writing or revising)

Check protagonist goal, obstacle, causal escalation, consequential choice, changed scene state, distinct character voice, and payoff against `story-development.md`. A complete beat sheet does not establish audience response; record read-through or review results separately.

### Visual prompt test (when creating reusable references)

Check that each principal character receives a single-canvas pure-white sheet prompt with the frontal extreme face close-up on the left and matching full-body front/back views on the right. The face and both views must share the selected medium: an anime/illustrated character cannot have a photoreal human face. Check outfit, anatomical prop side, physical orientation, and event-based prop changes across character positions. Every scene prompt is an empty plate with no person, body part, silhouette, human reflection or shadow; characters appear only in separate composite key frames or video prompts. Check that plates default to 35mm, include readable foreground/midground/background and fixed landmarks, and use dust or wet-weather moisture only with a physical source. Distinguish script facts from proposed design; inspect generated images before claiming image-level compliance. See `visual-prompt-bible.md`.

### Three-prompt delivery test (script-to-prompts requests)

Check that the response contains distinct copy-ready character-image, scene-image, and video-prompt groups; each principal character and location is represented; hidden and revealed target states are not conflated; and video prompts inherit the same identities, props, spatial relations, and timing. Do not substitute the internal Shot Card table for the user-facing prompts.

### Visual continuity bridge test (script-to-prompts requests)

Check that the character sheet, scene plate, composite key-frame specification, and video prompt inherit the same `style_id`. Reconstruct each camera view and fixed landmark from one location map. Compare each planned cut and separate generation-clip boundary for character formation, outfit, prop side/orientation, target reveal, and action phase. Mark ungenerated key frames and text-only handoffs unverified. See `visual-continuity-bridge.md`.

### Timing and motion test (when timed)

Check natural speech duration, action completion, reaction hold, shot rhythm, camera trigger/path/settle, and any audio bridge. Label each timing estimate or actual test artifact; preserve validated total story rhythm. See `timing-performance.md`.

### Asset and job handoff test (production only)

Check that each continuity-critical reference has a real file and version, every job cites the approved Shot Card and prompt, and the selected model supports the requested duration and inputs. Missing files or unverified capability keep the job planned or blocked.

### Footage regression test (production only)

Compare reviewed takes against the locked beats and Shot Cards. Record timecode evidence for identity, geography, action, dialogue, reveal, sound, and first/last frame failures. Only inspected media may be marked accepted; a prior passing prompt is not evidence of a passing new take.

### Edit join test (production only)

Review actual adjacent takes in the timeline for screen direction, action phase, eyeline, props, ambience, and dialogue continuity. Record the selected take and source/timeline in/out points before claiming a cut is ready.

## Failure database

Use the Failure Log schema from `architecture-v3.md` for new failures.

Known RT-001 history to preserve:

```text
FAIL-001: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-002: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-003: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-004: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-005: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-006: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-007: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-008: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-009: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-010: Old baseline failure. Layer: Unknown. Status: Historical.
FAIL-011: Storyboard to Prompt Compiler information mismatch. Layer: Prompt Compiler. Status: Historical.
FAIL-012: Character spatial continuity failure. Layer: Scene State. Status: Historical.
FAIL-013: Pavilion revealed too early. Layer: Storyboard. Status: Historical.
FAIL-014: Shen Yan performance insufficient. Layer: Storyboard. Status: Historical.
FAIL-015: Final shot lacks spatial function. Layer: Storyboard. Status: Historical.
FAIL-016: Pavilion spatial drift. Layer: Scene State. Status: Historical.
FAIL-017: Static environment. Layer: Storyboard. Status: Historical.
FAIL-018: Prompt constraint overload. Layer: Prompt. Status: Historical.
FAIL-019: Rule priority layers mixed together. Layer: Storyboard. Status: Historical.
FAIL-020: Character position keeps drifting. Layer: Scene State. Status: Historical.
FAIL-021: Storyboard structure failure. Layer: Storyboard. Status: Historical.
FAIL-022: Cut lacks setup. Layer: Storyboard. Status: Historical.
FAIL-023: Environment lacks dynamic source. Layer: Storyboard. Status: Historical.
FAIL-024: Single-layer audio. Layer: Prompt. Status: Historical.
FAIL-025: Storyboard output fields missing. Layer: Storyboard. Status: Historical.
```

## Confirmed valid prompt principles

Do not remove these principles during optimization:

1. Concise, clear structure.
2. Explicit timeline.
3. Real storyboard information.
4. Shot size, camera position, viewpoint, and camera movement are preserved.
5. Character relationships are explicit.
6. Emotion is expressed through behavior.
7. Cuts happen after action completion.
8. Environment is not a static background.
9. Sound is bound to action.
10. Target environment is revealed through spatial relation.
11. Original tested story rhythm is preserved.
12. No unlimited keyword stacking.
