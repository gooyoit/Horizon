---
layout: default
title: "Horizon Summary: 2026-04-17 (ZH)"
date: 2026-04-17
lang: zh
---

> From 86 items, 29 important content pieces were selected

---

1. [Anthropic 发布 Claude Opus 4.6，支持 200K 上下文和自适应思考](#item-1) ⭐️ 10.0/10
2. [Anthropic 发布 Claude Opus 4.7，带来多项重大更新](#item-2) ⭐️ 9.0/10
3. [Qwen3.6 在本地图像生成中胜过 Claude Opus 4.7](#item-3) ⭐️ 9.0/10
4. [我国牵头制定人形机器人数据集国际标准](#item-4) ⭐️ 9.0/10
5. [OpenAI、Anthropic 和谷歌联手遏制中国公司蒸馏其 AI 模型](#item-5) ⭐️ 9.0/10
6. [苹果将用谷歌 1.2 万亿参数 Gemini 模型重构 Siri](#item-6) ⭐️ 9.0/10
7. [阿里腾讯同日发布 3D 生成式 AI 模型](#item-7) ⭐️ 9.0/10
8. [DeepSeek 发布 DeepGEMM 更新，支持 Mega MoE 与 FP4 精度](#item-8) ⭐️ 9.0/10
9. [通义千问开源稀疏 MoE 模型 Qwen3.6-35B-A3B](#item-9) ⭐️ 9.0/10
10. [OpenAI 推出可用于生产的智能体 SDK](#item-10) ⭐️ 9.0/10
11. [OpenAI 的 Codex 获得完整电脑控制与长期自动化能力](#item-11) ⭐️ 8.0/10
12. [llm-anthropic 0.25 新增对 Claude Opus 4.7 的支持](#item-12) ⭐️ 8.0/10
13. [华为推出伴随式 AI 助手“小艺”](#item-13) ⭐️ 8.0/10
14. [“龙虾出行”完成近亿元天使轮融资](#item-14) ⭐️ 8.0/10
15. [AI 偏好资深员工，职场新人处境艰难](#item-15) ⭐️ 8.0/10
16. [RootFlow AI 推出 Opus 4.7 并提供限时优惠](#item-16) ⭐️ 8.0/10
17. [我国科学家发现大脑皮层的双重起源](#item-17) ⭐️ 8.0/10
18. [美国团队开发可自愈复合材料，寿命或达数百年](#item-18) ⭐️ 8.0/10
19. [群核科技港股上市首日大涨 170%](#item-19) ⭐️ 8.0/10
20. [吉利千里浩瀚 ADAS 计划 2026 年上车超百万辆](#item-20) ⭐️ 8.0/10
21. [MenuStatus：macOS 菜单栏服务与 AI 状态监控工具](#item-21) ⭐️ 8.0/10
22. [Agent Card 为 AI 智能体提供虚拟 Visa 卡](#item-22) ⭐️ 8.0/10
23. [中国将制定 2026—2030 年扩大内需与“人工智能+”战略](#item-23) ⭐️ 7.0/10
24. [有赞登陆港交所主板，预计 2026 年 AI 收入超 10 亿元](#item-24) ⭐️ 7.0/10
25. [Hermes Agent 会话标题支持自定义](#item-25) ⭐️ 7.0/10
26. [Gemini 手机客户端多节点代理仍无法使用](#item-26) ⭐️ 7.0/10
27. [小佩推出带多宠面部识别的智能宠物饮水机](#item-27) ⭐️ 7.0/10
28. [HyperX 将于 2026 年 4 月 20 日发布三款 AI 游戏本](#item-28) ⭐️ 7.0/10
29. [阿尔忒弥斯二号机组确认月球基地计划可行](#item-29) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 4.6，支持 200K 上下文和自适应思考](https://t.me/zaihuapd/40903) ⭐️ 10.0/10

Anthropic 发布了 Claude Opus 4.6，支持 20 万 token 的上下文窗口（测试版可达 100 万），输出上限翻倍至 12.8 万 token，并引入可根据任务复杂度动态调整推理深度的自适应思考模式，以及用于延长对话的自动上下文压缩功能。 此次更新大幅提升了模型处理长文本、复杂任务（如文档分析、代码生成和多轮推理）的能力，为前沿 AI 模型在企业和研究领域的应用树立了新标杆。 Opus 4.6 默认启用自适应思考模式，用户可通过 effort 参数（低/中/高）调节推理深度；当接近 token 限制时，上下文压缩功能会自动总结早期对话内容，无需人工干预即可保持连贯性。

telegram · zaihuapd · Apr 16, 14:28

**背景**: 大语言模型（LLM）以称为 token 的文本单元进行处理，其上下文窗口决定了单次可处理的输入长度。更大的上下文窗口使模型能处理更长的文档或维持更久的对话。自适应思考指模型能根据任务难度动态分配计算资源进行推理，从而提升效率与准确性。上下文压缩技术则通过剔除长输入中的无关信息，在 token 限制内保留关键内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking">Adaptive thinking - Claude API Docs</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-adaptive-thinking.html">Adaptive thinking - Amazon Bedrock</a></li>
<li><a href="https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/">Context Compression Techniques : Reduce LLM Costs by 50%</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Claude`, `#Anthropic`, `#Frontier AI`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 4.7，带来多项重大更新](https://www.anthropic.com/news/claude-opus-4-7) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 4.7，引入了自适应推理（adaptive thinking）、新的分词器（tokenizer），并更改了默认输出行为——除非明确请求，否则不再包含人类可读的推理摘要。 这些变更显著影响开发者如何集成和使用 Claude，尤其对依赖结构化推理输出的应用，在成本、token 使用、调试流程和用户体验方面带来重要影响。 新分词器根据内容类型使 token 数量增加 1.0 至 1.35 倍；若要恢复之前的推理摘要，必须显式添加 'display': 'summarized' 参数；自适应推理取代了旧版固定推理强度模式。

hackernews · meetpateltech · Apr 16, 14:23

**背景**: 大型语言模型（LLM）如 Claude 通过分词器将文本转换为 token（数值表示）进行处理，这直接影响上下文长度、成本和性能。“自适应推理”指根据输入复杂度动态调整模型推理深度的机制，旨在平衡准确性和效率。Anthropic 的 Opus 系列是其能力最强的模型，常用于复杂编程和分析任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/thinking-sand/what-is-llm-tokenization-and-why-is-it-important-4eb5fbefb075">What is LLM Tokenization and Why Is It Important? - Medium</a></li>
<li><a href="https://arxiv.org/pdf/2404.09170">Distilling Reasoning Ability from Large Language Models with...</a></li>
<li><a href="https://huggingface.co/learn/llm-course/chapter2/4">Tokenizers - Hugging Face LLM Course</a></li>

</ul>
</details>

**社区讨论**: 开发者对新的自适应推理接口感到困惑，并对即将无法使用如 Opus 4.5 等更受青睐的旧版本表示不满。一些人批评 Opus 4.6 存在严重幻觉和不稳定问题，还有人指出 token 使用量增加使得像 'caveman' 这类工具对生成更简洁输出变得更重要。

**标签**: `#AI`, `#Claude`, `#Large Language Models`, `#Anthropic`, `#Model Updates`

---

<a id="item-3"></a>
## [Qwen3.6 在本地图像生成中胜过 Claude Opus 4.7](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/#atom-everything) ⭐️ 9.0/10

Simon Willison 使用他戏谑的“鹈鹕骑自行车”基准测试，对比了阿里巴巴新发布的 Qwen3.6-35B-A3B 和 Anthropic 的 Claude Opus 4.7 的图像生成效果，发现 Qwen 在 MacBook Pro 上本地运行时输出更准确、更具创意。 这表明像 Qwen 这样的前沿开源模型即使在消费级硬件上运行，也能胜过 Claude Opus 等专有系统，凸显了本地大语言模型推理效率和多模态能力的进步。 Qwen 模型通过 LM Studio 在 M5 MacBook Pro 上运行，使用了 20.9GB 的 GGUF 量化版本（Q4_K_S）；两个模型还额外测试了全新的“火烈鸟骑独轮车”提示，以排除对鹈鹕基准的过拟合。

rss · Simon Willison · Apr 16, 17:16

**背景**: “鹈鹕骑自行车”基准是 Simon Willison 创建的一个幽默非正式测试，用于评估 AI 模型根据文本提示生成连贯 SVG 图像的能力。GGUF 是一种用于量化大语言模型的文件格式，可借助 LM Studio 和 llama.cpp 等工具实现高效的本地推理。Qwen 是阿里巴巴开发的一系列大语言模型，而 Claude Opus 是 Anthropic 的旗舰闭源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF">unsloth/ Qwen 3 . 6 - 35 B - A 3 B - GGUF · Hugging Face</a></li>
<li><a href="https://lmstudio.ai/docs/developer/core/server">LM Studio as a Local LLM API Server | LM Studio</a></li>
<li><a href="https://www.toolify.ai/ai-model/lmstudio-community-qwen3-30b-a3b-gguf">Qwen 3 -30 B - A 3 B - GGUF huggingface.co api... - Toolify</a></li>

</ul>
</details>

**标签**: `#AI models`, `#Qwen`, `#Claude Opus`, `#local LLM inference`, `#generative AI`

---

<a id="item-4"></a>
## [我国牵头制定人形机器人数据集国际标准](https://www.ithome.com/0/940/186.htm) ⭐️ 9.0/10

我国在国际标准化组织（ISO）成功立项全球首个《人形机器人数据集》国际标准，并推动成立首个由中国专家担任召集人的工作组，实现具身智能领域标准化的两大历史性突破。 此举标志着中国从国际标准的跟随者转变为制定者，在具身智能这一前沿科技领域掌握话语权，对全球人形机器人技术规范和产业发展方向将产生深远影响。 该国际标准参考了我国正在研制的人形机器人数据集系列国家标准；截至 2025 年底，中国拥有全球 84.7%的人形机器人出货量（1.44 万台），企业数量达 140 家，占全球总量近一半。

rss · IT HOME · Apr 17, 02:01

**背景**: 具身智能指通过机器人身体与物理世界交互的人工智能系统，如人形机器人。该领域的国际标准对确保数据质量、系统互操作性、安全性和伦理合规至关重要。长期以来，机器人国际标准主要由美、日、欧主导，通过 ISO/TC 299 技术委员会制定。中国此次突破是其在全球前沿科技治理中争取主导权的重要举措。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://std.samr.gov.cn/gb/search/gbDetailed?id=30D202B3ADBFE9F6E06397BE0A0A4001">人形机器人数据集第1部分：总则 - 全国标准信息公共服务平台</a></li>
<li><a href="http://orac.hainan.gov.cn/wtotbtzx/jsxmycsxw/2025/02/327454.shtml">StandICT.eu技术工作组发布《机器人标准前景》报告</a></li>
<li><a href="https://www.digitalchina.gov.cn/2025/xwzx/qwfb/202512/t20251229_5263139.htm">越来越智慧！具身智能走向更多生活场景_权威发布_数字中国建设峰会</a></li>

</ul>
</details>

**标签**: `#具身智能`, `#人形机器人`, `#AI标准`, `#国际标准化`, `#前沿科技`

---

<a id="item-5"></a>
## [OpenAI、Anthropic 和谷歌联手遏制中国公司蒸馏其 AI 模型](https://t.me/zaihuapd/40889) ⭐️ 9.0/10

OpenAI、Anthropic 和谷歌正通过前沿模型论坛（Frontier Model Forum）合作，共享有关中国 AI 公司使用“对抗性蒸馏”技术未经授权复制其前沿模型的情报。 此次合作回应了人们对 AI 领域知识产权盗窃及外国复制美国先进模型可能带来的国家安全风险的日益担忧。这也标志着竞争对手在地缘政治紧张局势下罕见地联合起来保护核心 AI 资产。 该行动重点检测大规模蒸馏活动，例如据称由深度求索（DeepSeek）、月之暗面（Moonshot）和 MiniMax 开展的活动——这些公司通过反复调用公开 API 来训练竞品模型。OpenAI 已在近期提交给美国国会的备忘录中提及此问题。

telegram · zaihuapd · Apr 16, 04:06

**背景**: 模型蒸馏是一种合法的机器学习技术，即较小的“学生”模型从较大的“教师”模型输出中学习。然而，若未经许可通过公开 API 进行，则可能构成对专有 AI 能力的未经授权复制。前沿模型论坛由领先 AI 开发商发起，旨在推动安全开发并减轻前沿 AI 系统带来的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://oecd.ai/en/incidents/2026-04-06-1282">US AI Firms Collaborate to Counter Unauthorized Model ...</a></li>
<li><a href="https://www.frontiermodelforum.org/">Frontier Model Forum</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#frontier AI`, `#model distillation`, `#AI policy`, `#geopolitical AI`

---

<a id="item-6"></a>
## [苹果将用谷歌 1.2 万亿参数 Gemini 模型重构 Siri](https://t.me/zaihuapd/40891) ⭐️ 9.0/10

苹果计划将谷歌开发的 1.2 万亿参数 Gemini 人工智能模型整合到代号为 Linwood 的 Siri 重大升级中，预计于 2026 年春季随 iOS 26.4 发布。据报导，苹果将根据新授权协议每年向谷歌支付约 10 亿美元。 此举标志着苹果战略的重大转变——该公司历来依赖自研 AI 技术，如今却转向采用第三方大模型，反映出整个行业对超大规模基础模型日益增长的依赖。这将显著提升 Siri 在推理、规划和摘要方面的能力，缩小与 Alexa 和 Google Assistant 等竞品的差距。 该模型很可能是 Gemini 3 Flash，被描述为一种“超稀疏”架构的 1.2 万亿参数模型，专为速度和效率优化。尽管目标定于 2026 年春季发布，但近期报道指出因测试问题可能出现延期，新 Siri 或推迟至 iOS 26.5 甚至 iOS 27 推出。

telegram · zaihuapd · Apr 16, 05:18

**背景**: Gemini 是由 Google DeepMind 开发的多模态大语言模型系列，是 LaMDA 和 PaLM 2 的继任者，于 2023 年 12 月发布，包含 Pro、Flash 和 Deep Think 等版本。苹果当前的 Siri 基于一个仅 1500 亿参数的模型，相比采用万亿级参数模型的新一代语音助手，在高级 AI 能力上明显受限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri">Apple Plans to Use 1.2 Trillion Parameter Google Gemini Model to Power New Siri - Bloomberg</a></li>
<li><a href="https://bdtechtalks.substack.com/p/what-i-think-makes-gemini-3-flash">What (I think) makes Gemini 3 Flash so good and fast</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#Siri`, `#Large Language Models`, `#Apple`

---

<a id="item-7"></a>
## [阿里腾讯同日发布 3D 生成式 AI 模型](https://www.bloomberg.com/news/articles/2026-04-16/alibaba-releases-new-ai-model-for-gaming-development) ⭐️ 9.0/10

阿里巴巴发布了 Happy Oyster 模型，可从文本、图像或视频生成交互式 3D 视频内容；腾讯则开源了混元 3D 世界模型 2.0，支持基于多模态输入生成、重建和模拟 3D 世界。 此举标志着游戏、影视和数字孪生领域 AI 驱动的 3D 内容创作取得重要进展，可大幅提升制作效率并推动沉浸式虚拟体验发展。同时也凸显了中国科技巨头在基础生成式 AI 能力上的竞争加剧。 腾讯模型支持导出 Mesh、3DGS（3D 高斯泼溅）和点云等格式，并可接入 Unity 和虚幻引擎；两家模型均支持基于真实场景的多视角视频或图像构建数字孪生。

telegram · zaihuapd · Apr 16, 07:58

**背景**: 3D 高斯泼溅（3DGS）是一种基于光栅化的技术，能从稀疏的 2D 图像中渲染出逼真的 3D 场景，实现高效且高保真的场景表达。AI 中的“世界模型”指能够构建环境内部表征并预测物体与物理规律如何随时间演化的系统，对规划、机器人和交互式内容生成至关重要。数字孪生是物理空间或物体的虚拟复制品，如今越来越多地通过 AI 从视觉数据构建，广泛应用于媒体、制造和城市规划等领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://arxiv.org/html/2504.13159v1">Digital Twin Generation from Visual Data: A Survey</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#3D content generation`, `#multimodal AI`, `#AI for gaming`, `#world models`

---

<a id="item-8"></a>
## [DeepSeek 发布 DeepGEMM 更新，支持 Mega MoE 与 FP4 精度](https://github.com/deepseek-ai/DeepGEMM/tree/public-release-260416) ⭐️ 9.0/10

2026 年 4 月 16 日，DeepSeek 发布了其 DeepGEMM CUDA 算子库的重大更新，推出了 Mega MoE 融合算子（将计算与 NVLink 通信重叠），并新增了 FP8×FP4 GEMM 算子、FP4 Indexer 以及程序化依赖启动（PDL）支持。 该进展大幅提升了在 NVIDIA H800 及更新 GPU 上训练和推理大模型（尤其是 MoE 架构）的效率，通过激进的量化和算子融合，提高了硬件利用率并降低了内存带宽需求。 该库面向 NVIDIA SM90（Hopper）和 SM100（Blackwell）架构，采用轻量级即时编译，无需预安装构建，并利用对称内存技术优化多专家负载；FP4 支持可实现约 2 倍的模型压缩。

telegram · zaihuapd · Apr 16, 09:57

**背景**: 混合专家（MoE）是一种神经网络架构，每次输入仅激活部分“专家”子网络，在不显著增加计算成本的前提下提升模型容量。FP4 是一种新兴的 4 位浮点格式，用于对模型权重进行量化以减少内存占用和带宽需求。程序化依赖启动（PDL）是 Hopper 和 Blackwell 架构的新特性，允许同一 CUDA 流中的依赖核函数安全地重叠执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/cutlass/latest/media/docs/cpp/dependent_kernel_launch.html">Dependent kernel launches — NVIDIA CUTLASS Documentation</a></li>
<li><a href="https://grokipedia.com/page/FP4_and_MS-FP8_Quantization">FP4 and MS-FP8 Quantization</a></li>
<li><a href="https://arxiv.org/html/2506.04667v2">FlashDMoE: Fast Distributed MoE in a Single Kernel - arXiv.org</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Mixture of Experts`, `#CUDA Kernels`, `#Model Optimization`, `#FP4 Quantization`

---

<a id="item-9"></a>
## [通义千问开源稀疏 MoE 模型 Qwen3.6-35B-A3B](https://qwenlm.github.io/blog/qwen3.6-35b-a3b/) ⭐️ 9.0/10

通义千问团队开源了 Qwen3.6-35B-A3B，这是一个总参数量达 350 亿、每次推理仅激活 30 亿参数的稀疏混合专家（MoE）模型。该模型在 SWE-bench 等编程基准和多模态任务中表现优异，并提供开放权重和开发者友好的 API。 此次发布推动了高效大语言模型的发展，证明稀疏架构能在编程和多模态推理能力上媲美更大的稠密模型，同时显著降低计算成本。这使得资源有限的开发者和机构也能更轻松地部署自托管 AI 系统。 该模型在 SWE-bench、Terminal-Bench 和 MCPMark 等代理式编程基准上表现突出，并具备可与部分闭源模型媲美的多模态理解能力。尽管总参数量庞大，但其设计支持单 GPU 部署，并提供兼容 OpenAI/Anthropic 风格的 API。

telegram · zaihuapd · Apr 16, 13:59

**背景**: 稀疏混合专家（MoE）模型在处理每个输入时仅激活部分参数，从而在不牺牲性能的前提下提升效率。SWE-bench 等基准测试使用来自 GitHub 的真实软件问题评估模型的编程修复能力，而 MCPMark 则通过模型上下文协议（MCP）测试模型的代理执行能力。这些评测对衡量 AI 编程助手的实际应用价值至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pulse24.ai/news/2026/4/16/15/qwen-releases-sparse-coding-moe">Qwen Releases Sparse Coding MoE - pulse24.ai</a></li>
<li><a href="https://www.swebench.com/">SWE - bench Leaderboards</a></li>
<li><a href="https://mcpmark.ai/docs/introduction">MCPMark · Docs · MCPMark</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#MoE`, `#Open Source`, `#Code Generation`

---

<a id="item-10"></a>
## [OpenAI 推出可用于生产的智能体 SDK](https://www.producthunt.com/products/openai) ⭐️ 9.0/10

OpenAI 发布了一个用于构建生产级 AI 智能体的新软件开发工具包（SDK），包含集成的智能体框架（harness）和沙箱环境。该 SDK 是其早期实验性 Swarm 框架的正式生产就绪版本。 此次发布降低了构建可靠、有状态、多步骤 AI 工作流的门槛，使智能体能安全地与现实系统交互。这标志着 OpenAI 正将智能体 AI 作为核心应用范式，超越简单的聊天界面。 该 SDK 包含类 Unix 沙箱，支持文件系统、shell 访问、包管理和快照功能，使智能体能安全执行代码并管理生成物。框架（harness）负责编排、工具调用、状态管理和审批流程，将智能体逻辑与底层模型分离。

producthunt · Zac Zuo · Apr 16, 06:51

**背景**: AI 智能体是可以自主规划、使用工具、保持状态并执行多步任务的系统。与仅响应单次提示的基础大语言模型 API 不同，智能体需要被称为“框架”（harness）的基础设施来管理执行、记忆和安全性。沙箱机制对于允许智能体运行代码或访问数据而不危及系统安全至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents/sandboxes">Sandbox Agents | OpenAI API</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#OpenAI`, `#AI Development`, `#Frontier Tech`, `#Software Development Kit`

---

<a id="item-11"></a>
## [OpenAI 的 Codex 获得完整电脑控制与长期自动化能力](https://openai.com/index/codex-for-almost-everything/) ⭐️ 8.0/10

OpenAI 发布了 Codex 的重大更新，使其能够通过视觉识别、鼠标点击和键盘输入自主操作 macOS 电脑，并支持跨越数天或数周的长期任务。此次更新包括后台智能体模式、90 多个针对 GitHub 和 Slack 等工具的新插件，以及用于记住用户偏好和上下文的增强记忆功能。 此次更新将 Codex 从代码生成工具转变为能跨应用执行复杂现实工作流的通用 AI 助手，可能彻底改变人类与计算机的交互方式。这也加剧了 AI 智能体领域的竞争，尤其是与 Anthropic 的 Claude Computer Use 等功能形成直接对标。 电脑控制功能目前仅支持 macOS，并以不干扰用户的后台模式运行；Codex 通过截图和界面理解来操作应用程序。安全问题仍然存在，因为赋予 AI 完整系统访问权限可能带来意外操作或数据泄露的风险。

hackernews · mikeevans · Apr 16, 17:12

**背景**: Codex 是 OpenAI 开发的代码理解和生成 AI 系统，最初为 GitHub Copilot 提供支持。随着多模态 AI 和智能体框架的进步，大模型现在能够感知屏幕并通过图形界面执行操作，从纯文本交互迈向类似人类的“具身”数字智能体，可直接操作各类软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zdnet.com/article/openai-codex-desktop-update/">OpenAI's Codex Desktop can run your computer now - ZDNET</a></li>
<li><a href="https://www.howtogeek.com/i-let-claude-control-my-computer/">I let Claude control my computer—and it filled my Amazon basket</a></li>
<li><a href="https://tech-insider.org/anthropic-claude-computer-use-agent-2026/">Claude Computer Use: What $20/Mo Actually Gets You [2026]</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：有人认为 Codex 只是在追赶 Claude Desktop 等已有工具，也有人看好其为非开发者简化复杂工作流的潜力。此外，用户还表达了对安全性、过度依赖 AI 以及“代码”与自然语言提示界限模糊等问题的担忧。

**标签**: `#AI`, `#Codex`, `#automation`, `#human-computer interaction`, `#OpenAI`

---

<a id="item-12"></a>
## [llm-anthropic 0.25 新增对 Claude Opus 4.7 的支持](https://simonwillison.net/2026/Apr/16/llm-anthropic/#atom-everything) ⭐️ 8.0/10

llm-anthropic 插件 0.25 版本新增对 Anthropic 最新 Claude Opus 4.7 模型的支持，该模型包含设为 'xhigh' 的 'thinking_effort' 参数。此外还增加了两个新的布尔选项 'thinking_display' 和 'thinking_adaptive'，并将默认的 'max_tokens' 提高至各模型允许的最大值。 此次更新让开发者能更精细地控制 Claude 的推理行为和输出长度，从而在应用中更高效地利用先进 AI 能力。它使开源工具与 Anthropic 最新模型创新保持同步，通过调节 effort 参数实现成本与性能的权衡。 'thinking_display' 功能目前仅在 JSON 输出或日志中可用，不支持纯文本。此外，该版本不再对旧模型使用已弃用的 'structured-outputs-2025-11-13' beta 请求头。

rss · Simon Willison · Apr 16, 20:37

**背景**: Anthropic 的 Claude 模型支持一个 'effort'（努力程度）参数，用于控制模型生成响应时消耗的计算资源（token 数量），让用户在速度、成本和推理质量之间取得平衡。Opus 4.7 中新增的 'xhigh' 级别属于这一能力的一部分。llm-anthropic 插件则用于将 Claude 模型集成到 Simon Willison 的 LLM 命令行工具生态中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort">Effort - Claude API Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7">What's new in Claude Opus 4.7 - Claude API Docs</a></li>
<li><a href="https://www.reddit.com/r/ClaudeAI/comments/1sn57af/introducing_claude_opus_47_our_most_capable_opus/">Introducing Claude Opus 4.7, our most capable Opus model yet. - Reddit</a></li>

</ul>
</details>

**社区讨论**: 一些 Reddit 用户表示担忧，尽管 Anthropic 在 API 中新增了参数，却在 Claude 应用界面中移除了相关设置；还有开发者声称 Opus 4.7 相比早期版本出现了性能退步。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#reasoning models`

---

<a id="item-13"></a>
## [华为推出伴随式 AI 助手“小艺”](https://36kr.com/newsflashes/3770277733745414?f=rss) ⭐️ 8.0/10

华为推出了名为“小艺”的伴随式 AI 助手，采用侧边栏交互形式，用户双击导航条即可唤醒。该功能将首发搭载于 4 月 20 日发布的华为 Pura X Max 智能手机。 这一创新通过为大屏设备提供一种低干扰、随时可用的交互界面，提升了端侧 AI 的实用性，可能为智能手机的人机交互树立新标准。这也体现了华为通过本地化、情境感知的 AI 体验来强化其生态差异化战略。 该助手采用专为阔型屏优化的“侧边态交互”设计，支持全局待办任务管理。其唤醒方式通过导航条硬件集成实现，而非仅依赖语音或应用内触发。

rss · 36kr · Apr 17, 02:04

**背景**: 端侧 AI 指在用户设备本地运行的人工智能模型，相比云端处理能更好地保障隐私、提升响应速度并支持离线使用。在美国制裁限制华为使用谷歌移动服务的背景下，华为持续加大对 HarmonyOS 生态和 AI 能力的投入。“小艺”助手此前已有基础版本，此次以伴随式、情境感知的新形态重新设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/KQN79A5V053469RG.html">华为推出伴随式AI解决方案 华为Pura X Max首发|小艺|max|pura|知名企...</a></li>
<li><a href="https://www.jiemian.com/article/14265613.html">华为大阔折将首发小艺伴随式AI|界面新闻 · 快讯</a></li>
<li><a href="https://news.qq.com/rain/a/20260417A02PRS00">华为推出伴随式AI解决方案 华为Pura X Max首发_腾讯新闻</a></li>

</ul>
</details>

**标签**: `#AI Assistant`, `#On-Device AI`, `#Human-Computer Interaction`, `#Smartphones`, `#Huawei`

---

<a id="item-14"></a>
## [“龙虾出行”完成近亿元天使轮融资](https://36kr.com/newsflashes/3770269152264705?f=rss) ⭐️ 8.0/10

AI 出行品牌“龙虾出行”已完成近亿元人民币的天使轮融资，并全球首发深度集成 OpenClaw 开源框架的 AI 个人出行助理。 此举标志着多智能体 AI 系统在现实出行服务中的重要应用，有望通过个性化的 AI 协同彻底改变用户的出行规划与执行方式。基于 OpenClaw 等开源框架的构建，有助于推动智能出行领域的互操作性与开发者生态发展。 融资资金将用于多智能体协作平台的技术迭代、AI 科学家团队组建及全球市场推广。该 AI 助理基于 OpenClaw 开源框架，支持可编程 AI 工作流、50 多种服务集成，并可在本地基础设施部署。

rss · 36kr · Apr 17, 01:56

**背景**: 多智能体 AI 系统通过多个专业化 AI 代理协同工作，以更高效地解决复杂任务。OpenClaw 是一个开源 AI 自动化框架，旨在构建可定制、注重隐私的个人 AI 助理，能跨应用和服务集成，目标是用统一的 AI 操作系统取代传统的应用孤岛式界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://openclaw.im/">Openclaw - Open-Source AI Automation Framework | Build Your ...</a></li>
<li><a href="https://github.com/openclaw/openclaw">OpenClaw — Personal AI Assistant - GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#mobility`, `#multi-agent systems`, `#OpenClaw`, `#startup funding`

---

<a id="item-15"></a>
## [AI 偏好资深员工，职场新人处境艰难](https://www.v2ex.com/t/1206534#reply0) ⭐️ 8.0/10

一家公司改变了招聘策略，只录用有经验的专业人士，不再招聘应届生，并称新部署的多模型交叉评估（Cross-Evaluation）AI 系统大幅提升了资深员工的产出，却使新人处于明显劣势。 这一趋势表明，企业采用 AI 可能加剧劳动力市场的不平等，扩大资深员工与新人之间的生产力差距，进而重塑职业入门路径和人才培养策略。 该公司的多模型交叉评估系统通过整合多种 AI 模型提升输出质量和速度，但更有利于具备领域知识的员工有效引导或解读 AI 结果，导致新人 KPI 排名靠后、裁员风险更高。

rss · V2EX · Apr 17, 02:22

**背景**: 多模型交叉评估（Cross-Evaluation）指利用多个大语言模型或多模态模型，通过协作或对比分析来评估、优化或验证输出结果的 AI 框架。这类系统正越来越多地应用于企业，以自动化复杂工作流、提升决策质量并减少人工干预。随着 AI 承担更多知识密集型任务，隐性经验的价值上升，而传统的岗位培训则逐渐失去意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.09507v1">An Automated Multi-modal Evaluation Framework for Mobile ...</a></li>
<li><a href="https://opensource.googleblog.com/2025/05/announcing-lmeval-an-open-ource-framework-cross-model-evaluation.html">Announcing LMEval: An Open Source Framework for Cross-Model ...</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-workflow">AI Workflow | IBM</a></li>

</ul>
</details>

**标签**: `#AI in workplace`, `#AI productivity`, `#enterprise AI`, `#labor market`, `#AI adoption`

---

<a id="item-16"></a>
## [RootFlow AI 推出 Opus 4.7 并提供限时优惠](https://www.v2ex.com/t/1206528#reply0) ⭐️ 8.0/10

RootFlow AI 正式上线 Opus 4.7，这是一款性能媲美 Anthropic Claude Opus 4.7 的 AI 模型，并在 4 月 20 日前为 SVIP 用户提供 0.9 倍 Token 费率。新用户通过加入官方群并留言 ID 可领取 15U 免费额度。 此举为开发者和高级用户提供了高性价比的前沿推理模型访问权限，该模型具备增强的多模态能力，有助于降低使用尖端 AI 执行代码审查、数据分析等复杂任务的门槛。 该服务声称通过 Opus 4.7 模型提供“满血版”Claude 体验，支持最高 3.75MP 的高分辨率图像输入。0.9 倍 Token 费率仅适用于活动期间充值成为 SVIP 的用户。

rss · V2EX · Apr 17, 02:16

**背景**: Claude Opus 4.7 是 Anthropic 最新推出的旗舰 AI 模型，具备更强的推理能力、对缺失信息的准确识别能力，以及高分辨率图像支持，代表了多模态 AI 的重要进展。RootFlow AI 等第三方平台有时会提供类似或代理主流商业模型的 API 服务，并以更具竞争力的价格吸引用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-7">Introducing Claude Opus 4.7 - Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7">What's new in Claude Opus 4.7 - Claude API Docs</a></li>
<li><a href="https://www.coderabbit.ai/blog/claude-opus-4-7-for-ai-code-review">What Claude Opus 4.7 means for AI code review - CodeRabbit</a></li>

</ul>
</details>

**标签**: `#AI models`, `#Claude`, `#Opus 4.7`, `#frontier AI`, `#AI inference`

---

<a id="item-17"></a>
## [我国科学家发现大脑皮层的双重起源](https://www.ithome.com/0/940/196.htm) ⭐️ 8.0/10

中国科学院与华大研究院等单位的研究人员发现，灵长类大脑皮层由源自异皮层和初级感觉皮层的两个方向相反的分子梯度共同构建，解决了神经科学领域长期存在的争议。该成果于 4 月 17 日发表在《科学》期刊上。 这一发现为理解大脑皮层的组织、演化和功能提供了统一框架，对推动脑机接口、神经技术和类脑人工智能的发展至关重要。它使研究人员能在临床诊断和神经工程中更精准地定位脑区。 研究确定了一条“互斥分子梯度轴”作为灵长类皮层的根本组织原则，将微观基因表达模式与宏观功能结构联系起来。该轴通过证明异皮层和初级感觉区共同作为互补起源，调和了此前相互冲突的理论。

rss · IT HOME · Apr 17, 02:09

**背景**: 大脑皮层是负责感知、决策和语言等高级认知功能的脑外层结构。数十年来，神经科学家一直争论皮层究竟是主要从海马等古老边缘结构演化而来，还是从初级感觉区向外扩展形成。这两种竞争性假说——双重起源假说与锚点假说——此前缺乏跨物种、多尺度的系统性证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ion.ac.cn/tt/202604/t20260417_8186718.html">脑智卓越中心合作发现大脑皮层双梯度组织规律--中国科学院脑科学与智...</a></li>
<li><a href="https://news.sciencenet.cn/htmlnews/2026/4/563209.shtm">大脑皮层演化“双极地图”终结百年争论—新闻—科学网</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#brain-computer interface`, `#frontier tech`, `#cerebral cortex`, `#biotech`

---

<a id="item-18"></a>
## [美国团队开发可自愈复合材料，寿命或达数百年](https://www.ithome.com/0/940/183.htm) ⭐️ 8.0/10

北卡罗来纳州立大学与休斯敦大学的研究团队开发出一种纤维增强复合材料，通过 3D 打印的乙烯-甲基丙烯酸共聚物（EMAA）热塑性中间层和嵌入式碳基加热层，可实现超过 1000 次自修复循环。 该突破有望将飞机、汽车、风力涡轮机和航天器等关键设备的使用寿命从几十年延长至数百年，从而降低更换成本、能源消耗和工业废弃物。它有效解决了复合材料中常见的分层失效问题，同时强度优于现有航空级材料。 该材料通过通电加热嵌入的碳层，使 EMAA 中间层熔化并流入微裂纹，依靠聚合物链重新缠结实现“热修复”。尽管多次修复后韧性略有下降，但理论上仍可支持长达 500 年的使用，远超传统纤维增强聚合物（FRP）15 至 40 年的寿命。

rss · IT HOME · Apr 17, 01:56

**背景**: 纤维增强聚合物（FRP）复合材料因高强度重量比被广泛应用于航空航天和汽车行业，但易发生层间分层，导致结构失效。自愈合复合材料旨在自动修复此类损伤。乙烯-甲基丙烯酸（EMAA）共聚物（如杜邦的 Surlyn）在加热时具有固有的自愈能力，但过去机械强度不足，难以用于承力结构。近期研究通过将 EMAA 与纤维增强体及智能加热层结合，克服了这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-022-33936-z">Prolonged in situ self-healing in structural composites via ... Integrated damage sensing and self-healing in polymers and ... Engineers Built a Material That Repairs Itself over 1,000 ... Healable polymer blends: Computational analysis of damage and ... Self-Healing of Polymer Composites: Process and Developments</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7794991/">Mechanical Properties of Poly (ethylene-co-methacrylic acid ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00289-021-03650-9">The role of poly (ethylene-co-methacrylic acid) (EMAA) on ...</a></li>

</ul>
</details>

**标签**: `#self-healing materials`, `#composite materials`, `#frontier tech`, `#aerospace engineering`, `#advanced manufacturing`

---

<a id="item-19"></a>
## [群核科技港股上市首日大涨 170%](https://www.ithome.com/0/940/178.htm) ⭐️ 8.0/10

群核科技于 4 月 17 日正式在港交所上市，发行价为每股 7.62 港元，开盘后股价一度涨至 20.62 港元，涨幅超 170%。公司此次 IPO 预计募资总额不超过 12.27 亿港元（约合 10.72 亿元人民币）。 作为“杭州六小龙”之一，群核科技的成功上市反映了投资者对空间智能及 AI 在物理世界应用（如数字孪生和具身智能训练）的信心增强。其强劲的市场表现表明，支撑 AI 融入现实世界的基础设施正获得广泛关注与认可。 本次 IPO 全球发售约 1.61 亿股，其中 10%面向香港公开发售，90%为国际配售，由摩根大通和建银国际担任联席保荐人。群核旗下酷家乐及海外版 Coohom 已服务全球 200 多个国家和地区，自称全球最大空间设计平台。

rss · IT HOME · Apr 17, 01:45

**背景**: 空间智能指人工智能通过传感器、摄像头、激光雷达和 3D 模型等数据，理解并交互物理空间的能力。数字孪生是物理实体的虚拟映射，广泛应用于建筑、制造、城市规划等领域，用于仿真、监控和优化。群核科技提出的“空间大模型”旨在融合空间数据与生成式 AI，为在现实世界中运行的智能体提供基础能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonathanreichental/2026/01/31/ai-must-master-spatial-intelligence-to-fully-operate-in-the-real-world/">Spatial Intelligence Enables AI To Operate In The ... - Forbes</a></li>
<li><a href="https://time.com/7339693/fei-fei-li-ai/">Spatial Intelligence Is AI’s Next Frontier - TIME</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_twin">Digital twin - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#spatial intelligence`, `#digital twin`, `#3D content generation`, `#frontier tech`

---

<a id="item-20"></a>
## [吉利千里浩瀚 ADAS 计划 2026 年上车超百万辆](https://www.ithome.com/0/940/171.htm) ⭐️ 8.0/10

吉利千里浩瀚高阶智能辅助驾驶系统已交付近 50 万辆，计划 2026 年上车超百万辆；明年将覆盖吉利系七大品牌的 96 款车型，并于今年启动出海。 此举标志着中国高阶智能驾驶技术加速走向全球，吉利有望成为首个在海外规模化落地无图高阶辅助驾驶的中国车企，凸显国产智能驾驶方案的竞争力与商业化能力。 该系统支持无图城市 NOA、360°全姿态泊车、全国机械车位自动泊入、悬空障碍物感知及 130km/h 超高速刹停；低阶的 H1、H3 方案将逐步收缩，主推 H5、H7、H9 高阶方案。

rss · IT HOME · Apr 17, 01:36

**背景**: 城市 NOA（领航辅助驾驶）能让车辆在复杂城区场景中自主完成路口通行、无保护左转等操作。“无图”NOA 不依赖高精地图，而是通过实时传感器数据和 AI 模型实现泛化能力，更易大规模推广。千里浩瀚系统于 2025 年 3 月正式发布，是吉利推进软件定义汽车战略的核心技术之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/930766725_122158079">车企争相引入的“无图城市NOA”到底在折腾什么？关于把车卖贵的阳谋_搜...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/624986242">真无图的城市 NOA，比你想象中来得更快 - 知乎</a></li>
<li><a href="https://xueqiu.com/3098434072/383756081">【小鹏汽车更新城市 NOA 落地进度，新增 26 座无图城市开放】4 月 13 ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Autonomous Driving`, `#ADAS`, `#Automotive Tech`, `#Frontier Technology`

---

<a id="item-21"></a>
## [MenuStatus：macOS 菜单栏服务与 AI 状态监控工具](http://incident.io/) ⭐️ 8.0/10

一款名为 MenuStatus 的新 macOS 菜单栏应用发布，支持实时监控 Atlassian Statuspage 和 incident.io 的服务状态页面，并内置“AI 降智监测”仪表盘，追踪 OpenAI 和 Anthropic 等主流 AI 模型的性能退化与排名变化。 该工具通过将 AI 模型性能监控直接集成到开发者桌面，满足了日益增长的 AI 可观测性需求，帮助用户快速发现关键 AI 服务的中断或质量下降，同时提升了依赖云服务的工作流的透明度。 MenuStatus 支持组件分组、运行时长条显示、当前事故与近期历史记录，并可跳转至官方状态页。其“AI 降智监测”视图聚合了全球指数、厂商对比、告警和退化指标，但未公开数据来源或评估方法。

telegram · zaihuapd · Apr 16, 09:12

**背景**: AI 可观测性指通过监控 AI 系统特有的遥测数据（如响应质量、token 使用量和模型漂移）来确保其可靠性与可信度。Atlassian Statuspage 和 incident.io 等平台为云服务提供公开状态更新，帮助用户追踪故障与维护信息。随着对第三方 AI API 依赖的加深，开发者越来越需要轻量级工具同时监控基础设施和模型健康状况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-observability">What is AI observability? - IBM</a></li>
<li><a href="https://www.atlassian.com/software/statuspage">Improve Transparency with Statuspage | Atlassian</a></li>
<li><a href="https://en.wikipedia.org/wiki/Incident_Command_System">Incident Command System</a></li>

</ul>
</details>

**标签**: `#AI Monitoring`, `#macOS`, `#OpenAI`, `#Anthropic`, `#AI Observability`

---

<a id="item-22"></a>
## [Agent Card 为 AI 智能体提供虚拟 Visa 卡](https://www.producthunt.com/products/agent-card) ⭐️ 8.0/10

Agent Card 推出了预付虚拟 Visa 卡，使 AI 智能体能够自主进行在线支付。这些卡可通过 API 或 CLI 即时发放，通过 Stripe 充值，并在单次使用后自动注销以确保安全。 这为 AI 智能体提供了真正的财务自主权，是实现能在现实世界中独立行动的智能体系统的关键一步。它弥合了数字智能与现实世界交易之间的鸿沟。 这些卡为一次性使用，支持设置消费限额，并可与 Claude、ChatGPT 及任何兼容 MCP 的智能体集成。目前通过 Stripe 充值，所有交易均可实时追踪。

producthunt · Felipe Abello · Apr 16, 05:42

**背景**: AI 智能体正从被动工具演变为能在现实世界中做决策并采取行动的主动执行者。要让它们在商业场景中自主运行（例如预订服务、购买数据或支付 API 费用），就需要安全且可编程的支付方式。传统支付系统并非为机器发起、策略驱动的交易而设计，因此催生了专为智能体 AI 定制的新金融科技基础设施需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentcard.ai/">AgentCard - Virtual Cards for AI Agents</a></li>
<li><a href="https://www.producthunt.com/products/agent-card">Prepaid virtual Visa cards for AI agents | Agent Card ...</a></li>
<li><a href="https://chain.link/article/ai-agent-payments">AI Agent Payments: The Future of Autonomous Commerce - Chainlink</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#fintech`, `#autonomous AI`, `#AI infrastructure`, `#frontier tech`

---

<a id="item-23"></a>
## [中国将制定 2026—2030 年扩大内需与“人工智能+”战略](https://36kr.com/newsflashes/3770293600273159?f=rss) ⭐️ 7.0/10

国家发展改革委宣布将制定 2026—2030 年扩大内需战略实施方案，并深入推进“人工智能+”行动，作为“十五五”规划的重点任务。该计划包括加快发展智能经济、推动重大工程项目开工以及加强民生保障。 该战略表明中国在面对全球不确定性时，致力于推动经济向内需驱动和高科技创新驱动转型。“人工智能+”被确立为提升新质生产力的核心引擎，对全球供应链、科技竞争格局和可持续发展具有深远影响。 发改委提出五大重点工作：宏观政策协同、扩大内需、以人工智能推动产业升级、稳就业促增收、保障能源粮食安全。“人工智能+”行动旨在推动 AI 在各领域深度融合，打造智能经济新形态。

rss · 36kr · Apr 17, 02:20

**背景**: 中国的五年规划是国家经济治理的核心工具，用于设定发展战略重点。“十五五”规划（2026—2030 年）延续了近年来对科技自立自强和高质量发展的强调。“人工智能+”行动是在此前将 AI 定位为通用技术的基础上推进的，2025 年 8 月中国政府已发布专门指导意见，推动 AI 在各行业深度应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://english.www.gov.cn/policies/latestreleases/202508/27/content_WS68ae7976c6d0868f4e8f51a0.html">China issues guideline to accelerate 'AI Plus' integration ...</a></li>
<li><a href="https://www.weforum.org/stories/2026/03/what-china-new-5-year-plan-mean-global-trade-and-investment/">China's Five-Year Plan: Insights for global trade and investment</a></li>
<li><a href="https://assets.ctfassets.net/ne8byh03zy6e/199iIZAQ1zYIuK6gzZ2q0k/80de01dd58089847141c40289f8007d1/2025_10_17_-_CIO_Perspectives_-_China_Vision_2030_priorities_of_the_15th_FYP_EN.pdf">China’s vision 2030: Priorities of the 15th five-year plan</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#artificial intelligence`, `#economic strategy`, `#smart economy`, `#government initiative`

---

<a id="item-24"></a>
## [有赞登陆港交所主板，预计 2026 年 AI 收入超 10 亿元](https://36kr.com/newsflashes/3770285217825288?f=rss) ⭐️ 7.0/10

有赞已正式从港交所创业板（GEM）转至主板上市。公司 2025 年全年收入约 14.9 亿元，经营性盈利约 1.8 亿元，并预计 2026 年 AI 相关直接收入将超过 10 亿元。 此举标志着有赞财务状况趋于成熟，并战略转向在其 SaaS 产品中深度整合 AI 技术，体现了商业软件领域应用 AI 的行业趋势。若能实现可观的 AI 收入，将验证 AI 在中国零售科技领域的商业化可行性。 所预测的 AI 收入特指来自有赞 SaaS 平台内 AI 功能的“直接”收入，预计将带动数亿元的关联收入增长。公司核心业务仍是面向微信等生态的私域运营零售 SaaS 工具。

rss · 36kr · Apr 17, 02:12

**背景**: 有赞是中国领先的零售电商 SaaS 服务商，为商家提供线上开店、客户管理、营销自动化和支付金融等一站式解决方案，主要帮助中小企业在微信等平台构建私域流量。港交所主板对上市公司的财务记录、盈利能力及公司治理要求远高于创业板（GEM），转板通常被视为企业走向成熟的重要标志。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/391947366">有赞产品分析——带商家盘私域的SaaS - 知乎 有赞SaaS是什么？主要功能与应用场景详解 - 有赞新零售 产品分析：有赞，全场景SaaS服务商 | 人人都是产品经理 有赞商家平台产品架构与平台深度分析 分析 | 有赞产品拆解_客户_SaaS_策略 - 搜狐 有赞SaaS架构 有赞saas平台_mob6454cc63081f的技术博客_51CTO博客</a></li>
<li><a href="https://www.hkex.com.hk/Join-Our-Market/IPO/GEM?sc_lang=zh-HK">GEM - HKEX</a></li>
<li><a href="https://www.woshipm.com/evaluating/3448317.html">产品分析：有赞，全场景SaaS服务商 | 人人都是产品经理</a></li>

</ul>
</details>

**标签**: `#AI applications`, `#SaaS`, `#fintech`, `#business software`, `#AI revenue`

---

<a id="item-25"></a>
## [Hermes Agent 会话标题支持自定义](https://www.v2ex.com/t/1206536#reply0) ⭐️ 7.0/10

用户可以在聊天中使用 /title 命令，或通过命令行执行 'hermes sessions rename' 来重命名 Hermes Agent 会话。这解决了用户对默认标签（如 '<think>' 和 'Cli Session'）无法编辑的困惑。 自定义会话标题有助于提升组织性和可用性，尤其当用户长期管理多个 AI Agent 对话时。这一功能对于将 Hermes Agent 视为持久化工作环境而非一次性聊天界面至关重要。 会话标题必须唯一，最多 100 个字符，控制字符会被自动清除。如果输入重复名称，/title 命令会提示用户，这是设计使然，并非程序错误。

rss · V2EX · Apr 17, 02:23

**背景**: Hermes Agent 是一个支持持久化会话、跨交互记忆和基于经验自我改进的 AI Agent 平台。它允许用户恢复、分支、导出和搜索历史对话，因此会话管理对提升工作效率至关重要。'<think>' 标签通常出现在 Agent 内部推理阶段，在最终回复前显示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hermes-agent.nousresearch.com/docs/user-guide/cli/">CLI Interface | Hermes Agent</a></li>
<li><a href="https://toolnavs.com/en/article/1573-why-does-hermes-agent-title-prompt-for-duplicate-names-the-title-cannot-be-repea">Why does Hermes Agent /title prompt for duplicate names? The ...</a></li>
<li><a href="https://www.juheapi.com/blog/hermes-agent-complete-guide-to-the-self-improving-ai-2026">Hermes Agent: Complete Guide to the Self-Improving AI (2026)</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Hermes Agent`, `#user interface`, `#AI tools`, `#developer experience`

---

<a id="item-26"></a>
## [Gemini 手机客户端多节点代理仍无法使用](https://www.v2ex.com/t/1206530#reply0) ⭐️ 7.0/10

一名用户报告称，即使切换了美国、新加坡和台湾等多个代理节点，仍无法使用 Google 的 Gemini 手机应用，但电脑端访问正常。 这凸显了在访问 Gemini 等前沿 AI 服务时，地区限制和设备端策略执行带来的持续挑战，影响全球用户使用 Google DeepMind 旗舰模型的能力。 该问题似乎仅限于移动端；相同代理设置在电脑上可正常使用。Google 的系统可能在移动平台上更严格地检测并屏蔽代理或 VPN 流量。

rss · V2EX · Apr 17, 02:17

**背景**: Google 的 Gemini 是由 Google DeepMind 开发的先进 AI 模型，通过网页和移动应用在特定地区提供服务。它基于用户 IP 地址实施地理限制。虽然新加坡、日本等国家已全面开放访问，但其他地区仍受限。Google 尚未为受限地区提供官方通用解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/VPN/comments/1pcwxxw/gemini_suddenly_blocking_all_my_vpns_vps_proxies/">Gemini suddenly blocking all my VPNs + VPS proxies since ... - Reddit</a></li>
<li><a href="https://www.aifreeapi.com/en/posts/gemini-regional-restrictions">Gemini Regional Restrictions 2025: Complete Guide to Access from Any ...</a></li>
<li><a href="https://workalizer.com/insights/gemini/gemini-web-access-issues-from-account-checks-to-browser-fixes/">Troubleshooting Gemini Web Access: Account Settings & Browser Solutions</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#Google DeepMind`, `#accessibility`, `#mobile`

---

<a id="item-27"></a>
## [小佩推出带多宠面部识别的智能宠物饮水机](https://www.ithome.com/0/940/198.htm) ⭐️ 7.0/10

小佩发布了智能宠物饮水机 ULTRA 可视版，配备 140°超广角摄像头和 AI 多宠面部识别功能，支持猫狗脸部识别，将于 4 月 22 日开启预售，售价 799 元。 该产品将计算机视觉技术应用于日常宠物用品，为多宠家庭提供个性化的饮水监测，体现了 AI 正加速融入智能家居设备以提升宠物护理水平和用户互动体验的趋势。 产品采用独立双水箱设计，物理隔离净水与污水；支持 App 自动控制排水、冲洗和补水，并生成饮水报告及异常提醒。AI 面部识别虽支持猫狗，但在光线不足或多宠同时出现时可能影响识别准确率。

rss · IT HOME · Apr 17, 02:22

**背景**: AI 宠物设备是智能家居和物联网市场的新兴领域。宠物面部识别通常采用轻量级卷积神经网络，在边缘设备上运行，实现实时识别而无需依赖云端。近年来，端侧 AI 和低功耗传感器的进步使喂食器、宠物门等消费级产品已广泛应用此类技术，如今扩展至饮水机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/kuaitongAI/article/details/155523217">宠物识别算法在AI摄像头的应用实践：从多宠识别到行为分析_识别宠物行...</a></li>
<li><a href="https://www.sohu.com/a/884469081_121492428">多宠识别的技术原理、应用场景及方案对比_宠物_管理_模型</a></li>

</ul>
</details>

**标签**: `#AI`, `#smart home`, `#pet tech`, `#computer vision`, `#IoT`

---

<a id="item-28"></a>
## [HyperX 将于 2026 年 4 月 20 日发布三款 AI 游戏本](https://www.ithome.com/0/940/201.htm) ⭐️ 7.0/10

惠普旗下 HyperX 品牌宣布将于 2026 年 4 月 20 日同步推出三款全新暗影精灵游戏本——PRO 15 英寸、PRO 16 英寸和 MAX 16 英寸，均搭载 AI 功能与升级版散热系统。 此举标志着 AI 技术正从软件层面向消费级硬件深度渗透，通过个性化调校和智能优化提升游戏体验，体现了 AI 在终端设备中落地的行业趋势。 暗影精灵 PRO 16 英寸整机功耗超 200W，配备 OGH 大师模式（支持 CPU/GPU 底层参数调节）、OMEN AI 智能优化及惠小微个性化 AI 服务，并搭载酷凉风暴 PRO+散热技术。

rss · IT HOME · Apr 17, 02:21

**背景**: OMEN 是惠普旗下的电竞子品牌，其 OMEN Gaming Hub（OGH）软件可管理性能模式、监控系统状态并支持超频。新增的“大师模式”允许用户精细调节 PL1/PL2/IccMax 等底层参数。OMEN AI 能根据具体游戏自动优化系统设置。酷凉风暴 PRO+是惠普研发的高效散热技术，旨在高负载下维持稳定性能同时控制噪音与表面温度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1942331679806060050">OMEN暗影精灵MAX大师模式实测：解锁250W满功耗，游戏性能终极优化指南...</a></li>
<li><a href="https://www.hp.com/us-en/gaming-pc/omen-ai.html">OMEN AI | HP® Official Site</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/652770495">一场「风暴」，让暗影精灵时刻保持出色战力 - 知乎 2026主流进阶玩家首选：HyperX 暗影精灵 PRO 16核心配置深度揭秘，购... 惠普（HP）暗影精灵11游戏本评测：游戏性能与散热技术的完美结合_酷凉... 2026主流进阶玩家首选：HyperX 暗影精灵 PRO 16核心配置深度揭秘，购... 惠普暗影精灵 11：酷凉风暴 Pro 高负载散热表现_哔哩哔哩_bilibili 卷疯了！仅需6K! 暗影精灵 11 深度测评：2.5K 240Hz + 酷凉风暴..._什...</a></li>

</ul>
</details>

**标签**: `#AI in hardware`, `#gaming laptops`, `#OMEN AI`, `#consumer electronics`, `#HyperX`

---

<a id="item-29"></a>
## [阿尔忒弥斯二号机组确认月球基地计划可行](https://www.ithome.com/0/940/187.htm) ⭐️ 7.0/10

2026 年 4 月 10 日完成阿尔忒弥斯二号绕月飞行任务返回地球后，美国宇航员仅隔两天就开展了月球表面任务模拟，并宣布建设可持续月球基地“绝对可行”。他们在模拟中穿着新一代舱外活动服执行地质采样任务，表现超出预期。 这是自阿波罗 17 号以来首次载人深空任务机组对 NASA 战略转向的肯定——放弃月球轨道空间站，转而专注月面基础设施建设，将加速实现人类在月球的长期驻留。此举也增强了人们对先进舱外服、月球车和居住系统等关键技术的信心。 机组使用专为月尘环境设计的新一代舱外服进行了月面模拟；指挥官里德·怀斯曼表示，若当时配备着陆器，他们完全有能力在距地约 25 万英里的绕月飞行中降落。NASA 计划在未来七年投入 200 亿美元，在月球南极附近建设基地。

rss · IT HOME · Apr 17, 02:04

**背景**: NASA 的阿尔忒弥斯计划旨在让人类重返月球：阿尔忒弥斯一号（2022 年）为无人测试飞行，阿尔忒弥斯二号（2026 年）是自 1972 年以来首次载人绕月飞行，阿尔忒弥斯三号将执行自阿波罗计划以来首次载人登月。该计划最初包含“月球门户”（Lunar Gateway）轨道空间站，但 NASA 于 2026 年 3 月宣布战略调整，转而直接建设月面基础设施。新的月球基地架构强调建设共享的能源、物流和导航系统，以支持可持续探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_II">Artemis II - Wikipedia</a></li>
<li><a href="https://nasaspaceflight.com/2026/03/nasa-moon-base-pivots-gateway/">NASA outlines Moon Base plans, pivots on Gateway</a></li>
<li><a href="https://www.cbsnews.com/news/nasa-moon-base-plan-lunar-south-pole/">NASA unveils ambitious $20 billion plan to build moon base ...</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#lunar base`, `#NASA`, `#Artemis program`, `#frontier tech`

---