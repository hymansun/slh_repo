import json, subprocess, os
from tts import say
fr = json.load(open('frames.json')); os.makedirs('clips', exist_ok=True)
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
lst = []
for f in fr:
    k = f['k']; a = f'audio/a{k:03d}.wav'
    say(f['speak'], a)
    lead = 0.6 if f['first'] else 0.25
    D = lead + dur(a) + 0.45
    prev = f'frames/f{k-1:03d}.png' if k else None
    cur = f'frames/f{k:03d}.png'; out = f'clips/c{k:03d}.mp4'
    xd = 0.6 if f['first'] else 0.35
    if prev:
        vin = ['-loop','1','-t',f'{D}','-i',prev,'-loop','1','-t',f'{D}','-i',cur]
        vf = f'[0:v][1:v]xfade=transition={"fade" if f["first"] else "fade"}:duration={xd}:offset=0,format=yuv420p[v]'
    else:
        vin = ['-loop','1','-t',f'{D}','-i',cur]
        vf = f'[0:v]fade=in:st=0:d=0.8,format=yuv420p[v]'
    ai = len(vin)//6 if prev else 1
    cmd = ['ffmpeg','-y','-v','error',*vin,'-i',a,'-filter_complex',
           vf+f';[{2 if prev else 1}:a]adelay={int(lead*1000)}:all=1,apad,atrim=0:{D},aresample=44100[a]',
           '-map','[v]','-map','[a]','-r','30','-c:v','libx264','-preset','medium','-crf','20','-c:a','aac','-b:a','160k','-ac','2','-t',f'{D}',out]
    subprocess.run(cmd, check=True); lst.append(f"file '{out}'")
    print(k, round(D,1), flush=True)
open('list.txt','w').write('\n'.join(lst))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','list.txt','-c','copy','video_raw.mp4'],check=True)
T = dur('video_raw.mp4')
subprocess.run(['ffmpeg','-y','-v','error','-i','video_raw.mp4','-vf',f'fade=out:st={T-1.2}:d=1.2','-af',f'afade=out:st={T-1.2}:d=1.2',
                '-c:v','libx264','-crf','20','-preset','medium','-c:a','aac','-b:a','160k','-movflags','+faststart','final.mp4'],check=True)
print('total', T)
