---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 103 items, 9 important content pieces were selected

---

1. [vllm-project/vllm released v0.21.0](#item-1) ⭐️ 8.0/10
2. [Antirez 发布 DwarfStar4 用于本地 DeepSeek 推理](#item-2) ⭐️ 8.0/10
3. [OpenAI 将 Codex 编程代理引入 ChatGPT 移动应用预览版](#item-3) ⭐️ 8.0/10
4. [Cerebras 上市首日暴涨，成为今年最大规模 IPO](#item-4) ⭐️ 8.0/10
5. [开源 3D 工具包：单张图片生成可交互 3D 世界](#item-5) ⭐️ 8.0/10
6. [美国批准英伟达 H200 对华销售，涉及多家头部企业](#item-6) ⭐️ 8.0/10
7. [DeepSeek 对话系统存在会话隔离漏洞：未闭合 <think 标签可泄露他人对话](#item-7) ⭐️ 8.0/10
8. [京东上线 AI 硬件自营专区，多款受制裁 NVIDIA 芯片恢复销售](#item-8) ⭐️ 8.0/10
9. [ChatGPT Android 版拆解发现 Codex 远程桌面控制功能](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vllm-project/vllm released v0.21.0](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 introduces major infrastructure updates including Blackwell GPU support for DeepSeek-R1/Kimi-K25 via the TOKENSPEED_MLA backend, a new Hybrid Memory Allocator for KV offloading, and speculative decoding for reasoning models.

github · vllm-project/vllm · May 14, 23:15

**标签**: `#AI Infrastructure`, `#LLM Serving`, `#vLLM`, `#Blackwell GPUs`, `#Inference Optimization`

---

<a id="item-2"></a>
## [Antirez 发布 DwarfStar4 用于本地 DeepSeek 推理](https://antirez.com/news/165) ⭐️ 8.0/10

Redis 的创造者 Antirez 发布了 DwarfStar4（DS4），这是一个小型、专注的本地 LLM 推理运行时，专门针对在高内存 Mac（96GB 以上）、NVIDIA CUDA 硬件和 AMD ROCm 环境上运行 DeepSeek V4 Flash 进行了优化。该项目基于 GGML 和 llama.cpp 构建，提供与 OpenAI 兼容的聊天补全服务器端点，可供本地编程代理使用。 DwarfStar4 表明，像 DeepSeek 这样的前沿开源 AI 模型现在可以在本地运行，早期用户称其性能惊人地接近 Claude 等专有模型。这标志着本地 AI 部署的一个重要里程碑，使开发者和研究人员能够在不依赖云 API 或专有服务的情况下利用顶级模型智能。 该运行时目前需要大约 96GB 的 VRAM 才能有效运行 DeepSeek，目标设备包括高端 MacBook 和 NVIDIA DGX Spark 系统。该项目使用 imatrix 量化，一些用户报告其效果优于 OpenRouter 等平台上其他推理后端所使用的量化方法。

hackernews · caust1c · May 14, 22:29 · [社区讨论](https://news.ycombinator.com/item?id=48142108)

**背景**: DeepSeek 是一家中国 AI 公司，其开源大语言模型（特别是 DeepSeek-V3 和 DeepSeek-R1）已能与 OpenAI 和 Anthropic 的顶级闭源模型相媲美，并在 MIT 等宽松许可证下发布。GGML 是由 Georgi Gerganov 创建的机器学习张量库，支持多种量化格式以显著降低内存占用，它也是广泛使用的开源 LLM 推理引擎 llama.cpp 的基础。Antirez 最为人熟知的身份是 Redis（全球最受欢迎的内存数据存储之一）的创造者，他进入本地 AI 推理领域引起了开发者社区的极大关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ ds 4 : DeepSeek 4 Flash local inference engine for...</a></li>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml-org/ggml: Tensor library for machine learning · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区整体上非常热情，用户对本地 DeepSeek 模型的智能水平如此接近 Claude 表示惊讶，尽管承认速度要慢得多。一位用户注意到该模型足够"自觉"，能够在未被告知的情况下识别出自己的服务器进程，这是以前在本地模型中从未观察到的行为。然而，一些开发者质疑构建特定模型推理引擎而非贡献给 llama.cpp 的合理性，认为这在一个可能很快过时的单一模型上重复投入精力，而开发者注意力是稀缺资源，更适合用于通用工具的开发。

**标签**: `#LLM Inference`, `#Local AI`, `#DeepSeek`, `#Open Source`, `#GGML`

---

<a id="item-3"></a>
## [OpenAI 将 Codex 编程代理引入 ChatGPT 移动应用预览版](https://x.com/ericmitchellai/status/2055098574669791243) ⭐️ 8.0/10

OpenAI 在 ChatGPT 移动应用中推出了 Codex 编程代理的预览功能，用户可以直接在手机上启动新任务、审查输出、指导执行并批准下一步操作。实际的代码执行则持续在用户的远程本地机器（如笔记本电脑、Mac mini 或开发机）上进行，而非在云端运行。 此次发布标志着 AI 编程代理能力向移动平台的重要扩展，使开发者能够随时随地管理和监控编程任务，不再受限于桌面环境。这种云端中继加本地执行的混合模式，将移动访问的便捷性与代码及凭证保留在本地的安全性相结合，有望重塑开发者的工作流程。 该系统采用安全中继层架构，能够实时同步工作线程、审批请求和项目上下文，并将截图、终端输出等结果回传至移动应用。所有文件和凭证均保留在本地机器上，不会上传至云端，但目前该预览功能暂不支持 Windows 端。

rss · AI Hot · May 15, 01:30

**背景**: Codex 是 OpenAI 开发的 AI 编程代理，用于编写功能、修复错误和提出拉取请求等软件工程任务，最初于 2025 年 4 月以 Codex CLI 的形式发布。它可通过多个平台使用，包括 ChatGPT 网页应用、Codex CLI、VS Code 扩展和桌面应用，每个任务在独立的沙盒环境中运行。Codex 包含在 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 订阅计划中，支持本地和云端两种执行工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Using Codex with your ChatGPT plan | OpenAI Help Center</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI Agents`, `#Mobile App`, `#Coding`

---

<a id="item-4"></a>
## [Cerebras 上市首日暴涨，成为今年最大规模 IPO](https://x.com/SemiAnalysis_/status/2055087062672429348) ⭐️ 8.0/10

AI 芯片制造商 Cerebras Systems 公司完成了 IPO，融资约 55 亿美元，成为今年最大规模的公开募股，股价在上市首日暴涨高达 90%。SemiAnalysis 团队表示他们早已预判到这一强劲的市场表现。 Cerebras 是前沿 AI 基础设施领域的重要参与者，其 IPO 的巨大成功表明投资者对 AI 芯片市场中 NVIDIA 替代方案的强烈需求。这一事件对整个 AI 硬件生态系统具有里程碑意义，可能加速该行业的资金投入和技术发展。 Cerebras 股价在早盘交易中一度暴涨 90%，收盘时涨幅约为 68%。公司首席执行官 Andrew Feldman 已公开谈及公司的 AI 芯片生产能力以及与 NVIDIA 的竞争定位。

rss · AI Hot · May 15, 00:45

**背景**: Cerebras Systems 以其晶圆级引擎（WSE）闻名，这是世界上最大的 AI 处理器，采用单晶圆级集成芯片设计，将计算、内存和互连结构整合在一起。与 NVIDIA 传统的基于 GPU 的方案不同，Cerebras 的架构专为超快速 AI 训练和推理而构建，声称具有业界领先的效率和更低的功耗。该公司将自身定位为以创纪录速度在生产规模上部署前沿 AI 模型的首选平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/video/ai-chipmaker-cerebras-climbs-68-201756755.html">AI Chipmaker Cerebras Climbs 68% After Year's Biggest IPO - Yahoo Finance</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Product - Chip - Cerebras</a></li>

</ul>
</details>

**标签**: `#Cerebras`, `#AI Hardware`, `#IPO`, `#AI Chips`, `#Tech Industry`

---

<a id="item-5"></a>
## [开源 3D 工具包：单张图片生成可交互 3D 世界](https://x.com/berryxia/status/2055086814009180316) ⭐️ 8.0/10

开发者 @neilsonks 开源了一套专为 Claude Code 设计的完整 3D 生成工具包，能够将单张输入图片自动转换为包含环境、网格、物理、灯光和音频的全套可交互 3D 场景，整个过程仅需几分钟。该项目已在 GitHub 上开源，将以往需要数天的 2D 转 3D 工作流程大幅压缩。 该工具包通过自动化从 2D 图像理解到 3D 场景组装（含物理和音频）的完整流程，代表了 AI 辅助世界构建的重大飞跃。它降低了游戏开发者、空间计算创作者和产品可视化团队的门槛，支持快速原型设计，有望重塑整个 3D 行业的创意工作流。 该流程首先利用图像与 3D 生成技术提取物体并生成高质量网格，随后移除物体以获得干净的静态背景，最后为整个场景添加物理模拟、实时灯光和环境音效。配套的查看器支持对生成物体的点击编辑和一键导出功能。

rss · AI Hot · May 15, 00:44

**背景**: Claude Code 是 Anthropic 推出的智能编程工具，能够理解代码库、编辑文件并运行命令，帮助开发者更快地交付项目。单图生成 3D 一直是活跃的研究领域，Unique3D 和 InstantMesh 等项目已展示了利用多视角扩散模型和稀疏视角大型重建模型从单张图片高效重建 3D 网格的能力。该工具包在这些技术进步的基础上，在 AI 辅助编程环境中编排了包含物理和音频在内的完整场景创建流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://wukailu.github.io/Unique3D/">Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image</a></li>
<li><a href="https://github.com/TencentARC/InstantMesh">GitHub - TencentARC/InstantMesh: InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-view Large Reconstruction Models · GitHub</a></li>

</ul>
</details>

**标签**: `#3D Generation`, `#Open Source AI`, `#Claude Code`, `#World Building`, `#Computer Vision`

---

<a id="item-6"></a>
## [美国批准英伟达 H200 对华销售，涉及多家头部企业](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) ⭐️ 8.0/10

美国商务部已批准约 10 家中国企业购买英伟达 H200 芯片，买家包括阿里巴巴、腾讯、字节跳动和京东等，联想和富士康等分销商也获得许可，单一客户最多可购买 7.5 万颗。但截至目前尚未有任何交付完成，部分中国企业在北京方面的指导下转趋谨慎，黄仁勋此次访华被视为推动交易落地的重要尝试。 这一进展直接影响全球 AI 算力格局和中美 AI 竞赛，因为获取先进芯片是训练前沿 AI 模型最关键的因素。此次批准表明美国出口管制执行出现了微妙的调整，在战略限制与商业利益之间寻求平衡，同时也凸显了中国在依赖进口芯片与发展国产替代方案之间的持续博弈。 H200 是英伟达的高性能 AI 推理和训练芯片，单一客户最多可购买 7.5 万颗，代表着相当可观的算力规模。尽管获得了美方批准，但尚未完成任何交付这一事实表明，中国监管层面的谨慎态度和地缘政治不确定性仍然是实际交易的重大障碍。

telegram · @zaihuapd · May 14, 08:57

**背景**: 自 2022 年 10 月以来，美国政府对中国实施了严格的 AI 芯片出口管制，旨在限制中国获取前沿 AI 研发和国防应用所需的算力。这些管制措施迫使中国 AI 企业只能使用合法渠道获取但性能较弱的芯片，造成了显著的性能差距。英伟达多次为中国市场开发符合出口规定的修改版芯片，而中国同时也加速了对国产 AI 芯片替代方案的投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://foreignpolicy.com/2025/09/19/ai-china-chips-export-controls-h20-nvidia/">China ’s Chip Dependence Is Good for U . S . Interests | Foreign Policy</a></li>
<li><a href="https://www.anthropic.com/research/2028-ai-leadership">Our views on the AI competition between the US and China .</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Nvidia`, `#US-China tech`, `#AI infrastructure`, `#export controls`

---

<a id="item-7"></a>
## [DeepSeek 对话系统存在会话隔离漏洞：未闭合 <think 标签可泄露他人对话](https://github.com/deepseek-ai/DeepSeek-R1/issues/840) ⭐️ 8.0/10

2026 年 5 月 11 日提交的一份漏洞报告（GitHub issue #840）声称，在 DeepSeek 的 Web 和 API 对话系统中，于全新的空对话里发送未闭合的 `<think` 字符串，模型会返回其他用户的对话历史片段，可能包含代码、密钥等敏感信息。 如果漏洞得到确认，这将是一个广泛使用的前沿 AI 模型中严重的跨用户数据泄露漏洞，直接威胁用户隐私和对 AI 部署平台的信任。但社区对此持怀疑态度，认为观察到的行为可能是 AI 幻觉而非真实的数据泄露。 报告者（cancat2024）以负责任的方式披露了该问题，并未利用漏洞获取或传播他人隐私数据。`<think` 标签是 DeepSeek-R1 思维链推理机制的一部分，模型在输出最终答案前会先输出内部推理过程，未闭合的标签可能导致模型的上下文解析出现混乱。

telegram · @zaihuapd · May 14, 13:15

**背景**: DeepSeek-R1 是一个专注于推理的大语言模型，它使用"思维模式"，在提供最终答案前会输出被 `<think...</think` 标签包裹的思维链推理过程。会话隔离是多用户 LLM 部署中的基本安全要求，确保一个用户的对话上下文和数据不能被其他用户访问。LLM 中的跨用户数据泄露虽然罕见，但属于一类关键漏洞，架构层面的弱点可能导致不同用户会话之间的上下文串通。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/guides/thinking_mode">Thinking Mode | DeepSeek API Docs</a></li>
<li><a href="https://www.linkedin.com/pulse/publicly-available-llms-unseen-vulnerabilities-real-risks-kpjef">Publicly Available LLMs: Unseen Vulnerabilities and Real Risks for...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该漏洞表示怀疑，指出在第三方部署的 DeepSeek 实例中也观察到了相同的行为，这表明返回的"其他用户对话"实际上可能是 AI 幻觉而非真实的泄露数据。这是一个重要的反驳论点，因为如果无法访问其他用户数据的第三方实例也能产生类似输出，说明模型是在编造看似合理的对话片段，而非检索真实的跨会话数据。

**标签**: `#AI Security`, `#DeepSeek`, `#Vulnerability`, `#Data Privacy`, `#LLM`

---

<a id="item-8"></a>
## [京东上线 AI 硬件自营专区，多款受制裁 NVIDIA 芯片恢复销售](https://u.jd.com/HaDkFMa) ⭐️ 8.0/10

京东开设了"AI 硬件京东自营专区"，首批上架了 NVIDIA H100、RTX PRO 6000 Blackwell 服务器版以及 GeForce RTX 5090 32G 涡轮版等高端 AI 芯片，用户可直接购买。 这些此前受限的芯片通过中国主流电商平台公开销售，可能显著提升中国获取高端 AI 算力的能力，直接冲击美国旨在限制中国前沿 AI 能力的出口管制体系。 RTX 5090 涡轮版据称为无阉割的全球统一规格，没有任何降频或规格缩减；RTX PRO 6000 面向专业渲染与数据中心应用场景。H100 此前曾因美国制裁被明确禁止对华出口。

telegram · @zaihuapd · May 14, 15:15

**背景**: 自 2022 年以来，美国政府对中国实施了日益严格的高端 AI 芯片出口管制，重点针对 NVIDIA 的 H100、A100 及后续的 H200 系列，旨在遏制中国的 AI 发展。尽管有这些限制，据报道仍有大量 NVIDIA 芯片通过走私渠道流入中国，估计价值约 10 亿美元的芯片绕过了出口管制。美国也已解除部分旧一代芯片的限制（如 H200），将管制重点转向更新的 Blackwell 架构（B200）芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/aayushchugh_america-banned-exports-of-nvidia-h100-and-activity-7431598668446613504-bXb8">US restricts Nvidia chip exports to China, China develops domestic AI alternatives | Ayush Chugh posted on the topic | LinkedIn</a></li>
<li><a href="https://www.reddit.com/r/explainlikeimfive/comments/1k4domz/eli5_arent_the_export_controls_on_nvidia_chips/">ELI5: aren't the export controls on NVIDIA chips absurdly easy to bypass? - Reddit</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#NVIDIA`, `#Compute Infrastructure`, `#Export Controls`, `#GPUs`

---

<a id="item-9"></a>
## [ChatGPT Android 版拆解发现 Codex 远程桌面控制功能](https://t.me/zaihuapd/41388) ⭐️ 8.0/10

ChatGPT Android 版 1.2026.125 的 APK 拆解发现了多处字符串，显示 OpenAI 正在开发一项新功能，允许手机远程查找、控制和重连活跃的 Codex 桌面会话。该功能要求桌面端登录同一账号，目前仍在开发中，尚无可用预览，也未公布正式上线时间。 这一发现表明 OpenAI 正在推动其 AI 编程代理在移动端和桌面端之间的打通，使开发者能够随时随地通过手机监控和管理长时间运行的 Codex 任务。这标志着 AI 代理在跨平台无缝集成和可访问性方面迈出了重要一步。 拆解发现的字符串涉及远程会话发现、重连已有会话以及移动端与桌面端的账号匹配要求等功能。该功能目前在任何预览版本中都不可用，实际实现方式和用户体验仍不得而知。

telegram · @zaihuapd · May 14, 21:48

**背景**: OpenAI Codex 是一个与 ChatGPT 集成的 AI 编程代理，允许用户将复杂的桌面任务委托给 AI，并行管理多个代理，并在长时间运行的任务中进行协作。Codex 桌面应用最初在 macOS 上推出，2026 年 3 月已扩展至 Windows 平台。APK 拆解是一种常见技术，通过反编译 Android 应用安装包来发现隐藏在代码字符串资源中的未发布功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-codex-app/">Introducing the Codex app | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://medium.com/commencis/apk-teardown-in-a-nutshell-7701c3628bf5">APK Teardown in a Nutshell. In short, converting/decompiling | Medium</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#APK Teardown`, `#Remote Desktop`, `#AI Agents`

---