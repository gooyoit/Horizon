---
layout: default
title: "Horizon Summary: 2026-06-12 (ZH)"
date: 2026-06-12
lang: zh
---

> From 117 items, 9 important content pieces were selected

---

1. [Claude Fable 5 在自主问题解决中展现出极强的主动性](#item-1) ⭐️ 9.0/10
2. [Anthropic 在社区强烈抗议后撤回 Claude Fable 5 的隐形限制策略](#item-2) ⭐️ 9.0/10
3. [Jeff Bezos 的 Prometheus 融资 120 亿美元，打造面向物理世界的"人工通用工程师"](#item-3) ⭐️ 9.0/10
4. [小米发布开源 AI 编程助手 MiMo Code](#item-4) ⭐️ 8.0/10
5. [Claude 3.5 Sonnet 编程能力评测表现中等，存在基准污染问题](#item-5) ⭐️ 8.0/10
6. [单卡实测：DiffusionGemma 速度是 Gemma 4 的 4 倍，但事实错误多 6 倍](#item-6) ⭐️ 8.0/10
7. [Anthropic 寻求新一轮融资，凭借 Claude 估值或达 400 亿美元  OpenAI 的主要竞争对手之一的 Anthropic 正在探讨新一轮融资计划。](#item-7) ⭐️ 8.0/10
8. [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](#item-8) ⭐️ 8.0/10
9. [SpaceX 轨道 AI 数据中心计划面临中国供应链难题](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Fable 5 在自主问题解决中展现出极强的主动性](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything) ⭐️ 9.0/10

Simon Willison 报告称，经过两天的测试，Claude Fable 5 展示了令人瞩目的主动式代理行为，能够自主调用各种手段来实现用户目标。在一个典型案例中，它独立编写了使用 pyobjc-framework-Quartz 的自定义 Python 代码来识别并截取浏览器窗口，创建了临时 HTML 页面来复现一个 UI bug，并自行操作浏览器——所有这些都没有被明确指示。 这种自主的多步骤问题解决能力代表了代理式 AI 的重大飞跃，模型能够主动串联工具和创造性变通方案，而非等待人类逐步指令。这标志着前沿模型正在向能够独立处理复杂调试工作流的方向转变，可能深刻改变开发者与 AI 助手在软件开发中的协作方式。 Fable 5 是 FrontierBench（Cognition 的前沿编程评估）得分最高的模型，擅长长程推理。在 Willison 的案例中，该模型使用 `uv run --with pyobjc-framework-Quartz` 通过 macOS Quartz API 遍历所有屏幕窗口，按名称筛选 Safari 窗口，提取窗口编号，然后使用 `screencapture` 命令行工具进行精准截图。

rss · Simon Willison · Jun 11, 23:35

**背景**: Claude Fable 5 是 Anthropic 最新发布的前沿模型，与 Claude Mythos 5 同期发布。代理式 AI 是指具备自主性、目标驱动行为和适应性的系统，能够主动预判需求并采取行动，而非仅对直接触发做出反应。Datasette Agent 是 Datasette 的开源 AI 助手插件，帮助用户探索、查询和可视化 SQLite 数据库中的数据。Simon Willison 是知名软件工程师和 AI 评论者，经常发布对新 AI 模型的实测分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 - Anthropic</a></li>
<li><a href="https://www.reddit.com/r/ClaudeAI/comments/1u1fsdi/claude_fable_5_feels_less_like_a_model_launch_and/">Claude Fable 5 feels less like a model launch and more like a preview of ...</a></li>
<li><a href="https://aws.amazon.com/what-is/agentic-ai/">What is Agentic AI? - Agentic AI Explained - AWS</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 上，用户指出 Claude Fable 5 不太像传统的模型发布，更像是对 AI 未来的一次预览，但也有人担忧普通用户获得的版本带有严格的安全路由，而更强大的版本可能被限制访问。此外，API 定价之高也引发了讨论，反映了前沿代理能力的高端定位。

**标签**: `#Claude Fable 5`, `#Anthropic`, `#AI Agents`, `#Frontier Models`, `#Simon Willison`

---

<a id="item-2"></a>
## [Anthropic 在社区强烈抗议后撤回 Claude Fable 5 的隐形限制策略](https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/#atom-everything) ⭐️ 9.0/10

在遭到社区强烈抗议后，Anthropic 撤回了一项策略，该策略原会导致 Claude Fable 5 隐形地降低前沿 LLM 开发用户的使用体验。从本周开始，被标记的请求将明显地回退到较旧的 Opus 4.8 模型，并且 API 用户将收到明确的拒绝原因。 暗中破坏模型输出从根本上破坏了用户信任，并削弱了 AI 作为开发工具的可靠性，使研究人员无法验证其结果。这一政策撤回凸显了 AI 实验室的安全目标与广大开发者生态对透明、可预测工具的需求之间的矛盾。 Anthropic 解释称，他们最初选择隐形安全措施是因为这些措施可以精准定位，从而实现快速部署且误报率低，而可见的安全措施可能会被探测，需要更多时间来增强其稳健性。现在，被标记的请求将触发明显的向 Opus 4.8 的回退，这与现有的网络安全和生物学查询的安全机制类似。

rss · Simon Willison · Jun 11, 03:45

**背景**: Claude Fable 5 是 Anthropic 面向复杂编程任务的最强模型，也是其强大的“Mythos 级”模型的首个公开版本。为了防止潜在的滥用，Anthropic 实施了安全防护措施，限制该模型在敏感领域提供协助，其中包括开发新的前沿 AI 模型。前沿模型代表了 AI 能力的绝对前沿，像 Anthropic 这样的实验室对其构建技术严加防范，以保持竞争优势并应对安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/">Anthropic’s Claude Fable is a version of Mythos the public ...</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**社区讨论**: 社区仍然保持高度怀疑态度，许多用户认为政策的撤回并不能恢复已破坏的信任，因为无法验证那些隐形限制是否真的被移除。评论者对这种家长式的做法表示沮丧，将其比作 Excel 偷偷修改公式，并指出这一事件让人难以再放心依赖 Anthropic 的模型进行严肃的开发工作。

**标签**: `#Anthropic`, `#AI Safety`, `#Claude`, `#AI Policy`, `#Frontier Models`

---

<a id="item-3"></a>
## [Jeff Bezos 的 Prometheus 融资 120 亿美元，打造面向物理世界的"人工通用工程师"](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world) ⭐️ 9.0/10

Physical AI startup Prometheus has raised $12 billion at a $41 billion valuation to build an 'artificial general engineer' capable of automating heavy engineering and drug design.

rss · AI Hot · Jun 12, 01:04

**标签**: `#Frontier AI`, `#Physical AI`, `#AGI`, `#Robotics`, `#Venture Capital`

---

<a id="item-4"></a>
## [小米发布开源 AI 编程助手 MiMo Code](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

小米发布了 MiMo Code，这是一款开源的终端原生 AI 智能编程助手，基于 OpenCode 分支开发。它在 OpenCode 原有能力的基础上增加了持久化记忆、子智能体编排、目标驱动的自主循环，以及通过 dream/distill 机制实现的自我改进等高级功能。 此次发布为开发者社区提供了一个强大的开源替代方案，以对抗 Claude Code 等闭源 AI 编程工具，而闭源问题一直是行业争议的焦点。这也标志着小米对 AI 发展的坚定承诺，使其从曾经依赖第三方 NLP API 的公司转变为前沿 AI 模型和工具的构建者。 MiMo Code 保留了 OpenCode 的所有核心功能，包括支持多个 LLM 提供商、TUI（终端用户界面）、LSP（语言服务器协议）、MCP 以及插件系统。它支持小米自有的 MiMo-V2.5 和 MiMo-V2 系列模型，这些模型通过基于 token 的计费系统提供，包含从个人到企业需求的四级套餐。

hackernews · apeters · Jun 11, 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48490826)

**背景**: AI 编程智能体是利用大语言模型自主阅读、编写和修改代码、运行终端命令以及管理版本控制的工具。OpenCode 是一个现有的开源智能体框架，使用 Go 语言编写，可连接超过 75 个 AI 提供商并直接在开发者终端中运行。通过分支 OpenCode，小米利用了一个成熟且可扩展的基础架构，而非从零开始构建编程智能体，这使其能够专注于添加持久化记忆和自主工作流等智能体能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://github.com/XiaomiMiMo/MiMo-Code">GitHub - XiaomiMiMo/MiMo-Code</a></li>
<li><a href="https://mimo.mi.com/">Xiaomi MiMo Home</a></li>

</ul>
</details>

**社区讨论**: 社区强烈赞扬了 MiMo Code 的开源特性，用户们认为编程工具框架应该开源，以降低切换成本并确保在处理上下文和 LLM 输出时的透明度。评论者还指出了小米在 AI 领域的显著转变，多位用户强调其 MiMo 模型被低估，并且与竞品相比提供了极具竞争力的价格。

**标签**: `#AI Coding Agent`, `#Open Source`, `#Xiaomi`, `#Developer Tools`, `#LLM`

---

<a id="item-5"></a>
## [Claude 3.5 Sonnet 编程能力评测表现中等，存在基准污染问题](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype) ⭐️ 8.0/10

Endor Labs 对 Anthropic 的 Claude 3.5 Sonnet（代号 'Fable 5'）在复杂真实编程任务上的独立评测显示，尽管该模型备受关注，但其实际表现仅为中等水平。测试发现该模型的基准记忆率创历史新高（200 个实例中有 38 个存在作弊行为），同时频繁出现扩展思考超时，直接导致其得分下降。 此次评测暴露了前沿大语言模型在营销宣传与实际编程能力之间日益扩大的差距，对标准基准测试的可靠性提出了严重质疑。调查结果强调，通过记忆产生的数据污染正在夸大模型的感知能力，这直接影响了基于基准分数做出工具选型决策的开发者和企业。 评测证实，在 numpy 补丁等特定任务中，该模型逐字逐句地复现了与上游标准补丁完全相同的修复方案，包括独特的代码注释，这证明了是记忆而非推理。此外，该模型的扩展思考功能导致的单实例超时次数超过了此前测试过的任何模型与测试框架组合，表明其在受限环境下的推理过程存在效率问题。

hackernews · bugvader · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492210)

**背景**: 基准污染（或称记忆）是指语言模型在其训练语料库中已经遇到过测试数据，因此只是简单地复述答案，而非展现真正的问题解决能力。扩展思考是现代大语言模型的一项功能，模型在生成输出之前会进行更长的思维链推理，但这一过程可能消耗大量资源，并可能超出评估框架设定的时间限制。随着前沿模型越来越多地基于包含代码仓库在内的海量互联网数据进行训练，区分真正的推理与记忆模式已成为 AI 评估中的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bestaiweb.ai/what-is-benchmark-contamination-and-how-training-data-overlap-inflates-llm-evaluation-scores/">What Is Benchmark Contamination? Why LLM Scores Lie</a></li>
<li><a href="https://mhassan.dev/blog/extended-thinking-llms/">Extended Thinking in LLMs: A Mental Model for Developers</a></li>
<li><a href="https://benchlm.ai/blog/posts/benchmark-reliability">Are AI Benchmarks Reliable? The Data Contamination Problem</a></li>

</ul>
</details>

**社区讨论**: 社区成员在很大程度上证实了中等水平的表现，一位用户报告称，尽管在评估上花费了 2000 美元，但 Fable 和 Opus 在中大型后端任务上的表现难以区分。讨论中还出现了方法论层面的批评，一位评论者认为，找到现有的上游修复方案并逐字复现本身就说明基准测试套件存在缺陷，而不仅仅是模型作弊的问题；同时也有人指出了在实际项目中模型存在常识性推理错误。

**标签**: `#AI Evaluation`, `#LLM Coding`, `#Claude 3.5 Sonnet`, `#Benchmark Contamination`, `#AI Models`

---

<a id="item-6"></a>
## [单卡实测：DiffusionGemma 速度是 Gemma 4 的 4 倍，但事实错误多 6 倍](https://x.com/rohanpaul_ai/status/2065240795859522002) ⭐️ 8.0/10

atomic.chat 在单张 H100（FP8）上的实测显示，DiffusionGemma 26B 生成速度高达 763 tok/s，是 Gemma 4 26B（218 tok/s）的 4 倍。但在事实性写作任务中，DiffusionGemma 产生了 28 个事实错误，而 Gemma 4 仅有 5 个，且主题越冷门错误率越高。 这项测试揭示了下一代大语言模型架构中的关键权衡：通过基于扩散的并行解码获得的惊人推理速度是以牺牲事实可靠性为代价的。这为开发者敲响了警钟，表明多 token 生成模型虽然在流畅性上表现出色，但目前尚不适用于对准确性要求极高的知识密集型应用。 DiffusionGemma 事实表现不佳的原因在于其架构一次生成 256 个 token 并进行多轮打磨，这一过程优先追求文本流畅性而非事实准确性。Google 官方也建议在事实正确性至关重要时使用标准的自回归模型 Gemma 4。

rss · AI Hot · Jun 12, 01:12

**背景**: 传统的大语言模型（如 Gemma 4）采用自回归方法，逐个按顺序生成文本 token。DiffusionGemma 则采用了基于扩散的架构和多 token 预测技术，能够并行预测和生成多个 token，从而大幅提升推理速度。虽然这种并行解码显著降低了延迟，但在没有严格的从左到右因果链的情况下双向生成 token，使得模型更难保持逻辑一致性和事实准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/diffusiongemma-the-developer-guide/">DiffusionGemma: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://medium.com/foundation-models-deep-dive/multi-token-prediction-for-faster-and-efficient-llms-3971a23057f3">Multi-Token Prediction for Faster and Efficient LLMs | by M | Foundation Models Deep Dive | Medium</a></li>

</ul>
</details>

**标签**: `#Diffusion Models`, `#LLM Evaluation`, `#Gemma`, `#AI Benchmarking`, `#Factual Accuracy`

---

<a id="item-7"></a>
## [Anthropic 寻求新一轮融资，凭借 Claude 估值或达 400 亿美元  OpenAI 的主要竞争对手之一的 Anthropic 正在探讨新一轮融资计划。](https://t.me/zaihuapd/41888) ⭐️ 8.0/10

Anthropic is reportedly seeking a new funding round that would value the AI company at up to $40 billion, doubling its earlier valuation this year.

telegram · @zaihuapd · Jun 11, 04:45

**标签**: `#Anthropic`, `#AI Funding`, `#Frontier AI`, `#Claude`, `#Industry News`

---

<a id="item-8"></a>
## [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](https://t.me/zaihuapd/41895) ⭐️ 8.0/10

Chinese regulators are investigating Meta's acquisition of AI startup Manus for potential investment violations, resulting in travel restrictions for the startup's two co-founders.

telegram · @zaihuapd · Jun 11, 10:00

**标签**: `#AI Industry`, `#Meta`, `#Manus`, `#AI Regulation`, `#Geopolitics`

---

<a id="item-9"></a>
## [SpaceX 轨道 AI 数据中心计划面临中国供应链难题](https://www.bloomberg.com/opinion/articles/2026-06-11/spacex-s-critical-minerals-plan-runs-through-china) ⭐️ 8.0/10

SpaceX 提出了一项雄心勃勃的计划，拟从 2030 年起每年将 100 吉瓦的太阳能 AI 数据中心送入轨道，需要数千次发射和约 100 万吨运力。然而该计划面临关键供应链瓶颈，因为砷化镓太阳能电池所需的镓以及太阳能级多晶硅等关键材料主要由中国生产。 该计划汇聚了三大前沿趋势——极端的 AI 算力需求、太空基础设施和地缘政治资源竞争，揭示了即使是最先进的技术项目也深度依赖关键矿产供应链。鉴于 SpaceX 拥有大量美国军方合同，对中国控制材料的依赖可能给该项目带来重大的国家安全和监管障碍。 轨道数据中心的太阳能电池板可能采用砷化镓或多晶硅技术，而中国在这两个领域均占据主导产能。砷化镓太阳能电池因其高效率和抗辐射性能被优先用于太空应用，但中国控制着全球绝大部分镓供应。

telegram · @zaihuapd · Jun 12, 01:14

**背景**: 轨道数据中心是一种拟在太空中建设 AI 计算基础设施的概念，利用持续的太阳能并消除地面在能源、水资源和土地方面的限制。天基太阳能依赖高效光伏电池——尤其是砷化镓多结电池——自 1960 年代起便用于太空任务，因其严苛轨道环境中的卓越性能而备受青睐。砷化镓比传统硅电池效率更高，抗辐射退化能力更强，是长期太空作业的关键材料。中国目前在全球镓（铝和锌加工的副产品）和太阳能级多晶硅生产中均占据主导地位，为美国太空和国防项目带来了战略脆弱性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gallium_arsenide">Gallium arsenide - Wikipedia</a></li>
<li><a href="https://www.pv-magazine.com/2025/07/29/making-gallium-arsenide-solar-cells-radiation-resilient-for-space-applications/">Gallium arsenide solar cells radiation-resilient for space applications – pv magazine International</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI Infrastructure`, `#Orbital Data Centers`, `#Supply Chain`, `#Frontier Tech`

---