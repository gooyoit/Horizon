---
layout: default
title: "Horizon Summary: 2026-05-27 (ZH)"
date: 2026-05-27
lang: zh
---

> From 107 items, 15 important content pieces were selected

---

1. [Qwen3.7-Max 在 Code Arena 排名第四，与 Claude Opus 4.6 持平](#item-1) ⭐️ 9.0/10
2. [Anthropic 的三层防御架构：AI 智能体安全工程实践总结](#item-2) ⭐️ 9.0/10
3. [微软发布终端原生 Web Agent 框架：Webwright](#item-3) ⭐️ 9.0/10
4. [SGLang v0.5.12.post1 修复 12 个 DeepSeek V4 关键 Bug](#item-4) ⭐️ 8.0/10
5. [Microsoft Copilot Cowork 存在提示注入数据泄露漏洞](#item-5) ⭐️ 8.0/10
6. [Claude Code 新插件 security-guidance：一个写代码，另一个独立的 Claude 实例审查](#item-6) ⭐️ 8.0/10
7. [高通与字节跳动达成 AI ASIC 芯片合作，采购量达数百万颗](#item-7) ⭐️ 8.0/10
8. [Anthropic 在 Code w/ Claude 伦敦活动发布自托管沙箱与 MCP 隧道](#item-8) ⭐️ 8.0/10
9. [Bonsai Studio：iPhone 端侧离线 AI 图像生成应用上线](#item-9) ⭐️ 8.0/10
10. [SkillOpt 框架实现 AI 技能迭代自我进化](#item-10) ⭐️ 8.0/10
11. [法律专家用 Codex 将 50 州法律研究从一周缩短至两小时](#item-11) ⭐️ 8.0/10
12. [蔚来 ES9 首发全新世界模型，实现端到端智驾直接控车](#item-12) ⭐️ 8.0/10
13. [🤖 马斯克称 xAI 将于年底前开源 0.5T 参数模型，外界推测或为 Grok 4.2](#item-13) ⭐️ 8.0/10
14. [中国审查 Meta 收购 Manus，联合创始人被限制出境](#item-14) ⭐️ 8.0/10
15. [MiniCPM5-1B 为紧凑型边缘 AI 模型创下新 SOTA](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen3.7-Max 在 Code Arena 排名第四，与 Claude Opus 4.6 持平](https://x.com/Alibaba_Qwen/status/2059445345667747849) ⭐️ 9.0/10

阿里巴巴的 Qwen3.7-Max 在 Code Arena 排行榜上攀升至第四名，与 Anthropic 的 Claude Opus 4.6 持平，成为该榜单上排名最高的中国 AI 实验室模型。 这一排名表明，在竞争激烈的编码大模型领域，中国 AI 实验室正在缩小与西方领先 AI 公司的差距，预示着前沿 AI 能力正在走向更加均衡的格局。 Qwen3.7-Max 是阿里巴巴 Qwen3.7 系列的旗舰模型，拥有 100 万 token 的上下文窗口，专为智能体工作负载设计，在编码和长达 35 小时的长期自主执行方面表现尤为突出。

rss · AI Hot · May 27, 01:23

**背景**: Code Arena 是托管在 LMArena（arena.ai）上的社区驱动排行榜，通过用户真实评估对 AI 模型进行排名，涵盖语言、图像和代码生成任务。Qwen 系列是阿里巴巴云的大语言模型家族，在各基准测试中持续进步。Claude Opus 4.6 是 Anthropic 最强大的模型，在写作、长上下文连贯性和指令遵循任务中表现出色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3.7-max">Qwen3.7 Max - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.marktechpost.com/2026/05/21/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/">Qwen Introduces Qwen3.7-Max: A Reasoning Agent Model With a 1M-Token Context Window - MarkTechPost</a></li>
<li><a href="https://arena.ai/">Arena AI: The Official AI Ranking & LLM Leaderboard</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Code Generation`, `#LLM Benchmarks`, `#Qwen`, `#Frontier AI`

---

<a id="item-2"></a>
## [Anthropic 的三层防御架构：AI 智能体安全工程实践总结](https://x.com/shao__meng/status/2059442456819839447) ⭐️ 9.0/10

Anthropic 系统发布了其在 Claude AI、Claude Code 和 Claude Cowork 三款旗舰产品上构建安全 AI 智能体的工程实践总结，详述了环境层、模型层和外部内容层三层防御架构，以及各产品对应的沙箱隔离模式。报告还披露了量化红队基准数据，例如 Claude Opus 4.7 在 Gray Swan Agent 基准上单次攻击成功率约 0.1%，Claude Code 自动模式拦截约 83% 的过度积极行为。 这份总结罕见地揭示了一家头部 AI 实验室在生产系统中实际工程化智能体安全的具体做法，为整个行业应对智能体 AI 部署风险提供了可操作的蓝图。其量化基准数据和真实攻击案例研究树立了新的透明度标杆，可能影响其他 AI 公司披露安全工程实践的方式。 每款产品根据其风险特征采用不同的隔离模型：Claude AI 使用短暂容器，Claude Code 采用人机协同沙盒，Claude Cowork 则部署密封虚拟机。报告强调出站阻断等环境层防御至关重要，并通过真实攻击案例证明即使模型层防御失效，沙箱边界仍能有效遏制损害。

rss · AI Hot · May 27, 01:11

**背景**: AI 智能体与普通聊天机器人的区别在于它们能自主执行操作，如编写代码、修改文件和发起网络调用，这大大扩展了攻击面。沙箱是一种核心安全策略，将智能体限制在权限有限的隔离环境中，防止被攻破或行为异常的智能体影响宿主系统。Gray Swan Agent 红队（ART）基准是一个实证基准，旨在系统评估 LLM 驱动的智能体在真实部署场景中对抗对抗性滥用的安全鲁棒性。Anthropic 的宪法 AI 训练方法及其对安全对齐的重视提供了模型层基础，而环境层和外部内容层则增加了纵深防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://commercetracks.com/anthropic-vs-openai-red-teaming-methods-reveal-different-security-priorities-for-enterprise-ai/">Anthropic vs. OpenAI red teaming methods reveal different security...</a></li>
<li><a href="https://www.emergentmind.com/topics/agent-red-teaming-art-benchmark">Agent Red Teaming Benchmark</a></li>
<li><a href="https://pub.towardsai.net/ai-agent-sandbox-architecture-how-to-let-agents-run-code-without-letting-them-run-everything-63a9293c35fb">AI Agent Sandbox Architecture: How to Let Agents Run... | Towards AI</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Agents`, `#Anthropic`, `#Red Teaming`, `#Agentic Architecture`

---

<a id="item-3"></a>
## [微软发布终端原生 Web Agent 框架：Webwright](https://x.com/shao__meng/status/2059435625552785617) ⭐️ 9.0/10

Microsoft open-sourced Webwright, a highly performant terminal-native Web Agent framework that uses an innovative 'code-as-action' approach to have LLMs write reusable Playwright scripts, achieving new state-of-the-art results on long-range web tasks.

rss · AI Hot · May 27, 00:44

**标签**: `#AI Agents`, `#Web Automation`, `#Microsoft Research`, `#LLMs`, `#Open Source`

---

<a id="item-4"></a>
## [SGLang v0.5.12.post1 修复 12 个 DeepSeek V4 关键 Bug](https://github.com/sgl-project/sglang/releases/tag/v0.5.12.post1) ⭐️ 8.0/10

SGLang 发布了 v0.5.12.post1 稳定性补丁，精选了 12 个关键 Bug 修复，主要针对 DeepSeek V4 的推理、分离式部署和精度问题。值得注意的修复包括解决 B200/B300 GPU 上的乱码输出问题、将 GSM8K 精度从 0.825 恢复到 0.960，以及消除启动时 20-40 秒的冷桶前向停滞。 该补丁对于任何在 SGLang 上运行 DeepSeek V4 的生产部署都至关重要，SGLang 已成为事实上的行业标准服务框架，在全球超过 40 万个 GPU 上运行。这些修复直接解决了下一代 NVIDIA 硬件（B200/B300）上的稳定性和正确性问题，并恢复了关键的推理精度，使这一万亿参数模型的大规模可靠部署成为可能。 关键技术修复包括修正 B200/B300 上 `deep_gemm` UE8M0 缩放打包路径、解决回收 KV 页面中过时的滑动窗口映射（该问题导致约 2000 个请求时崩溃），以及修复 FlashInfer mxfp4 虚拟加载时 `HashTopK.tid2eid` 查找表未初始化的问题。该补丁还通过 `nvidia-cutlass-dsl` 的 `[cu13]` 扩展添加了 CUDA 13 支持，这是 sm_103/B300 GPU 所必需的。

github · sgl-project/sglang · May 26, 23:58

**背景**: SGLang 是一个由 UC Berkeley 开发、托管在 LMSYS 下的高性能开源 LLM 服务框架，专为生产规模的高吞吐、低延迟推理而设计。DeepSeek V4 是新发布的前沿开源模型，拥有约 1 万亿参数，采用 NSA（原生稀疏注意力）、HiSparse（分层稀疏注意力）和 Engram 记忆架构等先进架构。PD（预填充-解码）分离是一种推理优化技术，将并行处理整个输入序列以构建 KV 缓存的预填充阶段与逐个自回归生成 token 的解码阶段分开，使每个阶段可以在不同的硬件实例上独立优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">sgl-project/ sglang : SGLang is a high-performance serving framework ...</a></li>
<li><a href="https://docs.sglang.io/docs/advanced_features/hisparse_guide">HiSparse : Hierarchical Sparse Attention - SGLang Documentation</a></li>
<li><a href="https://www.bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill - decode disaggregation | LLM Inference Handbook</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#DeepSeek V4`, `#SGLang`, `#LLM Serving`, `#Inference`

---

<a id="item-5"></a>
## [Microsoft Copilot Cowork 存在提示注入数据泄露漏洞](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

PromptArmor 的安全研究人员发现，Microsoft Copilot Cowork 存在提示注入攻击漏洞，攻击者可利用该漏洞让 AI 代理向用户自己的收件箱发送包含外部图片链接的电子邮件，从而泄露私有文件。由于该代理被允许在未经用户批准的情况下发送邮件，且这些消息会自动渲染外部图片，攻击者可以窃取 OneDrive 预认证下载链接并访问私有文件。 该漏洞凸显了在企业环境中安全部署代理式 AI 系统这一根本性未解难题——这些代理可以访问敏感的企业数据，并能执行发送邮件等真实操作。随着微软等主要厂商快速将代理式 AI 功能深度集成到生产力套件中，此类提示注入风险可能使数百万企业用户面临数据被盗的威胁。 该攻击利用了 Simon Willison 所称的"致命三要素"——即一个代理系统同时具备访问私有数据的能力、容易受到提示注入攻击、以及能够通过发送包含外部图片引用的邮件等出站操作泄露数据。OneDrive 的预认证下载链接使数据泄露尤为危险，因为单个泄露的 URL 即可让攻击者无需进一步认证就能完全访问文件。

rss · Simon Willison · May 26, 15:36

**背景**: Microsoft Copilot Cowork 是微软与 Anthropic 合作开发的、内置于 Microsoft 365 的新 AI 自动化层，目前正向早期访问用户推出。提示注入是一类攻击方式，攻击者将恶意指令隐藏在外部内容（如文档或网页）中，使基于大语言模型的系统执行非预期操作。在代理式 AI 架构中，这种风险被进一步放大，因为代理可以将多个操作串联起来——一条注入的指令就能触发一系列导致真实数据泄露的操作，打破了传统安全假设中只有人类才会发起敏感操作的前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/03/09/microsoft-copilot-cowork-ai-agents-anthropic-e7-m365-saas/">Microsoft debuts Copilot Cowork built with Anthropic’s help... | Fortune</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-ai-security-key-risks-secure-architecture-controls-vycec">Agentic AI Security : Key Risks , Secure Architecture, and Controls...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论反映出人们对代理式 AI 系统防范提示注入的持续困难深感担忧，许多评论者指出这类漏洞在根本上仍未被解决。多位参与者强调，在解决这些安全问题之前就推出具有广泛权限的自主 AI 代理，对企业客户构成了重大风险。

**标签**: `#AI Security`, `#Prompt Injection`, `#Microsoft Copilot`, `#Agentic AI`, `#Data Exfiltration`

---

<a id="item-6"></a>
## [Claude Code 新插件 security-guidance：一个写代码，另一个独立的 Claude 实例审查](https://x.com/frxiaobei/status/2059444190808039451) ⭐️ 8.0/10

Claude Code released a new open-source plugin called security-guidance that uses two isolated Claude instances—one to write code and another to independently review it across three layers—to catch security blind spots without blocking the development workflow.

rss · AI Hot · May 27, 01:18

**标签**: `#Claude Code`, `#AI Agents`, `#Code Security`, `#Multi-Agent Systems`, `#Developer Tools`

---

<a id="item-7"></a>
## [高通与字节跳动达成 AI ASIC 芯片合作，采购量达数百万颗](https://www.ithome.com/0/955/674.htm) ⭐️ 8.0/10

据报道，高通与字节跳动已就 AI ASIC 芯片达成合作关系，字节跳动计划采购数百万颗该芯片，以支撑其 AI 基础设施建设。 这一合作标志着 AI 芯片供应格局的重大变化，字节跳动作为领先的 AI 公司，正在从依赖 NVIDIA GPU 转向定制化 ASIC 方案，以获得更好的成本效益和性能表现。这也标志着高通在 AI 数据中心芯片市场的重要布局，加剧了芯片厂商之间争夺 AI 算力主导权的竞争。 据报道，采购规模达到数百万颗级别，表明这是一次大规模部署而非试运行。这些芯片专门设计为 ASIC（专用集成电路），意味着它们是为 AI 工作负载量身定制的，而非通用计算芯片。

rss · AI Hot · May 27, 01:12

**背景**: AI ASIC 芯片，即专用集成电路，是专门为加速机器学习和深度学习推理等人工智能任务而设计的硬件。与通用 GPU 不同，ASIC 是针对特定工作负载定制设计的，在目标 AI 应用中具有能效、成本和性能方面的优势。AI ASIC 芯片市场正因 AI 密集型应用对高性能、低延迟处理的需求不断增长而强劲增长，各大科技公司越来越多地开发或采购定制芯片，以减少对第三方 GPU 供应商的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/deep-dive-ai-asic-chips-market-itstrends-segmentation-0bhaf">Deep Dive into the AI ASIC Chips Market: ItsTrends, Market...</a></li>
<li><a href="https://www.credenceresearch.com/report/ai-asic-chip-market">AI ASIC Chip Market Size, Share, Growth and Forecast 2032</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Qualcomm`, `#ByteDance`, `#ASIC`, `#AI Infrastructure`

---

<a id="item-8"></a>
## [Anthropic 在 Code w/ Claude 伦敦活动发布自托管沙箱与 MCP 隧道](https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build) ⭐️ 8.0/10

在 Code w/ Claude 伦敦活动上，Anthropic 为 Claude Managed Agents 推出了两项新能力：自托管沙箱（公开测试版）和 MCP 隧道（研究预览）。这些功能使企业能够完全在自己的基础设施或指定托管服务商上运行 AI 智能体的工具执行环境，并连接到私有 MCP 服务器。 这些基础设施更新在安全的企业级 AI 智能体部署方面迈出了重要一步，使组织能够完全控制智能体代码的执行位置和方式。这解决了企业在数据主权、合规性和网络安全方面的核心关切，而这些关切一直是受监管行业中 AI 智能体采用的主要障碍。 自托管沙箱已进入公开测试阶段，而 MCP 隧道则以研究预览形式发布，表明后者仍处于实验阶段。目前已有 Spotify、Base44 和 Legora 等早期用户在使用这些新功能，活动还介绍了通过 Claude Code、优化思维预算和模型努力级别来提升开发体验。

rss · AI Hot · May 27, 01:04

**背景**: Claude Managed Agents 是 Anthropic 的全托管智能体平台，它将 AI 智能体的组件（包括会话、执行框架和沙箱）虚拟化，使开发者无需管理底层基础设施即可构建和部署智能体。MCP（模型上下文协议）是 Anthropic 推出的开放协议，使 AI 模型能够安全地连接外部工具和数据源。此前，Managed Agents 完全运行在 Anthropic 的云端，这限制了因监管或安全要求而需要本地执行的企业采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/">Anthropic debuts MCP tunnels and self-hosted... - The New Stack</a></li>
<li><a href="https://www.anthropic.com/engineering/managed-agents">Scaling Managed Agents : Decoupling the brain from the hands</a></li>
<li><a href="https://mer.vin/2026/05/claude-managed-agents-self-hosted-sandboxes-and-private-mcp-tunnels/">Claude Managed Agents: Self-Hosted Sandboxes and Private MCP ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Agents`, `#Enterprise AI`, `#MCP`, `#Developer Tools`

---

<a id="item-9"></a>
## [Bonsai Studio：iPhone 端侧离线 AI 图像生成应用上线](https://x.com/berryxia/status/2059436904215621723) ⭐️ 8.0/10

PrismML 发布了免费 iOS 应用 Bonsai Studio，用户可在 iPhone 15 Pro 及以上机型上完全离线运行 Bonsai Image 4B 扩散模型。该模型的 1-bit 压缩版仅占 0.93GB 存储空间，比全精度版小 8.3 倍，生成 512×512 图像耗时约几十秒，内存占用约 1.5GB。 这标志着端侧 AI 的一个重要里程碑，证明了十亿参数级的扩散模型可以通过极致压缩部署在消费级智能手机上，无需云端连接。它预示着强大的生成式 AI 能力将在移动设备上普及，同时具备更好的隐私保护和零网络延迟。 Bonsai Image 4B 模型基于 FLUX.2 Klein 构建，采用 1-bit 和三值权重量化技术大幅缩减 transformer 权重占用，以适配本地部署。应用支持多种艺术风格，但中文文字生成目前会出现乱码，Android 用户可通过 WebGPU 网页版体验该模型。

rss · AI Hot · May 27, 00:49

**背景**: FLUX.2 Klein 是由 Black Forest Labs 开发的高效图像生成模型系列，提供 4B 和 9B 参数版本，专为快速、高质量的扩散推理而设计。1-bit 量化是一种激进的模型压缩技术，将神经网络权重缩减为二值（或三值）表示——通常为-1、0 和+1——从而将模型大小从数 GB 压缩到 1GB 以下，同时尽量保持可用的输出质量。该方法借鉴了 BitNet 等研究成果，后者证明了大型语言模型可以被压缩到极低位宽，并在本地硬件上有效运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-image-4b">PrismML — Introducing 1-bit and Ternary Bonsai Image 4 B : Image ...</a></li>
<li><a href="https://bfl.ai/models/flux-2-klein">FLUX . 2 [ klein ] - Fast, Efficient Image Generation | Black Forest Labs</a></li>
<li><a href="https://digg.com/ai/cyontmtp">PrismML releases Bonsai Image 4 B , a 930 MB 1-bit diffusion...</a></li>

</ul>
</details>

**标签**: `#Edge AI`, `#On-device Inference`, `#Image Generation`, `#Model Compression`, `#Mobile AI`

---

<a id="item-10"></a>
## [SkillOpt 框架实现 AI 技能迭代自我进化](https://x.com/dotey/status/2059434459783389397) ⭐️ 8.0/10

微软及合作研究机构提出了 SkillOpt 框架，通过要求每次编辑必须在验证集上取得可衡量的得分提升才能合并，从而让 AI 迭代式地自我进化和优化技能。在实验中，该方法将 GPT-4o 的直接对话准确率提升了 23.5 分。 该框架代表了自动化提示词工程和 AI 自我改进领域的重要进展，模糊了提示词工程与传统模型训练之间的界限。它提供了一种将 Skill 作为外部状态进行系统性"训练"的方法论，可能对大规模 AI 智能体的开发和优化产生深远影响。 SkillOpt 的核心机制要求每次提出的编辑必须在验证集上证明得分提升后才能合并，并且该框架引入了学习率预算来控制优化过程。只有具备明确、可程序自动验收标准的 Skill（例如代码性能优化）才能有效地进行这种自我进化。

rss · AI Hot · May 27, 00:40

**背景**: 提示词优化是一个新兴的研究领域，超越了基础提示词工程，涵盖了基于梯度的提示词优化和进化方法等技术，用于自动提升 LLM 的性能。近期的研究探索了提示词优化与传统机器学习概念（如学习率预算和多臂老虎机）之间的联系，将提示词视为可训练的组件而非静态指令。Skill——即 AI 智能体的模块化、可复用能力——作为一种从模型外部结构化和管理复杂 AI 行为的方式，已经获得了广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://papers.nips.cc/paper_files/paper/2024/file/b46bc1449205888e1883f692aff1a252-Paper-Conference.pdf">Efficient Prompt Optimization Through the Lens of</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Prompt Engineering`, `#Automated Optimization`, `#LLM Research`, `#Microsoft Research`

---

<a id="item-11"></a>
## [法律专家用 Codex 将 50 州法律研究从一周缩短至两小时](https://x.com/emollick/status/2059431958447317381) ⭐️ 8.0/10

一位法律专家演示了通过 OpenAI 的 Codex 搭建覆盖美国 50 个州的法律研究工作流，将过去需要律师助理团队耗时一周、成本约 15 万至 30 万美元的任务，缩减至仅需约两小时且成本极低。该案例由知名 AI 生产力研究学者 Ethan Mollick 分享，强调如今是领域专家而非外行在验证 AI 在实际应用中被严重低估的能力。 这一案例标志着高风险专业服务的范式转变，表明 Codex 等 AI 代理已不再是实验性工具，而是能够变革知识密集型行业的生产级系统。成本和时间的急剧下降可能从根本上重塑法律研究的人员配置、定价和交付方式，并对咨询、合规及其他专家驱动的行业产生连锁反应。 该工作流基于 Codex API 搭建，OpenAI 自 2025 年初起便将 Codex 定位为超越纯软件开发任务的更广泛的企业级代理平台。截至 2026 年 3 月，Codex 的周活跃用户已超过 200 万，显示出其在法律、安全和研究等多种企业用例中的快速普及。

rss · AI Hot · May 27, 00:30

**背景**: OpenAI 的 Codex 最初于 2025 年 4 月作为面向软件工程任务的 AI 编码代理发布，可通过 ChatGPT 网页应用、CLI 工具、桌面应用程序和 IDE 集成使用。跨司法管辖区的法律研究——即比较美国全部 50 个州的法律、法规和判例——传统上是法律实践中最耗费人力和成本最高的工作之一，通常需要大型团队手动调查各州分散的数据库和如 CourtListener、康奈尔法律信息研究所等来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent)</a></li>
<li><a href="https://grokipedia.com/page/Multi-jurisdictional_Legal_Research_Platforms">Multi-jurisdictional Legal Research Platforms</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Applied AI`, `#OpenAI Codex`, `#Legal Tech`, `#Productivity`

---

<a id="item-12"></a>
## [蔚来 ES9 首发全新世界模型，实现端到端智驾直接控车](https://www.ithome.com/0/955/695.htm) ⭐️ 8.0/10

蔚来宣布其旗舰 ES9 行政 SUV 将首发全新版本的世界模型智能辅助驾驶系统，并将于 2026 年 6 月同步推送至 Banyan、Cedar、Cedar S 系统的全量车型。该版本是国内首个直接操作方向盘与踏板的智驾系统，采用完整的「世界模型+监督微调+闭环强化学习」三层训练框架，并首次实现车企自研系统对天空路牌的实时识别。 这标志着自动驾驶领域具身智能的重大技术突破，跳过传统轨迹规划直接控制车辆执行器，可降低延迟并实现更拟人的精准控车。此次更新覆盖从 2022 年到 2026 年购买的数十万辆不同车型，也体现了蔚来在智能驾驶体验平权方面的努力。 在 2026 年 1 月推送「世界模型+闭环强化学习」架构版本后的 3 个月内，蔚来用户城区领航辅助的使用里程和时长环比分别提升了 92%和 116%。新版本还通过重构传感器信息表征方式，在不依赖高精地图的前提下首次实现了对潮汐车道和可变车道天空路牌的实时识别与理解。

rss · IT HOME · May 27, 01:57

**背景**: 传统的智能辅助驾驶系统采用模块化架构，先由规划模块生成候选轨迹，再将其「翻译」为方向盘和踏板的操作指令。端到端自动驾驶旨在用单一神经网络直接将传感器输入映射为车辆控制动作，有望实现更低延迟和更自然的驾驶行为。世界模型通过学习物理世界的内部表征，使驾驶系统能够预测结果并对未来场景进行推理。强化学习尤其是闭环强化学习，通过与模拟或真实环境的试错交互来训练模型，帮助系统应对人类示范数据难以覆盖的罕见和极端场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2511.20325">AD-R1: Closed - Loop Reinforcement Learning for... | alphaXiv</a></li>
<li><a href="https://deeplearn.org/arxiv/676484/ad-r1:-closed-loop-reinforcement-learning-for-end-to-end-autonomous-driving-with-impartial-world-models">AD-R1: Closed - Loop Reinforcement Learning for End-to-End...</a></li>

</ul>
</details>

**标签**: `#Autonomous Driving`, `#World Model`, `#End-to-End AI`, `#Reinforcement Learning`, `#NIO`

---

<a id="item-13"></a>
## [🤖 马斯克称 xAI 将于年底前开源 0.5T 参数模型，外界推测或为 Grok 4.2](https://x.com/i/status/2058796067592736866) ⭐️ 8.0/10

Elon Musk announced that xAI will open-source a 0.5T parameter model by the end of the year, which outside sources speculate could be the Grok 4.2 base model.

telegram · @zaihuapd · May 26, 02:46

**标签**: `#xAI`, `#Open-Source AI`, `#Grok`, `#Frontier Models`, `#Elon Musk`

---

<a id="item-14"></a>
## [中国审查 Meta 收购 Manus，联合创始人被限制出境](https://t.me/zaihuapd/41577) ⭐️ 8.0/10

中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。审查期间，Manus 首席执行官肖弘和首席科学家季逸超本月在北京与国家发展和改革委员会会面后，已被限制出境，但可在中国境内自由出行。 此事件凸显了跨境 AI 收购日益增长的监管复杂性，尤其是当美国科技巨头试图吸纳中国 AI 人才和技术时。对创始人的出境限制表明，中国监管部门正在对涉及 AI 技术的对外投资和技术转让采取更加强硬的立场。 Meta 于去年 12 月宣布收购开发通用型 AI 智能体的 Manus，交易金额未公开。路透此前曾援引消息人士报道过该交易的估值，但具体数字仍未披露。

telegram · @zaihuapd · May 26, 09:56

**背景**: Manus 是一家专注于开发通用型 AI 智能体的初创公司，其 AI 智能体能够自主执行复杂任务。近年来，中国通过对外投资和技术转让等监管框架，持续加强对跨境技术交易的审查，尤其是在 AI 等战略领域。国家发展和改革委员会（发改委）是负责审查此类交易的关键机构之一。

**标签**: `#AI Industry`, `#Meta`, `#Manus`, `#AI Regulation`, `#Mergers and Acquisitions`

---

<a id="item-15"></a>
## [MiniCPM5-1B 为紧凑型边缘 AI 模型创下新 SOTA](https://www.producthunt.com/products/minicpm-4-0) ⭐️ 8.0/10

MiniCPM5-1B 是一个新发布的开源 AI 模型，拥有约 10 亿参数，声称在同等规模的模型中达到了最先进的性能。该模型专门针对边缘计算和端侧部署进行了优化，推动了小型语言模型能力的前沿。 用 10 亿参数模型达到 SOTA 结果证明了高性能 AI 可以在消费级硬件上高效运行，而无需依赖云基础设施。这一进展降低了开发者在移动和物联网设备上构建注重隐私、低延迟 AI 应用的门槛。 MiniCPM5-1B 属于知名的 MiniCPM 系列，该系列在边缘 AI 社区中因提供可靠、高效的小型语言模型而享有良好声誉。该模型完全开源，使研究人员和开发者能够自由检查、微调并在各种硬件环境中部署它。

producthunt · Zac Zuo · May 26, 03:07

**背景**: 边缘 AI 是指在智能手机、平板电脑和嵌入式系统等本地设备上直接运行人工智能模型，而不是依赖远程云服务器。拥有约 10 亿参数的小型语言模型（SLM）在这一用例中尤为重要，因为它们能够适应边缘硬件的内存和计算限制，同时仍能提供有意义的智能能力。由中国研究人员开发的 MiniCPM 系列一直是该领域的领先项目，持续发布性能超出其参数规模预期的紧凑型模型。在这一规模上达到最先进（SOTA）性能意味着该模型在同等或更小规模模型的标准基准测试中超越了所有先前发布的结果。

**标签**: `#AI`, `#Open Source`, `#Edge AI`, `#Small Language Models`, `#Machine Learning`

---