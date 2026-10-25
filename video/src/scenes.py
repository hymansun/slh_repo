# 每个场景: (标题标签, HTML主体, [(字幕, 显示到第几个元素, 朗读文本可选)])
# HTML中 class="r" 的元素按出现顺序编号，reveal=n 表示前 n 个可见

S = []

S.append(("", """
<div class="title-wrap">
  <div class="r kicker">2026 美国就业市场深度调研 · 视频解读</div>
  <h1 class="r big">美国电气工程与电力系统<br>初级岗位就业市场</h1>
  <div class="r sub">对象：0—2 年经验 · 应届本科 / 硕士 · 国际学生视角</div>
  <div class="r tags"><span>BLS</span><span>纽约联储</span><span>NACE</span><span>SHRM / Lightcast</span><span>企业招聘原文</span></div>
</div>""", [
    ("大家好，今天我们来解读一份美国电气工程就业市场的深度调研报告。", 2),
    ("研究对象是零到两年经验的工程师，以及应届本科生和硕士毕业生。", 3),
    ("报告综合了美国劳工统计局、纽约联储、NACE等数据，并逐条核查了企业真实招聘原文。", 4,
     "报告综合了美国劳工统计局、纽约联储、NACE等数据，并逐条核查了企业真实招聘原文。"),
]))

S.append(("01 核心结论", """
<h2>三个最值得关注的现象</h2>
<div class="cards3">
  <div class="r card up"><div class="num">+9.9%</div><div class="lbl">建筑与工程类招聘广告<br>12个月均值同比</div><p>工程岗位正在恢复增长</p></div>
  <div class="r card warn"><div class="num">5.6% / 42%</div><div class="lbl">22—27岁近期毕业生<br>失业率 / 就业不足率</div><p>应届生就业仍然紧张</p></div>
  <div class="r card acc"><div class="num">缺“熟手”</div><div class="lbl">不一定缺所有新人</div><p>部分“初级”岗仍要求1—4年经验、实习或限制签证</p></div>
</div>
<div class="r note">一句话：电力方向比纯软件更稳健，但行业需求增长 ≠ 初级岗位容易拿到</div>""", [
    ("先看核心结论。第一，工程岗位正在恢复增长，建筑与工程类招聘广告同比增长9.9%。", 1,
     "先看核心结论。第一，工程岗位正在恢复增长，建筑与工程类招聘广告同比增长百分之九点九。"),
    ("第二，应届生就业依然紧张，近期大学毕业生失业率约5.6%，就业不足率高达42%。", 2,
     "第二，应届生就业依然紧张，近期大学毕业生失业率约百分之五点六，就业不足率高达百分之四十二。"),
    ("第三，电力行业缺的是有技能的人，而不一定缺所有新人。", 3),
    ("所以，电力方向整体比纯软件更稳健，但行业需求增长，并不等于初级岗位容易拿到。", 4),
]))

