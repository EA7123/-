# RT-001 Mountain Road Regression Case

## Case identity

Rain-wet mountain stone steps leading to a pavilion at the summit.

The original 10-second rhythm has been validated. Do not split the case into 5 seconds, 6 seconds, or 5 + 5 seconds by default. Generation duration is 10 seconds; shot count is decided by dramatic and spatial function.

The role/gate audit example is [rt-001-audit.json](rt-001-audit.json). Its D01 dominant staging/reveal method and D05 supporting spatial method are choices for this rehearsal, not proof that any generated video passed QC. Gate 1 checks the editor, dialogue, action, art, and method handoffs; Gate 2 checks the five timed Shot Cards; Gate 3 checks the compiled prompt sections against those cards and the locked lines. Run `scripts/supervise.py` at each stage. A structural pass does not verify natural dialogue timing or visual output.

## Preserve-first record

```text
Previous Valid Elements:
- 10-second total rhythm.
- Two characters climb upward on rain-wet mountain steps.
- A-yue becomes tired, stops, complains, takes Shen Yan's hand, is pulled up, and continues.
- Shen Yan notices her, responds with concern, reaches back, pulls her up, and leads onward.
- Pavilion is revealed only near the end as the target at the summit.
- Dialogue remains exactly as written.
- Prompt should be concise, structured, and complete.

Changed Elements:
- Add formal Scene State, Character State, Reveal State, Audio State, Shot Card v3, Cut Gate, and Prompt Output Lock.

Newly Added Elements:
- Explicit spatial anchor for the pavilion.
- Action completion points for stop, reach, grasp, pull, stand, continue.
- Layered audio tied to wet steps, breath, cloth, leaves, wind, and distant mountain ambience.
- Environment motion caused by wind, rainwater, mist, and contact with wet stone.

Removed Elements:
- None.

Reason:
- Stabilize director-level storyboard, prevent spatial drift, early reveal, incomplete action cuts, static environment, and audio flattening.
```

## Locked story beats

```text
Two people climb with difficulty.
A-yue gradually tires.
A-yue stops.
A-yue complains.
Shen Yan notices her.
Shen Yan cares for her.
Shen Yan reaches out.
A-yue takes his hand.
Shen Yan pulls her up.
They continue climbing.
The pavilion at the summit is revealed at the end.
```

## Locked dialogue

```text
A-yue: “还有多远？我腿都酸了……”
Shen Yan: “快了，上面就是凉亭。”
A-yue: “早知道不跟你上来了……”
```

## Scene State

```text
Scene Location: Rain-wet mountain road with stone steps.
Scene Height: Mid-slope moving toward summit.
Terrain Direction: Low foreground/path behind -> higher steps ahead -> summit.
Weather: After rain; wet stone, mist, light wind.
Time: Soft daylight after rain.
Camera Side: Fixed same side of the climbing axis.
Main Axis: Characters move uphill toward the pavilion.
Character Formation: Shen Yan ahead, A-yue behind.
Target Object: Summit pavilion.
Target Distance: Far at the start, reachable visually only at the end.
Target Height: Higher than both characters, on the ridge/summit.
Reveal State: 0-8s Hidden, 8-9s Partial, 9-10s Visible/Full.
Environment Motion: Wind moves leaves and robe hems; mist shifts between trees; drops fall from branches; footsteps disturb water on stone.
Ambient Audio: Foreground breath/steps/cloth/contact; middle-ground leaves/drips; far-field valley wind.
```

## Shot Cards v3

