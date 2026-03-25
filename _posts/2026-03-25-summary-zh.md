---
layout: default
title: "Horizon Summary: 2026-03-25 (ZH)"
date: 2026-03-25
lang: zh
---

> From 93 items, 19 important content pieces were selected

---

1. [Claude Code 推出基于 AI 的自动权限模式](#item-1) ⭐️ 9.0/10
2. [流式专家技术让消费设备运行万亿参数 MoE 模型](#item-2) ⭐️ 9.0/10
3. [我国日均 AI 词元调用量两年激增超千倍](#item-3) ⭐️ 9.0/10
4. [Google 推出基于 Gemini 的暗网威胁情报 AI 代理](#item-4) ⭐️ 9.0/10
5. [OpenAI 拟停用 Sora，转向 AI 智能体与 Spud 模型](#item-5) ⭐️ 9.0/10
6. [Claude Code 推出内置安全审查的自动模式](#item-6) ⭐️ 9.0/10
7. [OpenAI 关停 Sora 视频生成应用](#item-7) ⭐️ 8.0/10
8. [LiteLLM 1.82.7–1.82.8 版本遭供应链攻击](#item-8) ⭐️ 8.0/10
9. [恶意 LiteLLM 包通过.pth 文件窃取凭证](#item-9) ⭐️ 8.0/10
10. [光象科技完成超亿元具身智能机器人融资](#item-10) ⭐️ 8.0/10
11. [英伟达借资金优势捆绑 AI 初创企业](#item-11) ⭐️ 8.0/10
12. [阿里发布玄铁 C950 RISC-V CPU，集成 AI 加速器](#item-12) ⭐️ 8.0/10
13. [包管理器引入依赖冷却期以提升安全性](#item-13) ⭐️ 7.0/10
14. [开源软件工厂结合 Claude Agent SDK 与 GitHub](#item-14) ⭐️ 7.0/10
15. [Chaterm 周年庆：赠送 3 个月 Pro 会员](#item-15) ⭐️ 7.0/10
16. [AMD RDNA 4m 核显 GFX1171/GFX1172 现身，强化 AI 计算能力](#item-16) ⭐️ 7.0/10
17. [天钡预热搭载锐龙 AI 9 HX 470 的 MACO470 迷你主机](#item-17) ⭐️ 7.0/10
18. [亚马逊收购人形机器人初创公司 Fauna Robotics](#item-18) ⭐️ 7.0/10
19. [中国刷新光通信纪录：2.5 Pb/s 实时光传输](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude Code 推出基于 AI 的自动权限模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 9.0/10

Claude Code 推出了“自动模式”（auto mode），该系统使用专用分类器模型（Claude Sonnet 4.6）根据用户意图和安全规则自动批准或阻止代码操作，取代了手动确认或不安全的跳过权限标志。 这一进步大幅提升了自主 AI 编码代理的可用性与安全性，在不牺牲安全性的前提下实现可信自动化，为安全的 AI 辅助开发工作流树立了新标准。 该分类器无论主模型为何均运行于 Claude Sonnet 4.6，执行默认的允许/拒绝规则（例如允许项目范围内的本地文件操作，但阻止执行外部代码），并支持自定义规则扩展；还能提前拦截看似为后续恶意操作做侦察的行为。

rss · Simon Willison · Mar 24, 23:57

**背景**: 像 Claude Code 这样的 AI 编程助手可执行编辑文件、运行命令或发起网络请求等强大操作，若缺乏监督则存在安全风险。传统方法要求用户手动批准每个操作，阻碍了自动化。权限系统借鉴移动应用权限机制，通过允许列表和拒绝列表控制 AI 代理可执行的操作，在自主性与安全性之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6">What's new in Claude 4.6 - Claude API Docs</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-4-6.html">Claude Sonnet 4.6 - Amazon Bedrock</a></li>
<li><a href="https://www.briangershon.com/blog/securing-ai-coding-tools/">Securing AI Coding Tools: Permission Controls and Credential Protection for Engineering Teams | Brian Gershon</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Code LLM`, `#Safety`, `#Claude`, `#Autonomous Coding`

---

<a id="item-2"></a>
## [流式专家技术让消费设备运行万亿参数 MoE 模型](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 9.0/10

研究人员利用“流式专家”（streaming experts）技术，在 MacBook 和 iPhone 等消费级设备上成功运行了 Kimi K2.5 和 Qwen3.5 等万亿参数的混合专家（MoE）模型。该技术在推理时仅从 SSD 加载当前所需的专家权重，近期演示已在配备 96GB 内存的 M2 Max MacBook Pro 和 iPhone（0.6 token/秒）上实现推理。 这一突破大幅降低了运行前沿大语言模型的硬件门槛，使普通设备无需昂贵 GPU 或云端支持即可本地运行超大规模模型。它推动了私有化、离线和个性化 AI 应用在日常设备上的普及趋势。 该技术利用 MoE 模型的稀疏性——在万亿参数模型中，每个 token 仅激活约 170 亿至 320 亿参数——并从 SSD 即时将所需专家权重流式加载到内存中。尽管性能有限（如 0.6–1.7 token/秒），但已证明在内存≤128GB 的 iPhone 和 MacBook 等设备上具备可行性。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家（Mixture-of-Experts, MoE）是一种神经网络架构，其中路由机制会为每个输入 token 动态选择一部分专用的“专家”子网络进行处理，使模型能扩展至万亿参数规模，同时控制每 token 的计算量。与密集模型（dense model）不同，MoE 模型每次仅激活部分参数，理论上更高效，但如果所有专家都需驻留内存，仍会占用大量 RAM。“流式专家”技术通过按需从存储设备加载专家权重来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.co/posts/streaming-experts">Streaming experts</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Mixture-of-Experts`, `#Efficient Inference`, `#On-Device AI`, `#Research`

---

<a id="item-3"></a>
## [我国日均 AI 词元调用量两年激增超千倍](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 9.0/10

据国家数据局披露，我国日均 AI 词元调用量在 2026 年 3 月突破 140 万亿，较 2024 年初的 1000 亿增长超千倍。 这一爆发式增长标志着中国大模型基础设施与商业化进程加速，反映出 AI 与经济深度融合及数据要素市场化改革取得进展。词元正成为 AI 驱动的数据经济中定价、交易和衡量价值的基础单元。 词元是大语言模型处理文本的最小单位，中文平均约 1.5 个字对应 1 个词元。该指标统计全国 AI 生态中每日模型输入与输出的总词元量，可作为 AI 实际应用规模和算力需求的重要代理指标。

telegram · zaihuapd · Mar 24, 07:22

**背景**: 在基于 Transformer 架构的 AI 系统中，词元是模型处理的基本文本单元，可以是一个词、子词或标点符号，直接影响上下文长度、计算成本和计费方式。在中国政策语境下，词元正被官方定义为可计量、可定价、可交易的数据要素，成为国家数据要素市场建设的关键组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.ifeng.com/c/8rkw9XWfkkx">词元（Token）是什么意思？官方首次定义：AI数据要素与投资价值全解析</a></li>
<li><a href="https://www.runoob.com/ai-agent/token-intro.html">Token (词元) - 菜鸟教程</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2633960">聊聊 AI 的 token 到底是啥？-腾讯云开发者社区-腾讯云</a></li>

</ul>
</details>

**标签**: `#AI Adoption`, `#LLM`, `#Token Economy`, `#Data Infrastructure`, `#China AI`

---

<a id="item-4"></a>
## [Google 推出基于 Gemini 的暗网威胁情报 AI 代理](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 9.0/10

Google 在 Google Threat Intelligence 中推出了一个基于最新 Gemini 模型的 AI 代理公开预览版，该代理每天分析 800 万至 1000 万条暗网帖子，以识别数据泄露、内部威胁和初始访问中介活动等风险，准确率据称达 98%。 此举标志着大语言模型在现实网络安全运营中的重要应用进展，可自动化处理繁重的威胁情报任务，帮助安全团队更快应对新兴风险。同时也体现了 Google 将智能体 AI 深度融入企业安全工作流的战略方向。 该系统首先为客户构建组织画像，然后持续扫描暗网论坛以发现相关威胁。如在 RSAC 2026 上所述，它利用智能体能力（自主数据合成与工件初筛）减轻分析师的认知负担。

telegram · zaihuapd · Mar 24, 13:15

**背景**: 初始访问中介（Initial Access Brokers, IABs）是入侵网络后将访问权限出售给其他攻击者的网络犯罪分子，常为勒索软件攻击铺路。暗网论坛是交易被盗数据、凭证和系统访问权限的主要场所。传统威胁情报依赖人工监控这些来源，耗时且难以扩展。智能体 AI 系统利用大语言模型（LLM）从暗网帖子等非结构化数据中自主收集、分析并优先处理情报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/rsac-26-supercharging-agentic-ai-defense-with-frontline-threat-intelligence">RSAC ’26: Supercharging agentic AI defense with frontline threat intelligence | Google Cloud Blog</a></li>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cybersecuritynews.com/google-gemini-ai-dark-web/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to Detect Threats</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#Gemini`, `#LLM`, `#Threat Intelligence`

---

<a id="item-5"></a>
## [OpenAI 拟停用 Sora，转向 AI 智能体与 Spud 模型](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 9.0/10

OpenAI 计划停用其 AI 视频生成模型 Sora，关闭开发者 API，并逐步结束与迪士尼的合作。公司将资源重新分配至开发 AI 智能体和一款名为“Spud”的新模型。 此举标志着 OpenAI 的重大战略转向，在 Sora 高调发布仅数月后便放弃多模态视频生成。这预示着行业正从内容生成转向智能体系统和下一代基础模型（如 Spud），可能重塑生成式 AI 的发展重心。 Sora 的独立应用和 API 将被关闭，与迪士尼的合作也在逐步终止。OpenAI 同时重组安全团队，将其更紧密地融入核心开发流程，以支持 AI 智能体和 Spud 模型的研发。

telegram · zaihuapd · Mar 25, 00:30

**背景**: Sora 由 OpenAI 于 2024 年初发布，是一款先进的文本到视频生成 AI 模型，能根据提示生成高质量、长达一分钟的视频。AI 智能体指利用大语言模型进行规划、推理并使用工具或外部 API 执行多步骤任务的自主系统。新提及的“Spud”模型似乎是 OpenAI 下一代基础 AI 系统，但技术细节尚未公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theinformation.com/articles/openai-ceo-shifts-responsibilities-preps-spud-ai-model">OpenAI CEO Shifts Responsibilities, Preps ‘Spud’ AI Model</a></li>
<li><a href="https://www.tomsguide.com/ai/openai-just-killed-sora-as-company-readies-ipo-and-new-spud-model">OpenAI just killed Sora as company readies IPO and new 'Spud' model | Tom's Guide</a></li>
<li><a href="https://getstream.io/blog/openai-agents-sdk/">OpenAI Agents SDK — Getting Started</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#Sora`, `#OpenAI`, `#Generative AI`, `#AI Strategy`

---

<a id="item-6"></a>
## [Claude Code 推出内置安全审查的自动模式](https://claude.com/blog/auto-mode) ⭐️ 9.0/10

Claude Code 推出了“自动模式”，在任务执行中赋予 AI 自主决策能力，通过分类器实时审查每次工具调用，自动放行安全操作，并拦截批量删除文件或敏感数据外泄等高风险行为。 该功能在可用性与安全性之间取得关键平衡，大幅推进了自主 AI 智能体的实际部署——既减少人工审批打断，又防范危险操作，对企业在工作流中采用 LLM 驱动的自动化至关重要。 自动模式目前以研究预览形式向 Team 计划用户开放，即将扩展至 Enterprise 和 API 用户；支持 Claude Sonnet 4.6 与 Opus 4.6 模型，可能轻微增加 Token 消耗和延迟，尽管比 --dangerously-skip-permissions 参数更安全，仍建议在隔离环境中使用。

telegram · zaihuapd · Mar 25, 01:15

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，以其“宪法 AI”（Constitutional AI）训练方法著称，旨在使模型符合伦理与法律原则。Claude Code 是 Anthropic 面向开发者的界面，支持 AI 辅助编程和工具调用。新提及的 Sonnet 4.6 和 Opus 4.6 模型分别针对复杂多步工作流和长上下文推理进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Sonnet_46">Claude Sonnet 4.6</a></li>
<li><a href="https://grokipedia.com/page/Claude_Opus_46">Claude Opus 4.6</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-6">Introducing Claude Opus 4.6 - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Autonomous Agents`, `#LLM`, `#Claude`, `#Tool Use`

---

<a id="item-7"></a>
## [OpenAI 关停 Sora 视频生成应用](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 8.0/10

OpenAI 宣布关停其 Sora AI 视频生成应用，尽管就在前一天公司还发布了该平台的安全使用指南。这一决定是在有限公开发布后、面临内外对其用途和影响日益增长的质疑下做出的。 Sora 标志着生成式 AI 向动态媒体领域迈出的重要一步，对娱乐、虚假信息和创意表达均有深远影响。其突然关停引发了外界对 OpenAI 产品战略以及社会是否准备好应对大规模 AI 生成视频的质疑。 Sora 既是一个文本到视频的生成模型，也是一个独立的社交媒体应用，允许用户创建并分享简短的 AI 生成视频。尽管具备从文本或图像生成场景、扩展现有视频片段等技术能力，但据报道用户在初期新鲜感过后参与度迅速下降。

hackernews · mikeocool · Mar 24, 20:01

**背景**: Sora 是 OpenAI 开发的文本到视频生成模型，能够根据自然语言提示生成最长一分钟的逼真或富有想象力的视频片段。与 DALL·E 等图像生成器不同，Sora 需要处理帧间的时间连贯性，技术复杂度显著更高。它被定位为 OpenAI 向多模态 AI 系统拓展的重要一环，旨在理解和生成多种媒体形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to-video model) - Wikipedia</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/video-generation">Video generation with Sora | OpenAI API</a></li>
<li><a href="https://openai.com/sora?via=1bestai.tools">Sora</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：有人认为关停是抵制企业控制的成瘾性内容的积极举措，也有人惋惜失去了一款曾激发真实创造力和亲情互动的工具。还有批评者质疑决策时机，指出安全指南竟在关停前一日才发布。

**标签**: `#AI Video Generation`, `#Sora`, `#OpenAI`, `#Generative AI`, `#Ethics`

---

<a id="item-8"></a>
## [LiteLLM 1.82.7–1.82.8 版本遭供应链攻击](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 8.0/10

恶意代码被注入 PyPI 上的 LiteLLM 1.82.7 和 1.82.8 版本，包括 proxy_server.py 中的 base64 编码载荷和一个 litellm_init.pth 文件，该文件在安装包时即可触发凭证窃取。相关包已被 PyPI 隔离，此次事件与威胁组织 TeamPCP 有关。 此次供应链攻击对依赖 LiteLLM 进行大语言模型路由和代理的 AI 开发者构成严重威胁，因其可在无需显式导入的情况下执行任意代码并窃取凭证。这凸显了整个 AI 生态系统在开源依赖信任和 CI/CD 安全实践方面的系统性漏洞。 恶意载荷通过 .pth 文件在 Python 启动时激活，意味着仅安装该包即可触发感染。此外，proxy_server.py 中还遗留了被注释掉的早期载荷版本，暴露了攻击者的开发过程，属于操作安全失误。

hackernews · dot_treo · Mar 24, 12:06

**背景**: LiteLLM 是一个流行的开源库，为 OpenAI、Anthropic 及开源大语言模型（LLM）提供统一 API，广泛用于 AI 基础设施中的负载均衡、故障转移和成本优化。供应链攻击通过污染上游软件依赖注入恶意代码，从而危害所有下游用户。TeamPCP 是一个已知威胁组织，此前曾攻陷 Aqua Security 的 Trivy 扫描器和 Checkmarx 的 GitHub Actions。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.dreamfactory.com/the-litellm-supply-chain-attack-a-complete-technical-breakdown-of-what-happened-who-is-affected-and-what-comes-next">The LiteLLM Supply Chain Attack: A Complete Technical ...</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/malicious-litellm/">Malicious litellm_init.pth in litellm 1.82.8 — credential stealer</a></li>
<li><a href="https://www.endorlabs.com/learn/teampcp-isnt-done">TeamPCP Isn't Done: Threat Actor Behind Trivy and... | Endor Labs</a></li>

</ul>
</details>

**社区讨论**: 维护者确认此次泄露可能源于被攻陷的 CI/CD 工具（Trivy），并澄清使用 Docker 的用户因依赖版本锁定而未受影响。社区成员呼吁加强沙箱隔离、纵深防御和依赖管理，还有人分享了如蜜罐检测工具等解决方案。另有用户指出 GitHub 议题页面遭到大量垃圾评论刷屏。

**标签**: `#AI Security`, `#Supply Chain Attack`, `#LLM`, `#LiteLLM`, `#DevSecOps`

---

<a id="item-9"></a>
## [恶意 LiteLLM 包通过.pth 文件窃取凭证](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 8.0/10

PyPI 上的 LiteLLM Python 包 1.82.8 版本被植入恶意的 litellm_init.pth 文件，安装后无需导入即可自动执行凭证窃取载荷。1.82.7 版本也包含隐藏在 proxy_server.py 中的类似恶意代码。 此次供应链攻击针对广泛使用的 AI 编排库，可能危及数千个 AI 项目的开发者凭证、云密钥和加密货币钱包。它凸显了开源依赖信任机制和 CI/CD 安全实践中的严重漏洞。 该.pth 文件利用 Python 的 site-packages 初始化机制，在每次解释器启动时执行代码，窃取用户主目录下的 SSH 密钥、AWS/Azure 配置、Docker 凭证乃至加密货币钱包等敏感文件。攻击归因于 TeamPCP 组织，其很可能通过此前对 LiteLLM CI 中使用的 Trivy 安全扫描器的入侵获取了 PyPI 发布凭证。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一个开源 Python 库，为 100 多个大语言模型（LLM）提供统一接口，允许开发者使用 OpenAI API 格式在 OpenAI、Anthropic、AWS Bedrock 等提供商之间无缝切换。它被广泛应用于 AI 智能体框架和生产系统中。在 Python 中，若 site-packages 目录下的.pth 文件包含 import 语句，会在解释器启动时自动执行任意代码，这一机制常被供应链攻击所滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI ... Getting Started | liteLLM TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via ... Popular LiteLLM PyPI package compromised in TeamPCP supply ... LiteLLM on PyPI Was Compromised, What the Attack Changed and ... LiteLLM Supply Chain Attack: What Happened, Who’s Affected ...</a></li>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack : Malicious PyPI... | Wiz Blog</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Supply Chain Attack`, `#LLM`, `#LiteLLM`, `#Cybersecurity`

---

<a id="item-10"></a>
## [光象科技完成超亿元具身智能机器人融资](https://36kr.com/newsflashes/3737738833232132?f=rss) ⭐️ 8.0/10

工业具身智能企业光象科技已完成种子轮、天使轮及天使+轮多轮融资，累计金额超 1 亿元人民币。本轮融资由 IDG 资本与东方富海联合领投，埃夫特、零一创投等机器人产业资本跟投。 此次大额融资反映出资本市场对具身智能作为 AI 落地关键方向的高度认可，尤其在工业自动化领域。资金将推动具备环境交互能力的物理智能体加速从研发走向商业化应用。 融资资金将主要用于具身机器人的核心技术研发、产品化推进及商业化交付。投资方既包括顶级财务投资机构，也涵盖机器人产业资本，体现出技术潜力与市场可行性的双重认可。

rss · 36kr · Mar 25, 02:24

**背景**: 具身智能（Embodied AI）指通过传感器和执行器与物理世界交互的智能系统，能在真实或仿真环境中学习。与仅处理文本或图像的传统“离身智能”不同，具身智能使机器人能在动态环境中感知、推理并行动，对工业自动化、物流和服务机器人至关重要。近期大语言模型（LLM）与 ManiSkill3 等仿真平台的进展正加速该领域发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://scis.scichina.com/cn/2025/SSI-2025-0177.pdf">SCIENTIA SINICA</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202510031755113354_1.pdf">Survey on Embodied AI, Liu Yang, et.al》中国银河证券研究院</a></li>
<li><a href="https://36kr.com/p/2714495949771399">具 身 智 能 的月亮与六便士-36氪</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#AI Hardware`, `#Startup Funding`, `#Industrial AI`

---

<a id="item-11"></a>
## [英伟达借资金优势捆绑 AI 初创企业](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

自 2022 年以来，英伟达已向 OpenAI、CoreWeave 和 Reflection 等 AI 初创公司投入数十亿美元，同时扮演芯片供应商、投资者和贷款方三重角色。该公司还与 Groq 达成 200 亿美元授权协议并挖走其核心团队，引发美国参议员质疑此类交易是否规避反垄断审查。 这一策略通过将客户锁定在其生态系统中巩固了英伟达在 AI 基础设施领域的主导地位，引发对市场竞争减弱、AMD 等竞争对手面临更高壁垒以及 AI 硬件创新可能受阻的担忧。 英伟达的交易常采用灵活结构以规避正式并购审查，其投资帮助初创公司负担昂贵的 GPU 基础设施，使转向 AMD 或 Groq 的 LPU 等替代方案在经济上难以实现。Groq 芯片采用时序指令集计算机架构，拥有 220MB 片上存储且无需外部高带宽内存（HBM），提供了一种不同的 AI 加速路径。

telegram · zaihuapd · Mar 24, 03:02

**背景**: 英伟达凭借其 GPU 主导 AI 芯片市场，这些 GPU 是训练大语言模型的关键。AMD 等竞争对手虽提供替代硬件，但因英伟达成熟的 CUDA 软件生态和客户锁定效应而处于劣势。Groq 作为新入局者，开发了专为推理优化的语言处理单元（LPU），具备确定性延迟，其架构与 GPU 有本质不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://36kr.com/p/2660945964753667">AI芯片黑马Groq走红，英伟达又多了一个挑战者-36氪</a></li>
<li><a href="https://www.36kr.com/p/3205490522694146">AI圈的“资金循环”——英伟达和“亲儿子”CoreWeave的故事-36氪</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#NVIDIA`, `#Antitrust`, `#Startup Ecosystem`, `#Chip Industry`

---

<a id="item-12"></a>
## [阿里发布玄铁 C950 RISC-V CPU，集成 AI 加速器](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

阿里达摩院发布了玄铁 C950 高性能 RISC-V CPU，在 SPECint2006 单核测试中得分超 70 分，并集成自研 AI 加速引擎，可原生运行 Qwen3、DeepSeek V3 等千亿参数大模型。 这是 RISC-V CPU 首次原生支持大规模生成式 AI 模型，将开源硬件架构与前沿 AI 部署结合，有望重塑边缘和云端的 AI 推理基础设施。 该芯片最高主频达 3.2GHz，支持 RVA23 RISC-V 标准，采用“通用计算+AI 专用加速”融合架构，针对大模型推理任务进行硬件级优化。

telegram · zaihuapd · Mar 24, 06:01

**背景**: RISC-V 是一种开源指令集架构（ISA），因其模块化和可定制性，在 AI 和嵌入式领域日益受到关注，被视为 x86 和 ARM 等专有架构的替代方案。像 Qwen3 和 DeepSeek V3 这样的大语言模型通常依赖 GPU 或 NPU 等专用硬件进行高效推理，因此在 CPU 上实现原生支持是一项重要突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/玄铁C950/67526091">玄铁C950 - 百度百科</a></li>
<li><a href="https://www.xinhuanet.com/tech/20260324/fdc7c3b201074147a46b5ce6ad51045f/c.html">阿里达摩院发布RISC-V CPU玄铁C950，首次原生支持千亿参数大模型</a></li>
<li><a href="https://www.ithome.com/0/931/986.htm">全球性能最高 RISC-V CPU：阿里达摩院新一代旗舰处理器玄铁 C950 正式...</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#AI Hardware`, `#LLM`, `#Chip Design`, `#Generative AI`

---

<a id="item-13"></a>
## [包管理器引入依赖冷却期以提升安全性](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

包括 pnpm、Yarn、Bun、Deno、uv、pip 和 npm 在内的主流包管理器近期纷纷增加了依赖冷却功能，可延迟安装新发布的软件包。这一趋势因近期恶意 LiteLLM 供应链攻击事件而加速推进。 依赖冷却机制通过为社区留出时间检测恶意更新，防止其大规模传播，从而缓解供应链攻击——这对严重依赖开源包的 AI/ML 系统至关重要。这一转变标志着安全防护正被直接嵌入开发工具链中。 各工具实现方式不同：pnpm 使用 minimumReleaseAge 并支持按包豁免，npm 11.10.0 引入了 min-release-age，而 pip 26.0 仅通过 --uploaded-prior-to 支持绝对时间戳（相对时长需借助 cron 等变通方案）。大多数工具允许受信任的包绕过冷却期。

rss · Simon Willison · Mar 24, 21:11

**背景**: 供应链攻击指攻击者通过篡改合法软件依赖注入恶意代码。2026 年初的 LiteLLM 事件中，攻击者劫持了维护者账户，发布了带有后门的流行 AI 代理库版本。依赖冷却机制作为一种基于时间的过滤器，可降低自动拉取刚发布但可能被篡改的软件包的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://maier.tech/notes/pnpm-minimum-release-age">PNPM minimumReleaseAge</a></li>

</ul>
</details>

**标签**: `#Supply Chain Security`, `#Package Managers`, `#AI Infrastructure`, `#Software Engineering`, `#LiteLLM`

---

<a id="item-14"></a>
## [开源软件工厂结合 Claude Agent SDK 与 GitHub](https://www.v2ex.com/t/1200923#reply1) ⭐️ 7.0/10

一位开发者发布了一个开源“软件工厂”，利用 GitHub 和 Anthropic 的 Claude Agent SDK，自动从 issue 创建 pull request，并根据评审者反馈优化代码。 该项目展示了 AI 智能体在软件开发工作流中的实际应用，有望减少人工编码任务并加速开发者的迭代周期。 该系统使用 git worktree 为每个任务管理隔离的分支环境，并直接对接项目的 GitHub issue 和 PR。它利用 Claude Agent SDK（原用于驱动 Claude Code）进行代码生成与优化。

rss · V2EX · Mar 25, 02:19

**背景**: Claude Agent SDK 是 Anthropic 提供的官方工具包，允许开发者基于 Claude 模型构建自定义 AI 智能体，尤其适用于编程任务。Git worktree 是 Git 的一项功能，允许多个工作目录关联到同一仓库，便于并行开发而无需切换上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Agent_SDK_Python">Claude Agent SDK (Python)</a></li>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git-worktree Documentation</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#LLM`, `#Developer Tooling`, `#GitHub Automation`, `#Open Source`

---

<a id="item-15"></a>
## [Chaterm 周年庆：赠送 3 个月 Pro 会员](https://www.v2ex.com/t/1200919#reply0) ⭐️ 7.0/10

AI 原生终端 Chaterm 为庆祝上线一周年，推出免费 3 个月 Pro 会员活动。该工具现已支持 SSH/堡垒机资产管理、可复用的 AI Agent 技能、Kubernetes 上下文切换、SFTP 文件传输，以及自然语言驱动的命令执行等功能。 Chaterm 展示了大语言模型与 AI Agent 在 DevOps 工作流中的实际融合，使工程师能通过自然语言和自动化更高效地管理复杂的云基础设施。这体现了 AI 原生开发者工具的兴起趋势，旨在降低认知负担和运维摩擦。 Chaterm 支持跨设备云同步的资产管​​理、可审计的 AI Agent 工作流、上下文感知的命令推荐，以及用于公有云和 Kubernetes 集成的插件系统。用户可将常用运维流程封装为可共享的“Agent Skill”，供团队复用。

rss · V2EX · Mar 25, 02:09

**背景**: “AI 原生终端”指集成了大语言模型（LLM）的命令行界面，能理解自然语言、感知环境上下文，并根据用户意图执行或推荐命令。其中的 AI Agent 是能执行多步任务的自主或半自主模块，通常通过预定义的“技能”（Skills）来实现——这些技能是封装了领域知识或操作流程的可复用工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1939630380220145925">9 款终端 AI 编码工具横向对比：从 Claude Code 到 gROK CLI，谁能重...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1993287535472960620">Agent Skills 完全指南：让你的 AI Agent 拥有超能力</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2628286">AI Agent核心能力载体：Skills技能模块从基础到实战全指南</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#DevOps`, `#LLM`, `#Developer Tools`, `#Cloud Infrastructure`

---

<a id="item-16"></a>
## [AMD RDNA 4m 核显 GFX1171/GFX1172 现身，强化 AI 计算能力](https://www.ithome.com/0/932/374.htm) ⭐️ 7.0/10

AMD 在其开源 LLVM 代码栈中新增了两款基于 RDNA 4m 架构的集成显卡目标 GFX1171 和 GFX1172，均原生支持 FP8/BF8 数据格式和用于 AI 加速的 WMMA 矩阵指令。 这些升级表明 AMD 正积极布局移动端和边缘设备的片上 AI 计算能力，顺应了行业向硬件优化的低精度 AI 推理发展的趋势。 尽管 GFX1171 和 GFX1172 与 GFX1170 拥有相同的指令集（包括 FP8/BF8 和 WMMA），但可能在计算单元数量或频率上有所差异；RDNA 4m 并非完整的 RDNA 4 架构，而是基于 RDNA 3 的衍生版本，专为 Zen 6“Medusa Point”APU 设计。

rss · IT HOME · Mar 25, 02:09

**背景**: FP8 和 BF8 是 8 位浮点数据格式，可在保持 AI 推理任务可接受精度的同时显著降低内存带宽和功耗。WMMA（Wave Matrix Multiply Accumulate）是一种 GPU 指令集，通过专用硬件单元加速神经网络核心的矩阵运算，类似于 NVIDIA 的 Tensor Core。AMD 首次在 RDNA 3 架构中引入 WMMA 支持，以提升消费级硬件的 AI 性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gpuopen.cn/learn/wmma_on_rdna3/">如何使用 WMMA 加速 RDNA 3 上的 AI 应用 - AMD GPUOpen - GPUOpen 文...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1912129762048074069">大模型精度：FP32、TF32、FP16、BF16、FP8、FP4、NF4、INT8</a></li>
<li><a href="https://blog.aiking.net:888/archives/shen-ru-jie-xi-xian-dai-ai-ji-suan-zhong-de-shu-ju-lei-xing-fp16bf16int8fp8">深入解析现代ai计算中的数据类型fp16bf16int8fp8 - 爱擎思考</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#RDNA 4m`, `#GPU`, `#On-Device AI`, `#AMD`

---

<a id="item-17"></a>
## [天钡预热搭载锐龙 AI 9 HX 470 的 MACO470 迷你主机](https://www.ithome.com/0/932/371.htm) ⭐️ 7.0/10

天钡（AOOSTAR）宣布推出搭载 AMD 锐龙 AI 9 HX 470 处理器、32GB 内存和 1TB 存储的 MACO470 迷你主机，支持本地运行 OpenClaw，将于 4 月 1 日上市，售价 6XX9 元。 该设备通过支持本地运行 OpenClaw 等自主 AI 代理，体现了端侧 AI 推理的发展趋势，可降低对云服务的依赖并提升响应速度，对边缘 AI 应用具有重要意义。其紧凑机身集成高性能 AI 硬件，可能影响面向 AI 负载的迷你主机设计方向。 尽管锐龙 AI 9 HX 470 仅有 16 条原生 PCIe 通道，MACO470 却宣称配备三个 PCIe Gen4 ×4 M.2 SSD 插槽和一个外置 OCuLink 接口，这一扩展能力如何实现尚存疑问，涉及 PCIe 通道复用或带宽分配的技术细节。

rss · IT HOME · Mar 25, 02:01

**背景**: AMD 锐龙 AI 9 HX 470 是 2026 年发布的移动处理器，基于 Zen 5/Zen 5c 架构，拥有 12 核 24 线程，并集成 AI 加速功能。OpenClaw 是一个开源的自主 AI 代理，可通过大型语言模型在消息平台上执行任务。OCuLink 是由 PCI-SIG 开发的基于 PCIe 的外部连接标准，使用铜缆或光缆为 eGPU、NVMe 存储等设备提供高带宽、低延迟的连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/cpu-specs/ryzen-ai-9-hx-470.c4320">AMD Ryzen AI 9 HX 470 Specs | TechPowerUp CPU Database</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://www.howtogeek.com/what-is-oculink/">What is OCuLink? (And Why You Might Want It) - How-To Geek Oculink: The new interface for external graphics cards | PCWorld What Is OCuLink: A Beginner's Guide - optcore.net PCIe vs OCuLink : Choosing the Best Interface for Mini PCs ... OCuLink Interface - Delock What the heck is OcuLink and do I need to buy one? What Is OCuLink : A Beginner's Guide - optcore.net Which eGPU Interface Is Best? OCuLink , NVMe, or Thunderbolt? OCuLink Interface - Delock What Is OCuLink : A Beginner's Guide - optcore.net Which eGPU Interface Is Best? OCuLink, NVMe, or Thunderbolt?</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Edge AI`, `#Mini PC`, `#AMD Ryzen AI`, `#On-Device Inference`

---

<a id="item-18"></a>
## [亚马逊收购人形机器人初创公司 Fauna Robotics](https://www.ithome.com/0/932/352.htm) ⭐️ 7.0/10

亚马逊已收购总部位于纽约的初创公司 Fauna Robotics，该公司近期推出了售价 5 万美元、面向消费者的 Sprout 人形机器人，专为在人类环境中安全互动而设计。此次收购包括 Fauna 约 50 名员工加入亚马逊个人机器人部门，且收购后 Sprout 将继续向外部研究人员提供。 此次收购标志着亚马逊正战略性进军具身智能（embodied AI）和面向消费者的实体智能体，与科技巨头将人形机器人视为 AI 生态系统延伸的行业趋势一致。这也凸显了市场对用于家庭、学校和科研领域的社交互动型机器人的日益增长的商业兴趣。 Sprout 机器人基于 NVIDIA Jetson Orin 硬件平台，高约 107 厘米，支持自然语音交互，可执行挥手、击掌等动作，单次充电续航 3 小时。尽管被收购，Fauna 仍将向研究人员继续提供 Sprout 作为开发平台。

rss · IT HOME · Mar 25, 01:34

**背景**: 具身智能（Embodied AI）指通过机器人身体与物理世界互动的人工智能系统，需融合感知、推理与运动控制能力。像 Sprout 这样的人形机器人并非用于工业任务，而是专为社交和家庭环境设计，强调安全性、直观交互与适应性。近年来，AI 硬件（如 NVIDIA Jetson）和大语言模型的进步加速了此类平台的发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://faunarobotics.com/">Fauna Robotics | Capable, Safe, Fun Robots for Everyone</a></li>
<li><a href="https://apnews.com/article/amazon-humanoid-robot-fauna-sprout-f51ced4a097b1af56b0b2561cdca8fef">Amazon buys Fauna Robotics, maker of the Sprout humanoid robot</a></li>
<li><a href="https://www.cnbc.com/2026/03/24/amazon-humanoid-maker-fauna-robotics-sprout.html">Amazon acquires 'approachable' humanoid maker Fauna Robotics HUMANOID ROBOTICS | Amazon Acquires Fauna Robotics to Advance ... Amazon acquires humanoid developer Fauna Robotics - The Robot ... Amazon Acquires Fauna Robotics, Entering Consumer Humanoid ... Fauna Robotics Unveils Sprout, a Humanoid Platform Built for ...</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#AI Hardware`, `#Embodied AI`, `#Corporate Strategy`, `#Humanoid Robots`

---

<a id="item-19"></a>
## [中国刷新光通信纪录：2.5 Pb/s 实时光传输](https://www.ithome.com/0/932/351.htm) ⭐️ 7.0/10

中国信科集团、鹏城实验室与烽火藤仓光纤科技有限公司联合实现 2.5 Pb/s（每秒 2.5 拍比特）的 24 芯单模光纤实时双向光传输，创下世界新纪录。该成果已被国际顶级光通信会议 OFC 2026 评为“高分论文”，并受邀在 SCI 期刊发表专题文章。 该突破为人工智能大模型训练和超大规模数据中心提供了关键的高带宽传输能力，有效缓解了传统光纤逼近容量极限的瓶颈。通过融合空分复用与多波段技术，验证了下一代光通信系统在工程落地上的可行性，对 AI 基础设施发展具有重要意义。 系统采用 24 芯光纤，覆盖 S+C+L 三波段（总带宽 19.65 THz），通过 262 个波分复用信道与 24 个纤芯组合形成 6288 个并行通道，并使用商用 S+C+L 一体化 400G 相干光模块（基于 64GBaud PDM-16QAM）。通过优化双向传输时的纤芯分配机制，在无需复杂 MIMO 处理的情况下有效抑制串扰，实现稳定运行。

rss · IT HOME · Mar 25, 01:32

**背景**: 传统单模光纤因非线性效应和带宽限制正逼近容量极限。空分复用（SDM）技术通过在空间维度增加传输通道来提升容量，典型实现包括多芯光纤（单根光纤包层内含多个纤芯）和少模光纤。同时，将光通信波段从传统的 C 波段扩展至 S 波段和 L 波段，可大幅增加可用光谱带宽，从而显著提升总传输速率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/空分复用技术/22291444">空分复用技术_百度百科</a></li>
<li><a href="https://www.cww.net.cn/article?id=608288">光全重实验室最新成果—《基于24芯单模光纤S+C+L波段实时双向2.5 Pb/s...</a></li>
<li><a href="https://baike.baidu.com/item/多芯光纤传输系统/67443166">多芯光纤传输系统_百度百科</a></li>

</ul>
</details>

**标签**: `#Optical Communication`, `#AI Infrastructure`, `#Networking`, `#Research`, `#Data Transmission`

---