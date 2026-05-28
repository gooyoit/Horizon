---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 98 items, 2 important content pieces were selected

---

1. [OpenAI 将于 6 月 2 日下架 Codex 平台上的 GPT-5.2 与 GPT-5.3-Codex](#item-1) ⭐️ 9.0/10
2. [FuriosaAI 携手博通开发 2nm AI 推理加速器](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 将于 6 月 2 日下架 Codex 平台上的 GPT-5.2 与 GPT-5.3-Codex](https://x.com/thsottiaux/status/2059650685948551384) ⭐️ 9.0/10

OpenAI 宣布，自 6 月 2 日起，通过 ChatGPT 账号登录 Codex 的用户将无法再使用 GPT-5.2 和 GPT-5.3-Codex，免费版用户将默认升级为更先进的 GPT-5.5 作为前沿编程模型。这两个被下架的模型仍会继续通过 API 提供服务，不会完全停用。 此举标志着 OpenAI 快速的模型迭代节奏，在 GPT-5.5 于 2026 年 4 月发布仅数周后，就用更强大的新模型替换了旧的前沿模型。这直接影响了依赖 Codex 平台进行 AI 辅助编程的开发者和用户，免费用户将获得更强大的模型，同时 OpenAI 也简化了其计算基础设施管理。 此次下架仅影响通过 ChatGPT 账号访问的 Codex 平台界面；GPT-5.2 和 GPT-5.3-Codex 仍将通过 API 继续完整提供服务。OpenAI 表示此举是为了简化 Codex 计算集群管理，这表明基础设施效率而非模型过时是主要驱动因素。

telegram · @zaihuapd · May 28, 01:20

**背景**: OpenAI Codex 是一个专注于编程的智能体平台，提供终端风格的界面用于 AI 辅助软件开发，允许用户将编程任务委托给 AI 智能体。GPT-5.5 于 2026 年 4 月 23 日发布，代号为"Spud"，是 OpenAI 最新的前沿模型，在 Terminal-Bench 2.0 上达到 82.7%的得分，专为编程、研究和数据分析等复杂任务设计。Codex 平台此前默认使用 GPT-5.2 作为主要模型，因此此次升级对免费用户来说是一次显著的提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5`, `#Codex`, `#Frontier Models`, `#AI Coding`

---

<a id="item-2"></a>
## [FuriosaAI 携手博通开发 2nm AI 推理加速器](https://www.ithome.com/0/956/278.htm) ⭐️ 8.0/10

韩国 AI 芯片初创企业 FuriosaAI 于 5 月 27 日宣布与博通合作开发其第三代 AI 推理加速器，目标在 2028 年上半年出样。该芯片将结合 2nm 先进制程计算裸晶、独立 I/O 裸晶和 HBM4(E)内存堆栈，并在机架内采用博通的纵向扩展以太网（SUE）实现全连接拓扑。 这一合作将 FuriosaAI 新颖的 TCP 架构与博通业界领先的互连和 XPU 平台专长相结合，对英伟达在 AI 推理硬件领域的主导地位构成了重要挑战。其以机架级系统形式交付并采用先进以太网纵向扩展的方案，直接针对大规模 AI 智能体部署中日益突出的通信瓶颈问题。 FuriosaAI 的张量收缩处理器（TCP）架构以张量和张量收缩运算为基本设计单元，而非像传统 GPU 那样管理数千个细粒度线程，优先考虑内存访问和高带宽数据传输以支持大规模张量运算。该芯片将以机架级系统形式出货，利用博通的 SUE 框架在机架内多个 XPU 之间提供低延迟、高带宽的连接。

rss · IT HOME · May 28, 01:34

**背景**: HBM4 是最新一代高带宽内存，支持在 2048 位接口上高达 8 Gb/s 的传输速度，总带宽可达 2 TB/s，专门为高性能计算和 AI 工作负载进行了优化。博通的纵向扩展以太网（SUE）是一个基于以太网为 XPU 纵向扩展网络提供低延迟、高带宽连接的框架，支持 200GbE 链路以满足现代 AI 集群对互连的苛刻需求。FuriosaAI 的 TCP 架构代表了从传统 GPU 设计的范式转变，将张量作为基本数据结构、张量收缩作为基本运算，最大化 AI 工作负载中的数据复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.supermicro.com/en/glossary/hbm4">What Is HBM4? | Supermicro</a></li>
<li><a href="https://docs.broadcom.com/doc/scale-up-ethernet-framework">Scale Up Ethernet Specification</a></li>
<li><a href="https://furiosa.ai/blog/tensor-contraction-processor-ai-chip-architecture">Tensor Contraction Processor : The first future-proof AI chip</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Hardware`, `#Broadcom`, `#FuriosaAI`, `#Inference`

---