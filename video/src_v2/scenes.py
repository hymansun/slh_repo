# 口播版分镜。每个场景: (标签, HTML, [句子])
# 句子: 字幕文本，或 (字幕文本, 朗读文本)。含阿拉伯数字的句子必须给出朗读文本。
# HTML 动画约定:
#   data-s="n"      第 n 句开始时出现（默认 0）；data-d="0.3" 额外延迟秒数
#   class a-up / a-left / a-right / a-pop / a-fade / a-zoom   入场方式
#   class grow + style="--w:66%"   条形从 0 生长到目标宽度
#   class count + data-to="9.9" data-dec="1" data-pre="+" data-suf="%"   数字滚动
#   class ring + data-to="90"   SVG 环形进度
#   class mark  第 data-s 句时出现荧光笔高亮

S = []

S.append(("", """
<div class="hero">
  <div class="a-fade kicker">2026 · 美国 EE 初级岗位调研</div>
  <div class="a-zoom q1">电网<span class="hl-am">缺人</span></div>
  <div class="a-pop neq" data-s="1">≠</div>
  <div class="a-up q2" data-s="1">应届生<span class="hl-g">好找工作</span>？</div>
  <div class="srcs">
    <span class="a-up" data-s="3">BLS 劳工统计局</span><span class="a-up" data-s="3" data-d="0.15">纽约联储</span>
    <span class="a-up" data-s="3" data-d="0.3">NACE</span><span class="a-up" data-s="3" data-d="0.45">SHRM / Lightcast</span>
    <span class="a-up" data-s="3" data-d="0.6">真实招聘原文</span>
  </div>
</div>""", [
    "美国电网正在大规模扩建，到处都在喊缺人。",
    ("但如果你是一名刚毕业的EE学生，工作真的好找吗？", "但如果你是一名刚毕业的 e e 学生，工作真的好找吗？"),
    ("这期视频，我们用一份2026年的调研报告，把这个问题讲清楚。", "这期视频，我们用一份二零二六年的调研报告，把这个问题讲清楚。"),
    ("数据来自劳工统计局、纽约联储、NACE，还有一批真实的企业招聘原文。", "数据来自劳工统计局、纽约联储、n a c e，还有一批真实的企业招聘原文。"),
]))

S.append(("01 三个信号", """
<h2 class="a-left">先说结论：三个信号</h2>
<div class="cards3">
  <div class="a-up card up" data-s="1"><div class="ic">▲</div><div class="num"><span class="count" data-to="9.9" data-dec="1" data-pre="+" data-suf="%" data-s="1">0</span></div><div class="lbl">工程类招聘广告 · 同比</div><p>工程岗位在回暖</p></div>
  <div class="a-up card warn" data-s="2"><div class="ic">!</div><div class="num"><span class="count" data-to="42" data-suf="%" data-s="2" data-d="0.8">0</span></div><div class="lbl">近期毕业生就业不足率<br>（失业率 5.6%）</div><p>应届生依然紧张</p></div>
  <div class="a-up card acc" data-s="3"><div class="ic">★</div><div class="num">要熟手</div><div class="lbl">不一定缺所有新人</div><p>能直接上手的人最抢手</p></div>
</div>""", [
    "先说结论，有三个信号值得注意。",
    ("第一个是好消息：工程类招聘广告，一年里涨了9.9%。", "第一个是好消息：工程类招聘广告，一年里涨了百分之九点九。"),
    ("第二个就没那么乐观：近期毕业生失业率5.6%，而从事着不需要大学学历工作的，竟然有42%。",
     "第二个就没那么乐观：近期毕业生失业率百分之五点六，而从事着不需要大学学历工作的，竟然有百分之四十二。"),
    "第三个最关键：电力行业缺的，其实是能直接上手的人，而不是所有新人。",
]))

