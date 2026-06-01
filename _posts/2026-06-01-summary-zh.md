---
layout: default
title: "Horizon Summary: 2026-06-01 (ZH)"
date: 2026-06-01
lang: zh
---

> From 103 items, 4 important content pieces were selected

---

1. [MiniMax 发布 M3：融合前沿编码、百万上下文与原生多模态的开源模型](#item-1) ⭐️ 9.0/10
2. [戴尔向 CoreWeave 交付全球首套可运行的 NVIDIA Vera Rubin NVL72 系统](#item-2) ⭐️ 9.0/10
3. [宇树科技科创板 IPO 上会，拟募资 42.02 亿元](#item-3) ⭐️ 8.0/10
4. [OpenAI 与 SpaceX 融资热潮点燃亚洲 AI 供应链](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MiniMax 发布 M3：融合前沿编码、百万上下文与原生多模态的开源模型](https://x.com/MiniMax_AI/status/2061266317815296322) ⭐️ 9.0/10

MiniMax 发布了 M3 模型，宣称是首个同时具备前沿编码与智能体能力、通过 MiniMax Sparse Attention (MSA) 实现百万 token 上下文窗口、以及从零开始原生多模态训练的开源权重模型。该模型在 SWE-Bench Pro 上达到 59.0%，在 Terminal Bench 2.1 上达到 66.0%，在 BrowseComp 上以 83.5 分超越 Opus 4.7 的 79.3 分，权重和技术报告预计约 10 天后发布。 M3 将前沿编码与智能体性能、百万级上下文和原生多模态三大能力首次融合于单一开源模型中，此前这些能力分散在不同模型中。这种融合可能重塑竞争格局，让开发者和企业通过一个模型即可处理长程自主编码任务、多模态理解和海量上下文处理，无需在各能力之间做出取舍。 MSA（MiniMax Sparse Attention）架构基于 GQA（分组查询注意力），采用块级选择机制，在真实 KV 上执行注意力计算而非压缩维度，在处理 100 万 token 时预填充阶段的推理速度相比 MiniMax M2 提升了 9.7 倍。API 提供 M3 和 M3-highspeed 两个版本，结果完全一致但后者速度更快；在 PostTrainBench 自主微调评测中，M3 得分 37.1，仅次于 Opus 4.7（42.4）和 GPT-5.5（39.3）。

rss · AI Hot · Jun 1, 01:59

**背景**: 稀疏注意力机制通过添加预过滤阶段选择相关 token，解决了标准 Transformer 注意力的二次复杂度问题，从而支持更长的上下文窗口而不会带来过高的计算成本。SWE-Bench Pro 是一个高难度基准测试，在真实的多文件软件工程任务上评估模型的复杂推理和智能体行为能力；MCP Atlas 则通过 36 个真实 MCP（模型上下文协议）服务器和 220 个工具来衡量模型的工具使用能力。原生多模态意味着模型从预训练的第一步就在文本和视觉数据上同时训练，而非后期拼接视觉能力，从而实现文本与视觉语义空间的深度对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All...</a></li>
<li><a href="https://labs.scale.com/leaderboard/swe_bench_pro_public">SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale</a></li>
<li><a href="https://labs.scale.com/leaderboard/mcp_atlas">MCP Atlas - Scale Labs Leaderboard</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Source AI`, `#Agentic Coding`, `#Sparse Attention`, `#Multimodal`

---

<a id="item-2"></a>
## [戴尔向 CoreWeave 交付全球首套可运行的 NVIDIA Vera Rubin NVL72 系统](https://www.ithome.com/0/957/941.htm) ⭐️ 9.0/10

戴尔已向 CoreWeave 交付了全球首套可运行的 NVIDIA Vera Rubin NVL72 系统，标志着这一下一代机架级 AI 超级计算平台首次被部署到实际生产环境中。此次交付是将 NVIDIA 最新 AI 基础设施硬件从发布推向实际可用的重要里程碑。 Vera Rubin NVL72 专为驱动代理式 AI 和大规模推理模型而设计，其部署为训练和运行下一代前沿 AI 模型提供了关键的基础硬件支撑。此次交付表明整个 AI 行业正朝着大规模普及 NVIDIA 后 Blackwell 架构的方向迈进，有望显著加速整个生态系统的 AI 能力提升。 NVIDIA Vera Rubin NVL72 是一套完整的机架级系统，搭载最新的 Rubin R100 GPU，配备 HBM4 内存和 NVLink 6 互连技术，旨在消除通信、协调和内存方面的瓶颈，实现高效的多步骤 AI 工作流。CoreWeave 作为专注于 GPU 基础设施的 AI 原生云服务商，预计将把这一算力提供给企业客户，用于大规模 AI 训练和推理工作负载。

rss · AI Hot · Jun 1, 00:58

**背景**: NVIDIA Vera Rubin NVL72 是 Blackwell 架构的继任者，以天体物理学家薇拉·鲁宾的名字命名，代表了 NVIDIA 在数据中心 GPU 设计上的又一次重大飞跃。它被设计为一种机架级超级计算方案，通过高带宽 NVLink 互连将 72 个 GPU 在单个机架中紧密耦合，使其能够作为一个巨型 GPU 运行，以应对最苛刻的 AI 工作负载。CoreWeave 是一家总部位于新泽西州的专用 AI 云计算公司，为 AI 开发者和企业提供 GPU 基础设施，并一直在快速扩展其尖端 NVIDIA 硬件集群，以满足日益增长的 AI 算力需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-gb/data-center/dgx-vera-rubin-nvl72/">Gigascale AI Training & Inference... | NVIDIA DGX Vera Rubin NVL 72</a></li>
<li><a href="https://www.spheron.network/blog/nvidia-vera-rubin-nvl72-guide/">NVIDIA Vera Rubin NVL 72 : Rack-Scale H300 System ... | Spheron Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#NVIDIA`, `#Supercomputing`, `#CoreWeave`, `#Hardware`

---

<a id="item-3"></a>
## [宇树科技科创板 IPO 上会，拟募资 42.02 亿元](https://www.ithome.com/0/957/968.htm) ⭐️ 8.0/10

6 月 1 日，宇树科技科创板 IPO 正式上会审议，拟募资约 42.02 亿元。募集资金将用于智能机器人模型研发、机器人本体研发、新型智能机器人产品开发及智能机器人制造基地建设四大项目。 宇树科技是中国具身智能和机器人领域的领军企业之一，此次 IPO 是全球人形及四足机器人行业规模最大的融资事件之一。巨额资金的注入将大幅加速宇树在下一代智能机器人领域的研发，并扩大其制造能力，有望重塑与波士顿动力等竞争对手的竞争格局。 宇树科技 2025 年实现营业收入约 17 亿元，主营业务毛利率达 60.13%，较 2023 年的 44.22%提升近 16 个百分点。公司核心部组件自研自产率超过 90%，显示出强大的垂直整合能力。此外，5 月 12 日宇树还发布了全球首款量产版载人变形机甲 GD01，官方指导价 390 万元起。

rss · IT HOME · Jun 1, 02:02

**背景**: 科创板是上海证券交易所设立的科技创新企业板块，旨在支持中国高科技和创新驱动型企业，上市条件相对灵活。具身智能（Embodied AI）是指集成于物理实体中的人工智能系统，能够通过传感器和执行器感知、理解并与真实世界进行交互，典型代表包括人形机器人、四足机器人和无人驾驶汽车等。宇树科技由 90 后团队创立，已成为该领域的知名企业，以其四足机器人和人形机器人闻名，曾展示侧空翻等先进能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.guancha.cn/industry-science/2026_05_12_816701.shtml">宇树发布GD01载人变形机甲，定价390万元起-观察者网</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/620342675">具身智能 (Embodied AI)概述 - 知乎</a></li>

</ul>
</details>

**标签**: `#robotics`, `#embodied-AI`, `#Unitree`, `#IPO`, `#humanoid-robots`

---

<a id="item-4"></a>
## [OpenAI 与 SpaceX 融资热潮点燃亚洲 AI 供应链](https://www.bloomberg.com/news/articles/2026-05-31/spacex-openai-windfall-fuels-bets-on-next-wave-asian-ai-winners) ⭐️ 8.0/10

SpaceX、OpenAI 和 Anthropic 的大规模融资预期预计将带来约 700 亿美元的新增 AI 支出，促使投资者将目光转向提供服务器零部件、散热系统和电力设备等关键数据中心组件的亚洲硬件公司。 这一趋势标志着 AI 投资浪潮正从台积电等核心芯片制造商向更广泛的亚洲供应链生态系统扩散，为制造专用材料、散热基础设施和电力供应系统等 AI 数据中心关键组件的公司创造了新的机遇。 预计新增的 700 亿美元支出是在大型云厂商已承诺投入的超过 7500 亿美元基础之上的，投资者的兴趣正从半导体股票扩展到亚洲各地生产服务器组件、热管理解决方案和电力基础设施的公司。

telegram · @zaihuapd · May 31, 06:22

**背景**: AI 数据中心需要大量电力和先进的散热系统才能高效运行，浸没式液冷技术以及碳化硅和氮化镓等宽禁带半导体材料正变得越来越重要。AI 基础设施的电力需求已经使现有电网容量承受巨大压力，推动了对专用变压器、断路器和其他高压设备的需求。亚洲制造商长期以来一直是这些关键硬件组件的重要供应商，使其在全球 AI 基础设施持续扩张中处于显著受益的位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.siemens-energy.com/global/en/home/stories/powering-ai-data-centers.html">Efficient power delivery to AI data centers</a></li>
<li><a href="https://www.eli.org/vibrant-environment-blog/ais-cooling-problem-how-data-centers-are-transforming-water-use">AI’s Cooling Problem: How Data Centers Are Transforming Water Use | Environmental Law Institute</a></li>
<li><a href="https://navitassemi.com/datacenter/">Powering AI: Efficient, Scalable, Sustainable with GaN and SiCAI Data Center Power Supply | Navitas</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Supply Chain`, `#AI Investment`, `#Data Centers`, `#Hardware`

---