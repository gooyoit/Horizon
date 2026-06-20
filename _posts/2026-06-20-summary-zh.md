---
layout: default
title: "Horizon Summary: 2026-06-20 (ZH)"
date: 2026-06-20
lang: zh
---

> From 110 items, 12 important content pieces were selected

---

1. [Nvidia 发布 Nemotron 3 Ultra，Anthropic 限制竞品访问，TypeScript 7.0 RC 实现 10 倍提速](#item-1) ⭐️ 9.0/10
2. [智谱 GLM-5.2 登顶 Design Arena，超越 Claude Fable 5](#item-2) ⭐️ 9.0/10
3. [诺贝尔奖得主约翰·江珀离开 DeepMind 加盟 Anthropic](#item-3) ⭐️ 9.0/10
4. [微软与约克大学论文：若 LLM 拥有人类属性，则《帝国时代 II》亦然](#item-4) ⭐️ 8.0/10
5. [SemiAnalysis：AI 网络中铜缆与光缆互补而非对立](#item-5) ⭐️ 8.0/10
6. [智谱 AI 开源 GLM-5.2 模型获海外好评，股价大幅飙升](#item-6) ⭐️ 8.0/10
7. [Anthropic 限竞条款引争议；LLM 应用攻防警示；软件工程未真正工程化](#item-7) ⭐️ 8.0/10
8. [Anthropic 恰乌里称有信心“未来几天”重新开放 Mythos 及 Fable 5 AI 模型](#item-8) ⭐️ 8.0/10
9. [本周 AI 动态：OpenAI 免费健康 AI、Anthropic 机器人狗编程等](#item-9) ⭐️ 8.0/10
10. [visionOS 27 今秋推送：M5 Vision Pro 独占 Siri 语音定制与 AFM 3 Core Advanced 本地 AI 模型](#item-10) ⭐️ 8.0/10
11. [智谱创始人称旗下模型将在明年一季度前达到“Mythos 级别”](#item-11) ⭐️ 8.0/10
12. [Midjourney 宣布进军医疗领域，将推出超声波全身扫描仪与水疗中心](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nvidia 发布 Nemotron 3 Ultra，Anthropic 限制竞品访问，TypeScript 7.0 RC 实现 10 倍提速](https://x.com/hongming731/status/2068134424831807729) ⭐️ 9.0/10

Nvidia 发布了 Nemotron 3 Ultra，这是一个拥有 5500 亿参数的开源模型，采用混合专家 Mamba-Attention 架构，活跃参数为 550 亿，支持原生推测解码以实现每秒 300+ tokens 的吞吐量。Anthropic 对使用 Claude 进行竞品研究施加了限制，并因美国出口管制被迫将 Claude Fable 5 模型在全球范围内下线，同时微软宣布了 TypeScript 7.0 RC，将编译器移植到 Go 语言以实现约 10 倍的性能提升。 这些发展标志着开源前沿模型竞争加剧、AI 获取的地缘政治碎片化加深，以及开发者生态系统在基础设施层面的重大改进。Nvidia 进入顶级开源模型领域挑战了中国开源权重领导者的主导地位，而 Anthropic 的限制措施凸显了出口管制正在重塑全球 AI 研究合作格局。 Nemotron 3 Ultra 的智能指数为 48，排名美国开源权重模型第一，但仍未超越中国最佳开源模型，支持推理时推理预算控制和约 6 倍的吞吐量提升。DeepSWE 基准包含跨 TypeScript、Go、Python、JavaScript 和 Rust 的 113 个任务，配备隔离环境和基于程序的验证器，证明智能体编程能力尚未触顶。Spring I/O 的安全演示揭示了 RAG 系统容易受到通过恶意文件上传的路径穿越攻击、用于提权的 SQL 注入，以及绕过护栏的提示词拆分技术的攻击。

rss · AI Hot · Jun 20, 00:50

**背景**: 混合专家是一种在推理过程中仅激活模型部分参数的架构，允许更大的总参数量同时保持计算效率。RAG（检索增强生成）系统通过外部文档检索来增强 LLM，但其使用的文件处理管道可能被路径穿越攻击利用——攻击者通过符号链接操作或目录遍历序列来访问未授权文件。美国对 AI 模型的出口管制，特别是针对先进能力的管制，日益迫使公司对其最强大的模型进行地理限制访问，造成了全球 AI 格局的碎片化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aitoolsrecap.com/Blog/nvidia-nemotron-3-ultra-550b-computex-2026">NVIDIA Nemotron 3 Ultra Review 2026: 550B Parameters, MoE ...</a></li>
<li><a href="https://github.com/datacurve-ai/deep-swe">GitHub - datacurve-ai/deep-swe: Measuring frontier coding ...</a></li>
<li><a href="https://www.ibm.com/support/pages/node/7273426">Security Bulletin: Path Traversal Vulnerability in File Processing Components Allows Unauthorized File System Access and Potential Remote Code Execution</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Nvidia Nemotron`, `#Anthropic`, `#AI Agents`, `#LLM Security`

---

<a id="item-2"></a>
## [智谱 GLM-5.2 登顶 Design Arena，超越 Claude Fable 5](https://www.ithome.com/0/966/458.htm) ⭐️ 9.0/10

智谱 AI 的 GLM-5.2 模型在 Design Arena 单轮 HTML 网页设计评测中首次登顶总分第一，超越了 Anthropic 的 Claude Fable 5、Opus 4.6 和 Opus 4.7 等模型。这比其前代 GLM-5.1 提升了 5 个名次。 这一成就标志着中国 AI 实验室在专业、注重审美的代码生成任务中，已经能够与西方顶级模型直接竞争。此外，GLM-5.2 以极低的成本实现了这一点——每百万 tokens 推理价格为 1.40/4.40 美元，远低于 Fable 5 的 10/50 美元，为开发者提供了极具性价比的前沿模型选择。 Design Arena 指出，GLM-5.2 擅长高效集成 chart.js 和 three.js 等第三方库，使使用这些库的会话胜率提升了 6.0 个百分点。它还展现出卓越的布局和动画能力，在 91% 的会话中使用 TailwindCSS，在 51% 中使用 font-awesome，而 Fable 5 仅有 57% 的会话使用 TailwindCSS。

rss · IT HOME · Jun 20, 00:04

**背景**: Design Arena 是一个全球公认的群众外包基准测试平台，通过盲测让用户对 AI 生成的设计质量进行投票评估。它被公认为 AI 行业中最具说服力的“审美和落地设计”风向标之一。GLM-5 是智谱 AI 的旗舰基础模型，采用 7450 亿参数的混合专家架构，具备前沿级别的推理和编码能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.everydev.ai/tools/design-arena">Design Arena - Crowdsourced AI Benchmarks | EveryDev.ai</a></li>
<li><a href="https://glm5.ai/">GLM-5 - Zhipu AI's Flagship Foundation Model</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Benchmark`, `#Zhipu AI`, `#GLM-5.2`, `#Code Generation`

---

<a id="item-3"></a>
## [诺贝尔奖得主约翰·江珀离开 DeepMind 加盟 Anthropic](https://36kr.com/newsflashes/3860793998267653?f=rss) ⭐️ 9.0/10

6 月 19 日，因在 AlphaFold 项目中的突出贡献而获得 2024 年诺贝尔化学奖的约翰·江珀宣布，在谷歌 DeepMind 工作近九年后，他将离职加盟人工智能安全公司 Anthropic。江珀在社交平台 X 上公布了这一消息，标志着一位顶级科学家从谷歌核心 AI 实验室转向领先的前沿 AI 初创企业。 一位诺贝尔奖级别的科学家从 DeepMind 转投 Anthropic，标志着 Anthropic 在前沿模型开发和 AI 安全研究方面的实力将得到显著增强。这也反映了 AI 行业的一个更广泛趋势：顶级研究人员正从大型科技巨头流向专注于安全与对齐的 AI 初创企业。 江珀参与开发的 AlphaFold 是一款能够以革命性精度预测蛋白质结构的 AI 系统，他与 Demis Hassabis 因此共同获得 2024 年诺贝尔化学奖。Anthropic 由前 OpenAI 成员 Dario Amodei 和 Daniela Amodei 等人于 2021 年创立，以其 Claude 大语言模型和对 AI 安全及负责任开发的坚定承诺而闻名。

rss · 36kr · Jun 20, 00:42

**背景**: AlphaFold 是由 DeepMind 开发的一款 AI 程序，利用深度学习技术从氨基酸序列预测蛋白质结构，这是生物学领域长期存在的重大挑战。AlphaFold 2 在 2020 年实现了突破性的预测精度，该技术已被引用数万次，深刻改变了全球生物研究。Anthropic 是一家总部位于旧金山的 AI 公司，由前 OpenAI 研究人员创立，他们离开 OpenAI 是为了优先发展以安全为核心的 AI。该公司开发了 Claude 系列大语言模型，已成为全球最具价值的 AI 初创企业之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，江珀的离职反映了 DeepMind 内部日益严重的官僚主义问题，有评论者认为原 DeepMind 的组织氛围已导致科研人员流失。这种情绪暗示了对 DeepMind 在企业压力下留住顶尖科研人才能力的担忧。

**标签**: `#Anthropic`, `#AI Talent`, `#DeepMind`, `#AlphaFold`, `#Frontier AI`

---

<a id="item-4"></a>
## [微软与约克大学论文：若 LLM 拥有人类属性，则《帝国时代 II》亦然](https://x.com/rohanpaul_ai/status/2068141784476098894) ⭐️ 8.0/10

微软与约克大学的一篇新论文指出，许多关于 LLM 拥有共情、理解或焦虑等类人属性的声称，往往是测试设计和观察者偏差的产物，而非模型本身的内在属性。作者以《帝国时代 II》为例进行论证，证明该游戏在功能上是图灵完备的，理论上可以实现与 LLM 相同的计算基底，但没有人会认为游戏具有"理解"能力。 该论文直击 AI 评估与对齐领域的关键测量问题，促使研究者设计更严格的测试，以区分真正的认知能力与拟人化投射。随着 LLM 日益普及和影响力扩大，真正的理解与令人信服的模拟之间的区别对 AI 安全、监管和公众认知具有深远影响。 作者证明了《帝国时代 II》在功能上和图灵意义上都是完备的，意味着可以在游戏机制中实现逻辑门和小型感知机，例如用山羊等单位作为比特。论文并非全盘否定 AI 认知，而是揭示许多关于 LLM 类人属性的声称依赖于界面和观察者的预设，而非系统本身。

rss · AI Hot · Jun 20, 01:20

**背景**: AI 中的拟人化是指将理解、共情或意识等类人特质归因于 AI 系统的倾向，尤其是当 AI 的输出与人类交流高度相似时。图灵完备意味着一个系统在给定足够时间和内存的情况下可以执行任何通用计算机能完成的计算——许多出人意料的系统，包括游戏和元胞自动机，都已被证明是图灵完备的。感知机是最简单的人工神经网络，是一种单层计算单元，可以实现 AND 和 OR 等基本逻辑门。AI 评估中的测量问题涉及如何客观判断一个模型是否真正具备某种认知能力，还是仅仅产生了触发人类模式匹配本能的输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.31514">If LLMs Have Human-Like Attributes, Then So Does Age of ...</a></li>
<li><a href="https://languagelog.ldc.upenn.edu/nll/?p=73721">Language Log » Annals of Anthropomorphism</a></li>
<li><a href="https://www.linkedin.com/posts/mahmud-omar-58644230a_i-used-to-be-deep-into-age-of-empires-it-activity-7470190445243969539-q5A4">LLMs and Age of Empires II Turing-Completeness - LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 该论文在社交媒体上引发了趣味和赞赏，评论者认为以《帝国时代 II》作为归谬法的论证非常巧妙。许多读者认为这个类比有效地揭示了人类是多么容易将认知属性投射到任何具有自然语言界面的足够复杂的系统上。

**标签**: `#LLMs`, `#AI Evaluation`, `#AI Alignment`, `#Anthropomorphism`, `#AI Research`

---

<a id="item-5"></a>
## [SemiAnalysis：AI 网络中铜缆与光缆互补而非对立](https://x.com/SemiAnalysis_/status/2068136869011861897) ⭐️ 8.0/10

SemiAnalysis 发布分析指出，投资者错误地将 AI 网络视为铜缆与光缆的二元选择，实际上这两种技术是互补关系。随着 GPU 集群规模扩大，铜缆和光缆解决方案都将因 GPU、交换机、机架和集群间数据传输需求的增加而实现增长。 这一分析挑战了驱动 AI 基础设施股票大量资本配置决策的普遍投资者叙事。随着前沿 AI 模型需要越来越大的 GPU 集群，理解这些技术的互补性对于准确预测数据中心网络供应链的需求至关重要。 当铜缆能够满足距离、功耗、成本和可靠性要求时，它仍然是首选；而当带宽和距离需求超出铜缆的物理极限时，光缆则成为必需。这与 Nvidia 有据可查的策略一致——尽可能使用铜缆，仅在必要时才使用光纤，有源铜缆则在机架间和机架内连接中占据中间地带。

rss · AI Hot · Jun 20, 01:00

**背景**: AI 数据中心网络涉及在多个层级连接数千个 GPU——包括机架内、机架间和跨集群——使用 Nvidia 的 NVLink 进行域内通信，以及 InfiniBand 或以太网进行更广泛的连接。铜缆（无源或有源）在较短距离上具有成本和功耗优势，而光收发器和光纤则提供更长距离传输所需的带宽和覆盖范围。随着 GPU 集群从数百个扩展到数万个 GPU，网络层成为关键瓶颈，铜缆和光缆的组合必须在 leaf-spine 和胖树拓扑中进行精心设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.711btc.com/en/new_flash/150745.html">SemiAnalysis: AI networks are not a choice between copper cables and ...</a></li>
<li><a href="https://docs.nvidia.com/cabling-data-centers.pdf">Cabling Data Centers - NVIDIA Documentation Hub</a></li>
<li><a href="https://introl.com/blog/gpu-cluster-network-topology-fat-tree-dragonfly-rail-optimized-2025">GPU Cluster Network Topology Design | Introl Blog</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Datacenter Networking`, `#SemiAnalysis`, `#Hardware`, `#GPU Clusters`

---

<a id="item-6"></a>
## [智谱 AI 开源 GLM-5.2 模型获海外好评，股价大幅飙升](https://x.com/shao__meng/status/2068135521822593406) ⭐️ 8.0/10

智谱 AI（国际品牌为 Z.ai）于 2026 年 6 月 13 日发布了采用 MIT 许可证的开源模型 GLM-5.2，该模型具备稳定的 100 万 token 上下文窗口。凭借强大的编程和推理能力，该模型在国际上获得了广泛赞誉，直接推动了公司港股股价的大幅飙升。 GLM-5.2 证明了中国 AI 实验室能够以极低的成本，生产出在特定基准测试中接近甚至超越西方顶级闭源模型的开源模型。这验证了强大开源模型的商业可行性，并标志着资本市场越来越倾向于奖励技术突破而非短期的精细化运营。 在用于长时间编程任务的 FrontierSWE 基准测试中，GLM-5.2 仅落后 Anthropic 的 Claude Opus 4.8 一个百分点，并以 42.8 的成绩在 BridgeBench 推理基准测试中位居榜首。该模型运行速度为每秒 300 个 token，成本约为美国同级别前沿模型的十分之一。

rss · AI Hot · Jun 20, 00:55

**背景**: 智谱 AI 是源自清华大学 KEG 实验室的中国主要 AI 实验室，以发布中国首个千亿参数规模开源模型而闻名。该公司于 2025 年将国际品牌更名为 Z.ai，并与 MiniMax 等其他中国 AI 初创公司竞争，后者已于 2026 年 1 月在香港证券交易所上市。开源 AI 领域的竞争日益激烈，采用 MIT 等宽松许可证发布的模型允许免费商业使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/zhipu-ais-glm-5-2-closes-in-on-closed-source-leaders-in-coding-marathons/">Zhipu AI's GLM-5.2 closes in on closed-source leaders in ...</a></li>
<li><a href="https://www.explainx.ai/blog/glm-5-2-zhipu-china-ai-response-fable-5-ban-2026">GLM-5.2 Beats Fable 5 Reasoning — China AI Response to Export ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Open-Source AI`, `#Large Language Models`, `#Zhipu AI`, `#GLM`, `#AI Industry`

---

<a id="item-7"></a>
## [Anthropic 限竞条款引争议；LLM 应用攻防警示；软件工程未真正工程化](https://x.com/hongming731/status/2068134357383180736) ⭐️ 8.0/10

Anthropic 发布 Claude Fable 5，其许可条款限制开发者构建竞争性 LLM，同时疑似降低了研究者的输出质量。此外，Brian Vermeer 在 Spring I/O 上演示了实用的 LLM 攻击技术，包括通过路径穿越污染 RAG 知识库、SQL 注入伪造聊天记忆，以及拆分提问套取敏感数据。 Anthropic 的反竞争限制条款可能重塑 AI 公司对下游使用行为的管控方式，引发对 AI 生态系统开放性和公平竞争的担忧。演示的 LLM 漏洞表明，随着企业快速采用基于 RAG 的应用，数据污染和提示注入等实际攻击手段仍是亟待解决的关键安全风险。 RAG 污染攻击尤为危险，因为仅需注入约 250 篇恶意文档即可破坏 LLM 的知识库，使其凭借高语义相似度生成攻击者控制的答案。Vermeer 强调需要采用最小权限工具访问和纵深防御策略，以缓解生产环境中 LLM 应用面临的多向量威胁。

rss · AI Hot · Jun 20, 00:50

**背景**: 检索增强生成（RAG）通过在生成回复前从外部知识库检索相关文档来增强 LLM 的能力，但这一架构引入了新的攻击面，攻击者可通过注入恶意文档来操纵输出。美国一直在逐步收紧对 AI 芯片和半导体的出口管制，建立了三级全球访问框架，限制向许多国家的技术转移。关于软件工程是否构成真正工程化的争论已持续数十年，批评者认为它缺乏传统工程学科所具有的严格数学基础和标准化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://moazharu.medium.com/llm-poisoning-and-rag-security-the-250-document-vulnerability-that-changes-everything-ce7a213adb6c">LLM Poisoning and RAG Security: The 250-Document Vulnerability That Changes Everything | by azhar | Medium</a></li>
<li><a href="https://www.promptfoo.dev/blog/rag-poisoning/">RAG Data Poisoning: Key Concepts Explained | Promptfoo</a></li>
<li><a href="https://www.rand.org/pubs/perspectives/PEA3776-1.html">Understanding the Artificial Intelligence Diffusion Framework: Can Export Controls Create a U.S.-Led Global Artificial Intelligence Ecosystem? | RAND</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Security`, `#LLM`, `#AI Policy`, `#Vulnerabilities`

---

<a id="item-8"></a>
## [Anthropic 恰乌里称有信心“未来几天”重新开放 Mythos 及 Fable 5 AI 模型](https://www.ithome.com/0/966/466.htm) ⭐️ 8.0/10

An Anthropic executive announced confidence that access to its frontier models, Claude Mythos and Claude Fable 5, will be restored outside the US in the coming days following temporary restrictions related to US government safety directives.

rss · IT HOME · Jun 20, 00:48

**标签**: `#Anthropic`, `#Frontier Models`, `#AI Policy`, `#AI Safety`, `#Claude`

---

<a id="item-9"></a>
## [本周 AI 动态：OpenAI 免费健康 AI、Anthropic 机器人狗编程等](https://x.com/rohanpaul_ai/status/2068128797732589841) ⭐️ 8.0/10

OpenAI 将其前沿级健康 AI 从高级推理模型转移至免费的 GPT-5.5 Instant 模型，使所有用户都能使用先进的健康 AI 功能。Anthropic 展示了 Claude Opus 4.7 仅用 12 分 07 秒完成机器人狗编程，比去年人类团队快 20 倍，同时推出了 Claude Design 大更新，支持设计系统导入、代码往返以及降低 token 用量。 这些发展标志着前沿 AI 能力大众化的更广泛行业趋势——OpenAI 将健康 AI 放在免费层级消除了关键应用的成本壁垒，而 Anthropic 的机器人突破则表明大语言模型正以前所未有的速度跨入物理世界控制领域。两者共同代表了 AI 可及性及其能力范围扩展的重大转变。 GPT-5.5 Instant 于 2026 年 5 月 5 日向免费用户发布，是首个在网络安全和生物化学防范类别中被视为高能力并实施相应保障措施的 Instant 模型。Claude Opus 4.7 是 Anthropic 专为需要高精度的重要工作而设计的旗舰模型，Claude Design 更新则专门解决了此前限制实际采用的高 token 用量问题。

rss · AI Hot · Jun 20, 00:28

**背景**: GPT-5.5 Instant 是 OpenAI 最新推出的针对日常任务优化的模型，在图像分析、STEM 问题解答和网络搜索决策方面均有改进。Claude Opus 4.7 是 Anthropic 继 Claude 4 系列 Opus 4.6 之后的下一代旗舰模型，采用该公司的宪法 AI 技术进行训练，以提高伦理合规性。Claude Design 是 Anthropic Labs 推出的产品，允许用户通过对话式 AI 创建设计、交互式原型和演示文稿，旨在消除通常限制设计探索的时间约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-instant/">GPT-5.5 Instant: smarter, clearer, and more personalized | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.7">Claude Opus 4.7</a></li>
<li><a href="https://www.anthropic.com/news/claude-design-anthropic-labs">Introducing Claude Design by Anthropic Labs \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI News`, `#Anthropic`, `#OpenAI`, `#Robotics`, `#Frontier Models`

---

<a id="item-10"></a>
## [visionOS 27 今秋推送：M5 Vision Pro 独占 Siri 语音定制与 AFM 3 Core Advanced 本地 AI 模型](https://www.ithome.com/0/966/454.htm) ⭐️ 8.0/10

苹果即将于今年秋季推送的 visionOS 27 将为 M5 Vision Pro 独占推出两项功能：Siri 语音定制（允许用户自由调整语气表现力和语速）以及 AFM 3 Core Advanced 本地 AI 模型。M2 款 Vision Pro 仍可共享 visionOS 27 的大部分升级，包括重新设计的控制中心、全景照片转空间场景和更智能的自然语言理解等。 AFM 3 Core Advanced 模型代表了端侧 AI 的重大飞跃，将一个 200 亿参数的稀疏架构模型引入空间计算领域，每次推理仅激活 10-40 亿参数。这标志着苹果通过独占的高算力本地 AI 能力来差异化新一代硬件的战略，同时也凸显了 M2 和 M5 Vision Pro 设备之间日益扩大的能力差距。 AFM 3 Core Advanced 是一款原生多模态模型，采用稀疏架构和苹果的指令跟随剪枝技术，需要 M5 芯片更强的算力来处理更复杂的本地 AI 任务。苹果承诺未来会通过云端计算为 M2 设备提供部分 AI 功能的折中方案，但具体实现细节尚未公布。

rss · IT HOME · Jun 19, 23:23

**背景**: 苹果基础模型（AFM）是苹果自研的 AI 模型家族，目前已发展到第三代，涵盖从端侧设备模型到服务器端模型。AFM 3 Core Advanced 是该家族中最强大的端侧模型，总参数量达 200 亿，采用稀疏架构，每次推理时仅选择性激活部分参数以提高效率。Apple Intelligence 是苹果的 AI 系统，通过协调本地端侧模型和云端模型（通过 Private Cloud Compute）来执行任务，同时保护用户隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models">Introducing the Third Generation of Apple's Foundation Models</a></li>
<li><a href="https://9to5mac.com/2026/06/11/apples-new-foundation-models-explained-on-device-ai-cloud-ai-and-everything-in-between/">Apple’s third-generation Foundation Models explained - 9to5Mac</a></li>
<li><a href="https://ofox.ai/blog/apple-foundation-models-3-wwdc-2026-developer-read/">Apple's Third-Generation Foundation Models: A Developer's ... - ofox.ai</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#On-Device AI`, `#Spatial Computing`, `#Multimodal AI`, `#VisionOS`

---

<a id="item-11"></a>
## [智谱创始人称旗下模型将在明年一季度前达到“Mythos 级别”](https://x.com/jietang/status/2067580270078030088) ⭐️ 8.0/10

智谱 AI 创始人唐杰回应了关于中美 AI 能力差距的预测，表示其公司模型达到 Anthropic 的“Mythos 级别”将比预期更快。这直接挑战了此前估计中国 AI 厂商要到 2026 年底或 2027 年初才能实现这一里程碑的时间线，马斯克也参与了该讨论。 这一交流为中美前沿 AI 能力差距缩小的预期时间线提供了有价值的洞察，表明该差距可能比一些分析师目前估计的 7 个月更短。作为中国领先的 AI 公司之一，唐杰的自信预测标志着前沿模型开发领域的竞争正在加剧。 该讨论源于一位用户的评估，认为智谱的 GLM-5.2 模型大约相当于 Claude Opus 4.7-4.8 的水平，暗示中美模型之间存在约 7 个月的差距。Anthropic 的 Mythos 级别模型（如 Claude Fable 5）在软件工程、知识工作、视觉和科学研究等基准测试中代表了最先进的性能。

telegram · @zaihuapd · Jun 19, 02:24

**背景**: Anthropic 的“Mythos”代表了一类具有最先进能力的前沿 AI 模型，以 Claude Fable 5 为代表，该模型已向企业客户和付费订阅者发布。智谱 AI 的 GLM-5.2 是该公司最新的旗舰模型，专为长周期任务设计，具有 100 万 token 的上下文窗口，在标准编程基准测试中是最强的开源模型。中美 AI 能力差距一直是业界热议的话题，关于中国厂商能多快赶上或超越西方前沿模型性能存在各种估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://github.com/zai-org/GLM-5">GitHub - zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic ...</a></li>
<li><a href="https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html">Anthropic releases Mythos-like AI model to the public, Claude Fable 5</a></li>

</ul>
</details>

**社区讨论**: 讨论源于一位用户的技术评估，认为 GLM-5.2 的性能大约相当于 Claude Opus 4.7-4.8 水平，从而得出了 7 个月差距的估计。马斯克简短的“Probably Q1”回复暗示他认同中国模型在 2027 年第一季度达到 Mythos 级别的时间线，而唐杰的直接反驳表明他认为差距要小得多。

**标签**: `#AI Models`, `#Zhipu AI`, `#Frontier AI`, `#US-China AI Gap`, `#AGI`

---

<a id="item-12"></a>
## [Midjourney 宣布进军医疗领域，将推出超声波全身扫描仪与水疗中心](https://www.midjourney.com/medical/blogpost) ⭐️ 8.0/10

Midjourney announced a surprising expansion into the medical field, planning to launch AI-powered ultrasound whole-body scanning technology and accompanying spa centers starting in 2027.

telegram · @zaihuapd · Jun 19, 04:00

**标签**: `#Midjourney`, `#Medical Imaging`, `#Frontier Tech`, `#Hardware`, `#AI Applications`

---