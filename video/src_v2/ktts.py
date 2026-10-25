import sys, sherpa_onnx, soundfile as sf
import os; d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'models/kokoro-multi-lang-v1_1/')
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
  model=d+'model.onnx',voices=d+'voices.bin',tokens=d+'tokens.txt',data_dir=d+'espeak-ng-data',dict_dir=d+'dict',
  lexicon=d+'lexicon-us-en.txt,'+d+'lexicon-zh.txt'),num_threads=8),
  rule_fsts=f'{d}phone-zh.fst,{d}date-zh.fst,{d}number-zh.fst',max_num_sentences=1)
tts=sherpa_onnx.OfflineTts(cfg)
SID=int(__import__('os').environ.get('SID','3'))
def say(text,out,speed=1.0,sid=None):
    a=tts.generate(text,sid=SID if sid is None else sid,speed=speed); sf.write(out,a.samples,a.sample_rate); return a.sample_rate
if __name__=='__main__':
    print(tts.num_speakers)
    mkdir=__import__('os').makedirs('voices',exist_ok=True)
    for s in [int(x) for x in sys.argv[1].split(',')]:
        say('你可能听说过，美国电网正在大规模扩建，到处都在喊缺人。但对于刚毕业的EE学生来说，工作真的好找吗？',f'voices/v{s}.wav',sid=s)
