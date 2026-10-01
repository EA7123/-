# Live-action role handoffs and creative supervision

The roles below are separate responsibilities, not proof of separate reviewers. The Supervisor has authority to return work at each gate. Keep an issue record with shot/prompt ID, observed design evidence, likely visible failure, owner, smallest repair, and recheck status. Status is `block`, `revise`, or `watch`: block for contradictions or measured impossibility; revise for credible quality/generation risk; watch for untested behavior that cannot be decided from text. Never describe a watch item as verified.

| Role | Handoff required before review |
|---|---|
| 编导 | Locked beats/dialogue, objective, turn, causality, duration evidence, protected reveal |
| 导演选择 | Dominant method ID, optional supporting ID, reason and two shot-level consequences |
| 文戏指导 | Stimulus, attention, microexpression, gesture, speech delivery, listener reaction and breath/overlap plan per dialogue beat |
| 武打指导 | Body/prop positions, grip, force path, contact, footing, recovery and safe cut; or justified not applicable |
| 美术/摄影 | One proposed or approved casting/wardrobe/style record, physical location map, motivated light and palette, atmosphere source |
| 真人分镜师 | Timed, executable Shot Cards with function, method impact, axis, blocking, camera, performance, light, audio, action result and cut inheritance |
| 提示词编译 | Three copy-ready groups, each video shot traced to the card and same identity/location/style record |

## Gate 1: before shot design

Check the story's causal turn and what emotion the audience should infer from behavior rather than an adjective. Challenge whether casting, wardrobe, props, geography, light and atmosphere support the same world. Check whether action and dialogue can be attempted in the proposed time without a superhuman performance. Return missing or contradictory choices to the responsible role; do not let the storyboard invent an absent drama/action/art decision.

## Gate 2: before compilation

For every shot, ask: What does the eye find first? What changes by the end? Could an actor physically do it on this terrain, with this grip and camera path? Can the viewer locate both people? Does a close shot hide the decisive contact? Is the speaker listening and being answered, not just reciting? Do light direction, wardrobe, moisture, prop side and screen movement survive each cut? Is a camera move motivated and settled? Does the shot have enough time for orientation, line, breath, action, reaction and reveal? If only text exists, time is estimated. A natural-speed table read or scratch performance is the first timing evidence; an animatic tests action and reveal readability.

## Gate 3: after compilation

Compare each video section with its Shot Card and the character/scene plates. Reject any scene prompt/image containing an actor, extra, cropped human part, silhouette, reflection or shadow; reject any character sheet that mixes photoreal and anime/cartoon rendering across its left face and right full-body views. Verify exact locked lines, identity and costume, anatomical prop side, camera side, action start/contact/result, eyeline, microexpression, light/color, sound, and cut continuity. Predict the highest-risk visual artifact, not merely a missing keyword: identity drift, porcelain skin, extra fingers, sliding feet, weightless pull, flat set, light flip, premature reveal, rushed speech or mismatched lips. Repair the causal source, reference binding, shot design or prompt in that order; more adjective layers are not a repair. Inspect actual images before claiming image-level compliance.

## Generation-risk triage

Count simultaneous burdens in a proposed model job: multiple identified people, hands/contact, large body travel, moving camera, exact dialogue/lip sync, weather effects, hidden-to-visible reveal and multiple internal cuts. Use the **selected model's verified** capabilities and actual approved assets; if unknown, mark them unverified. Reduce only redundant burden: hold the camera for complex contact, keep the key action in one readable frame, use consistent first/last state references where supported, or propose separate generation and edit/audio passes. Do not silently drop locked dialogue, a required action, total rhythm or reveal. Before any retry on real output, inspect the failed frame/timecode, change one dominant variable, retain accepted work, and stop after two inconclusive repair cycles to ask for a tradeoff. Never spend credits or invoke external generation without authorization.

## Receipt

Keep the final note short: method and two visible consequences; Gate 1/2/3 design status; highest `watch` risk and needed evidence; actual read/animatic/frame/take status. A text-only package may be design-reviewed but is not footage-approved, "S grade," or a proven low-retry prompt.
