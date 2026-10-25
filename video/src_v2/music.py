# 程序化合成背景音乐：I–V–vi–IV 轻快科技感，pad + 琶音 + 贝斯 + 轻鼓，带混响
import sys, numpy as np, soundfile as sf
from scipy import signal
SR = 48000; BPM = 92; BEAT = 60 / BPM; BAR = 4 * BEAT
L = float(sys.argv[1]) if len(sys.argv) > 1 else 60.0
nbars = int(L / BAR) + 2
N = int((nbars * BAR + 3) * SR)
rng = np.random.default_rng(3)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
# C G Am F，每和弦一小节；后半程换成 Am F C G 变化
PROG_A = [[48, 55, 60, 64, 67], [43, 55, 59, 62, 67], [45, 57, 60, 64, 69], [41, 53, 57, 60, 65]]
PROG_B = [[45, 57, 60, 64, 69], [41, 53, 57, 60, 65], [48, 55, 60, 64, 67], [43, 55, 59, 62, 67]]
pad = np.zeros((N, 2)); arp = np.zeros((N, 2)); bass = np.zeros(N); drums = np.zeros(N)
def tone(f, dur, harm=((1, 1),), det=0.0):
    t = np.arange(int(dur * SR)) / SR
    return sum(a * np.sin(2 * np.pi * f * h * (1 + det) * t + rng.uniform(0, 6)) for h, a in harm)
for b in range(nbars):
    t0 = b * BAR; i0 = int(t0 * SR)
    sect = (b // 16) % 2; chord = (PROG_B if sect else PROG_A)[b % 4]
    # pad：每小节一个和弦，带交叉淡变
    dur = BAR + 1.2; n = int(dur * SR); env = np.minimum(1, np.arange(n) / (0.7 * SR)) * np.minimum(1, (n - np.arange(n)) / (1.2 * SR))
    for k, m in enumerate(chord[1:]):
        h = ((1, 1), (2, .35), (3, .18), (4, .08))
        for side, det in ((0, -0.0025), (1, 0.0025)):
            seg = tone(hz(m), dur, h, det) * env * 0.05
            e = min(N, i0 + n); pad[i0:e, side] += seg[:e - i0]
    # 贝斯：1、3 拍
    if b >= 4:
        for beat in (0, 2, 2.5 if b % 2 else None):
            if beat is None: continue
            s = int((t0 + beat * BEAT) * SR); n = int(0.9 * SR); t = np.arange(n) / SR
            seg = (np.sin(2 * np.pi * hz(chord[0] - 12 if chord[0] > 44 else chord[0]) * t) + .25 * np.sin(4 * np.pi * hz(chord[0]) * t)) * np.exp(-t * 3.5) * np.minimum(1, t / .01) * 0.22
            e = min(N, s + n); bass[s:e] += seg[:e - s]
    # 琶音：8 分音符
    if b >= 8:
        pat = [1, 2, 3, 4, 3, 2, 4, 3] if sect == 0 else [2, 3, 4, 3, 1, 3, 4, 2]
        for k in range(8):
            m = chord[pat[k]] + 12; s = int((t0 + k * BEAT / 2) * SR); n = int(0.5 * SR); t = np.arange(n) / SR
            seg = (np.sin(2 * np.pi * hz(m) * t) + .3 * np.sin(4 * np.pi * hz(m) * t) + .08 * np.sin(6 * np.pi * hz(m) * t)) * np.exp(-t * 7) * np.minimum(1, t / .004) * 0.07
            pan = 0.5 + 0.35 * np.sin(k * 1.3); e = min(N, s + n)
            arp[s:e, 0] += seg[:e - s] * (1 - pan); arp[s:e, 1] += seg[:e - s] * pan
    # 鼓：第 4 小节起；每 16 小节最后 2 小节留白
    if b >= 4 and (b % 16) < 14:
        for beat in range(4):
            s = int((t0 + beat * BEAT) * SR)
            if beat in (0, 2):  # kick
                n = int(.3 * SR); t = np.arange(n) / SR; f = 45 + 75 * np.exp(-t * 30)
                seg = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 0.35
                e = min(N, s + n); drums[s:e] += seg[:e - s]
            if beat in (1, 3) and b >= 8:  # 轻拍
                n = int(.2 * SR); t = np.arange(n) / SR
                seg = signal.lfilter(*signal.butter(2, [900, 4000], 'band', fs=SR), rng.standard_normal(n)) * np.exp(-t * 22) * 0.12
                e = min(N, s + n); drums[s:e] += seg[:e - s]
            for off in (0.5,):  # hat
                s2 = int((t0 + (beat + off) * BEAT) * SR); n = int(.06 * SR); t = np.arange(n) / SR
                seg = signal.lfilter(*signal.butter(2, 7000, 'high', fs=SR), rng.standard_normal(n)) * np.exp(-t * 60) * 0.05
                e = min(N, s2 + n); drums[s2:e] += seg[:e - s2]
pad = signal.lfilter(*signal.butter(2, 2200, 'low', fs=SR), pad, axis=0)
# 混响（合成指数衰减脉冲响应）
irn = int(2.4 * SR); t = np.arange(irn) / SR
ir = rng.standard_normal((irn, 2)) * np.exp(-t * 2.6)[:, None]; ir /= np.sqrt((ir ** 2).sum(0))
wet_in = pad * 0.8 + arp
wet = np.stack([signal.oaconvolve(wet_in[:, c], ir[:, c])[:N] for c in range(2)], 1)
mix = pad + arp + 0.45 * wet + bass[:, None] + drums[:, None] * np.array([1, 1])
mix = signal.lfilter(*signal.butter(1, 35, 'high', fs=SR), mix, axis=0)
mix = mix[:int(L * SR)]
fi, fo = int(2 * SR), int(4 * SR)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]; mix[-fo:] *= np.linspace(1, 0, fo)[:, None]
mix /= np.abs(mix).max() * 1.12
sf.write('music.wav', mix.astype(np.float32), SR)
print('music', L)