| Time | Shot Function | Shot Size | Camera Position | Camera Side | Camera Angle | Viewpoint | Lens / Focal Character | Composition | Character Position | Character Relation | Character Facing | Movement Direction | Action | Expression | Eye Direction | Dialogue | Audio | Environment Motion | Action Completion Point | Cut Reason | Next Shot Continuity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-2s | Establish uphill geography and formation | Medium wide | Same side of stone-step axis, slightly below and beside them | Fixed same side | Slight low angle along steps | Observing the climb | 32-40mm, both | Wet steps lead upward; Shen Yan ahead, A-yue behind lower | Shen Yan front/high, A-yue rear/low | Front/back and height difference clear | Both face uphill | Low to high | They climb slowly; A-yue lags | A-yue already tired, Shen Yan focused | A-yue glances at steps and Shen Yan's back | None | Wet footsteps foreground; breath; nearby drips; far valley wind | Formation and uphill direction established | Cut to fatigue when lag becomes visible | Preserve same camera side and uphill axis |
| 2-4s | Show fatigue, stop, first complaint | Medium on A-yue with Shen Yan still ahead in frame edge/depth | Same side, closer to A-yue | Fixed same side | Eye-level to slight low | A-yue performance | 50-65mm, A-yue | A-yue lower step foreground; Shen Yan higher ahead | A-yue behind, Shen Yan in front | Distance opens slightly as she stops | A-yue faces uphill, bends slightly | Stops on wet step | Tired, breathy complaint | Looks from steps to Shen Yan | A-yue: “还有多远？我腿都酸了……” | Footsteps stop; breath rises; cloth and light wind; drips continue | A-yue fully stops and complaint lands | Cut because Shen Yan must react | Shen Yan remains ahead/higher; A-yue remains behind/lower |
| 4-6s | Shen Yan notices and responds with care | Over-shoulder / two-shot relation | Behind/near A-yue shoulder toward Shen Yan higher step | Fixed same side | Slight upward angle to Shen Yan | Relationship angle | 50-65mm, Shen Yan | A-yue shoulder lower foreground; Shen Yan turns back on higher step | Shen Yan front/high, A-yue rear/low | Distance visible between hand reach range | Shen Yan turns back toward A-yue | Uphill movement pauses | Shen Yan stops, turns, softens, speaks | Concerned, reassuring | Shen Yan looks at A-yue | Shen Yan: “快了，上面就是凉亭。” | His step sound stops; voice foreground; wind and leaves middle layer | Shen Yan has turned and delivered reassurance | Cut to hand action after emotional attention is established | Same side; pavilion still hidden |
| 6-8s | Complete reach, grasp, pull-up action | Medium close on hands and torsos, enough space for height relation | Same side, near their shared axis | Fixed same side | Eye-level, slight tilt following hands | Action continuity | 50-65mm, hands then both | Shen Yan higher left/front reaches down/back; A-yue lower right/rear reaches up | Height gap and front/back preserved | Their bodies angle toward each other | A-yue shifts upward; Shen Yan braces uphill | Shen Yan extends hand; A-yue grasps; he pulls; she steps up and steadies | A-yue reluctant but trusts; Shen Yan focused | A-yue looks at hand then up; Shen Yan checks her balance | A-yue: “早知道不跟你上来了……” | Hand contact foreground; wet step scrape; breath; cloth rub; drips/leaves | A-yue reaches a stable higher step | Cut only after pull and balance complete | They are closer and ready to continue uphill |
| 8-10s | Resume climb and reveal target pavilion | Wide to medium wide | Same side, slightly behind them looking uphill | Fixed same side | Low angle opening to summit | Shared destination reveal | 32-40mm, both then pavilion | Characters lower foreground continue upward; mist parts at summit | Shen Yan ahead, A-yue just behind after being helped | Relationship stable and closer | Both face uphill | Continue low to high | They climb on together; pavilion emerges ahead | A-yue still annoyed but moving; Shen Yan calm | Both look uphill toward reveal | None | Footsteps resume; breath settles; wind lifts leaves/robe hems; far ambience opens | Pavilion reaches Visible/Full state without spatial drift | End on destination payoff | No next shot; target anchored high ahead |

## Shot Card performance and photography overlay

These columns supplement the earlier Shot Card table and are inherited by the compiled prompt. The internal 2-second boundaries remain estimated; natural dialogue may bridge a phase-compatible cut.

