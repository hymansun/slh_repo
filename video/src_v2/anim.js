// 确定性动画：seek(t) 把整页设置到时间 t 的状态，逐帧截图
const C = window.CUES, D = window.DUR, SUBS = window.SUBS, ENDS = window.ENDS;
const clamp = x => Math.max(0, Math.min(1, x));
const eo = x => 1 - Math.pow(1 - x, 3);
const eb = x => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
function startOf(el) { const s = +(el.dataset.s || 0), d = +(el.dataset.d || 0); return (s === 0 ? 0.25 : C[s]) + d; }
const ANIMS = [...document.querySelectorAll('[class*="a-"]')].filter(e => /\ba-(up|left|right|pop|fade|zoom)\b/.test(e.className));
const GROWS = [...document.querySelectorAll('.grow')], COUNTS = [...document.querySelectorAll('.count')];
const RINGS = [...document.querySelectorAll('.ring')], MARKS = [...document.querySelectorAll('.mark')];
// 背景粒子
const bgl = document.querySelector('.bgl'), PP = [];
let seed = window.SEED || 1; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
for (let i = 0; i < 26; i++) { const p = document.createElement('div'); p.className = 'pp'; bgl.appendChild(p);
  PP.push({ el: p, x: rnd() * 2300, y: rnd() * 1500, vx: (rnd() - .5) * 14, vy: -6 - rnd() * 14, s: .5 + rnd() * 1.2, ph: rnd() * 6 }); }
const o1 = document.querySelector('.o1'), o2 = document.querySelector('.o2'), o3 = document.querySelector('.o3');
const main = document.querySelector('.main'), sub = document.querySelector('.subt'), prog = document.querySelector('.prog i');
function fmt(v, el) { const dec = +(el.dataset.dec || 0); let s = v.toFixed(dec);
  if (el.dataset.sep) s = Math.round(v).toLocaleString('en-US'); return (el.dataset.pre || '') + s + (el.dataset.suf || ''); }
window.seek = function (t) {
  const T = t + (window.T0 || 0);
  o1.style.transform = `translate(${1250 + 120 * Math.sin(T * .11)}px,${-150 + 80 * Math.cos(T * .09)}px)`;
  o2.style.transform = `translate(${-100 + 140 * Math.cos(T * .08)}px,${700 + 90 * Math.sin(T * .1)}px)`;
  o3.style.transform = `translate(${700 + 200 * Math.sin(T * .06)}px,${300 + 120 * Math.sin(T * .07)}px)`;
  for (const p of PP) { const y = ((p.y + p.vy * T) % 1500 + 1500) % 1500, x = p.x + p.vx * T + 20 * Math.sin(T * .5 + p.ph);
    p.el.style.transform = `translate(${x}px,${y}px) scale(${p.s})`; p.el.style.opacity = .25 + .3 * Math.sin(T * .8 + p.ph) ** 2; }
  main.style.transform = `scale(${1 + 0.03 * eo(clamp(t / D))})`;
  prog.style.width = (window.P0 + (window.P1 - window.P0) * clamp(t / D)) * 100 + '%';
  for (const el of ANIMS) {
    const p = clamp((t - startOf(el)) / 0.7), e = eo(p), c = el.className; let tr = '', op = e;
    if (/\ba-up\b/.test(c)) tr = `translateY(${(1 - e) * 60}px)`;
    else if (/\ba-left\b/.test(c)) tr = `translateX(${(1 - e) * -90}px)`;
    else if (/\ba-right\b/.test(c)) tr = `translateX(${(1 - e) * 90}px)`;
    else if (/\ba-pop\b/.test(c)) { const b = p > 0 ? eb(p) : 0; tr = `scale(${0.3 + 0.7 * b})`; op = clamp(p * 2.5); if (/stamp/.test(c)) tr += ' rotate(-8deg)'; }
    else if (/\ba-zoom\b/.test(c)) tr = `scale(${1.25 - 0.25 * e})`;
    el.style.opacity = op; el.style.transform = tr;
    el.style.filter = (/\ba-zoom\b/.test(c) && p < 1) ? `blur(${(1 - e) * 8}px)` : '';
  }
  for (const el of GROWS) { const p = eo(clamp((t - startOf(el) - 0.2) / 1.3)); el.style.width = `calc(${el.style.getPropertyValue('--w')} * ${p})`; }
  for (const el of COUNTS) { const p = eo(clamp((t - startOf(el) - 0.2) / 1.4)); el.textContent = fmt(+el.dataset.to * p, el); }
  for (const el of RINGS) { const p = eo(clamp((t - startOf(el)) / 1.6)); el.style.strokeDashoffset = 502.65 * (1 - p * +el.dataset.to / 100); }
  for (const el of MARKS) { const p = eo(clamp((t - startOf(el)) / 0.6)); el.style.backgroundSize = `${p * 100}% 100%`; }
  // 字幕
  let k = -1; for (let i = 0; i < C.length; i++) if (t >= C[i] - 0.05 && t < ENDS[i] + 0.3) k = i;
  if (k < 0) { sub.textContent = ''; } else { sub.textContent = SUBS[k]; sub.style.opacity = clamp((t - C[k] + 0.05) / 0.2); }
};
window.seek(0);
