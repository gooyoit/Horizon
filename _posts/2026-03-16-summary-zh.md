---
layout: default
title: "Horizon Summary: 2026-03-16 (ZH)"
date: 2026-03-16
lang: zh
---

> From 81 items, 29 important content pieces were selected

---

1. [Chrome DevTools 新增 MCP 支持和独立 CLI](#item-1) ⭐️ 9.0/10
2. [小米 SU7 全系标配 12 项高端配置，Pro 版 CLTC 续航 902 公里](#item-2) ⭐️ 9.0/10
3. [问界 M6 智慧 SUV 将于 3 月 23 日开启预订](#item-3) ⭐️ 9.0/10
4. [全国首所独立设置网安类本科高校今秋招生](#item-4) ⭐️ 9.0/10
5. [华为与广汽深度联合推出启境 GT7 电动车](#item-5) ⭐️ 9.0/10
6. [苹果发布采用融合架构的 M5 Pro 和 M5 Max 芯片](#item-6) ⭐️ 9.0/10
7. [科学家实现成年小鼠大脑玻璃化冷冻及功能恢复](#item-7) ⭐️ 9.0/10
8. [2026 年“3·15”晚会曝光七大消费侵权问题](#item-8) ⭐️ 9.0/10
9. [小米春季发布会定档 3 月 19 日，新一代 SU7 上市](#item-9) ⭐️ 9.0/10
10. [加拿大 C-22 法案强制大规模元数据监控](#item-10) ⭐️ 8.0/10
11. [49MB 网页凸显网络膨胀问题](#item-11) ⭐️ 8.0/10
12. [大语言模型架构趋同于通用设计模式](#item-12) ⭐️ 8.0/10
13. [分离 Wayland 合成器与窗口管理器](#item-13) ⭐️ 8.0/10
14. [什么是智能体工程？](#item-14) ⭐️ 8.0/10
15. [GrapWork v0.4.1 新增斜杆命令与定时任务](#item-15) ⭐️ 8.0/10
16. [奇瑞定档 2026 年推出全固态电池电动车](#item-16) ⭐️ 8.0/10
17. [AOC 推出 RGB 条纹 QD-OLED 游戏显示器](#item-17) ⭐️ 8.0/10
18. [Meta 因外包人员查看雷朋智能眼镜视频遭集体诉讼](#item-18) ⭐️ 8.0/10
19. [力积电完成向美光出售铜锣 P5 晶圆厂](#item-19) ⭐️ 8.0/10
20. [ImageGlass 10 Beta 1 新增 macOS 和 Linux 支持](#item-20) ⭐️ 8.0/10
21. [OpenAI 在 ChatGPT 测试广告，目标贡献近半营收](#item-21) ⭐️ 8.0/10
22. [腾讯云支撑日均产出 4 万张 AI 漫画及近 40 小时视频](#item-22) ⭐️ 7.0/10
23. [我国 26 个绿色物流案例纳入国际标准](#item-23) ⭐️ 7.0/10
24. [OpenClawX：支持本地推理的桌面级 AI 智能体平台](#item-24) ⭐️ 7.0/10
25. [为何我无法全程“氛围编程”而不看代码](#item-25) ⭐️ 7.0/10
26. [Besi 对收购传闻保持沉默](#item-26) ⭐️ 7.0/10
27. [极客湾揭露送测机乱象视频遭多平台下架](#item-27) ⭐️ 7.0/10
28. [Windows 11 预览版支持安装时自定义用户文件夹名称](#item-28) ⭐️ 7.0/10
29. [iOS 27 将保留液态玻璃设计并新增系统级透明度滑块](#item-29) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Chrome DevTools 新增 MCP 支持和独立 CLI](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) ⭐️ 9.0/10

Chrome DevTools 现在支持模型上下文协议（MCP），使 AI 代理能够直接与实时浏览器会话交互以进行调试。同时发布了新的独立 CLI（v0.20.0），可在无需完整浏览器界面的情况下以编程方式访问 DevTools 数据。 这一集成将 AI 编码助手与真实浏览器上下文连接起来，显著提升其准确诊断和修复前端问题的能力。它支持结合人类与 AI 的混合工作流，充分利用 Chrome 的深度检查功能，可能彻底改变开发者调试复杂 Web 应用的方式。 MCP 服务器会向兼容的 AI 客户端暴露浏览器和 DevTools 数据，但用户被提醒不要共享敏感信息。该 CLI 目前仅支持 Chrome，但可适配其他基于 Chromium 的浏览器，且已有开发者构建了利用此接口的 AI 代理技能。

hackernews · xnx · Mar 15, 19:12

**背景**: 模型上下文协议（MCP）是一种允许 AI 模型访问并与外部工具和环境交互的标准。在此场景中，Chrome DevTools 充当 MCP 服务器，使 AI 代理能够实时访问活跃浏览器会话中的 DOM、网络、控制台和性能数据。这建立在现有的 Chrome DevTools 协议（CDP）之上，将其扩展用于 AI 代理应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/ chrome - devtools - mcp : Chrome DevTools ...</a></li>
<li><a href="https://developer.chrome.com/blog/chrome-devtools-mcp">Chrome DevTools ( MCP ) for your AI agent | Blog | Chrome for...</a></li>
<li><a href="https://kailash-pathak.medium.com/how-google-chrome-devtools-mcp-empowers-ai-debugging-with-real-time-performance-insights-8d2f58c1c4d4">How Google Chrome DevTools MCP Empowers AI... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区成员对实际应用表现出热情，例如使用 AI 代理自动化网页交互并从中提取 API。现任/前任 DevTools 团队成员 Paul Irish 证实了尚未正式公布的 CLI 发布，其他人则强调其相比无头解决方案在保留丰富调试上下文方面的优势。也有用户指出了一些限制，包括仅支持 Chrome 以及潜在的服务条款风险。

**标签**: `#Chrome DevTools`, `#MCP`, `#Web Development`, `#Debugging`, `#AI Agents`

---

<a id="item-2"></a>
## [小米 SU7 全系标配 12 项高端配置，Pro 版 CLTC 续航 902 公里](https://www.ithome.com/0/929/401.htm) ⭐️ 9.0/10

小米宣布新一代 SU7 电动汽车将于 3 月 19 日正式上市，全系标配 12 项高端配置，包括 Pro 版 CLTC 续航 902 公里、激光雷达、700TOPS 辅助驾驶算力以及碳化硅高压平台。 此次发布使小米在高端电动车市场成为有力竞争者，凭借极具竞争力的配置、先进的智能驾驶系统和出色的安全性能，以 22.99 万元起的定价直接对标特斯拉、蔚来等品牌。 SU7 Pro 版采用 752V 碳化硅平台，CLTC 续航达 902 公里；全系标配 2200MPa 超高强度钢、9 个安全气囊、三重冗余门把手及搭载 4D 毫米波雷达的 Xiaomi HAD 端到端辅助驾驶系统。Max 版电压架构为 897V，最大功率 690 马力。

rss · IT HOME · Mar 16, 02:16

**背景**: CLTC（中国轻型汽车行驶工况）是中国自 2021 年起实施的电动车续航测试标准，其测得的续航里程通常高于实际使用或 WLTC 等国际标准。碳化硅（SiC）功率器件应用于 800V 以上高压平台，可提升能效、降低能耗并支持更快充电。小米于 2024 年正式进军电动车市场，首款 SU7 推出后迅速迭代，此次发布为新一代升级车型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/China_Light-Duty_Vehicle_Test_Cycle">China Light-Duty Vehicle Test Cycle - Wikipedia</a></li>
<li><a href="https://www.auto-testing.net/news/show-121014.html">电动汽车为什么要上800V？_汽车技术__汽车测试网</a></li>
<li><a href="https://baike.baidu.com/item/小米端到端辅助驾驶/65659974">小米端到端辅助驾驶 - 百度百科</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Xiaomi`, `#Automotive Tech`, `#ADAS`, `#Product Launch`

---

<a id="item-3"></a>
## [问界 M6 智慧 SUV 将于 3 月 23 日开启预订](https://www.ithome.com/0/929/397.htm) ⭐️ 9.0/10

华为支持的 AITO 品牌宣布，全新中大型智慧电动 SUV 问界 M6 将于 2024 年 3 月 23 日开启预订，配备顶置激光雷达、“向日葵”旋转中控屏，并提供多种增程版车型，纯电续航最高达 272 公里。 问界 M6 是华为鸿蒙智行联盟进军 25 万元级智能 SUV 市场的重要产品，凭借华为生态深度整合、高阶智能驾驶硬件和创新座舱设计，将与特斯拉 Model Y、小米 SU7 等热门车型正面竞争，进一步推动智能电动汽车的技术与体验升级。 问界 M6 车长 4960mm，轴距 2950mm，提供橙、白、黑、银、青、紫、蓝七种外观色及“紫慕白”双拼内饰，配备全景天幕、HUD 抬头显示、天空声道音响和副驾“灵感橱窗”；增程版提供 180 公里、260 公里和 272 公里三种纯电续航版本（测试工况未明确）。

rss · IT HOME · Mar 16, 02:11

**背景**: 鸿蒙智行（HIMA）是华为于 2023 年 11 月正式推出的智能汽车技术生态联盟，联合赛力斯（AITO）、奇瑞、北汽、江淮等车企，共同打造深度融合鸿蒙操作系统（HarmonyOS）、华为 ADS 高阶智能驾驶和鸿蒙智能座舱的电动汽车。AITO 作为鸿蒙智行的核心品牌，由华为与赛力斯联合打造，主打“软件定义汽车”和全场景智能互联体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1963191371339929045">一文解读华为自动驾驶布局之鸿蒙智行 - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/鸿蒙智行/63668052">鸿蒙智行_百度百科 AWE2026：从鸿蒙智家到鸿蒙智行，华为改写智能产业的竞争终局|车机|aw... 一文解读华为自动驾驶布局之鸿蒙智行-电子工程专辑 一文解读华为自动驾驶布局之鸿蒙智行 - 懂车帝 鸿蒙智行官网 一文解读华为自动驾驶布局之 鸿蒙智行 - 知乎 一文解读华为自动驾驶布局之 鸿蒙智行 - 知乎 鸿蒙座舱 - 华为乾崑智能汽车解决方案</a></li>
<li><a href="https://www.ithome.com/0/929/012.htm">鸿蒙智行问界 M6 内饰图公布：紫慕白双拼，“会转头”的随动屏 + 灵感橱...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Huawei`, `#Smart Cars`, `#Automotive Tech`, `#Product Launch`

---

<a id="item-4"></a>
## [全国首所独立设置网安类本科高校今秋招生](https://www.ithome.com/0/929/393.htm) ⭐️ 9.0/10

中国教育部近日正式批复同意设立全国唯一独立设置的网络安全类本科高校——网络空间安全学院，校址位于武汉，今年秋季开始招生，首批开设人工智能、数据科学与大数据技术、软件工程、计算机科学与技术四个本科专业。 此举是中国应对日益增长的网络安全人才需求和国家数字安全战略的关键举措。该学院强调产教融合与实战能力培养，有望为国家网络安全和高质量发展提供坚实的人才与科技支撑，并引领国内网安教育模式创新。 学院推行“三融一体”（产教融合、科教融合、军民融合）和“三制协同”（校企双导师制、双学分制、书院制）育人机制，强调“实网攻防、实岗训练、实操演练、实战检验”的培养路径。校址位于武汉临空港经济技术开发区国家网络安全人才与创新基地，毗邻武汉大学、华中科技大学网安学院及 400 余家网安企业。

rss · IT HOME · Mar 16, 01:51

**背景**: 此前，中国的网络安全教育多作为计算机学科下的一个方向开展。近年来，随着网络安全被提升至国家战略高度，多所“双一流”高校已设立独立的网络空间安全学院。但此次获批的网络空间安全学院是全国首个独立设置、仅聚焦网安领域的公办普通本科高校，标志着国家在网安人才培养体系上的重大升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://coe.njau.edu.cn/info/1050/5206.htm">产教融合再升级：工学院首创校企双导师制贯通毕设全流程</a></li>
<li><a href="https://dxs.moe.gov.cn/zx/a/gxdt/241025/1977245.shtml">校企创新联合体推进产教融合 校企“双导师”联合培养卓越人才 - 高校动...</a></li>
<li><a href="https://www.cnblogs.com/Johny-zhao/p/18902131">网络安全攻防演练实战指南 - Johny_Zhao - 博客园</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#higher education`, `#artificial intelligence`, `#data science`, `#national security`

---

<a id="item-5"></a>
## [华为与广汽深度联合推出启境 GT7 电动车](https://www.ithome.com/0/929/379.htm) ⭐️ 9.0/10

华为乾崑与广汽集团联合打造的高端电动车型启境 GT7 将于 3 月 17 日全球首秀，搭载华为全栈智能汽车技术，包括支持 L3 级自动驾驶的乾崑 ADS 4.0、896 线激光雷达、XMC 数字底盘引擎和鸿蒙座舱 HarmonySpace。 此次合作标志着智能电动汽车发展的重要里程碑，展示了科技巨头与传统车企深度协同如何加速高阶自动驾驶与智能座舱系统的落地。GT7 所搭载的 L3 架构与尖端硬件有望为行业树立新标杆。 GT7 搭载全球量产最高分辨率的 896 线激光雷达、响应速度达 1 毫秒的华为 XMC 数字底盘引擎，以及基于 MoLA 混合大模型架构的鸿蒙座舱 HarmonySpace 5。研发采用合署办公模式，依托华为 IPD/IPMS 体系及“红蓝军对抗”机制确保品质与效率。

rss · IT HOME · Mar 16, 01:27

**背景**: 华为“乾崑”是其智能汽车解决方案的统一品牌，涵盖乾崑智驾 ADS（高级驾驶辅助系统）、XMC 数字底盘引擎和鸿蒙座舱 HarmonySpace。乾崑 ADS 4.0 于 2025 年 4 月发布，已支持高速场景下的 L3 级商用自动驾驶。XMC 数字底盘通过千兆以太网和 ASN 切片网络实现底盘部件毫秒级协同控制，而 HarmonySpace 5 则采用 MoLA 混合大模型架构，提供多模态智能交互体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/703537549">华为乾崑智驾ADS二三事 - 知乎</a></li>
<li><a href="https://auto.gasgoo.com/news/202504/23I70423522C601.shtml">“能够超越ADS的只有ADS”，华为发布乾崑智驾ADS 4-盖世汽车资讯</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1898143400080934464">汽车底盘引擎新突破！华为乾崑XMC数字底盘如何做到“知行合一”？</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Huawei`, `#Autonomous Driving`, `#Smart Cockpit`, `#Automotive Technology`

---

<a id="item-6"></a>
## [苹果发布采用融合架构的 M5 Pro 和 M5 Max 芯片](https://t.me/zaihuapd/40272) ⭐️ 9.0/10

苹果发布了 M5 Pro 和 M5 Max 芯片，采用全新融合架构，将两颗 3 纳米晶粒集成到单一 SoC 中，并配备 18 核 CPU。这些芯片用于新款 MacBook Pro，而新款 MacBook Air 则搭载基础版 M5 芯片。 这是苹果首次在其芯片中采用多晶粒封装技术，为专业工作流带来显著性能提升，并为未来芯片设计指明新方向。此举也进一步强化了苹果在硬件和 AI 加速领域的垂直整合战略。 M5 Pro 和 M5 Max 包含 6 个高性能“超级核心”和 12 个能效核心，采用第三代 3 纳米工艺制造。融合架构通过高带宽、低延迟互连技术，将两颗晶粒集成于单一系统级芯片中。

telegram · zaihuapd · Mar 15, 07:20

**背景**: Apple Silicon 是苹果自研的系统级芯片（SoC），自 2020 年 M1 芯片起用于 Mac 和 iPad 设备。此前的 M1 至 M4 芯片均采用单晶粒设计。全新的融合架构标志着苹果转向先进封装技术，这与半导体行业其他领先企业用于高性能计算的方法类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/">Apple debuts M5 Pro and M5 Max to supercharge the most demanding pro workflows - Apple</a></li>
<li><a href="https://dev.to/tyson_cung/apple-m5-fusion-architecture-explained-two-dies-one-chip-infinite-possibilities-o9e">Apple M5 Fusion Architecture Explained - Two Dies, One Chip ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#M5 chip`, `#MacBook Pro`, `#semiconductors`, `#hardware`

---

<a id="item-7"></a>
## [科学家实现成年小鼠大脑玻璃化冷冻及功能恢复](https://www.pnas.org/doi/10.1073/pnas.2516848123) ⭐️ 9.0/10

研究人员开发了一种名为 V3 的新型玻璃化保护剂及优化的灌注方案，成功实现了成年小鼠脑片和原位全脑的玻璃化冷冻，并在复温后恢复了代谢活性、电生理功能和突触可塑性。 该突破解决了低温生物学中冰晶形成和保护剂毒性的长期难题，使具有完整功能的复杂脑组织长期保存成为可能，为脑库建设、神经科学研究乃至未来人体冷冻技术提供了重要基础。 V3 保护剂使用浓度为 59%（w/v），通过血管灌注技术在全脑保存中平衡了脱水与保护剂渗透；电子显微镜显示，玻璃化冷冻及复温后海马 CA1 区超微结构保存良好。

telegram · zaihuapd · Mar 15, 08:30

**背景**: 玻璃化冷冻是一种利用高浓度冷冻保护剂配合快速降温，使生物组织转变为无冰晶形成的玻璃态固体的低温保存技术。与传统慢速冷冻不同，玻璃化可避免冰晶造成的机械损伤，更有效地保护细胞结构与功能。该技术已广泛应用于胚胎和卵子冷冻，但因毒性及保护剂分布不均等问题，在大脑等大型复杂组织中的应用仍极具挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/479197177">玻璃化冷冻技术及其研究进展 - 知乎</a></li>
<li><a href="https://cdn.ebiotrade.com/newsf/2026-3/20260305084303825.htm">玻璃化低温保存：成年小鼠海马体结构与功能恢复的重大突破</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2015478938844038871">人类首次让冷冻大脑复活：小鼠脑组织在零下196度保存7天，记忆功能还...</a></li>

</ul>
</details>

**标签**: `#cryobiology`, `#neuroscience`, `#brain preservation`, `#vitrification`, `#PNAS`

---

<a id="item-8"></a>
## [2026 年“3·15”晚会曝光七大消费侵权问题](https://tv.cctv.com/live/cctv2/) ⭐️ 9.0/10

2026 年央视“3·15”晚会曝光了七大类侵害消费者权益的问题，包括鸡爪漂白、AI 大模型 GEO“投毒”、外泌体医美骗局、青少年增高玄学、私域营销坑老、超标电动自行车租赁以及荐股分成金融骗局。国家市场监管总局已对涉事企业展开执法，查封问题产品并立案调查。 此次曝光揭示了食品、医疗、金融和人工智能等日常消费领域存在的系统性风险，尤其警示了生成式 AI 等新兴技术被滥用的隐患。作为中国最具影响力的消费者权益节目，“3·15”晚会的调查结果将推动公众警惕并可能促成相关领域的监管升级。 所谓 GEO“投毒”是指服务商通过批量生产软文和虚假信息，诱导 AI 大模型在回答中优先推荐特定品牌，属于利用公开数据训练机制漏洞的“数据投毒”行为。而被包装成“万能神药”的外泌体（exosomes）在中国尚未获批为药品，仍处于科研阶段，其商业化使用属违规且存在安全风险。

telegram · zaihuapd · Mar 15, 12:05

**背景**: “3·15”晚会是中央电视台自 1991 年起每年 3 月 15 日（国际消费者权益日）播出的专题节目，以揭露侵害消费者权益行为著称，具有广泛社会影响力。AI“投毒”指通过污染训练数据或干扰模型学习过程，使其输出偏见或错误信息。外泌体是由细胞分泌的纳米级囊泡，在细胞间通讯和疾病治疗研究中备受关注，但目前在中国尚无任何外泌体药物获批上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lookonchain.com/feeds/50284">315 Gala Exposes AI Large Model " Poisoning ," AI "Brainwashing...</a></li>
<li><a href="https://aihub.org/2025/11/24/what-is-ai-poisoning-a-computer-scientist-explains/">What is AI poisoning ? A computer scientist explains - ΑΙhub</a></li>
<li><a href="https://www.cn-healthcare.com/articlewm/20230824/content-1596723.html">外泌体：极具潜力的再生医学技术及药物递送工具（上）|标志物|蛋白质|...</a></li>

</ul>
</details>

**标签**: `#consumer protection`, `#AI ethics`, `#food safety`, `#financial fraud`, `#public safety`

---

<a id="item-9"></a>
## [小米春季发布会定档 3 月 19 日，新一代 SU7 上市](https://m.weibo.cn/detail/5277018858982553) ⭐️ 9.0/10

小米宣布将于 3 月 19 日 19:00 举办春季新品发布会，正式推出新一代 SU7 电动汽车，以及全新 Xiaomi Book Pro 14 笔记本电脑和 Xiaomi Watch S5 智能手表。 此次发布标志着小米从消费电子领域向竞争激烈的电动汽车市场迈出关键一步，同时通过高度协同的硬件生态强化其战略。SU7 的推出可能改变市场对科技公司跨界造车的认知。 新一代 SU7 搭载小米自研 HyperOS 操作系统和 HyperEngine 电驱系统，部分版本续航可达 500 英里。Book Pro 14 采用 Intel Core Ultra X7 358H 处理器和镁合金一体机身，Watch S5 则支持 eSIM、升级健康传感器，并拥有最长 21 天续航。

telegram · zaihuapd · Mar 16, 02:15

**背景**: 小米于 2024 年推出首款电动汽车 SU7，定位为高性能电动轿车，设计灵感源自保时捷，并集成先进智能功能。HyperOS 是小米自主研发的统一操作系统，旨在打通手机、汽车与 IoT 设备。自 2010 年成立以来，小米持续构建覆盖多品类的智能硬件生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_SU7">Xiaomi SU 7 - Wikipedia</a></li>
<li><a href="https://www.gizmochina.com/2026/03/12/xiaomi-book-pro-14-tease-intel-core-ultra-x7-358h/">Xiaomi shows its first laptop in three years, the Xiaomi Book Pro 14</a></li>
<li><a href="https://www.gizmochina.com/2026/03/14/xiaomi-watch-s5-design-features-battery-life/">Xiaomi Watch S5 Official Teasers Reveal Slimmer Design, 316L Steel Body, and eSIM Option - Gizmochina</a></li>

</ul>
</details>

**标签**: `#Xiaomi`, `#Electric Vehicles`, `#Product Launch`, `#Consumer Electronics`, `#SU7`

---

<a id="item-10"></a>
## [加拿大 C-22 法案强制大规模元数据监控](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/) ⭐️ 8.0/10

加拿大 2026 年提出的 C-22 法案建立了一个法律框架，要求电信和在线服务提供商保留特定类别的元数据（如传输数据和位置信息）最多一年，并配合执法部门的数据访问请求。尽管该法案声称未赋予新的监控权力，但它允许基于搜查令的访问，并包含可能延迟或省略通知受影响个人的例外条款。 该立法通过制度化对所有加拿大人（而不仅限于嫌疑人）的大规模元数据留存，严重影响数字隐私权，引发对功能蔓延、滥用以及是否符合《宪章》禁止无理搜查和扣押条款的担忧。它还使加拿大更紧密地与“五眼联盟”的监控行为保持一致，可能削弱公众对数字服务的信任。 该法案明确允许制定法规，强制保留元数据（包括《刑事法典》第 487.011 条定义的传输数据），最长可达一年。此外，法案还包含条款，允许法官免除向受影响个人提供搜查令副本的要求，从而可能实现秘密监控。

hackernews · opengrass · Mar 15, 21:22

**背景**: C-22 法案是加拿大长期“合法访问”（lawful access）倡议的一部分，旨在为数字时代更新警方权力。此前的尝试，如 2012 年的 C-30 法案和 2015 年的 C-51 法案，因隐私问题引发强烈公众反对，最终被撤回或修改。元数据（即关于通信的数据，如时间、位置和设备标识符）即使不含内容也极具揭示性，强制留存制度已被隐私倡导者批评，并被欧盟等民主国家的法院裁定为不成比例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.canada.ca/en/public-safety-canada/news/2026/03/backgrounder--securing-access-to-information-in-bill-c-22.html">Backgrounder – Securing Access to Information (Bill C-22 – Part 2) - Canada.ca</a></li>
<li><a href="https://reclaimthenet.org/canada-bill-c22-lawful-access-act-metadata-retention-surveillance">Canada's Bill C-22 Mandates Mass Metadata Surveillance of Canadians</a></li>
<li><a href="https://www.parl.ca/DocumentViewer/en/45-1/bill/C-22/first-reading">Government Bill (House of Commons) C-22 (45-1) - First Reading - Lawful Access Act, 2026 - Parliament of Canada</a></li>

</ul>
</details>

**社区讨论**: 社区评论对法案声称未扩大监控权力表示怀疑，指出存在诸如免除搜查令通知等漏洞。其他评论强调了“五眼联盟”合作的地缘政治背景，并呼吁采取公民行动，例如联系国会议员或支持 OpenMedia 和加拿大公民自由协会（CCLA）等倡导组织。

**标签**: `#privacy`, `#surveillance`, `#legislation`, `#digital rights`, `#law enforcement`

---

<a id="item-11"></a>
## [49MB 网页凸显网络膨胀问题](https://thatshubham.com/blog/news-audit) ⭐️ 8.0/10

一篇题为《49MB 网页》的博客文章批评了极端的网页膨胀现象，引用了 750MB 网页等真实案例，并分析了过度使用 JavaScript 和媒体加载对性能、隐私和可用性的影响。 过度的网页膨胀会损害用户体验、增加数据消耗、通过追踪器侵犯隐私并浪费能源——这些问题影响数十亿用户，尤其是在移动设备或带宽受限的环境下。这一批评揭示了现代网页开发实践中的系统性缺陷。 文章提到一些视频密集型网页会不必要地预加载数百兆字节数据，并指出即使标签页在后台，仍会持续消耗 CPU 并追踪用户。文中建议使用 webpack-bundle-analyzer 等工具和设定性能预算来缓解问题。

hackernews · kermatt · Mar 15, 19:25

**背景**: 网页膨胀指因过度使用脚本、图片、视频和第三方追踪器而导致网页体积不必要地增大。过去十年中，平均网页大小显著增长，通常超过 2–3MB，尽管研究表明更大的网页会损害核心网页指标（如最大内容绘制 LCP 和累积布局偏移 CLS）。开发者因网络速度提升而忽视效率，误以为硬件能弥补问题，但这对低速连接用户造成伤害，并增加了碳足迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.speedcurve.com/blog/page-bloat-web-performance/">SpeedCurve | What is page bloat? And how is it hurting your ...</a></li>
<li><a href="https://www.howtogeek.com/why-do-websites-keep-getting-more-bloated-every-year/">Why Do Websites Keep Getting More Bloated Every Year?</a></li>
<li><a href="https://dev.to/techresolve/solved-bundle-size-investigation-a-step-by-step-guide-to-shrinking-your-javascript-1a7n">Solved: Bundle Size Investigation: A Step-by-Step Guide to ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对《纽约时报》等臃肿新闻网站的不满，分享了因预加载视频导致 750MB 网页的真实经历，并强调后台追踪器持续侵犯隐私的问题。有人指出，与 2005 年每月仅 400MB 的数据配额相比，如今的资源浪费显得荒谬。

**标签**: `#web performance`, `#page bloat`, `#frontend development`, `#privacy`, `#JavaScript`

---

<a id="item-12"></a>
## [大语言模型架构趋同于通用设计模式](https://sebastianraschka.com/llm-architecture-gallery/) ⭐️ 8.0/10

Sebastian Raschka 的“大语言模型架构画廊”以可视化方式展示了尽管多年来尝试了专家混合（MoE）、状态空间模型等替代方案，主流开源大语言模型仍趋同于一套共享的架构组件。 这种趋同表明该领域已趋于成熟，架构创新正让位于模型规模、数据质量和训练技术，成为性能提升的主要驱动力，有助于研究人员和工程师更高效地聚焦关键方向。 主流架构是采用 RMSNorm、旋转位置编码（RoPE）、SwiGLU 激活函数和分组查询注意力（GQA）的稠密解码器-only Transformer；Llama 3、Mistral 和 Qwen 等模型之间的差异如今仅是该模板内的微小变体。

hackernews · tzury · Mar 15, 16:01

**背景**: 大语言模型（LLM）主要是基于 2017 年提出的 Transformer 架构构建的深度神经网络。原始 Transformer 采用带自注意力机制的编码器-解码器结构，但现代 LLM（尤其是专注于文本生成的模型）通常仅使用解码器部分。随着时间推移，旋转位置编码（RoPE）、SwiGLU 激活函数和分组查询注意力（GQA）等关键改进被引入，以提升效率和性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/tutai-ai/transformers-and-llms-the-architecture-behind-the-ai-revolution-93ba27b4646e">Transformers and LLMs: The Architecture Behind the AI ...</a></li>
<li><a href="https://blog.bytebytego.com/p/how-transformers-architecture-powers">How Transformers Architecture Powers Modern LLMs</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/large-language-models-llms-vs-transformers/">Large Language Models (LLMs) vs Transformers - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，竞争性开源模型在架构上显著趋同，认为自 GPT-2 以来基础性创新已趋于停滞。许多人称赞 Raschka 的教育资源，并建议增加演化时间线或可缩放的可视化以提升画廊的实用性。

**标签**: `#LLM`, `#Transformer`, `#Neural Networks`, `#Machine Learning`, `#Model Architecture`

---

<a id="item-13"></a>
## [分离 Wayland 合成器与窗口管理器](https://isaacfreund.com/blog/river-window-management/) ⭐️ 8.0/10

River 合成器项目提出了一种新架构，将窗口管理器从 Wayland 合成器中解耦，并引入 river-window-management-v1 协议来实现这一分离。该设计旨在允许窗口管理逻辑独立开发，同时保持与合成器的逐帧同步。 这一转变可减少各 Wayland 合成器之间的重复工作，促进模块化，可能催生更健壮、可复用的窗口管理组件。但同时也引发担忧：此类协议是否会成为标准，还是会加剧生态系统的碎片化。 该实现通过在合成器进程内使用同步通信，避免了进程间每帧的往返通信，从而保持视觉一致性。该协议目前仅限 River 使用，尚不确定 Sway 或 Hyprland 等其他合成器是否会采纳。

hackernews · dpassens · Mar 15, 15:09

**背景**: 在传统的 Wayland 架构中，合成器将显示服务器、合成器和窗口管理器的角色合并为一个程序——这与 X11 不同（例如 Xorg + i3 + picom 是分离的）。这种单体设计意味着每个 Wayland 窗口管理器都必须实现完整的合成器，增加了开发复杂性。wlroots 等项目通过提供共享基础设施缓解了这一负担，但在大多数情况下，窗口管理逻辑仍与合成器紧密耦合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=47388137">Separating the Wayland compositor and window manager | Hacker ...</a></li>
<li><a href="https://wiki.archlinux.org/title/Wayland">Wayland - ArchWiki Separating the Wayland Compositor and Window Manager What is the difference between display server, a window ... The Comprehensive List of Wayland Compositors for Unix Wayland - ArchWiki What is the difference between display server, a window manager , an… Wayland - ArchWiki Wayland - ArchWiki Sway</a></li>
<li><a href="https://wayland.freedesktop.org/architecture.html">Wayland Architecture Wayland in linux development & programming - GeeksforGeeks Wayland Protocol Documentation | Wayland Explorer A Deep Dive Into The Wayland Protocol For Linux Introduction - The Wayland Protocol mikeroyal/Wayland-Guide - GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些人称赞其技术优雅且是迟来的架构改进，另一些人则担心这可能导致又一个合成器专属协议，加剧碎片化。多位评论者希望此举能推动标准化，但鉴于 Wayland 生态系统的历史趋势，他们仍持怀疑态度。

**标签**: `#Wayland`, `#window-manager`, `#compositor`, `#Linux-graphics`, `#system-architecture`

---

<a id="item-14"></a>
## [什么是智能体工程？](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/#atom-everything) ⭐️ 8.0/10

Simon Willison 正式将“智能体工程”定义为借助 AI 编码智能体开发软件的实践，这些智能体能通过循环编写和执行代码来实现指定目标。该方法利用 Claude Code、OpenAI Codex 和 Gemini CLI 等工具自动化迭代式软件开发任务。 智能体工程代表了软件开发范式的转变：人类专注于定义问题和验证解决方案，而 AI 负责具体实现。这有望大幅提升开发者生产力，并支持更宏大、更具影响力的项目。 其核心机制是智能体通过循环调用工具以达成目标，其中代码执行对迭代优化至关重要。与普通 LLM 输出不同，智能体系统能测试并改进自身代码，但仍需人类在问题定义、工具配置和结果验证方面提供指导。

rss · Simon Willison · Mar 15, 22:41

**背景**: 在大语言模型（LLM）语境中，AI 智能体通常指能够感知环境、做出决策并通过调用外部工具采取行动以完成目标的系统。编码智能体进一步扩展了这一概念，可生成并执行真实代码。该理念源于数十年来对自主智能体的 AI 研究，但直到最近随着 LLM 在可靠代码生成和工具使用方面的突破才变得切实可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>
<li><a href="https://www.agenticengineeringinstitute.com/">Agentic Engineering Institute (AEI)</a></li>

</ul>
</details>

**标签**: `#agentic engineering`, `#AI coding agents`, `#LLMs`, `#software development`, `#AI tools`

---

<a id="item-15"></a>
## [GrapWork v0.4.1 新增斜杆命令与定时任务](https://www.v2ex.com/t/1198546#reply0) ⭐️ 8.0/10

GrapWork v0.4.1 新增了通过输入“/”触发的斜杆命令，并引入新的“/loop”命令，允许用户在聊天中直接创建类似 cron 的定时自动化任务。 这些功能大幅提升了 GrapWork 作为桌面 AI Agent 的实用性，通过支持结构化、可重复且上下文感知的自动化，为开发者和高级用户弥合了对话式 AI 与可执行工作流之间的鸿沟。 斜杆命令界面提升了内置操作的可发现性与易用性，而“/loop”命令则依托 GrapWork 对 MCP（模型上下文协议）的支持，可执行文件操作或 API 调用等定时任务。此外，云同步功能也已优化并补充了相关说明文档。

rss · V2EX · Mar 16, 02:12

**背景**: GrapWork 是一款开源跨平台桌面 AI Agent，支持任意兼容 OpenAI 的大语言模型（LLM）API。它采用 Anthropic 于 2024 年 11 月推出的模型上下文协议（MCP），使 AI 能够与外部工具、文件和网络资源交互。通过注入“Skills”，可为 AI 提供领域知识，使其更深入理解用户业务流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/29001189476">MCP (Model Context Protocol)，一篇就够了。 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Open Source`, `#Desktop Application`, `#Automation`, `#LLM`

---

<a id="item-16"></a>
## [奇瑞定档 2026 年推出全固态电池电动车](https://www.ithome.com/0/929/396.htm) ⭐️ 8.0/10

奇瑞汽车宣布将于 3 月 18 日举办“电池之夜”活动，披露其全固态电池将于 2026 年上车（定向运营），2027 年实现量产，目标纯电续航达 1500 公里。 此举使奇瑞跻身全球首批推动全固态电池商业化的车企行列。全固态电池具备更高能量密度、更优安全性和超长续航，有望加速电动汽车普及并重塑行业竞争格局。 全固态电池将于 2026 年先用于定向运营场景，2027 年才开始大规模量产；该技术属于奇瑞 2024 年发布的鲲鹏电池品牌体系，其当前液态电池版本已宣称续航超 1200 公里。

rss · IT HOME · Mar 16, 02:07

**背景**: 全固态电池用固态电解质替代传统锂离子电池中的易燃液态电解液，可提升能量密度、热稳定性和安全性。主流技术路线包括硫化物、氧化物、聚合物和卤化物体系，其中硫化物在室温下离子电导率最高，但存在稳定性差和制造难度大等问题。尽管全球研发活跃，但高成本、界面阻抗和量产工艺仍是产业化的主要障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1902405237270090015">固态电池基本结构原理及主流技术路径 - 知乎</a></li>
<li><a href="https://blog.csdn.net/m0_66858441/article/details/155279431">深入讲解全固态电池 - CSDN博客</a></li>
<li><a href="https://www.grepow.cn/hyxw/ytldcygtldcjjsnqdwl.html">液 态 锂 电 池 与 固 态 锂 电 池 ：究竟谁能驱动 电 池 技术的未来？ -格瑞普 电 池</a></li>

</ul>
</details>

**标签**: `#solid-state-battery`, `#electric-vehicles`, `#Chery-Auto`, `#battery-technology`, `#automotive-innovation`

---

<a id="item-17"></a>
## [AOC 推出 RGB 条纹 QD-OLED 游戏显示器](https://www.ithome.com/0/929/395.htm) ⭐️ 8.0/10

AOC 推出了 AGON PRO AGP346UCSD，这是一款 34 英寸 QD-OLED 游戏显示器，采用 RGB V-Stripe 子像素排列、360Hz 刷新率和 DisplayPort 2.1 接口。这是首批在 QD-OLED 面板上采用 RGB 条纹子像素排列的主流显示器之一，相比传统 OLED 布局显著改善了文字清晰度。 此次发布让 RGB 条纹 QD-OLED 显示器不再局限于华硕、微星等小众品牌，推动该技术在消费市场的普及。同时，其 360Hz 刷新率和 DisplayPort 2.1 等顶级规格为游戏显示器树立了新标杆。 该显示器采用三星制造的 QD-OLED 面板，具备 RGB V-Stripe 排列，HDR 全屏亮度达 515 尼特，峰值亮度 1300 尼特，并通过 VESA DisplayHDR True Black 500 认证。配备 HDMI 2.1、DisplayPort 2.1、支持 15W PD 输出的 USB-C、内置 8W 扬声器、KVM 切换功能和 Light FX 音乐律动氛围灯。

rss · IT HOME · Mar 16, 01:59

**背景**: 传统 OLED 显示器常采用 PenTile 或 BGR 等非标准 RGB 子像素排列，易导致文字边缘出现彩边、清晰度下降。RGB 条纹排列将红、绿、蓝子像素按标准垂直列排布，与操作系统字体渲染方式匹配，从而提升可读性。QD-OLED 结合了 OLED 的纯黑表现与量子点技术，实现更高亮度和更广色域。VESA 的 DisplayHDR True Black 认证专为 OLED 面板设计，强调深邃黑色而非仅追求峰值亮度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/dataconomy-media_ces-2026-vertical-rgb-pixels-arrive-to-solve-activity-7413923559452065792-lVtp">CES 2026: Vertical RGB pixels arrive to solve OLED text fringing issues</a></li>
<li><a href="https://www.rtings.com/tv/learn/what-is-qd-oled">What Is QD-OLED?: The Pros And Cons Of QD-OLED TVs</a></li>
<li><a href="https://displayhdr.org/">Vesa Certified DisplayHDR™</a></li>

</ul>
</details>

**标签**: `#OLED`, `#QD-OLED`, `#RGB Stripe`, `#Gaming Monitor`, `#Display Technology`

---

<a id="item-18"></a>
## [Meta 因外包人员查看雷朋智能眼镜视频遭集体诉讼](https://www.ithome.com/0/929/392.htm) ⭐️ 8.0/10

Meta 在美国遭遇集体诉讼，指控其将雷朋智能眼镜用户拍摄的私人视频发送至肯尼亚的一家外包公司，人工审核员在训练 AI 模型过程中接触了包括亲密行为和金融操作在内的敏感内容。 此案凸显了用户隐私、知情同意以及 AI 训练中使用人工标注数据的伦理问题，尤其是在涉及敏感个人影像且由海外人员处理的情况下。这可能影响科技公司未来在全球范围内的数据标注实践与透明度标准。 Meta 承认当用户主动将内容发送给 Meta AI 时，有时会使用第三方审核员进行数据标注（业内常见做法），并称已过滤数据以去除可识别个人信息。但一名匿名内部人士称曾看到未经脱敏的私密场景，质疑其保护措施的有效性。

rss · IT HOME · Mar 16, 01:46

**背景**: 雷朋 Meta 智能眼镜由 Meta 与依视路陆逊梯卡联合开发，支持用户通过语音指令拍摄照片和视频，并与 AI 助手互动。为提升 AI 准确性，企业常依赖人工标注员对真实世界数据进行标记——若缺乏严格管控，这一过程可能导致原始敏感用户内容被暴露。数据标注是 AI 开发中的关键环节，却常被忽视，持续引发隐私争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ray-ban.com/canada/en/rayban-meta-ai-glasses">Ray - Ban Meta AI glasses Gen 2 & Gen 1 | Ray - Ban ® CA</a></li>
<li><a href="https://36kr.com/p/2455661925963907">用 AI 来 训 练 大模型？ 但 人 工 数 据 标 注 还很难取代-36氪</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI ethics`, `#smart glasses`, `#data protection`, `#Meta`

---

<a id="item-19"></a>
## [力积电完成向美光出售铜锣 P5 晶圆厂](https://www.ithome.com/0/929/378.htm) ⭐️ 8.0/10

力积电已正式完成以 18 亿美元向美光出售其位于台湾铜锣的 P5 晶圆厂。同时，双方将在力积电新竹厂区展开合作，包括 HBM/PWF 代工服务及 DRAM 制程技术研发。 该交易增强了美光在先进 DRAM 制造方面的能力，同时助力力积电转向高附加值的 3D AI 代工业务，尤其是在 AI 驱动下快速增长的 HBM 市场。这也标志着存储芯片厂商与专业晶圆代工厂在半导体生态中的进一步融合。 力积电将把铜锣厂设备搬迁至新竹厂区并重新配置产线，而美光则加速在收购的洁净室中部署先进 DRAM 生产线。力积电目标在三年内将其 3D AI 代工业务营收占比从 3%提升至 20%。

rss · IT HOME · Mar 16, 01:27

**背景**: HBM（高带宽内存）是一种主要用于 AI 加速器和高端 GPU 的高性能 DRAM，需采用先进的封装和硅通孔（TSV）技术。PWF（Post Wafer Fabrication，晶圆后段制造）指晶圆制造完成后的堆叠、测试等后道工序。DDR4 是广泛使用的 DRAM 标准，“8G”可能指单颗芯片 8Gb 容量。力积电传统上从事 DRAM 与逻辑芯片代工，正逐步转型为专注 AI 相关内存与逻辑服务的特色代工厂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technews.tw/2026/03/16/psmc-completes-p5-plant-transaction-3d-ai-foundry-set-to-soar/">力積電 P5 廠完成售予美光，將在新竹廠展開 HBM/PWF 代工服務 | TechN...</a></li>
<li><a href="https://www.investor.com.tw/onlineNews/HeadlineNews.asp?AJX=2026/3/1682643">財訊快報-力積電P5廠完成售予美光，新竹廠區展開HBM/PWF代工、推進記...</a></li>
<li><a href="https://www.ctee.com.tw/news/20260206700184-439901">不只賣廠 力積電與美光深化合作 切入HBM供應鏈 3D AI有斬獲</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#DRAM`, `#HBM`, `#Micron`, `#Foundry`

---

<a id="item-20"></a>
## [ImageGlass 10 Beta 1 新增 macOS 和 Linux 支持](https://imageglass.org/news/imageglass-10-beta-1-is-here-99) ⭐️ 8.0/10

ImageGlass 10 Beta 1 在使用 .NET 和 Avalonia UI 框架完全重写后发布，现已原生支持 Windows、macOS 和 Linux。新版本强调更快的启动速度、快速切换图片以及对大图的流畅缩放。 这标志着 ImageGlass 的重大里程碑，使其从仅限 Windows 的工具转变为真正的跨平台开源看图软件。它为 macOS 和 Linux 用户提供了更多选择，同时也展示了现代 .NET 与 Avalonia 框架在构建跨平台高性能桌面应用方面的成熟度。 ImageGlass 9 已进入维护模式，后续开发将集中于 10 版本。但当前 Beta 版本的二进制文件尚未进行数字签名，可能影响部分系统上的信任或安装体验。

telegram · zaihuapd · Mar 15, 11:40

**背景**: ImageGlass 是一款广受欢迎的开源看图软件，以轻量、支持 90 多种图片格式（包括 WEBP、SVG、HEIC 和 JXL）以及无广告体验著称。Avalonia 是一个受 WPF 启发的开源跨平台 .NET UI 框架，允许开发者使用 XAML 和 C# 构建适用于 Windows、macOS、Linux 等平台的原生应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Avalonia_(software_framework)">Avalonia (software framework) - Wikipedia</a></li>
<li><a href="https://avaloniaui.net/">Avalonia UI – Open-Source .NET XAML Framework | WPF & MAUI ...</a></li>
<li><a href="https://github.com/d2phap/ImageGlass">ImageGlass - A lightweight, versatile image viewer - GitHub ImageGlass is the open-source Windows photo viewer you ... - MUO ImageGlass download | SourceForge.net ImageGlass - A lightweight, versatile image viewer | ImageGlass ImageGlass: The Windows Photo Viewer You Need - ByteTrending Download ImageGlass - MajorGeeks</a></li>

</ul>
</details>

**标签**: `#ImageGlass`, `#cross-platform`, `#open-source`, `#.NET`, `#Avalonia`

---

<a id="item-21"></a>
## [OpenAI 在 ChatGPT 测试广告，目标贡献近半营收](https://t.me/zaihuapd/40282) ⭐️ 8.0/10

OpenAI 于 2 月 9 日开始在 ChatGPT 中测试带有明确标识的广告，最初面向免费和 Plus 订阅用户，在聊天界面下方的独立区域展示。首席执行官 Sam Altman 表示，广告收入长期有望占公司总营收的近一半。 此举标志着 OpenAI 商业模式的重大转变，表明其对 ChatGPT 用户规模和参与度的信心。若成功，可能重塑生成式 AI 平台在不损害核心功能的前提下实现可持续盈利的方式。 广告仅出现在回复下方的指定区域，明确标注为广告，且不会使用用户的私密对话数据；广告主无法干预 AI 生成的回答。OpenAI 还透露 ChatGPT 月活跃用户增长率已回升至 10%以上。

telegram · zaihuapd · Mar 16, 01:23

**背景**: ChatGPT 由 OpenAI 于 2022 年底推出，迅速成为增长最快的消费级应用之一，提供 AI 驱动的对话功能。此前，OpenAI 的主要收入来源包括企业 API 销售、ChatGPT Plus 订阅以及与微软的合作。广告业务为其面向消费者的 AI 产品开辟了新的变现路径。

**标签**: `#OpenAI`, `#ChatGPT`, `#AI Monetization`, `#Advertising`, `#Sam Altman`

---

<a id="item-22"></a>
## [腾讯云支撑日均产出 4 万张 AI 漫画及近 40 小时视频](https://36kr.com/newsflashes/3725004280068739?f=rss) ⭐️ 7.0/10

腾讯云于 3 月 15 日披露，已服务国内超 80%的头部 AI 漫剧团队，支撑其日均产出 4 万张 AI 漫画和近 40 小时的视频内容。 这体现了 AIGC（人工智能生成内容）在数字媒体领域的工业化应用，凸显腾讯云在推动融合漫画与短视频的新兴内容形态全球化分发中的关键作用。如此大规模的内容产出彰显了 AI 对创意生产流程和全球传播模式的深刻变革。 日均产出折合约 800 至 1300 集漫剧，覆盖北美、东南亚、日韩等全球市场。腾讯云为这些工作室提供底层基础设施，支持剧本智能改编、角色场景生成及视频合成等 AI 创作环节。

rss · 36kr · Mar 16, 02:30

**背景**: AI 漫剧是一种新兴内容形式，利用 AIGC 技术将小说或剧本转化为类似动画漫画的图文短视频。自 2024 年以来，阅文旗下的“漫剧助手”和“漫剧工场”等平台提供端到端 AI 创作工具，推动该形式在抖音、快手等短视频平台快速爆发。腾讯云则为这一行业提供云计算与 AI 模型基础设施，支撑高并发、自动化的海量内容生产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bilibili.com/video/BV1QTPUz2En9/">【AI漫剧教程】2026最新！揭秘AI漫剧制作全流程！新手入门AI视频制作... 人工智能 - AI漫剧制作完全指南：从零开始用AI创作爆款短剧 - 个人文... 漫剧助手 - 一键生成，剧现精彩 | 阅文旗下AI漫剧创作平台 漫剧工场 - AI漫剧一站式创作与发行平台 亲测2025年4款AI漫剧工具！从小说到漫剧，网文作者必看 所有人都All in，AI漫剧到底是怎么个事_腾讯新闻</a></li>
<li><a href="https://segmentfault.com/a/1190000047645766">人工智能 - AI漫剧制作完全指南：从零开始用AI创作爆款短剧 - 个人文...</a></li>
<li><a href="https://manjugongchang.com/">漫剧工场 - AI漫剧一站式创作与发行平台</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cloud Computing`, `#Digital Media`, `#Content Generation`, `#Tencent Cloud`

---

<a id="item-23"></a>
## [我国 26 个绿色物流案例纳入国际标准](https://36kr.com/newsflashes/3724994250422913?f=rss) ⭐️ 7.0/10

我国牵头制定的国际标准《绿色物流活动应用案例》（ISO/TR 25326:2026）正式发布，收录来自 15 个国家 28 家企业的 83 个案例，其中 26 个来自中国，涵盖物流全链条的可持续实践。 该标准为全球物流行业提供可操作的绿色实践指南，有助于推动碳减排和可持续发展，彰显中国在国际绿色标准制定中日益增强的话语权，并助力全球供应链低碳转型。 该标准聚焦运输、储存、装卸、搬运、包装、流通加工、配送及信息处理八大物流环节，从资源集约利用、低碳排放、资源循环利用、环境保护和职业健康五个维度评估案例，并提出标准化实施建议。

rss · 36kr · Mar 16, 02:26

**背景**: 绿色物流指在保障效率的同时，最大限度降低物流活动对环境影响的策略与实践。国际标准化组织（ISO）发布的标准为跨国界协调可持续发展行动提供框架。ISO 技术报告（如 ISO/TR 25326）不具强制性，主要用于分享最佳实践。中国主导此项标准，体现了其在“双碳”战略下推动产业绿色转型的政策导向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.samr.gov.cn/xw/sj/art/2026/art_2f5fcee2389d43869997448b09620668.html">我国26个绿色物流案例纳入国际标准</a></li>
<li><a href="http://www.worldmetals.com.cn/viscms/qiyedongtai0275/20251028/269330.html">鞍山钢铁主导制定绿色物流国际标准ISO/TR 25326---世界金属导报</a></li>
<li><a href="https://news.cctv.cn/2026/03/16/ARTItHRY6hIByEuTE1czF2B5260316.shtml">聚焦运输、储存等 我国26个绿色物流案例纳入国际标准_新闻频道_央视网...</a></li>

</ul>
</details>

**标签**: `#green logistics`, `#international standards`, `#sustainability`, `#supply chain`, `#carbon reduction`

---

<a id="item-24"></a>
## [OpenClawX：支持本地推理的桌面级 AI 智能体平台](https://www.v2ex.com/t/1198547#reply0) ⭐️ 7.0/10

一位开发者发布了 OpenClawX，这是一个基于 OpenClaw 复刻的开源桌面优先 AI 智能体平台，支持多通道消息（飞书、钉钉、微信、Telegram）、通过 GGUF 格式实现本地大模型推理以避免消耗云端 Token，并兼容 MCP 协议和插件扩展。 OpenClawX 满足了市场对低成本、注重隐私且可离线运行的 AI 智能体的需求，同时深度集成中国主流办公协作工具，对国内开发者和企业具有实际应用价值。 它通过 node-llama-cpp 支持 GGUF 模型的零 Token 本地推理，允许在同一对话中实时切换本地与云端智能体，并采用统一 Gateway 架构处理多通道消息路由。项目采用限制性 MIT 许可证，并基于 OpenBot 框架构建。

rss · V2EX · Mar 16, 02:13

**背景**: GGUF 是一种为高效本地大模型推理优化的量化格式，常与 llama.cpp 配合使用。Model Context Protocol（MCP）由 Anthropic 于 2024 年底推出，是一种开放标准，允许 AI 模型安全连接外部工具和数据源。OpenClawX 利用这些技术实现灵活、低成本的桌面端 AI 智能体部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://medium.com/@narayanpanigrahy18/run-any-hugging-face-llm-locally-a-step-by-step-guide-to-gguf-conversion-with-llama-cpp-bd22250f1f70">Run Any Hugging Face LLM Locally : A Step-by-Step Guide to GGUF ...</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Local LLM`, `#Open Source`, `#Desktop Application`, `#MCP`

---

<a id="item-25"></a>
## [为何我无法全程“氛围编程”而不看代码](https://www.v2ex.com/t/1198541#reply8) ⭐️ 7.0/10

一位开发者解释了自己为何不愿完全采用“氛围编程”（即不审查 AI 生成的代码），因为担心在团队协作或调试时因缺乏对代码的深入理解而丧失可信度。 这揭示了现代软件开发中的一个关键矛盾：在 AI 驱动的效率与代码所有权、可维护性及团队责任之间取得平衡。随着 AI 编程工具日益普及，这类反思有助于建立负责任的使用规范。 作者采用半自动化方式：先与 AI 沟通设计方案，再严格审查后端修改（尤其是逻辑变更部分），前端则仅做粗略检查。他们担心若完全依赖 AI 而不理解代码，在同事提问或线上故障排查时将无法应对。

rss · V2EX · Mar 16, 01:59

**背景**: “氛围编程”（vibe coding）是由 Andrej Karpathy 于 2025 年初推广的一种 AI 辅助编程实践，开发者通过向大语言模型（LLM）描述任务，凭直觉和迭代反馈接受生成的代码，而非仔细审查。这一概念体现了向快速、流畅开发的转变，但也因可能损害代码质量、安全性和长期可维护性而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://vibecodng.org/">Welcome to Vibe Coding</a></li>

</ul>
</details>

**标签**: `#AI programming`, `#software engineering`, `#code review`, `#developer productivity`, `#LLM tools`

---

<a id="item-26"></a>
## [Besi 对收购传闻保持沉默](https://www.ithome.com/0/929/389.htm) ⭐️ 7.0/10

荷兰半导体设备制造商 Besi 拒绝对被应用材料或泛林集团收购的传闻置评，并重申其作为独立公司执行现有战略、提升股东价值的承诺。 这一传闻凸显了半导体设备行业在先进封装（如混合键合）领域日益加剧的整合压力，而该技术对下一代芯片集成至关重要。作为关键技术提供商且被应用材料持股 9%，Besi 的未来可能影响行业竞争格局。 Besi 是混合键合设备领域的领导者，其 Datacon 8800 CHAMEO ultra plus AC 平台以超高贴装精度和高吞吐量支持 3D 集成。应用材料是其第一大股东（持股 9%），此前已与 Besi 在混合键合技术商业化方面展开合作。

rss · IT HOME · Mar 16, 01:41

**背景**: 混合键合是一种先进的半导体封装技术，通过铜-铜直接连接实现芯片间互连，相比传统引线键合可提供更高密度、更优性能和更低功耗。它是台积电（SoIC）和英特尔等领先厂商 3D 集成战略的核心。实现此类先进封装的大规模生产，依赖于具备超高精度对准和洁净工艺能力的设备，例如 Besi 的产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aminext.blog/en/post/hybrid-bonding-the-next-frontier-of-3d-ic-1">Hybrid Bonding : The Vertical Revolution Powering the Next...</a></li>
<li><a href="https://www.juxinlitech.com/news/hybrid-bonding-a-key-technology-leading-the-future-development-of-the-semiconductor-industry/">Hyrbid Bonding : A Vital Leap in Semiconductor Industry Advancement</a></li>
<li><a href="https://www.besi.com/products-technology/product-details/product/datacon-8800-chameo-ultra-plus-ac/">Datacon 8800 CHAMEO ultra plus AC - Besi</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#M&A`, `#advanced packaging`, `#hybrid bonding`, `#Besi`

---

<a id="item-27"></a>
## [极客湾揭露送测机乱象视频遭多平台下架](https://t.me/zaihuapd/40268) ⭐️ 7.0/10

极客湾发布的一则揭露手机厂商向媒体提供特调优化“送测机”的视频已被哔哩哔哩和 YouTube 下架，作者随后提供了补档下载链接并公开回应此事。 该事件引发了对科技媒体透明度和行业施压审查的严重担忧，也凸显了独立评测者在挑战大型手机厂商时所面临的脆弱处境。 该视频题为《手机游戏性能大横评：厂商作弊太疯狂！》，通过对比 44 台零售版手机与媒体送测机，发现后者存在专属性能调校；涉事品牌包括 OPPO、vivo、小米和一加等主流厂商。

telegram · zaihuapd · Mar 15, 03:15

**背景**: 在智能手机行业，厂商常向媒体提供未上市的样机用于评测。这些“送测机”有时会通过临时软件或硬件调校，在跑分和性能测试中表现更优，从而误导消费者。这种被称为“媒体机特调”或“评测作弊”的做法，破坏了公平比较的基础，损害用户信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2011446523708335527">极客湾评测下架事件：一场关于"媒体机特调"的行业信任危机与方法论反...</a></li>
<li><a href="https://post.smzdm.com/p/a8w48wpl/">开工就掀行业遮羞布！极客湾测评遭下架，反手开源让厂商无力回天_安卓...</a></li>
<li><a href="https://agent.qianwen.com/mos/f0aa3b941ba6486a94fc6a7db19b03dc/949d8dd2a83cda5bb83a3486f4f1c3aa">极客湾手机横评视频下架事件分析报告</a></li>

</ul>
</details>

**社区讨论**: 视频下架后 24 小时内，极客湾 B 站粉丝激增 18.6 万，显示公众强烈支持；众多技术爱好者和开发者也在论坛拆解厂商作弊手段，将事件演变为一场推动行业透明化的集体行动。

**标签**: `#tech journalism`, `#smartphone industry`, `#media ethics`, `#censorship`, `#hardware reviews`

---

<a id="item-28"></a>
## [Windows 11 预览版支持安装时自定义用户文件夹名称](https://blogs.windows.com/windows-insider/2026/03/13/announcing-windows-11-insider-preview-build-26300-8068-dev-channel/) ⭐️ 7.0/10

微软发布了 Windows 11 Insider Preview Build 26300.8068，允许用户在初始安装过程中自定义用户文件夹名称，而不再仅依据 Microsoft 账户邮箱地址自动生成。 这一改进解决了长期存在的用户体验问题——此前自动生成的文件夹名常被截断、包含特殊字符，或在命令行操作和系统管理中带来不便。现在用户可在安装初期就掌控自己的文件夹命名。 该功能仅在开箱体验（OOBE）设置阶段可用；已安装系统的用户即使升级到此版本，也无法通过此功能直接修改现有用户文件夹名称。

telegram · zaihuapd · Mar 15, 06:15

**背景**: 在之前的 Windows 11 版本中，C:\Users 下的用户文件夹会根据 Microsoft 账户邮箱的前五个字符自动生成，或在使用本地账户时采用通用名称。这常常导致文件夹名称混乱或不实用，尤其对频繁使用命令行或脚本操作文件系统的开发者和高级用户造成困扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://windiscover.com/posts/windows-11-custom-user-folder-name-setup.html">Windows 11 初始安装流程新增用户文件夹自定义命名功能 - WinDiscover</a></li>
<li><a href="https://bbs.pcbeta.com/viewthread-2066707-1-1.html">微软终于允许Windows 11安装阶段自定义用户文件夹名称（蓝点网） - 远...</a></li>
<li><a href="https://blogs.windows.com/windows-insider/2026/03/13/announcing-windows-11-insider-preview-build-26300-8068-dev-channel/">Announcing Windows 11 Insider Preview Build 26300 . 8068 ...</a></li>

</ul>
</details>

**标签**: `#Windows 11`, `#Microsoft`, `#Operating System`, `#User Experience`, `#Insider Preview`

---

<a id="item-29"></a>
## [iOS 27 将保留液态玻璃设计并新增系统级透明度滑块](https://9to5mac.com/2026/03/15/ios-27-likely-wont-include-any-major-changes-to-liquid-glass-report/) ⭐️ 7.0/10

苹果计划在 iOS 27 和 macOS 27 中保留液态玻璃（Liquid Glass）设计，不进行重大视觉改动，但可能会引入一个系统级滑块，让用户调整界面中玻璃效果的透明度和模糊强度。 该功能通过赋予用户对界面美学的精细控制，提升了个性化与可访问性，体现了苹果在保持设计一致性的同时，向更可定制化系统界面的转变。 该滑块最初在 iOS 26 开发阶段尝试实现，但因工程挑战仅限于锁定屏幕时钟；iOS 27 则计划将其扩展至应用文件夹、主屏幕和导航栏等全局界面元素。

telegram · zaihuapd · Mar 15, 15:36

**背景**: 液态玻璃（Liquid Glass）是苹果在 2025 年全球开发者大会（WWDC）上推出的统一设计语言，采用兼具玻璃般透明感与流动感的动态材质。它构成了 iOS 26、macOS Tahoe 等平台的视觉基础，强调深度、半透明效果和响应性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Liquid_glass">Liquid Glass - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/2026/03/15/ios-27-may-add-a-useful-setting/">Apple is Aiming to Add a System-Wide Liquid Glass Slider to ...</a></li>
<li><a href="https://www.macobserver.com/news/ios-27-to-finally-bring-full-control-over-liquid-glass-opacity-says-report/">iOS 27 to Finally Bring Full Control Over Liquid Glass ...</a></li>

</ul>
</details>

**标签**: `#iOS`, `#Apple`, `#UI/UX`, `#Liquid Glass`, `#System Design`

---