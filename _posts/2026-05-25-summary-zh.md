---
layout: default
title: "Horizon Summary: 2026-05-25 (ZH)"
date: 2026-05-25
lang: zh
---

> From 103 items, 8 important content pieces were selected

---

1. [Cerebras 在单个晶圆上实现 NVL72 机架级算力](#item-1) ⭐️ 9.0/10
2. [内存已占 AI 芯片组件成本的近三分之二](#item-2) ⭐️ 8.0/10
3. [阿里云开启 Qwen Conference 2026 全球直播](#item-3) ⭐️ 8.0/10
4. [AI 行业三大趋势：企业落地、下一代 Claude 开发与超级个体](#item-4) ⭐️ 8.0/10
5. [英伟达将在新加坡设立具身智能研发中心](#item-5) ⭐️ 8.0/10
6. [Claude 即将推出 Memory Files 功能](#item-6) ⭐️ 8.0/10
7. [华为发表半导体韬定律：预计到 2031 年，基于该定律的高端芯片晶体管密度将达到 1.4 纳米制程的同等水平](#item-7) ⭐️ 8.0/10
8. [DeepSeek-V4 团队持续征集角色扮演等能力反馈](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cerebras 在单个晶圆上实现 NVL72 机架级算力](https://x.com/SemiAnalysis_/status/2058714944313450805) ⭐️ 9.0/10

Cerebras 展示了其晶圆级引擎（WSE）能够在单个硅晶圆上提供相当于一整个 NVIDIA NVL72 GPU 机架的计算性能——后者集成了 72 颗 Blackwell GPU 和 36 颗 Grace CPU。这一成果通过绕过制造缺陷并将所有数据保留在片内实现，从而消除了传统多 GPU 集群固有的网络功耗瓶颈。 这代表了 AI 基础设施领域一次潜在的范式转变，因为前沿 AI 模型的训练和推理越来越受到 GPU 间通信开销和网络功耗的制约，而非原始算力。如果 Cerebras 的方案能够规模化，它将大幅降低大规模 AI 系统的成本、功耗和物理空间占用，为 NVIDIA 在 AI 训练硬件领域的主导地位提供一个强有力的替代方案。 Cerebras 通过设计冗余通信路径来实现接近 100%的良率，这些路径能够自动绕过晶圆上的制造缺陷，将缺陷点视为城市地图上的堵塞路口来处理。WSE 在单个芯片上集成了计算、内存和互连架构，这意味着数据无需穿越片外网络——而片外网络正是 NVL72 等传统 GPU 集群中功耗和延迟开销的主要来源。

rss · AI Hot · May 25, 01:01

**背景**: NVIDIA GB200 NVL72 是一个液冷机架级系统，将 72 颗 Blackwell GPU 和 36 颗 Grace CPU 整合到一个平台上，专为万亿参数模型的训练和推理而设计。Cerebras 的晶圆级引擎（WSE）采用了截然不同的方法：它不将硅晶圆切割成单个芯片再通过高速网络连接，而是将整个晶圆作为一个巨型处理器使用。晶圆级集成历史上因制造缺陷而被认为不切实际，但 Cerebras 通过内置大规模缺陷容差解决了这一问题——2021 年发布的 WSE-2 通过自动缺陷路由声称实现了 100%的良率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem">100x Defect Tolerance: How Cerebras Solved the Yield Problem - Cerebras</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL 72 | NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wafer-scale_integration">Wafer-scale integration - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Cerebras`, `#Wafer-Scale Computing`, `#AI Infrastructure`, `#GPU Alternatives`

---

<a id="item-2"></a>
## [内存已占 AI 芯片组件成本的近三分之二](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

Epoch AI 的分析显示，内存（主要是 HBM 和 DRAM）已飙升至占 AI 芯片组件成本的近三分之二，这是 AI 加速器成本结构的重大转变。这一增长是由整个行业对 AI 训练和推理硬件的爆炸性需求所驱动的。 这一成本转变对 AI 扩展经济学有直接影响，因为内存的可用性和定价现在已成为制约 AI 基础设施扩张的主要瓶颈。内存成本的主导地位影响着整个半导体供应链，如果供应无法跟上需求，可能会减缓 AI 的发展。 Nvidia、AMD 和 Google 的现代 AI 加速器都需要 HBM（高带宽内存），这是一种通过硅通孔连接的专用 3D 堆叠 DRAM，每堆栈提供超过 1 TB/s 的带宽。例如，Nvidia 的 Blackwell B100 配备 192GB HBM，而 AMD 的 MI350X 包含 288GB，这说明了推动这些成本的巨大内存需求。

hackernews · intelkishan · May 24, 16:31 · [社区讨论](https://news.ycombinator.com/item?id=48258684)

**背景**: HBM（高带宽内存）是一种特殊形式的 DRAM，通过将多个内存芯片垂直堆叠并利用硅通孔（TSV）连接，实现远超标准 DDR5 内存的数据传输速率。AI 训练和推理需要巨大的内存带宽，因为神经网络计算涉及在内存和处理单元之间不断移动大量模型参数和激活数据。随着 AI 模型增长到数百亿甚至数万亿参数，内存需求及相关成本急剧上升，使内存成为 AI 硬件生产的关键瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://luna3.ai/what-is-hbm-memory">What Is HBM Memory ? The Bottleneck Behind Every AI Chip</a></li>
<li><a href="https://www.techtimes.com/articles/317078/20260524/ai-memory-shortage-amds-lisa-su-identifies-high-bandwidth-memory-ai-chip-supplys-next-cap.htm">AI Memory Shortage: AMD's Lisa Su Identifies High-Bandwidth...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，一旦 DRAM 供应赶上需求，内存成本飙升理论上可以实现约 3 倍的硬件成本降低，且不需要任何技术创新，只需扩大制造规模。多位用户对消费级 RAM 价格飙升表示不满，有人指出 96GB 内存从几年前的约 250 美元涨到了 1200 美元，还有人感叹对于不从事 AI 的玩家和 PC 爱好者来说，现在是个糟糕的时期。

**标签**: `#AI hardware`, `#memory`, `#HBM`, `#semiconductors`, `#infrastructure`

---

<a id="item-3"></a>
## [阿里云开启 Qwen Conference 2026 全球直播](https://x.com/alibaba_cloud/status/2058724425340522834) ⭐️ 8.0/10

阿里云正式开启了 Qwen Conference 2026 的全球直播，活动在新加坡举办，面向全球观众同步放送。本次大会包含技术领袖主题演讲，涵盖全栈 AI、全球洞察和商业创新等核心议题。 作为前沿 Qwen 系列大语言模型的开发者，阿里巴巴此次大会释放了其在全球范围内推进 AI 开发与部署的战略方向信号。该活动为社区提供了直接了解全球领先开源 AI 生态未来进展的机会。 直播通过 X（原 Twitter）的广播功能进行，远程参与者可以实时观看主题演讲。大会议程围绕四大核心板块展开：技术领袖主题演讲、全栈 AI、全球洞察以及商业创新。

rss · AI Hot · May 25, 01:38

**背景**: Qwen 是阿里巴巴旗下的旗舰大语言模型系列，已成为全球最知名的开源 AI 模型系列之一。最新版本如 Qwen 3.7-Max 具备深度思考模式和高达 100 万 token 的上下文窗口等先进能力，在前沿模型中具有强劲竞争力。阿里巴巴已将 AI 相关业务整合至专门部门统一管理，涵盖通义大模型业务、Qwen 及其他 AI 创新项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://overchat.ai/models/qwen/qwen-3-7">Qwen 3.7 AI Model</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#Alibaba Cloud`, `#AI Conference`, `#Full-Stack AI`, `#Frontier Models`

---

<a id="item-4"></a>
## [AI 行业三大趋势：企业落地、下一代 Claude 开发与超级个体](https://x.com/hongming731/status/2058709546525470874) ⭐️ 8.0/10

The AI industry is seeing intensified enterprise deployment competition among major labs, alongside Anthropic revealing that next-gen Claude development uses automated user feedback loops and a 'dreaming' memory consolidation mechanism.

rss · AI Hot · May 25, 00:39

**标签**: `#AI Industry`, `#Anthropic`, `#Claude`, `#Enterprise AI`, `#AI Strategy`

---

<a id="item-5"></a>
## [英伟达将在新加坡设立具身智能研发中心](https://www.ithome.com/0/954/655.htm) ⭐️ 8.0/10

英伟达宣布计划在新加坡开设一个专注于具身智能领域的 AI 研究实验室，旨在推动 AI 与物理世界的交互。该实验室致力于提升 AI 模型训练效率、降低基础设施成本，并推进自动化与机器人技术的发展。 英伟达 CEO 黄仁勋将 AI 与现实世界的交互视为下一个前沿，表明具身智能（涵盖机器人、自动驾驶和物理自动化）正成为 AI 行业的战略重点。此举将新加坡定位为下一代 AI 研究的重要枢纽，有望加速能够在真实环境中运行的智能机器人的发展。 该研究中心将专门聚焦具身智能，即通过传感器和执行器在物理环境中进行感知、推理和行动的 AI 系统。其核心目标之一是降低大模型训练所需的巨额计算成本，目前训练前沿 AI 模型的费用可达数千万甚至上亿美元。

rss · AI Hot · May 25, 00:02

**背景**: 具身智能是指将人工智能集成到物理系统中（如机器人、自动驾驶汽车和智能工厂），使其能够感知并与物理世界进行交互。与传统 AI 仅在数字领域处理信息不同，具身智能要求智能体持续从环境中采集信息、做出决策并执行行动，形成感知、认知和行动的闭环。该领域融合了计算机视觉、自然语言处理和机器人学等多个学科，被广泛认为是实现更通用、更接近人类水平人工智能的关键一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>
<li><a href="https://github.com/tianxingchen/Embodied-AI-Guide">GitHub - TianxingChen/Embodied-AI-Guide: [Lumina具身智能社区] 具身智能技术指南 Embodied-AI-Guide · GitHub</a></li>
<li><a href="https://www.engineering.org.cn/sscae/CN/10.15302/J-SSCAE-2025.07.019">具身智能发展趋势与展望</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Embodied AI`, `#Robotics`, `#AI Research`, `#Infrastructure`

---

<a id="item-6"></a>
## [Claude 即将推出 Memory Files 功能](https://x.com/berryxia/status/2058698083748426233) ⭐️ 8.0/10

Anthropic is launching a 'Memory Files' feature for Claude that allows the AI to autonomously create, read, and edit organized persistent notes, significantly upgrading its long-term memory capabilities for agentic tasks.

rss · AI Hot · May 24, 23:54

**标签**: `#Anthropic`, `#Claude`, `#AI Memory`, `#AI Agents`, `#LLM Features`

---

<a id="item-7"></a>
## [华为发表半导体韬定律：预计到 2031 年，基于该定律的高端芯片晶体管密度将达到 1.4 纳米制程的同等水平](https://www.ithome.com/0/954/677.htm) ⭐️ 8.0/10

Huawei announced 'Tao's Law' (τ-law) at a semiconductor conference, proposing a new industry paradigm using 'time scaling' and logic folding techniques to achieve 1.4nm-equivalent transistor density by 2031, with a new Kirin mobile chip utilizing this technology expected this autumn.

rss · IT HOME · May 25, 01:24

**标签**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#compute infrastructure`

---

<a id="item-8"></a>
## [DeepSeek-V4 团队持续征集角色扮演等能力反馈](https://www.xiaohongshu.com/discovery/item/6a0ac4ce000000003601e8f6) ⭐️ 8.0/10

DeepSeek-V4 开发团队正在积极向用户征集关于角色扮演等特定模型能力的反馈意见，以推进下一代前沿模型的开发。这表明 DeepSeek-V4 正处于活跃的开发和调优阶段，团队希望通过社区输入来塑造模型的能力。 DeepSeek 是全球顶尖的 AI 研究实验室之一，此前凭借 DeepSeek-R1 和 V3 等高性价比、高性能模型颠覆了整个行业。V4 的积极开发表明该公司正在向前沿模型能力的又一次重大飞跃推进，这可能进一步重塑全球 AI 行业的竞争格局。 团队正在专门收集关于角色扮演能力的反馈，这暗示该领域可能是 V4 模型的重点改进方向之一。反馈通过小红书社区渠道进行收集，表明 DeepSeek 持续与其中国用户群体保持互动以优化模型。

telegram · @zaihuapd · May 24, 12:10

**背景**: DeepSeek 是一家中国 AI 公司，由梁文锋于 2023 年 7 月创立，以远低于竞争对手的成本开发开源大语言模型而闻名。其 2025 年 1 月发布的 DeepSeek-R1 模型性能可与 OpenAI 的 GPT-4 和 o1 相媲美，同时声称 V3 模型的训练成本仅为 600 万美元。该公司采用混合专家（MoE）层等技术，并在对华 AI 芯片出口限制下运营，这种高性价比路径被描述为美国 AI 行业的「斯普特尼克时刻」，曾导致英伟达单日市值蒸发 6000 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 : 1T Parameter AI Model Guide | Independent DeepSeek...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Frontier Models`, `#AI Research`, `#LLM`

---