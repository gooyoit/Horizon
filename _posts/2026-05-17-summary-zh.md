---
layout: default
title: "Horizon Summary: 2026-05-17 (ZH)"
date: 2026-05-17
lang: zh
---

> From 84 items, 4 important content pieces were selected

---

1. [SGLang v0.5.12 新增 DeepSeek-V4 首日推理支持](#item-1) ⭐️ 9.0/10
2. [NVIDIA 发布 SANA-WM，一个 26 亿参数的开源世界模型](#item-2) ⭐️ 9.0/10
3. [δ-mem：面向大语言模型的高效在线记忆机制](#item-3) ⭐️ 8.0/10
4. [SpaceX、OpenAI 和 Anthropic 筹备具有里程碑意义的 IPO](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.12 新增 DeepSeek-V4 首日推理支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 9.0/10

SGLang v0.5.12 为前沿的 DeepSeek-V4 模型提供了完整的 Day-0 推理支持，涵盖张量并行、专家并行、上下文并行和数据并行注意力等多种并行策略，以及 Prefill-Decode 分离架构和 DeepGemm、FlashMLA、MegaMoE 等优化内核。该版本还将硬件支持扩展到下一代 Nvidia B300/GB200/GB300 和 AMD MI35X 加速器，并新增了面向 Blackwell GPU 的 TokenSpeed MLA 注意力内核（支持 FP8 KV 缓存）。 此次发布对前沿 AI 部署至关重要，因为它确保了新发布的 DeepSeek-V4 模型能够在发布首日就在多种尖端硬件上高效运行，缩短了模型发布与生产就绪推理之间的典型延迟。先进的 MoE 量化内核（W4A4、W4A8）和推测解码改进直接带来更高的吞吐量和更低的延迟，这对于大规模 LLM 服务的成本效益至关重要。 值得注意的技术新增包括以极低精度损失实现更快速度的 W4A4 MegaMoE 内核、针对 Hopper GPU 优化的 Marlin/FlashInfer W4A8 MoE 内核，以及适用于所有 Nvidia GPU 的统一 Docker 标签（`lmsysorg/sglang:v0.5.12`）。该版本还将 DeepEP 迁移至官方 `deepseek-ai/DeepEP@hybrid-ep` 源以兼容 CUDA 13，并引入了通过 Mooncake store 进行 SSD 卸载的 HiCache 以实现高效的 KV 缓存管理。

github · sgl-project/sglang · May 16, 18:23

**背景**: SGLang 是一个高性能的大语言模型服务引擎，通过 RadixAttention 前缀缓存和专用 GPU 内核集成等技术提供高效推理。DeepSeek-V4 是 DeepSeek 最新发布的前沿模型，采用混合专家（MoE）架构，每个 token 仅激活模型参数的一个子集，因此需要专用内核和并行策略来实现高效服务。Prefill-Decode 分离是一种服务模式，将计算密集的 Prefill 阶段（处理输入提示）与内存带宽受限的 Decode 阶段（生成 token）分开，使每个阶段可以独立扩展和优化。FlashMLA 是由 DeepSeek 开发的高效多头潜在注意力解码内核，最初针对 Nvidia Hopper 架构优化，可加速对 MoE 模型至关重要的注意力计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill-decode disaggregation | LLM Inference Handbook</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20250422-new-kernel-deep-dive.md">FlashMLA/docs/20250422-new-kernel-deep-dive.md at main · deepseek-ai/FlashMLA</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#DeepSeek-V4`, `#LLM Inference`, `#AI Infrastructure`, `#Mixture of Experts`

---

<a id="item-2"></a>
## [NVIDIA 发布 SANA-WM，一个 26 亿参数的开源世界模型](https://nvlabs.github.io/Sana/WM/) ⭐️ 9.0/10

NVIDIA NVLabs 发布了 SANA-WM，这是一个 26 亿参数的开源世界模型，能够生成 60 秒 720p 视频，并支持 6 自由度（6-DoF）摄像机控制，且可在单张 GPU 上运行。模型权重已在 Hugging Face 上以 NVIDIA 开放模型许可证发布，代码采用 Apache 2.0 许可证。 SANA-WM 在可控视频生成和空间智能方面代表了一次重大飞跃，能够在生成的视频环境中实现精确的摄像机操控。其开源发布和单 GPU 需求使前沿世界建模能力得以普及，有望加速游戏、机器人、自动驾驶和交互媒体等领域的研究。 该模型具备 6 自由度摄像机控制功能，允许用户在视频生成过程中指定摄像机沿所有六个轴（三个平移轴和三个旋转轴）的位置和方向。该模型标注为仅供研究使用，但许可证允许商业使用和创建衍生模型。

hackernews · mjgil · May 16, 12:06 · [社区讨论](https://news.ycombinator.com/item?id=48159445)

**背景**: AI 中的世界模型是一种神经网络，它构建环境的内部表示，并预测环境如何随时间响应动作而变化，模拟物理、物体交互和因果关系等动态特性。与简单的视频生成器不同，世界模型旨在理解空间属性和物理动态，使其适用于机器人、自动驾驶和交互式模拟。6 自由度（6-DoF）指的是三维空间中的全部运动范围：三个平移运动（上/下、左/右、前/后）和三个旋转运动（俯仰、偏航、翻滚）。NVIDIA 的 SANA 系列模型一直专注于在可及的硬件上实现高效、高质量的生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Is a World Model? | NVIDIA Glossary</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://studio.aifilms.ai/blog/sana-wm-nvidia-world-model">SANA - WM : NVIDIA 's Open Source World Model for Minute-Scal...</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些用户对开源声明表示怀疑，因为模型权重最初标注为"即将发布"，有评论者称其为"空气"直到权重实际可用。另一些人注意到生成的视频具有类似电子游戏的美学风格，推测训练数据使用了虚幻引擎的合成数据。还有用户提出了关于网站自动播放演示视频导致大量带宽消耗的实际问题。

**标签**: `#world-model`, `#video-generation`, `#open-source-AI`, `#NVIDIA`, `#generative-AI`

---

<a id="item-3"></a>
## [δ-mem：面向大语言模型的高效在线记忆机制](https://arxiv.org/abs/2605.12357) ⭐️ 8.0/10

来自南洋理工大学、复旦大学等机构的研究者发表了一篇新论文，提出了δ-mem 方法，该方法利用 delta 规则学习将历史信息压缩到一个固定大小的状态矩阵中，使大语言模型能够在海量 token 历史中维持高效的在线记忆。 该方法解决了前沿 AI 中的一个关键瓶颈：使大语言模型能够处理有效无限的上下文，而无需承担简单扩展上下文窗口的巨大成本，这可能解锁新一代可无限运行的 AI 智能体。 固定大小的状态矩阵意味着内存使用量相对于 token 历史长度呈 O(1)复杂度，可以稳定地适配 GPU 显存，但论文并未显著报告计算成本或延迟指标。delta 规则学习机制通过计算实际输出与期望输出之间的差异来更新状态，迭代地优化压缩表示。

hackernews · 44za12 · May 16, 09:30 · [社区讨论](https://news.ycombinator.com/item?id=48158506)

**背景**: 当前的大语言模型在上下文长度和计算成本之间面临根本性矛盾：简单地扩展上下文窗口代价高昂，且往往无法确保有效利用所有可用上下文。delta 规则又称 Widrow-Hoff 规则，是一种经典的梯度下降学习规则，通过最小化实际输出与期望输出之间的差异来调整权重。δ-mem 重新利用了这一思想，在新 token 到达时持续更新压缩的记忆状态，使模型无需存储完整序列即可保留关键历史信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12357">$δ$-mem: Efficient Online Memory for Large Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Delta_rule">Delta rule - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/delta-rule">Delta Rule - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**社区讨论**: 社区态度谨慎乐观：多位评论者对固定大小状态能够实现基本无限的上下文、适配 GPU 并为无限运行的智能体提供动力感到兴奋。然而，怀疑者认为压缩到固定大小矩阵并不能真正解决根本的容量问题，因为微小的输入变化可能产生截然不同的激活，还有人指出论文中缺少成本和延迟基准测试。

**标签**: `#AI Research`, `#Large Language Models`, `#Memory Management`, `#Machine Learning`, `#AI Agents`

---

<a id="item-4"></a>
## [SpaceX、OpenAI 和 Anthropic 筹备具有里程碑意义的 IPO](https://t.me/zaihuapd/41409) ⭐️ 8.0/10

美国三家最具价值的私营科技公司——SpaceX、OpenAI 和 Anthropic——据报道正在筹备首次公开募股（IPO），计划最早于 2026 年上市，拟合计筹集数百亿美元资金。SpaceX 预计若无重大市场波动将在未来 12 个月内公开上市，而 Anthropic 已聘请法律顾问启动准备工作。 这三家公司的 IPO 筹资总额可能超过 2025 年美国约 200 例 IPO 的总和，将成为航天和 AI 行业的分水岭事件。巨额公开市场资金的涌入将直接资助并塑造未来数年前沿 AI 研究、开发和基础设施的发展方向。 SpaceX 的上市取决于市场条件稳定，预计在未来 12 个月内完成；Anthropic 已采取实质性步骤，聘请了法律顾问推进上市进程。OpenAI 的具体 IPO 时间表和结构在当前报道中细节较少，但其参与表明整个行业正加速向公开市场迈进。

telegram · @zaihuapd · May 16, 03:10

**背景**: SpaceX、OpenAI 和 Anthropic 是全球估值最高的私营公司之一，合计估值达数千亿美元。OpenAI 和 Anthropic 是两大领先的前沿 AI 实验室，分别负责开发最先进的大语言模型 GPT 系列和 Claude 系列。IPO（首次公开募股）是私营公司首次向公众发行股票的过程，为早期投资者提供流动性并筹集扩张资金。上市同时意味着公司将面临更严格的监管审查和季度业绩压力。

**标签**: `#IPO`, `#OpenAI`, `#Anthropic`, `#SpaceX`, `#AI Industry`

---