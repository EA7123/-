---
name: storyboard-director
description: Turn an AI drama script into production-ready character-sheet image prompts, spatial scene image prompts, and cinematic video prompts. Also support storyboard, continuity, timing, script revision, and production planning when requested. Use for 漫剧提示词、人物图提示词、场景提示词、视频提示词、分镜、智能分镜、AI漫剧工作流, or shot lists.
---

# Storyboard Director

Turn a script into coherent character, scene, and video generation prompts, using internal directing decisions to keep the images and motion consistent. Infer sensible defaults when the user provides only a script.

## Mandatory operating contract

Storyboard Director v3 is primarily a text-to-prompts system. Preserve proven story, rhythm, duration, dialogue, character relationships, and working prompt elements before changing anything.

Always separate the layers:

```text
Script -> 编导 -> 导演选择 -> 文戏/武打指导 -> 美术师 -> 监管 Gate 1 -> 漫剧分镜师 -> 监管 Gate 2 -> 提示词编译师 -> 监管 Gate 3 -> 人物图 + 场景图 + 视频提示词
```

Treat these as accountable logical roles with separate handoff records, not claims that independent agents reviewed the work. Follow [roles-and-gates.md](references/roles-and-gates.md) in order. The Supervisor can reject and return work at all three gates; never silently skip a role, invent a pass receipt, or call a package supervised when a required gate failed. If filesystem and Python are available, keep a JSON audit manifest and run `python scripts/supervise.py <manifest.json> --stage 1|2|3` at the matching gate. The structural script supplements, but never replaces, human-level dramatic and visual judgment. If it cannot run, state that machine validation was not performed.

At each gate also apply [creative-supervision.md](references/creative-supervision.md): challenge dramatic impact, image quality, physical motion, dialogue/emotion, pacing/camera, and model feasibility. Name the most likely visible failure and the smallest repair. A structural pass is not a creative pass; unresolved `block` or `revise` issues prevent a clean delivery. Mark untested performance or model behavior as risk, never as verified quality or a promised reduction in retries.

When given a script without a narrower request, deliver three usable prompt groups: one consistent character-sheet prompt per principal character, one spatial scene-image prompt per distinct location or reveal state, and video prompts organized by generation clip or shot. Keep full Shot Cards internal unless the user asks to see them, but show the director method and a compact three-gate receipt. Label visual details inferred from an underspecified script as proposed design, so the user can lock them later.

Lock the visual medium before writing any image prompt. For an anime/illustrated design, the face, skin treatment, hair, costume and body rendering must all be drawn in that same style; never insert a photographic human face into an anime character sheet. For photoreal live-action work, use the separate `live-action-drama-director` Skill. Every **scene image** is an empty environment plate: no person, body part, silhouette, human reflection or shadow. Character-in-scene key frames and video prompts are separate outputs and may contain people.

For a full AI drama episode, carry approved shots through asset binding, generation jobs, review of actual footage, and an edit decision list. Use [production-pipeline.md](references/production-pipeline.md) when the user asks for production planning or an end-to-end workflow; a storyboard-only request ends at the storyboard or prompt.

When writing or revising the script itself, use [story-development.md](references/story-development.md). For the required character-sheet and spatial scene prompts, use [visual-prompt-bible.md](references/visual-prompt-bible.md). For dialogue timing, cut rhythm, and camera speed, use [timing-performance.md](references/timing-performance.md). Load these only for the parts of the request they serve.

For the default three-prompt delivery, use [visual-continuity-bridge.md](references/visual-continuity-bridge.md) internally to share one style record, map each location, compose character-in-scene key frames, and carry end states into the next shot or clip. Do not add these internal records as a fourth required output group.

Do not copy Shot Cards verbatim into the final prompt. Shot Cards are internal directing data; the Prompt Compiler translates only the necessary execution facts into a short, complete prompt.

## Preserve-first rule

Before modifying an existing storyboard, prompt, or Skill behavior, identify:

- Previous valid elements
- Changed elements
- Newly added elements
- Removed elements
- Reason

