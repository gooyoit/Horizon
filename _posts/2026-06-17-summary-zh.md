---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> From 117 items, 12 important content pieces were selected

---

1. [智谱发布并开源 GLM-5.2：专注 Coding 与长程任务](#item-1) ⭐️ 10.0/10
2. [SpaceX 将以 600 亿美元收购 AI 代码编辑器 Cursor](#item-2) ⭐️ 9.0/10
3. [DeepSeek 拟首轮外部融资超 500 亿人民币](#item-3) ⭐️ 9.0/10
4. [本地开源 AI 模型正在变得真正具有竞争力](#item-4) ⭐️ 8.0/10
5. [llama.cpp 创始人 Georgi Gerganov 高度评价 Qwen3.6-27B 的本地编程能力](#item-5) ⭐️ 8.0/10
6. [Claude Fable 5 因修复漏洞代码而被出口管制封禁](#item-6) ⭐️ 8.0/10
7. [OpenAI Codex 三种操作电脑能力详解：Browser、Chrome 与 Computer Use](#item-7) ⭐️ 8.0/10
8. [微软 Copilot Cowork 全球可用，拟引入 Azure 托管 DeepSeek V4 降本](#item-8) ⭐️ 8.0/10
9. [Cursor 推出 Origin：面向 AI 智能体协作的代码托管平台](#item-9) ⭐️ 8.0/10
10. [字节跳动将 AI 资源重心从豆包转向企业服务](#item-10) ⭐️ 8.0/10
11. [中国加紧筹建世界人工智能合作组织](#item-11) ⭐️ 8.0/10
12. [Android 17 正式发布：强制大屏适配与原生 AI 集成](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [智谱发布并开源 GLM-5.2：专注 Coding 与长程任务](https://mp.weixin.qq.com/s/hrZcV05ZSIKvd1dzSqDNDQ) ⭐️ 10.0/10

智谱今日正式发布并开源了 GLM-5.2 模型，该模型具备 100 万 token 的无损上下文能力，并引入了 IndexShare 架构和改进的 MTP 层等创新设计。在 Code Arena 盲测中，GLM-5.2 取得了全球可用模型第一名，且在主流编程基准上与 Claude Opus 4.8 和 GPT-5.5 等前沿模型表现相当。 在部分国际前沿模型突然变得不可用的背景下，此次发布为开发者社区提供了一个强大且完全开源的替代方案。该模型不仅能够处理百万级上下文和跨越数天的复杂智能体任务，还全面适配了多种国产算力平台，极大地推动了开源 AI 生态的发展。 在技术层面，该模型引入的 IndexShare 架构将 1M 上下文下的单位 token FLOPs 降至 2.9 倍，同时改进的 MTP 层将接受长度提升了 20%。模型权重采用 MIT 协议开源，并在发布首日（Day 0）即完成了对华为昇腾、平头哥、摩尔线程和寒武纪等国产算力平台的适配。

rss · AI Hot · Jun 17, 01:10

**背景**: 长程任务和超大上下文窗口对于 AI 编程智能体至关重要，因为这要求模型在长时间（有时跨越数天）的工作中保持逻辑连贯并准确回忆信息。多 Token 预测（MTP）是一种旨在通过同时预测多个 Token（而非逐字预测）来提升推理效率和速度的架构技术。Code Arena 是一个前端开发盲测平台，在不知道具体模型来源的情况下对模型的真实开发能力进行评估。

**标签**: `#AI Models`, `#Open Source`, `#Coding Agents`, `#Long Context`, `#Zhipu AI`

---

<a id="item-2"></a>
## [SpaceX 将以 600 亿美元收购 AI 代码编辑器 Cursor](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/) ⭐️ 9.0/10

2026 年 6 月 16 日，SpaceX 宣布将收购 AI 代码编辑器 Cursor 的母公司 Anysphere，交易对该初创公司的估值约为 600 亿美元。这一估值相比 Cursor 在 2026 年初的 293 亿美元估值翻了一倍多。 此次收购标志着一家航空航天与太空探索公司前所未有地进军 AI 驱动的软件开发工具市场，暗示了 SpaceX 的重大战略转型。600 亿美元的标价凸显了市场对 AI 编程工具赋予的极高估值，可能重塑 AI 辅助开发行业的竞争格局。 截至 2026 年初，Cursor 的年度经常性收入（ARR）已超过 30 亿美元，使其成为历史上增长最快的 SaaS 公司之一。这笔交易是有史以来最大的科技收购案之一，600 亿美元的估值仅比几个月前 Cursor 的前一轮估值翻了一倍。

hackernews · itsmarcelg · Jun 16, 10:44 · [社区讨论](https://news.ycombinator.com/item?id=48553224)

**背景**: Cursor 由 Anysphere 公司开发，成立于 2022 年，是一款 AI 优先的代码编辑器，将大语言模型直接集成到软件开发工作流中，允许程序员使用自然语言指令来编写、编辑和调试代码。该工具在开发者和企业中获得了广泛采用，NVIDIA 首席执行官黄仁勋曾公开表示 Cursor 为其 4 万名工程师带来了显著的效率提升。AI 编程工具市场已成为科技领域最热门的赛道之一，Cursor、GitHub Copilot 等公司正在竞争定义 AI 时代软件的编写方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anysphere">Anysphere</a></li>

</ul>
</details>

**社区讨论**: 社区反应高度质疑和困惑。多位评论者质疑一家太空公司为何要收购 IDE，有人指出 600 亿美元的价格相当于建造 150 座现代医院的费用。还有人讨论估值的合理性，将其与 Mojang/Minecraft 25 亿美元的收购价进行不利对比，同时一些用户表示已弃用 Cursor 转而选择 Codex 和 Claude 等竞争工具，暗示该产品可能正在失去竞争优势。

**标签**: `#AI Coding`, `#M&A`, `#SpaceX`, `#Cursor`, `#Frontier Tech`

---

<a id="item-3"></a>
## [DeepSeek 拟首轮外部融资超 500 亿人民币](https://t.me/zaihuapd/41983) ⭐️ 9.0/10

据报道，DeepSeek 正推进其首轮外部融资，目标募集规模超过 500 亿人民币，若顺利落地将成为中国 AI 公司迄今规模最大的一轮融资。创始人梁文锋计划在此轮中顶格出资，具有国资背景的产业投资基金或将参与领投。 这笔巨额融资标志着 DeepSeek 正从研究型实验室向商业化企业级 AI 竞争者转型，即将推出的 V4.1 模型将重点面向企业端客户。国资背景基金的参与也凸显了前沿 AI 对中国国家科技战略的重要性。 公司计划于 2025 年 6 月正式推出 V4.1 版本模型，该版本将重点向企业端发力以加速商业化落地。超过 500 亿人民币（约 70 亿美元）的融资规模在中国 AI 公司中史无前例，反映出投资者极大的信心。

telegram · @zaihuapd · Jun 16, 08:20

**背景**: DeepSeek 由同时创立量化对冲基金幻方量化的梁文锋创立，已成为中国最知名的 AI 实验室之一。该公司此前凭借开源模型获得全球关注，这些模型以显著更低的训练成本实现了与西方领先模型相媲美的性能。与许多资金充裕的 AI 初创公司不同，DeepSeek 此前一直未进行外部融资，而是依靠母公司的资金支持。

**标签**: `#DeepSeek`, `#AI Funding`, `#Frontier Models`, `#Artificial Intelligence`, `#China AI`

---

<a id="item-4"></a>
## [本地开源 AI 模型正在变得真正具有竞争力](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) ⭐️ 8.0/10

一场热门的 Hacker News 讨论指出，像 Qwen3.6-27B 这样的本地开源模型已经发展到让部分用户在日常任务中更倾向于使用它们，而非 Claude Sonnet 4.6 等付费专有模型。这场对话揭示了在更优的模型架构和消费级硬件普及的推动下，本地模型与前沿云端 AI 之间的差距正在迅速缩小。 随着本地模型能力的不断增强，它们通过提供注重隐私且仅需一次性成本的方案，对主要 AI 实验室的订阅收入构成了威胁，成为月度云 API 费用的有力替代品。这一转变将推动高性能 AI 的普及，并为硬件供应商（尤其是具备高带宽统一内存架构的 Apple）创造巨大的市场机遇。 用户指出了模型架构上的根本性权衡：稠密模型（如 Qwen 27B）更智能但速度慢，而混合专家模型（如 Gemma 26B）速度快但更容易出错。此外，虽然量化（降低权重精度以节省内存）使本地 AI 变得可行，但用户反映过度激进的量化（例如低于 4-bit）会显著降低工具调用等复杂任务的性能。

hackernews · jfb · Jun 16, 14:36 · [社区讨论](https://news.ycombinator.com/item?id=48555993)

**背景**: 本地大语言模型（LLM）是在用户自己的硬件（如 GPU 或 Apple Silicon）上运行，而非依赖云服务器的大型语言模型，能够确保所有数据处理保持私密。为了将庞大的模型塞进消费级硬件中，用户采用了“量化”技术，将模型权重的精度从 16 位降低到更低的位宽（如 4 位），在质量损失极小的情况下大幅减少了内存需求。GPU 的显存容量和内存带宽几乎总是本地推理速度的主要瓶颈。虽然“开放权重”模型允许任何人下载并运行预训练的数值参数，但它与真正的“开源” AI 有所不同，后者还需要公开训练数据和代码以实现完全透明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hardwarepedia.com/learn/local-ai">Running AI Locally: Complete Hardware & Software Guide (2026) | Hardwarepedia</a></li>
<li><a href="https://deasadiqbal.medium.com/understanding-open-weights-vs-open-source-models-988b50ce64d7">Understanding Open Weights vs. Open Source Models | by Asad Iqbal | Medium</a></li>
<li><a href="https://www.local-llm.net/learn/hardware-requirements/">Local AI Hardware Guide: GPU, CPU, RAM, and Storage Requirements</a></li>

</ul>
</details>

**社区讨论**: 社区的整体态度是谨慎乐观的，但在当前的实际可用性上存在分歧；一些用户抱怨由于极高的内存需求和量化导致的工具调用能力下降，运行本地模型仍然相当痛苦。相反，另一些人则认为，由于带有更少的强加观点，像 Qwen3.6-27B 这样的模型在用户满意度上已经超越了 Claude 等付费选项。许多评论者一致认为，这一趋势对 Anthropic 等公司的定价构成了严重的上限威胁，同时强调 Apple 的硬件有望成为未来无缝本地 AI 的主导平台。

**标签**: `#Local LLMs`, `#Open Source AI`, `#Hacker News`, `#AI Hardware`, `#Open Weights`

---

<a id="item-5"></a>
## [llama.cpp 创始人 Georgi Gerganov 高度评价 Qwen3.6-27B 的本地编程能力](https://simonwillison.net/2026/Jun/16/georgi-gerganov/#atom-everything) ⭐️ 8.0/10

llama.cpp 的创始人 Georgi Gerganov 公开分享了他过去一个半月以来在日常编程任务中使用 Qwen3.6-27B 模型的极佳体验。他详细介绍了自己使用的硬件设备（M2 Ultra 和 RTX 5090）以及运行在离线模式下的 pi agent 轻量级配置。 作为本地大模型社区的领军人物，Gerganov 的实际背书证明了像 Qwen3.6-27B 这样的开源权重模型已经在专业软件开发中具备了真正的实用价值。他展示的具体工作流证明了完全私有化的本地 AI 编程环境是可行的，且无需依赖外部云 API。 Gerganov 使用 `pi -nc --offline` 命令运行去除了网络和云端功能的 pi agent，并配合一段简短的自定义系统提示词，使模型的输出风格与他个人的编程习惯保持一致。Qwen3.6-27B 是一个拥有 270 亿参数的稠密模型，具备 262K 上下文窗口和混合注意力机制。

rss · Simon Willison · Jun 16, 16:04

**背景**: llama.cpp 是一个广泛使用的开源 C/C++ 库，能够在消费级硬件上实现高效的大语言模型推理。pi agent 是一个基于终端的编程助手，可以直接与本地 llama.cpp 服务器集成，从而完全在离线状态下浏览和加载模型。Qwen3.6-27B 是 Qwen 模型家族的最新成员，专门设计用于在体积更小、可本地运行的封装中提供旗舰级的智能体编程能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6-27b">Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml - org / llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://github.com/gsanhueza/pi-llama-cpp">gsanhueza/pi-llama-cpp - GitHub</a></li>

</ul>
</details>

**标签**: `#Local LLMs`, `#Qwen`, `#llama.cpp`, `#Coding Assistants`, `#Open Source AI`

---

<a id="item-6"></a>
## [Claude Fable 5 因修复漏洞代码而被出口管制封禁](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything) ⭐️ 8.0/10

安全专家 Kate Moussouris 证实，导致 Claude Fable 5 被美国出口管制封禁的所谓"越狱"手段，实际上仅仅是要求模型"修复这段代码"——这是一项标准的编程能力。研究人员获取了含有已知 CVE 漏洞的开源代码和故意植入漏洞的新代码，然后利用 Fable 5 修复漏洞的输出生成补丁测试脚本，整个过程需要手动多步操作。 这一案例暴露了当前 AI 出口管制政策的一个根本性缺陷：它实际上因为模型具备防御性网络安全能力而将其封禁，而这些能力对软件开发者和安全防御者至关重要。正如 Moussouris 所指出的，发现、修复和验证安全漏洞的能力是 AI 在防御安全领域所能做的最有价值的事情，移除这一能力将使模型在其核心用途上大打折扣。 研究人员最初要求 Fable 5"审查代码中的安全问题"，模型拒绝了；只有当他们将请求改为"修复这段代码"时，模型才予以配合。Moussouris 强调，这一能力无法在不损害模型整体漏洞修复和补丁验证能力的前提下被移除，因为安全漏洞只是软件漏洞中一个关键类别而已。

rss · Simon Willison · Jun 16, 05:20

**背景**: 美国越来越多地利用出口管制来监管 AI 技术，拜登政府从 2025 年初开始成为首批通过出口管制监管 AI 的政府之一。Claude Fable 5 由 Anthropic 于 2026 年 6 月 9 日发布，是一款 Mythos 级别的模型，专为高自主性和高可靠性的复杂长周期编程任务而设计。CVE（通用漏洞披露）是业界广泛使用的公开披露网络安全漏洞的标准化词典。出口管制框架似乎针对那些被认为能够"制造网络攻击"的模型，但缺乏技术背景的政策制定者可能难以区分攻击性能力和必要的防御性功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregreview.org/2025/09/25/flatley-the-united-states-regulates-artificial-intelligence-with-export-controls/">The United States Regulates Artificial Intelligence with Export Controls | The Regulatory Review</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Policy`, `#Export Controls`, `#Cybersecurity`, `#Anthropic`

---

<a id="item-7"></a>
## [OpenAI Codex 三种操作电脑能力详解：Browser、Chrome 与 Computer Use](https://x.com/shao__meng/status/2067051854312452575) ⭐️ 8.0/10

一篇详细的技术分析解释了 OpenAI Codex 的三个不同层级电脑交互能力：用于本地开发的沙箱内浏览器（Browser）、用于已登录 SaaS 会话的 Chrome 扩展，以及完全控制 macOS 和 Windows 原生桌面 GUI 的 Computer Use。三种模式分别通过 Plugin → Browser、Plugin → Chrome 和 Settings → Computer Use 触发，信任面和权限依次递增，但速度也依次降低。 这种分层方法反映了行业更广泛的趋势：AI 智能体正从隔离的编码沙箱走向真实工作发生的实际计算环境。其决策框架——优先使用结构化 API，然后是沙箱浏览器，再到已认证的 Chrome，最后才是完全桌面控制——为开发者提供了在自动化能力与安全风险之间取得平衡的实用心智模型。 沙箱浏览器没有 Cookie、扩展或登录态，仅适用于本地开发和视觉调试；Chrome 则利用用户真实的已认证身份（意味着操作算作用户本人行为）；Computer Use 最慢但可以操作原生应用和系统设置。Appshots（双击 Cmd）仅向 Codex 提供视觉上下文而不授予任何控制权，是一个只读检查工具。

rss · AI Hot · Jun 17, 01:09

**背景**: OpenAI Codex 最初是一个基于终端的编码智能体，但已迅速扩展为多环境自动化平台。2026 年 5 月初发布的 Codex Chrome 扩展是一个关键里程碑，使智能体能够直接访问已认证的浏览器会话，将其从开发者沙箱推向 Gmail、Salesforce 和 LinkedIn 等 Web 应用。Computer Use 代表了 GUI 智能体能力的前沿，模型通过截图和输入模拟而非 API 与桌面应用程序进行交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/codex/app/computer-use">Computer Use – Codex app | OpenAI Developers</a></li>
<li><a href="https://developers.openai.com/codex/app/browser">In-app browser – Codex app | OpenAI Developers</a></li>
<li><a href="https://chierhu.medium.com/openai-codexs-browser-use-feature-b7dffa761d45">OpenAI Codex’s browser use feature | by Chier Hu | Apr, 2026 ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#Computer Use`, `#AI Agents`, `#Browser Automation`

---

<a id="item-8"></a>
## [微软 Copilot Cowork 全球可用，拟引入 Azure 托管 DeepSeek V4 降本](https://x.com/shao__meng/status/2067047987403268337) ⭐️ 8.0/10

微软宣布其多模型智能体系统 Copilot Cowork 正式全球可用，并正在转向基于使用量的定价模式。为了控制智能体工作流的高昂成本，微软正积极评估在 Azure 上托管微调版的 DeepSeek V4，作为 Anthropic 和 OpenAI 模型的低成本替代方案。 这一举措凸显了智能体 AI 应用中 token 消耗成本的不可持续性，标志着行业正从包月无限用模式转向基于使用量的计费。通过潜在地整合微调版 DeepSeek 模型，微软展示了开源模型如何通过在受信任的云内保持数据驻留的同时提供极高的成本效益，从而颠覆企业级 AI 市场。 顶级模型之间的定价差距巨大；例如，Anthropic 的 Fable 5 输出定价为每百万 token 50 美元，而 DeepSeek V4 Pro 仅为 0.87 美元，两者相差约 57 倍。微软保证，托管的 DeepSeek 模型将完全保留在 Azure 内，受企业级安全、合规和数据驻留控制保护，并预计在未来几周内发布官方公告。

rss · AI Hot · Jun 17, 00:53

**背景**: Copilot Cowork 是集成在 Microsoft 365 中的智能体系统，能够跨各种应用和数据规划和执行长期、多步骤的工作流。与简单的聊天机器人不同，AI 智能体需要反复调用底层语言模型来完成复杂任务，导致 token 消耗和计算成本呈指数级增长。DeepSeek 是一家中国 AI 公司，以其高效的开源权重模型而闻名，这些模型以远低于传统西方模型的训练和推理成本实现了极具竞争力的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done - microsoft.com</a></li>
<li><a href="https://thewincentral.com/microsoft-copilot-cowork-generally-available-ai-teammate/">Microsoft Copilot Cowork General Availability: Complete Guide - WinCentral</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#Microsoft Copilot`, `#DeepSeek`, `#Multi-Model`, `#AI Agents`, `#Azure`

---

<a id="item-9"></a>
## [Cursor 推出 Origin：面向 AI 智能体协作的代码托管平台](https://x.com/AYi_AInotes/status/2067045317707436290) ⭐️ 8.0/10

Cursor 宣布推出 Origin，这是一款 AI 原生的代码托管与 Git 协作平台，定位为 GitHub 的替代方案，专为人机与 AI 智能体协同编码而优化。Origin 由 Cursor 近期收购的 Graphite 团队研发，可承载每小时 81,000 次推送，自动处理高频合并冲突，并基于 S3 实现无限副本快速分发给不同 Agent，预计于 2025 年秋季正式上线。 此次发布标志着 Cursor 从热门 AI 代码编辑器向端到端开发平台的战略升级，直接挑战 GitHub 在代码托管领域的主导地位。随着 AI 编程智能体的普及，为人类工作节奏设计的现有基础设施正成为瓶颈，因此专为智能体规模操作打造的平台将成为软件工程未来的关键基础设施层。 Origin 原生兼容 Git，这意味着开发者现有的工作流无需任何改动即可上手使用。该系统基于 S3 存储实现无限代码库副本以支持 Agent 的并行操作，并具备专为多个 AI 智能体高频、并发代码贡献设计的自动合并冲突解决机制。

rss · AI Hot · Jun 17, 00:43

**背景**: Cursor 是一款广泛使用的 AI 原生 IDE，将大语言模型直接集成到编程体验中，其母公司 Anysphere 近期被 SpaceX 收购，成为一起引人注目的跨界交易。Origin 背后的 Graphite 团队是一款代码审查和堆叠工具，Cursor 收购它是为了加强自身的协作能力。GitHub 等传统平台围绕人类节奏的 Pull Request 和代码审查而设计，在面对数十个 AI 智能体同时读取、写入和合并代码的极端吞吐量需求时可能会显得力不从心。

**标签**: `#AI Agents`, `#Cursor`, `#AI Infrastructure`, `#Software Engineering`, `#Developer Tools`

---

<a id="item-10"></a>
## [字节跳动将 AI 资源重心从豆包转向企业服务](https://www.ithome.com/0/965/167.htm) ⭐️ 8.0/10

据报道，字节跳动正在将 AI 资源从面向大众的豆包应用转向企业服务，原因是豆包日收入不足百万元，而日算力成本高达数千万元。与此同时，其企业级产品 Seedance 年化收入已达约 20 亿美元，字节还于 6 月 15 日上线了 Seedance 2.0 Mini 视频生成模型。 这一转变暴露了消费级 AI 应用的严峻经济现实——巨额算力成本远超收入，同时表明目前最可持续的 AI 商业模式可能在于企业服务。作为中国最大的科技公司之一，字节的这一举措可能会影响整个行业未来在 AI 投资和资源分配上的优先级。 豆包的日算力成本达数千万元人民币，而日收入不足百万元；Seedance 单月收入超 10 亿元，几乎可以抵消豆包的算力支出。Seedance 2.0 Mini 主打高性价比的视频生成能力，且 Seedance 的收入主要来自企业客户。

rss · AI Hot · Jun 17, 00:30

**背景**: 豆包是字节跳动面向消费者的 AI 助手应用，类似于 ChatGPT，为中国普通用户提供聊天和内容生成服务。大规模运行大语言模型需要巨大的算力，通常依赖昂贵的 GPU，这使得消费级 AI 应用的运营成本极高。相比之下，企业级 AI 服务是将 API 访问、定制模型或视频生成等专业工具直接出售给愿意支付高价的商业客户。年化收入（ARR）是将当前月收入按全年折算来估算年度营收规模的指标。

**标签**: `#ByteDance`, `#AI Strategy`, `#Enterprise AI`, `#Doubao`, `#Video Generation`

---

<a id="item-11"></a>
## [中国加紧筹建世界人工智能合作组织](https://36kr.com/newsflashes/3856646470227201?f=rss) ⭐️ 8.0/10

中国在 6 月 17 日的国新办新闻发布会上宣布，正在加紧筹建世界人工智能合作组织（WAICO），欢迎各方加入，共促智能向善。该组织于 2025 年 7 月 26 日由中国政府倡议成立，初步考虑总部设在上海。 此举使中国成为塑造全球人工智能治理的关键力量，为西方主导的 AI 监管努力提供了替代框架。该组织旨在促进在 AI 安全、伦理和标准方面的包容性国际合作，特别是让全球南方国家参与到规则制定过程中。 WAICO 旨在作为国际公共产品，主要围绕三大支柱：深化创新合作、推动普惠发展、加强协同共治。该组织致力于打造供需对接平台，破除生产要素流动壁垒，促进各国间务实的 AI 合作。

rss · 36kr · Jun 17, 02:23

**背景**: 该倡议由国务院总理李强于 2025 年 7 月 26 日在上海举行的世界人工智能大会（WAIC）上首次宣布。它体现了中国坚持多边主义、推动共商共建共享全球治理的更广泛战略。在中美两国争夺变革性 AI 技术影响力之际，WAICO 代表了中国制定包容性全球标准、制衡西方在 AI 治理中主导地位的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/yaowen/liebiao/202507/content_7033957.htm">中国政府倡议成立世界人工智能合作组织__中国政府网</a></li>
<li><a href="https://www.reuters.com/world/china/china-proposes-new-global-ai-cooperation-organisation-2025-07-26/">China proposes new global AI cooperation organisation | Reuters</a></li>
<li><a href="https://www.outlookbusiness.com/deeptech/artificial-intelligence/whats-world-ai-cooperation-organization-launched-by-china-to-counter-western-dominance-in-ai-governance">What's 'World AI Cooperation Organization' Launched by China to Counter Western Dominance in AI Governance – Outlook Business</a></li>

</ul>
</details>

**标签**: `#AI Governance`, `#AI Policy`, `#China`, `#International Relations`, `#World AI Cooperation Organization`

---

<a id="item-12"></a>
## [Android 17 正式发布：强制大屏适配与原生 AI 集成](https://android-developers.googleblog.com/2026/06/Android-17.html) ⭐️ 8.0/10

Android 17 已正式推送到支持的 Pixel 设备并同步开放源代码。该版本引入了 AppFunctions API（API 级别 36），让 Gemini 等 AI 助手可以直接调用应用内功能；同时强制要求应用适配大屏，移除了开发者锁定屏幕方向和尺寸的选项，并要求本地网络访问必须获得明确授权。 此次发布标志着向 AI 驱动操作系统的重大范式转变，AI 助手可以直接在应用内执行操作，而不再依赖屏幕自动化。强制大屏适配以及官方将 Jetpack Compose 确立为首选 UI 工具包，将迫使开发者大幅重构现有应用，重塑整个 Android 开发生态。 针对 Android 17 的应用现在需要 ACCESS_LOCAL_NETWORK 运行时权限，或必须使用系统级设备选择器进行本地网络通信；系统还将根据设备总内存强制执行严格的内存上限。传统 Android View 系统已进入维护模式，Google 正式将 Android 开发全面转向 Jetpack Compose。

telegram · @zaihuapd · Jun 17, 01:02

**背景**: AppFunctions 框架允许任何应用暴露一个或多个功能供 Gemini 等 AI 助手发现和调用，作为构建 AI Agent 的屏幕自动化的结构化设备端替代方案。Jetpack Compose 是 Google 面向 Android 的现代声明式 UI 工具包，相比旧版命令式 View 系统具有更清晰的架构，被推荐用于新项目。在 Android 17 之前，应用无需用户明确同意即可自由访问本地网络，能够静默扫描同一 Wi-Fi 网络上的设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.android.com/reference/android/app/appfunctions/package-summary">android . app . appfunctions | API reference | Android Developers</a></li>
<li><a href="https://android-developers.googleblog.com/2026/06/Android-17.html">Android Developers Blog: Android 17 is here</a></li>
<li><a href="https://developer.android.google.cn/ai/appfunctions/add-appfunctions?hl=en">Add the AppFunctions API to your app | AI | Android Developers</a></li>

</ul>
</details>

**标签**: `#Android`, `#Mobile AI`, `#Gemini`, `#Operating System`, `#AppFunctions`

---