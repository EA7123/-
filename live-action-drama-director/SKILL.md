---
name: live-action-drama-director
description: Convert a script into film-grade photoreal live-action AI drama character-sheet, scene, and shot-by-shot video prompts. Use for 真人写实漫剧、电影级真人短剧、真人角色提示词、真人场景提示词、真人视频分镜 or live-action AI drama. Preserve real human performance, continuity, dialogue, and generation feasibility.
---

# Live-Action Drama Director

Turn an approved script into three copy-ready groups: photoreal human character sheets, physical location plates, and timed live-action video prompts. This is a distinct medium from animation: real human anatomy, weight, skin, fabric, optics, light, sound, and acting must remain credible. Do not convert an unspecified script into animation or assume photorealism can be obtained by adding "cinematic, 8K" adjectives.

Keep a strict photoreal medium lock: all three views of a character sheet must be the same plausible human, with no anime/cartoon face or body. Every scene image is an **empty location plate** with no actor, extra, body part, silhouette, human reflection or shadow. Actor-in-location key frames and video prompts are separate deliverables and may contain people.

## Operating contract

```text
Locked script -> 编导 -> 导演选择 -> 文戏/武打指导 -> 美术/摄影 -> 监管 Gate 1
-> 真人分镜师 -> 监管 Gate 2 -> 提示词编译 -> 监管 Gate 3
-> 人物图 + 场景图 + 视频提示词 + compact risk receipt
```

These are accountable logical roles in one Skill, not a claim that independent people or models worked. Follow [supervision.md](references/supervision.md) for handoffs, rejection and recheck. A structural checklist does not establish artistic quality. Never invent a pass, tested timing, approved asset, model capability, or generated-footage QC.

When the user supplies only a script, proceed with clearly labeled proposed casting, wardrobe, location, aspect ratio, and look. Preserve original dialogue, causal beat order, character intent, positions, prop ownership, reveal, and any user-validated total rhythm. Ask only when a missing fact would change the story or an identity/reference choice cannot be inferred safely. Never imply that a real actor, celebrity likeness, or location was supplied when it was not.

## Workflow

1. 编导 locks source facts and maps each scene's objective, conflict, turn, emotional change, exact spoken lines, action phases, tested versus estimated duration, and reveal rule. Record protected elements before revising existing work.
2. 导演选择 chooses one dominant and at most one supporting method from [director-methods.md](references/director-methods.md), with a reason and at least two observable shot consequences. Use those methods as analytical staging frameworks, not exact imitation presets.
3. 文戏指导 maps stimulus -> attention -> microexpression/gesture -> line delivery -> listener reaction. 武打指导 maps start position -> force/contact -> weight transfer -> recovery for physical exchanges, or records why not applicable. 美术/摄影 establishes a single style ID, casting/wardrobe/prop design, location map, lens tendency, motivated light, color separation, and practical atmosphere using [live-action-bible.md](references/live-action-bible.md).
4. 监管 Gate 1 challenges causal drama, acting intention, physical feasibility, and look coherence before shots are made. Resolve blocking findings before advancing.
5. 真人分镜师 creates timed Shot Cards. Each has a dramatic function, selected-method impact, shot size/lens band, camera side/height/angle, movement trigger/path/stop or deliberate hold, blocking, hand/prop state, observable performance, light/color, sound, action completion, cut reason, and compatible next-shot state. Use [timing-performance.md](references/timing-performance.md) for dialogue and motion windows. Internal cut points stay estimated without a read or animatic.
6. 监管 Gate 2 reviews each shot for spatial legibility, actor behavior, weight/contact, visual hierarchy, pacing, lighting continuity, and whether the planned model job is overloaded. A proposed ten-second clip is not proof that a model can execute multiple internal cuts and synchronized dialogue.
7. 提示词编译 produces the three groups from one style/location/identity record. Character prompts use a white-background composite: left frontal extreme face close-up; right matching full-body front and back. Scene prompts use a 35mm spatial plate by default, with foreground, playable midground, background, physically sourced atmosphere, and a stable location map. Video prompts translate each Shot Card into concise executable shots with exact dialogue and motivated camera, light, sound and transition. Do not paste rule lists into the prompt.
8. 监管 Gate 3 compares every final prompt to its Shot Card and predicts the likely visible artifact: plastic skin, identity drift, extra fingers, floating contact, lips out of sync, flat set, inconsistent light, or impossible cut. Repair the smallest responsible upstream decision; report unresolved risk. Deliver a compact gate receipt that separates design review, structural checks, timed tests, and generated-footage QC.

## Output lock

- Character prompts are individually copy-ready, one stable identity per principal character; left face and right front/back use the same adult human anatomy, wardrobe and prop side. Do not use cartoon, anime, doll-like, porcelain, or beauty-filter faces for a photoreal request.
- Scene prompts are empty physical, navigable places, not atmospheric wallpaper: no complete or partial human, silhouette, reflection or shadow. Fix entrances, exits, height, target position, camera axis, natural or practical light sources, surface condition, and foreground/midground/background readability.
- Video prompts have real shot changes. Each shot shows who moves, where, under what force, what the face and hands do, how the camera moves or holds, which exact line is spoken and by whom, how light/sound behave, and what completed state permits the cut.
- Lens/focus, motion blur, skin/fabric detail, light falloff and atmosphere must agree with the stated photographic approach. Avoid mutually incompatible lens or camera commands and avoid excessive texture adjectives.
- Respect the selected generator's verified duration, references, audio and editing abilities. If unknown, label those as unverified; propose a fallback such as separate dialogue/audio or clip assembly without silently changing locked story timing.
- No "S-grade" or lower-retry-rate claim follows from text alone. A read, animatic, generated frame and reviewed take each support different levels of confidence.
- At Gate 3, reject mixed cartoon/photoreal character design or a contaminated scene plate. If images are generated, inspect the actual pixels before claiming those constraints passed; a text prompt alone is not visual proof.
