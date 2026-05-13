---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 78 items, 7 important content pieces were selected

---

1. [Needle：基于纯注意力架构的 2600 万参数工具调用模型](#item-1) ⭐️ 8.0/10
2. [llm CLI 0.32a2 新增对 OpenAI /v1/responses 端点的支持](#item-2) ⭐️ 8.0/10
3. [Anthropic 推出 Claude Opus 4.7 快速模式研究预览](#item-3) ⭐️ 8.0/10
4. [宇树发布全球首款量产载人变形机甲 GD01](#item-4) ⭐️ 8.0/10
5. [美国商务部网站悄然删除 AI 模型安全测试协议细节](#item-5) ⭐️ 8.0/10
6. [SpaceX 与 Google 磋商轨道数据中心发射合作](#item-6) ⭐️ 8.0/10
7. [MiniCPM-V 4.6：超高效的移动端视觉语言模型](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Needle：基于纯注意力架构的 2600 万参数工具调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus 开源了 Needle，这是一个拥有 2600 万参数的函数调用模型，采用了全新的"简单注意力网络"架构，完全移除了 MLP 层，仅使用注意力和门控机制。它在消费级设备上实现了每秒 6000 token 的预填充速度和每秒 1200 token 的解码速度，在单次函数调用基准测试中超越了 FunctionGemma-270M 和 Qwen-0.6B 等更大模型。 Needle 证明了工具调用本质上是一个检索与组装任务而非深度推理，可以被蒸馏到极小的模型中，从而使智能体 AI 在廉价手机、可穿戴设备和其他边缘设备上成为可能。研究发现 FFN 参数对于涉及外部结构化知识（RAG、工具调用）的任务并非必需，这可能会重塑行业设计专用边缘 AI 模型的方式。 该模型在 16 块 TPU v6e 芯片上用 2000 亿 token 进行了 27 小时的预训练，随后仅用 45 分钟在 20 亿由 Gemini 合成的函数调用数据上完成了后训练，涵盖 15 个工具类别。整个模型采用 MIT 许可证，权重已在 Hugging Face 上发布，并提供了可在 Mac/PC 上测试和微调的本地演练环境。

hackernews · HenryNdubuaku · May 12, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=48111896)

**背景**: 传统的 Transformer 模型将自注意力层与前馈神经网络（FFN/MLP）层结合使用，其中 FFN 被认为在其权重中存储事实性知识。LLM 中的工具调用允许模型通过将用户查询与工具定义匹配并输出结构化 JSON 来调用外部函数（API、计算器、网络搜索等）。交叉注意力是自注意力的一种变体，它在两个不同的序列之间进行操作，天然适合将查询与工具模式进行匹配。Needle 背后的核心洞察是，当输入中已提供外部结构化知识时，模型不需要在 FFN 权重中记忆事实，因此可以完全移除 MLP 组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention">Understanding and Coding Self-Attention, Multi-Head Attention, Causal-Attention, and Cross-Attention in LLMs</a></li>
<li><a href="https://blog.n8n.io/tool-calling-llm/">LLM Tool Calling: How it works and how to implement it – n8n Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对微型模型的推进表示了热情，一位开发者分享了使用 200 亿参数以下的小模型编排集群来构建隐私优先桌面应用的经验，并希望将此扩展到移动端。有人对模型在超出简单单工具场景的复杂工具选择场景中的判别能力提出了实际问题，也有人提出了创意应用，比如将微调后的模型嵌入命令行程序以实现自然语言参数解析。一个小的可用性建议是发布一个在线演示演练环境，还有评论者指出 "26M" 的表示方式容易与十亿混淆，建议改用 "0.026B"。

**标签**: `#Small Language Models`, `#Edge AI`, `#Function Calling`, `#Agentic AI`, `#Open Source`

---

<a id="item-2"></a>
## [llm CLI 0.32a2 新增对 OpenAI /v1/responses 端点的支持](https://simonwillison.net/2026/May/12/llm/#atom-everything) ⭐️ 8.0/10

Simon Willison 的 llm CLI 工具发布了 0.32a2 版本，将大多数支持推理的 OpenAI 模型切换到新的 /v1/responses 端点，取代了原有的 /v1/chat/completions。这为 GPT-5 级别模型启用了跨工具调用的交错推理能力，并在执行提示时以不同颜色显示摘要推理 token。 此次更新弥合了 OpenAI 最新 API 能力与依赖 llm CLI 进行模型交互的广大开发者社区之间的关键差距。通过支持新的 responses 端点，开发者现在可以利用推理 token 可见性和复杂多工具交互等高级功能，这些对于前沿模型工作流至关重要。 用户可以使用 -R 或 --hide-reasoning 标志来控制推理 token 的显示。/v1/responses 端点使用 input 字段而非旧版 Chat Completions API 中的 messages 数组，并且被设计为一个状态机，以事件驱动的流式格式原生处理复杂的多工具交互。

rss · Simon Willison · May 12, 17:45

**背景**: 由 Simon Willison 创建的 llm CLI 工具是一个流行的命令行界面和 Python 库，用于与包括 OpenAI、Anthropic 的 Claude、Google 的 Gemini 和 Meta 的 Llama 在内的数十种大语言模型进行交互。OpenAI 的 /v1/responses 端点是其下一代 API，旨在取代旧版 /v1/chat/completions 端点，原生支持复杂的多工具交互和交错思考。交错思考允许模型在多次工具调用之间穿插推理步骤，从而基于中间结果做出更细致的决策，但会增加 token 使用量和响应延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw / llm : Access large language models from the...</a></li>
<li><a href="https://jessearmand.com/responses-vs-chat-completions/">Streaming APIs: OpenAI 's Responses vs . Chat Completions</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/interleaved_thinking/">Interleaved Thinking - vLLM</a></li>

</ul>
</details>

**标签**: `#llm-cli`, `#openai`, `#reasoning-models`, `#ai-tooling`, `#gpt-5`

---

<a id="item-3"></a>
## [Anthropic 推出 Claude Opus 4.7 快速模式研究预览](https://www.v2ex.com/t/1212317#reply2) ⭐️ 8.0/10

Anthropic 已将 Claude Opus 4.7 的「快速模式」以研究预览形式发布，现已通过 API 和 Claude Code 开放使用。该配置的响应速度是标准 Opus 模型的 2.5 倍，面向低延迟场景。 此次更新大幅降低了 Anthropic 最强模型之一的推理延迟，使其在实时交互场景（如智能编程工作流）中更加实用。这也反映了行业趋势：在不牺牲模型能力的前提下优化前沿模型的响应速度。 Claude Opus 4.7 快速模式并非新模型，而是一种低延迟的 API 配置，定价为输入 30 美元/MTok、输出 150 美元/MTok。用户需要 Claude Code v2.1.139 或更高版本才能使用该功能。

rss · V2EX · May 13, 01:33

**背景**: Claude Code 是 Anthropic 推出的智能编程工具，可在终端和 IDE 中运行，能够理解代码库、编辑文件并执行命令。LLM API 的定价通常以每百万 token（MTok）的成本来衡量，不同模型和供应商之间价格差异很大。快速模式允许开发者在同一底层模型上以更高成本换取更低延迟，而不必切换到更便宜但能力较弱的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.cloudzero.com/blog/llm-api-pricing-comparison/">LLM API Pricing Comparison In 2026: Every Major Model, Ranked By Cost</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI API`, `#LLM`, `#Low-Latency Inference`

---

<a id="item-4"></a>
## [宇树发布全球首款量产载人变形机甲 GD01](https://m.mydrivers.com/newsview/1121657.html) ⭐️ 8.0/10

宇树科技正式发布了 GD01，这是全球首款量产版载人变形机甲，定价 390 万元人民币起。该机甲重约 500 公斤，可直立行走并搭载乘员，也能迅速变形为四足状态行进。 GD01 代表了具身智能和先进机器人领域的重大里程碑，是首款将双足和四足运动结合的商业化载人机甲。这一发布标志着变形机器人正从科幻概念走向现实产品，在文旅展示、特种作业和私人高端出行等领域具有广阔应用前景。 GD01 采用高强度合金与精密伺服驱动，实测演示中单拳即可锤倒砖墙。整机包括智能操控系统在内的所有核心部件均由宇树全自研，定位为民用交通工具而非军事装备。

telegram · @zaihuapd · May 12, 05:25

**背景**: 宇树科技由王兴兴于 2016 年创立，总部位于杭州，最初专注于消费级高性能四足机器人。2024 年公司开始生产人形机器人，最新款人形机器人售价约 16000 美元。具身智能是指嵌入物理实体的人工智能系统，通过传感器和执行器感知并与真实世界交互，代表了从纯数字 AI 到物理交互系统的重要演进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Embodied AI`, `#Unitree`, `#Humanoid Robots`, `#Frontier Tech`

---

<a id="item-5"></a>
## [美国商务部网站悄然删除 AI 模型安全测试协议细节](https://www.reuters.com/legal/litigation/microsoft-google-xai-security-test-details-deleted-us-government-website-2026-05-11/) ⭐️ 8.0/10

The US Department of Commerce quietly deleted details from its website regarding agreements with Google, xAI, and Microsoft to test new AI models for safety vulnerabilities before public deployment.

telegram · @zaihuapd · May 12, 13:38

**标签**: `#AI Safety`, `#AI Governance`, `#AI Regulation`, `#US Policy`, `#Frontier Models`

---

<a id="item-6"></a>
## [SpaceX 与 Google 磋商轨道数据中心发射合作](https://www.wsj.com/tech/spacex-google-in-talks-to-explore-data-centers-in-orbit-7b7799e2) ⭐️ 8.0/10

Google is in talks with SpaceX to launch orbital data centers for its 'Project Suncatcher', while SpaceX is also positioning itself as a major AI infrastructure provider through a massive GPU compute deal with Anthropic.

telegram · @zaihuapd · May 12, 16:28

**标签**: `#AI Infrastructure`, `#SpaceX`, `#Google`, `#Anthropic`, `#Data Centers`

---

<a id="item-7"></a>
## [MiniCPM-V 4.6：超高效的移动端视觉语言模型](https://www.producthunt.com/products/minicpm-4-0) ⭐️ 8.0/10

MiniCPM-V 4.6 已正式发布，这是一款仅有 13 亿参数的超高效开源视觉语言模型，专门针对在移动端和边缘设备上本地运行进行了优化。它致力于在极小的参数规模内提供接近 GPT-4o 级别的多模态能力，包括单图、多图和高帧率视频理解功能。 将前沿的视觉语言能力压缩到 13 亿参数并在手机上运行，标志着端侧 AI 迈出了重要一步，实现了无需依赖云端即可进行实时多模态推理。这一进展通过降低硬件门槛来推动强大 VLM 的普及，使隐私敏感型应用和离线场景在整个边缘 AI 生态系统中受益。 MiniCPM-V 在同等规模模型中，于 MMMU、MME 和 MMbench 等多个基准测试上达到了最先进的性能表现。该模型由 OpenBMB 团队开发，采用开源方式在 Hugging Face 上发布，专为在资源受限的移动硬件上高效部署而设计。

producthunt · Zac Zuo · May 12, 03:30

**背景**: 视觉语言模型（VLM）是一种能够同时理解和生成图像与文本信息的 AI 系统，将大语言模型的能力扩展到了纯文本处理之外。边缘 AI 是指在靠近用户的设备上本地运行 AI 模型，与云端方案相比可以降低延迟并提升隐私保护。LLaVA、InstructBLIP 和 MiniGPT-4 等开源 VLM 作为 GPT-4V 和 Google Gemini 等商业模型的小型替代方案相继出现，使多模态 AI 在实验和部署方面变得更加普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/openbmb/MiniCPM-V">openbmb/ MiniCPM - V · Hugging Face</a></li>
<li><a href="https://github.com/mosabutey/minicpm-v">GitHub - mosabutey/ minicpm - v : MiniCPM - V 4.5: A GPT-4o Level...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision-language_model">Vision-language model</a></li>

</ul>
</details>

**标签**: `#AI`, `#Vision-Language Model`, `#Edge AI`, `#Open Source`, `#Mobile AI`

---