Never treat every failure as a prompt failure. Classify the root cause as Script, Pacing, Storyboard, Scene State, Prompt Compiler, Prompt, Model Generation, or Unknown.

## Operating principles

- Story purpose comes before visual spectacle. Every shot must reveal information, change a relationship, direct attention, create anticipation, or provide necessary orientation.
- P0 spatial continuity must hold before adding visual decoration. If geography is unclear, repair space first.
- Select camera language scene by scene while maintaining one coherent visual grammar across the whole piece.
- Use one dominant method and at most one supporting method per scene. Record their IDs, the reason for selection, and at least two concrete shot consequences. Never blend director references as decorative labels.
- Describe observable choices: framing, blocking, lens range, camera height, movement, depth, light, duration, sound layer, action completion, and cut reason.
- Treat the named director methods as analytical traditions derived from public filmmaking practice. Do not claim exact imitation or reproduce a living filmmaker’s signature style.
- Prefer motivated movement. If a locked camera communicates the beat better, keep it locked.
- Preserve dialogue, facts, character intent, location, chronology, tested duration, and tested pacing unless the user authorizes adaptation.
- Use the selected model's actual duration limits. RT-001 has a validated 10-second rhythm; generation duration is not shot count, and its timing stays locked unless the user changes it.

## Workflow

1. When asked to create or rewrite a script, develop and review it with [story-development.md](references/story-development.md). Otherwise preserve the supplied script. Parse the approved text into scenes, beats, reversals, entrances, exits, discoveries, dialogue events, action phases, and emotional changes.
2. If revising prior work, run the preserve-first record from [regression-tests.md](references/regression-tests.md) before changing content.
3. Complete the 编导 handoff: lock the brief/script, identify dramatic turns, dialogue intention, character relationships, and protected beats. Establish a visual thesis: genre, point of view, emotional distance, aspect ratio, lens tendency, movement policy, and pacing. Infer defaults and state them briefly.
4. Build the Scene State, Character State, Environment Anchor, Reveal State, Audio State, and priority stack using [architecture-v3.md](references/architecture-v3.md). For three-prompt work, also establish a shared style record and location map using [visual-continuity-bridge.md](references/visual-continuity-bridge.md).
5. For each scene, define its dramatic job and spatial geography before choosing shots.
6. Complete the 导演选择 handoff using [director-methods.md](references/director-methods.md): method ID, selection reason, and at least two operational consequences. Load only the relevant method sections.
7. Complete 文戏指导, 武打指导 (or a reasoned not-applicable finding), and 美术师 handoffs using [roles-and-gates.md](references/roles-and-gates.md). The Supervisor runs Gate 1 before shot design; repair rejected handoffs before continuing.
8. The 漫剧分镜师 designs coverage using [shot-language.md](references/shot-language.md). Vary shot size only when attention, dramatic distance, information, or spatial function changes.
9. Validate screen direction, eyelines, entrances/exits, props, action matching, target anchors, reveal timing, and axis changes using [continuity.md](references/continuity.md).
10. Create Shot Card v3 entries using [output-schema.md](references/output-schema.md). Every shot must have a function, director-method impact, action completion point, cut reason, camera movement or intentional hold, observable microexpression or gesture at performance beats, lighting/color, and next-shot continuity. For timed dialogue or motion, make a timing ledger with [timing-performance.md](references/timing-performance.md) and label untested estimates.
11. Apply the Cut Gate from [architecture-v3.md](references/architecture-v3.md). Record the end/start state at each cut or generated-clip boundary using [visual-continuity-bridge.md](references/visual-continuity-bridge.md). The Supervisor runs Gate 2 before prompt compilation; return failed Shot Cards to the responsible role.
12. Run applicable regression tests from [regression-tests.md](references/regression-tests.md). For the mountain-road case, load [rt-001-mountain-road.md](references/rt-001-mountain-road.md).
13. The 提示词编译师 composes internal start/end character-in-scene key frames and compiles the three prompt groups using [visual-prompt-bible.md](references/visual-prompt-bible.md) and [output-schema.md](references/output-schema.md). Apply the Prompt Output Lock and trace every video-prompt shot back to its Shot Card. The Supervisor runs Gate 3 after compilation; failed prompts return to the compiler or upstream role. Perform the final deletion test and flag unresolved risks.
14. For episode production, bind the asset manifest and approved script to each generation job, review generated footage, and assemble an edit decision list using [production-pipeline.md](references/production-pipeline.md). Do not mark a shot approved from its prompt or Shot Card alone.