| Time | Camera movement and stop | Observable microexpression / small gesture | Lighting and color | Cut result |
|---|---|---|---|---|
| 0-2s | Low same-side lateral follow; stop as A-yue stops | Shoulder sinks, brow tightens, gaze lifts from steps to Shen Yan | Soft upper-left daylight; blue-gray wet stone, deep green forest, warm skin | Stopped foot and opening line lead to her close view |
| 2-4s | Same-side slow half-step push on A-yue; settle on raised eyes | Hand braces on knee, nostrils open with breath, lower lip presses before complaint | Eye light soft; retain cool background and warm face | First complaint lands; cut to Shen Yan's response |
| 4-6s | Over-shoulder gentle pan with Shen Yan's turn; settle at eye contact | Brow relaxes, mouth corner lifts slightly, eyes check her leg then return to face; hand begins to extend | Warm bounce on face, cool green background; pavilion unshown | Reach carries motion into hand shot |
| 6-8s | Same-side two-shot tilts down to reach and up with pull; settle on both faces | A-yue presses lips, hesitates, meets his gaze, grasps; shoulders release once steady; Shen Yan checks her balance | Same light direction; wet stone glints without shifting palette | Grasp, pull, and stable stance complete before wide; line tail may bridge |
| 8-10s | Same-side rear wide rises gently with climb and tilts to summit; stop on shared gaze | A-yue exhales and briefly glances sideways; Shen Yan returns a short confirming look | Soft light opens on ridge; slight distant warmth within same blue-gray/green grade | Pavilion Partial then Visible at fixed high anchor; end |

## Compiled AI video prompt

10秒、16:9，五个有明确切点的内部镜头。雨后山路湿石阶，柔和日光从画面左上穿过薄雾，青灰石面、深绿树林、人物面部略暖；光向和色调贯穿全段。摄影机始终位于上山轴线同一侧。沈砚始终在前方高处，阿月在后方低处，直到拉起后距离缩短。山顶凉亭位置固定在前方高处，0-8秒完全被山脊和树遮挡，8-9秒局部露出，9-10秒清楚可见。以下内部切点为待配音验证的设计时间，不改10秒总节奏。

镜1，0-2秒，建立空间的35mm中远景，机位在石阶左侧稍低处；两人向上，摄影机以慢速侧跟，阿月步伐变重时停机。近景湿石反光，中景两人前后高低清楚，远景山脊被雾遮住；阿月肩微塌，眉心收紧，视线从石阶抬向沈砚背影，约末尾停步并开始第一句。湿脚步、呼吸、近处滴水、远处山风分层。她的脚步停住，切向她的反应近景。

镜2，约2-4秒，同侧50mm中近景，阿月仍处低处，沈砚的背影留在高处画面边缘。她一手撑膝，鼻翼轻张、下唇微抿，抬眼看他，带疲惫和轻微埋怨说完：“还有多远？我腿都酸了……”摄影机在她停稳后缓慢推近半步，停在眼神抬起处；左上柔光照亮眼部，背景维持冷青灰。她的脚步声消失、呼吸凸显。台词落点后切到沈砚；若自然语速需要，第一句可从镜1末段跨入本镜。

镜3，约4-6秒，阿月肩后过肩中景，摄影机仍在轴线同侧、略向高处仰拍沈砚。听见她后他先停脚、回头，眉峰松开，嘴角克制地抬一下，目光从她脸移到她发软的腿，再回到她眼睛；摄影机随转头轻摇并在两人对视时停住。他略放轻声音说：“快了，上面就是凉亭。”说话末尾身体侧转、向下伸出手。面部有柔和暖反光，背后树林保持冷绿；凉亭仍不可见。脚步停声，风吹叶与衣摆。以伸手动作切入下一镜。