S.append(("02 十年预测", """
<h2 class="a-left">长期看：十年增长明显高于平均</h2>
<div class="bls">
  <div class="a-up blsrow" data-s="1"><div class="who">电气工程师</div>
    <div class="track"><i class="grow g1" style="--w:90%" data-s="1" data-d="0.3"></i><span class="tag">2035 · 21.95万</span></div>
    <div class="big g"><span class="count" data-to="9.9" data-dec="1" data-pre="+" data-suf="%" data-s="1" data-d="0.3">0</span></div></div>
  <div class="a-up blsrow" data-s="2"><div class="who">电子工程师</div>
    <div class="track"><i class="grow g2" style="--w:34%" data-s="2" data-d="0.2"></i><span class="tag">2035 · 10.18万</span></div>
    <div class="big ac"><span class="count" data-to="3.7" data-dec="1" data-pre="+" data-suf="%" data-s="2" data-d="0.2">0</span></div></div>
  <div class="a-pop salary" data-s="2" data-d="1.2">中位年薪 <b>$<span class="count" data-to="120630" data-sep="1" data-s="2" data-d="1.2">0</span></b> / <b>$<span class="count" data-to="130220" data-sep="1" data-s="2" data-d="1.4">0</span></b></div>
</div>
<div class="a-right callout" data-s="3"><b>每年约 16,300 个空缺</b>　大多是退休、跳槽留下的位置 —— <span class="mark" data-s="3" data-d="1.5">不是专门给应届生的</span></div>
<div class="a-right callout warnc" data-s="4">BLS 没有单独统计 “电力系统工程师” → 看到 “暴涨 20%” <span class="mark" data-s="4" data-d="2">先打个问号</span></div>""", [
    "那长期来看呢？",
    ("劳工统计局预测，未来十年电气工程师会增长9.9%，到2035年接近22万人。", "劳工统计局预测，未来十年电气工程师会增长百分之九点九，到二零三五年接近二十二万人。"),
    ("电子工程师增长慢一些，是3.7%。不过两类工程师的中位年薪，都超过了12万美元。", "电子工程师增长慢一些，是百分之三点七。不过两类工程师的中位年薪，都超过了十二万美元。"),
    ("但这里有个坑：每年约1万6千个空缺，大部分是退休和跳槽留下的，可不是专门给应届生的。", "但这里有个坑：每年约一万六千个空缺，大部分是退休和跳槽留下的，可不是专门给应届生的。"),
    ("而且劳工统计局根本没有单独统计电力系统工程师。下次看到电力工程师要暴涨20%这种说法，先打个问号。", "而且劳工统计局根本没有单独统计电力系统工程师。下次看到电力工程师要暴涨百分之二十这种说法，先打个问号。"),
]))

S.append(("03 今年的市场", """
<h2 class="a-left">今年的信号：有点矛盾</h2>
<div class="hbars">
  <div class="a-left hb" data-s="1"><span class="k">工程类招聘广告</span><div class="t"><i class="grow pos" style="--w:66%" data-s="1"></i></div><b class="g"><span class="count" data-to="9.9" data-dec="1" data-pre="+" data-suf="%" data-s="1">0</span></b></div>
  <div class="a-left hb" data-s="1" data-d="1.8"><span class="k">雇主计划招聘应届生</span><div class="t"><i class="grow pos" style="--w:37%" data-s="1" data-d="1.8"></i></div><b class="g"><span class="count" data-to="5.6" data-dec="1" data-pre="+" data-suf="%" data-s="1" data-d="1.8">0</span></b></div>
  <div class="a-left hb" data-s="2"><span class="k">Handshake 应届职位</span><div class="t"><i class="grow neg" style="--w:14%" data-s="2" data-d="0.6"></i></div><b class="rd"><span class="count" data-to="2" data-pre="−" data-suf="%" data-s="2" data-d="0.6">0</span></b></div>
</div>
<div class="split">
  <div class="a-up sp upc" data-s="3"><div class="arrow">↗</div><div><b>扩招</b>工程咨询 · 建筑施工</div></div>
  <div class="a-up sp dnc" data-s="3" data-d="1.6"><div class="arrow">↘</div><div><b>收缩</b>公用事业 · 电子制造</div></div>
</div>
<div class="a-zoom punch" data-s="4">同样学电力，<span class="mark" data-s="4" data-d="1">投哪类公司</span>，难度完全不一样</div>""", [
    "再看今年的招聘市场，信号其实挺矛盾。",
    ("工程类广告涨了9.9%，雇主也说今年要多招5.6%的应届生。", "工程类广告涨了百分之九点九，雇主也说今年要多招百分之五点六的应届生。"),
    ("可在求职平台Handshake上，应届职位反而少了2%。", "可在求职平台 handshake 上，应届职位反而少了百分之二。"),
    "更有意思的是行业分化：工程咨询和建筑施工在扩招，公用事业和电子制造却在收缩。",
    "所以同样学电力，投设计咨询公司和投大型电力公司，难度可能完全不一样。",
]))

