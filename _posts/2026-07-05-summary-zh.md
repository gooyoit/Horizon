---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> From 93 items, 6 important content pieces were selected

---

1. [Karpathy 推出 'nanochat'，用 100 美元打造最强 ChatGPT](#item-1) ⭐️ 9.0/10
2. [Leaking YouTube creators' private videos](#item-2) ⭐️ 8.0/10
3. [Anthropic 最新模型在工具调用模式遵循上出现退步](#item-3) ⭐️ 8.0/10
4. [美光投资 93 亿美元扩建广岛工厂，生产先进 HBM 芯片](#item-4) ⭐️ 8.0/10
5. [华为发表“韬定律”：以时间缩微替代几何缩微，探索半导体新路径  近日在上海举行的 2026 国际电路与系统研讨会上，华为发表“韬定律”，提出以“时间缩微”替代“](#item-5) ⭐️ 8.0/10
6. [韩国拟投 800 万亿韩元建设半导体集群，DRAM 产能预计五年内翻倍](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy 推出 'nanochat'，用 100 美元打造最强 ChatGPT](https://github.com/karpathy/nanochat) ⭐️ 9.0/10

Andrej Karpathy 创建了一个名为 'nanochat' 的新开源代码仓库，其宏伟目标是在仅需 100 美元计算成本的条件下，构建出尽可能好的类 ChatGPT 模型。该项目旨在提供一种从零开始、极具技术深度的方案，在极度紧张的预算下训练出具备实用功能的聊天机器人。 作为人工智能教育和开源领域最具影响力的人物之一，Karpathy 的项目持续为全球开发者普及复杂的深度学习技术。这一举措可能会大幅降低理解和实验大语言模型（LLM）训练的门槛，证明在大型企业级计算集群之外，依然可以进行有意义的模型开发。 该项目的核心限制是严格的 100 美元计算预算，这迫使开发者在模型架构、数据集筛选和训练效率上采取创新的方法。虽然该代码仓库刚刚创建，具体代码仍在开发中，但它遵循了 Karpathy 一贯的著名理念：将代码的可读性和教育价值置于不必要的复杂性之上。

github · karpathy/nanochat · Jul 4, 03:44

**背景**: Andrej Karpathy 是 OpenAI 的联合创始成员之一，也是特斯拉前人工智能总监，他因能够将复杂的神经网络概念转化为通俗易懂的教育材料而广受赞誉。他之前的“nano”系列项目（如 'micrograd' 和 'nanogpt'）通过用极其精简且易读的 Python 代码实现强大的模型，已经成为 AI 工程师必备的学习资源。一个类 ChatGPT 模型不仅需要预测下一个词，还需要指令微调和强化学习等对齐技术，才能表现出类似智能助手的行为。

**标签**: `#LLM`, `#Machine Learning`, `#Open Source`, `#Andrej Karpathy`, `#AI Education`

---

<a id="item-2"></a>
## [Leaking YouTube creators' private videos](https://javoriuski.com/post/youtube) ⭐️ 8.0/10

A security researcher discovered a prompt injection vulnerability in YouTube Studio's AI comment assistant that could allow attackers to access creators' private videos.

hackernews · javxfps · Jul 4, 16:45 · [社区讨论](https://news.ycombinator.com/item?id=48786781)

**标签**: `#prompt-injection`, `#ai-security`, `#youtube`, `#llm-vulnerability`, `#information-disclosure`

---

<a id="item-3"></a>
## [Anthropic 最新模型在工具调用模式遵循上出现退步](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Armin Ronacher 报告称，Anthropic 的新模型——特别是 Claude Opus 4.8 和 Sonnet 5——在工具调用参数中凭空发明无效字段，导致模式验证失败，而旧模型则没有出现此问题。这些模型能生成正确的编辑内容，但会在嵌套数组中编造不存在的键，导致 Pi 等第三方编程工具框架拒绝工具调用。 这种退步揭示了前沿模型开发中的一个根本矛盾：针对第一方工具优化的模型可能会降低与第三方生态系统的互操作性，从而破坏智能体工作流的可靠性。随着 AI 智能体越来越依赖精确的工具调用来完成实际任务，SOTA 模型在模式遵循上的退步直接影响生产环境的可靠性，并削弱开发者的信任。 Armin 推测，Anthropic 通过强化学习训练这些模型以擅长 Claude Code 内置的搜索替换编辑工具，但这无意中降低了模型在使用具有不同模式的自定义第三方工具时的表现。这与 OpenAI Codex 使用的 apply_patch 机制形成对比，引发了第三方框架是否需要实现多种编辑工具以匹配各模型首选格式的问题。

rss · Simon Willison · Jul 4, 22:53

**背景**: 工具调用（或函数调用）是一种允许大语言模型通过生成与预定义 JSON 模式匹配的结构化参数来与外部系统交互的机制。当模型生成的参数包含违反模式的虚构字段时，接收系统会拒绝该调用，从而中断智能体循环。不同的模型提供商采用了不同的编辑范式——Anthropic 使用搜索替换方式，而 OpenAI 使用 apply_patch 方式——模型可能在训练中被隐式引导偏向各自提供商的原生工具格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/about-claude/models/overview">Models overview - Anthropic</a></li>
<li><a href="https://tianpan.co/blog/tags/tool-use">11 posts tagged with " tool - use " - TianPan.co</a></li>
<li><a href="https://bananalabs.io/blog/openai-vs-anthropic-for-agents">OpenAI vs Anthropic for Building AI Agents : 2026... | Bananalabs</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#Tool Calling`, `#Anthropic`, `#AI Agents`, `#AI Reliability`

---

<a id="item-4"></a>
## [美光投资 93 亿美元扩建广岛工厂，生产先进 HBM 芯片](https://36kr.com/newsflashes/3882061184413701?f=rss) ⭐️ 8.0/10

美光科技于 7 月 4 日正式启动其位于日本广岛工厂的扩建工程，该项目总投资达 1.5 万亿日元（约合 93 亿美元）。该工厂将生产包括高带宽存储器（HBM）在内的先进存储芯片，预计将于 2028 年下半年开始出货。 HBM 是 AI 处理器（尤其是英伟达用于训练前沿 AI 模型的硬件）的关键瓶颈组件。这项巨额投资凸显了包括美光、三星和 SK 海力士在内的存储巨头之间正在展开一场行业竞赛，旨在扩大制造能力并满足 AI 基础设施激增的需求。 广岛新工厂专门用于生产 HBM 芯片，旨在满足 AI 加速器对数据高吞吐量的严格要求。美光的这一举措与 SK 海力士近期宣布的另一项投资并行——后者计划投资约 514.6 亿美元在韩国新建一座 NAND 闪存工厂。

rss · 36kr · Jul 5, 01:16

**背景**: 高带宽存储器（HBM）是一种通过垂直堆叠 DRAM（动态随机存取存储器）芯片来实现的高级存储技术。通过使用硅通孔（TSV）和微凸块技术，HBM 能够比传统内存架构存储更多信息，并以更快的速度传输数据。这种高速数据处理能力使 HBM 成为 AI 加速器中不可或缺的组件，因为它能有效突破在复杂 AI 训练任务中限制处理器与内存之间通信速度的“内存墙”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xueqiu.com/3263995677/291559154">一文读懂限制AI发展的 HBM 是 什 么 HBM 是 什 么 ？ HBM 全称 High...</a></li>
<li><a href="https://ai.bnext.com.tw/answer/hbm高頻寬-20-2069868">HBM 高頻寬記憶體 在 AI 時代為何如此重要？ | 數位時代</a></li>
<li><a href="https://www.xktang.com/article/439">为何都盯上了 HBM ...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#HBM`, `#Micron`, `#Semiconductors`, `#Hardware`

---

<a id="item-5"></a>
## [华为发表“韬定律”：以时间缩微替代几何缩微，探索半导体新路径  近日在上海举行的 2026 国际电路与系统研讨会上，华为发表“韬定律”，提出以“时间缩微”替代“](https://t.me/zaihuapd/42346) ⭐️ 8.0/10

Huawei announced 'Tao's Law,' a new semiconductor paradigm focusing on 'time scaling' rather than geometric scaling to bypass Moore's Law, aiming to achieve 1.4nm-equivalent transistor density by 2031.

telegram · @zaihuapd · Jul 4, 04:56

**标签**: `#semiconductors`, `#hardware`, `#huawei`, `#moore's-law`, `#frontier-compute`

---

<a id="item-6"></a>
## [韩国拟投 800 万亿韩元建设半导体集群，DRAM 产能预计五年内翻倍](https://t.me/zaihuapd/42357) ⭐️ 8.0/10

韩国产业通商部长官金正宽公布了半导体全国集群计划，将在西南圈（湖南地区）打造第二半导体生产基地，吸引企业投资 800 万亿韩元（约 3.52 万亿元人民币）建设 4 座内存晶圆厂。此外，韩国政府将在未来 15 年内投入 30 万亿韩元（约 1321.2 亿元人民币）支持该项目。 这项巨额投资直接针对制约 AI 模型训练和推理的内存带宽瓶颈，因为 DRAM 和高带宽内存（HBM）是 AI 算力基础设施的关键组件。随着全球内存市场预计在未来五年内实现四倍以上的增长，韩国希望在来自美国、中国和日本日益激烈的半导体制造竞争中保持领先地位。 该计划规划建设 4 座专用内存晶圆厂，每座都是耗资数百亿美元的资本密集型设施，现代内存晶圆厂的月产能可达 12 万片晶圆。金正宽长官强调，韩国必须在速度和创新方面领先全球，而非仅仅追赶竞争对手，将该集群定位为确保长期经济增长的战略举措。

telegram · @zaihuapd · Jul 4, 15:15

**背景**: DRAM（动态随机存取存储器）是一种存储芯片，每个存储单元由一个电容器和一个晶体管组成，比 SRAM 密度更高、成本更低，广泛应用于包括 AI 服务器在内的计算系统。晶圆厂（制造工厂）是通过复杂的光刻和物理化学工艺在硅晶圆上制造半导体器件的设施。韩国以三星和 SK 海力士为代表，目前主导着全球 DRAM 市场，但随着世界各国补贴本国芯片生产，面临着越来越大的地缘政治压力。湖南地区的选址也引发了政治争议，有人质疑该决定是否有利于特定利益群体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chosun.com/english/national-en/2026/06/28/KBGG4DX6TVF23HPVC7QCJZPNBU/">President Lee Jae Myung: Honam Semiconductor Cluster a National...</a></li>
<li><a href="https://www.techtarget.com/searchstorage/definition/DRAM">What is DRAM ( Dynamic Random Access Memory )? How Does it...</a></li>
<li><a href="https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor">How to Build a $20 Billion Semiconductor Fab</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#AI-infrastructure`, `#hardware`, `#memory-chips`, `#South-Korea`

---