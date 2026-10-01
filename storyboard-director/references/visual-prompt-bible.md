# Character, prop, and scene image prompts

This Skill normally outputs text prompts from a script. It can work before any reference images exist. Distinguish script facts from proposed visual design; once the user approves a generated image, give it a versioned asset ID and reuse that identity in later prompts. `production-pipeline.md` applies only when the user asks to manage actual generation or editing.

Use the shared style record, location map, composite key frames, and boundary ledger in `visual-continuity-bridge.md` to keep the three prompt groups aligned.

Before prompting, record `medium` and `style_id` for the entire character-sheet set. If `medium=anime/illustrated`, draw the face, eyes, nose, mouth, skin shading, hair and body in one coherent illustrated language; do not use a photographic face, skin pores, photo-real portrait crop, or face-swap look inside an anime sheet. If the user requests photoreal humans, route to the live-action Skill instead of mixing media. This style lock applies to the left face and both right-side full-body views, and to their later video appearances.

## Character design from a script

For each principal character, extract script-supported age range, role, silhouette cues, costume, carried objects, and emotional baseline. If appearance is unspecified, make one coherent visual proposal that fits the genre and mark those traits `proposed`, not canonical. Avoid claiming a face, ethnicity, period, or costume was in the source when it was inferred. Keep the same proposed traits and `style_id` across every shot and view until the user changes them.

Character state fields for prompt compilation:

```text
character_id / design_version / approval: proposed | approved
identity: face, hair, body silhouette, distinctive marks
costume_id: clothing, footwear, accessories
prop_ids: canonical design and attachment side or hand
scene state: position, facing, motion, action phase, eyeline, emotion
```

## Fixed character-sheet composition

Use one composite canvas per character. The layout is a production constraint, not a suggestion:

- Entire canvas: pure seamless white background, neutral soft studio lighting, clean contact shadows only, no scene, gradients, text, borders, extra characters, duplicated limbs, or cropped feet in the full-body views.
- Left region, roughly 45% of the canvas: straight-on extreme close-up of the face, from forehead to chin or upper neck, looking toward camera. Facial structure, eyes, style-appropriate skin treatment, hairline, and defining marks are readable. This region identifies the character and must match the rendering of both full-body views.
- Right region, roughly 55%: two equal full-body views side by side, front view on the inner right panel and back view on the outer right panel, both standing upright at the same scale and ground line. Neutral pose keeps costume silhouette, footwear, and accessories visible. The front and back must be recognizably the same person as the left portrait.
- Keep one outfit and one prop design across the three views. If a prop belongs in the character sheet, fix the anatomical hand or attachment point, grip, orientation relative to the body, and visible wear. A front-to-back camera reversal may change which screen side the prop appears on; the anatomical side and physical orientation must remain consistent.
- Output a separate sheet or explicit version when outfit or carried-prop configuration changes materially. Do not cram multiple costumes into one identity sheet.

Copy-ready prompt structure:

```text
Create one clean character reference sheet for [character_id, proposed/approved design].
Medium/style_id: [one locked anime/illustrated rendering system; no photographic face].
Identity: [stable face, hair, age range, silhouette, distinctive features].
Costume: [one outfit, materials, colors, footwear, accessories].
Prop: [prop_id, design, anatomical hand/attachment, orientation relative to body; omit if none].
Single canvas, seamless pure white studio background, soft even light.
LEFT ~45%: frontal extreme close-up face casting portrait, eyes facing camera,
face unobscured, detailed and recognizably identical to the full-body views.
RIGHT ~55%: two adjacent full-body views at identical scale and ground line:
front view then back view, neutral standing pose, complete head-to-toe visibility.
Match identity, outfit, body proportions, and prop attachment across all three views.
Render face, skin, hair and body consistently in the locked illustrated style;
no photoreal human face or mixed photographic facial texture.
No environment, typography, panel borders, additional poses, or extra people.
Aspect ratio: [sufficiently wide for the three-view layout; model-supported value].
```

If the model cannot render three coherent views on one canvas, generate an approved face plate and matching front/back plates separately, then assemble the same layout. Record that as a generation workaround, not a different delivery design.

## Prop and position continuity

Track important props separately from appearance. A prop follows its owner through movement until an explicit event changes ownership, hand, orientation, or placement. Track the body's movement and the prop's movement together:

```text
shot_id / character_id / position and facing / prop_id
attachment: right hand | left hand | belt | back | ground | other
orientation: tip/face/handle direction relative to body and travel
event: drawn | gripped | passed | dropped | placed | retrieved | none
resulting owner, attachment, orientation, and position
```

