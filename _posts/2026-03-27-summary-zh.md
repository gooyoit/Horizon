---
layout: default
title: "Horizon Summary: 2026-03-27 (ZH)"
date: 2026-03-27
lang: zh
---

> From 86 items, 13 important content pieces were selected

---

1. [LiteLLM PyPI 软件包遭供应链攻击](#item-1) ⭐️ 9.0/10
2. [小米 MiMo-V2-Pro 登顶 OpenRouter，周消耗超 3 万亿 token](#item-2) ⭐️ 9.0/10
3. [Anthropic 获初步禁令叫停美国政府对 Claude 的禁令](#item-3) ⭐️ 9.0/10
4. [Google 发布实时多模态 AI 模型 Gemini 3.1 Flash Live](#item-4) ⭐️ 9.0/10
5. [苹果拟在 iOS 27 中向第三方 AI 助手开放 Siri](#item-5) ⭐️ 9.0/10
6. [交互式教程详解大语言模型量化与浮点数表示](#item-6) ⭐️ 8.0/10
7. [字节跳动通过剪映全球推出 Dreamina Seedance 2.0](#item-7) ⭐️ 8.0/10
8. [ChatGPT 广告试水年化收入破亿美元](#item-8) ⭐️ 8.0/10
9. [Anvil 支持并行运行多个 Claude 实例](#item-9) ⭐️ 8.0/10
10. [AI 一天内用 Go 重写 JSONata](#item-10) ⭐️ 7.0/10
11. [知行机器人完成近亿元融资，发力灵巧手研发](#item-11) ⭐️ 7.0/10
12. [谷歌在 Android 17 引入后量子加密](#item-12) ⭐️ 7.0/10
13. [中科院发布开源“香山”RISC-V 处理器与“如意”操作系统](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM PyPI 软件包遭供应链攻击](https://simonwillison.net/2026/Mar/26/response-to-the-litellm-malware-attack/#atom-everything) ⭐️ 9.0/10

2026 年 3 月 24 日至 26 日，广泛使用的 LiteLLM Python 软件包的 1.82.7 和 1.82.8 版本被发现包含一个恶意的 litellm_init.pth 文件，该文件会在 Python 启动时自动执行窃取凭证的代码。这一漏洞由机器学习工程师 Callum McMahon 发现，他借助 Anthropic 的 Claude 实时分析恶意软件并协调向 PyPI 安全团队披露。 此次事件暴露了 AI/ML 软件供应链中的严重漏洞，因为 LiteLLM 是跨多个大模型提供商路由 API 调用的基础工具。攻击可能影响数十万开发者和系统，凸显了被攻破的开源软件包如何成为大规模数据窃取的载体。 恶意软件位于 PyPI wheel 中的一个 34,628 字节的 litellm_init.pth 文件内，利用 Python 的.pth 机制在每次解释器启动时执行 base64 编码的恶意代码——无需显式导入 litellm。该载荷会窃取环境变量和凭证，证据表明攻击者可能已攻破维护者的 PyPI 账户。

rss · Simon Willison · Mar 26, 23:58

**背景**: LiteLLM 是一个流行的开源库，通过统一接口简化对各类大语言模型（如 OpenAI、Anthropic 及开源模型）API 的调用。PyPI（Python Package Index）是分发 Python 包的默认仓库，而.pth 文件是 Python 在启动时自动执行的配置文件（若置于 site-packages 目录中），这使其成为持久化恶意软件的隐蔽载体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/popular-litellm-pypi-package-compromised-in-teampcp-supply-chain-attack/">Popular LiteLLM PyPI package backdoored to steal credentials ...</a></li>
<li><a href="https://docs.litellm.ai/blog/security-update-march-2026">Security Update: Suspected Supply Chain Incident - liteLLM</a></li>
<li><a href="https://www.truesec.com/hub/blog/malicious-pypi-package-litellm-supply-chain-compromise">Malicious PyPI Package - LiteLLM Supply Chain Compromise - Truesec</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞使用 Claude 实时安全分析威胁的做法，并强调需要加强对软件包仓库的监控。一些人警告称，LLM 代理在缺乏安全防护的情况下执行命令存在风险，还有人呼吁 PyPI 提供实时更新流，以支持社区更快地发现威胁。

**标签**: `#AI Security`, `#LLM`, `#Supply Chain Attack`, `#Malware`, `#DevSecOps`

---

<a id="item-2"></a>
## [小米 MiMo-V2-Pro 登顶 OpenRouter，周消耗超 3 万亿 token](https://36kr.com/newsflashes/3740507252670720?f=rss) ⭐️ 9.0/10

小米推出的万亿参数混合专家（MoE）模型 MiMo-V2-Pro 成为 OpenRouter 平台上首个周 token 消耗量突破 3 万亿的模型，并在编程领域占据超 30%的市场份额。 这一里程碑表明国产大模型在智能体（Agent）和编程任务中获得强劲的实际应用，以更低的成本挑战西方主流模型，凸显了高效、可扩展的 MoE 架构在大模型竞争中的战略价值。 MiMo-V2-Pro 总参数达 1 万亿，每次推理激活约 420 亿参数，支持百万级上下文窗口，专为智能体工作流和编程优化，性能据称可媲美 Claude Sonnet 4.6，而成本仅为后者的一小部分。

rss · 36kr · Mar 27, 01:35

**背景**: 混合专家（MoE）是一种模型架构，通过门控机制将输入动态分配给多个专业化子网络（“专家”），每次仅激活部分专家，从而在模型容量与计算效率之间取得平衡。该技术使 MiMo-V2-Pro 等万亿参数模型能在不显著增加推理成本的前提下实现高性能。Google、Mistral 等公司已采用 MoE，小米如今也加入这一技术路线以实现高效扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://awesomeagents.ai/models/mimo-v2-pro/">Xiaomi MiMo - V 2 - Pro - Agentic 1T MoE Model | Awesome Agents</a></li>
<li><a href="https://nowletus.com/news/xiaomi-stuns-with-new-mimo-v2-pro-llm-nearing-gpt-5-2-opus-4-6-performance-at-a-fraction-of-the-cost-now870.html">Xiaomi stuns with new MiMo - V 2 - Pro LLM nearing... | NOW LET US</a></li>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts (MoE)? How It Works, Use Cases & More | DataCamp</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#AI Infrastructure`, `#Model Adoption`, `#Agent AI`

---

<a id="item-3"></a>
## [Anthropic 获初步禁令叫停美国政府对 Claude 的禁令](https://www.ithome.com/0/933/160.htm) ⭐️ 9.0/10

美国一名联邦法官批准了 Anthropic 的初步禁令申请，暂停特朗普政府对其 Claude 模型的禁令，裁定政府可能违反了宪法第一修正案，且缺乏国家安全主张的法律依据。 该裁决质疑了美国政府在缺乏正当程序的情况下以国家安全为由限制本土 AI 企业的权力，可能为 AI 监管与言论自由、企业权利之间的关系树立重要先例。 法官林萍指出，政府将 Anthropic 列为“供应链风险”具有报复性质，因其公开倡导 AI 安全立场；Anthropic 是首家被如此定性的美国公司，此前该标签仅用于外国对手。禁令在案件审理期间暂停执行，而最终判决可能需数月。

rss · IT HOME · Mar 27, 02:11

**背景**: 美国政府历来将“供应链风险”标签用于限制被认为威胁国家安全的外国技术，如华为或 TikTok。Anthropic 由前 OpenAI 研究人员共同创立，开发 Claude 系列大语言模型，并强调 AI 安全与“合宪 AI”原则。特朗普政府针对 AI 工具的行政措施引发了对新兴技术治理中政府越权的担忧。

**标签**: `#AI Policy`, `#LLM`, `#Anthropic`, `#Legal`, `#National Security`

---

<a id="item-4"></a>
## [Google 发布实时多模态 AI 模型 Gemini 3.1 Flash Live](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/) ⭐️ 9.0/10

Google 发布了 Gemini 3.1 Flash Live，这是一款支持 90 多种语言的实时多模态 AI 模型，现已集成到 Gemini Live、Search Live、企业 API 和 Google AI Studio 中。该模型带来更快响应、更长上下文记忆（提升至此前的 2 倍），并增强了在嘈杂环境中的语音处理能力。 此次发布大幅推进了实时对话 AI 的发展，使消费者和企业应用能够在全球范围内实现流畅的“语音优先”交互。这有助于 Google 在日益增长的实时多模态 AI 助手市场中增强竞争力，此类助手能理解并响应复杂的上下文用户输入。 Gemini 3.1 Flash Live 基于 Gemini 3 Pro 构建，支持文本、图像、音频和视频等多模态输入，上下文窗口达 128K tokens，并可生成音频与文本输出。该模型在音高、语速等韵律特征识别方面表现优异，并具备强大的工具调用能力，可在实时对话中执行复杂任务。

telegram · zaihuapd · Mar 26, 17:01

**背景**: 多模态 AI 模型能够跨多种数据类型（如文本、语音、图像和视频）处理和生成信息，从而实现更自然的人机交互。实时音频 AI（如 Gemini Live）旨在支持具有上下文记忆的连续低延迟语音对话，超越传统的回合制聊天界面。Google 的 Gemini 系列是其旗舰大语言模型，包含针对速度（Flash）、质量（Pro）或实时交互（Flash Live）优化的不同版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-1-flash-live/">Gemini 3.1 Flash Live - Model Card — Google DeepMind</a></li>
<li><a href="https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Flash-Live-Model-Card.pdf">Gemini 3.1 Flash with Native Audio Capabilities (Flash Live)</a></li>
<li><a href="https://wallstreetcn.com/articles/3768515">谷歌发布最高质量音频模型Gemini 3.1 Flash Live，低延迟、高精度响应...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Multimodal AI`, `#Real-time AI`, `#Gemini`, `#AI Deployment`

---

<a id="item-5"></a>
## [苹果拟在 iOS 27 中向第三方 AI 助手开放 Siri](https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27?srnd=phx-technology) ⭐️ 9.0/10

苹果计划在 iOS 27 中允许 Gemini、Claude 等第三方 AI 助手直接与 Siri 集成，用户可像当前调用 ChatGPT 一样将查询转交给这些服务。此举将打破 ChatGPT 在 Apple Intelligence 中的独家地位。 此举标志着苹果向开放的 AI 生态系统迈出关键一步，促进大语言模型之间的竞争，赋予用户更多选择权，并将苹果定位为 AI 平台协调者而非唯一提供者。这可能加速移动端设备端与云端 LLM 的普及。 集成将通过 App Store 实现，用户可在 Apple Intelligence 和 Siri 设置中手动启用或关闭相关服务；但该功能在 2026 年 6 月 8 日 WWDC 正式发布前仍可能调整或延期。

telegram · zaihuapd · Mar 27, 01:40

**背景**: Apple Intelligence 是苹果于 2024 年 6 月推出的生成式 AI 系统，内置于 iOS 18、iPadOS 18 和 macOS Sequoia 中，结合设备端与云端处理能力。初期仅支持 ChatGPT 作为外部大语言模型选项。支持设备包括 iPhone 15 Pro/Pro Max、iPhone 16 全系，以及搭载 M1 或更高芯片的 Mac 和 iPad。值得注意的是，由于监管限制，Apple Intelligence 目前在中国大陆地区不可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence - Apple</a></li>

</ul>
</details>

**标签**: `#AI Assistants`, `#Siri`, `#iOS 27`, `#LLM Integration`, `#Apple Intelligence`

---

<a id="item-6"></a>
## [交互式教程详解大语言模型量化与浮点数表示](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose 发布了一篇名为《从零开始理解量化》的交互式深度教程，详细解释了大语言模型（LLM）量化技术，并包含一个用于理解二进制浮点数表示的可视化工具。文章还介绍了“异常值”（outlier values）的概念——这些罕见但关键的权重一旦被移除会严重影响模型性能。 该教程让复杂但关键的 AI 工程技巧——量化——变得易于理解，帮助开发者在资源受限的硬件上更高效地部署模型。了解异常值处理和精度权衡有助于在不造成灾难性质量损失的前提下优化模型。 教程指出，将精度从 16 位降至 8 位几乎不会带来质量损失，而 4 位量化仍能保留约 90%的原始性能（具体取决于评估指标）。作者使用 llama.cpp 的困惑度（perplexity）工具和 GPQA 基准对 Qwen 3.5 9B 模型进行测试，并解释了某些量化方案如何通过单独存储来保留异常值。

rss · Simon Willison · Mar 26, 16:21

**背景**: 大语言模型量化是一种模型压缩技术，将高精度权重（如 16 位浮点数）转换为低精度格式（如 8 位或 4 位整数），以减少内存占用并加速推理。二进制浮点数表示遵循 IEEE 754 标准，使用符号位、指数位和尾数位编码实数，这对理解 AI 模型中的数值精度限制至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single-precision_floating-point_format">Single-precision floating-point format - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Quantization`, `#AI Engineering`, `#Model Optimization`, `#Technical Tutorial`

---

<a id="item-7"></a>
## [字节跳动通过剪映全球推出 Dreamina Seedance 2.0](https://www.ithome.com/0/933/197.htm) ⭐️ 8.0/10

字节跳动正式推出由全新多模态 AI 模型 Dreamina Seedance 2.0 驱动的 CapCut Video Studio，支持无需时间轴的端到端 AI 视频创作。该工具现已在非洲、南美洲、中东和东南亚上线，支持生成最长 15 秒的视频，并提供六种宽高比选项。 此次发布标志着通过生成式 AI 普及专业级视频创作的重要一步，将故事板、角色构建和剪辑整合到一体化工作流中。其严格的版权保护措施和内容溯源功能也为创意类 AI 工具的负责任部署树立了先例。 Dreamina Seedance 2.0 支持在无参考图像情况下生成最长 15 秒的视频，包含可见 AI 水印和符合 C2PA 标准的内容凭证，并采用“隐形水印”用于平台外识别。初期推广阶段限制基于真实人脸图像生成视频，并通过主动监控与创作者合作防止未经授权的知识产权内容生成。

rss · IT HOME · Mar 27, 02:33

**背景**: Dreamina Seedance 2.0 是字节跳动开发的用于视频合成的多模态生成式 AI 模型，属于集成在 CapCut（中国版名为剪映）中的 Dreamina 套件的一部分。此类多模态 AI 模型融合文本、图像和音频理解能力，以生成连贯的视频内容。CapCut 最初是一款移动视频编辑器，现已发展为与 Runway、Pika Labs 等竞争的 AI 创意平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/03/26/bytedances-new-ai-video-generation-model-dreamina-seedance-2-0-comes-to-capcut/">ByteDance's new AI video generation model , Dreamina Seedance ...</a></li>
<li><a href="https://www.capcut.com/ai-creator/start">CapCut video studio ｜The all-in-one canvas for video creation</a></li>
<li><a href="https://dreamina.capcut.com/tools/seedance-2-0">Free Seedance 2 . 0 — Multimodal AI Video Creator Online</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Multimodal Models`, `#Video Generation`, `#AI Tools`, `#LLM`

---

<a id="item-8"></a>
## [ChatGPT 广告试水年化收入破亿美元](https://www.ithome.com/0/933/157.htm) ⭐️ 8.0/10

OpenAI 在美国推出的 ChatGPT 广告试点项目上线六周内实现年化收入超 1 亿美元，并吸引了 600 多家广告主，主要面向免费用户和低价 Go 订阅用户。 此举标志着 OpenAI 商业模式的关键转变，表明广告可在不损害用户信任的前提下成为 AI 平台的重要收入来源，可能重塑生成式 AI 产品的全球商业化路径。 目前每日仅向约 20%的符合条件用户展示广告（85%的美国用户具备资格），广告与 ChatGPT 回答内容相互独立，且不会将用户对话数据分享给广告主；低关闭率和不断提升的相关性显示初步成效良好。

rss · IT HOME · Mar 27, 02:01

**背景**: ChatGPT 是由 OpenAI 开发的全球广泛使用的 AI 聊天机器人，提供免费和付费版本。随着 AI 研发成本激增，OpenAI 等公司正寻求订阅之外的可持续收入模式。在 AI 界面中引入广告对用户体验、数据隐私和内容完整性提出了特殊挑战。

**标签**: `#AI Monetization`, `#ChatGPT`, `#Advertising`, `#OpenAI`, `#Business Strategy`

---

<a id="item-9"></a>
## [Anvil 支持并行运行多个 Claude 实例](https://www.producthunt.com/products/anvil-5) ⭐️ 8.0/10

Anvil 是一款新型开发者工具，允许用户并行运行 Anthropic 的 Claude AI 模型的多个实例，显著提升编码和自动化任务的工作流可扩展性。 该功能通过支持并发执行，解决了在复杂多步骤任务中使用大语言模型的关键瓶颈，对构建 AI 智能体团队或实现大规模工作流自动化的开发者和研究人员至关重要。 Anvil 似乎专注于编排“一支 Claude 实例舰队”，可能通过基于浏览器的智能体或 API 协调实现，社区案例显示其应用于网页自动化和协作代码生成等场景。

producthunt · Zachary Denham · Mar 26, 06:59

**背景**: Claude 是 Anthropic 开发的领先大语言模型（LLM），以强大的推理和编程能力著称。并行运行多个实例（常被称为“智能体团队”）可将复杂问题分解为多个子任务同时处理，从而提升效率并降低延迟。这种方法在 AI 研究与开发中日益普及，用于软件编译、数据抓取和自动化测试等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fazm.ai/blog/claude-code-parallel-instances-ctrl-c-muscle-memory">Running 5 Claude Code Instances in Parallel ... - Fazm Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/parallel-browser-agents-claude-code">Parallel Browser Agents: How to Run Multiple Claude Code Instances ...</a></li>
<li><a href="https://www.anthropic.com/engineering/building-c-compiler">Building a C compiler with a team of parallel Claudes \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 开发者分享了使用多个 Claude Code 实例执行表单填写和构建编译器等任务的经验，既肯定其强大能力，也指出操作挑战，例如进程管理和不一致的用户体验反馈。

**标签**: `#AI`, `#LLM`, `#Claude`, `#Developer Tools`, `#Parallel Computing`

---

<a id="item-10"></a>
## [AI 一天内用 Go 重写 JSONata](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

Reco 团队使用大语言模型（LLM）在不到一天的时间内将 JSONata 表达式语言从 JavaScript 重写为 Go，通过原始测试套件和为期一周的影子部署验证了行为完全一致。 这展示了“氛围移植”（vibe porting）在现实中的高影响力应用——利用 AI 以极少人力迁移关键软件，预计每年节省 50 万美元，并实现更快、更易维护的基础设施。 该项目仅花费 400 美元的 LLM token 费用，7 小时内就产出可运行版本；其正确性由 JSONata 原有的完整测试套件保障，并通过与原始实现并行运行的影子部署进一步验证。

rss · Simon Willison · Mar 27, 00:35

**背景**: JSONata 是一种轻量级开源的 JSON 数据查询与转换语言，功能类似 jq 但表达能力更强，广泛用于 Node-RED 等数据集成工具中。“氛围移植”（vibe porting）指利用 AI 根据示例、测试和对话式提示，在新语言或框架中复现软件行为，而非依赖正式规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata</a></li>
<li><a href="https://devopstales.github.io/ai/ai-software-development-spec-vs-vibe/">AI Software Development: Spec-Driven vs. Vibe Coding</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Software Engineering`, `#Go`, `#JSONata`

---

<a id="item-11"></a>
## [知行机器人完成近亿元融资，发力灵巧手研发](https://36kr.com/p/3740523277517063?f=rss) ⭐️ 7.0/10

中国机器人公司知行机器人连续完成 B+轮和 B++轮融资，累计融资近亿元人民币，用于推进其全栈式灵巧手技术和具身智能解决方案。公司已推出两款新产品：面向工业物流场景的四指“灵思手”和采用绳驱动、支持左右手自适应数据采集的五指“束巧手”。 高性能灵巧手是具身智能落地的关键硬件，使机器人能在工业和高端服务场景中可靠地与物理世界交互。知行机器人在高可靠性、高性价比设计以及高效数据采集方面的突破，有望推动通用操作能力在中国快速增长的机器人生态中实现规模化应用。 “灵思手”拥有 12 个关节、8 个主动自由度，负载 5kg，采用驱控一体化设计，便于集成到协作机械臂；“束巧手”采用仿生绳驱动结构，具备 16 个关节和 11 个主动自由度，单只手可同时采集左右手操作数据，使数据采集成本降低一半。两款产品均基于公司自研的欠驱动、可重构及柔性自适应机构，其用于数据采集的灵巧手寿命超 500 万次，达行业平均水平的百倍以上。

rss · 36kr · Mar 27, 01:37

**背景**: 具身智能（Embodied Intelligence）指通过物理身体与环境动态交互来实现学习和决策的智能系统，强调感知、行动与认知的深度融合。灵巧手是模仿人手结构与功能的机器人末端执行器，对完成复杂操作任务至关重要，也是机器人领域技术难度最高的部件之一，需在有限空间内兼顾自由度、驱动力、精度和可靠性。绳驱动和欠驱动是当前主流技术路线，旨在平衡灵巧性、成本与工程可行性，尤其在物流、制造和医疗等场景加速落地的背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/具身智能/63286570">具身智能（智能体通过身体将感知、行动与认知深度融合的智能系统）_...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/678744015">机器人灵巧手行业深度：市场现状、未来发展方向、核心部位及相关企业... 灵巧手（人形机器人末端执行器）_百度百科 Images 灵巧手技术全景解析（一）：从三大核心到应用场景的完整指南 - 艾邦机... 百亿独角兽，为人形机器人放「手」一搏-36氪 Top Stories 机器人着力展示“打工”技能 灵巧手厂商关注度提升｜2026中关村论坛年会... 机器人灵巧手：技术演进、市场格局与未来前景 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位</a></li>
<li><a href="https://baike.baidu.com/item/灵巧手/67387238">灵巧手（人形机器人末端执行器）_百度百科</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#Hardware`, `#Dexterous Manipulation`, `#AI Infrastructure`

---

<a id="item-12"></a>
## [谷歌在 Android 17 引入后量子加密](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) ⭐️ 7.0/10

谷歌在 Android 17 中引入了后量子加密（PQC），在引导加载程序中加入抗量子数字签名，并将密钥库系统升级至符合 PQC 标准的体系。 此举为 Android 安全体系提前防御未来量子计算威胁，防止现有公钥加密被破解，保障设备启动链和通信安全，对移动端 AI 应用及敏感数据保护至关重要。 该实现覆盖 Verified Boot 启动链和密钥库，采用 NIST 标准化或候选的 PQC 算法，在 2030 年强制要求前率先部署，旨在保护设备启动时的完整性及运行时的加密操作。

telegram · zaihuapd · Mar 26, 07:09

**背景**: 后量子加密（PQC）指能抵御量子计算机攻击的新一代加密算法。当前广泛使用的 RSA 和 ECC 等公钥密码体系可能被量子计算机上的 Shor 算法破解。美国国家标准与技术研究院（NIST）自 2016 年起推动 PQC 标准化，预计将在本十年内完成最终标准。谷歌等科技公司正积极部署 PQC，以防范“现在窃取、未来解密”的长期安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/security/resources/post-quantum-cryptography?hl=zh-CN">后量子加密 (PQC) | Google Cloud</a></li>
<li><a href="https://winbuzzer.com/2026/03/26/google-android-17-quantum-resistant-encryption-pqc-xcxwbn/">Android 17 Gets Quantum-Safe Encryption Across Full Security ...</a></li>
<li><a href="https://www.secrss.com/articles/79273">MITRE后量子密码学 (PQC) 迁移路线图深度解读 - 安全内参 | 决策者的...</a></li>

</ul>
</details>

**标签**: `#Post-Quantum Cryptography`, `#Android`, `#Security`, `#Quantum Computing`, `#Mobile OS`

---

<a id="item-13"></a>
## [中科院发布开源“香山”RISC-V 处理器与“如意”操作系统](https://h.xinhuaxmt.com/vh512/share/13024070?docid=13024070) ⭐️ 7.0/10

中国科学院发布了开源高性能 RISC-V 处理器“香山”和原生操作系统“如意”，并联合阿里、腾讯、字节跳动等数十家科技企业启动下一代芯片与操作系统的协同研发。 此举通过构建基于 RISC-V 的开源软硬件生态，强化了中国自主可控的计算基础设施，有助于支撑 AI 等高性能计算需求，并降低对 x86 和 ARM 等国外架构的依赖。多家头部科技企业的参与预示着该平台有望成为未来 AI 基础设施的重要选项。 “香山”处理器性能达国际先进水平，并集成了全球首个开源片上互连网络 IP；“如意”操作系统全面支持国际标准。进迭时空、奕斯伟等企业已推出基于“香山”的商用芯片并实现规模化落地。

telegram · zaihuapd · Mar 26, 10:08

**背景**: RISC-V 是一种开源指令集架构（ISA），允许任何人自由设计、制造和销售芯片及配套软件，无需支付授权费。与 x86（英特尔/AMD）或 ARM 等专有架构不同，RISC-V 支持高度定制化，特别适用于 AI 加速器、边缘计算和国家自主可控计算体系。中科院计算所于 2020 年启动“香山”项目，目标是打造一款性能可与商业处理器竞争的开源高性能 RISC-V CPU 核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://github.com/OpenXiangShan/XiangShan">GitHub - OpenXiangShan/XiangShan: Open-source high-performance RISC-V processor · GitHub</a></li>
<li><a href="https://openxiangshan.github.io/">XiangShan: An Open Source High Performance RISC-V Processor and Infrastructure for Architecture Research</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#Open Source Hardware`, `#Operating Systems`, `#Semiconductors`, `#AI Infrastructure`

---