S.append(("02 长期预测", """
<h2>BLS 十年预测：明显好于全美平均</h2>
<div class="two">
  <div class="r panel">
    <div class="ph">电气工程师</div>
    <div class="row"><span>2025 就业</span><b>19.97万</b></div>
    <div class="row"><span>2035 预测</span><b>21.95万</b></div>
    <div class="bar"><i style="width:99%"></i></div><div class="row"><span>十年增速</span><b class="g">+9.9%</b></div>
    <div class="row"><span>职业中位年薪</span><b>$120,630</b></div>
  </div>
  <div class="r panel">
    <div class="ph">电子工程师（不含计算机）</div>
    <div class="row"><span>2025 就业</span><b>9.82万</b></div>
    <div class="row"><span>2035 预测</span><b>10.18万</b></div>
    <div class="bar"><i style="width:37%"></i></div><div class="row"><span>十年增速</span><b class="g">+3.7%</b></div>
    <div class="row"><span>职业中位年薪</span><b>$130,220</b></div>
  </div>
</div>
<div class="r note">两类合计每年约 <b>16,300</b> 个空缺（含替补）—— 不是 16,300 个应届生职位</div>
<div class="r note warnline">⚠ BLS 没有单独的 “Power Systems Engineer” 预测序列，警惕把行业增长当成职业增长</div>""", [
    ("从长期看，美国劳工统计局预测，电气工程师未来十年增长9.9%，从约20万人增加到约22万人。", 1,
     "从长期看，美国劳工统计局预测，电气工程师未来十年增长百分之九点九，从约二十万人增加到约二十二万人。"),
    ("电子工程师增长3.7%，两类职业的中位年薪都在12万美元以上。", 2,
     "电子工程师增长百分之三点七，两类职业的中位年薪都在十二万美元以上。"),
    ("两者合计每年约有一万六千三百个岗位空缺，但这包括替补需求，并不是一万六千多个应届生职位。", 3),
    ("还要注意，劳工统计局并没有单独预测电力系统工程师，如果有人说这个职业要增长百分之二十，需要先核查口径。", 4),
]))

S.append(("03 近期招聘", """
<h2>工程类回暖，但应届生市场没有同步转好</h2>
<div class="bars">
  <div class="r hb"><span class="k">建筑与工程类招聘广告</span><div class="t"><i class="pos" style="width:66%"></i></div><b class="g">+9.9%</b></div>
  <div class="r hb"><span class="k">计算机与数学职业招聘广告</span><div class="t"><i class="pos" style="width:23%"></i></div><b class="g">+3.4%</b></div>
  <div class="r hb"><span class="k">NACE 2026届预期招聘量</span><div class="t"><i class="pos" style="width:37%"></i></div><b class="g">+5.6%</b></div>
  <div class="r hb"><span class="k">Handshake 应届职位广告</span><div class="t"><i class="neg" style="width:13%"></i></div><b class="rd">−2%</b></div>
</div>
<div class="src">来源与统计对象不同，不可直接相加或比较</div>
<div class="two small">
  <div class="r panel"><div class="ph g">校招意向上升</div>工程技术服务 · 建筑施工</div>
  <div class="r panel"><div class="ph rd">校招意向下降</div>公用事业 · 计算机和电子制造</div>
</div>""", [
    ("再看近期信号。工程类招聘广告增长9.9%，高于计算机与数学类的3.4%。", 2,
     "再看近期信号。工程类招聘广告增长百分之九点九，高于计算机与数学类的百分之三点四。"),
    ("NACE调查显示2026届预期招聘量增长5.6%，但Handshake平台上的应届职位广告反而下降了2%。", 4,
     "NACE调查显示二零二六届预期招聘量增长百分之五点六，但Handshake平台上的应届职位广告反而下降了百分之二。"),
    ("更有价值的发现是行业分化：工程技术服务和建筑施工的校招意向上升，", 5),
    ("而公用事业和电子制造的校招意向下降。也就是说，去设计咨询公司求职和去大型电力公司求职，面对的市场可能很不一样。", 6),
]))

