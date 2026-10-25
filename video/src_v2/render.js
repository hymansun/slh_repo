// 逐帧 seek + 截图，JPEG 管道送入 ffmpeg，每个场景一个无声视频
const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
const FPS=30, W=+process.env.WORKERS||4;
const plan=JSON.parse(fs.readFileSync('plan.json'));fs.mkdirSync('clips',{recursive:true});
const only=process.argv[2]?process.argv[2].split(',').map(Number):null;
const queue=plan.filter(s=>!only||only.includes(s.scene));
async function renderScene(b,s){
  const n=String(s.scene).padStart(2,'0');const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+process.cwd()+'/html/s'+n+'.html');
  const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','clips/s'+n+'.mp4']);
  const N=Math.round(s.dur*FPS);
  for(let i=0;i<N;i++){await p.evaluate(t=>seek(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:92});
    if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
  ff.stdin.end();await new Promise(r=>ff.on('close',r));await p.close();console.log('done',n,N);
}
(async()=>{const b=await chromium.launch();
  await Promise.all(Array.from({length:W},async()=>{while(queue.length)await renderScene(b,queue.shift());}));
  await b.close();})();