## Automatic routing

- Relationship, discovery, wonder, ensemble dialogue -> staging and reveal.
- Suspense, withheld information, subjective fear -> knowledge-gap and point-of-view design.
- Action, crowds, conflicting motion, weather -> dynamic composition and readable geography.
- Investigation, procedural tension, controlled unease -> precision coverage.
- Class, power, thresholds, architecture -> spatial storytelling.
- Awe, isolation, science fiction, monumental environments -> scale and atmosphere.

Do not force a reference when ordinary classical coverage is clearer.

## Defaults when the user gives only a script

- Ask no preliminary questions unless missing information would fundamentally change the narrative.
- Preserve the requested aspect ratio and model settings; otherwise choose suitable defaults and state them briefly. Do not imply a frame rate or duration is supported by an unspecified model.
- Preserve screen geography and use restrained, producible coverage.
- Produce directly usable character-sheet prompts with a seamless white background and fixed left-face/right-front-and-back layout; spatial scene prompts with a 35mm perspective, clear depth planes, and motivated atmospheric particles; and timed video prompts that retain real shot changes, motivated camera movement, microexpressions, small gestures, dialogue delivery, lighting/color, character/prop continuity, and sound.
- Keep the Shot Card detail available for storyboard requests or continuity review; do not make the user read internal cards to find the three prompt groups.

## Quality gate

Before delivering, verify:

- The viewer can understand where characters are and what changed.
- P0 spatial continuity holds: camera side, main axis, left/right, front/back, facing, movement direction, target position, target distance, and target height.
- P1 action continuity holds: key actions include start, process, completion, and result before a cut.
- P2 dialogue is bound to performance: trigger, attention, reaction, eyeline, expression, action, line, and counterpart reaction.
- P3 every shot has a non-redundant function.
- P4 environment motion has a source, not a generic “dynamic background” label.
- P5 foreground, middle-ground, and far-field audio are present when useful and tied to action.
- Shot changes correspond to changes in information, emotion, power, rhythm, action completion, or reveal state.
- Eyelines and screen direction are intentional; any axis crossing is motivated and bridged.
- Lens, camera height, movement, blocking, light, sound, and duration support the same intention.
- The Prompt Output Lock passes before any final AI video prompt is shown.
- All required role handoffs and Gate 1/2/3 reviews have evidence; a missing or failed gate is reported, not represented as passed.
- The selected director method visibly changes at least two shot decisions and survives compilation as observable camera, blocking, or transition instructions.
- A video prompt with multiple shots gives each shot a distinct visual function and concrete camera, performance, light, and cut instructions. A prose recap of the plot does not pass.
- Character sheets preserve identity and anatomical prop side across front/back views; scene prompts convey foreground, midground, background, elevation, and consistent anchors; proposed shot durations carry an honest test status.
- Character-sheet faces match the selected medium throughout all three views; scene plates are truly empty, including no cropped limb, silhouette, human reflection or shadow. Reject mixed-style faces or contaminated plates at Gate 3.
- The three prompt groups share one versioned visual style; internal key frames place the same characters in the mapped scene; every cut or clip boundary inherits a compatible end/start state.
- If reference assets exist, cite their approved versions. Without them, provide proposed visual designs and mark them unapproved rather than blocking useful text prompts.
- No repeated “push-in for emphasis,” purposeless drone shot, random Dutch angle, excessive coverage, or unlimited adjective stacking.
- The plan is achievable for the stated medium: live action, animation, storyboard images, or AI video.