镜4，约6-8秒，同侧50mm双人中近景，保留两人的脸、手和台阶高差。摄影机先轻俯跟随沈砚伸下的手，阿月先看手、嘴唇绷紧，随后眼神抬向他，犹豫半拍才握住；镜头随握手微抬并停在两人脸部同框。沈砚后脚踩稳，手臂用力拉她上一阶；阿月边起身边带一点嘴硬的气声说：“早知道不跟你上来了……”她脚踏实后肩膀松开，沈砚用短暂眼神确认她站稳。手掌接触、湿石擦步和衣料摩擦位于前景，滴水与风声持续。动作完成再切；台词尾音可连到下一镜，人物和声音归属不变。

镜5，8-10秒，同侧稍后方35mm中远景，两人继续向前，沈砚仍领先、阿月距离更近；她余音落下，轻呼气并侧看他一眼，沈砚回以很短的确认眼神。摄影机沿石阶缓慢上移并轻仰，风推动前景叶片和湿雾；8-9秒山顶凉亭先从固定山脊后局部露出，9-10秒清楚显现，仍在两人前方高处。画面左上柔光掠过湿石，远处略暖但整体青灰绿色调不变。脚步重新响起，近处呼吸渐平，远处山风展开；镜头在两人看向凉亭时停住结束。

## Production handoff example

This is a plan for the existing 10-second case. No character plates, location references, model account, generated takes, or edited export were supplied. Do not mark its video QC or edit as passed.

```text
episode_id: RT-001
source_script: locked beats and dialogue above; version not supplied
opening: uphill geography and Shen Yan / A-yue formation
turn: A-yue stops and complains; Shen Yan notices and helps
payoff: both resume climbing; pavilion revealed only in the final two seconds
target runtime: 10 seconds, validated story rhythm
```

Asset inventory to create or bind before generation:

| Asset ID | Required reference | Current status |
|---|---|---|
| CHAR-SHENYAN | Approved front, side, full-body, outfit and expression references | missing |
| CHAR-AYUE | Approved front, side, full-body, outfit and expression references | missing |
| LOC-MOUNTAIN-ROAD | Wet stone-step views and a simple uphill orientation map | missing |
| LOC-PAVILION | Pavilion design and fixed summit position relative to road | missing |
| STYLE-RT001 | Approved look and palette reference | missing |

Planned job `RT001-GEN-01` binds the five Shot Cards above to one 10-second result only if the selected model can follow multiple internal shots, exact dialogue, and the late reveal reliably. Record the model/version, supported inputs, actual asset file paths, prompt version, and any first/last frames before moving the job to `ready`. Otherwise test a supported alternative while preserving the 10-second story rhythm; do not silently change the tested pacing.

The footage reviewer must inspect whether Shen Yan stays uphill and ahead, A-yue stops before the first line, the hand grasp and pull reach a stable result, all three lines stay intact, and the pavilion is absent before 8 seconds and anchored above them at the end. Note exact failure timecodes and the selected take ID. The edit plan then uses the accepted take with source in/out points and checks that the final reveal and sound resolve cleanly. Current generation, footage QC, and edit status: `pending`.

## Visual prompt and timing rehearsal

Character prompts `CHAR-SHENYAN` and `CHAR-AYUE` can be written immediately as visual design proposals: the source defines their names, relative positions, actions, and emotions but does not specify faces, hair, costumes, or style. Choose one coherent proposed look for the pair, label inferred traits, and keep them stable across the prompt set. Each prompt must request the pure-white single canvas with a frontal extreme face close-up at left and matched full-body front/back views at right. Do not call the proposals approved character assets or claim cross-shot visual consistency has been tested. See `visual-prompt-bible.md`.

