import json, os, html, subprocess
from scenes import S
os.makedirs('frames', exist_ok=True); os.makedirs('audio', exist_ok=True)
CSS = open('style.css').read()
frames = []
total = len(S)
for si,(label, body, sents) in enumerate(S):
    for ji, sent in enumerate(sents):
        sub, rev = sent[0], sent[1]
        speak = sent[2] if len(sent) > 2 else sub
        k = len(frames)
        page = f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head>
<body><div class="stage">
<div class="top"><span class="lab">{label}</span><span class="brand">EE / Power Systems · 2026 美国初级岗位</span></div>
<div class="main">{body}</div>
<div class="prog"><i style="width:{(si+1)/total*100:.1f}%"></i></div>
<div class="subt">{html.escape(sub)}</div></div>
<script>document.querySelectorAll('.r').forEach((e,i)=>{{if(i>={rev})e.classList.add('hid')}});</script></body></html>"""
        open(f'frames/f{k:03d}.html','w').write(page)
        frames.append(dict(k=k, scene=si, first=(ji==0), speak=speak))
json.dump(frames, open('frames.json','w'), ensure_ascii=False, indent=1)
print(len(frames), 'frames')
