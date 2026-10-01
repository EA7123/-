# Dialogue, shot rhythm, and camera motion

Use when designing shot durations, dialogue coverage, motion speed, or a timed video prompt. Keep story beats and any user-validated total duration locked. Treat proposed per-shot timestamps as provisional until dialogue and action have been performed or tested.

## Timing ledger

For every beat, record a timing window and what must finish within it:

| Beat ID | Required action and result | Line / speaker | Speech in/out | Reaction or hold | Shot in/out | Cut or overlap | Evidence |
|---|---|---|---|---|---|---|---|

Start with a natural-speed table read or scratch voice recording when possible. Time each line, breath, interruption, and reaction from actual audio. An animatic or rough visual test checks action duration and viewer comprehension. Do not estimate speech from a universal words-per-second constant as final proof. If only text exists, mark the windows `estimated` and identify lines whose spoken duration may exceed their allotted shot.

Dialogue can bridge a cut or play over a reaction shot when spatial and emotional continuity remain clear; the speaker need not occupy the entire spoken interval on screen. Keep exact dialogue and causal order. Do not compress a performance into unnatural speech speed to satisfy a draft time grid. If measured speech and action cannot fit a locked total duration, surface the conflict and test an internal reallocation or legitimate overlap before proposing a story or runtime change.

## Shot duration and sequence rhythm

Allocate time from the audience's task: orient in space, perceive action, read a reaction, hear a line, or recognize a reveal. A shot may hold through a performance change; a short shot still needs a readable new fact. Use the Cut Gate to preserve action phases and eyelines. Across the sequence, inspect the pattern of holds and cuts: repeated equal-length shots can feel mechanical even when individually valid. Contrast pace only when a story turn, information reveal, or emotional shift warrants it. Avoid a fixed short/long alternation formula.

Record both `planned_duration` and `tested_duration`. Check whether a character can enter, act, speak, receive a response, and exit in the assigned window. A single scene can preserve its validated overall rhythm while moving internal cut points after a read-through. Do not call a revised internal timing tested until the audio/animatic or generated clip has been reviewed.

## Camera movement speed

For each moving shot, specify the subject or event that triggers motion, start position, path, direction, relative speed, settling point, and the fact revealed or relationship changed. Prefer observable relative language such as "tracks with the walking pace" or "slowly closes distance during the pause" over unsupported numerical speed. Check that the camera move finishes before the next cut or that the next shot inherits the motion vector. A static shot is a deliberate pace choice when performance carries the beat.

## Review gate

- Spoken dialogue remains natural and complete; speaker and reaction timing are clear.
- Actions reach a legible result or continue across a phase-compatible cut.
- Shot lengths allow geography, emotion, and reveals to register.
- Camera acceleration and stop points serve the beat and do not contradict character movement.
- Sound and picture cuts preserve ambience and causal order.
- Timing status is labeled `estimated`, `table-read`, `animatic-tested`, or `footage-tested`, with the artifact path or timecode when available.

For an AI video model, confirm its actual duration and audio abilities in the generation job. A text prompt with timestamps is an instruction, not proof that the model followed them. Verify in generated footage and log drift by timecode.