Draft scene plate for `LOC-MOUNTAIN-ROAD`: an empty environment image with no person, body part, silhouette, human reflection or shadow. Use a 35mm perspective, with near wet stones and leaves in the foreground, the unoccupied climbable steps and character path in the midground, and the higher ridge as a legible background destination. Rain-wet stone steps climb from low to high, with trees, post-rain mist, soft daylight, and light wind. Use fine moisture, droplets, and shifting mist in the air rather than dry dust. Camera remains on the same side of the uphill path. Branch drips disturb small water patches; wind moves leaves and mist. Keep the summit pavilion spatially high and ahead on the map but fully occluded in views used before 8 seconds. A separate empty 8-10s reveal plate shows it emerging in the same fixed location. Add characters only in a separate composite key frame or video prompt. The plate remains a proposed layout until a location map or generated reference is approved.

The original 10-second story rhythm is locked. The five 2-second Shot Card windows above are a proposed internal allocation, not measured dialogue or action durations. Use `timing-performance.md` to record a scratch performance or animatic before calling these boundaries feasible:

| Beat | Draft window | Spoken line or physical action | Timing evidence | Check before approval |
|---|---|---|---|---|
| A-yue stops and complains | 2-4s | “还有多远？我腿都酸了……” | estimated; no audio supplied | Stop, breath, and full natural-speed line fit or bridge the cut coherently |
| Shen Yan responds | 4-6s | “快了，上面就是凉亭。” | estimated; no audio supplied | He notices, turns, and speaks before hand action begins |
| Hand help and A-yue's second line | 6-8s | “早知道不跟你上来了……” plus reach, grasp, pull, stable stance | estimated; no audio/animatic supplied | Complete action and line without rushed performance; overlapping speech may bridge action phases |
| Destination reveal | 8-10s | Climb resumes; pavilion Hidden -> Partial -> Visible | estimated visual timing; no clip supplied | Target appears only near the end and remains high ahead |

Adjust internal cut points or carry a line across a phase-compatible cut if a natural performance needs it. Keep the exact dialogue, beat order, character relation, late reveal, and validated 10-second total. If a read-through or animatic still cannot fit, report that conflict rather than claiming the prompt resolves it.

## Internal visual continuity bridge

The following is a text-only rehearsal of `visual-continuity-bridge.md`; it is not a fourth output group or evidence that images were generated.

```text
style_id: STYLE-RT001/v1, proposed, not approved.
rendering: grounded cinematic animation; natural proportions and materials;
restrained wet-stone gray and foliage green; soft post-rain daylight.
character sheet: same rendering and proportions, neutral light on pure white.
scene/video: same design language, with moisture and moving mist rather than dry dust.

map: LOC-MOUNTAIN-ROAD/v1, proposed.
positive u: uphill along stone steps toward summit.
v: left/right when facing uphill; h: elevation.
Shen Yan starts at greater u and h than A-yue; both face positive u.
camera stays on one chosen side of the path; later angles inherit that side.
pavilion: fixed at far positive u, high h on the summit ridge.
0-8s visibility Hidden behind ridge/trees and viewing angle;
8-9s Partial through shifting mist; 9-10s Visible in the same position.
```

Composite key-frame specifications: `K0` shows both climbing in the mapped formation, pavilion occluded; `K4` shows A-yue stopped lower behind Shen Yan, looking toward him; `K6` shows Shen Yan turned on the higher step and beginning the reach; `K8` shows the grasp/pull completed, A-yue steady and closer behind him, pavilion still unrevealed at the boundary; `K10` shows both continuing uphill with the pavilion visible high ahead. All carry `STYLE-RT001/v1` and the same character/outfit designs once proposed. The precise sub-shot boundaries are estimated until a table read or animatic exists.

Boundary checks: `K4 -> K6` keeps Shen Yan ahead/higher while he turns; `K6 -> K8` records hand contact, pull, and A-yue's resulting stable position; `K8 -> K10` carries that closer formation into the resumed climb and changes only pavilion visibility. No prop changes are specified in the source, so do not introduce or transfer a prop in the video prompt. These are internal shot boundaries within the planned 10-second result, not claims that five separate model jobs or real first/last-frame images exist.
