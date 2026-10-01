# Creative and generation-feasibility supervision

Use this review after each structural gate for script-to-prompts work. Its job is to improve the expected result, not to award an unearned "S grade." A complete checklist or passing `scripts/supervise.py` does not establish visual quality or lower a measured retry rate. Review the actual story, shot plan, and prompt as a skeptical director, cinematographer, performance director, and production supervisor. If only text exists, call the outcome a **design judgment**; only a timed read, animatic, generated frame, or reviewed take can verify the corresponding result.

## The six judgments

| Judgment | Test the draft against | Return work when |
|---|---|---|
| Dramatic force | For each beat, name what the audience knows, expects, then feels differently. Trace stimulus -> perception -> physical response -> choice -> consequence. Try removing a shot or line: does the turn survive? | Shots merely illustrate dialogue, emotional labels replace visible behavior, or a reveal has no setup/payoff. |
| Image quality | Inspect subject hierarchy, negative space, depth planes, perspective, art continuity, motivated light direction, palette contrast, focus target, and a single readable visual change per shot. State what the eye should find first. | The frame has competing focal points, generic "cinematic" adjectives, flat space, inconsistent light, or no designed depth. |
| Motion and action | Mentally replay each body/prop path from start to contact to recovery; track hands, footing, weight, screen direction, occlusion, camera parallax, and action across cuts. Verify start/end states can be pictured as still frames. | An action teleports, reverses direction without a bridge, hides the decisive contact, or asks a moving camera to obscure critical motion. |
| Dialogue and emotion | Read each line aloud when possible; map speaker/listener, breath, pauses, interruption, eyeline, microexpression, small action, and counterpart reaction. Check whether dialogue overlaps a compatible shot and whether lip-sync/audio is in scope. | Dialogue is squeezed into an untested window, characters recite without listening, expression is only an adjective, or a model is asked for unsupported synchronized speech. |
| Rhythm and camera | Check the sequence of wide/close, hold/move, compression/release, and the precise reason for every cut. Test whether the viewer has enough time to orient, read the face, follow the action, and recognize the result. | Repeated equal beats flatten rhythm, movements have no trigger/stop, or the cut arrives before action/emotion completes. |
| Generation robustness | Count simultaneous independent burdens in each model job: identity, multiple characters, hands/contact, fast motion, camera move, exact dialogue/lip sync, environmental effects, reveal, and multi-shot edit. Compare with the selected model's verified abilities and available reference assets. | A job depends on unverified capabilities or stacks too many fragile requirements without a fallback. |

Do not turn these into a numerical quality score. Identify the one or two highest-risk failure modes that would waste a generation attempt. For each, name the likely visible artifact (e.g., hand swaps sides, weightless pull, mushy dialogue, flat lighting), its cause, and the smallest change that preserves the locked story. Prioritize by impact on audience comprehension and probability given **known** model behavior; if model behavior is unknown, label that uncertainty instead of pretending to know a probability.

## Repair order

1. Protect locked dialogue, beat order, total duration when tested, character intent, geography, and reveal. Never improve "quality" by silently removing them.
2. Fix causal and physical contradictions in the script/state/Shot Card first. More ornate prompt wording cannot repair an impossible action or missing reaction.
3. Simplify each generation job to a coherent visual task while preserving the scene: stabilize identity and location references, reduce redundant camera moves, make contact or reveal the primary beat, and route unsupported speech/audio to a separate pass where appropriate. A job split is a **proposal**, not an automatic change to tested runtime or edit rhythm.
4. Recompile with positive, observable instructions: subject, spatial anchor, event, camera trigger/path/stop, performance, light/color, sound, result. Keep the prompt concise enough that priority is clear. Do not pile on synonyms or generic negative prompts.
5. Re-run structural gates and the six judgments. If a real model is authorized and available, test a small representative shot, inspect timecodes/frames, then change one dominant variable per retry. Keep accepted assets and takes. Do not spend credits or invoke a model without authorization.

## Review record

For any **material** risk, record a concise issue, not a self-congratulatory pass:

```text
Gate / shot or prompt ID:
Observed design evidence:
Predicted visible failure and uncertainty:
Severity: block | revise | watch
Owner and smallest repair:
Recheck evidence or untested dependency:
```

`block` means contradiction, omitted protected content, unsupported required model feature, or unperformable timing established by measurement. `revise` means a credible quality/generation risk with a concrete repair. `watch` means the text is plausible but requires a read, animatic, frame, or take to decide. A design-only reviewer must not mark a watch item verified. After two repair cycles without new evidence, surface the tradeoff to the user rather than looping or silently lowering requirements.

## RT-001 rehearsal

For the 10-second mountain-road example, a structural pass confirms five internal shot sections and exact lines, but does not prove that all three lines, the hand pull, and the late pavilion reveal fit naturally. The creative supervisor should flag speech/action timing as **watch** until a read/animatic exists; check that the hand grasp and stable footing remain visible before the summit cut; and compare the five-shot design with a less fragmented internal coverage option if reactions feel rushed. Preserve the validated 10-second story rhythm and exact lines. A different cut pattern is a proposed internal edit, not a new validated result.
