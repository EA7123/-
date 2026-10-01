# Storyboard Director v3 Architecture

This file defines the required internal structures for director-level storyboard generation and AI video prompt compilation.

## Priority Layer

Apply the layers in order. Do not add lower-priority decoration while a higher-priority layer is broken.

### P0: Spatial continuity

Must define and preserve:

- Main axis
- Camera side
- Character left/right relationship
- Character front/back relationship
- Character distance
- Character facing
- Character movement direction
- Target object position
- Target object height
- Character-to-target distance

If P0 fails, stop and repair geography before writing prettier images.

### P1: Action continuity

Every key action needs:

```text
start state -> action process -> action completion -> result state
```

Do not cut from an action start directly to an unrelated shot. Cut only after the action phase is readable or when both sides of the cut preserve a compatible action phase.

### P2: Performance and dialogue

Dialogue is a performance event, not a text field. Bind each line to:

```text
trigger -> attention -> reaction -> eyeline -> expression -> action -> dialogue -> counterpart reaction
```

Avoid blank delivery, detached action, meaningless exits during a line, or long empty waits before speech.

### P3: Shot function

Every shot must provide one or more non-redundant functions:

- Establish space
- Establish character relation
- Establish movement direction
- Expose emotion
- Show reaction
- Complete action
- Deliver dialogue
- Reveal information
- Shift rhythm
- Reveal environment
- Resolve emotion

If two shots have the same function and the second adds no new visual information, combine or remove one.

### P4: Environment

Environment must have dynamic causes. Name the source and visible/audible effects:

```text
wind -> leaves shift -> mist changes -> robe hem moves -> fabric sound rises
wet stone -> foot pressure -> water splash -> footstep timbre changes
```

Avoid generic phrases such as “dynamic environment” without a cause.

### P5: Audio

Audio is a formal Shot Card field. Build layers where relevant:

- Foreground: dialogue, breath, footsteps, cloth, hand contact
- Middle ground: nearby leaves, near wind, water drops, grass or branches
- Far field: valley wind, distant ambience, spatial echo

Bind sound to action and geography. When feet stop, footstep sound stops and breath can come forward. When wind rises, leaves and cloth should react.

## Scene State

Create once per scene and inherit it across shots.

```text
Scene Location:
Scene Height:
Terrain Direction:
Weather:
Time:
Camera Side:
Main Axis:
Character Formation:
Target Object:
Target Distance:
Target Height:
Reveal State:
Environment Motion:
Ambient Audio:
```

Scene State prevents each shot from reinventing the world.

## Character State

Create for every major character and inherit between shots.

```text
Position:
Relative Position:
Facing:
Movement Direction:
Action Phase:
Emotion State:
Eye Direction:
Dialogue State:
Goal:
```

A character may change position, facing, distance, action phase, eyeline, or emotional state only through a visible event: stop, turn, approach, reach, grasp, pull, step forward, look away, and so on.

## Environment Anchor

Important environmental targets must have stable spatial anchors.

```text
Target:
Relative Position:
Height:
Distance:
Spatial Anchor:
```

The anchor must not drift from front to side, far to near, low to high, or one part of the scene to another unless the scene explicitly moves there.

## Reveal State

Separate target location from target visibility.

```text
Hidden -> Partial -> Visible -> Full
```

A target can exist in the Scene State while remaining hidden. Do not leak a target visually before its reveal window.

## Shot Capacity Rule

Default capacity per shot:

```text
1 primary action + 1 primary emotional change + 1 primary information change
```

If a shot carries heavy travel, multi-character interaction, multiple dialogue turns, environment reveal, and a major camera move at once, split it. If a tested 10-second rhythm works, split into motivated internal shots without changing total duration.

## Cut Gate

Before every cut, check:

```text
Shot Function complete?
Action complete or phase-compatible?
Emotion Beat complete?
Dialogue complete, or intentionally bridged across the cut with clear speaker and reaction continuity?
Spatial State inheritable?
Next shot adds new visual information?
```

If a key item fails, do not cut yet.

## Shot Card v3 fields

A complete Shot Card must include at least:

```text
Time
Shot Function
Director Method Impact
Shot Size
Camera Position
Camera Side
Camera Angle
Camera Movement: trigger, path, speed, stop
Viewpoint
Lens / Focal Character
Composition
Character Position
Character Relation
Character Facing
Movement Direction
Action
Expression
Observable Microexpression and Small Gesture
Eye Direction
Lighting Direction and Color Treatment
Dialogue
Audio
Environment Motion
Action Completion Point
Cut Reason
Next Shot Continuity
```

Shot Card is internal design data, not the final prompt.

## Supervisor gates

Use the three returnable gates in `roles-and-gates.md`. Gate 1 checks 编导, 导演选择, 文戏指导, 武打指导 (or justified not-applicable), and 美术师 handoffs before shot design. Gate 2 checks the 漫剧分镜师 Shot Cards against P0-P5, state inheritance, environment anchors, reveal timing, shot capacity, Cut Gate, timing, and protected prior elements before compilation. Gate 3 compares each compiled prompt section to its source Shot Card and verifies exact dialogue, method consequences, camera, blocking, performance, light/color, audio, and transition before delivery. A failed gate returns work to the responsible role; no later gate overrides it.

## Prompt Compiler

The compiler translates Shot Cards into the shortest complete AI video prompt that preserves execution-critical facts.

Keep:

- Scene
- Characters
- Camera
- Camera movement with a motivated start and stop
- Space
- Action
- Emotion visible in face, eyeline, and a small physical choice
- Dialogue
- Lighting and color treatment that persists across adjacent shots
- Sound
- Environment motion
- Reveal and cut logic

Delete:

- Director explanations
- Rule explanations
- Failure Log content
- Regression Test content
- Repeated limitations
- Synonym piles
- Literary redundancy

The goal is short and complete, not short and missing fields.

## Prompt Output Lock

Before showing a final prompt, verify that it contains:

```text
[ ] Duration
[ ] Aspect ratio
[ ] Base style
[ ] Reference image notes, if any
[ ] Timeline
[ ] Shot count
[ ] Shot Function
[ ] Director method has an observable shot-level consequence
[ ] Shot size
[ ] Camera position
[ ] Camera angle
[ ] Viewpoint
[ ] Camera movement
[ ] Camera movement trigger and stop, or a deliberate locked camera
[ ] Character placement
[ ] Character facing
[ ] Movement direction
[ ] Action
[ ] Expression
[ ] Observable microexpression and small gesture at dialogue or reaction beats
[ ] Eyeline
[ ] Lighting direction and color treatment
[ ] Dialogue
[ ] Sound effects
[ ] Environment motion
[ ] Cut logic
[ ] Next-shot continuity
```

If a core item is missing, repair the prompt before output.
Run Gate 3 after this lock. The lock alone is not a Supervisor pass.

## Prompt Regression Rule

For every modification, record:

```text
Previous Valid Elements:
Changed Elements:
Newly Added Elements:
Removed Elements:
Reason:
```

After the change, ask whether fixing one issue removed something that already worked.

## Failure Log schema

Use this format:

```text
FAIL-ID:
Problem:
Observed Result:
Root Cause:
Layer:
Fix:
Regression Test:
Status:
```

Layer must be one of:

```text
Script | Pacing | Storyboard | Scene State | Asset | Prompt Compiler | Prompt | Generation Job | Model Generation | Footage QC | Edit | Audio | Unknown
```