For example, if a character holds a staff in the right hand while walking uphill, later side and back views keep it in the right hand and advancing with that character. A screen-side flip caused by a camera reversal is not a hand switch. If the character passes the staff to another person, show the transfer and update both character and prop states before the next prompt. Apply the same event-based rule to character front/back, left/right, height, distance, and motion direction.

## Spatial scene prompt

Make a separate **empty environment plate** for each distinct location or reveal state. It contains no people, body parts, silhouettes, human reflections or human shadows, even when the script places characters there. Derive camera positions and fixed landmarks from the location map in `visual-continuity-bridge.md`. The default visual language is a 35mm perspective at a stated camera height, unless the script or user specifies another lens. A scene plate should reveal depth and three-dimensional geography rather than flattening the background. Keep an unobstructed action zone where characters can be composited later:

```text
location_id / design_version / approval: proposed | approved
camera position, height, direction, and side of the action axis
foreground: near objects and readable scale cue
midground: playable character path or action zone
background: distant architecture, terrain, or destination
elevation and landmark order; entrance, exit, and target anchor
time, weather, light direction, palette, and material state
atmospheric source and effect; reveal target visibility
```

Use foreground occlusion, receding lines, overlapping forms, scale falloff, and controlled focus separation. The midground action zone and important background anchor must remain readable; do not blur away the place the viewer needs to understand. Add fine airborne dust or particles only when a believable source and light reveal them, such as a dry room, sunbeam, disturbed floor, or windy path. For rain-wet settings, use mist, spray, droplets, or moisture in the air instead of dry dust. Avoid decorative haze that hides geography.

Copy-ready prompt structure:

```text
Create a scene reference image for [location_id, proposed/approved design].
Empty environment plate only; no characters, extras, body parts, silhouettes,
human reflections or human shadows, including at frame edges and in windows.
35mm lens perspective, camera [height/position] facing [direction] from [axis side].
Foreground: [near depth cue]. Midground: [clear playable path/action zone].
Background: [landmark and fixed target at stated distance/elevation].
Preserve [landmark order, terrain direction, entrances/exits, target anchor].
Light from [direction], [time/weather], material detail [surfaces].
Atmosphere: [physical source -> fine dust/mist/droplets visible in light],
subtle enough to preserve depth and landmark readability.
Reveal target: [Hidden | Partial | Visible | Full] at this beat, using
camera placement or occlusion consistent with the same map.
Only environment and scene props; no human presence. Character-in-scene
composites belong in a separate key-frame or video prompt, never this plate.
Aspect ratio: [script/user/model choice].
```

For a hidden target, do not put the object in the visible image while also saying it is hidden. Keep its location in the internal scene map; use an occluding ridge, building, or camera direction that hides it. A later reveal plate returns to the same mapped target position.

## Composite key frames and video prompt handoff

Combine `style_id + character_id + outfit_id + prop_id + location_id + map_version + shot_id` with the shot's action, formation, eyeline, and reveal state. The character sheet supplies identity; the scene plate supplies spatial design; the Shot Card supplies the change over time. Use the internal start/end key-frame and boundary records from `visual-continuity-bridge.md` to check this combination. In the final video prompt, include only facts the model needs to execute the clip, including any prop transfer or formation change. Keep reference handles and versions when actual images exist; without images, the three prompt groups are valid proposed designs, not proven consistent assets.

If a target model imposes reference count, first/last-frame, or aspect-ratio constraints, adapt the *binding* of references to that model and record the choice. Do not quietly remove a locked face, prop state, character relation, or scene anchor to fit a model setting.

## Prompt review

- Character sheet has the exact left face / right front and back layout on pure white and one coherent identity.
- Full-body views show complete feet, the same outfit, and a physically consistent prop attachment and orientation.
- Scene plate uses 35mm by default, with foreground, midground, background, readable geography, motivated atmosphere, and a fixed target anchor.
- Inspect generated plates when available: reject any person or human fragment/reflection/shadow. Inspect character sheets for one consistent medium across the close face and both full-body views; an anime sheet with a photographic face fails even if the layout is correct. Text-only checks are design review, not proof of image compliance.
- Character positions and props change only after named events; reveal state is separate from target position.
- Script facts and proposed visual details are clearly distinguished.
- When images are actually generated, compare identity, props, depth, and anchors in those images; text review alone cannot certify visual consistency.
