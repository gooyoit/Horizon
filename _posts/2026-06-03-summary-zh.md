---
layout: default
title: "Horizon Summary: 2026-06-03 (ZH)"
date: 2026-06-03
lang: zh
---

> From 115 items, 13 important content pieces were selected

---

1. [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 模型](#item-1) ⭐️ 9.0/10
2. [MiniMax M3 开源模型上线 SiliconFlow，首周五折优惠](#item-2) ⭐️ 9.0/10
3. [Anthropic 将 Project Glasswing 扩展至 150 家新组织](#item-3) ⭐️ 8.0/10
4. [FluxMem：面向 AI 智能体的动态图记忆系统](#item-4) ⭐️ 8.0/10
5. [微软重新定义 Windows 11 为 AI 智能体开发平台](#item-5) ⭐️ 8.0/10
6. [Marvell 发布 102.4 Tbps Teralynx T100 AI 交换芯片](#item-6) ⭐️ 8.0/10
7. [OpenAI Codex Sites 功能面向企业用户推出](#item-7) ⭐️ 8.0/10
8. [微软 MAI-Image-2.5 在图像编辑评测中位列第二](#item-8) ⭐️ 8.0/10
9. [ChatGPT 月活突破 10 亿，创史上最快纪录](#item-9) ⭐️ 8.0/10
10. [Cognition 将 Windsurf 并入 Devin，推出 Devin Desktop](#item-10) ⭐️ 8.0/10
11. [Perplexity Computer 将升级混合 AI 调度：本地与云端模型自动拆分任务](#item-11) ⭐️ 8.0/10
12. [腾讯秘密打造微信 AI 智能体，拟连接数百万小程序](#item-12) ⭐️ 8.0/10
13. [特朗普签署 AI 行政令，建立自愿模型审查框架](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 模型](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 9.0/10

在 Build 2026 大会上，微软发布了 MAI-Thinking-1——一个总参数量为 1 万亿、活跃参数为 350 亿的混合专家（MoE）推理模型，据称在盲测人类评估中优于 Anthropic 的 Sonnet 4.6；同时发布的还有 MAI-Code-1-Flash，这是一个总参数 1370 亿、活跃参数 50 亿的编程模型，已于 2026 年 6 月 2 日起向所有 GitHub Copilot 用户逐步推送。 这两款模型标志着微软在构建独立于 OpenAI 的自主 AI 模型产品线方面迈出了最重要的一步，因为两者均从头训练，未使用第三方前沿模型的蒸馏数据。MAI-Thinking-1 据称在性能上可与 Anthropic 的 Sonnet 4.6 匹敌，表明微软现在有能力在前沿推理模型领域直接参与竞争。 两款模型均采用混合专家（MoE）架构，推理时仅激活总参数的一小部分，从而在保持高性能的同时降低计算成本。尽管微软声称使用了"清洁且获得适当许可的数据"，但 MAI-Thinking-1 的技术论文显示其训练数据包含约 7940 亿页的专有网络爬取数据以及 Common Crawl 数据，这意味着它与其他主流大语言模型面临相同的许可问题。

rss · Simon Willison · Jun 2, 22:21

**背景**: 混合专家（MoE）是一种神经网络架构，将模型的总参数分配到多个"专家"子网络中，但每次输入时仅激活一小部分，从而大幅降低推理成本的同时保持庞大的知识容量。微软此前一直严重依赖 OpenAI 的 GPT 模型来驱动 GitHub Copilot 等产品，因此推出不使用 OpenAI 数据训练的自研模型标志着一项重大战略转变。"蒸馏"是指利用更大、更强的模型的输出来训练较小模型的技术，微软在此明确避免了蒸馏，而是从头开始训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI-Thinking-1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI - Code - 1 - Flash | Microsoft AI</a></li>
<li><a href="https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm">Microsoft Build 2026: MAI -Thinking- 1 Is First In-House Reasoning...</a></li>

</ul>
</details>

**社区讨论**: 原文作者 Simon Willison 公开更正了他最初对模型参数量的误读，并承认训练数据与其他主流大语言模型存在相同的许可问题，对未在发布前深入调查表示了遗憾。他对错误的坦诚引发了关于准确解读企业公告中模型规格的难度，以及训练数据透明度这一行业普遍问题的讨论。

**标签**: `#AI Models`, `#LLMs`, `#Microsoft`, `#Reasoning`, `#Coding AI`

---

<a id="item-2"></a>
## [MiniMax M3 开源模型上线 SiliconFlow，首周五折优惠](https://x.com/MiniMax_AI/status/2061987216914788401) ⭐️ 9.0/10

MiniMax 官方宣布其开源权重模型 M3 已在 SiliconFlow 推理平台上线，并提供为期 7 天的五折限时优惠，输入价格为每百万 token 0.30 美元，输出价格为每百万 token 1.20 美元。该模型号称是首个同时具备前沿编程与智能体能力（在 SWE-Bench Pro 上超越 GPT-5.5 和 Gemini 3.1 Pro）、通过 MiniMax Sparse Attention 支持 100 万 token 上下文窗口，以及原生多模态支持（图像、视频与计算机使用）三大前沿能力的开源模型。 M3 的发布代表了开源模型对前沿 AI 领域的重大挑战，一个开源权重模型声称在企业级编程基准上超越了 GPT-5.5 和 Gemini 3.1 Pro 等顶级闭源模型。100 万 token 上下文窗口、原生多模态能力与极具竞争力的定价相结合，可能使 M3 成为开发者构建复杂编程智能体和多步推理应用的极具吸引力的选择。 该模型采用 MiniMax Sparse Attention（MSA）来绕过标准的二次复杂度，原生扩展至 100 万 token，但这一自定义注意力机制目前尚未被 vLLM 等主流推理框架支持。SiliconFlow 的促销价格为缓存 $0.06/百万 token、输入 $0.30/百万 token、输出 $1.20/百万 token，为原价（$0.12/$0.60/$2.40）的五折。

rss · AI Hot · Jun 3, 01:43

**背景**: SWE-Bench Pro 是一个高级软件工程基准测试，包含来自 41 个活跃维护仓库的 1,865 个问题，旨在评估语言模型在需要扩展推理和多步问题求解的复杂、真实企业级编程任务上的表现。MiniMax Sparse Attention（MSA）是一种新型注意力架构，通过重构模型处理长序列的方式来实现在不增加传统全注意力机制计算开销的情况下处理 100 万 token 的上下文窗口。SiliconFlow 是一个高性能 AI 推理平台，提供超过 200 个优化模型和兼容 OpenAI 的 API，为开发者提供对开源和闭源 AI 模型的可扩展访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/MachineLearning/comments/1tvameq/minimax_dropped_a_new_attention_architecture_n/">MiniMax dropped a new attention architecture. [N] : r/MachineLearning</a></li>
<li><a href="https://scaleapi.github.io/SWE-bench_Pro-os/">SWE-Bench Pro</a></li>
<li><a href="https://discuss.vllm.ai/t/minimax-m3-support/2689">Minimax m3 support - vLLM Forums</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 的机器学习社区中，用户对 MiniMax 的新型稀疏注意力架构表现出浓厚兴趣，指出 MSA 通过完全重构注意力计算来绕过二次复杂度。与此同时，在 vLLM 论坛上，开发者指出 MSA 尚未被支持，表明这一新架构的更广泛生态系统集成仍在推进中。

**标签**: `#Frontier AI`, `#Large Language Models`, `#Open Source AI`, `#MiniMax`, `#Multimodal AI`

---

<a id="item-3"></a>
## [Anthropic 将 Project Glasswing 扩展至 150 家新组织](https://www.anthropic.com/news/expanding-project-glasswing) ⭐️ 8.0/10

Anthropic 正在扩展 Project Glasswing 项目，将其 Claude Mythos 模型部署到 15 个国家的约 150 家新组织中，用于防御性网络安全应用。此前该项目已于 2026 年 4 月向约 50 家合作伙伴进行了初步推出，此次扩展标志着该计划的大规模推进。 此次扩展是专为保护关键基础设施软件而设计的前沿 AI 模型在现实世界中最重要的部署之一。该计划的成功与否可能为全球 AI 融入国家网络安全防御策略树立标杆。 Claude Mythos 是 Anthropic 迄今为止最强大的前沿模型，在评估基准上相比 Claude Opus 4.6 有显著飞跃，但仅作为防御性网络安全工作流的研究预览版通过邀请方式提供。早期用户报告称，虽然安全扫描框架本身有用，但该模型会产生数百甚至数千个误报，使团队被大量噪音淹没。

hackernews · surprisetalk · Jun 2, 13:15 · [社区讨论](https://news.ycombinator.com/item?id=48369863)

**背景**: Project Glasswing 是 Anthropic 的一项计划，旨在将其最先进的 AI 模型应用于发现和修复支撑关键基础设施和互联网的软件中的漏洞。该项目涉及与安全行业合作伙伴、开源软件维护者以及美国政府的合作。Claude Mythos 专为防御性网络安全目的而开发，旨在在恶意行为者利用漏洞之前识别缺陷。该模型不对外公开，仅通过邀请制访问模式分发，以控制在敏感场景中的部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/expanding-project-glasswing">Expanding Project Glasswing \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/glasswing-initial-update">Project Glasswing: An initial update \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/06/02/anthropic-mythos-ai-project-glasswing.html">Anthropic expands Mythos to 150 additional organizations - CNBC</a></li>

</ul>
</details>

**社区讨论**: 社区情绪明显持怀疑态度，一位一线用户报告称该工具使团队被数百个误报和次要问题淹没，表明实际效用落后于宣传。一些评论者猜测 Anthropic 正在利用"道德化推出"的框架来掩盖计算能力不足导致无法公开提供 Mythos 的问题。还有人提出更广泛的担忧：即使软件漏洞被修复，先进的 AI 驱动社会工程攻击仍可能入侵系统，并指出许多顶级安全组织仍然无法获得该工具的访问权限。

**标签**: `#Anthropic`, `#AI Deployment`, `#Cybersecurity`, `#Critical Infrastructure`, `#AI Agents`

---

<a id="item-4"></a>
## [FluxMem：面向 AI 智能体的动态图记忆系统](https://x.com/rohanpaul_ai/status/2061991005201825984) ⭐️ 8.0/10

FluxMem 提出了一种全新的 AI 智能体记忆架构，将记忆建模为动态演化的图网络而非静态存储，其中事实、过往任务经历和可复用技能作为相互连接的节点进行存储。该系统在 LoCoMo 基准上达到了 95.06 的平均准确率，并在 GAIA 基准上使 Kimi K2 的性能提升了 12.73 分，超越了所有现有记忆系统。 记忆是构建能够在长期交互中运行的强大 AI 智能体的关键瓶颈，FluxMem 基于图的方法比传统静态检索方式提供了更灵活、更具适应性的解决方案。其出色的基准测试结果表明，重新思考记忆架构可以为前沿模型带来显著的性能提升，有望加速更自主、更可靠的 AI 智能体的开发。 在任务执行过程中，FluxMem 首先收集可能相关的记忆，然后根据任务反馈动态调整记忆节点之间的连接权重，使网络能够持续优化其结构。该系统还能自动将反复成功的任务路径转化为可复用的技能节点，实现跨任务的知识积累与迁移。

rss · AI Hot · Jun 3, 01:59

**背景**: LoCoMo（长对话记忆）基准由 UNC Chapel Hill、USC 和 Snap Research 的研究人员创建，发表于 ACL 2024，是评估对话式 AI 系统长期记忆与推理能力的行业标准基准。GAIA 基准由 Meta 和 Hugging Face 开发，通过 466 道人工标注的三级难度题目，评估通用 AI 助手在多步推理、网页浏览、工具使用和多模态理解等真实世界任务上的表现。Kimi K2 是由月之暗面（Moonshot AI）开发的前沿混合专家（MoE）语言模型，拥有 320 亿激活参数和 1 万亿总参数，专门针对智能体能力进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/snap-research/locomo">GitHub - snap-research/locomo · GitHub</a></li>
<li><a href="https://huggingface.co/gaia-benchmark">gaia-benchmark (GAIA) - Hugging Face</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-K2">GitHub - MoonshotAI/Kimi-K2: Kimi K2 is the large language ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Memory Systems`, `#Graph Networks`, `#AI Research`, `#LLM`

---

<a id="item-5"></a>
## [微软重新定义 Windows 11 为 AI 智能体开发平台](https://www.ithome.com/0/959/087.htm) ⭐️ 8.0/10

在 2026 年 Build 开发者大会（6 月 2 日至 3 日）上，微软正式宣布 Windows 11 将从带有 AI 功能的桌面操作系统转型为 AI 应用和智能体的综合开发平台。新增内容包括用于安全管控智能体行为的 Microsoft Execution Containers、本地模型 Aion 1.0 Instruct 和 Aion 1.0 Plan，以及覆盖 NPU、GPU 和 CPU 的扩展 Windows AI 接口。 这一战略转型将 Windows 定位为新兴智能体 AI 生态的基础层，直接解决当前 AI 开发工具链分散、开发者需要在多个割裂环境之间切换的痛点。通过将开发、部署、监控和企业治理统一到操作系统级别的工作流中，微软有望使 Windows 成为企业级 AI 智能体开发的默认平台。 Microsoft Execution Containers 允许开发者限制 AI 智能体可访问的文件、网络、系统资源和应用程序，并由 Windows 在运行时强制执行这些边界。智能体还可以绑定本地 ID 或 Entra 云身份以便追踪活动来源，该平台还集成了 NVIDIA RTX Spark 硬件（提供高达 1 petaFLOP 的 FP4 AI 性能和 128GB 统一内存）以及 Azure 云端扩展能力。

rss · IT HOME · Jun 3, 01:50

**背景**: AI 智能体是利用大语言模型动态生成代码、链接多个操作并以最少人工干预执行复杂任务的自主软件程序，其行为本质上是非确定性的，比传统应用程序更难控制。微软一直在通过 Windows AI 接口（由 Windows Machine Learning 驱动）逐步构建 Windows 的 AI 能力，并于近期推出了 Windows 365 for Agents 公开预览版，为智能体提供可信的云端托管运行时。智能体 AI 的更广泛行业趋势催生了对统一平台的需求，这类平台需要覆盖智能体开发的完整生命周期，从代码生成到部署、监控和企业安全治理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/">Windows platform security for AI agents</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-365-for-agents-now-in-public-preview-run-ai-agents-securely-at-scale/4513479">Windows 365 for Agents now in public preview: Run AI agents ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/ai/apis/">What are Windows AI APIs? | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Windows 11`, `#AI Agents`, `#AI Infrastructure`, `#Developer Tools`

---

<a id="item-6"></a>
## [Marvell 发布 102.4 Tbps Teralynx T100 AI 交换芯片](https://www.ithome.com/0/959/086.htm) ⭐️ 8.0/10

Marvell 发布了 Teralynx T100 网络交换芯片，采用 3nm 制程和单片式架构，带宽达 102.4 Tbps，号称是业界首款专为 AI 负载从头设计的交换芯片。该芯片支持最多 512 个端口，兼容 ESUN、UEC 等新兴互联协议，将于本季度出样。 随着 AI 训练集群扩展到数万张 GPU 规模，网络互连已成为限制性能和效率的关键瓶颈。Teralynx T100 通过降低功耗、延迟和布线复杂度直接应对这些挑战，有望显著改善大规模 AI 数据中心的总体拥有成本和可扩展性。 该芯片典型功耗低于 1000W，Marvell 宣称比竞品节能 25%，这是通过消除 AI 负载不需要的遗留冗余元素实现的。它可配置为 BGA、CPC 或 CPO 封装，为不同的系统设计和光集成方案提供了灵活性。

rss · IT HOME · Jun 3, 01:49

**背景**: 在 AI 数据中心中，存在两种主要的网络范式：Scale-up（在节点或 Pod 内连接 GPU）和 Scale-out（跨更大集群的连接）。ESUN（以太网 Scale-up 网络）是一种新兴开放标准，专注于将以太网用于 Scale-up AI 基础设施；UEC（超以太网联盟）是一个行业联盟，旨在通过新的传输和链路层特性增强以太网以适应 AI 和 HPC 工作负载。CPO（共封装光学）是一种先进封装技术，将光引擎与交换芯片直接集成，相比传统可插拔光模块可大幅降低功耗并提高带宽密度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eletimes.ai/introducing-ethernet-scale-up-networking-advancing-ethernet-for-scale-up-ai-infrastructure">Introducing Ethernet Scale-Up Networking : Advancing Ethernet for...</a></li>
<li><a href="https://ultraethernet.org/">Ultra Ethernet Consortium</a></li>
<li><a href="https://en.luxshare-tech.com/company/resources/news/22.html">Reconstructing the Future of Intelligent Computing with CPO ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#networking chips`, `#datacenter hardware`, `#Marvell`, `#HPC interconnect`

---

<a id="item-7"></a>
## [OpenAI Codex Sites 功能面向企业用户推出](https://x.com/gdb/status/2061988413105156128) ⭐️ 8.0/10

OpenAI launches 'Codex Sites', a new feature allowing Business and Enterprise users to instantly build, deploy, and share interactive web applications and websites using the Codex AI model.

rss · AI Hot · Jun 3, 01:48

**标签**: `#OpenAI`, `#Codex`, `#AI Coding`, `#Enterprise Software`, `#Product Launch`

---

<a id="item-8"></a>
## [微软 MAI-Image-2.5 在图像编辑评测中位列第二](https://x.com/berryxia/status/2061988157349130675) ⭐️ 8.0/10

微软发布了拥有 200 亿参数的扩散模型 MAI-Image-2.5，该模型在 Image Edit Arena（单图编辑）评测中以 1401 分获得第二名。它比 Nano Banana 2、Grok Imagine 和 ChatGPT-Image-Latest-High Fidelity 高出 10 分，但仍落后于排名第一的 GPT-Image-2。 这一结果表明微软已成为前沿 AI 图像生成与编辑领域的有力竞争者，正在缩小与 OpenAI 领先模型之间的差距。微软、Google（Nano Banana 2）和 OpenAI 等科技巨头之间的竞争态势，正在加剧最先进图像编辑能力的角逐。 MAI-Image-2.5 是一个拥有 200 亿参数的扩散模型，采用 flow-matching 目标函数，同时支持文生图和图生图编辑。该模型于 2026 年 6 月 2 日以私有预览版发布，在文字渲染、视觉推理和指令遵循方面相比前代均有显著提升。

rss · AI Hot · Jun 3, 01:47

**背景**: Image Edit Arena 是托管在 arena.ai 上的社区驱动评测基准，使用基于人类偏好对比的 Bradley-Terry/Elo 评分系统对 AI 图像模型进行排名。MAI-Image-2.5 是微软 MAI-Image 系列的一部分，最初于 2026 年 5 月发布时在文生图排行榜上位列第三。竞争模型包括 Google 的 Nano Banana 2（基于 Gemini 3.1 Flash）和 OpenAI 的 GPT-Image-2，后者目前在图像编辑排名中领先。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/mai-image-2-5-launches-at-no-3-on-arena-ai/">MAI-Image-2.5 launches at No. 3 on Arena | Microsoft AI</a></li>
<li><a href="https://github.com/microsoft-foundry/forgebook/blob/main/notebooks/mai-image-2-5.ipynb">forgebook/notebooks/mai-image-2-5.ipynb at main - GitHub</a></li>
<li><a href="https://windowsreport.com/microsoft-launches-mai-image-2-5-with-better-ai-image-quality-and-text-rendering/">Microsoft Launches MAI-Image-2.5 With Better AI Image Quality ...</a></li>

</ul>
</details>

**标签**: `#AI image generation`, `#Microsoft`, `#MAI-Image-2.5`, `#image editing`, `#benchmark evaluation`

---

<a id="item-9"></a>
## [ChatGPT 月活突破 10 亿，创史上最快纪录](https://www.ithome.com/0/959/083.htm) ⭐️ 8.0/10

据市场情报机构 Sensor Tower 估计，OpenAI 旗下 ChatGPT 在 2025 年 5 月全球月活跃用户突破 10 亿，成为史上达成该里程碑最快的应用，增速超过 Google Maps 和 TikTok。与此同时，竞争对手 Anthropic 的 Claude 月活达到 5600 万，同比增长约 640%，并且 Anthropic 已秘密递交了 IPO 申请。 这一里程碑标志着 AI 对话工具已被大规模主流用户接受，ChatGPT 的用户规模已可与全球最大的社交媒体平台相媲美。ChatGPT 和 Claude 的快速增长，加上 OpenAI 和 Anthropic 双双筹备上市，表明 AI 行业正进入激烈竞争与市场整合的新阶段。 Sensor Tower 的数据显示，部分用户已开始在 Claude 和 ChatGPT 之间切换使用，表明用户对单一 AI 助手的忠诚度并不牢固，多平台使用行为正在兴起。OpenAI 和 Anthropic 均在筹备上市，其中 Anthropic 已秘密递交了 IPO 申请。

rss · AI Hot · Jun 3, 01:31

**背景**: Sensor Tower 是一家领先的市场情报平台，提供全球数字经济领域的应用商店分析、下载数据和用户参与度洞察。秘密递交 IPO 申请是根据 2012 年《JOBS 法案》允许的制度，企业可向美国证券交易委员会（SEC）私下提交注册声明，避免在路演前被公开审查，从而在上市时机和策略上拥有更大灵活性。ChatGPT 由 OpenAI 于 2022 年 11 月发布，增长速度前所未有，此前仅用两个月就达到了 1 亿用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings</a></li>
<li><a href="https://sensortower.com/">Digital Intelligence & App Data Analysis by Sensor Tower</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#Anthropic`, `#AI Industry`, `#User Milestones`

---

<a id="item-10"></a>
## [Cognition 将 Windsurf 并入 Devin，推出 Devin Desktop](https://x.com/shao__meng/status/2061982033828790558) ⭐️ 8.0/10

Cognition 将 Windsurf 和 Devin 两条产品线整合为统一的 Devin 平台，并推出 Devin Desktop 作为下一代 IDE，允许用户从单一界面管理本地与云端的 AI 编码智能体舰队。此次更新还引入了三个新组件：智能体指挥中心（Agent Command Center）、开放的智能体通信协议（ACP），以及作为 Windsurf Cascade 继任者的 Devin Local。 这一整合标志着 AI 编码工具领域的重大转变，从孤立的单一智能体助手走向跨本地和云端环境的统一多智能体舰队管理。开放 ACP 协议的引入有望促进 AI 编码智能体之间更强的互操作性，可能减少供应商锁定，并重塑开发者工具之间的集成方式。 完整的 Devin 平台现在包含四个组件：Devin Desktop（带智能体管理功能的 IDE）、Devin Cloud（长期运行的自主云端智能体）、Devin CLI（终端界面）和 Devin Review（代码审查）。Devin Local 取代了 Windsurf 的 Cascade 作为本地智能体编码助手，而智能体指挥中心则提供了一个统一的仪表板，用于同时编排多个智能体。

rss · AI Hot · Jun 3, 01:23

**背景**: Devin 由 Cognition 创建，被介绍为全球首个完全自主的 AI 软件工程师，能够独立完成编码、调试和从自然语言提示中规划任务。Windsurf 被 Cognition 收购，是一款 AI 驱动的 IDE，其核心功能 Cascade 是一个以多步骤代码编辑、工具调用和实时感知著称的智能体 AI 助手。智能体通信协议（ACP）是一个开放标准，旨在解决跨不同框架和基础设施连接 AI 智能体的挑战，最初由 JetBrains 和 Zed 合作构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devin.ai/">Devin | The AI Software Engineer</a></li>
<li><a href="https://windsurf.com/cascade">Cascade | Windsurf</a></li>
<li><a href="https://www.jetbrains.com/acp/">Agent Client Protocol (ACP): Use Any Coding Agent in Any IDE</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#AI Coding`, `#Devin`, `#Windsurf`, `#Developer Tools`

---

<a id="item-11"></a>
## [Perplexity Computer 将升级混合 AI 调度：本地与云端模型自动拆分任务](https://www.ithome.com/0/959/069.htm) ⭐️ 8.0/10

Perplexity plans to upgrade its Perplexity Computer AI agent in July with a hybrid scheduling system that automatically routes sensitive tasks to local models and complex tasks to cloud-based frontier models.

rss · AI Hot · Jun 3, 01:08

**标签**: `#AI Agents`, `#Hybrid AI`, `#Perplexity`, `#Edge Computing`, `#On-Device AI`

---

<a id="item-12"></a>
## [腾讯秘密打造微信 AI 智能体，拟连接数百万小程序](https://t.me/zaihuapd/41705) ⭐️ 8.0/10

3 月 10 日晚间，外媒援引 4 位知情人士报道称，腾讯正秘密为微信打造一款新型 AI 智能体，计划连接微信内运行的数百万个小程序，覆盖预约出租车、订购杂货等服务，潜在覆盖微信 14 亿月活跃用户。截至发稿时，腾讯尚未就此事向媒体作出回应。 如果成功部署，这将成为全球最大规模的 AI 智能体实际应用之一，可能从根本上改变 14 亿用户日常使用数字服务的方式。这也标志着腾讯、阿里巴巴和字节跳动等科技巨头在中国 AI 竞赛中的重大升级。 该 AI 智能体旨在自主操控微信生态中大量的小程序——即无需单独安装即可在微信内运行的轻量级应用——代替用户执行各类任务。该项目目前仍处于保密状态，腾讯未予官方确认，表明其可能仍处于早期开发阶段。

telegram · @zaihuapd · Jun 2, 05:03

**背景**: 微信由腾讯开发，自 2011 年发布以来已成为全球最大的独立移动应用之一，被称为中国的'万能应用'和超级应用。其小程序生态允许第三方开发者在微信内构建轻量级应用，涵盖打车、外卖、购物和政务服务等多种功能。AI 智能体与传统聊天机器人不同，能够自主规划、推理并使用外部工具执行操作，因此非常适合在多个不同服务之间完成复杂的多步骤任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WeChat_Mini_Program">WeChat Mini Program</a></li>
<li><a href="https://langcopilot.com/posts/2025-09-17-llm-agents-explained-visual-guide-ai">LLM Agents Explained: Architecture, Tools, Memory & Multi ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Tencent`, `#WeChat`, `#LLM Applications`, `#Tech Industry`

---

<a id="item-13"></a>
## [特朗普签署 AI 行政令，建立自愿模型审查框架](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) ⭐️ 8.0/10

特朗普总统于 6 月 2 日签署了一项行政命令，建立了一个自愿性框架，邀请 AI 开发商在发布"受保护的尖端模型"前 30 天将其提交给政府进行网络安全审查。该命令还指示财政部、国防部和国土安全部组建 AI 网络安全清算所，以协调漏洞扫描并加强联邦系统的防御能力。 这项行政命令代表了美国 AI 治理政策的重大转变，选择了自愿的公私合作模式而非强制性监管。它直接影响美国前沿 AI 实验室的运营方式，并在国家安全需求与减少 AI 行业监管负担的承诺之间设定了平衡基调。 最终签署的命令在行业压力和白宫内部分歧下，将原计划的 90 天审查期缩短为 30 天。该命令明确禁止建立强制性的政府许可或预审机制，转而强调为自愿共享模型的公司提供保密保护。

telegram · @zaihuapd · Jun 2, 16:44

**背景**: 前沿 AI 模型是当前最先进的 AI 系统，在海量数据集上训练而成，在推理、文本生成和智能体工作流等任务上提供最先进的性能。政策制定者和网络安全专家日益关注这些模型发现漏洞的能力，特别是它们被用于网络犯罪或威胁关键基础设施的潜在风险。美国一直在探索如何监管这些强大的系统，在不同政府执政期间在更严格的监督和放手不管之间摇摆不定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/policy/941775/trump-ai-executive-order">Trump signs executive order to review AI models before... | The Verge</a></li>
<li><a href="https://federalnewsnetwork.com/cybersecurity/2026/06/ai-executive-order-sets-stage-for-new-cybersecurity-directives/">AI executive order sets stage for new cybersecurity ...</a></li>
<li><a href="https://www.cybersecuritydive.com/news/trump-ai-security-executive-order/821755/">Trump signs EO seeking early government access to powerful AI ...</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#AI Governance`, `#AI Safety`, `#Frontier Models`, `#US Regulation`

---