S.append(("04 真实岗位", """
<h2 class="a-left">翻了一遍真实招聘原文</h2>
<div class="jobs">
  <div class="a-right job" data-s="2"><b>Shermco</b><span>New Grad Power Studies Engineer</span><em class="ok">零经验 · 提供培训</em></div>
  <div class="a-right job" data-s="2" data-d="0.4"><b>LNV</b><span>Entry Level Power Systems Engineer</span><em class="ok">零经验可申请</em></div>
  <div class="a-right job" data-s="3"><b>Black &amp; Veatch</b><span>Graduate Substation Engineer</span><em class="no">不提供签证担保</em></div>
  <div class="a-right job" data-s="3" data-d="0.4"><b>WSP</b><span>Entry Level Substation Engineer</span><em class="no">需永久工作授权</em></div>
  <div class="a-right job" data-s="4"><b>Black &amp; Veatch</b><span>Associate Power System Studies</span><em class="mid">要 1—4 年经验</em></div>
  <div class="a-right job" data-s="4" data-d="0.4"><b>SMUD</b><span>Electrical Engineer, Entry</span><em class="mid">≥1年 或 半年实习</em></div>
</div>
<div class="a-fade foot" data-s="1">2026年8—10月核查样本 · 非随机抽样</div>""", [
    "说了这么多宏观数据，来看点实际的。",
    ("我们翻了2026年8到10月的真实招聘原文。", "我们翻了二零二六年八到十月的真实招聘原文。"),
    ("好消息是，零经验岗位确实存在，比如Shermco和LNV，都明确欢迎新人。", "好消息是，零经验岗位确实存在，比如舍姆科和 l n v，都明确欢迎新人。"),
    "但不少岗位，要么不提供签证担保，要么要求永久工作授权。",
    "还有一些名字叫初级的岗位，实际要一到四年经验。",
]))

S.append(("05 两个案例", """
<h2 class="a-left">同叫 “初级”，门槛天差地别</h2>
<div class="vs">
  <div class="a-left vcard okc" data-s="1"><div class="vh">Shermco</div>
    <div class="quote">“不需要经验，我们来培训，<br>还配导师。”</div>
    <div class="chips2"><span>短路分析</span><span>Arc Flash</span><span>保护配合</span><span>ETAP</span></div>
    <div class="stamp ok a-pop" data-s="1" data-d="3">真·新人岗</div></div>
  <div class="a-pop vsdot" data-s="2">VS</div>
  <div class="a-right vcard amc" data-s="2"><div class="vh">SMUD · 加州</div>
    <div class="money">$<span class="count" data-to="110802" data-sep="1" data-s="2" data-d="0.5">0</span><small> – $146,786</small></div>
    <div class="req a-up" data-s="3">≥ 1 年相关经验<br>或 6 个月 SMUD 实习</div>
    <div class="stamp warn a-pop" data-s="3" data-d="2.5">名叫 Entry</div></div>
</div>""", [
    "举两个例子，你就明白了。",
    ("Shermco写得很直白：不需要经验，我们来培训，还配导师。这是真正的新人岗位。", "舍姆科写得很直白：不需要经验，我们来培训，还配导师。这是真正的新人岗位。"),
    ("再看加州的SMUD，初级工程师年薪11万到14.7万美元，看起来很诱人。", "再看加州的 s m u d，初级工程师年薪十一万到十四点七万美元，看起来很诱人。"),
    ("可仔细一看，要求至少一年相关经验，或者半年内部实习。名字叫Entry，门槛一点也不低。", "可仔细一看，要求至少一年相关经验，或者半年内部实习。名字叫 entry，门槛一点也不低。"),
]))

S.append(("06 电力电子", """
<h2 class="a-left">电力电子：产品岗 vs 研究岗</h2>
<div class="vs">
  <div class="a-left vcard okc" data-s="1"><div class="vh">Keysight · 电源硬件研发</div>
    <ul class="ul"><li>本科 / 硕士应届生</li><li>功率变换 · 反馈控制</li><li>原型调试 · 大功率测试</li><li>有导师带</li></ul>
    <div class="stamp ok a-pop" data-s="3" data-d="0.5">优先瞄准</div></div>
  <div class="a-pop vsdot" data-s="2">VS</div>
  <div class="a-right vcard rdc" data-s="2"><div class="vh">GM · 电力电子研究员</div>
    <ul class="ul"><li>要求<b class="rd">博士</b></li><li>强硬件研究能力</li><li>须 U.S. Person</li><li class="rd">不支持 OPT / STEM OPT</li></ul>
    <div class="stamp warn a-pop" data-s="3" data-d="0.8">门槛高得多</div></div>
</div>""", [
    "电力电子方向也一样，同叫初级，差别很大。",
    ("Keysight的电源研发岗，直接招本科和硕士应届生，做功率变换、控制和大功率测试。", "是德科技的电源研发岗，直接招本科和硕士应届生，做功率变换、控制和大功率测试。"),
    ("而通用汽车的电力电子研究岗，要博士学位，还要求美国人身份，不接受OPT。", "而通用汽车的电力电子研究岗，要博士学位，还要求美国人身份，不接受 o p t。"),
    "所以想尽快就业的硕士，优先瞄准产品设计岗，而不是研究岗。",
]))

