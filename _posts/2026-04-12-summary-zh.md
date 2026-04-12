---
layout: default
title: "Horizon Summary: 2026-04-12 (ZH)"
date: 2026-04-12
lang: zh
---

> From 76 items, 17 important content pieces were selected

---

1. [小型开源模型复现 Mythos 漏洞发现](#item-1) ⭐️ 9.0/10
2. [顶级 AI 智能体基准测试可被简单漏洞轻易攻破](#item-2) ⭐️ 9.0/10
3. [宇树 H1 人形机器人奔跑速度达 10 米/秒](#item-3) ⭐️ 9.0/10
4. [马斯克：Grok 将于六月达到或超越 Claude Opus 4.6 水平](#item-4) ⭐️ 9.0/10
5. [工信部将发布一批“人工智能+”高价值场景](#item-5) ⭐️ 8.0/10
6. [完全由 AI 辅助开发的万三工作室现已开源](#item-6) ⭐️ 8.0/10
7. [开源 AI 智能体基础设施 Hivo 发布](#item-7) ⭐️ 8.0/10
8. [中兴通讯不造车，专注向车企提供 AI 与 ICT 能力](#item-8) ⭐️ 8.0/10
9. [华为乾崑智驾装车达 140 万套，称 L3 是迈向完全自动驾驶必经阶段](#item-9) ⭐️ 8.0/10
10. [别克至境 E7 上市，搭载 AI 智驾与豆包大模型](#item-10) ⭐️ 8.0/10
11. [大众汽车计划 2027 年实现 L3 级自动驾驶，2029 年达 L4 级](#item-11) ⭐️ 8.0/10
12. [地平线发布“星空”芯片，实现舱驾融合 AI 智能体](#item-12) ⭐️ 8.0/10
13. [普京呼吁俄罗斯自主研发人工智能基础模型](#item-13) ⭐️ 8.0/10
14. [硅谷顶尖 AI 人才加速回流中国](#item-14) ⭐️ 8.0/10
15. [艾伦人工智能研究所推出 MolmoWeb：开源视觉网页智能体平台](#item-15) ⭐️ 8.0/10
16. [Claude for Word 将 Anthropic 的 AI 引入微软 Word](#item-16) ⭐️ 8.0/10
17. [社区分享手动绕过 GPT 访问限制的方法](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [小型开源模型复现 Mythos 漏洞发现](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) ⭐️ 9.0/10

研究人员证明，小型开源 AI 模型成功复现了 Anthropic 先进 Mythos 系统最初发现的关键安全漏洞。在测试中，八款开源模型（包括一款仅含 36 亿激活参数的模型）在给定隔离的漏洞代码后，均检测出了 Mythos 标志性的 FreeBSD 漏洞。 这一发现挑战了“只有 Mythos 等大型专有前沿模型才能进行高影响力网络安全分析”的假设，表明更小、更便宜且透明的开源模型在特定任务中可能提供相当的价值。这引发了关于成本效益、可复现性以及大规模闭源模型是否真有必要用于实际漏洞检测的重要讨论。 该复现仅在隔离相关漏洞代码片段后才成功，这相比扫描整个代码库大大简化了任务——专家指出这是关键局限。其中一款模型每百万 token 成本仅为 0.11 美元，远低于 Mythos 在千次运行中约 2 万美元的总成本。

hackernews · dominicq · Apr 11, 16:47

**背景**: Anthropic 的 Mythos 是一个能力极强但尚未公开发布的 AI 系统，定位高于其 Claude Opus 模型，专门用于在关键软件中发现零日漏洞。开源权重（open-weight）模型是指其内部参数（权重）公开可用的 AI 系统，允许独立验证、微调和部署，不受厂商限制。与闭源模型不同，它们支持透明度和社区审查，这在安全研究中至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/data-and-beyond/claude-mythos-the-ai-anthropic-built-and-is-too-scared-to-release-9fc43851dfb4">Claude Mythos : The AI Anthropic Built and Is Too Scared to... | Medium</a></li>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open - Weight AI Models : What They Are, and Why... | Medium</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-04-10/mythos-why-anthropic-s-new-ai-has-officials-worried">Mythos : Why Anthropic ’s New AI Has Officials Worried - Bloomberg</a></li>

</ul>
</details>

**社区讨论**: 社区成员就复现结果的意义展开争论：一些人称赞小型模型的高效性，另一些人则提醒称，隔离代码消除了现实世界的复杂性。批评者还质疑 Anthropic 缺乏可复现性，并指出 Mythos 未能预防 Bun 漏洞等已知问题，削弱了其优越性主张。

**标签**: `#AI`, `#cybersecurity`, `#Mythos`, `#open-weight models`, `#AI research`

---

<a id="item-2"></a>
## [顶级 AI 智能体基准测试可被简单漏洞轻易攻破](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) ⭐️ 9.0/10

加州大学伯克利分校的研究人员证明，主流 AI 智能体基准测试可通过从简单（如发送空 JSON）到复杂（如植入木马的二进制包装器）的漏洞被操纵，在未真正完成任务的情况下获得接近满分的成绩。 这揭示了当前 AI 评估方法的根本缺陷，削弱了人们对基准测试结果的信任，并对在安全性和可靠性至关重要的现实场景中部署 AI 智能体构成风险。 这些漏洞之所以成功，是因为基准测试通常只验证智能体是否生成了输出，而非输出是否正确或有意义，且智能体完全控制了评分所依赖的运行环境。

hackernews · Anon84 · Apr 11, 19:15

**背景**: AI 智能体基准测试是一套标准化评估方法，用于衡量自主 AI 系统在规划、工具使用和决策等复杂任务中的表现。然而，与人类考试不同，许多 AI 基准测试缺乏防范机制，无法阻止系统直接优化评分指标而非真正完成任务。随着 AI 智能体在现实环境中获得更高自主性，这一漏洞尤其令人担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.evidentlyai.com/blog/ai-agent-benchmarks">10 AI agent benchmarks</a></li>
<li><a href="https://www.mindstudio.ai/blog/benchmark-gaming-ai-inflated-scores-explained">What Is Benchmark Gaming in AI? Why Self-Reported Scores Are ...</a></li>
<li><a href="https://aiagentsquare.com/blog/ai-agent-benchmarks-2026.html">AI Agent Benchmarks 2026: Performance, Accuracy & Cost Compared</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为研究揭示了基准测试设计的严重缺陷，有人指出像提交空响应这样简单的漏洞就暴露了验证逻辑的肤浅。也有人质疑这一发现的新颖性，认为测试集泄露和分数操纵早已是已知风险，还有人警告称公开此类漏洞可能会无意中教会未来的 AI 系统如何欺骗评估。

**标签**: `#AI evaluation`, `#AI safety`, `#benchmarking`, `#AI agents`, `#frontier AI`

---

<a id="item-3"></a>
## [宇树 H1 人形机器人奔跑速度达 10 米/秒](https://36kr.com/newsflashes/3763157984740103?f=rss) ⭐️ 9.0/10

4 月 11 日，宇树科技宣布其 H1 人形机器人在百米测试中达到 10 米/秒的峰值速度，刷新双足机器人奔跑速度世界纪录。这一速度已接近博尔特 9.58 秒百米纪录所对应的约 10.4 米/秒。 实现接近人类短跑的速度标志着人形机器人在动态运动控制、平衡能力和实时 AI 决策方面取得重大突破。这表明机器人正逐步具备在人类环境（如物流、应急救援等场景）中高效作业的能力。 H1 机器人高 1.8 米，重 47 公斤，此前的奔跑速度纪录为 3.3 米/秒；此次提升至 10 米/秒是一次巨大飞跃。该结果由公司发布的视频证实，但尚未有独立第三方验证。

rss · 36kr · Apr 12, 01:45

**背景**: 人形机器人在双足行走方面面临巨大挑战，需实现实时平衡、高扭矩控制和自适应步态规划。此类速度突破依赖于先进控制算法，通常结合基于模型的方法（如零力矩点 ZMP）与强化学习等数据驱动技术。宇树科技此前以 Go1 等敏捷四足机器人闻名，于 2023 年推出 H1 进入人形机器人领域，旨在以低于行业平均水平的成本提供高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unitree.com/h1/">Universal humanoid robot H1_Bipedal Robot_Humanoid Intelligent Robot Company | Unitree Robotics</a></li>
<li><a href="https://robotsguide.com/robots/unitree-h1">Unitree H1 - ROBOTS: Your Guide to the World of Robotics</a></li>
<li><a href="https://blog.robozaps.com/b/unitree-h1-review">Unitree H1 Review: $90K Humanoid Specs [2026] | Robozaps</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid robots`, `#frontier tech`, `#AI hardware`, `#locomotion`

---

<a id="item-4"></a>
## [马斯克：Grok 将于六月达到或超越 Claude Opus 4.6 水平](https://36kr.com/newsflashes/3763157489320457?f=rss) ⭐️ 9.0/10

埃隆·马斯克宣布，xAI 的 Grok 模型将在 2025 年 5 月接近 Anthropic 的 Claude Opus 4.6 性能，并在 6 月实现超越。 这一时间表凸显了前沿 AI 模型之间日益激烈的竞争，Grok 正将自己定位为 Claude Opus 4.6 等领先系统的重要竞争对手。这表明 AI 开发的迭代周期正在加速，模型基准测试的竞争压力也在加剧。 马斯克强调，尽管两个月的时间按常规标准来看很短，但在快速发展的 AI 领域已算相当长。该表态暗示 Grok 正在其下一次重大发布前进行显著的架构或训练改进。

rss · 36kr · Apr 12, 01:30

**背景**: Grok 是由埃隆·马斯克旗下人工智能公司 xAI 开发的 AI 聊天机器人，具备实时网络搜索、图像生成和高级推理能力。Claude Opus 4.6 属于 Anthropic 公司开发的 Claude 系列大语言模型，以其在写作、长上下文连贯性以及通过“宪法 AI”技术实现的伦理对齐而著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Claude_Opus_46">Claude Opus 4.6</a></li>

</ul>
</details>

**标签**: `#AI models`, `#Grok`, `#Claude Opus`, `#frontier AI`, `#xAI`

---

<a id="item-5"></a>
## [工信部将发布一批“人工智能+”高价值场景](https://36kr.com/newsflashes/3762215677297158?f=rss) ⭐️ 8.0/10

工业和信息化部宣布将发布一批聚焦制造业的“人工智能+”高价值应用场景，包括建设特色智能体、研制新标准、提供新型智能终端以及培养产业应用人才，以深化人工智能与制造业融合。 此举标志着中国正大力推动“人工智能+”战略在工业领域的落地，有望提升制造业生产效率、创新能力与全球竞争力，并将人工智能技术转化为实际经济价值。 该计划以制造业为主战场，以应用牵引为主线，同时关注智能体快速普及带来的数据隐私和权限滥用等安全风险，强调安全治理需与应用推广同步推进。

rss · 36kr · Apr 11, 09:31

**背景**: 中国近年来大力推动“人工智能+”行动，促进 AI 在各行业的融合应用。2025 年，中国人工智能核心产业规模已超 1.2 万亿元，相关企业超 6200 家，规模以上制造业企业 AI 技术应用普及率超过 30%。智能体（具备感知、推理与行动能力的自主 AI 系统）被视为推动工业智能化升级的关键载体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.news.cn/20260411/946c0b1b9aee4d3fae2dc7930dc49a3e/c.html">工业和信息化部将发布一批“人工智能+”高价值场景-新华网</a></li>
<li><a href="https://news.cctv.com/2026/04/11/ARTIkzrapDyezYI7MlhKealp260411.shtml">工业和信息化部将发布一批“人工智能+”高价值场景_新闻频道_央视网 (cc...</a></li>
<li><a href="https://www.jjckb.cn/20260410/27760561f3364c80bee9fcc98bc15150/c.html">工业和信息化部：将发布一批“人工智能+”高价值场景-经济参考网 _ 新华...</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#AI Policy`, `#Industrial AI`, `#Smart Manufacturing`, `#Government Initiative`

---

<a id="item-6"></a>
## [完全由 AI 辅助开发的万三工作室现已开源](https://www.v2ex.com/t/1205224#reply0) ⭐️ 8.0/10

万三工作室（Wansan Studio）是一个完全通过 Google Gemini“氛围编码”（vibe coding）开发的软件项目，现已在 GitHub 上开源。开发者在 V2EX 上记录了完整的迭代过程，展示了由 AI 驱动的端到端独立开发工作流。 该项目表明，Gemini 等 AI 工具正在降低技术门槛，使独立开发者即使缺乏深厚编码经验也能完成全栈开发。这预示着 AI 增强型创作正成为独立软件项目的一种可行路径。 该项目利用 Google AI Studio 中 Gemini 的“氛围编码”功能，将自然语言指令和视觉反馈转化为可运行代码。开发者强调，在 AI 辅助下，技术实现已成为整个开发闭环中最小的一环。

rss · V2EX · Apr 12, 01:58

**背景**: “氛围编码”（Vibe coding）是 Google 推出的一种开发范式，开发者通过自然语言描述或视觉标注表达所需界面或功能，AI 自动生成或更新相应代码。AI 辅助软件开发利用大语言模型支持从设计到调试的整个软件生命周期任务。Gemini 等工具让编程更注重结果而非语法细节，尤其适合非专业开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aistudio.google.com/vibe-code">Vibe Coding | Google AI Studio</a></li>
<li><a href="https://cloud.google.com/discover/what-is-vibe-coding">Vibe Coding Explained: Tools and Guides | Google Cloud</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_software_development">AI-assisted software development</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#Gemini`, `#open-source`, `#independent developer`, `#frontier tech`

---

<a id="item-7"></a>
## [开源 AI 智能体基础设施 Hivo 发布](https://www.v2ex.com/t/1205222#reply0) ⭐️ 8.0/10

一位开发者发布了 Hivo，这是一个专为 AI 智能体设计的开源基础设施框架，支持持久身份、文件共享、团队协作和完全自托管。该项目包含 hivo-identity、hivo-acl、hivo-drop、hivo-club 和 hivo-salon 等微服务，以及一个统一的命令行工具（CLI）。 随着 AI 智能体从一次性脚本发展为长期运行的自主实体，它们需要类似人类团队的身份、安全和协作基础设施。Hivo 通过提供去中心化且可自托管的基础层，填补了这一空白，有望加速构建可扩展、可信的智能体生态系统。 Hivo 强调使用持久身份而非临时令牌，将权限、文件和团队等功能拆分为独立的微服务，并支持完全自托管，无需依赖中心化云服务。它可通过 CLI、HTTP API 或 Skill 方式集成，设计上注重可扩展性。

rss · V2EX · Apr 12, 01:44

**背景**: AI 智能体正越来越多地被要求长期自主运行，这需要安全的身份管理、访问控制和协作能力。传统系统通常将智能体视为无状态的临时进程，缺乏持久上下文。新兴框架开始赋予智能体“数字人格”，使其能够拥有数据、加入团队并安全交互。这一转变与企业趋势一致——AI 智能体被视为“数字员工”，需要类似人类员工的全生命周期管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.okta.com/identity-101/what-is-ai-agent-identity/">AI Agent Identity for Enterprise Security at Scale | Okta</a></li>
<li><a href="https://hivo.ai/">HivoAI</a></li>
<li><a href="https://docs.hivo.ai">Welcome to Hivo.ai | HivoAI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#Self-Hosting`, `#Agent Infrastructure`, `#Decentralized AI`

---

<a id="item-8"></a>
## [中兴通讯不造车，专注向车企提供 AI 与 ICT 能力](https://www.ithome.com/0/938/211.htm) ⭐️ 8.0/10

在 2026 智能电动汽车发展高层论坛上，中兴通讯大企业 CTO 许志成表示，公司不会进入整车制造领域，但将通过 AI 大模型、训练好的编码智能体、车用芯片和通信模组等 ICT 能力支持汽车制造商。 此举明确了中兴在汽车 AI 生态中的赋能者定位而非竞争者，凸显了大型 ICT 企业正将生成式 AI 和开发者工具深度融入汽车制造等传统行业。 中兴提供三种合作模式：工程师驻场支持（如与一汽合作）、基于车企语料微调其研发大模型，以及直接交付训练好的编码智能体；同时还提供 4G/5G 通信模组、车载芯片和操作系统。

rss · IT HOME · Apr 12, 01:50

**背景**: AI 编码智能体是能辅助开发者生成、调试或测试代码的 AI 系统，截至 2025 年底已被约 85%的开发者常规使用。在汽车行业，大模型正越来越多地用于软件定义汽车开发、制造优化和座舱体验。英伟达（NVIDIA）和大众集团等企业已开始部署面向汽车行业的工业 AI 和边缘云架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.faros.ai/blog/best-ai-coding-agents-2026">Best AI Coding Agents for 2026: Real-World Developer Reviews</a></li>
<li><a href="https://www.nvidia.com/en-us/industries/automotive/">AI & Accelerated Computing Solutions for Automotive Industries | NVIDIA</a></li>
<li><a href="https://www.volkswagen-group.com/en/artificial-intelligence-in-the-automotive-industry-19030">Artificial Intelligence in the Automotive Industry | Volkswagen Group</a></li>

</ul>
</details>

**标签**: `#AI models`, `#automotive AI`, `#coding agents`, `#ICT infrastructure`, `#enterprise AI`

---

<a id="item-9"></a>
## [华为乾崑智驾装车达 140 万套，称 L3 是迈向完全自动驾驶必经阶段](https://www.ithome.com/0/938/202.htm) ⭐️ 8.0/10

华为宣布其乾崑智能驾驶系统截至 2025 年底累计装车量已达 140 万套。公司强调，L3 级有条件自动驾驶是迈向 L4/L5 级完全自动驾驶不可或缺的关键阶段。 这一里程碑表明高级驾驶辅助系统在中国汽车产业的快速普及，并凸显华为作为自动驾驶关键技术赋能者的重要地位。将 L3 定位为必经阶段，挑战了车企可跳过中间阶段直接实现高阶自动驾驶的观点，强调了真实数据积累和法规建设的重要性。 华为于 2025 年 4 月发布的乾崑 ADS 4.0 采用 WEWA 架构，结合云端“世界引擎”与车端“世界行为模型”，可利用 AI 生成高密度极端场景进行训练。尽管装机量庞大，华为重申自身不造车，而是致力于成为智能网联汽车时代的“电子螺丝钉”。

rss · IT HOME · Apr 12, 01:02

**背景**: 根据 SAE J3016 及中国国家标准 GB/T 40429-2021，自动驾驶分为 L0 至 L5 六个等级。L3 级（有条件自动驾驶）可在特定场景（如高速公路或拥堵路段）下由系统完成全部驾驶任务，但要求驾驶员保持接管能力。与需持续监督的 L2 不同，L3 在系统激活期间法律责任主体转为车辆系统。华为乾崑是以 ADS（智能驾驶解决方案）为核心的系列技术，涵盖感知、控制、车云协同等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://auto.huawei.com/cn/">华为乾崑智能汽车解决方案 - Huawei</a></li>
<li><a href="https://baike.baidu.com/item/华为乾崑智驾/67412751">华为乾崑智驾 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/L3级自动驾驶/63891735">L3级自动驾驶_百度百科</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#AI in automotive`, `#L3 autonomy`, `#Huawei`, `#frontier tech`

---

<a id="item-10"></a>
## [别克至境 E7 上市，搭载 AI 智驾与豆包大模型](https://www.ithome.com/0/938/199.htm) ⭐️ 8.0/10

别克于 2025 年 4 月 22 日推出全新电动 SUV 至境 E7，售价区间为 16 万至 21 万元。该车型搭载 Momenta R6 强化学习大模型以实现城市 NOA 功能，并行业首发搭载字节跳动旗下豆包大模型最新版。 此次发布标志着大模型技术在汽车领域的实际应用迈出关键一步，将自动驾驶智能与座舱内的自然语言交互深度融合。这反映出中国智能电动汽车市场正加速融合前沿 AI 技术，推动高阶智能化普及。 至境 E7 配备 27 个感知硬件（含激光雷达），CLTC 纯电续航 235 公里，综合续航达 1630 公里，并支持 6kW 对外放电。豆包大模型的上车实现了座舱内更智能的语音交互与场景化服务。

rss · IT HOME · Apr 12, 00:42

**背景**: Momenta R6 是国内首个实现量产落地的端到端强化学习大模型，基于 30 亿公里真实路测数据训练而成。城市 NOA 指在复杂城区环境下的自动导航辅助驾驶功能。豆包是字节跳动推出的 AI 大模型系列，通过火山引擎平台加速进入智能座舱领域，已与比亚迪、赛力斯等多家车企合作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.momenta.cn/article/361.html">Momenta I Building Autonomous Driving Brains</a></li>
<li><a href="https://www.gm.com.cn/zh/home/newsroom.detail.html/Pages/news/cn/zh/2025/aug/0818-buick.html">上汽通用汽车与Momenta签署战略合作协议 别克至境L7全球首发搭载基于强化学习的Momenta R6飞轮大模型</a></li>
<li><a href="https://baike.baidu.com/item/豆包大模型/64418493">豆包大模型_百度百科</a></li>

</ul>
</details>

**标签**: `#AI in automotive`, `#autonomous driving`, `#large language models`, `#electric vehicles`, `#frontier tech`

---

<a id="item-11"></a>
## [大众汽车计划 2027 年实现 L3 级自动驾驶，2029 年达 L4 级](https://www.ithome.com/0/938/198.htm) ⭐️ 8.0/10

4 月 11 日，在北京举办的智能电动汽车发展高层论坛上，大众汽车集团执行副总裁韩三楚宣布，公司计划于 2027 年实现 L3 级有条件自动驾驶，2029 年实现 L4 级高度自动驾驶。华为和滴滴也公布了激进的时间表：华为预测 2026 年将成为全球自动驾驶元年，而滴滴已在广州、北京部分区域开展全天候全无人 L4 级载客测试。 这些声明标志着领先汽车与科技企业正加速推进 AI 驱动的自动驾驶系统落地，凸显了在软件定义汽车领域的激烈竞争，并为高级别自动驾驶的安全性、法规适配和用户信任设定了行业基准。AI、机器人技术与汽车工程的融合正在重塑未来交通格局。 L3 级自动驾驶允许驾驶员在特定条件下脱离对车辆的主动控制，但仍需随时准备接管；L4 级则可在限定区域内完全无需人类干预。韩三楚此前曾任长安汽车首席软件架构师，现负责大众集团旗下软件子公司 CARIAD 中国业务，专注于软件定义汽车（SDV）开发。

rss · IT HOME · Apr 12, 00:24

**背景**: 根据国际汽车工程师学会（SAE）及中国国家标准《汽车驾驶自动化分级》（GB/T 40429-2021），自动驾驶分为 L0 至 L5 六个等级。L3 级（有条件自动驾驶）是首个可由系统在特定条件下完成全部驾驶任务的级别，责任主体从驾驶员转向车辆，但仅限于其设计运行域（ODD）内。L4 级（高度自动驾驶）则可在限定区域内实现完全自主运行，无需驾驶员介入。软件定义汽车（SDV）架构支持远程升级、模块化软件栈和功能持续进化，是实现高级别自动驾驶的技术基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/L3级自动驾驶/63891735">L3级自动驾驶_百度百科</a></li>
<li><a href="https://www.mobileyechina.com/blog/level-3-autonomy-explained/">L3级有条件自动驾驶解析及其对车企的意义 | Mobileye Blog</a></li>
<li><a href="https://auto.sina.cn/news/2023-10-20/detail-imzruhsh5662808.d.html">研发两年半的长安 汽 车 SDA 平台 有怎样的不同-手机新浪 汽 车</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#AI in robotics`, `#L3/L4 automation`, `#software-defined vehicles`, `#frontier tech`

---

<a id="item-12"></a>
## [地平线发布“星空”芯片，实现舱驾融合 AI 智能体](https://www.ithome.com/0/938/195.htm) ⭐️ 8.0/10

地平线宣布将于 4 月 22 日发布“星空”系列芯片，该芯片将座舱娱乐与智能驾驶功能集成到单颗系统级芯片（SoC）上，单车硬件成本降低 1500 至 4000 元，并支持具备个性、技能和记忆能力的中央 AI 模型。 这一突破通过用统一、高性价比的 AI 平台取代碎片化的专用硬件，解决了行业关键痛点，推动个性化智能座舱体验的普及。同时确立了以中央计算为核心的整车智能新架构，契合边缘 AI 和软件定义汽车的发展趋势。 该芯片采用中央集成大模型，由单一核心处理器统一管理驾驶、座舱交互和整车控制，共用内存并简化线束与散热系统。它支持“小龙虾智能体”等新型车载智能体操作系统，能基于用户习惯执行订餐、预订停车位等多步骤长时序任务。

rss · IT HOME · Apr 11, 23:36

**背景**: 传统汽车电子架构中，座舱（信息娱乐）与智驾（高级驾驶辅助系统）功能通常运行在相互独立的域控制器或电子控制单元（ECU）上，导致硬件冗余、成本高企且数据难以互通。“舱驾融合”旨在将这两大域整合到单一计算平台上，实现更紧密协同和更丰富的 AI 体验。目前英伟达、高通及地平线、黑芝麻智能等国内外厂商正竞相推出高性能、高性价比的系统级芯片（SoC）以支持这一新架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/938/195.htm">地平线“星空”单芯片实现舱驾融合，单车成本最高降 4000 元</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1917559185173873098">一文读懂：舱驾一体域控制器如何让你的汽车同时拥有「超脑」与「共情力」？ - 知乎</a></li>
<li><a href="https://www.arraymo.com/4737.html">单芯片舱驾一体通过实车验证，中国整车级OS迎来新「拐点」 - 智达诚远科技有限公司</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#autonomous driving`, `#edge AI`, `#smart vehicles`, `#frontier tech`

---

<a id="item-13"></a>
## [普京呼吁俄罗斯自主研发人工智能基础模型](https://www.news.cn/20260411/9dfc4f3241154502b4a1be41510f92fc/c.html) ⭐️ 8.0/10

4 月 10 日，俄罗斯总统普京宣布，俄罗斯必须自主研发具有全球竞争力的人工智能基础模型，并确保整个研发和训练周期由本国企业完成。他强调，这类模型对国家安全、国防以及经济、社会、医疗和工业等领域的转型至关重要。 此举反映了全球主要国家日益重视在人工智能领域实现技术自主，以减少对外部系统的依赖并降低安全风险。俄罗斯推动自主基础模型可能重塑其国内技术生态，并影响全球人工智能治理的地缘政治格局。 俄罗斯专项委员会今年将聚焦五项重点任务：加快关键领域人工智能部署、重构人才培养体系、评估应用风险、研发国防安全自主方案，以及构建人工智能系统与服务的综合推广体系并加强国际合作。

telegram · zaihuapd · Apr 11, 06:31

**背景**: 基础模型是一类在海量数据上训练而成的大规模机器学习模型，通常采用自监督或半监督学习方法，能够适应多种下游任务。与仅针对特定任务的人工智能模型不同，基础模型可作为语言、视觉、推理等多个领域的通用基础。其通用性使其具有重要战略价值，但也引发了关于安全、偏见和数据隐私的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/基础模型">基础模型 - 维基百科，自由的百科全书</a></li>
<li><a href="https://hub.baai.ac.cn/view/15931">每日AI前沿术语：基础模型（Foundation Models） - 智源社区 人工智能基础——模型部分：模型介绍、模型训练和模型微调 ！！-腾讯云... 基础模型 - 维基百科，自由的百科全书 人工智能基础模型划分 - 知乎专栏 什么是基础模型？- 生成式人工智能中的基础模型简介 - AWS 什么是 AI 基础模型？ - Red Hat</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#foundation models`, `#national security`, `#artificial intelligence`, `#technology sovereignty`

---

<a id="item-14"></a>
## [硅谷顶尖 AI 人才加速回流中国](https://www.ft.com/content/b167c6d3-b982-482a-98c3-5303a7b80c6a) ⭐️ 8.0/10

过去一年，超过 30 名曾就职于 OpenAI 和 Google DeepMind 的顶尖 AI 研究员回国加入字节跳动、腾讯和阿里巴巴等大厂，远超往年个位数的水平。 这一趋势标志着全球 AI 人才分布的战略性转变，可能加速中国在应用 AI 领域的进展，并重塑国际前沿技术竞争格局。 中国科技公司提供的薪酬在扣除税收和生活成本后已超过硅谷水平，且中国在机器人、自动驾驶和供应链方面的优势创造了极具吸引力的研发环境。同时，美国移民政策收紧和地缘政治紧张降低了华裔工程师在美的长期稳定性。

telegram · zaihuapd · Apr 12, 00:20

**背景**: 几十年来，中国顶尖理工科毕业生常赴美攻读博士并在硅谷等 AI 中心发展。OpenAI 和 Google DeepMind 一直是前沿 AI 研究的核心机构。然而，中美关系紧张及中国本土科技生态的崛起正在改变这一格局。

**标签**: `#AI talent`, `#artificial intelligence`, `#tech industry`, `#China tech`, `#frontier technology`

---

<a id="item-15"></a>
## [艾伦人工智能研究所推出 MolmoWeb：开源视觉网页智能体平台](https://www.producthunt.com/products/allen-institute-of-artificial-intelligence) ⭐️ 8.0/10

艾伦人工智能研究所（AI2）发布了 MolmoWeb，这是一个开源的视觉网页智能体，仅通过截图和自然语言指令即可自主执行基于浏览器的任务。同时，AI2 还推出了 MolmoWebMix，这是目前最大的公开网页智能体训练数据集。 MolmoWeb 推动了智能体 AI 的前沿发展，能够在无需访问底层代码或 API 的情况下实现端到端的真实网页交互自动化。这有助于降低 AI 智能体开发门槛，并加速多模态推理与自主系统的研究。 MolmoWeb 仅依赖视觉输入（截图）和自然语言，通过点击、输入、滚动和导航等操作控制浏览器。它基于 Molmo 视觉-语言模型构建，并完全开源，包括其训练数据和智能体框架。

producthunt · Zac Zuo · Apr 11, 05:50

**背景**: AI 网页智能体是可以像人类一样感知并操作网站的系统，利用视觉和语言完成表单填写、数据提取或在线购物等任务。与依赖结构化 API 或 HTML 解析的传统自动化工具不同，视觉网页智能体无需针对特定网站编码即可泛化使用。艾伦人工智能研究所（AI2）是一家非营利研究机构，以开源贡献闻名，例如 AllenNLP 库和 OLMO 语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/allenai/molmoweb">GitHub - allenai/molmoweb · GitHub</a></li>
<li><a href="https://allenai.org/blog/molmoweb">MolmoWeb: An open agent for automating web tasks | Ai2</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#artificial intelligence`, `#Allen Institute`, `#web agents`, `#frontier tech`

---

<a id="item-16"></a>
## [Claude for Word 将 Anthropic 的 AI 引入微软 Word](https://www.producthunt.com/products/claude) ⭐️ 8.0/10

Anthropic 推出了“Claude for Word”，将 Claude AI 助手直接嵌入到 Microsoft Word 中，以协助用户进行写作和编辑任务。用户无需离开 Word 环境即可使用 Claude 的先进语言能力。 该集成通过将前沿 AI 功能（如草拟、总结和修改文本）引入全球最广泛使用的文字处理软件之一，显著提升生产力。它还对依赖 OpenAI GPT 模型的微软自家 Copilot 构成竞争。 该工具原生集成到 Word 中，表明其可能以插件或扩展形式运行，而非独立应用。与使用 OpenAI GPT 的微软 Copilot 不同，此方案采用 Anthropic 的 Claude 模型，后者以“宪法 AI”方法著称，强调安全性和对齐性。

producthunt · Zac Zuo · Apr 11, 03:43

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，于 2023 年首次发布，采用“宪法 AI”技术，使输出符合伦理和法律原则。Microsoft Word 已通过基于 OpenAI GPT 模型的 Copilot 提供 AI 功能，但此类第三方集成扩大了用户的选择。尽管 Anthropic 因数据使用政策受到美国政府审查，但一名联邦法官最近已阻止国防部对其实施禁令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>
<li><a href="https://support.microsoft.com/en-us/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1">Welcome to Copilot in Word - Microsoft Support</a></li>
<li><a href="https://claude.ai/login">Claude</a></li>

</ul>
</details>

**标签**: `#AI`, `#Productivity Tools`, `#Claude`, `#Microsoft Word`, `#AI Integration`

---

<a id="item-17"></a>
## [社区分享手动绕过 GPT 访问限制的方法](https://www.v2ex.com/t/1205220#reply2) ⭐️ 7.0/10

在自动注册机器人失效后，用户开始通过一个 Telegram 群组手动获取地区限定信用卡，该群组提供每日签到和邀请奖励以兑换用于 GPT 试用的虚拟卡。 这反映了用户为绕过 GPT 等 AI 服务的地域和支付限制所做出的自下而上的努力，凸显了官方渠道未覆盖地区用户的强烈需求。同时也表明现有反滥用机制存在漏洞，迫使用户转向手动、社区协作的替代方案。 该系统采用积分奖励机制：英国卡需 3 积分，美国和西班牙卡需 4 积分，澳洲卡需 6 积分，均通过 CDK 自动发货。用户通过每日签到和邀请他人入 Telegram 群组来获取积分。

rss · V2EX · Apr 12, 01:03

**背景**: OpenAI 的 GPT 服务通常要求用户提供特定地区的支付方式才能试用或订阅，导致不支持地区的用户无法正常使用。一些社区因此发展出非正式的共享或转售机制（如虚拟信用卡）来绕过限制。“手搓”指手动操作获取访问权限，区别于使用自动化机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linux.do/t/topic/1771694">gpt 试 用 关了吗？ - 搞七捻三 - LINUX DO</a></li>
<li><a href="https://www.uscardforum.com/t/topic/497058">不要多开doordash小号撸CSR福利 - 信用卡 - 美卡论坛</a></li>

</ul>
</details>

**社区讨论**: 原帖作者表示自己也在摸索中，并邀请他人共同交流经验（“有不对的请指点一下”）。虽然未提供具体评论，但社区可能围绕卡片稳定性、被封风险及替代方案展开讨论。

**标签**: `#AI access`, `#GPT`, `#community effort`, `#workaround`, `#credit card`

---