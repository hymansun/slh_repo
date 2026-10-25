const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
const fr=JSON.parse(fs.readFileSync('frames.json'));const only=process.argv[2];
for(const f of fr){if(only&&!only.split(',').includes(String(f.k)))continue;
const n=String(f.k).padStart(3,'0');await p.goto('file://'+process.cwd()+'/frames/f'+n+'.html');await p.screenshot({path:'frames/f'+n+'.png'});}
await b.close();})();
