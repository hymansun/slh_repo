# 合成：场景间转场 + 人声逐句响度统一 + 背景音乐自动避让 + 整体响度标准化
import json, subprocess, numpy as np, soundfile as sf
from scipy import signal
plan = json.load(open('plan.json')); XF = 0.8; SR = 48000
TRANS = ['fade', 'smoothleft', 'circleopen', 'slideup', 'smoothright', 'fadeblack', 'radial',
         'wipeleft', 'smoothup', 'dissolve', 'circlecrop', 'slideleft', 'fadeblack']
offs, acc = [], 0.0
for i, p in enumerate(plan):
    offs.append(acc - i * XF if i else 0.0); acc += p['dur']
offs = [sum(p['dur'] for p in plan[:i]) - i * XF for i in range(len(plan))]
TOTAL = offs[-1] + plan[-1]['dur']
# 1) 视频转场
ins, fc, last = [], [], '0:v'
for i, p in enumerate(plan): ins += ['-i', f'clips/s{i:02d}.mp4']
for i in range(1, len(plan)):
    out = f'v{i}'
    fc.append(f'[{last}][{i}:v]xfade=transition={TRANS[(i-1) % len(TRANS)]}:duration={XF}:offset={offs[i]:.3f}[{out}]'); last = out
fc.append(f'[{last}]fade=in:st=0:d=0.8,fade=out:st={TOTAL-1.5:.3f}:d=1.5,format=yuv420p[vout]')
import sys
AUDIO_ONLY = '--audio' in sys.argv
if not AUDIO_ONLY: subprocess.run(['ffmpeg', '-y', '-v', 'error', *ins, '-filter_complex', ';'.join(fc), '-map', '[vout]',
                '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-r', '30', 'video_only.mp4'], check=True)
print('video ok', TOTAL)
# 2) 人声：逐句统一响度后按时间轴摆放
voice = np.zeros(int((TOTAL + 1) * SR))
for i, p in enumerate(plan):
    for j, c in enumerate(p['cues']):
        x, sr = sf.read(f'audio/s{i:02d}_{j}.wav')
        x = signal.resample_poly(x, SR, sr)
        act = x[np.abs(x) > 0.02]; rms = np.sqrt((act ** 2).mean())
        x = x * (0.12 / rms)                       # 每句有效段统一到相同 RMS
        x = np.tanh(x * 1.6) / 1.6                 # 柔和限幅，压掉突出的峰
        s = int((offs[i] + c) * SR); voice[s:s + len(x)] += x
# 轻压缩：平滑包络，进一步抹平句内起伏
env = np.sqrt(signal.lfilter([1 - 0.999], [1, -0.999], voice ** 2)) + 1e-6
gain = np.clip((0.10 / env) ** 0.35, 0.6, 1.8); gain = signal.lfilter([0.002], [1, -0.998], gain)
voice *= gain
voice = signal.lfilter(*signal.butter(2, 80, 'high', fs=SR), voice)
# 3) 音乐 + 自动避让
subprocess.run(['python3', 'music.py', str(TOTAL + 0.5)], check=True)
mus, _ = sf.read('music.wav'); mus = mus[:len(voice)]
if len(mus) < len(voice): mus = np.pad(mus, ((0, len(voice) - len(mus)), (0, 0)))
talk = (signal.lfilter([1 - 0.9995], [1, -0.9995], np.abs(voice)) > 0.004).astype(float)
duck = signal.lfilter([1 - 0.99985], [1, -0.99985], talk)       # 约 0.15s 平滑
duck = np.clip(duck * 1.5, 0, 1)
mgain = 0.30 - 0.19 * duck                                    # 讲话时 ≈ -21dB，停顿时 ≈ -10dB
mix = voice[:, None] * 1.0 + mus * mgain[:, None]
sf.write('mix.wav', mix.astype(np.float32), SR)
if AUDIO_ONLY: sys.exit(0)
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', 'video_only.mp4', '-i', 'mix.wav',
                '-af', 'loudnorm=I=-16:LRA=7:TP=-1.5', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
                '-shortest', '-movflags', '+faststart', 'final_v2.mp4'], check=True)
print('done', TOTAL)
