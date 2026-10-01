# Photoreal live-action prompt bible

Use one `style_id`, character IDs, wardrobe IDs, prop IDs, location map, and shot IDs across all three prompt groups. Mark visual choices inferred from an underspecified script `proposed`; call them `approved` only after the user approves actual references. Use adult casting by default only when consistent with the source; never alter a stated age.

Lock `medium=photoreal_live_action`. The left face and both full-body views must have the same real-human anatomy and photographic rendering; no anime eyes, illustrated facial planes, toon shading, or pasted cartoon face. This is a style-consistency requirement across all three prompt groups, not an invitation to over-retouch skin.

## Human casting sheet

For each character, define stable facial structure, skin tone and real texture, hairline/style, height and build, posture, wardrobe materials and wear, footwear, and any distinguishing mark. Describe identity with a few concrete features, not a list of beauty adjectives. Keep complexion and facial structure stable across close-up, front and back; avoid airbrushed skin, identical faces, implausible symmetry, waxy shine, extra fingers, and inconsistent hairlines. If a reference is supplied, follow it rather than inventing a new face. Do not imply a real person's likeness unless provided and authorized.

Copy-ready layout contract:

```text
One photoreal live-action casting reference sheet, [character ID], [proposed/approved].
Identity: [stable facial structure, hair, skin detail, build, age per script].
Wardrobe: [single outfit, fabric, color, fit, footwear, wear].
Prop: [owner, anatomical hand/attachment, orientation; omit if none].
One wide canvas, seamless pure white studio background, neutral soft light,
only natural contact shadows; no location, text, borders, or additional poses.
LEFT ~45%: straight-on extreme face close-up from forehead to chin/upper neck,
unobscured eyes, lifelike pores and skin variation, neutral casting expression.
RIGHT ~55%: two matching head-to-toe full-body views, front then back,
same scale, ground line, anatomical proportions, outfit and prop attachment.
Same adult human identity across all three views, no retouched or stylized face.
No anime/cartoon facial features or illustrated body rendering in any view.
```

Keep a distinct expression/performance reference from the neutral identity sheet when a scene needs tears, anger, blood, rain, dirt, or changed wardrobe. Do not bake a temporary emotion or environmental effect into the identity anchor. Prop ownership and anatomical side change only through an explicit event shown or specified between shots.

## Physical location plate

Every location plate is an **empty set image**. No actor or extra, cropped body part, silhouette, face in a window, human reflection in glass/water, or human shadow. Do not depict a hand or foot merely to suggest scale. Keep the action zone clear for later compositing. Default to a 35mm perspective at a specified human camera height, adjusted only when the scene's purpose requires another lens. Identify entrance, exit, action zone, camera side of the main axis, foreground scale cue, playable midground, background anchor, terrain height, and destination/reveal position. Use motivated light: sun direction and cloud cover, window, practical lamp, reflected bounce, or explicitly placed film light. Keep exposure and color separation plausible across reverse angles. Atmosphere has a source: dust from a dry disturbed surface, mist after rain, breath in cold air, spray from water, or smoke from a visible emitter. Do not use dry dust in a rain-soaked scene or haze that hides essential geography.

Copy-ready plate contract:

```text
Photoreal live-action location plate, [location ID], [proposed/approved].
Empty set only: no people, body parts, silhouettes, human reflections or shadows,
including frame edges, doorways, windows, mirrors and water surfaces.
35mm camera at [height], [side] of the action axis, facing [direction].
Foreground [physical scale/depth cue]; midground [walkable actor path/action zone];
background [fixed landmark/target and elevation].
Material and weather [state]; light source from [direction], natural falloff and bounce;
palette [two or three functional color relationships, not one flat tint].
Air [physical source and restrained effect]. Preserve readable depth and safe footing.
Target visibility [hidden/partial/visible], consistent with the same map.
Only architecture, terrain and scene props; no cast of any kind, floating props,
impossible architecture, or decorative fog.
```

For hidden/revealed states, write two plates from one map. The target must be spatially fixed even when occluded; a reveal should arise from camera position, character movement, opening, or clearing atmosphere, not relocation.
An actor-in-location composite is a separate key frame or video prompt, never an empty plate. When actual images exist, inspect character-sheet style consistency and the entire scene frame for human fragments or reflections before approval.

## Moving-image prompt

Compile the approved Shot Cards into numbered, timed shot sections. Every section states: dramatic function; subject start position/facing and end state; shot size/lens/camera side; movement trigger, path, relative speed and stop or intentional hold; physical action in causal order; visible performance, eyeline and exact dialogue; key/fill or available-light direction and color; foreground/mid/far sound where useful; cut reason and inherited state. A prompt should be shorter than the cards, but not lose execution-critical facts.

For contact, show stance and grip before force, the moved body's weight and foot placement, then recovery. For dialogue, leave space for breath, listening and overlapping line tails; do not force a speaking face in every frame. If the selected model does not reliably produce precise lip sync or sound, keep the visual performance and timing markers, and plan separately authorized audio/post work. Timecodes are design estimates until a read, animatic, or take is reviewed. One prompt can describe multiple internal shots only if the model/job can plausibly follow them; a single generation invocation and a final edited sequence are not the same thing.

Use photographic detail purposefully: real skin texture, fabric weave where visible, plausible depth of field, exposure roll-off, restrained motion blur, and consistent focal transitions. Avoid "8K masterpiece cinematic" stacks, fake lens metadata, excessive grain, constant slow motion, and contradictory directions such as simultaneous locked-off and tracking camera.
