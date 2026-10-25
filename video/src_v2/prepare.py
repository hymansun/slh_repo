# 1) 合成每句语音  2) 计算时间轴  3) 生成场景 HTML
import json, os, re, sys, subprocess
import numpy as np, soundfile as sf
sys.path.append(os.path.abspath('..'))
from scenes import S
LEAD, GAP, TAIL = 1.0, 0.45, 1.1
os.makedirs('audio', exist_ok=True); os.makedirs('html', exist_ok=True)
need_tts = '--no-tts' not in sys.argv
if need_tts:
    from ktts import say
CSS, JS = open('style.css').read(), open('anim.js').read()
plan, total = [], len(S)
for si, (label, body, sents) in enumerate(S):
    cues, ends, subs, t = [], [], [], LEAD
    for j, s in enumerate(sents):
        sub, speak = (s, s) if isinstance(s, str) else s
        assert not re.search(r'\d', speak), speak
        f = f'audio/s{si:02d}_{j}.wav'
        if need_tts or not os.path.exists(f):
            say(speak, f, speed=1.02)
        x, sr = sf.read(f)
        nz = np.where(np.abs(x) > 0.01)[0]; x = x[max(0, nz[0] - int(.03*sr)): nz[-1] + int(.08*sr)]  # 去首尾静音
        sf.write(f, x, sr)
        d = len(x) / sr
        cues.append(round(t, 3)); ends.append(round(t + d, 3)); subs.append(sub); t += d + GAP
    dur = round(t - GAP + TAIL, 3)
    plan.append(dict(scene=si, dur=dur, cues=cues, ends=ends))
    page = f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class="stage">
<div class="bgl"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="grid"></div></div>
<div class="top"><span class="lab">{label}</span><span>EE / Power Systems · 2026 美国初级岗位</span></div>
<div class="main">{body}</div><div class="prog"><i></i></div><div class="subt"></div></div>
<script>window.CUES={json.dumps(cues)};window.ENDS={json.dumps(ends)};window.SUBS={json.dumps(subs, ensure_ascii=False)};
window.DUR={dur};window.T0={si*37};window.SEED={si+7};window.P0={si/total};window.P1={(si+1)/total};</script>
<script>{JS}</script></body></html>"""
    open(f'html/s{si:02d}.html', 'w').write(page)
    print(si, dur, flush=True)
json.dump(plan, open('plan.json', 'w'), indent=1)
print('sum', sum(p['dur'] for p in plan))
