---
layout: default
title: "Horizon Summary: 2026-05-30 (ZH)"
date: 2026-05-30
lang: zh
---

> From 90 items, 6 important content pieces were selected

---

1. [vLLM v0.22.0 发布：DeepSeek V4 推理大幅强化并引入实验性 Rust 前端](#item-1) ⭐️ 8.5/10
2. [Liquid AI 发布基于 38 万亿 Token 训练的 8B-A1B MoE 模型](#item-2) ⭐️ 8.0/10
3. [你的手机变遥控器，OpenAI 扩展 Codex 远程控制支持 Win10/Win11](#item-3) ⭐️ 8.0/10
4. [Anthropic 超越 OpenAI 成为估值最高的 AI 初创公司](#item-4) ⭐️ 8.0/10
5. [华为郑俊：基于韬（τ）定律研发的 Mate 90 芯片制程已达 3 纳米水平，金融客户快速部署 AI 模型  华为技术有限公司金融系统部 CTO 郑俊在深圳举行](#item-5) ⭐️ 8.0/10
6. [中国首次将 9 款国产 AI 芯片纳入安可安全采购目录](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0 发布：DeepSeek V4 推理大幅强化并引入实验性 Rust 前端](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 8.5/10

vLLM v0.22.0 正式发布，包含来自 230 位贡献者的 459 次提交，为 DeepSeek V4 推理带来了重大强化，包括 NVFP4 融合 MoE 支持、完整及分段 CUDA 图以及 MTP 推测解码。该版本还推进了 Model Runner V2 向默认引擎的过渡，引入了带有 DP Supervisor 数据并行服务的实验性 Rust 前端，并新增了多层 KV 缓存卸载框架。 作为部署最广泛的开源 LLM 推理引擎之一，vLLM 对 DeepSeek V4 的 NVFP4 量化支持直接推动了在 NVIDIA 最新 Blackwell 硬件上高效部署前沿模型。实验性 Rust 前端预示着向内存安全、低延迟服务方向的潜在架构转变，可能重塑生产推理系统的构建方式。 批量不变推理通过 Cutlass FP8 支持实现了 28.9% 的端到端延迟提升，而新的多层 KV 缓存卸载框架将缓存扩展到 CPU 内存之外的 Python 文件系统二级层和 Mooncake 磁盘卸载。Model Runner V2 现在通过预测器自动为 Qwen3 稠密模型选择自身，并在存在 KV 连接器时自动回退到 MRv1。

github · vllm-project/vllm · May 29, 10:28

**背景**: NVFP4 是专为 NVIDIA Blackwell 架构 Tensor Core 设计的原生 4 位浮点量化格式，相比 FP8 或 BF16 可提供约 2 倍的性能提升，同时保持模型质量。CUDA 图通过将 GPU 内核启动序列作为单一单元捕获和重放来降低 LLM 推理延迟，消除了每步启动开销并实现了显著加速。MTP（多令牌预测）推测解码允许具有原生多令牌预测能力的模型在每次前向传播中生成多个令牌，在不改变输出质量的前提下提升吞吐量。MoE（混合专家）架构如 DeepSeek V4 每个令牌仅激活模型参数的子集，需要专门的融合内核来实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM Documentation</a></li>
<li><a href="https://dev.to/sfahad/cuda-graphs-in-llm-inference-deep-dive-36pb">CUDA Graphs in LLM Inference: Deep Dive - DEV Community</a></li>
<li><a href="https://zenn.dev/toki_mwc/articles/rtx5090-nvfp4-quantization-reality?locale=en">Testing NVFP 4 Quantization on RTX 5090: The Significant Quality...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM inference`, `#DeepSeek V4`, `#open-source AI`, `#high-performance computing`

---

<a id="item-2"></a>
## [Liquid AI 发布基于 38 万亿 Token 训练的 8B-A1B MoE 模型](https://www.liquid.ai/blog/lfm2-5-8b-a1b) ⭐️ 8.0/10

Liquid AI 发布了 LFM2-5-8B-A1B，这是一个全新的混合专家（MoE）语言模型，总参数量为 80 亿，活跃参数约 10 亿，在高达 38 万亿 Token 的数据上完成训练。这一训练数据规模在同参数量级的模型中属于最大之列。 此次发布将小型 MoE 架构的训练数据规模推向了新的高度，可能为在消费级硬件上运行的高效 AI 系统提供一条新路径。然而，早期社区测试表明，单纯的训练规模扩大未必能带来特定任务上的优越性能，该模型在代码 Bug 修复等领域未能匹敌更早的专用模型。 模型名称中的'8B-A1B'表示总参数量为 80 亿，但推理时仅有约 10 亿活跃参数，这意味着其计算需求远低于密集型的 80 亿参数模型。社区测试显示，在一个 Bug 修复基准测试中，该模型仅修复了约 12%的 Bug，而 Qwen2.5-Coder-3B 修复了约 50%；部分用户质疑 38 万亿 Token 的训练量对该模型规模而言是否属于过度训练。

hackernews · simjnd · May 29, 16:19 · [社区讨论](https://news.ycombinator.com/item?id=48325306)

**背景**: 混合专家（MoE）是一种 AI 模型架构，它使用多个被称为'专家'的专用子网络，每次推理时仅激活其中一部分，从而比单一密集型模型更高效。'8B-A1B'的命名方式遵循了 AI 社区日益增长的趋势，即分别标注模型的总参数量和活跃参数量，以反映 MoE 设计的稀疏特性。Liquid AI 总部位于马萨诸塞州剑桥市，是一家专注于开发高效通用 AI 系统的 AI 实验室，此次发布属于其 LFM（Liquid 基础模型）系列的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://himalayas.app/companies/liquid-ai">Liquid AI | Himalayas</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一位测试者发现该模型在 Bug 修复基准测试中显著逊于更早的 Qwen2.5-Coder-3B（约 12%对约 50%），不过也指出它并非代码专用模型。另一位用户对 80 亿参数模型使用 38 万亿 Token 训练是否属于过度训练提出了质疑，而其他用户则对该架构扩展到视觉-语言-动作（VLA）模型的潜力表示兴奋，认为其稀疏设计能支持更多实时本地推理。

**标签**: `#AI Models`, `#Liquid AI`, `#Mixture of Experts`, `#LLM`, `#Machine Learning`

---

<a id="item-3"></a>
## [你的手机变遥控器，OpenAI 扩展 Codex 远程控制支持 Win10/Win11](https://www.ithome.com/0/957/422.htm) ⭐️ 8.0/10

OpenAI has expanded its Codex remote control feature to Windows 10 and 11, allowing users to initiate tasks via mobile and enabling a new 'computer use' capability where the AI can autonomously operate desktop applications by viewing the screen and simulating clicks and typing.

rss · IT HOME · May 30, 01:05

**标签**: `#OpenAI`, `#Codex`, `#Computer Use`, `#AI Agents`, `#Windows`

---

<a id="item-4"></a>
## [Anthropic 超越 OpenAI 成为估值最高的 AI 初创公司](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) ⭐️ 8.0/10

Anthropic 完成了新一轮 650 亿美元的融资，投后估值达到 9650 亿美元，正式超越最新估值约 8520 亿美元的 OpenAI，成为全球估值最高的 AI 初创公司。 这一里程碑标志着前沿 AI 开发竞争格局的重大转变，资本正越来越集中于少数几家顶级实验室。如此规模的融资凸显了投资者的信心，表明 AI 竞赛远未结束，Anthropic 被视为 OpenAI 霸主地位的有力挑战者。 Anthropic 是 Claude 系列大语言模型的开发公司，该系列模型作为 OpenAI GPT 产品线的竞争对手已获得显著的市场关注。此次融资的主要资金用途包括算力基础设施、模型训练和商业化扩张。

telegram · @zaihuapd · May 29, 03:29

**背景**: Anthropic 由前 OpenAI 研究人员（包括 Dario 和 Daniela Amadei 兄妹）于 2021 年创立，以 AI 安全研究为核心使命。该公司近年来已从 Google、Amazon 和 Spark Capital 等主要投资方完成了多轮巨额融资。与此同时，OpenAI 也在以巨额估值持续融资，反映出前所未有的资本正涌入前沿 AI 公司，推动它们竞相构建更强大的基础模型。

**标签**: `#Anthropic`, `#AI Funding`, `#OpenAI`, `#Frontier AI Labs`, `#Valuation`

---

<a id="item-5"></a>
## [华为郑俊：基于韬（τ）定律研发的 Mate 90 芯片制程已达 3 纳米水平，金融客户快速部署 AI 模型  华为技术有限公司金融系统部 CTO 郑俊在深圳举行](https://t.me/zaihuapd/41632) ⭐️ 8.0/10

A Huawei executive announced that their latest Mate 90 chip achieves 3nm process technology, while also highlighting the rapid deployment of AI models like DeepSeek on their autonomous computing platform for the financial sector.

telegram · @zaihuapd · May 29, 05:06

**标签**: `#Huawei`, `#Semiconductors`, `#AI Infrastructure`, `#DeepSeek`, `#3nm Chip`

---

<a id="item-6"></a>
## [中国首次将 9 款国产 AI 芯片纳入安可安全采购目录](https://www.tomshardware.com/tech-industry/semiconductors/china-certifies-nine-domestic-ai-chips-for-government-procurement) ⭐️ 8.0/10

中国信息安全测评中心等机构首次在安全认证框架下新增"AI 训练与推理芯片"品类，共 9 款国产 AI 处理器通过认证，有效期三年，华为昇腾、阿里平头哥镇武、壁仞、海光等厂商在列。 该认证将作为政府机构和国有企业采购的依据，在中国面临美国出口管制的背景下，大幅加速国产 AI 硬件自主可控进程，减少对 NVIDIA 等外国供应商的依赖。 值得注意的是，寒武纪与百度昆仑芯此次未出现在认证名单中，表明并非所有主要国产 AI 芯片厂商都满足了安全认证要求。该认证有效期为三年，专门针对用于 AI 训练和推理工作负载的芯片。

telegram · @zaihuapd · May 29, 08:41

**背景**: "安可"（安全可靠）采购目录是中国政府推动的国产化技术产品认证体系，要求关键信息基础设施运营者优先采购经过认证的产品和服务，涵盖公共通信、金融、政务、能源、交通、水利和国防等领域。华为昇腾系列，尤其是 910B，已成为 NVIDIA GPU 的主要国产替代方案，DeepSeek 等重大 AI 项目已采用昇腾 NPU 基础设施进行大规模模型训练和推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.tencent.com/developer/article/1958838">国务院要求关键信息基础设施运营者应优先采购「安可产品和服务」：包括公共通信、金融、政务、能源、交通、水利、国防等-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://www.doit.com.cn/p/527695.html">华 为 昇 腾 +DeepSeek：国产AI推理引擎的破局之战</a></li>
<li><a href="https://m.nbd.com.cn/articles/2026-04-24/4358607.html">m.nbd.com.cn/articles/2026-04-24/4358607.html</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Semiconductors`, `#China`, `#Government Procurement`, `#AI Infrastructure`

---