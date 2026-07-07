---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> From 88 items, 3 important content pieces were selected

---

1. [A global workspace in language models](#item-1) ⭐️ 9.0/10
2. [腾讯发布 Hy3：一款 2950 亿参数的开源 MoE 模型](#item-2) ⭐️ 9.0/10
3. [Anthropic 与 TeraWulf 签署价值 190 亿美元的 20 年数据中心租赁协议](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [A global workspace in language models](https://www.anthropic.com/research/global-workspace) ⭐️ 9.0/10

Anthropic's research identifies a 'global workspace' within language models where abstract concepts from different inputs converge, shedding light on the mechanistic processes of AI reasoning and multimodal integration.

hackernews · in-silico · Jul 6, 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**标签**: `#Mechanistic Interpretability`, `#AI Research`, `#Anthropic`, `#Global Workspace Theory`, `#Multimodality`

---

<a id="item-2"></a>
## [腾讯发布 Hy3：一款 2950 亿参数的开源 MoE 模型](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 9.0/10

腾讯以 Apache 2.0 许可证正式发布了 Hy3，这是一款总参数量达 295B、激活参数为 21B 且支持 256K 上下文窗口的混合专家（MoE）模型。该模型在预览版发布后通过更高质量的数据进行了扩展训练，使其性能足以媲美参数量大 2 至 5 倍的旗舰开源模型。 此次发布显著提高了开源 AI 领域的门槛，为社区提供了一款能够处理复杂推理和智能体任务的高效模型，同时避免了同等规模稠密模型带来的巨大计算开销。这也进一步巩固了顶尖中国科技实验室向全球开发者生态系统提供最先进、利于商用的开源 AI 的趋势。 全精度模型需要高达 598GB 的存储空间，而 FP8 量化版本则将这一占用空间缩减至 300GB。该模型包含 3.8B 专用于多 Token 预测（MTP）层的参数以优化推理速度，用户目前可以在 OpenRouter 上免费测试该模型，直至 7 月 21 日。

rss · Simon Willison · Jul 6, 23:57

**背景**: 混合专家（MoE）是一种将模型拆分为多个专用子网络（即“专家”）的架构技术，每次处理仅激活一小部分子网络，从而将推理成本与模型总容量解耦。FP8 量化是一种将模型权重的精度从标准的 16 位或 32 位格式降低至 8 位浮点数的方法，在保持准确性的同时大幅减少了内存需求。多 Token 预测（MTP）层允许模型同时预测多个未来的 Token，在推理阶段可利用其进行投机解码，从而降低生成延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Mixture of Experts Calculator - MoE Model Parameters ... Mixture of Experts Explained: MoE Architecture MoE Chapter 4 Guide | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.spheron.network/blog/fp8-quantization-inference-performance-hardware-explained/">What is FP8 Quantization? AI Inference Performance, Accuracy ...</a></li>
<li><a href="https://arxiv.org/pdf/2505.07608">MiMo: Unlocking the Reasoning Potential of Language Model -- From...</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#mixture-of-experts`, `#open-source`, `#tencent`, `#moE`

---

<a id="item-3"></a>
## [Anthropic 与 TeraWulf 签署价值 190 亿美元的 20 年数据中心租赁协议](https://www.ithome.com/0/973/347.htm) ⭐️ 8.0/10

Anthropic 与数字基础设施企业 TeraWulf 签署了一项为期 20 年的租赁协议，预计全周期收入约为 190 亿美元。TeraWulf 将在肯塔基州 Hawesville 建设一个关键 IT 负载容量约 401MW 的专用 AI 数据中心园区，计划于 2027 年下半年分阶段投入使用，2028 年初达到最大装机容量。 这笔交易是 AI 实验室有史以来最大、最长期的基础设施承诺之一，表明前沿 AI 公司正在为未来数十年锁定大规模算力。401MW 的规模使该园区跻身全球最大的专用 AI 计算设施之列，凸显了领先 AI 开发商之间日益激烈的算力军备竞赛。 401MW 的关键 IT 负载特指用于 GPU 和服务器等计算硬件的电力，不包括冷却和配电等支持性基础设施。在同一公告中，TeraWulf 还披露出售了其与 Fluidstack 在得克萨斯州合资项目的全部 50.1% 股权，该合资企业成立于 2025 年，旨在建设一个 168MW 的 AI 数据中心园区。

rss · IT HOME · Jul 7, 01:15

**背景**: TeraWulf 是一家数字基础设施公司，最初专注于比特币挖矿，后来转向为 AI 和高性能计算工作负载提供能源基础设施。该公司于 2021 年由 Paul Prager 和 Nazar Khan 成立，两人均有能源行业背景。关键 IT 负载是数据中心规划中的一个核心指标，指的是输送到 IT 设备的电力，而非整个设施的总用电量。随着前沿 AI 模型对算力的需求呈指数级增长，Anthropic 等主要 AI 实验室越来越多地签署长期租约，以确保获得有保障的电力和基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TeraWulf">TeraWulf - Wikipedia</a></li>
<li><a href="https://www.terawulf.com/">TeraWulf: Leading the Digital Energy Revolution</a></li>
<li><a href="https://datacenterss.com/data-center-power-planning-calculation-guide/">Data Center Power Planning Guide 2026: Load Calculations, UPS...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Infrastructure`, `#Data Center`, `#Compute`, `#AI Industry`

---