S.append(("07 细分方向", """
<h2 class="a-left">哪些方向对新人更友好？</h2>
<div class="meter">
  <div class="a-left mrow" data-s="1"><span>电力系统分析 / 保护控制</span><div class="dots"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i></i></div><em class="g">优先关注</em></div>
  <div class="a-left mrow" data-s="1" data-d="0.5"><span>变电站 / 输配电设计</span><div class="dots"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i></i></div><em class="g">入口明确</em></div>
  <div class="a-left mrow" data-s="2"><span>电力电子硬件研发</span><div class="dots"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></div><em class="am">壁垒较高</em></div>
  <div class="a-left mrow" data-s="2" data-d="0.4"><span>工业控制 / 自动化</span><div class="dots"><i class="on"></i><i class="on"></i><i></i><i></i><i></i></div><em class="am">要现场经验</em></div>
  <div class="a-left mrow" data-s="2" data-d="0.8"><span>嵌入式 / 电子硬件</span><div class="dots"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></div><em>跨界备选</em></div>
</div>
<div class="kw">
  <span class="a-pop strike" data-s="3">Electrical Engineer</span>
  <span class="a-pop" data-s="4">Power System Studies</span><span class="a-pop" data-s="4" data-d="0.5">Protection &amp; Control</span>
  <span class="a-pop" data-s="4" data-d="1">Interconnection</span><span class="a-pop" data-s="4" data-d="1.5">Commissioning</span><span class="a-pop" data-s="4" data-d="2">Distribution Planning</span>
</div>""", [
    "那么，哪些细分方向对新人更友好？",
    "电力系统分析、保护控制，还有变电站设计，入口相对明确。",
    "电力电子研发和工业控制门槛更高，嵌入式可以作为跨界的备选。",
    ("还有个求职小技巧：别只搜Electrical Engineer。", "还有个求职小技巧：别只搜 electrical engineer。"),
    ("试试这些关键词：System Studies、Protection and Control、Interconnection、Commissioning，你会发现多出很多机会。",
     "试试这些关键词：system studies，protection and control，interconnection，commissioning，你会发现多出很多机会。"),
]))

S.append(("08 核心矛盾", """
<h2 class="a-left">既然缺人，为什么新人还难？</h2>
<div class="duo">
  <div class="a-up dcard" data-s="1"><div class="huge g">+<span class="count" data-to="17900" data-sep="1" data-s="1" data-d="0.3">0</span></div><div class="lbl">2025 年美国输配电行业新增就业</div></div>
  <div class="a-up dcard" data-s="2"><svg viewBox="0 0 200 200" class="donut"><circle cx="100" cy="100" r="80" class="bg"/><circle cx="100" cy="100" r="80" class="ring fg" data-to="90" data-s="2" data-d="0.8"/></svg>
    <div class="dn am"><span class="count" data-to="90" data-suf="%" data-s="2" data-d="0.8">0</span></div><div class="lbl">能源人才缺口集中在技术工种<br><small>GE Vernova 模型估计</small></div></div>
</div>
<div class="a-zoom punch" data-s="3">缺几十万电网人才 <span class="neq2">≠</span> 缺几十万 EE 硕士</div>
<div class="chips">
  <span class="a-pop" data-s="4" data-d="0.8">建模分析</span><span class="a-pop" data-s="4" data-d="1.3">看图纸</span><span class="a-pop" data-s="4" data-d="1.8">现场调试</span><span class="a-pop" data-s="4" data-d="2.3">做测试</span><span class="a-pop" data-s="4" data-d="2.8">客户沟通</span>
</div>""", [
    "回到开头的问题：既然缺人，为什么新人还难找工作？",
    "去年美国输配电行业，确实新增了大约一万八千个岗位。",
    ("但GE Vernova估计，未来能源人才缺口里，大约九成是电工、安装、调试这类技术工种。", "但 g e 维诺瓦估计，未来能源人才缺口里，大约九成是电工、安装、调试这类技术工种。"),
    "换句话说，缺几十万电网人才，不等于缺几十万电气工程硕士。",
    "雇主真正看重的，是你能不能交付：建模、看图、调试、做测试、跟客户沟通。",
]))

