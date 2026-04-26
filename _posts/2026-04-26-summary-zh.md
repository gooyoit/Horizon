---
layout: default
title: "Horizon Summary: 2026-04-26 (ZH)"
date: 2026-04-26
lang: zh
---

> From 78 items, 20 important content pieces were selected

---

1. [OpenAI 将 Codex 并入 GPT-5.5，大幅提升智能体编程能力](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-5.5 提示工程指南](#item-2) ⭐️ 9.0/10
3. [OpenAI 推出 GPT-5.5 生物安全漏洞赏金计划，奖金 2.5 万美元](#item-3) ⭐️ 9.0/10
4. [谷歌拟向 Anthropic 投资至多 400 亿美元](#item-4) ⭐️ 9.0/10
5. [AI 在混乱图像中自发添加“你为啥这样”路牌](#item-5) ⭐️ 8.0/10
6. [中国公司量产微米级磁悬浮魔毯输送系统](#item-6) ⭐️ 8.0/10
7. [DeepSeek-V4-Pro 模型 API 限时 2.5 折优惠至 2026 年 5 月](#item-7) ⭐️ 8.0/10
8. [润芯微发布国产软硬一体 AI 智能基座](#item-8) ⭐️ 8.0/10
9. [卡尔动力发布 KargoBot Inside 进军 L4 自动驾驶货运](#item-9) ⭐️ 8.0/10
10. [海康机器人 2025 年营收超 64 亿，加码 AI 融合与具身智能](#item-10) ⭐️ 8.0/10
11. [用户寻求可在 32GB MacBook Air M5 上运行的 MoE 大模型](#item-11) ⭐️ 8.0/10
12. [三大主流大模型在复杂成本优化问题中集体失利](#item-12) ⭐️ 8.0/10
13. [免费网站集成 GPT-image-2 与 Grok 生成图片和视频](#item-13) ⭐️ 8.0/10
14. [Momenta CEO 预判智驾市场将加速整合](#item-14) ⭐️ 8.0/10
15. [东风风行星海 V6 搭载华为乾崑智驾亮相](#item-15) ⭐️ 8.0/10
16. [AI 需求致苹果 M4 Mac mini 基础款缺货](#item-16) ⭐️ 8.0/10
17. [Anthropic 推出真实货币 AI 智能体交易实验](#item-17) ⭐️ 8.0/10
18. [湖南 AI 中心落地湘江新区](#item-18) ⭐️ 7.0/10
19. [本周产品榜单聚焦 AI 工具与知识管理平台](#item-19) ⭐️ 7.0/10
20. [问界 M9 三天预订量突破 25000 台](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 将 Codex 并入 GPT-5.5，大幅提升智能体编程能力](https://simonwillison.net/2026/Apr/25/romain-huet/#atom-everything) ⭐️ 9.0/10

OpenAI 从 GPT-5.4 开始将 Codex 编程模型与主 GPT 系列统一，GPT-5.5 在智能体编程、计算机操作及通用计算机任务执行方面展现出显著提升。 这一整合消除了对专用编程模型的需求，简化了 AI 开发工作流，并使 AI 智能体能够端到端地自主处理复杂的软件工程任务，推动开发自动化迈向新阶段。 据 Romain Huet 表示，将不会发布 GPT-5.5-Codex 版本，因为 Codex 的能力现已完全内嵌于基础 GPT-5.5 模型中；该系统采用统一架构，同时优化了通用推理和代码生成能力。

rss · Simon Willison · Apr 25, 12:06

**背景**: OpenAI Codex 于 2025 年 4 月首次发布，是一款专为编写和调试代码等软件工程任务设计的 AI 智能体。智能体编程（agentic coding）指 AI 系统能根据高层指令自主规划、编写、测试和修改代码，其操作单位是整个项目而非单个代码行。GPT-5.5（代号“Spud”）于 2026 年 4 月 23 日发布，在 Terminal-Bench 2.0 等基准测试中表现优异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases</a></li>

</ul>
</details>

**标签**: `#generative-ai`, `#gpt`, `#openai`, `#ai`, `#llms`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.5 提示工程指南](https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/#atom-everything) ⭐️ 9.0/10

OpenAI 为其新模型 GPT-5.5（现已通过 API 提供）发布了官方提示工程指南，并推荐使用 Codex 的 $openai-docs 技能来改善用户体验和迁移现有代码。 该指南对从旧版 GPT 模型升级的开发者至关重要，因为 OpenAI 明确建议不要将 GPT-5.5 视为直接替代品，而是应从头重新设计提示，以充分发挥其更强的推理能力。 指南建议在多步骤任务中立即发送用户可见的更新，并提供迁移命令“$openai-docs migrate this project to gpt-5.5”，该命令遵循包含轻量级提示重写的升级路径；GPT-5.5 还支持可配置的推理强度级别（从 none 到 xhigh）。

rss · Simon Willison · Apr 25, 04:13

**背景**: GPT-5.5 是 OpenAI 于 2026 年 4 月发布的前沿模型，专为复杂专业任务设计，具有更少的幻觉和更强的推理能力。它提供“Thinking”和“Pro”等变体，定价更高以反映其先进性能。Codex 编码代理集成了 openai-docs 等技能，可实现自动化代码升级和工具辅助开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.5">GPT - 5 . 5 Model | OpenAI API</a></li>
<li><a href="https://apidog.com/blog/what-is-gpt-5-5/">What Is GPT - 5 . 5 ? OpenAI's New Frontier Model Explained</a></li>
<li><a href="https://developers.openai.com/codex/skills">Agent Skills – Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#GPT-5.5`, `#AI prompting`, `#OpenAI`, `#frontier AI`, `#large language models`

---

<a id="item-3"></a>
## [OpenAI 推出 GPT-5.5 生物安全漏洞赏金计划，奖金 2.5 万美元](https://www.ithome.com/0/943/558.htm) ⭐️ 9.0/10

2026 年 4 月 23 日，OpenAI 启动了一项漏洞赏金计划，向首位发现通用越狱方法的研究人员提供 2.5 万美元奖励，该方法需让 GPT-5.5 在不触发内容审核机制的情况下回答全部五道生物安全挑战题。 该计划回应了前沿 AI 模型可能被滥用于生成有害生物知识的日益增长的担忧，体现了业界通过红队测试和外部审查主动缓解灾难性风险的努力。它也为高能力 AI 系统在敏感领域的负责任部署树立了先例。 测试仅限于 Codex Desktop 中的 GPT-5.5 模型，要求使用一个通用提示词在干净对话环境中通过全部五道生物安全挑战题，且全程受保密协议约束，并采用申请加邀请制。测试阶段从 2026 年 4 月 28 日持续至 7 月 27 日。

rss · IT HOME · Apr 25, 23:06

**背景**: GPT-5.5（代号“Spud”）是 OpenAI 于 2026 年 4 月 23 日发布的最新大语言模型，具备更强的推理能力和更高效率。AI 生物安全旨在防止 AI 系统被滥用于设计或制造危险生物制剂。红队测试是由可信专家进行的对抗性评估，用于在模型公开前发现潜在漏洞。美国近期政策（包括拜登总统的 AI 行政命令）明确要求评估 AI 带来的生物安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>
<li><a href="https://www.nti.org/analysis/articles/statement-on-biosecurity-risks-at-the-convergence-of-ai-and-the-life-sciences/">Statement on Biosecurity Risks at the Convergence of AI and the Life Sciences</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#GPT-5.5`, `#Red Teaming`, `#Biosecurity`, `#OpenAI`

---

<a id="item-4"></a>
## [谷歌拟向 Anthropic 投资至多 400 亿美元](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic) ⭐️ 9.0/10

谷歌计划向人工智能公司 Anthropic 投资最多 400 亿美元，其中包括以 3500 亿美元估值进行的 100 亿美元现金注资，以及在达成业绩目标后追加的 300 亿美元。该协议还包括五年内提供 5 吉瓦计算能力，并支持 Anthropic 使用谷歌最新的 TPU 芯片。 这项投资极大增强了 Anthropic 在前沿人工智能领域的地位，并使谷歌在自身 Gemini 模型之外进一步巩固了在大语言模型生态中的战略布局。此举还加剧了与微软（支持 OpenAI）和亚马逊（近期向 Anthropic 追加 50 亿美元投资）的竞争，重塑了 AI 基础设施格局。 这 400 亿美元包括直接现金投资和通过云计算及 TPU 使用权提供的大量实物支持；5 吉瓦的电力承诺反映了 AI 训练基础设施前所未有的规模。Anthropic 还计划最早于 2026 年 10 月进行首次公开募股（IPO）。

telegram · @zaihuapd · Apr 25, 11:02

**背景**: Anthropic 是一家以 AI 安全为核心理念的领先公司，以其 Claude 系列大语言模型著称，其中包括近期发布的 Claude Code——一种智能编程代理工具，可在终端或 IDE 中直接协助开发者编写代码，同时保留人类对关键决策的控制权。谷歌的 TPU（张量处理单元）是专为机器学习任务定制的 AI 加速芯片；最新第八代 TPU 8t 和 TPU 8i 由谷歌与 DeepMind 联合设计，分别面向前沿模型训练和大规模推理任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system</a></li>
<li><a href="https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive">TPU 8t and TPU 8i technical deep dive | Google Cloud Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Google`, `#Frontier Models`, `#Cloud Compute`

---

<a id="item-5"></a>
## [AI 在混乱图像中自发添加“你为啥这样”路牌](https://simonwillison.net/2026/Apr/25/why-are-you-like-this/#atom-everything) ⭐️ 8.0/10

OpenAI 的 ChatGPT Images 2.0 根据用户提示生成了一幅混乱图像：一只鹈鹕骑着自行车，上面叠着一名宇航员和一匹马，并自发在背景中添加了一个写着“WHY ARE YOU LIKE THIS”的路牌。原始提示并未包含该路牌，证实是模型自主添加的。 这表明先进的多模态 AI 模型可能生成出人意料且带有语义负载的元素，反映出其内部偏见或训练数据中的痕迹，引发人们对生成式 AI 可控性与可解释性的担忧。随着这些模型被用于需要可靠性和连贯性的现实场景，此类怪异行为愈发值得关注。 该图像由 ChatGPT Images 2.0 生成，OpenAI 称其具备改进的文本渲染和视觉推理能力；然而，模型自发添加了语境荒谬但语义通顺的文本“WHY ARE YOU LIKE THIS”，表明它可能过度解读提示或幻觉出叙事元素。尽管技术进步，AI 图像生成器在文本一致性和构图逻辑方面仍存在挑战。

rss · Simon Willison · Apr 25, 16:44

**背景**: 像 ChatGPT Images 2.0 这样的文生图模型通过扩散过程，依据语言提示生成图像。这些模型在海量图文对数据上训练，学习的是统计关联而非真实理解。一个已知弱点是在图像中生成清晰且符合语境的文本，尽管最新版本已有改进。如今，MMMU 等基准测试开始评估多模态模型在跨学科复杂推理任务上的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2.0 - OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2409.18142">A Survey on Multimodal Benchmarks: In the Era of Large AI Models MMMU-Pro Benchmark Leaderboard - Artificial Analysis BenchGeckoAI/ai-model-benchmarks-2026 - Hugging Face LLM Leaderboard 2026 — Compare 220 AI Models Across 178 ... MMMU: A Massive Multi-discipline Multimodal Understanding and ... A Deep Dive into Multimodal AI Benchmarks: Measuring Vision ... Evaluation Benchmarks for Large Multimodal Models</a></li>
<li><a href="https://lifehacker.com/tech/chatgpt-update-renders-highly-realistic-text">ChatGPT's Latest Update Makes It Harder Than Ever to Spot AI-Generated Images | Lifehacker</a></li>

</ul>
</details>

**标签**: `#AI image generation`, `#multimodal AI`, `#frontier models`, `#AI evaluation`, `#ChatGPT`

---

<a id="item-6"></a>
## [中国公司量产微米级磁悬浮魔毯输送系统](https://36kr.com/p/3782960065108996?f=rss) ⭐️ 8.0/10

总部位于广东佛山的增广智能成为全球第二家、中国唯一一家实现六自由度平面磁悬浮输送系统大规模量产的企业，该系统具备微米级定位精度和最高 2G 加速度。 该技术通过用智能无接触“磁悬浮魔毯”取代传统刚性传送带，实现了柔性与效率兼得的高速工业自动化，支持实时调度和运动中工艺执行，对下一代智能制造和具身智能发展具有重要意义。 系统采用自研微秒级通信协议，在 50 微秒内同步上万个驱动器；仅通过磁场计算即可实现无需编码器的六维微米级定位；每个动子本身也是六维力传感器，并基于强化学习的 AI 算法实现智能调度。

rss · 36kr · Apr 26, 01:06

**背景**: 平面磁悬浮输送系统（如德国倍福的 XPlanar）利用电磁场使载具（称为动子）在平面上无接触悬浮并多自由度运动。与传统传送带不同，它允许多个动子独立、无碰撞地运行，实现产线动态重构。六自由度（6DOF）指物体在三维空间中的三个平移方向（X、Y、Z）和三个旋转方向（俯仰、偏航、滚转），对复杂装配至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.beckhoff.com/en-us/products/motion/xplanar-planar-motor-system/">XPlanar | Planar motor system | Beckhoff USA</a></li>
<li><a href="https://www.chuandong.com/news/news257951.html">国内外磁悬浮智能输送系统盘点-自动化行业资讯</a></li>
<li><a href="https://zh-yue.wikipedia.org/wiki/六自由度">六自由度 - 維基百科，自由嘅百科全書</a></li>

</ul>
</details>

**标签**: `#robotics`, `#industrial automation`, `#magnetic levitation`, `#smart manufacturing`, `#frontier tech`

---

<a id="item-7"></a>
## [DeepSeek-V4-Pro 模型 API 限时 2.5 折优惠至 2026 年 5 月](https://36kr.com/newsflashes/3782954220608512?f=rss) ⭐️ 8.0/10

DeepSeek 宣布其 DeepSeek-V4-Pro 模型 API 开启限时 2.5 折优惠，有效期至 2026 年 5 月 5 日。优惠后，百万输入 token 价格为 0.25 元（缓存命中）或 3 元（缓存未命中），百万输出 token 价格为 6 元。 此次大幅折扣显著降低了使用高性能万亿参数混合专家（MoE）模型的门槛，使前沿 AI 能力更易于被开发者和企业采用。这也反映出 AI 基础设施市场竞争正在加剧。 DeepSeek-V4-Pro 模型总参数达 1.6 万亿，每次推理激活 490 亿参数，支持最高百万 token 上下文长度。输出 token 价格远高于输入 token，这与行业惯例一致，因生成过程计算开销更大。

rss · 36kr · Apr 26, 01:00

**背景**: DeepSeek-V4-Pro 属于 DeepSeek 最新模型系列，采用混合专家（MoE）架构，在性能与效率之间取得平衡。MoE 模型每次仅激活部分参数，可在不显著增加计算成本的前提下部署超大规模模型。AI API 普遍采用按 token 计费模式，其中输入 token 指提供给模型的上下文，输出 token 指模型生成的回复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing">Models & Pricing | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#AI models`, `#API pricing`, `#DeepSeek`, `#frontier AI`, `#large language models`

---

<a id="item-8"></a>
## [润芯微发布国产软硬一体 AI 智能基座](https://36kr.com/p/3782901034785801?f=rss) ⭐️ 8.0/10

中国科技公司润芯微发布了“国产软硬一体 AI 智能基座”，这是一个集国产芯片、AI 操作系统（AIOS）和端侧 AI 模型于一体的全栈平台。该解决方案面向汽车、移动设备、机器人和智能硬件等领域，C200 和 X100 等产品已实现车载量产。 此举解决了中国在多行业推进自主、安全、可扩展 AI 部署的关键瓶颈，尤其是在汽车领域，国外厂商长期主导导致国产芯片难以规模化上车。润芯微通过提供高国产化率的垂直整合方案，显著缩短研发周期，降低对非国产技术栈的依赖。 C200 平台算力达 60K~90K DMIPS，国产化率 90%，支持 3D 沉浸式交互；X100 平台算力达 100K+80TOPS，支持高速 NOA 等高阶智驾功能。其基于 openvela 构建的 AIOS Lite 系统，搭载于全球首款通过 openvela 官方兼容性认证的 Gemini-S1 开发板。

rss · 36kr · Apr 26, 00:08

**背景**: 端侧 AI 指将 AI 模型直接部署在终端设备上，而非云端，可实现低延迟、隐私保护和离线运行。在汽车领域，域控架构将座舱、智驾等功能整合到集中式计算单元中。openvela 是由小米发起的开源物联网操作系统，旨在统一智能硬件生态的软件底座。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.admin5.com/article/20260415/1061046.shtml">openvela ...</a></li>
<li><a href="https://developer.aliyun.com/article/1667145">端侧AI模型实现原理优势与落地应用-开发者社区-阿里云</a></li>
<li><a href="https://blog.csdn.net/Soly_kun/article/details/146757754">电子电气 架 构 --- 智能座舱 域 控 设计_汽 车 座舱 域 的系统设计-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#edge AI`, `#autonomous vehicles`, `#operating systems`, `#frontier tech`

---

<a id="item-9"></a>
## [卡尔动力发布 KargoBot Inside 进军 L4 自动驾驶货运](https://36kr.com/newsflashes/3782201831742724?f=rss) ⭐️ 8.0/10

2026 年 4 月 24 日，卡尔动力在 2026 北京国际车展上正式发布 KargoBot Inside，这是全球首个面向干线 L4 级自动驾驶货运的“AI+Robot+Service”全栈战略，旨在通过人工智能、机器人与服务融合重塑未来十年货运物流。 此举标志着可规模化无人驾驶货运的重要进展，有助于缓解行业长期面临的司机短缺和安全问题，并加速 L4 级自动驾驶在物流领域的商业化落地。卡尔动力借此成为构建全球供应链物理 AI 基础设施的关键参与者。 KargoBot Inside 将数据驱动的强化学习、自动驾驶卡车硬件（“Robot”）与网络化服务体系深度融合，形成统一全栈方案。该战略瞄准规模化部署，推动行业进入公司所称的“万台时代”。

rss · 36kr · Apr 25, 12:14

**背景**: L4（四级）自动驾驶车辆可在特定条件或限定区域内无需人工干预运行，适用于干线货运等封闭场景。像源自滴滴的 KargoBot 等自动驾驶货运企业，正通过编队行驶和枢纽间运输模式提升效率。近期里程碑包括美国完成首次横跨全国的无人货运测试，以及在中国大宗货物运输中的试点运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://autonews.gasgoo.com/icv/70035153.html">KargoBot, Elenergy to co-facilitate L 4 autonomous freight ... - Gasgoo</a></li>
<li><a href="http://www.cnautonews.com/lingbujian/2026/04/25/detail_20260425389119.html">KargoBot Inside战略发布，卡尔动力驱动L4自动驾驶货运进入万台时代</a></li>
<li><a href="https://robohorizon.com/en-us/videos/kargobots-driverless-truck-hauls-freight-in-china/">KargoBot's Driverless Truck Hauls Freight in China</a></li>

</ul>
</details>

**标签**: `#AI`, `#Robotics`, `#Autonomous Vehicles`, `#Logistics`, `#Frontier Tech`

---

<a id="item-10"></a>
## [海康机器人 2025 年营收超 64 亿，加码 AI 融合与具身智能](https://36kr.com/p/3782137908403457?f=rss) ⭐️ 8.0/10

海康机器人公布 2025 年全年营收达 64.52 亿元，机器视觉产品累计出货超 1000 万台，移动机器人下线突破 18 万台。公司在 2026 智造大会上发布 35 款以上新品，并明确提出以“眼、脚、手”协同为核心的具身智能与 AI 融合战略。 这标志着工业自动化正从刚性产线向环境自适应的智能系统演进。作为中国工业机器人领域的头部企业，海康机器人的具身智能布局有望推动 AI 在制造业的规模化落地，并影响全球智能制造发展方向。 公司当前主要采用多个小模型组合实现工程落地，同时也在投入研发端到端的视觉-语言-动作（VLA）大模型。其 AI 质检系统仅需一两百张样本即可部署，对 0.8 毫米以上缺陷检出率超 99.995%，显著提升交付效率。

rss · 36kr · Apr 25, 11:15

**背景**: 具身智能指通过与物理环境交互来学习和执行任务的人工智能系统，强调感知、决策与动作的闭环，区别于处理静态数据的传统“离身”AI。在工业场景中，这意味着机器人能根据实时感知动态调整行为，而非依赖固定程序。机器视觉、自主移动机器人（AMR）和协作机械臂构成了具身智能的硬件基础。这一理念契合柔性制造与人机协同的产业升级趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://scis.scichina.com/cn/2025/SSI-2025-0177.pdf">SCIENTIA SINICA</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202510031755113354_1.pdf">Survey on Embodied AI, Liu Yang, et.al》中国银河证券研究院</a></li>
<li><a href="https://www-file.huawei.com/admin/asset/v1/pro/view/dda7ee674ced41d4bb989b365ea0a028.pdf">工业与AI融合应用指南 - www-file.huawei.com</a></li>

</ul>
</details>

**标签**: `#AI Robotics`, `#Embodied Intelligence`, `#Industrial Automation`, `#Machine Vision`, `#Frontier Technology`

---

<a id="item-11"></a>
## [用户寻求可在 32GB MacBook Air M5 上运行的 MoE 大模型](https://www.v2ex.com/t/1208567#reply3) ⭐️ 8.0/10

一位 V2EX 用户表示已在 32GB MacBook Air M5 上测试了数十个最高达 350 亿参数的 4 比特量化 Mixture-of-Experts（MoE）大语言模型，但效果不佳，现向社区求助推荐兼容 Ollama 框架且附带 Hugging Face 链接的模型。 在消费级笔记本上高效本地部署前沿 MoE 模型有助于推动强大 AI 能力的普及，体现了模型压缩与边缘推理的持续进步。这使得用户无需依赖云端即可实现隐私保护和离线可用的 AI 应用。 该用户明确使用 4 比特量化和 Ollama 框架（可能误写为“omlx”），此前曾达到约每秒 35 个 token 的推理速度。他们愿意尝试 270 亿至 350 亿参数的模型，但反映模型质量明显下降（“感觉降智了”）。

rss · V2EX · Apr 26, 00:16

**背景**: Mixture-of-Experts（MoE）是一种架构，每次推理仅激活部分专用的“专家”子网络，从而在保持高模型容量的同时降低计算开销。4 比特量化通过将权重压缩至 4 位表示，大幅减少模型体积和内存占用，使百亿参数模型能在 MacBook 等内存有限的设备上运行。Ollama 是一个流行的开源框架，可简化在 macOS 和 Linux 上本地运行量化大语言模型的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://ollama.com/">Ollama is the easiest way to automate your work using open models...</a></li>
<li><a href="https://alain-airom.medium.com/run-big-llms-on-small-gpus-a-hands-on-guide-to-4-bit-quantization-and-qlora-40e9e2c95054">Run Big LLMs on Small GPUs: A Hands-On Guide to 4-bit ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#local AI`, `#model quantization`, `#Ollama`

---

<a id="item-12"></a>
## [三大主流大模型在复杂成本优化问题中集体失利](https://www.v2ex.com/t/1208565#reply6) ⭐️ 8.0/10

一位用户设计了一个涉及多种会员天数和记忆币购买选项的复杂现实成本优化问题，并测试了 GPT、Gemini 和 Claude。GPT 在一次提示后找到了正确的最低成本解，而 Gemini 和 Claude 即使经过多次提示也未能找出最优或接近最优的方案。 该测试揭示了主流大语言模型在处理多步数值推理和约束优化方面的显著差距——这些能力对现实世界的决策支持至关重要。它挑战了人们普遍认为前沿模型天然擅长逻辑与成本效益分析任务的假设。 最优解花费 272.20 元，获得 1023 天会员并剩余 167 个记忆币；一个“更划算”的替代方案花费 305.76 元，获得 1116 天会员并剩余 5367 个记忆币。GPT 正确解决了最低成本问题，但在“更划算”方案上因过度追求最少天数而犯错。Gemini 给出了“更划算”方案却未找到真正最低成本解，而 Claude 则混淆两者，提出了多个 400 元以上的昂贵无效方案。

rss · V2EX · Apr 25, 19:44

**背景**: 此类成本优化问题类似于计算机科学中的经典“零钱兑换”问题，通常通过动态规划或穷举搜索求解。随着大语言模型被越来越多地应用于金融、物流和个人规划工具，人们期望它们能处理这类结构化推理任务。然而，其表现取决于对约束条件的准确内部表征、数值精度以及多步规划能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/h1429541165/article/details/121565356">数据结构与算法-26.零钱兑换 - CSDN博客</a></li>
<li><a href="https://www.cnblogs.com/Candycan/p/14811157.html">LeetCode - 322. 零钱兑换（递归、记忆化搜索、动态规划、广度优先） ...</a></li>
<li><a href="https://blog.csdn.net/aolan123/article/details/142978182">当你提出一个 问 题 ，AI 大 模 型 是如何给出答案的？_ai...</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#large language models`, `#optimization`, `#GPT`, `#Gemini`

---

<a id="item-13"></a>
## [免费网站集成 GPT-image-2 与 Grok 生成图片和视频](https://www.v2ex.com/t/1208564#reply0) ⭐️ 8.0/10

一位开发者上线了一个免费公开的网页工具（grok.17nas.com），将 GPT-image-2、Grok 图片生成和 Grok 视频生成模型整合到一个界面中，用于提示词测试和创意工作流。 该工具降低了体验前沿多模态 AI 模型的门槛，让创作者和开发者无需管理 API 或预付费用，即可比较不同模型输出、迭代提示词并快速制作视觉内容原型。 网站提供每日免费额度用于图片和视频生成，支持参考图生图/视频，登录后可云端同步会话记录，也适配移动端；但由于上游模型限制和额度约束，不建议重度商用或批量生成。

rss · V2EX · Apr 25, 19:40

**背景**: GPT-image-2 是 OpenAI 推出的先进文生图模型，作为 DALL·E 系列的继任者，已集成到 ChatGPT 及第三方平台中。Grok 的图片与视频生成功能由 xAI 的 Aurora 引擎驱动，可生成逼真图像并内置安全过滤机制。两者均为 2025 至 2026 年间发布的前沿生成式 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT_Image">GPT Image</a></li>
<li><a href="https://x.ai/news/grok-image-generation-release">Grok Image Generation Release | xAI</a></li>
<li><a href="https://grokvideo.ai/">Grok Video - Turn Imagination Into Videos with Grok Imagine</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#image generation`, `#video generation`, `#Grok`, `#AI tools`

---

<a id="item-14"></a>
## [Momenta CEO 预判智驾市场将加速整合](https://www.ithome.com/0/943/572.htm) ⭐️ 8.0/10

Momenta CEO 曹旭东在 2026 北京车展上表示，智能驾驶领域最终仅会有 2-3 家中国供应商和 3-4 家全球供应商胜出。公司同时发布了基于强化学习、按 L4 标准打造的 R7“物理 AI”世界模型，并首次搭载于上汽大众 ID. ERA 9X 车型。 这一预判表明智驾供应链将经历剧烈整合，凸显了早期与主机厂建立合作及可扩展 AI 软件的战略优势。Momenta 的 R7 模型代表了向具备物理世界理解能力的具身 AI 系统转变，有望加速实现 L4 级自动驾驶。 Momenta 称已获得超 200 款车型定点合作，交付量产车型 70 余款，搭载其智能辅助驾驶方案的车辆已超 80 万台，并出口至英国、挪威等 10 国。R7 模型被描述为基于强化学习训练、面向 L4 标准的“物理 AI 车手”。

rss · IT HOME · Apr 26, 00:47

**背景**: 智能驾驶系统依赖感知、决策与控制模块，强化学习正越来越多地用于复杂环境中的行为规划。“物理 AI”通过具身智能体（如自动驾驶汽车）将推理能力与物理世界规律结合，超越传统纯软件 AI。与纯软件 AI 不同，物理 AI 需将感知、执行与仿真训练策略紧密耦合，才能在动态物理环境中安全运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.remio.ai/post/physical-ai-in-japan-how-robots-are-filling-the-jobs-nobody-wants">Physical AI in Japan: How Robots Are Filling the Jobs Nobody Wants</a></li>
<li><a href="https://arxiv.org/pdf/2002.00444">Deep Reinforcement Learning for Autonomous Driving: A Survey Deep Reinforcement and IL for Autonomous Driving: A Review in ... Autonomous Driving Using Deep Reinforcement Learning A review on reinforcement learning-based highway autonomous ... (PDF) Reinforcement learning in autonomous driving - ResearchGate A Comprehensive Review of Reinforcement Learning for ...</a></li>
<li><a href="https://www.mdpi.com/2076-3417/15/16/8972">Deep Reinforcement and IL for Autonomous Driving: A Review in ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Autonomous Driving`, `#Intelligent Vehicles`, `#Reinforcement Learning`, `#Frontier Tech`

---

<a id="item-15"></a>
## [东风风行星海 V6 搭载华为乾崑智驾亮相](https://www.ithome.com/0/943/566.htm) ⭐️ 8.0/10

东风风行星海 V6 六座 SUV 于 2026 北京车展正式亮相，搭载华为乾崑智驾系统，预计将于 2026 年第三季度上市。 此次发布标志着先进 AI 驱动的自动驾驶技术进一步融入主流消费级车型，使华为前沿的乾崑智驾系统不再局限于高端品牌。这体现了中国车企与科技巨头在智能出行领域日益紧密的合作趋势。 星海 V6 采用“2+2+2”六座布局，轴距达 2900mm，并搭载华为乾崑智驾系统，支持拥堵跟车、高速自动变道及窄位智能泊车等功能。该系统基于华为自研的 WEWA 架构（世界引擎+世界行为模型），具备对物理世界的理解与预判能力。

rss · IT HOME · Apr 25, 23:54

**背景**: 华为乾崑智驾系统改变了传统智驾系统单纯模仿人类驾驶行为的模式，转而通过构建“世界模型”来理解物理规律并预判场景，从而提升在复杂环境中的适应性与安全性。其智能泊车功能通常依赖超声波传感器和环视摄像头识别车位，并自动完成转向、加速与制动操作，大幅降低用户停车难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://post.smzdm.com/p/a3r707mk/">华 为 乾 崑 智 驾 新版实测：从尝鲜到常用，AI...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/711219379">自动泊车技术大爆发，一文带你速览自动泊车技术 - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/自动泊车系统/6145702">自动泊车系统 - 百度百科 自动泊车功能原理和发展趋势__财经头条__新浪财经 自动泊车技术-入门理解_智能泊车算法是怎么设计的-CSDN博客 自动泊车（APA）系统介绍-电子工程专辑 自动泊车（APA）系统介绍 - 知乎 自动 泊车 技术大爆发，一文带你速览自动 泊车 技术 - 知乎 自动 泊车 技术大爆发，一文带你速览自动 泊车 技术 - 知乎 一文尽览 | APA 自动泊车：系统定义与原理尽览！-CSDN博客 自动 泊车 技术大爆发，一文带你速览自动 泊车 技术 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#autonomous driving`, `#Huawei`, `#smart vehicles`, `#frontier tech`

---

<a id="item-16"></a>
## [AI 需求致苹果 M4 Mac mini 基础款缺货](https://www.ithome.com/0/943/561.htm) ⭐️ 8.0/10

苹果官网售价 599 美元的基础款 M4 Mac mini（16GB 内存+256GB 固态硬盘）已全球售罄，所有内存配置均无法立即发货。eBay 等二手平台上同款机型售价高达 700 至 979 美元，出现严重溢价。 这一热潮凸显了消费者硬件正成为前沿端侧 AI 推理的重要载体，推动边缘 AI 普及。它表明市场对小巧、低功耗且能运行 OpenClaw、Perplexity Computer 等本地 AI 代理设备的需求正在快速增长。 缺货仅限基础款 Mac mini，高端 Mac Studio 和 MacBook Pro 多款配置仍可在数周内发货。16GB+256GB 版本在二手市场溢价最严重，部分商品标价 925 美元并注明“最后一台”。

rss · IT HOME · Apr 25, 23:26

**背景**: OpenClaw 和 ZeroClaw 是开源或注重隐私的 AI 助手，可在本地电脑上完全离线运行，通过大语言模型在 WhatsApp、Telegram 等消息平台自动执行任务。Perplexity Computer 是 Perplexity AI 推出的专有 AI 代理，需在专用 Mac mini 上全天候运行以处理工作流。这些工具依赖大内存和高效神经网络引擎（NPU），而苹果 M 系列芯片在静音、持续运行的小型设备（如 Mac mini）中表现尤为突出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://www.zeroclawlabs.ai/">ZeroClaw — Private AI Assistant | ZeroClaw</a></li>
<li><a href="https://www.perplexity.ai/products/computer">Computer - Perplexity AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#edge computing`, `#Apple`, `#hardware`, `#local AI`

---

<a id="item-17"></a>
## [Anthropic 推出真实货币 AI 智能体交易实验](https://www.ithome.com/0/943/557.htm) ⭐️ 8.0/10

Anthropic 开展了一项名为“交易计划”（Project Deal）的真实货币市场实验，由不同模型驱动的 AI 智能体在 69 名员工之间扮演买卖双方，完成 186 笔总价值超 4000 美元的真实商品交易。研究发现，使用更先进 AI 智能体的用户获得了客观上更优的交易结果，但他们自身并未意识到这种差距。 该实验展示了 AI 智能体如何在具有现实后果的经济互动中自主运作，既凸显了智能体 AI 在商业中的潜力，也揭示了能力不对称可能被用户忽视的风险。同时，它为不同模型在谈判等复杂开放式任务中的性能差异提供了实证数据。 实验包含四个独立市场：一个使用 Anthropic 最先进模型的真实市场（交易具有约束力），以及三个仅用于研究的市场。尽管 AI 能力不同，但给予智能体的初始指令对成交概率或定价并无显著影响。

rss · IT HOME · Apr 25, 22:57

**背景**: 基于 AI 智能体的经济模拟是一个新兴领域，大型语言模型在类市场环境中充当自主参与者，以研究行为、效率和涌现动态。这类实验继承了经济学中的基于智能体建模（ABM）传统，但利用现代大语言模型实现更丰富、更具适应性的行为。Anthropic 是一家以 AI 安全为核心的研究实验室，开发了 Claude 系列模型，并一直在受控环境中探索智能体应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/anthropicresearch_project-deal-our-claude-run-marketplace-activity-7453501515673030656-ICr8">Project Deal : our Claude-run marketplace experiment | Anthropic</a></li>
<li><a href="https://digitaleconomy.stanford.edu/project/economic-simulations-with-ai/">Economic Simulations with AI - Stanford Digital Economy Lab</a></li>
<li><a href="https://aclanthology.org/2024.acl-long.829/">EconAgent: Large Language Model-Empowered Agents for ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Anthropic`, `#AI research`, `#autonomous systems`, `#economic simulation`

---

<a id="item-18"></a>
## [湖南 AI 中心落地湘江新区](https://36kr.com/newsflashes/3782957337926921?f=rss) ⭐️ 7.0/10

4 月 24 日，省级人工智能产业应用创新平台——湖南 AI 中心在湖南湘江新区世界计算·长沙智谷正式发布。该中心由五八科创集团打造并全权运营，旨在推动人工智能产业协同与落地应用。 该中心强化了湖南省的人工智能基础设施，推动 AI 技术在各行业的实际应用。此举也契合中国将 AI 创新从北京、上海等一线城市向区域扩散的国家战略。 该中心集展示体验、场景研发、供需对接和生态培育四大核心功能于一体，致力于打造“可看、可体验、可合作、可落地”的 AI 产业综合体。

rss · 36kr · Apr 26, 01:24

**背景**: 湘江新区是湖南省国家级新区，聚焦先进计算与数字经济。“世界计算·长沙智谷”是该区重点打造的项目，旨在建设成为中部地区人工智能与计算产业的重要枢纽。

**标签**: `#AI Infrastructure`, `#Artificial Intelligence`, `#Regional Tech Development`, `#AI Applications`, `#Innovation Platform`

---

<a id="item-19"></a>
## [本周产品榜单聚焦 AI 工具与知识管理平台](https://www.v2ex.com/t/1208569#reply0) ⭐️ 7.0/10

新上线的中文产品发现平台“产品派”发布了首期周榜，上榜产品包括智能体、AI 浏览器等 AI 工具，以及知识社区和效率工具。其中 2Libra（知识社区）、AionUi（AI 协同办公）和 LaunchX（macOS 启动器）位列前三。 这反映了中国开发者和产品经理群体对 AI 在日常工作流中实际应用的日益重视，表明行业关注点正从大模型本身转向可落地、嵌入式的人工智能工具。 榜单凸显两大趋势：一是智能体深度融入任务自动化，二是个人知识管理需求持续旺盛。其中 AionUi 代表 AI 增强的协同办公方向，而 2Libra 则融合专业讨论与生活分享。

rss · V2EX · Apr 26, 00:35

**背景**: 智能体（AI Agent）是能感知环境、自主决策并执行动作以达成目标的 AI 系统，通常以大语言模型为“大脑”。AI 浏览器（如 Comet、Fellou）不仅能浏览网页，还能主动总结、分析甚至操作网页内容。知识管理平台则帮助用户长期组织、检索和构建个人或团队的知识体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1918763414857159516">一文讲清智能体（AI Agent），这是一篇不得不看的干货总结！</a></li>
<li><a href="https://www.runoob.com/ai-agent/ai-agent-tutorial.html">AI Agent (智能体) 教程 - 菜鸟教程</a></li>
<li><a href="https://www.amassai.net/ai-tools/browser/fellou/">Fellou： AI 智能 浏 览 器 革新工作流，提升效率必备</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#productivity`, `#knowledge management`, `#intelligent agents`, `#AI applications`

---

<a id="item-20"></a>
## [问界 M9 三天预订量突破 25000 台](https://www.ithome.com/0/943/573.htm) ⭐️ 7.0/10

华为问界 M9 系列搭载华为 ADS 5 高阶智驾系统和 800V 高压平台，发布后 72 小时内预订量突破 25000 台。基础版起售价为 49.98 万元，顶配 M9 Ultimate 领世加长版起售价为 66.98 万元。 强劲的预订数据表明市场对华为深度融合 AI 智驾与高端电动技术的高度认可。这也凸显了中国高端智能电动车市场竞争加剧，软件定义汽车正成为关键差异化因素。 M9 配备 6 颗激光雷达、双腔双阀空气悬架、后轮转向，并基于 800V 高压平台，提供增程和纯电两种版本。顶配 M9 Ultimate 领世加长版还搭载 2.0T 增程器、三电机系统和线控转向技术。

rss · IT HOME · Apr 26, 00:52

**背景**: 华为 ADS（高阶智能驾驶系统）是一套全栈自研方案，融合激光雷达、摄像头和毫米波雷达，结合 AI 算法实现城区与高速领航辅助驾驶。800V 高压平台可显著提升充电速度和电驱效率，已被极氪 001 等高端电动车采用。双腔空气悬架通过两个独立气室实现更精细的阻尼调节，提升操控稳定性与舒适性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AITO_(marque)">AITO (marque) - Wikipedia</a></li>
<li><a href="https://pepelac.news/en/posts/id21697-huawei-s-ads-5-autonomous-driving-system-and-harmonyos-update-for-vehicles">Huawei 's ADS 5 autonomous driving system and HarmonyOS...</a></li>
<li><a href="https://chinaevtimes.com/posts/the-rise-of-dual-chamber-air-suspension-in-affordable-electric-vehicles/">The Rise of Dual - Chamber Air Suspension in... | ChinaEVTimes</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#AI in automotive`, `#electric vehicles`, `#Huawei`, `#frontier tech`

---