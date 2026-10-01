# Continuity and spatial logic

Before shot design, sketch the scene as inherited state: positions, facing directions, entrances, exits, important props, environmental anchors, target reveal state, light sources, sound sources, and camera-safe side of the axis.

For multiple scene-image views or video clips, use the coordinate map and boundary ledger in `visual-continuity-bridge.md`; a 35mm scene description alone does not locate the camera or anchor the target.

## Required state checks

- Scene State persists across shots unless an explicit event changes it.
- Character State persists across shots. Position, facing, distance, action phase, emotion, eyeline, and dialogue state may change only through visible or audible events.
- Environment Anchor stays fixed in relative position, height, and distance.
- Reveal State controls when an existing target becomes visible; do not reveal targets early.
- Audio State follows distance, action, and point of view.

## Spatial checks

- Keep left/right screen direction stable across movement and dialogue.
- Keep front/back and height relationships stable unless a visible action changes them.
- Match eyeline height and direction to the target’s established position.
- Preserve hand, prop, costume, body posture, and action phase across cuts.
- Cut on action only when both shots share a compatible action phase or when the action has completed.
- Maintain the viewer’s map after inserts and close-ups by returning to an orienting view when needed.
- Track sources of key, practical, and motivated light across reverse angles.
- Track diegetic sound perspective and ambience through spatial changes.

## Crossing the axis

Cross only intentionally. Bridge with a neutral-axis shot, visible camera/character movement across the line, a new establishing shot, or a motivated POV that resets geography. If disorientation is the intention, identify the dramatic reason and the shot that later restores orientation.

## AI-generation continuity

Lock character identity, costume, props, time of day, weather, screen direction, lens tendency, palette, location anchors, character formation, and target reveal timing. Each prompt should repeat only the continuity facts the generator must preserve. Define the start frame, subject action, camera action, sound action, environment motion, and end frame; avoid asking one short clip to perform multiple unrelated beats without internal shot timing.
