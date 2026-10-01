# Visual continuity bridge

Use this internal bridge when compiling character, scene, and video prompts from the same script. It does not add a fourth required user-facing prompt group. Its records keep visual style, geography, composite key frames, and clip boundaries aligned. Work with proposed text designs when no images exist; actual visual consistency requires reviewing generated images or footage.

## 1. Shared visual style record

Create one `style_id` per coherent visual treatment. Reuse its version across every character sheet, scene plate, composite key frame, and video prompt. Record only visible decisions that help the chosen model; avoid decorative adjective lists.

```text
style_id / version / status: proposed | approved
rendering medium: 2D illustration | 3D animation | live-action look | other
character proportions and face treatment:
linework or surface/material treatment:
palette and contrast range:
lighting logic and shadow softness:
texture/grain and atmospheric treatment:
motion/rendering treatment for video:
locked visual motifs and allowed scene-specific variation:
source: script fact | user art direction | proposed inference
```

Apply identity and rendering style to the pure-white character sheet, but keep its light neutral so facial and costume details are inspectable. For anime/illustrated work, the left face and right full-body views must share drawn facial and body rendering; never merge a photographic human face into an illustrated sheet. Apply the same rendering language to the 35mm **empty** scene plate while allowing scene-specific weather and light. The scene plate contains no person, body part, silhouette, human reflection or shadow. Only the separate composite key frame combines the character and environment without changing face proportions, costume material, palette, or landmark design. The video prompt states the compact style signature once per clip or sequence. If the user supplies a style reference, it overrides a proposed style. A style record can be replaced deliberately; version the change and recheck all three prompt groups.

## 2. Scene map

For each location, sketch or state a small coordinate map before writing alternate scene views. Text coordinates are enough when no image exists. Pick an axis that follows the main travel or interaction direction:

```text
location_id / map_version
origin and main axis: positive u points toward [destination]
v: left/right when facing positive u; h: elevation
entry / exit / path / obstacles / foreground occluders
landmark_id -> u, v, h or ordered near/mid/far relation
character_id -> starting u, v, h, facing, travel direction
camera_id -> u, v, h, looking direction, side of main axis
reveal_target_id -> fixed u, v, h; visibility timeline separately
```

Use relative or ordinal positions when precise measurements are unsupported; do not invent meter values. A 35mm lens describes perspective, not where the camera stands. Derive the scene plate's foreground/midground/background and all later camera views from this map. When a camera crosses the main axis, show or state the event that reorients the viewer. A hidden target remains fixed on the map and is concealed by a plausible camera direction or occluder, not teleported when revealed.

## 3. Character-in-scene key frames

Before compiling each generated clip, prepare an internal start and end key-frame specification from `style_id + character_id + outfit_id + prop_id + location_id + map_version + shot_id`. Add a middle key frame only for a critical contact, transfer, turn, or reveal that cannot be inferred safely from the endpoints.

```text
keyframe_id / clip_id / start | critical | end
style_id and approved/proposed status
character identity and outfit versions
camera/map position, view direction, lens band, framing
character formation, facing, eyelines, pose and action phase
prop owner, anatomical hand/attachment, orientation, map position
visible landmarks, foreground/midground/background
target position and reveal state
light, weather, atmosphere; exact story beat
```

The key-frame prompt is a composite image instruction: show the same character design *inside* the mapped scene, at the specified camera view and action state. It is distinct from the white-background identity sheet and the empty environment plate; never insert the actor into the environment plate itself. Keep only key frames that establish a start/end state or a difficult change; do not produce a still for every minor movement. If images are generated, bind the resulting reference files to the video job. If not, use these specifications to ensure the text video prompt agrees with the character and scene prompts; do not claim image-to-video conditioning occurred.

## 4. Shot and clip boundary ledger

Record a boundary state at each planned cut and at the start/end of each generation clip. A cut within one generated clip and a boundary between two model jobs are different; both need state continuity, but only the latter can bind a real last frame as the next job's first-frame reference when supported.

```text
boundary_id / preceding shot or clip / following shot or clip
time and timing status: estimated | tested
preceding end keyframe_id / following start keyframe_id
character positions, facing, movement vectors, action phases, eyelines
prop owners, hands/attachments, orientations, positions
camera side, look direction, framing and motion end/start
fixed landmarks, light/weather, reveal state
dialogue and ambience crossing the boundary
change event or match rule; unresolved mismatch
```

At a straight continuity cut, the next start state inherits the prior result. A new camera angle may change screen placement while character/map positions and anatomical prop sides remain stable. A new location or time requires an explicit transition. For a cut on action, both sides share a compatible action phase. If a take's actual last frame differs from the planned state, update the next prompt or reject the take after review; do not preserve a fiction that the written plan matched the footage.

When the selected model supports first/last frames, map compatible key-frame assets to those inputs. Check the model's current controls before promising simultaneous camera, motion, style, and frame references; some combinations are unavailable. When unsupported, pass the essential start/end facts in text and mark the handoff as unverified until footage review.

## Compilation and review gate

The three final prompt groups inherit the same `style_id`, character/outfit/prop IDs, scene map, and locked beats. Character prompts describe the white-sheet views; scene prompts describe 35mm spatial plates; video prompts describe temporal change between key-frame states. Do not paste the full map or ledger into every prompt. Include only execution-critical anchors and changes.

Check these questions before delivery:

- Does the same design appear in the character, scene, composite, and video descriptions?
- Can the scene map explain every character position and camera view without moving landmarks?
- Does every key-frame character have a known place, facing, outfit, and prop state?
- Does each cut or clip boundary inherit or explicitly change the prior state?
- Are proposed style and ungenerated key frames clearly labeled as untested?
