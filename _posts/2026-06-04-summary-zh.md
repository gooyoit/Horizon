---
layout: default
title: "Horizon Summary: 2026-06-04 (ZH)"
date: 2026-06-04
lang: zh
---

> From 111 items, 6 important content pieces were selected

---

1. [Google 发布 Gemma 4 12B：无编码器的多模态模型](#item-1) ⭐️ 9.0/10
2. [Ideogram 4.0 开源：支持边界框控制与多语言文字渲染](#item-2) ⭐️ 9.0/10
3. [李飞飞定义世界模型三大功能：渲染、模拟与规划](#item-3) ⭐️ 9.0/10
4. [苹果 iOS 27 Siri 部分查询将经 Google Cloud 调用授权版 Gemini，使用 NVIDIA Blackwell B200 集群处理](#item-4) ⭐️ 9.0/10
5. [SK 集团与台积电深化下一代 HBM 和先进封装合作](#item-5) ⭐️ 8.0/10
6. [三星在 Computex 2026 展示面向 HBM5 的 HPB 封装散热架构](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google 发布 Gemma 4 12B：无编码器的多模态模型](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) ⭐️ 9.0/10

Google 发布了 Gemma 4 12B，这是一款开放权重的多模态模型，它摒弃了传统的视觉编码器（如 SigLIP），转而采用仅由单次矩阵乘法、位置嵌入和归一化组成的轻量级嵌入模块。这种无编码器架构将音频和视觉输入直接整合到语言模型中，相比传统方法降低了延迟和内存占用。 这代表了多模态 AI 设计领域一次真正的架构创新，证明了强大的多模态性能可能并不需要庞大、独立的视觉编码器。如果该方法被证明足够稳健，它可能会大幅降低整个行业构建和部署多模态模型的计算成本和复杂度。 该轻量级嵌入模块仅有约 3500 万参数，比 SigLIP 等传统视觉编码器小得多。社区早期使用通过 llama.cpp 运行的 Q4 量化版本进行测试，结果显示表现尚可，但在代码生成任务中暴露了一些小的语法错误，例如多余的闭合括号和函数定义之间的逗号。

hackernews · rvz · Jun 3, 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48385906)

**背景**: 传统的多模态模型通常依赖独立的专用视觉编码器（如 SigLIP 或 CLIP）来处理图像并将其转换为语言模型能够理解的 token 表示。这些编码器是在视觉-语言任务上预训练的大型神经网络，在推理时会增加显著的内存开销和延迟。无编码器方法用最小的转换层替代了整个子系统，使主语言模型骨干能够在训练期间直接从原始像素数据中学习视觉表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/">Introducing Gemma 4 12B: a unified, encoder-free multimodal model</a></li>
<li><a href="https://arxiv.org/abs/2504.13181">[2504.13181] Perception Encoder: The best visual embeddings are not at the output of the network</a></li>
<li><a href="https://rocm.blogs.amd.com/software-tools-optimization/vllm-dp-vision/README.html">Accelerating Multimodal Inference in vLLM: The... — ROCm Blogs</a></li>

</ul>
</details>

**社区讨论**: 社区对无编码器架构最感兴趣，像 minimaxir 这样的用户质疑 3500 万参数的嵌入层相比专用视觉编码器是否足够稳健。一些用户对 Google 发布开放权重模型的战略动机表示好奇，而早期的实际测试显示了尚可但不完美的代码生成能力，至少有一位用户报告图像处理质量较差。

**标签**: `#ai-model-release`, `#multimodal-ai`, `#open-source-ai`, `#google-deepmind`, `#vision-encoder`

---

<a id="item-2"></a>
## [Ideogram 4.0 开源：支持边界框控制与多语言文字渲染](https://x.com/xiaohu/status/2062348355787956717) ⭐️ 9.0/10

Ideogram 发布了其首个开源 AI 图像生成模型 Ideogram 4.0，引入了通过坐标精确指定元素位置的边界框布局控制，并支持结构化 JSON 提示词格式而不再局限于纯文本。该模型在 X-Omni 基准测试中英文 OCR 准确率达到 0.97，并支持包括中日韩文字在内的跨语言密集文字渲染。 此次发布通过解决 AI 图像生成中两个公认的难题——图像内文字的精确渲染和空间布局的精准控制——实质性地推动了开源图像生成的技术前沿。需要在 AI 生成图像中获得排版正确的多语言文字（尤其是中日韩语言）的设计师、开发者和内容创作者将从中显著受益。 边界框控制允许用户为单个元素指定精确的坐标位置，从而在生成的图像中实现像素级的空间精度。结构化 JSON 提示词格式相比传统的自由文本提示提供了更具程序化和可靠性的接口，使其更容易集成到自动化工作流和生产流水线中。

rss · AI Hot · Jun 4, 01:38

**背景**: 精确的文字渲染一直是 AI 图像生成中最具挑战性的问题之一，大多数模型在尝试将文字嵌入图像时会产生乱码或无意义的字符。边界框控制是生成式 AI 中的一项新兴技术，允许用户定义特定元素应出现的精确空间区域，从而解决模型经常忽略文本提示中空间指令的常见问题。JSON 提示是一种结构化输入方法，用有组织的键值对替代自由形式的自然语言，为 AI 模型提供更清晰、更一致的指令，使其更有可能准确地遵循。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/json-prompting-hidden-superpower-ai-image-video-valentin-shapovalov-9vhyc">JSON Prompting : The Hidden Superpower for AI Image & Video...</a></li>
<li><a href="https://arxiv.org/html/2602.20672v1">BBQ-to-Image: Numeric Bounding Box and Qolor Control in Large-Scale Text-to-Image Models</a></li>
<li><a href="https://github.com/getomni-ai/benchmark/blob/main/README.md?ref=upstract.com">benchmark /README.md at main · getomni-ai/ benchmark · GitHub</a></li>

</ul>
</details>

**标签**: `#AI Image Generation`, `#Open Source AI`, `#Text Rendering`, `#Generative Models`, `#Computer Vision`

---

<a id="item-3"></a>
## [李飞飞定义世界模型三大功能：渲染、模拟与规划](https://x.com/berryxia/status/2062343921116852489) ⭐️ 9.0/10

李飞飞提出了基于 POMDP 框架的世界模型分类体系，将世界模型分为渲染器（输出像素）、模拟器（输出几何/物理状态）和规划器（输出动作）三种功能。她指出模拟器最为关键但数据极度稀缺，并展示了 World Labs 的 Marble 项目，该项目可从多模态提示生成可探索的 3D 环境，同时输出高斯溅射和碰撞网格。 这一框架为理解和推进空间智能提供了严谨的理论基础，而空间智能对于具身智能、自动驾驶和机器人等领域至关重要。通过明确指出模拟器是关键瓶颈，该框架将研究和投资引向了世界建模中最具影响力但发展最不足的领域。 Marble 项目同时输出用于逼真视觉渲染的 3D 高斯溅射和用于物理交互的碰撞网格，从而生成具有物理属性、真正可探索的 3D 世界。其长期目标是构建一个统一模型，能够在渲染、模拟和规划能力之间无缝切换。

rss · AI Hot · Jun 4, 01:21

**背景**: POMDP（部分可观测马尔可夫决策过程）是一种数学框架，用于建模智能体的决策过程，其中系统动态由马尔可夫决策过程决定，但智能体无法直接观测到底层状态，非常适合建模真实世界的 AI 交互。3D 高斯溅射是一种将 3D 场景表示为数百万个椭球形状、具有不同透明度粒子的技术，能够实现高效且逼真的新视角合成。由李飞飞联合创立的 World Labs 是一家专注于空间智能的公司，致力于开发能够理解和生成 3D 环境的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process">Partially observable Markov decision process - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://marble.worldlabs.ai/">Marble</a></li>

</ul>
</details>

**标签**: `#World Models`, `#Spatial Intelligence`, `#3D Generation`, `#Embodied AI`, `#Fei-Fei Li`

---

<a id="item-4"></a>
## [苹果 iOS 27 Siri 部分查询将经 Google Cloud 调用授权版 Gemini，使用 NVIDIA Blackwell B200 集群处理](https://www.ithome.com/0/959/615.htm) ⭐️ 9.0/10

Apple's iOS 27 Siri will route specific user queries to an authorized version of Google's Gemini model, utilizing Google's new NVIDIA Blackwell B200 GPU clusters with confidential computing to ensure privacy.

rss · AI Hot · Jun 4, 01:10

**标签**: `#Apple Siri`, `#Google Gemini`, `#NVIDIA Blackwell`, `#Cloud Infrastructure`, `#Confidential Computing`

---

<a id="item-5"></a>
## [SK 集团与台积电深化下一代 HBM 和先进封装合作](https://www.ithome.com/0/959/618.htm) ⭐️ 8.0/10

SK 集团董事长崔泰源于 6 月 3 日在 2026 台北国际电脑展上与台积电董事长兼 CEO 魏哲家会面，双方同意在下一代 HBM 开发和先进封装领域进一步拓展合作。SK 海力士还在展会上展出了 HBM4E 48GB 12Hi 样品，引脚速率达 16.0Gbps，单堆栈带宽达 4.0TB/s，实现了 38%的带宽提升和 33%的单 Die 容量提升。 SK 海力士作为全球主导的 HBM 生产商与台积电作为世界领先的先进芯片代工厂之间的深化合作，将直接影响前沿 AI 计算的发展速度。双方在 HBM 和先进封装领域的协作对于为英伟达等公司的下一代 AI 加速器提供所需的高带宽内存解决方案至关重要。 HBM4E 48GB 12Hi 样品基于 12 层堆叠的 32Gb 1cnm DRAM Die，在 16.0Gbps 引脚速率下实现了 4.0TB/s 的单堆栈带宽。英伟达 CEO 黄仁勋也于 6 月 2 日参观了 SK 海力士的 Computex 展台，凸显了 AI 芯片设计商与 HBM 供应商之间的紧密依存关系。

rss · IT HOME · Jun 4, 01:21

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，旨在为 GPU、AI 加速器和高性能计算应用提供极高的数据吞吐量。它通过在处理器附近垂直堆叠多个 DRAM Die 来解决内存瓶颈问题，实现远超传统内存的带宽。先进封装技术（如 2.5D/3D IC 封装和基于中介层的设计）是将 HBM 与逻辑芯片集成在同一封装中的关键。SK 海力士和三星合计掌控全球 95%以上的 HBM 产能，使 HBM 成为 AI 硬件供应链中的核心组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/高頻寬記憶體">高频宽记忆体 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/先进封装">先进封装 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/30443031971">一文读懂 HBM：概念、架构与应用 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#HBM`, `#TSMC`, `#SK Hynix`, `#Advanced Packaging`

---

<a id="item-6"></a>
## [三星在 Computex 2026 展示面向 HBM5 的 HPB 封装散热架构](https://www.ithome.com/0/959/639.htm) ⭐️ 8.0/10

三星在 2026 台北国际电脑展上展示了面向 HBM5 内存的 HPB（热阻断路径）封装散热结构，该技术在封装内部加入独立热柱，从堆叠内部带走热量并导向外部散热器。三星还确认 HBM5 基底芯片将从 HBM4/HBM4E 使用的 4nm 节点转向自家 2nm 工艺。 随着 AI 数据中心不断追求更高的带宽和密度，热管理已变得与内存性能同等关键，先进的散热方案正成为 HBM 市场决定性的竞争要素。三星的 HPB 与 SK 海力士的 iHBM 方案形成直接竞争，这场技术路线之争将影响下一代 AI 加速器的散热与封装发展方向。 三星的 HPB 重点针对 D2D PHY（裸片到裸片物理层）区域，即 HBM 基底芯片与 GPU 之间的高速连接层，随着堆叠变高、速度变快，该区域的温度和功耗密度急剧上升。HPB 已在 HBM4E 上完成部署和验证，后者的首批 12 层样品已于上月出货，速率为 14Gbps（后续可扩展至 16Gbps），每堆叠带宽达 3.6TB/s。

rss · IT HOME · Jun 4, 02:27

**背景**: 高带宽内存（HBM）是一种堆叠式 DRAM，相比传统内存提供更高的带宽和更低的功耗，是 AI 训练和推理加速器的关键组件。每一代 HBM 的堆叠层数、数据速率和容量都在增加，这导致热密度急剧上升，封装内散热因此成为关键瓶颈。三星和 SK 海力士是 HBM 市场的两大主导厂商，它们采用了截然不同的散热策略：三星通过 HPB 建立专用的热量外排通道，而 SK 海力士则通过 iHBM 架构在热点处嵌入集成冷却元件（ICE），声称可降低超过 30% 的热阻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling">Samsung shows first HBM5 mockup with Heat Path Block cooling</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-unveils-ihbm-thermal-architecture-that-cools-ai-memory-at-the-source-integrated-cooling-elements-inside-hbm-interface-cut-thermal-resistance-by-30-percent-target-next-gen-hbm5-accelerators-and-dense-ai-data-centers">SK hynix unveils ' iHBM ' thermal architecture that... | Tom's Hard...</a></li>
<li><a href="https://wccftech.com/next-gen-hbm-architecture-detailed-hbm4-hbm5-hbm6-hbm7-hbm8-up-to-64-tbps-bandwidth-240-gb-capacity-per-24-hi-stack-embedded-cooling/">Next-Gen HBM Architecture Detailed Including HBM4, HBM5, HBM6, HBM7 & HBM8: Up To 64 TB/s Bandwidth, 240 GB Capacity Per 24-Hi Stack, Embedded Cooling</a></li>

</ul>
</details>

**标签**: `#HBM5`, `#Samsung`, `#AI Hardware`, `#Thermal Management`, `#Semiconductors`

---