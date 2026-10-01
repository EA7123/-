# Role handoffs and supervisor gates

Use this protocol for script-to-prompts work. The roles are distinct responsibilities in one Skill, not a claim that separate agents or people ran. Do not say a gate passed without a recorded review and, when tools are available, a passing `scripts/supervise.py` result. At every gate also apply `creative-supervision.md`; a machine pass alone is only structural. Keep the existing Scene State, P0-P5, Shot Card, Cut Gate, visual bridge, prompt compiler, and regression rules.

## Role sequence

```text
Script and locked facts
  -> 编导 (story/beat editor)
  -> 导演选择 (method and staging thesis)
  -> 文戏指导 + 武打指导 when action exists + 美术师
  -> 监管 Gate 1: approve story, method, performance/action, and art handoff
  -> 漫剧分镜师 (timed Shot Cards and continuity)
  -> 监管 Gate 2: approve shot design and cut readiness
  -> 提示词编译师 (character, scene, and video prompts)
  -> 监管 Gate 3: compare every final prompt with approved shot decisions
  -> three prompt groups plus a short gate receipt
```

One scene uses one dominant directing method and at most one supporting method. The method is a decision framework, not a name pasted into the final video prompt. The method choice must produce observable shot decisions and a `method_impact` on each Shot Card. Use `director-methods.md` for the wider method menu. Classical coverage is a valid explicit choice when it best fits the story; explain it as a decision rather than silently skipping the director role.

## Responsibilities and handoffs

| Role | Required handoff | Reject when |
|---|---|---|
| 编导 | Locked script facts, beat IDs, scene objective, conflict/turn, exact dialogue, duration status, reveal rule | Story beats or dialogue were silently changed, or a scene has no causal job |
| 导演选择 | Dominant method ID, optional supporting method ID, reason, visual thesis, and two or more concrete shot consequences | Method is only a director name/style label or conflicts with the scene problem |
| 文戏指导 | For every dialogue beat: trigger, listener, eyeline, microexpression, small physical choice, spoken delivery, counterpart reaction, timing estimate | Characters merely recite lines, or emotion is only an adjective |
| 武打指导 | For each physical exchange: positions, force/contact path, action phases, prop ownership, screen vectors, impact/recovery and safe cut points; otherwise `not_applicable` with reason | Action teleports, contact is unreadable, or a cut skips the result |
| 美术师 | Locked medium/style ID, character identity/costume/prop proposals, white-sheet layout, empty 35mm scene plates, motivated light and color, environment/reveal anchors | The three prompt groups disagree on design, an illustrated sheet contains a photographic face, a scene plate contains human presence, or props/light/geography drift |
| 漫剧分镜师 | Timed Shot Cards with shot function, camera and movement, blocking, performance, light/color, sound, completion/cut point, inherited start/end state, and method impact | Shots are plot sentences, redundant, spatially invalid, or not performable in the duration |
| 提示词编译师 | Character and scene prompts plus shot-linked video prompt sections; every shot's execution facts trace to final text | A final prompt loses a director, acting, camera, art, sound, or continuity decision |
| 监管 | Gate verdict, evidence, failures with owner and repair request, then a recheck after repair | Any required handoff is missing, unreviewed, contradicted, or degraded by compilation |

The 武打指导 role is mandatory when bodies or props collide, people are pulled or lifted, a fall occurs, weapons move, or action geography is demanding. For dialogue-only scenes, record `not_applicable` and a reason. 文戏指导 remains active even during action when characters speak or react. 美术师 sets visual rules before Shot Cards and checks their implementation after. The supervisor can return work to a named role; the compiler may not invent a missing role decision.

## Gate decisions

- **Gate 1, before Shot Cards:** source facts and tested rhythm are locked; editor beat map exists; director method has a reason and concrete consequences; drama/action guidance and art bible are present. Creatively challenge the causal beat, emotional turn, frame concept, and model-dependent assumptions. A failure returns to the owning role.
- **Gate 2, before compilation:** every shot has a distinct function, method impact, readable space, physical action phases, dialogue performance, camera move or hold, light/color, sound, completion, and inheritable boundary. Apply P0-P5, Cut Gate, and applicable RT regressions. Replay action and dialogue timing, inspect rhythm and visual hierarchy, and identify any overloaded model job. Reject if a critical field is absent or a credible `revise`/`block` issue remains.
- **Gate 3, before delivery:** compare each Shot Card with its final video prompt section and the art/character/scene prompts. Check exact dialogue, duration, screen geography, light/color, camera trigger/path/stop, microperformance, sound, reveal, and cut result. Reject any scene prompt that invites people, body parts, silhouettes, human reflections or shadows; reject an anime character prompt with a photographic face or mixed rendering. Recompile any missing information and rerun Gate 3. A keyword checklist alone is insufficient; name the retained phrase or sentence for every shot. Also predict the likely visible failure, remove competing instructions, and verify that the prompt emphasizes the primary beat. Inspect actual generated images before claiming image-level compliance.

Stop after at most two repair passes on the same failed gate without new evidence. Report the unresolved failure and owner rather than declaring success. If no scripts or tools are available, perform the same review visibly and state `manual review`; never claim a machine-validated pass. If only text exists, distinguish design review from actual generated-image/video QC. A creative review must record `block`, `revise`, or `watch` for material risks; a structural pass does not erase them.

## Machine-checkable manifest

When a filesystem and Python are available, keep an internal JSON manifest and run `scripts/supervise.py <manifest.json> --stage 1`, then `--stage 2`, then `--stage 3` at the three gates. The script uses only the Python standard library. It checks role handoffs, field presence, timing bounds, shot-to-prompt coverage, exact locked dialogue, and quoted evidence retained in each video prompt. It cannot judge acting quality, artistic merit, or whether a video model will obey; the supervisor reviews those semantically.

See the script's `--help` and the RT-001 example manifest in `rt-001-audit.json`. A Stage 3 pass is required before describing a prompt package as structurally supervised. When deliverables are chat text only, the manifest may be temporary; the final response includes a compact gate receipt such as:

```text
Director: D01 staging/reveal + D05 spatial storytelling.
Gate 1/2/3: PASS / PASS / PASS (structural); creative review: timing WATCH pending read/animatic.
Key retained choices: same-side uphill axis; hand pull finishes before pavilion reveal. Generated-video QC: not tested.
```

Keep the receipt short and place the three user-facing prompt groups after it. Never substitute the receipt for the prompts.