S.append(("09 AI 的影响", """
<h2 class="a-left">AI 会抢 EE 的饭碗吗？</h2>
<div class="vs">
  <div class="a-left vcard" data-s="1"><div class="vh ac">AI 能帮上忙</div><ul class="ul"><li>写计算报告</li><li>画简单的图</li><li>写仿真脚本</li></ul></div>
  <div class="a-pop vsdot" data-s="2">VS</div>
  <div class="a-right vcard okc" data-s="2"><div class="vh g">AI 绕不开</div><ul class="ul"><li>现场调试</li><li>排查故障</li><li>安全签字 · 法规责任</li></ul></div>
</div>
<div class="a-zoom punch" data-s="3">不是抢饭碗，而是<span class="mark" data-s="3" data-d="1.2">抬高门槛</span></div>""", [
    ("顺便聊聊AI。", "顺便聊聊 a i。"),
    ("写报告、画简单的图、写仿真脚本，这些活AI确实能帮上忙。", "写报告、画简单的图、写仿真脚本，这些活 a i 确实能帮上忙。"),
    "但现场调试、排查故障、安全签字，绕不开物理世界和法规责任。",
    ("所以目前看，AI不是在抢EE的饭碗，而是在抬高门槛：越有实战经验，越吃香。", "所以目前看，a i 不是在抢 e e 的饭碗，而是在抬高门槛：越有实战经验，越吃香。"),
]))

S.append(("10 说说钱", """
<h2 class="a-left">EE vs CS：近期毕业生</h2>
<div class="cmp">
  <div class="a-up crow" data-s="1"><span class="k">失业率</span><div class="pair">
    <div><i class="grow ee" style="--w:30%" data-s="1" data-d="0.5"></i><b>EE <span class="count" data-to="3.2" data-dec="1" data-suf="%" data-s="1" data-d="0.5">0</span></b></div>
    <div><i class="grow cs" style="--w:66%" data-s="1" data-d="0.9"></i><b>CS <span class="count" data-to="7.0" data-dec="1" data-suf="%" data-s="1" data-d="0.9">0</span></b></div></div></div>
  <div class="a-up crow" data-s="2"><span class="k">早期年薪中位数</span><div class="pair">
    <div><i class="grow ee" style="--w:77%" data-s="2" data-d="0.5"></i><b>EE $<span class="count" data-to="82000" data-sep="1" data-s="2" data-d="0.5">0</span></b></div>
    <div><i class="grow cs" style="--w:82%" data-s="2" data-d="0.9"></i><b>CS $<span class="count" data-to="87000" data-sep="1" data-s="2" data-d="0.9">0</span></b></div></div></div>
</div>
<div class="a-right callout warnc" data-s="3">$120,630 是整个职业的中位数 —— <span class="mark" data-s="3" data-d="1.5">不是毕业生的起薪</span></div>
<div class="a-fade foot" data-s="1">纽约联储按专业统计 · 2024 ACS 样本 · 22—27 岁</div>""", [
    "再来说说钱。",
    ("纽约联储的数据显示，EE毕业生失业率只有3.2%，不到计算机专业的一半。", "纽约联储的数据显示，e e 毕业生失业率只有百分之三点二，不到计算机专业的一半。"),
    ("但起薪中位数大约8万2，反而比CS的8万7略低。", "但起薪中位数大约八万二，反而比 c s 的八万七略低。"),
    ("所以别被12万的中位薪资迷惑，那是整个职业的数字，不是毕业生的。", "所以别被十二万的中位薪资迷惑，那是整个职业的数字，不是毕业生的。"),
]))