S.append(("04 真实岗位", """
<h2>真实初级岗位：零经验岗位确实存在</h2>
<table>
<tr><th>企业与职位</th><th>经验要求</th><th>签证</th></tr>
<tr class="r"><td>Shermco · New Grad Power Studies Engineer</td><td class="g">零经验，提供培训</td><td>未明确</td></tr>
<tr class="r"><td>LNV · Entry Level Power Systems Engineer</td><td class="g">零经验可申请</td><td>未明确</td></tr>
<tr class="r"><td>Black &amp; Veatch · Graduate Substation Engineer</td><td class="g">面向毕业生</td><td class="rd">不提供担保</td></tr>
<tr class="r"><td>WSP · Entry Level Substation Electrical Engineer</td><td>0—1 年</td><td class="rd">需永久工作授权</td></tr>
<tr class="r"><td>Black &amp; Veatch · Associate Power System Studies</td><td class="am">1—4 年</td><td class="rd">不提供担保</td></tr>
<tr class="r"><td>SMUD · Electrical Engineer, Entry</td><td class="am">≥1年 或 6个月实习</td><td>未确认</td></tr>
</table>
<div class="src">2026年8—10月核查样本，非随机抽样；“未明确”不代表提供签证支持</div>""", [
    ("报告最重要的证据，是2026年8到10月的真实招聘原文。", 0, "报告最重要的证据，是二零二六年八到十月的真实招聘原文。"),
    ("Shermco和LNV的电力系统岗位明确接受零经验，Shermco还提供培训。", 2),
    ("Black and Veatch和WSP有面向毕业生的变电站岗位，但都不提供签证担保，或要求永久工作授权。", 4),
    ("而有些名为初级的岗位，实际要求一到四年经验，或者至少半年实习。", 6),
]))

S.append(("05 两个案例", """
<h2>同叫“初级”，门槛天差地别</h2>
<div class="two">
  <div class="r panel big-p">
    <div class="ph g">案例A · Shermco</div>
    <div class="quote">“不需要电力系统研究经验，提供系统培训与导师辅导”</div>
    <ul><li>短路分析 · Arc Flash · 保护配合</li><li>单线图阅读</li><li>逐步学习 ETAP / SKM / ASPEN</li></ul>
    <div class="tagline g">真正的初级人才培养岗</div>
  </div>
  <div class="r panel big-p">
    <div class="ph am">案例B · SMUD（加州）</div>
    <div class="num2">$110,802–$146,786</div>
    <ul><li>电动车充电 · 分布式能源接入</li><li>最低：≥1年相关经验 或 6个月SMUD实习</li><li>与更高一级职位共用一个名额</li></ul>
    <div class="tagline am">名称是 Entry，门槛却不低</div>
  </div>
</div>""", [
    ("来看两个对比鲜明的案例。Shermco明确写着不需要电力系统研究经验，公司提供培训和导师辅导。", 1),
    ("工作内容包括短路分析、电弧闪络、保护配合，以及逐步学习ETAP等工业软件。这是真正的新人培养岗位。", 1,
     "工作内容包括短路分析、电弧闪络、保护配合，以及逐步学习E TAP等工业软件。这是真正的新人培养岗位。"),
    ("而加州SMUD的初级岗位，年薪高达11万到14.7万美元，", 2, "而加州SMUD的初级岗位，年薪高达十一万到十四点七万美元，"),
    ("但要求至少一年相关经验或半年内部实习，还和高一级职位共用名额。名称里的Entry，并不等于没有经历就能入职。", 2),
]))

S.append(("06 电力电子", """
<h2>电力电子：有真实校招，但研发岗位分层明显</h2>
<div class="two">
  <div class="r panel big-p">
    <div class="ph g">Keysight · Power Electronics Hardware R&amp;D</div>
    <div class="meta">新泽西 · 2026年9月 · BS/MS 应届生 · 有导师</div>
    <ul><li>功率变换拓扑、反馈控制、仿真</li><li>FPGA、原型调试、大功率测试</li><li>要求：电力电子与控制课程、模拟电路</li></ul>
    <div class="tagline g">产品设计岗 → EE硕士的直接目标</div>
  </div>
  <div class="r panel big-p">
    <div class="ph rd">GM · Power Electronics Researcher</div>
    <div class="meta">密歇根 · 2026年10月12日</div>
    <ul><li>逆变器、变换器、微电网、储能</li><li>要求：相关领域<b>博士</b> + 强硬件实验能力</li><li>要求 U.S. Person，不支持 OPT / STEM OPT</li></ul>
    <div class="tagline rd">前沿研究岗 → 门槛高得多</div>
  </div>
</div>""", [
    ("电力电子方向同样有真实校招。Keysight的电源硬件研发岗直接面向本科和硕士应届生，", 1),
    ("工作涉及功率变换拓扑、反馈控制、仿真和大功率测试，并配有导师指导。", 1),
    ("而通用汽车的电力电子研究岗，要求博士学位，还明确要求美国人身份，不支持OPT。", 2,
     "而通用汽车的电力电子研究岗，要求博士学位，还明确要求美国人身份，不支持O P T。"),
    ("所以要区分产品设计工程师和研究科学家，对想尽快就业的EE硕士来说，前者通常是更直接的目标。", 2,
     "所以要区分产品设计工程师和研究科学家，对想尽快就业的E E硕士来说，前者通常是更直接的目标。"),
]))

