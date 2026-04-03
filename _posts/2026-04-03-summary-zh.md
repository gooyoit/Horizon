---
layout: default
title: "Horizon Summary: 2026-04-03 (ZH)"
date: 2026-04-03
lang: zh
---

> From 90 items, 27 important content pieces were selected

---

1. [谷歌 DeepMind 发布开源 Gemma 4 人工智能模型](#item-1) ⭐️ 10.0/10
2. [谷歌发布 Gemma 4 开放模型，覆盖手机到工作站](#item-2) ⭐️ 10.0/10
3. [谷歌 DeepMind 发布 Gemma 4 视觉大语言模型](#item-3) ⭐️ 9.0/10
4. [llm-gemini 0.30 新增对 Gemini 3.1 和 Gemma 4 模型的支持](#item-4) ⭐️ 9.0/10
5. [通义千问 Qwen 3.6-Plus 登 Code Arena 全球第二](#item-5) ⭐️ 9.0/10
6. [阿里发布千问新一代多模态大模型 Qwen3.6-Plus](#item-6) ⭐️ 9.0/10
7. [微软发布三款自研 AI 模型，覆盖语音与图像任务](#item-7) ⭐️ 9.0/10
8. [GLM-5V-Turbo：面向 GUI 自动化的视觉到代码模型](#item-8) ⭐️ 9.0/10
9. [开发者比较 Cursor 3 与 Claude Code 的 AI 编码能力](#item-9) ⭐️ 8.0/10
10. [通义千问推出专注智能体能力的托管模型 Qwen3.6-Plus](#item-10) ⭐️ 8.0/10
11. [AMD 推出 Lemonade：开源多模态本地大语言模型服务器](#item-11) ⭐️ 8.0/10
12. [西蒙·威利森谈 AI 拐点与智能体系统](#item-12) ⭐️ 8.0/10
13. [西蒙·威利森 2026 年 3 月 AI 通讯聚焦智能体模式与混合专家模型进展](#item-13) ⭐️ 8.0/10
14. [叽伴：用「共同经历」重新定义 AI 社交](#item-14) ⭐️ 8.0/10
15. [量旋科技完成 6 亿元 C+轮融资](#item-15) ⭐️ 8.0/10
16. [开发者打造跨平台 AI 超级管家 Wanny](#item-16) ⭐️ 8.0/10
17. [西湖大学团队构建全球最大人类泛基因组，发现 13%未知序列](#item-17) ⭐️ 8.0/10
18. [广汽本田 P7 推送 OTA 升级，新增 AI 大模型与声音复刻功能](#item-18) ⭐️ 8.0/10
19. [FuriosaAI 计划 2024 年量产 2 万颗 RNGD AI 芯片](#item-19) ⭐️ 8.0/10
20. [2025 年英伟达在中国 AI 芯片份额降至 55%](#item-20) ⭐️ 8.0/10
21. [近半数美国大学生因 AI 考虑更换专业](#item-21) ⭐️ 8.0/10
22. [Cushion 推出开源 AI 笔记应用](#item-22) ⭐️ 8.0/10
23. [前 Azure 工程师指责内部决策损害信任](#item-23) ⭐️ 7.0/10
24. [用户组织共享 Google AI Ultra 订阅](#item-24) ⭐️ 7.0/10
25. [AI 技能自动化处理 Harness 工程](#item-25) ⭐️ 7.0/10
26. [荣耀与京东达成三年战略合作，目标销售额超千亿元](#item-26) ⭐️ 7.0/10
27. [Windows 11 任务管理器新增详细 NPU 监控功能](#item-27) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌 DeepMind 发布开源 Gemma 4 人工智能模型](https://deepmind.google/models/gemma/gemma-4/) ⭐️ 10.0/10

谷歌 DeepMind 发布了 Gemma 4 系列开源 AI 模型，支持推理、多模态理解（文本和图像）以及工具调用。该系列包含 2B、4B、26B-A4B、E4B 和 31B 等多个版本，已在 Hugging Face 上提供 BF16 精度模型，并将为 NVIDIA Blackwell GPU 推出量化版本。 Gemma 4 将前沿的多模态和智能体能力带给开源社区，使开发者能够构建先进的端侧和边缘 AI 应用。其出色的基准表现和较低的幻觉率使其成为同类闭源模型的有力竞争者。 这些模型使用'<turn|>'作为序列结束符，'<|channel>thought\n'用于推理轨迹；推荐推理参数为 temperature=1.0、top_p=0.95、top_k=64。较小的模型（2B/4B）在多模态输出质量上有限，但 26B-A4B 版本在消费级硬件上表现出色，而 31B 模型在本地运行时可能失效，需通过 Google AI Studio API 调用才有效。

hackernews · jeffmcjunkin · Apr 2, 16:10

**背景**: Gemma 是谷歌 DeepMind 推出的轻量级开源语言模型系列，旨在支持负责任的 AI 开发并实现端侧部署。此前的 Gemma 1 和 2 仅支持纯文本，而 Gemma 4 首次引入多模态输入（文本+图像）和工具调用功能。工具调用使模型能与外部 API 或软件工具交互，是实现超越简单文本生成的智能体 AI 系统的关键特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://huggingface.co/blog/gemma4">Welcome Gemma 4 : Frontier multimodal intelligence on device</a></li>
<li><a href="https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/">Bringing AI Closer to the Edge and On-Device with Gemma 4 | NVIDIA...</a></li>

</ul>
</details>

**社区讨论**: 社区用户反馈 Gemma 4 在实际应用中表现优异，尤其是 26B-A4B 模型幻觉较少，但 31B 版本存在本地推理问题。用户分享了量化模型和使用指南，强调应重视实际测试而非过度关注基准分数。还有人指出该模型能处理如 Toki Pona 语言翻译等小众任务，显示出良好的上下文记忆能力。

**标签**: `#AI models`, `#Gemma 4`, `#Google DeepMind`, `#open-source AI`, `#frontier technology`

---

<a id="item-2"></a>
## [谷歌发布 Gemma 4 开放模型，覆盖手机到工作站](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) ⭐️ 10.0/10

谷歌发布了 Gemma 4 开放模型家族，包含 E2B、E4B、26B MoE 和 31B Dense 四种规格，适用于从手机、笔记本电脑到工作站和加速器的多种设备。这些模型支持多模态输入（E2B 和 E4B 原生支持音频）、高级推理、智能体工作流、函数调用、结构化 JSON 输出、代码生成，并提供最高达 256K 的上下文窗口。 Gemma 4 在宽松的 Apache 2.0 许可证下提供高性能开放模型，极大提升了开发者在消费级设备上离线构建和部署先进 AI 应用的能力。其在开源模型榜单中的优异排名和多模态能力，使其成为开源前沿模型生态中的重要竞争者。 E2B 和 E4B 采用混合专家（MoE）架构，专为端侧离线推理优化，支持 128K 上下文；31B 稠密模型在 Arena AI 开源模型榜单中排名第 3，26B MoE 模型排名第 6。所有模型均以 Apache 2.0 许可证发布，允许免费商用。

telegram · zaihuapd · Apr 2, 16:12

**背景**: Gemma 是谷歌面向开发者和研究人员推出的轻量级开放权重语言模型系列。此前版本主要聚焦文本处理，而 Gemma 4 实现了重大突破，新增对图像、视频和音频等多模态输入的支持，并具备复杂的智能体工作流能力。Apache 2.0 许可证在 AI 领域具有重要意义，因其允许免费商用、修改和分发，比某些竞争对手使用的限制性许可证更为宽松。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Gemma 4: Byte for byte, the most capable open models</a></li>
<li><a href="https://huggingface.co/google/gemma-4-E2B">google/gemma-4-E2B · Hugging Face</a></li>
<li><a href="https://www.qbitai.com/2025/08/319141.html">刚刚，OpenAI开源2个推理 模 型 ：笔记本/手机就能跑，性能接近o4-mini</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Gemma`, `#Google`, `#Open-Source AI`, `#Multimodal AI`

---

<a id="item-3"></a>
## [谷歌 DeepMind 发布 Gemma 4 视觉大语言模型](https://simonwillison.net/2026/Apr/2/gemma-4/#atom-everything) ⭐️ 9.0/10

谷歌 DeepMind 发布了 Gemma 4，这是一套四个新开源、具备视觉推理能力的大语言模型（2B、4B、31B 和 26B-A4B 混合专家模型），采用每层嵌入（Per-Layer Embeddings）技术提升参数效率，并原生支持图像、视频和音频输入。 Gemma 4 在构建高性能且紧凑的 AI 模型方面取得重要进展，使先进的多模态推理能力可在本地设备上运行，推动高效 AI 部署的发展。其 Apache 2.0 许可证也促进了开源社区的广泛采用与创新。 较小的 E2B 和 E4B 模型采用每层嵌入（PLE）技术，为每个解码器层存储大型但稀疏访问的嵌入表，从而在推理时实现更低的“有效”参数量。所有模型均支持可变分辨率的视觉任务（如 OCR 和图表理解），而 E2B/E4B 还支持原生音频输入用于语音识别。

rss · Simon Willison · Apr 2, 18:28

**背景**: 大语言模型（LLM）正越来越多地整合多模态能力，以处理文本、图像、音频和视频。混合专家（MoE）等参数高效架构以及每层嵌入（PLE）等新技术旨在降低计算成本的同时保持性能。“有效参数量”指能提供相似性能的等效稠密模型的参数规模，用以衡量效率提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/introducing-gemma-3n-developer-guide/">Introducing Gemma 3n: The developer guide - Google Developers Blog</a></li>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B">google/gemma-4-26B- A 4 B · Hugging Face</a></li>
<li><a href="https://thegrigorian.medium.com/the-densing-law-of-large-language-models-99da152e8050">The Densing Law of Large Language Models ... | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Gemma`, `#Google DeepMind`, `#open-source`

---

<a id="item-4"></a>
## [llm-gemini 0.30 新增对 Gemini 3.1 和 Gemma 4 模型的支持](https://simonwillison.net/2026/Apr/2/llm-gemini/#atom-everything) ⭐️ 9.0/10

llm-gemini 插件 0.30 版本现已支持新的 Google AI 模型：gemini-3.1-flash-lite-preview、gemma-4-26b-a4b-it 和 gemma-4-31b-it。此次更新使开发者能够通过开源 LLM 框架调用这些前沿模型。 该版本极大地扩展了使用开源工具的开发者可访问的先进 AI 能力，尤其适用于高效率推理和企业级开源模型。它将 Google 最新的专有与开源模型与更广泛的 LLM 生态系统连接起来。 gemini-3.1-flash-lite-preview 针对高吞吐量场景优化，性能优于前代；Gemma 4 变体（26B 和 31B 参数）采用 Apache 2.0 许可证，支持 128K–256K 上下文长度，并包含指令微调版本。所有模型均于 2026 年 4 月初发布。

rss · Simon Willison · Apr 2, 18:25

**背景**: llm-gemini 插件是一个开源扩展，用于 LLM 命令行工具，允许用户调用 Google 的 Gemini 系列模型。Google 的 Gemma 系列是从 Gemini 相同研究中衍生出的轻量级、开放权重语言模型，旨在实现负责任的部署。最新的 Gemma 4 模型在规模和能力上相比早期版本有显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://www.digitalapplied.com/blog/google-gemma-4-apache-2-open-source-complete-guide">Google Gemma 4: Apache 2.0 Open-Source Complete Guide</a></li>
<li><a href="https://openrouter-web.vercel.app/google/gemini-3.1-flash-lite-preview">Gemini 3 . 1 Flash Lite Preview - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Gemini`, `#Gemma`, `#open-source`

---

<a id="item-5"></a>
## [通义千问 Qwen 3.6-Plus 登 Code Arena 全球第二](https://36kr.com/newsflashes/3750451260474121?f=rss) ⭐️ 9.0/10

4 月 3 日，LMArena 旗下的盲测编程榜单 Code Arena 发布最新排名，阿里巴巴大模型 Qwen 3.6-Plus 位列全球第二，是中国大模型中排名最高的。 这一成绩彰显了中国在前沿人工智能领域的竞争力，证明 Qwen 在编程能力上已比肩 GPT-4 等国际顶尖模型。同时凸显了 LMArena 等独立盲测基准在大模型竞争日益激烈背景下的关键作用。 评测通过 Code Arena 进行，该平台采用众包式盲测机制，用户在不知模型身份的情况下进行横向比较。Qwen 3.6-Plus 是阿里通义千问系列的最新版本，专为代码生成与推理任务优化。

rss · 36kr · Apr 3, 01:56

**背景**: LMArena 起源于 2023 年加州大学伯克利分校的 Chatbot Arena 项目，现已发展为业内权威的大模型盲测平台，常被比作 AI 界的“可乐盲测”。Code Arena 专注于长代码任务，通过真实编程挑战评估模型能力，而非依赖合成数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.felicis.com/insight/lmarena-announcement">LMArena : Benchmarking and Advancing The Progress of All... | Felicis</a></li>
<li><a href="https://arena.ai/code">Code Arena : Build & Test with AI Coding Models</a></li>
<li><a href="https://www.linkedin.com/posts/jasoncalacanis_ai-startups-llms-activity-7319111708461985793-0zqk">LM Arena : a blind leaderboard for LLMs | Jason Calacanis... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Qwen`, `#Code Benchmarking`, `#Frontier Tech`

---

<a id="item-6"></a>
## [阿里发布千问新一代多模态大模型 Qwen3.6-Plus](https://t.me/zaihuapd/40658) ⭐️ 9.0/10

阿里巴巴发布了新一代多模态大语言模型 Qwen3.6-Plus，具备更强的编程能力和自主任务执行能力。该模型在 SWE-bench 和 Claw-Eval 等权威评测中展现出接近顶尖水平的表现。 此次发布标志着智能体 AI 和真实场景代码生成的重大进展，有望大幅提升开发者效率并推动自主 AI 系统的发展。其在多项评测中逼近 Claude 等顶尖模型，凸显了中国在基础大模型领域的竞争力。 Qwen3.6-Plus 具备原生多模态理解与推理能力，可自主拆解、规划、测试并完成前端网页开发等复杂编码任务。它支持“氛围编程”，即通过自然语言指令直接生成可用代码。

telegram · zaihuapd · Apr 2, 05:02

**背景**: 多模态大语言模型（MLLM）在传统大语言模型基础上扩展了对文本、图像和结构化代码等多种数据类型的理解能力，从而实现更复杂的推理。SWE-bench 基准使用真实的 GitHub 问题评估模型自主修复漏洞和完成功能的能力。Claw-Eval 则通过 100 多个真实世界任务评估 AI 智能体的实际行动能力，超越了传统合成基准的局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swebench.com/">SWE - bench Leaderboards</a></li>
<li><a href="https://github.com/SWE-bench/SWE-bench">GitHub - SWE - bench / SWE - bench : SWE - bench : Can Language...</a></li>
<li><a href="https://x.com/_TobiasLee/status/2032129181673570479">Claw-Eval Update: 7 more models on the leaderboard! Now featuring ... - X</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Model`, `#Multimodal AI`, `#Autonomous Agents`, `#Qwen`

---

<a id="item-7"></a>
## [微软发布三款自研 AI 模型，覆盖语音与图像任务](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) ⭐️ 9.0/10

微软于 4 月 2 日发布了三款全新自研 AI 模型：用于语音转文本的 MAI-Transcribe-1、文本转语音的 MAI-Voice-1 和图像生成的 MAI-Image-2。这些模型现已通过 Microsoft Foundry 和新的 MAI Playground 上线。 这些模型增强了微软在核心生成式 AI 能力上对 OpenAI 和谷歌的竞争优势，使其能在 Copilot、Bing 和 PowerPoint 等生态中提供更快、更准确且可定制的企业级 AI 服务。其性能基准表明，多语言转录、语音合成速度和逼真图像生成方面取得了显著进步。 MAI-Transcribe-1 在 FLEURS 基准测试的 25 种语言上平均词错误率为 3.8%，全面优于 Whisper-large-v3；MAI-Voice-1 可在 1 秒内生成 60 秒自然语音，并支持仅用数秒音频定制声音；MAI-Image-2 的生成速度至少比前代快 2 倍，在逼真度和图像中文本渲染方面也有提升。

telegram · zaihuapd · Apr 2, 11:31

**背景**: 微软正大力投资自研基础模型，以减少对 OpenAI 等第三方 AI 提供商的依赖。MAI（Microsoft AI）系列体现了其在生产力、云服务和消费产品中垂直整合 AI 能力的战略。语音转文本、文本转语音和图像生成是多模态 AI 系统和企业应用（如客服自动化、内容创作和无障碍工具）的基础能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-mai-transcribe-1-mai-voice-1-and-mai-image-2-in-microsoft-foundry/4507787">Introducing MAI - Transcribe - 1 , MAI-Voice-1, and MAI-Image-2 in...</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-voices">What is MAI-Voice? - Foundry Tools | Microsoft Learn</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-image-2/">Introducing MAI-Image-2: for limitless creativity | Microsoft AI</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Generative AI`, `#Microsoft`, `#Speech Recognition`, `#Image Generation`

---

<a id="item-8"></a>
## [GLM-5V-Turbo：面向 GUI 自动化的视觉到代码模型](https://www.producthunt.com/products/z-ai) ⭐️ 9.0/10

Z.AI 发布了其首个原生多模态编码基础模型 GLM-5V-Turbo，专为基于视觉的 GUI 自动化任务设计。该模型能够处理图像、视频和文本，生成可执行代码并执行长周期规划。 该模型连接了视觉理解和代码生成，使得图形用户界面的自动化更加直观和可扩展，无需手动编写脚本。这标志着通用人工智能代理向人类一样与软件交互迈出了重要一步。 GLM-5V-Turbo 在复杂编码、动作执行以及对截图或录屏等视觉输入的多模态推理方面表现出色。它针对真实世界的 GUI 自动化场景进行了优化，而非依赖合成或简化的基准测试。

producthunt · Zac Zuo · Apr 2, 03:17

**背景**: 视觉到代码模型旨在将用户界面的视觉表示转换为功能性源代码。多模态 AI 的最新进展——结合计算机视觉和语言建模——使系统能够解读屏幕并生成相应的操作或代码。这延续了如 Google 的 Codey（文本到代码模型）等趋势，但将其扩展到了视觉输入领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/GLM-5V-Turbo">GLM-5V-Turbo</a></li>
<li><a href="https://docs.z.ai/guides/vlm/glm-5v-turbo?ref=producthunt">GLM - 5 V - Turbo - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.emergentmind.com/topics/modular-multi-agent-vision-to-code-frameworks">Modular Multi-Agent Vision - to - Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#foundation model`, `#vision-to-code`, `#GUI automation`, `#multimodal AI`

---

<a id="item-9"></a>
## [开发者比较 Cursor 3 与 Claude Code 的 AI 编码能力](https://cursor.com/blog/cursor-3) ⭐️ 8.0/10

搭载全新 Composer 2 AI 模型的 Cursor 3 正被开发者在实际编码工作流中与 Anthropic 的 Claude Code 进行对比。用户强调了两者在实用性、成本和感知智能方面的差异。 随着 AI 编码助手日益成为开发者生产力的核心，选择 Cursor 3 或 Claude Code 等工具将影响工作流效率、成本和代码质量。这一对比反映了软件工程中应用 AI 的更广泛趋势。 Cursor 3 将 Composer 2 作为默认模型，用户认为其智能程度虽不及 OpenAI 或 Anthropic 的旗舰模型，但在日常编码中更实用。一些开发者将 Claude Code 与 Cursor 免费版结合用于自动补全，质疑其付费版的价值。

hackernews · adamfeldman · Apr 2, 18:13

**背景**: Cursor 是一个由 AI 驱动的集成开发环境（IDE），支持多种大语言模型，提供代码补全、聊天辅助和仓库感知编辑等功能。Claude Code 是 Anthropic 推出的专用 AI 编码助手，可通过桌面应用和 API 使用，旨在利用上下文感知处理复杂的编程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/">Cursor : The best way to code with AI</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://learn-cursor.com/en/docs">Cursor AI User Guide | Learn Cursor</a></li>

</ul>
</details>

**社区讨论**: 开发者观点不一：有人偏好 Cursor 3 的实用性及 Composer 2 集成，也有人认为 Claude Code 更具性价比或更强大。担忧包括 Cursor 的定价过高、过度依赖聊天界面，以及相比独立 AI 工具的独特价值正在减弱。

**标签**: `#AI coding assistant`, `#Cursor IDE`, `#Claude Code`, `#developer tools`, `#applied AI`

---

<a id="item-10"></a>
## [通义千问推出专注智能体能力的托管模型 Qwen3.6-Plus](https://qwen.ai/blog?id=qwen3.6) ⭐️ 8.0/10

阿里巴巴通义千问团队发布了 Qwen3.6-Plus，这是一款强调现实世界智能体能力（如编程和多模态推理）的托管大语言模型，标志着其从此前开源权重模型的战略转变。 此次发布表明阿里巴巴意图在实际智能体任务中直接与 Claude Opus 和 Gemini Pro 等顶级闭源模型竞争，同时也引发了业界对其透明度和基准测试做法的质疑，尤其是在 AI 技术快速迭代的背景下。 Qwen3.6-Plus 采用线性注意力与稀疏混合专家（MoE）路由相结合的混合架构，支持高达 100 万上下文长度，目前可通过阿里云和 OpenRouter 的 API 使用，但该模型并非开源权重，且未公布参数量。

hackernews · pretext · Apr 2, 14:28

**背景**: 开源权重（open-weight）模型（如早期的 Qwen 版本）会公开其训练好的参数，允许用户下载并在本地运行。而托管模型（或称闭源模型）仅能通过 API 访问，限制了用户的控制权和透明度。通义千问系列此前以强大的开源权重模型著称，因此此次转向专有、聚焦智能体能力的模型尤为引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6">Qwen3.6-Plus: Towards Real World Agents</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.6-plus:free/api">Qwen: Qwen3.6 Plus (free) – API Quickstart | OpenRouter</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/qwen-3-6-plus-preview-review">Qwen 3.6 Plus Preview: 1M Context, Speed & Benchmarks 2026</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些用户对放弃开源权重策略表示不满，并质疑为何选择与 Claude Opus 4.5 而非更新的 4.6 版本进行对比；另一些人则认为，在模型快速迭代的背景下，这种对比是合理的，相关批评有些过度。

**标签**: `#AI models`, `#Qwen`, `#large language models`, `#AI research`, `#frontier tech`

---

<a id="item-11"></a>
## [AMD 推出 Lemonade：开源多模态本地大语言模型服务器](https://lemonade-server.ai/) ⭐️ 8.0/10

AMD 发布了 Lemonade，这是一个开源的本地大语言模型服务器，支持在 AMD GPU、NPU 和 CPU 上进行多模态推理，包括文本、图像和音频。它提供了一个统一的运行时环境，可通过 ROCm、Vulkan 和 CPU 等多种后端实现硬件加速的本地大模型运行。 Lemonade 降低了在 AMD 硬件上本地运行先进多模态 AI 模型的门槛，解决了驱动兼容性和工具碎片化等长期难题。这有望推动消费者级 AMD 系统上的本地 AI 应用普及，并促进更易访问、注重隐私的 AI 生态发展。 尽管 Lemonade 支持 NPU 加速，但社区测试表明，Ryzen AI NPU 在运行较大模型时性能目前不如独立 GPU。此外，Lemonade 使用的部分 NPU 专用内核是专有的，并未开源，限制了透明度和社区驱动的优化。

hackernews · AbuAssar · Apr 2, 11:04

**背景**: 本地大语言模型服务器允许用户在自有硬件上运行大模型，而非依赖云端 API，从而提升隐私性并降低延迟。NPU（神经网络处理单元）是专为高效处理机器学习任务而设计的 AI 加速器，常见于 AMD Ryzen AI 系列等现代处理器中。AMD 的 ROCm 是一个用于 GPU 计算的开源软件栈，类似于 NVIDIA 的 CUDA，但在 AI 推理方面历史积累较弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_processing_unit">Neural processing unit - Wikipedia</a></li>
<li><a href="https://www.comet.com/site/blog/build-local-llm-server/">Building a Low-Cost Local LLM Server to Run 70 Billion Parameter Models</a></li>
<li><a href="https://blog.n8n.io/local-llm/">How to Run a Local LLM: Complete Guide to Setup & Best Models (2025) – n8n Blog</a></li>

</ul>
</details>

**社区讨论**: 用户称赞 Lemonade 快速的开发节奏和广泛的硬件支持，尤其是在 AMD Strix Halo 系统上。但也有人质疑 Ryzen AI NPU 相比独立 GPU 的实际性能，并指出关键的 NPU 组件仍是闭源的。还有人将其与 Ollama 和 LM Studio 对比，但强调其在统一多模态编排方面的雄心。

**标签**: `#AI`, `#LLM`, `#open-source`, `#AMD`, `#local-inference`

---

<a id="item-12"></a>
## [西蒙·威利森谈 AI 拐点与智能体系统](https://simonwillison.net/2026/Apr/2/lennys-podcast/#atom-everything) ⭐️ 8.0/10

西蒙·威利森做客 Lenny 播客，讨论了 2025 年 11 月 AI 发展的拐点——GPT-5.1 和 Claude Opus 4.5 等模型在代码生成可靠性上实现质的飞跃，推动了更自主的智能体工作流和“黑灯工厂”等自动化趋势。 这标志着 AI 从编码助手向能以极少监督执行复杂任务的自主智能体转变，可能重塑软件开发、制造业及各行业的知识工作模式。 威利森指出，软件开发的瓶颈已从编写代码转向测试，而当前的编码智能体已在安全研究中展现价值。他还提醒，人们常误以为 AI 工具易于使用，实际上负责任地运用它们需要相当的专业知识。

rss · Simon Willison · Apr 2, 20:40

**背景**: 智能体 AI（Agentic AI）指能在复杂环境中自主行动、无需人类持续干预即可决策并执行多步骤任务的系统。“黑灯工厂”（或熄灯制造）指完全自动化的生产设施，无需现场人工操作。所谓“2025 年 11 月拐点”是指 AI 模型（尤其在代码理解和生成方面）性能出现显著跃升，使系统行为更加可靠和自主。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dark_factories">Dark factories</a></li>

</ul>
</details>

**标签**: `#AI`, `#agentic AI`, `#automation`, `#frontier tech`, `#AI policy`

---

<a id="item-13"></a>
## [西蒙·威利森 2026 年 3 月 AI 通讯聚焦智能体模式与混合专家模型进展](https://simonwillison.net/2026/Apr/2/march-newsletter/#atom-everything) ⭐️ 8.0/10

西蒙·威利森发布了 2026 年 3 月仅限赞助者的通讯，内容涵盖智能体工程模式、在 Mac 上流式运行混合专家（MoE）模型、3 月新模型发布、氛围移植（vibe porting），以及 PyPI 和 NPM 的供应链攻击风险。其中特别提到通过 SSD 流式加载权重，在消费级 Mac 上成功运行如 Kimi K2.5 这类万亿参数 MoE 模型的实际案例。 这些主题反映了前沿 AI 在实际部署中的最新进展，尤其是资源受限的开发者如何通过专家流式加载和智能体工作流等技术利用尖端模型。这有助于推动大规模 AI 的普及，并为快速发展的生态系统提供安全高效的工程实践指导。 通讯中描述了 Dan Woods 等人通过为每个 token 从 SSD 流式加载专家权重，在仅 48–96GB 内存的设备上运行 Qwen3.5-397B-A17B 和 Kimi K2.5 等巨型 MoE 模型的实验。同时将“氛围移植”与借助 AI 快速重写 JSONata 等系统联系起来，其可行性依赖于完善的测试套件。

rss · Simon Willison · Apr 2, 05:15

**背景**: 智能体工程模式指与 AI 编程智能体交互的结构化方法，旨在提升输出质量和可靠性。混合专家（MoE）是一种神经网络架构，针对不同输入激活不同的参数子集（“专家”），从而在可控计算成本下构建大模型。专家流式加载指在推理过程中仅从磁盘加载当前活跃的专家权重，以运行超出内存容量的模型。“氛围移植”则是利用 AI 基于现有系统的测试和文档复现其行为，而非从头重写。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Mar/24/streaming-experts/">Streaming experts</a></li>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/">Agentic Engineering Patterns - Simon Willison's Weblog</a></li>
<li><a href="https://simonwillison.net/tags/vibe-porting/">Simon Willison on vibe-porting</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mixture-of-Experts`, `#agentic AI`, `#model releases`, `#frontier tech`

---

<a id="item-14"></a>
## [叽伴：用「共同经历」重新定义 AI 社交](https://36kr.com/p/3749816005657093?f=rss) ⭐️ 8.0/10

AI 社交应用「叽伴」已开启公测，提出一种全新虚拟陪伴模式：用户与 AI 伙伴通过动态、用户自创的虚拟世界共同经历事件，建立基于记忆的持久关系。与传统聊天式 AI 伴侣不同，叽伴强调共同探索、共享选择和跨世界记忆留存。 叽伴直击当前 AI 陪伴产品的核心痛点——记忆缺失、角色性格漂移（OOC）和用户留存率低——将重心从对话流畅性转向关系深度。若能成功，或将为长期、有情感共鸣的人机互动树立新标准。 叽伴采用自研的三层记忆系统（事件记忆、行为记忆、互动记忆），确保 AI 在不同会话和世界中保持人格连贯性。其 AI 驱动的世界编辑器允许非技术用户通过简单提示生成包含 NPC、剧情线和分支叙事的完整虚拟世界。

rss · 36kr · Apr 3, 02:00

**背景**: 随着大语言模型的发展，AI 陪伴应用大量涌现，但多数依赖短上下文聊天，缺乏记忆能力，导致互动重复或不一致。「OOC」（Out of Character，角色性格漂移）指 AI 因上下文限制或记忆管理不佳而偏离预设性格。近期研究强调，要支持连贯且不断演化的互动关系，AI 智能体需具备长期记忆架构，例如情景记忆与语义记忆分层机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7535740692191936538">AI 智能体 记 忆 机 制 详解作者 | Bhavishya Pandit...</a></li>
<li><a href="https://aigirlfriend.expert/guides/character-ai-ooc-guide/">ULTIMATE Character AI OOC Guide (+ 21 Examples)</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/697862154">全球80+ AI Agent构建平台大盘点，了解智能体平台看这一篇就够了 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI companionship`, `#large language models`, `#AI agents`, `#virtual social interaction`, `#AI memory`

---

<a id="item-15"></a>
## [量旋科技完成 6 亿元 C+轮融资](https://36kr.com/newsflashes/3750435077423625?f=rss) ⭐️ 8.0/10

中国量子计算公司量旋科技近日完成 6 亿元人民币的 C+轮融资，使其在一个季度内的融资总额接近 10 亿元人民币。本轮融资吸引了包括国泰君安创新投、浙江财通资本和四川振兴集团在内的多家国有及市场化投资机构参与。 此次大额融资表明投资者对量子计算这一前沿技术的战略价值高度认可，该技术有望在人工智能、密码学和复杂系统模拟等领域产生深远影响。这也反映出中国正加速布局本土硬科技，以在全球量子竞赛中占据有利位置。 量旋科技已具备从量子芯片设计、流片到封装测试的全链条能力，并计划在 2025 年底前推出 100 量子比特的量子计算机。毅达资本、华强资本等老股东也在本轮继续跟投。

rss · 36kr · Apr 3, 01:39

**背景**: 量子计算利用量子比特（qubit）可同时处于多种状态的特性，在特定问题上比经典计算机实现指数级加速。量旋科技成立于深圳，专注于超导和核磁共振（NMR）两种量子计算技术路线，并提供云端量子计算服务。C+轮融资通常出现在企业高速扩张阶段，可能为上市或重大产品发布做准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spinquanta.com/">Quantum Computer Company & Practical Computing Solutions | SpinQ</a></li>
<li><a href="https://www.techinasia.com/news/chinese-startup-spinq-plans-100-qubit-quantum-computer-in-2025">Chinese startup SpinQ plans 100-qubit quantum computer in 2025</a></li>
<li><a href="https://eu.36kr.com/en/p/3750411191550467">36Kr Exclusive: Shenzhen Quantum Computing Firm Secures ...</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#frontier tech`, `#startup funding`, `#SpinQ`, `#deep tech`

---

<a id="item-16"></a>
## [开发者打造跨平台 AI 超级管家 Wanny](https://www.v2ex.com/t/1203245#reply1) ⭐️ 8.0/10

开发者 Edison Wong 发布了开源 AI 助手 Wanny，它将微信、米家、美的家电、奔驰汽车和 Home Assistant 的设备控制统一到一个控制台中，并支持 AI 驱动的查询、控制、记忆、审批流程和主动关怀功能。 Wanny 展示了 AI、物联网和自动化在现实场景中的融合，解决了智能环境中跨品牌和平台互操作性的核心难题，使数字助手能无缝控制物理世界的各类设备。 Wanny 目前已接入微信、米家（基于 MIoT 协议）、美的 IoT、奔驰车辆 API 和 Home Assistant，计划新增海信等平台。它通过语义理解解析自然语言指令，并计划引入天气建议、设备巡检等主动服务功能。

rss · V2EX · Apr 3, 01:48

**背景**: Home Assistant 是一个开源的家庭自动化平台，支持本地控制并集成数千种智能设备。小米的 MIoT 协议是一套标准化的物联网设备能力描述规范，支持第三方平台（如 Home Assistant）接入米家设备。美的和奔驰也为其智能产品提供了开发者可用的 API，但通常文档有限。由于各厂商生态封闭，跨平台设备统一控制仍是行业难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iot.mi.com/v2/new/doc/introduction/knowledge/spec">MIoT Spec 协议详解 - Xiaomi</a></li>
<li><a href="https://www.home-assistant.io/integrations/">Integrations - Home Assistant</a></li>
<li><a href="https://github.com/al-one/hass-xiaomi-miot">GitHub - al-one/hass-xiaomi-miot: Automatic integrate all ... hass-xiaomi-miot: 自动集成小米/米家设备到 ... - Gitee 美的IoT开发者平台 Home Assistant 米家集成_miot-spec-v2-CSDN博客 给开放智能家居生态一个好的开始：小米官方 Home Assistant 集成上手... Midea - 美的IoT</a></li>

</ul>
</details>

**标签**: `#AI`, `#IoT`, `#Smart Home`, `#Automation`, `#Device Integration`

---

<a id="item-17"></a>
## [西湖大学团队构建全球最大人类泛基因组，发现 13%未知序列](https://www.ithome.com/0/935/593.htm) ⭐️ 8.0/10

西湖大学杨剑教授团队开发了一种名为 PIGA（基于泛基因组的联合组装）的新方法，成功构建了迄今规模最大的人类泛基因组（基于 1000 名中国人），并发现了约 13%（4.053 亿个碱基对）的全新基因组序列。该成果于 2026 年 4 月 1 日发表在《自然》期刊上。 这一突破为精准医疗和遗传病研究提供了更完整、更多样化的人类基因组变异参考，尤其有助于填补此前代表性不足人群的基因组空白。同时，高性价比的 PIGA 方法使大规模泛基因组研究成为可能，克服了以往因测序成本高昂而难以扩展的瓶颈。 PIGA 采用混合测序策略，在泛基因组图框架内整合中等深度的短读长和长读长数据，实现群体水平的二倍体基因组联合组装。相比传统的纯长读长测序方法，该方法将单个样本的测序成本降低数倍，同时提升了组装的准确性和完整性。

rss · IT HOME · Apr 3, 02:04

**背景**: 泛基因组是指一个物种所有个体中包含的全部 DNA 序列总和，既包括多数人共有的“核心”基因，也涵盖部分个体特有的“附属”区域。传统人类基因组参考序列（如 GRCh38）仅基于单个或少数个体，遗漏了大量结构和序列多样性。长读长测序技术（如 PacBio、Oxford Nanopore）虽能实现更完整的基因组组装，但用于大规模人群时成本过高。因此，整合多种测序数据的计算方法对构建可扩展、高精度的泛基因组至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/JianYang-Lab/PIGA">Pangenome-Informed Genome Assembly (PIGA) - GitHub</a></li>
<li><a href="https://www.westlake.edu.cn/news_events/westlakenews/Research/202604/t20260401_65569.html">Nature报道丨西湖大学团队泛基因组“拼装”方法新突破，发现人类13%未知...</a></li>
<li><a href="https://news.qq.com/rain/a/20260402A03H2T00">西湖大学最新Nature论文：杨剑团队构建迄今最大规模人类泛基因组，发...</a></li>

</ul>
</details>

**标签**: `#biotech`, `#genomics`, `#pan-genome`, `#precision medicine`, `#frontier tech`

---

<a id="item-18"></a>
## [广汽本田 P7 推送 OTA 升级，新增 AI 大模型与声音复刻功能](https://www.ithome.com/0/935/589.htm) ⭐️ 8.0/10

广汽本田为其 P7 纯电 SUV 推送了智导互联 4.2.2 版本 OTA 升级，新增车载 AI 大模型，支持旅行规划、用车答疑和闲聊等功能，并可通过手机 App 实现声音复刻，将语音助手变为亲友的声音。 此次升级标志着生成式 AI 技术正加速融入主流消费级电动汽车，通过高度个性化的声音交互、智能出行服务和沉浸式座舱体验，为智能电动车树立了新的标杆。 声音复刻功能仅需通过手机 App 录制简短音频即可实现，AI 大模型还能在特定节日主动问候并提供导航提示；但官方未明确说明所采用的具体大模型（如 Qwen 或 DeepSeek）。

rss · IT HOME · Apr 3, 01:59

**背景**: AI 大语言模型正被广泛应用于汽车场景，实现自然语言交互与个性化服务。声音复刻技术通常基于零样本语音合成（zero-shot TTS），仅需少量参考音频即可克隆目标声音。广汽本田的“云驰智能座舱”通过软硬件深度融合，支持覆盖视觉、听觉、触觉和嗅觉的多感官智能体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bitauto.com/news/100399793935.html">云驰架构赋能！广汽本田 P7上市，重塑智电时代新驾趣 | BitAuto</a></li>
<li><a href="https://github.com/index-tts/index-tts">An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech ...</a></li>
<li><a href="https://www.semidrive.com/en/news/view-NDMwNjU=.html">芯驰科技发布X10，打造全民AI时代座舱处理器新标杆-Enterprise Inform...</a></li>

</ul>
</details>

**标签**: `#AI in automotive`, `#large language models`, `#voice cloning`, `#smart cockpit`, `#OTA update`

---

<a id="item-19"></a>
## [FuriosaAI 计划 2024 年量产 2 万颗 RNGD AI 芯片](https://www.ithome.com/0/935/560.htm) ⭐️ 8.0/10

韩国 AI 芯片公司 FuriosaAI 宣布计划在 2024 年量产 2 万颗第二代 RNGD 推理芯片，继今年 1 月首批 4000 颗之后。该公司还公布了内存升级至 72GB HBM3E，并规划了面向云端和终端设备的芯片路线图，将持续至 2028 年。 这一进展标志着 AI 推理硬件市场竞争加剧，以更高能效和更低总拥有成本挑战英伟达的主导地位。同时，这也体现了该公司向数据中心与终端设备双轨并行的战略转变。 据称，RNGD 芯片在运行 Qwen3-32B（FP8）模型时，在相同功耗下可支持的并发用户数是英伟达 RTX PRO 6000 的 2.2 至 7.4 倍，且总拥有成本仅为后者的 40%。未来版本包括面向 PC 和工作站的轻量版 RNGD S（目标 2026 年底至 2027 年初发布）以及 2028 年推出的第三代芯片。

rss · IT HOME · Apr 3, 01:12

**背景**: FuriosaAI 是一家专注于高能效 AI 推理加速器的韩国半导体初创公司。其 RNGD 芯片面向数据中心的大语言模型推理，强调每瓦性能和成本效益。高带宽内存（HBM），尤其是 HBM3 及更新的 HBM3E，对 AI 芯片至关重要，因其能提供推理所需的海量数据吞吐能力。要与英伟达等巨头竞争，不仅需要技术差异化，还需获得客户认可——FuriosaAI 已成功赢得 LG AI Research 作为首个主要客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.moomoo.com/news/post/55726343/nvidia-challenger-furiosaai-secures-first-major-client-lg">NVIDIA Challenger FuriosaAI Secures First Major Client LG - Moomoo</a></li>
<li><a href="https://www.toolify.ai/daily-ai-news">Latest AI News Today & Daily Updates (2026) - Toolify.ai</a></li>
<li><a href="https://www.moomoo.com/news/post/64283503/star-market-evening-report-baili-tianhe-s-world-first-adc">STAR Market Evening Report | Baili Tianhe's world-first ADC drug ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#inference acceleration`, `#FuriosaAI`, `#RNGD`, `#AI hardware`

---

<a id="item-20"></a>
## [2025 年英伟达在中国 AI 芯片份额降至 55%](https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips) ⭐️ 8.0/10

2025 年，英伟达在中国 AI 芯片市场的份额从制裁前的 95%降至 55%，而中国本土厂商合计拿下 41%的市场份额，共交付 165 万块 AI GPU。华为以近 20%的份额领跑本土厂商，并于近期发布了 Atlas 350 加速器，宣称其性能达到英伟达 H20 的 2.8 倍。 这一变化反映出在美国出口管制和中国政府强力扶持下，中国 AI 基础设施正加速与西方技术脱钩。这标志着国产 AI 芯片竞争力显著提升，可能重塑全球 AI 硬件供应链和技术创新格局。 华为 2025 年出货约 81.2 万块 AI 芯片，阿里平头哥以 25.6 万块紧随其后；新款 Atlas 350 在 FP4 精度下提供 1.56 PFLOPS 算力，配备最高 112GB HBM，功耗为 600W，约为 H20 的 1.5 倍。而 H20 本身是专为中国市场设计的降规版 GPU，核心数比 H100 减少 41%。

telegram · zaihuapd · Apr 2, 06:08

**背景**: 自 2022 年底以来，美国不断加强对华先进 AI 芯片的出口管制，迫使英伟达推出合规但性能削弱的 A800 和 H20 等型号。作为回应，中国将半导体自主可控提升为国家战略，华为等企业依托国产制造工艺和自研软件栈（如 CANN、MindSpore）重启并加速 AI 芯片研发与部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS ...</a></li>
<li><a href="https://wccftech.com/nvidia-china-compliant-h20-gpu-41-percent-fewer-cores-lower-performance-vs-top-hopper-h100/">NVIDIA’s China-Compliant H20 GPU Has 41% Fewer Cores & 28% ...</a></li>
<li><a href="https://eprnews.com/nvidia-h20-ai-chips-features-comparison-with-h100-and-geopolitical-significance-685933/">Nvidia H20 AI Chips: Features, Comparison with H100, and ...</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Semiconductors`, `#Geopolitics`, `#Huawei`, `#Artificial Intelligence`

---

<a id="item-21"></a>
## [近半数美国大学生因 AI 考虑更换专业](https://www.axios.com/2026/04/02/ai-college-students-change-majors-poll) ⭐️ 8.0/10

一项新调查显示，47%的美国大学生因担忧人工智能对未来就业的影响而认真考虑过更换专业，其中 16%已经付诸行动。 这一趋势表明，学生对 AI 时代职业前景的看法正在发生深刻变化，可能重塑高校各专业的招生格局和学业规划。这也凸显了下一代劳动者对技术颠覆就业市场的日益焦虑。 男生比女生更受影响（60%对 38%考虑换专业），技术和职业教育领域的学生担忧比例最高（70–71%）。尽管 42%的学校不鼓励使用 AI，许多学生仍在禁用 AI 的院校中频繁使用相关工具。

telegram · zaihuapd · Apr 2, 12:37

**背景**: 随着大语言模型等人工智能技术能力不断提升，人们越来越担心自动化会取代多个行业的人类工作者。高等教育体系正面临压力，需调整课程设置和职业指导，以帮助学生适应 AI 塑造的就业市场。学生选择专业往往基于对长期就业能力和经济安全的判断。

**标签**: `#AI impact`, `#higher education`, `#career disruption`, `#AI adoption`, `#student behavior`

---

<a id="item-22"></a>
## [Cushion 推出开源 AI 笔记应用](https://www.producthunt.com/products/cushion-5) ⭐️ 8.0/10

开源 AI 笔记应用 Cushion 已在 Product Hunt 上亮相，它利用人工智能帮助用户记录并总结会议内容或个人想法。 随着 AI 重塑生产力工具，像 Cushion 这样的开源替代方案提供了透明度、可定制性和隐私保护——这对开发者和注重隐私的用户至关重要。这也契合了市场对伦理化、社区驱动型 AI 应用日益增长的需求。 Cushion 完全开源，任何人都可以审查、修改或自行托管代码。与许多商业 AI 记录工具不同，它默认不依赖专有云服务，从而增强了用户对数据的控制权。

producthunt · Boyuan Chen · Apr 2, 02:12

**背景**: AI 笔记应用利用语音识别和自然语言处理技术实时转录并总结口语内容，常见例子包括 Otter.ai 和 Fireflies.ai。随着用户越来越希望避免供应商锁定和算法不透明，开源 AI 工具正获得广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thedigitalprojectmanager.com/tools/best-ai-note-taking-apps/">14 Best AI Note-Taking Apps Reviewed in 2026</a></li>
<li><a href="https://www.wired.com/gallery/best-ai-notetakers/">4 Best AI Notetakers (2026), Tested and Reviewed | WIRED</a></li>

</ul>
</details>

**标签**: `#AI`, `#note-taking`, `#open-source`, `#productivity`, `#frontier tech`

---

<a id="item-23"></a>
## [前 Azure 工程师指责内部决策损害信任](https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion) ⭐️ 7.0/10

一位前 Azure 核心工程师发表了一篇详细批评文章，指控微软的内部决策严重削弱了 Azure 的可靠性、文档质量和用户信任。文章特别指出了 Azure OpenAI 服务的故障和 AI 生成文档的问题。 这很重要，因为 Azure 是全球企业广泛使用的主要云平台，可靠性的下降或误导性文档会直接影响业务运营、安全性和 AI 服务的采用。这也引发了更广泛的担忧：在缺乏足够监督的情况下，AI 如何被整合到关键基础设施中。 作者声称已于 2025 年初向微软 CEO 和董事会提交了关切，但未获回应。社区报告包括 Azure OpenAI 在高负载下泄露其他客户数据，以及明显不准确且由 AI 生成的文档。

hackernews · axelriet · Apr 2, 16:00

**背景**: 微软 Azure 是全球领先的云计算平台之一，与 AWS 和谷歌云竞争。近年来，微软通过与 OpenAI 的合作，大力将 AI 集成到 Azure 服务中。然而，文档和服务部署的快速扩展与自动化可能会损害质量与安全性。

**社区讨论**: 社区反应褒贬不一，但大多印证了文章观点：用户分享了关于 Azure 界面混乱、OpenAI 服务不可靠以及 AI 编写文档的第一手经历。一些人质疑作者动机，另一些人则基于自身使用 Azure 的挫败感认同这些说法。

**标签**: `#AI`, `#Cloud Computing`, `#Azure`, `#AI Safety`, `#Enterprise Tech`

---

<a id="item-24"></a>
## [用户组织共享 Google AI Ultra 订阅](https://www.v2ex.com/t/1203254#reply0) ⭐️ 7.0/10

一位 V2EX 用户发起了一项共享（拼车式）Google AI Ultra 订阅计划，将每月 250 美元的费用分摊给多位需要稳定访问权限但不愿管理多个账号的用户。 这反映了用户对高端 AI 服务的真实需求，并展示了用户如何通过非正式的费用分摊方式应对高昂的订阅价格。这也表明社区对 Gemini 3.1 Pro 和 Veo 视频生成等前沿 AI 功能的参与度正在提升。 组织者按每人每月约 300 元人民币（约合 42 美元）收费，基于全年约 1720 元人民币（约合 250 美元）的总费用。参与者需长期承诺，中途退出者将无法享受年底前三个月优惠的平分权益，且不欢迎轻度用户或需要反代的用户加入。

rss · V2EX · Apr 3, 02:00

**背景**: Google AI Ultra 是 Google DeepMind 推出的高级订阅服务，提供对 Gemini 3.1 Pro、Veo 视频生成和深度研究（Deep Research）等先进 AI 模型的增强访问权限。其定价为每月 250 美元，面向需要高调用限额和标准 Pro 版所不具备的前沿多模态能力的专业用户和重度使用者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gemini.google/us/subscriptions/?hl=en">Google AI Pro & Ultra — get access to Gemini 3.1 Pro & more</a></li>
<li><a href="https://www.tomsguide.com/ai/google-ai-ultra-everything-in-the-usd250-month-subscription-and-why-it-might-be-worth-it">Google AI Ultra: Everything in the $250/month subscription ...</a></li>
<li><a href="https://workspace.google.com/products/ai-ultra/">AI Ultra for Business | Google Workspace</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#AI Models`, `#Cloud AI Access`, `#Frontier Tech`, `#AI Subscription`

---

<a id="item-25"></a>
## [AI 技能自动化处理 Harness 工程](https://www.v2ex.com/t/1203250#reply0) ⭐️ 7.0/10

一个名为 harness-engineering 的新开源 AI “技能”已发布，开发者可通过自然语言生成和迭代 Harness 基础设施即代码配置，无需深厚专业知识。它通过 npx skills CLI 安装，并集成到新兴的智能体技能生态中。 该工具降低了采用 Harness 工程等高级 DevOps 实践的门槛，通过自动化复杂基础设施工作流加速产品开发。它体现了 AI 智能体通过可复用、上下文感知的自动化来提升开发者生产力的趋势。 该技能托管在 GitHub 的 10xChengTu/harness-engineering 仓库下，通过 'npx skills add' 命令安装。它被设计为根据用户遇到的问题持续更新能力，并推荐全局安装。

rss · V2EX · Apr 3, 01:58

**背景**: Harness 工程指为 AI 编码智能体设计结构化接口，以在长期软件任务中提供上下文、约束和反馈机制。它不同于提示工程，更注重可持续、可维护的智能体工作流。Vercel Labs 推出的 'skills' CLI 等工具支持模块化、可组合的智能体能力，可在不同项目间共享复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users - Martin Fowler</a></li>
<li><a href="https://www.anthropic.com/engineering/harness-design-long-running-apps">Harness design for long-running application development - Anthropic</a></li>
<li><a href="https://skills.sh/docs/cli">CLI | Skills Documentation</a></li>

</ul>
</details>

**标签**: `#AI Developer Tools`, `#DevOps Automation`, `#Infrastructure as Code`, `#AI Coding Assistant`, `#Frontier Tech Application`

---

<a id="item-26"></a>
## [荣耀与京东达成三年战略合作，目标销售额超千亿元](https://www.ithome.com/0/935/568.htm) ⭐️ 7.0/10

4 月 2 日，荣耀与京东宣布达成三年全方位战略合作，目标实现累计超 1000 亿元销售额。双方将在产品共创、用户共营、生态共享基础上，聚焦 AI 合作、机器人、智能硬件及 C2M（消费者直连工厂）定制项目。 此次合作标志着头部手机品牌与国内最大电商平台在 AI 与智能硬件生态上的深度融合，有望推动以消费者需求为导向的智能制造和智慧零售创新，体现了行业向 AI 驱动、需求响应型供应链转型的趋势。 合作强调 C2M（消费者直连工厂）模式，通过平台将消费者需求直接对接工厂，跳过中间环节，并包含联合 IP 开发与 AI 驱动的用户体验优化。荣耀将发挥硬件研发优势，京东则提供电商数据与物流能力。

rss · IT HOME · Apr 3, 01:25

**背景**: C2M（Customer-to-Manufacturer，消费者直连工厂）是一种通过数字平台让消费者直接对接制造商的商业模式，可实现大规模定制并降低成本，省去品牌商、代理商等中间环节。在中国，京东等电商平台积极推动 C2M 模式，以支持智能制造和提升供应链效率。此类 AI 合作通常利用消费数据和生成式 AI 优化产品设计与个性化体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/C2M/9858878">C2M - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/70278004">电商平台的C2M模式是什么? - 知乎专栏</a></li>

</ul>
</details>

**标签**: `#AI collaboration`, `#smart hardware`, `#robotics`, `#C2M`, `#strategic partnership`

---

<a id="item-27"></a>
## [Windows 11 任务管理器新增详细 NPU 监控功能](https://www.windowscentral.com/microsoft/windows-11/windows-11-task-manager-npu-stats-insider) ⭐️ 7.0/10

Windows 11 Insider 预览版 Build 26300.8142 在任务管理器中扩展了 NPU 监控功能，在进程、用户和详细信息选项卡中新增了 NPU 使用率列，并在性能选项卡中加入了神经引擎条目及专用/共享 NPU 内存指标。 此次更新让用户和开发者能更清晰地观察本地 AI 工作负载的运行情况，有助于优化和调试依赖 NPU 的应用程序——NPU 是高效本地 AI 推理的关键硬件。这也表明微软正积极构建对 AI PC 生态系统的系统级支持。 新增的 NPU 指标包括 NPU 使用率、NPU 引擎、专用 NPU 内存和共享 NPU 内存等列，仅在配备 NPU 的设备上显示；此前任务管理器仅在性能选项卡中显示基础的 NPU 使用百分比。

telegram · zaihuapd · Apr 2, 10:25

**背景**: NPU（神经网络处理单元）是一种专为加速神经网络计算而设计的处理器，尤其适用于图像识别或实时背景虚化等 AI 推理任务。与通用 CPU 或侧重图形处理的 GPU 不同，NPU 针对低功耗、高效率的本地 AI 工作负载进行了优化，广泛应用于智能手机和 AI PC 等设备。微软正通过 Windows 11 深度集成 NPU 支持，以推动新一代端侧 AI 体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1969000469310464891">NPU是什么？详细介绍CPU、GPU、NPU、TPU！ - 知乎</a></li>
<li><a href="https://www.cnblogs.com/geekbruce/articles/18675150">NPU的概念理解，以及和CPU/GPU的区别解析。 - AlphaGeek - 博客园</a></li>
<li><a href="https://www.ithome.com/0/934/288.htm">微软 Win 11 任 务 管 理 器 迎 AI 硬件 监 控 升级：新增 NPU 监 测 功 能 - IT之家</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#NPU`, `#Windows 11`, `#system monitoring`, `#on-device AI`

---