S.append(("11 签证", """
<h2 class="a-left">对留学生：签证可能比岗位数量更重要</h2>
<div class="locks">
  <div class="a-up lk" data-s="1"><div class="li">✕</div><b>WSP</b><span>永久工作授权</span></div>
  <div class="a-up lk" data-s="1" data-d="1.2"><div class="li">✕</div><b>Black &amp; Veatch</b><span>不提供签证担保</span></div>
  <div class="a-up lk" data-s="1" data-d="2.6"><div class="li">✕</div><b>GM 研究岗</b><span>不支持 OPT / H-1B</span></div>
</div>
<div class="gates">
  <div class="a-left gate" data-s="2" data-d="0.8"><i>1</i>能用 OPT 合法工作</div><div class="a-fade ga" data-s="2" data-d="1.6">→</div>
  <div class="a-left gate" data-s="2" data-d="2.4"><i>2</i>公司不用马上办 H-1B</div><div class="a-fade ga" data-s="2" data-d="3.6">→</div>
  <div class="a-left gate" data-s="2" data-d="4.4"><i>3</i>公司愿意长期支持签证</div>
</div>
<div class="a-right callout warnc" data-s="3">招聘网站的 “Supports H-1B” 标签别全信 —— <span class="mark" data-s="3" data-d="1.8">以招聘原文为准</span></div>""", [
    "接下来这一点，对留学生来说可能最重要：签证。",
    ("WSP要永久工作授权，Black and Veatch不提供担保，通用汽车直接写明不支持OPT和H1B。", "w s p 要永久工作授权，博莱克威奇不提供担保，通用汽车直接写明不支持 o p t 和 h 一 b。"),
    ("要分清三件事：能用OPT合法工作，公司不用马上办H1B，公司愿意长期支持签证。这是三道不同的门。", "要分清三件事：能用 o p t 合法工作，公司不用马上办 h 一 b，公司愿意长期支持签证。这是三道不同的门。"),
    ("还有，招聘网站上支持H1B的标签别全信，一切以招聘原文为准。", "还有，招聘网站上支持 h 一 b 的标签别全信，一切以招聘原文为准。"),
]))

S.append(("12 怎么选", """
<h2 class="a-left">那到底该怎么选？</h2>
<div class="podium">
  <div class="a-up pd p2" data-s="1" data-d="2.4"><div class="pt">电力系统分析<br>保护控制</div><div class="pb">2</div></div>
  <div class="a-up pd p1" data-s="1"><div class="pt">电力电子<br>+ 储能 / 电网</div><div class="pb">1</div></div>
  <div class="a-up pd p3" data-s="1" data-d="4.2"><div class="pt">嵌入式<br>硬件系统</div><div class="pb">3</div></div>
</div>
<div class="chain">
  <div class="a-pop step" data-s="2">功率电子 + 控制<span>DC-DC · 逆变器 · PWM</span></div><div class="a-fade arr" data-s="3">→</div>
  <div class="a-pop step" data-s="3" data-d="0.3">仿真 + 硬件实现<span>PLECS · PCB · MCU</span></div><div class="a-fade arr" data-s="3" data-d="2">→</div>
  <div class="a-pop step" data-s="3" data-d="2.3">真实应用<span>储能 · 充电 · 并网</span></div>
</div>
<div class="a-right callout warnc" data-s="4">只做电池寿命预测算法 <span class="lt">&lt;</span> <span class="mark" data-s="4" data-d="2">亲手做过一块变换器</span></div>""", [
    "那到底该怎么选？",
    "报告的建议是：优先电力电子，结合储能和电网应用；电力系统分析与保护控制作为第二选择；嵌入式作为补充。",
    "读研期间，可以沿着这条线积累：先打牢功率电子和控制，",
    ("再做仿真、PCB和单片机的硬件实现，最后落到储能、充电、并网这些真实应用上。", "再做仿真、p c b 和单片机的硬件实现，最后落到储能、充电、并网这些真实应用上。"),
    "一个提醒：只做电池寿命预测这类算法项目，说服力不如亲手做过一块变换器。",
]))

S.append(("13 总结", """
<h2 class="a-left">三句话总结</h2>
<div class="checks">
  <div class="a-left ck" data-s="1"><i class="tick a-pop" data-s="1" data-d="0.6">✓</i><b>首要目标</b>Power Electronics Engineer I / New Grad</div>
  <div class="a-left ck" data-s="2"><i class="tick a-pop" data-s="2" data-d="0.6">✓</i><b>平行备选</b>Power System Studies Engineer I</div>
  <div class="a-left ck" data-s="3"><i class="tick a-pop" data-s="3" data-d="0.6">✓</i><b>投递之前</b>先筛签证条件</div>
</div>
<div class="a-zoom end" data-s="4">去找你<span class="mark" data-s="4" data-d="2.5">真正能申请</span>的岗位</div>""", [
    "最后，三句话总结。",
    "首要目标：电力电子新人岗。",
    "平行备选：电力系统研究工程师。",
    "投简历之前，先筛签证条件。",
    "与其关心行业缺多少人，不如直接去找那些你真正能申请的岗位。我们下期见。",
]))