S.append(("07 细分方向", """
<h2>哪些细分方向对新人更开放？</h2>
<table>
<tr><th>细分职业</th><th>主要进入门槛</th><th>综合判断</th></tr>
<tr class="r"><td>电力系统分析、保护与控制</td><td>三相系统、潮流、短路、继保、ETAP</td><td class="g">较值得优先关注</td></tr>
<tr class="r"><td>变电站、输配电设计</td><td>单线图、设计规范、AutoCAD</td><td class="g">入口较明确</td></tr>
<tr class="r"><td>电力电子硬件研发</td><td>变换器、控制、仿真、PCB、调试</td><td class="am">技术壁垒较高</td></tr>
<tr class="r"><td>工业控制、自动化</td><td>PLC、HMI、驱动、现场调试</td><td class="am">需较强实践经历</td></tr>
<tr class="r"><td>嵌入式与电子硬件</td><td>C/C++、MCU、PCB、软硬件协同</td><td>可作跨领域路径</td></tr>
</table>
<div class="r note">搜索别只用 “Electrical Engineer”：试试 System Studies · Protection &amp; Control · Interconnection · Distribution Planning · Commissioning</div>""", [
    ("综合来看，电力系统分析与保护控制有明确的零经验岗位，较值得优先关注；变电站和输配电设计的入口也比较明确。", 2),
    ("电力电子硬件研发技术壁垒较高，工业控制需要较强的现场经历，嵌入式可作为跨领域路径。", 5),
    ("还有一个容易忽略的点：企业招的不是统一的电力系统工程师，而是一系列分工明确的岗位。", 6),
    ("只搜Electrical Engineer，会漏掉大量相关机会。", 6),
]))

S.append(("08 核心矛盾", """
<h2>行业喊“人才短缺”，新人却不一定好找工作？</h2>
<div class="two">
  <div class="r panel center"><div class="num">+17,900</div><div class="lbl">2025年美国输配电行业就业增长（约 +2%）<br><span class="src">美国能源部 USEER 2026</span></div></div>
  <div class="r panel center"><div class="num am">≈90%</div><div class="lbl">2032年能源人才缺口集中在技术工种与现场岗位<br><span class="src">GE Vernova 模型估计，非实测</span></div></div>
</div>
<div class="r note">“美国缺几十万电网人才” ≠ “美国缺几十万电气工程硕士”</div>
<div class="r chips"><span>电网建模与分析</span><span>图纸与设计规范</span><span>现场工程调试</span><span>硬件研发与验证</span><span>项目沟通与交付</span></div>""", [
    ("这是报告中最重要的矛盾。2025年美国输配电行业就业增长了约一万七千九百人。", 1),
    ("但根据GE Vernova的估计，未来能源人才缺口约九成集中在技术工种和现场岗位。", 2),
    ("所以，美国缺几十万电网人才，不能理解为美国缺几十万电气工程硕士。", 3),
    ("对新人来说，真正的门槛是可交付能力：建模分析、图纸规范、现场调试、硬件验证和项目沟通。", 4),
]))

S.append(("09 AI 影响", """
<h2>AI 的影响：不能照搬软件行业</h2>
<div class="two">
  <div class="r panel big-p"><div class="ph">较易被 AI 辅助</div><ul><li>计算报告、简单制图</li><li>技术文档</li><li>代码初稿、仿真脚本</li></ul></div>
  <div class="r panel big-p"><div class="ph g">受物理与法规约束</div><ul><li>设备调试、复杂故障定位</li><li>工程现场协调、安全审查</li><li>系统责任签署</li></ul></div>
</div>
<div class="r note">目前没有可靠数据量化 AI 造成的 EE 初级岗位损失 —— 更有依据的判断是：门槛正在向实际技能和工程经验倾斜</div>""", [
    ("AI会不会冲击EE初级岗位？目前没有可靠的全国数据能量化这种影响。", 0,
     "AI会不会冲击E E初级岗位？目前没有可靠的全国数据能量化这种影响。"),
    ("从任务层面看，计算报告、文档、脚本初稿等工作容易获得AI辅助。", 1),
    ("但设备调试、故障定位、现场协调和安全签署，受到物理和法规约束。", 2),
    ("更有依据的判断是：竞争门槛正在更强调实际技能和工程经验，而不是已经发生大规模替代。", 3),
]))

S.append(("10 工资与结果", """
<h2>EE vs CS：近期毕业生就业结果</h2>
<div class="cmp">
  <div class="r crow"><span class="k">近期毕业生失业率</span><div class="pair"><div><i class="ee" style="width:32%"></i><b>EE 3.2%</b></div><div><i class="cs" style="width:70%"></i><b>CS 7.0%</b></div></div></div>
  <div class="r crow"><span class="k">就业不足率</span><div class="pair"><div><i class="ee" style="width:42%"></i><b>EE 21.1%</b></div><div><i class="cs" style="width:38%"></i><b>CS 19.1%</b></div></div></div>
  <div class="r crow"><span class="k">职业早期年薪中位数</span><div class="pair"><div><i class="ee" style="width:82%"></i><b>EE $82,000</b></div><div><i class="cs" style="width:87%"></i><b>CS $87,000</b></div></div></div>
</div>
<div class="src">纽约联储按专业统计（2024 ACS 样本，22—27岁）；NACE 2025届工程类本科平均起薪约 $81,518</div>
<div class="r note">EE 失业表现更好，但早期薪资不一定更高 —— 不能用 12 万美元的职业中位数代表毕业生收入</div>""", [
    ("再看工资。纽约联储数据显示，EE近期毕业生失业率只有3.2%，明显低于计算机科学的7%。", 1,
     "再看工资。纽约联储数据显示，E E近期毕业生失业率只有百分之三点二，明显低于计算机科学的百分之七。"),
    ("但EE的就业不足率略高，职业早期年薪中位数约8.2万美元，也低于CS的8.7万。", 3,
     "但E E的就业不足率略高，职业早期年薪中位数约八点二万美元，也低于C S的八点七万。"),
    ("所以，不能用十二万美元的职业中位薪资，来代表毕业生的实际收入。", 4),
]))

S.append(("11 签证限制", """
<h2>对国际学生：签证限制可能比岗位数量更重要</h2>
<table>
<tr><th>企业</th><th>具体限制</th><th>对 F-1 毕业生的意义</th></tr>
<tr class="r"><td>WSP</td><td>需无需担保的永久工作授权</td><td class="rd">通常不适合仅靠 OPT 的申请人</td></tr>
<tr class="r"><td>Black &amp; Veatch</td><td>Graduate 职位不提供签证担保</td><td class="am">须确认 OPT 及未来签证是否被接受</td></tr>
<tr class="r"><td>GM 研究岗</td><td>不支持 OPT / STEM OPT / CPT / H-1B</td><td class="rd">一般 F-1 毕业生不符合</td></tr>
</table>
<div class="r three-k"><div>有合法 OPT 资格</div><div>企业无需立即申请 H-1B</div><div>企业愿意支持长期签证</div></div>
<div class="r note warnline">第三方网站的 “Supports H-1B” 标签不可全信 —— 以招聘原文条款为准</div>""", [
    ("对国际学生来说，签证限制可能比岗位数量更重要。", 0),
    ("WSP要求永久工作授权，Black and Veatch不提供签证担保，通用汽车研究岗明确不支持OPT和H一B。", 3,
     "WSP要求永久工作授权，Black and Veatch不提供签证担保，通用汽车研究岗明确不支持O P T和H一B。"),
    ("要区分三件事：有合法OPT资格、企业不需要立即申请H一B、以及企业愿意支持长期签证，这并不是同一件事。", 4,
     "要区分三件事：有合法O P T资格、企业不需要立即申请H一B、以及企业愿意支持长期签证，这并不是同一件事。"),
    ("另外，招聘网站上的支持H一B标签不能全信，一定以招聘原文为准。", 5),
]))

S.append(("12 方向排序", """
<h2>哪些方向值得优先考虑？</h2>
<div class="rank">
  <div class="r rk first"><em>优先</em><div><b>电力电子硬件研发 + 电网 / 储能应用</b><span>Power Electronics · Power Conversion · ESS</span></div></div>
  <div class="r rk"><em>第二</em><div><b>电力系统分析与保护控制</b><span>Power System Studies · Protection &amp; Control · Substation</span></div></div>
  <div class="r rk"><em>补充</em><div><b>嵌入式控制与硬件系统</b><span>Embedded Systems · Controls · Hardware Validation</span></div></div>
</div>
<div class="chain">
  <div class="r step">功率电子基础与控制<span>DC-DC · 逆变器 · PWM · 闭环</span></div><div class="r arr">→</div>
  <div class="r step">建模仿真与硬件实现<span>PLECS / Simulink · PCB · MCU</span></div><div class="r arr">→</div>
  <div class="r step">实际能源应用<span>储能PCS · 充电 · 并网 · 电驱</span></div>
</div>""", [
    ("综合需求、入口、技能壁垒和跨行业能力，报告给出的优先方向是电力电子硬件研发，结合电网和储能应用。", 1),
    ("第二方向是电力系统分析与保护控制，嵌入式控制与硬件系统可以作为补充路径。", 3),
    ("硕士阶段可以围绕一条技术链来建设：从功率电子基础与控制，", 4),
    ("到建模仿真和PCB、MCU硬件实现，再落到储能、充电、并网和电驱等实际应用。", 8,
     "到建模仿真和P C B、M C U硬件实现，再落到储能、充电、并网和电驱等实际应用。"),
    ("要注意，纯粹的电池健康度预测项目，说服力通常不如做过真实功率变换器设计和测试的项目。", 8),
]))

S.append(("13 最终建议", """
<h2>最终建议</h2>
<div class="final">
  <div class="r fi"><i>1</i><div><b>首要目标</b>Power Electronics Engineer I / New Grad</div></div>
  <div class="r fi"><i>2</i><div><b>平行备选</b>Power System Studies Engineer I</div></div>
  <div class="r fi"><i>3</i><div><b>第一轮筛选</b>把签证资格作为首要过滤条件</div></div>
</div>
<div class="r note">下一步：直接核查 2027 届 EE 硕士可申请、接受 0—2 年经验、且明确允许国际学生工作授权的岗位</div>
<div class="r end">从“行业前景研究” → “可执行的求职策略”</div>""", [
    ("最后总结。报告建议把电力电子工程师新人岗作为首要目标，", 1),
    ("把电力系统研究工程师作为平行备选，并且把签证资格作为第一轮岗位筛选条件。", 3),
    ("下一步最有价值的，不是继续看行业缺多少万人，而是直接核查能申请、接受零到两年经验、并允许国际学生工作授权的岗位。", 4),
    ("这样才能把行业前景研究，真正变成可执行的求职策略。感谢观看。", 5),
]))
