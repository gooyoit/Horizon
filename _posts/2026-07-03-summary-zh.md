---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> From 110 items, 12 important content pieces were selected

---

1. [美团 LongCat-2.0 发布，OpenAI 推理成本减半等 AI 动态](#item-1) ⭐️ 9.0/10
2. [字节跳动 Seed 发布 EdgeBench：专测 AI 智能体长时间任务能力](#item-2) ⭐️ 9.0/10
3. [Anthropic 将 Claude Code 进化为全公司级 Claude Tag 平台](#item-3) ⭐️ 8.0/10
4. [美国商务部禁止差分隐私技术，引发专家强烈谴责](#item-4) ⭐️ 8.0/10
5. [Google 发布 Nano Banana 2 Lite 与 Gemini Omni Flash](#item-5) ⭐️ 8.0/10
6. [PerceptionRubrics：将多模态评估校准至人类感知](#item-6) ⭐️ 8.0/10
7. [Anthropic 详解 Claude Fable 5 网络安全分类器与越狱严重性框架](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 自主调度 22 个 Agent 完成 SEO/GEO 全流程优化](#item-8) ⭐️ 8.0/10
9. [Claude Fable 5 因过度安全防护导致能力大幅削弱](#item-9) ⭐️ 8.0/10
10. [Meta 拟出售富余 AI 算力，引发韩国股市大幅抛售](#item-10) ⭐️ 8.0/10
11. [OpenAI 提议让美国政府持有主要 AI 公司 5% 股份](#item-11) ⭐️ 8.0/10
12. [Anthropic 洽谈由三星代工自研 AI 芯片](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美团 LongCat-2.0 发布，OpenAI 推理成本减半等 AI 动态](https://aihot.virxact.com/items/cmr48jkqb01jysl3gjo27vxoi) ⭐️ 9.0/10

A high-signal AI news digest highlighting Meituan's LongCat-2.0 model, OpenAI's halved inference costs, Anthropic's new Claude Science initiative, and Meta's massive token consumption.

rss · AI Hot · Jul 3, 00:42

**标签**: `#AI Models`, `#Inference Cost`, `#LLM`, `#AI Industry`, `#Frontier AI`

---

<a id="item-2"></a>
## [字节跳动 Seed 发布 EdgeBench：专测 AI 智能体长时间任务能力](https://aihot.virxact.com/items/cmr47gz8u019usl3gk5yymk6x) ⭐️ 9.0/10

字节跳动 Seed 推出了 EdgeBench，这是一个开源基准，专门用于评估 AI 智能体在耗时 12 至 72 小时的复杂真实世界任务中的表现。在累计运行了约 38000 小时的智能体评估后，研究人员发现智能体的性能精确遵循 log-sigmoid 曲线，且顶级模型的学习速度正每三个月翻倍一次。 该基准通过提供一种标准化的方法来衡量长时间跨度的自主能力，填补了 AI 研究中的一个关键空白，这对于未来的通用智能体至关重要。所发现的学习速度缩放定律提供了具体的量化证据，表明 AI 智能体在处理持续性、复杂工作流方面正在快速进步。 该基准目前包含 134 个任务中的 51 个开源任务，涵盖科学、软件工程、优化和形式数学等六大类别。智能体在本地工作区中通过快速试错进行操作，并接收来自隐藏裁判的反馈，而这些任务的人类平均完成时间为 57.2 小时。

rss · AI Hot · Jul 3, 00:15

**背景**: 长时间跨度任务要求 AI 智能体执行数十或数百个连续步骤，在较长时间内保持意图的连贯性，并自主从错误中恢复。与单轮查询不同，这些任务会持续数小时或数天，因此成为评估智能体 AI 在现实世界中实用性的关键基准。此前的研究（如 METR 的时间跨度追踪）表明，AI 智能体能够完成的任务长度一直在呈指数级增长，尽管字节跳动的发现表明这种加速趋势甚至更快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/tech/7gby8q0r">ByteDance-Seed releases EdgeBench, showing AI agent performance ...</a></li>
<li><a href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/">Measuring AI Ability to Complete Long Tasks - METR</a></li>
<li><a href="https://www.ai21.com/glossary/ai-agent/what-are-long-horizon-tasks/">What are Long-Horizon Tasks? - AI21</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Benchmark`, `#ByteDance Seed`, `#Long-Horizon Tasks`, `#Frontier AI`

---

<a id="item-3"></a>
## [Anthropic 将 Claude Code 进化为全公司级 Claude Tag 平台](https://aihot.virxact.com/items/cmr49gi1s001rslvaoeia6ynk) ⭐️ 8.0/10

据报道，Anthropic 已将其内部工程工具 Claude Code 转型为全公司使用的结构化 Agent 平台 Claude Tag，目前已接入其最强模型 Claude Fable 5。该工具最初由工程师为编写代码和运行 Agent 而开发，现已演变为跨部门协作平台，通过结构化 Agent 界面开放最强模型的能力。 这一演进展示了企业级 AI Agent 部署的重大进展，说明了内部工程工具如何扩展为全组织范围的协作平台。它让人们得以一窥 Anthropic 这样的顶级 AI 实验室如何构建内部的人机协作工作流，这可能为跨部门 AI 集成的行业实践提供参考。 Claude Tag 已接入 Claude Fable 5，这是 Anthropic 迄今为止能力最强的模型，在软件工程、知识工作、视觉和科学研究等基准测试中均达到业界领先水平。该平台采用结构化 Agent 界面，意味着它为 AI Agent 的运行和交互提供了明确的框架，而非自由形式的聊天交互。

rss · AI Hot · Jul 3, 01:31

**背景**: Claude Code 是 Anthropic 的 Agent 编码系统，能够跨整个项目运行，理解代码库、执行多文件更改并自主完成开发任务。Claude Fable 5 是 Anthropic 最新、最强大的模型，具有默认始终开启且无法禁用的自适应思维模式。结构化 Agent 平台的概念是指在特定操作模式的定义框架内运行 AI Agent 的系统，区别于非结构化的对话式 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Agents`, `#Claude`, `#Internal Tools`, `#Enterprise AI`

---

<a id="item-4"></a>
## [美国商务部禁止差分隐私技术，引发专家强烈谴责](https://aihot.virxact.com/items/cmr49t25u0079slvav2k0l01k) ⭐️ 8.0/10

2026 年 6 月 4 日，美国商务部发布指令 DAO 216-26，禁止在经济分析局和人口普查局出版物中使用差分隐私等现代隐私保护技术，仅允许粗化（四舍五入、聚合、范围化）和压制等过时方法，并取消了 2030 年人口普查的差分隐私方案。 该指令标志着重大政策倒退，将同时降低数据可用性和削弱公民隐私保护。差分隐私是安全 AI 模型训练和隐私保护机器学习的基础数学框架，禁止该技术将破坏对算法公平性和现代数据治理至关重要的数据基础设施。 该指令明确禁用了多项已使用多年的技术：自 1990 年用于人口普查的交换技术、自 2002 年用于季度劳动力指标的输入噪声注入、以及自 2008 年用于 OnTheMap 的差分隐私。哈佛教授 Cynthia Dwork 等专家联名指出，此举绕过了法定程序，服务于政治利益而非科学严谨性。

rss · AI Hot · Jul 3, 01:28

**背景**: 差分隐私是由 Cynthia Dwork 等人共同开发的严格数学框架，通过向数据集或查询中注入经过校准的噪声来提供形式化的隐私保证。与数据压制（删除字段）、粗化（数值四舍五入）或 k-匿名等传统匿名化方法不同，差分隐私无论攻击者拥有什么辅助信息，都能提供可证明的重标识攻击防护保证。它已成为隐私保护数据发布的黄金标准，被广泛应用于机器学习流程中以保护训练数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/522721297">（1）差分隐私算法基础——差分隐私的介绍 - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/671263684">简析数据匿名化的方法、挑战与应用实践 - 知乎</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cynthia_Dwork">Cynthia Dwork - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Differential Privacy`, `#AI Policy`, `#Data Governance`, `#Privacy-Preserving AI`, `#Cynthia Dwork`

---

<a id="item-5"></a>
## [Google 发布 Nano Banana 2 Lite 与 Gemini Omni Flash](https://aihot.virxact.com/items/cmr488d3901dqsl3gwh7ryby4) ⭐️ 8.0/10

Google 发布了两款新的媒体生成模型：Nano Banana 2 Lite（也称为 Gemini 3.1 Flash-Lite Image）和 Gemini Omni Flash。两款模型现已在 Gemini 应用和 API 中全面可用，其中 Nano Banana 2 Lite 可在 4 秒内生成 1K 分辨率图片，Omni Flash 则以每秒 0.10 美元的价格提供多模态视频生成能力。 这两款模型的发布大幅降低了开发者在应用中集成图片和视频生成的成本和延迟门槛。以大约 1 美元 30 张图片的价格，Nano Banana 2 Lite 使 Google 在高性价比媒体生成 API 市场中具备了极强的竞争力，而 Omni Flash 则推动了能够在单一系统中处理视频、图片和文本的统一多模态模型的发展。 Nano Banana 2 Lite 的正式名称为 Gemini 3.1 Flash-Lite Image，是 Nano Banana 系列中速度最快、性价比最高的模型，1K 分辨率下每美元约可生成 30 张图片。Gemini Omni Flash 专为视频生成和对话式编辑优化，能够同时输出视频和文本响应，定价为每秒生成内容 0.10 美元。

rss · AI Hot · Jul 3, 00:40

**背景**: Nano Banana 系列是 Google 基于 Gemini 架构构建的图片生成与编辑模型品牌，旨在提供高速视觉内容创作能力。Gemini Omni Flash 代表了 Google 在统一"全能"模型方面的进展，这类模型能够在单一模型中处理和生成文本、图片、音频和视频等多种模态的内容，而无需依赖多个独立的专用系统。整个行业的大趋势是提供更快、更便宜、更强大的多模态 AI 模型，并通过 API 供开发者使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-lite-and-gemini-omni-flash-available/">Nano Banana 2 Lite and Gemini Omni Flash available - Google Cloud</a></li>
<li><a href="https://deepmind.google/models/gemini-image/flash-lite/">Gemini 3.1 Flash-Lite Image - Nano Banana 2 Lite — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-omni-flash/">Gemini Omni Flash - Model Card — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#Image Generation`, `#Multimodal AI`, `#Generative AI`, `#API`

---

<a id="item-6"></a>
## [PerceptionRubrics：将多模态评估校准至人类感知](https://aihot.virxact.com/items/cmr47jyta01bgsl3gq0tpfu1k) ⭐️ 8.0/10

研究人员提出了 PerceptionRubrics，这是一个基于评分准则的评估框架，通过将密集的图像理解分解为原子化、可验证的评分准则，并引入门控评分机制。对 25 个多模态大语言模型（MLLM）的实验揭示了单个事实识别与一致性联合感知之间存在明显的可靠性差距，尤其在 GUI 等信息密集领域表现突出。 该框架解决了多模态 AI 模型中饱和的基准分数与实际应用脆弱性之间的关键差距，暴露了现有指标隐藏的感知失败。PerceptionRubrics 分数与人类偏好之间的高度一致性表明，它有望成为可靠多模态评估的新标准。 该框架实施了一种门控评分机制，要求模型同时满足所有组件评分准则，而不是允许基于粗略相似性的部分得分。它在 25 个 MLLM 上进行了验证，并揭示了模型在 GUI、图表和图示等信息密集视觉领域中的持续弱点。

rss · AI Hot · Jul 3, 00:26

**背景**: 当前的多模态基准测试通常显示接近饱和的分数，表明模型表现良好，然而这些模型在实际应用中却表现出显著的脆弱性。这种差异源于传统评估指标依赖粗略的相似性度量，可能掩盖感知失败——即模型能够识别单个事实，但无法同时一致地整合多个视觉事实。基于评分准则的评估通过将复杂的理解分解为原子化、可验证的标准来解决这一问题，从而实现更细粒度、更符合人类判断的评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.28322v1">[2606.28322v1] PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception</a></li>
<li><a href="https://arxiv.org/html/2606.28322v1">PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception</a></li>

</ul>
</details>

**标签**: `#Multimodal AI`, `#AI Evaluation`, `#Human-Computer Interaction`, `#Machine Learning`, `#AI Alignment`

---

<a id="item-7"></a>
## [Anthropic 详解 Claude Fable 5 网络安全分类器与越狱严重性框架](https://aihot.virxact.com/items/cmr46rbvk012esl3ggltylooc) ⭐️ 8.0/10

Anthropic 重新部署了 Claude Fable 5，其内置网络安全安全分类器将使用场景分为禁止使用、高风险双重用途、低风险双重用途和良性使用四个等级。此外，Anthropic 还与 Glasswing 合作发布了 AI 越狱严重性评估框架初稿，并启动了 HackerOne 漏洞赏金项目来收集越狱案例。 这一进展代表了 AI 安全治理从对所有安全失败一视同仁，转向基于风险的精细化网络安全管理方式。该框架可能为 AI 提供商如何衡量和应对越狱严重性建立行业标准，影响整个生态系统的未来 AI 监管和安全实践。 分类器直接拦截禁止使用和高风险双重用途类别，而低风险类别则进行部分监控，仅在安全边际内选择性拦截。拟议的越狱严重性框架被描述为初稿版本，HackerOne 项目则利用外部安全研究人员持续测试系统漏洞。

rss · AI Hot · Jul 3, 00:19

**背景**: 网络安全中的双重用途技术是指既能用于合法防御目的、也能用于恶意攻击目的的工具或能力，这给 AI 提供商带来了监管挑战。AI 越狱是指用户通过精心设计的提示词绕过模型的安全防护栏，以获取受限内容或功能。HackerOne 等漏洞赏金平台将组织与安全研究人员连接起来，研究人员通过测试系统漏洞获取奖励，这一模式正越来越多地应用于 AI 安全测试领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/fable-safeguards-jailbreak-framework">More details on Fable 5’s cyber safeguards and our jailbreak framework</a></li>
<li><a href="https://www.versaroc.co.jp/blog/the-new-4-axis-safety-standards-in-claude-fable-5-and-the-20-1782915385329">What the New 4-Axis Jailbreak Framework and Fab… | VERSAROC</a></li>
<li><a href="https://digg.com/tech/z5r036fk">The framework could restore access to Mythos and Fable.</a></li>

</ul>
</details>

**社区讨论**: 公众反应褒贬不一：支持者欢迎该框架从零容忍规则转向务实的严重性评分，认为这是平衡安全性与可用性的合理方式。然而，批评者则将其视为安全表演或企业和政府对 AI 访问权的控制手段。

**标签**: `#AI Safety`, `#Anthropic`, `#Cybersecurity`, `#Jailbreaking`, `#AI Governance`

---

<a id="item-8"></a>
## [Claude Fable 5 自主调度 22 个 Agent 完成 SEO/GEO 全流程优化](https://aihot.virxact.com/items/cmr4768yq013qsl3g29wasjnp) ⭐️ 8.0/10

名为 Claude Fable 5 的 AI 模型自主启动 22 个 Agent，进行了 40 分钟的调研，优化了 AIHOT 网站的 SEO 与 GEO 基础设施。该系统独立发现了流量异常，否定了有缺陷的 Cloudflare 方案并改用火山引擎 CDN，自行提交专业工单与人类工程师协作，最终在切换域名解析后 10 分钟内将 616 个海外请求成功路由至新线路。 这一案例展示了全自主 Agent 工作流在实际应用中的重大飞跃，AI 能够独立管理传统上需要高级运维工程师才能完成的复杂多步骤基础设施任务。其推理网络配置、与人类支持团队专业沟通以解决问题，以及主动修补安全漏洞的能力，充分展现了 AI 在生产环境中实现端到端自主任务完成的巨大潜力。 AI 否定了 Cloudflare 方案，原因是该方案无法实现国内直连与海外分流，且 Cloudflare 计划自 2026 年起默认拦截 AI 爬虫。当人类支持工程师漏答回源 IP 网段问题时，AI 礼貌追问并补充了备选方案，并在发现官方配置存在安全漏洞后，自行添加了暗号验证机制。

rss · AI Hot · Jul 3, 00:16

**背景**: GEO（生成式引擎优化）是一种针对 ChatGPT、Perplexity 和 Google Gemini 等 AI 驱动搜索引擎优化网站内容的策略，标志着从传统 SEO 的重大转变。CDN（内容分发网络）通过全球分布的服务器加速网页内容传输，需要正确配置回源 IP 白名单以确保 CDN 与源站之间的安全通信。互联网基础服务巨头 Cloudflare 近期宣布了默认拦截混合用途 AI 爬虫的政策，迫使 AI 公司将搜索爬虫与训练、智能体爬虫分离，否则需付费获取内容访问权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnblogs.com/cnabke/p/19808470">什么是 GEO ？ 一文看懂生成式引擎 优 化 （ Generative Engine ...</a></li>
<li><a href="https://www.ithome.com/0/971/510.htm">Cloudflare 细化网络爬虫屏蔽管理，将默认禁止 AI 代理与训练爬虫访问...</a></li>
<li><a href="https://blog.csdn.net/weixin_34290096/article/details/86006255">别让 CDN 的 回 源 把你的服务器拖垮，采用正确的 回 源 策略-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Autonomous Systems`, `#Claude`, `#SEO`, `#Infrastructure`

---

<a id="item-9"></a>
## [Claude Fable 5 因过度安全防护导致能力大幅削弱](https://aihot.virxact.com/items/cmr47bczi0163sl3gcs5wh1vi) ⭐️ 8.0/10

BridgeBench 基准测试结果显示，Anthropic 发布的 Claude Fable 5（底层为 Mythos 模型）因安全防护过度触发，在编程任务中出现严重能力退化。调试能力从 86.2 降至 25.9（降幅 70%），重构能力从 73.6 降至 38.4（降幅 48%），幻觉控制从 75.9 降至 61.7（降幅 19%），大量正常编程请求被误判为高风险。 这一案例清晰地揭示了 AI 安全防护与模型可用性之间的关键权衡，这是当前 AI 对齐研究和部署中的核心矛盾。据报道，付费用户在支付 Fable 5 价格的同时，模型却静默回退到更弱的 Opus 4.8，这对依赖前沿模型进行生产工作的企业客户在透明性和性价比方面提出了严重质疑。 据报道，过度触发的安全机制还限制了代码安全审查、新模型开发以及生化相关任务，甚至有指控称 prompt 被修改以生成错误结果。Anthropic 尚未对能力退化发布官方解释，用户无法得知是否会有修复方案。

rss · AI Hot · Jul 3, 00:06

**背景**: 过度拒绝是 LLM 安全对齐中一个被广泛记录的问题，模型将拒绝阈值设置得过于保守，导致它们拒绝恰好包含某些关键词或模式的良性请求。BridgeBench 是一个基准测试平台，通过调试、重构、UI 生成、安全性和幻觉控制等真实世界任务来评估 AI 编程模型。随着 AI 公司竞相部署更强的安全过滤器以防止有害输出，它们有可能削弱使模型本身有用的核心能力，这为整个行业带来了持续的安全校准挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bridgebench.ai/">BridgeBench — AI Coding & Vibe Coding Benchmark</a></li>
<li><a href="https://www.promptlayer.com/glossary/overrefusal/">What is Overrefusal in LLMs?</a></li>
<li><a href="https://www.bridgemind.ai/bridgebench">BridgeBench — The Open-Source Vibe Coding ... | BridgeMind</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Claude`, `#Anthropic`, `#LLM Evaluation`, `#Alignment`

---

<a id="item-10"></a>
## [Meta 拟出售富余 AI 算力，引发韩国股市大幅抛售](https://www.bloomberg.com/news/articles/2026-07-02/south-korean-stocks-tumble-6-as-ai-jitters-hurt-chipmakers) ⭐️ 8.0/10

Meta 正筹划向外部客户出售多余的 AI 算力和模型服务，实质性地进军云计算市场。该消息叠加苹果正洽谈向中国存储芯片厂采购芯片的报道，于 7 月 2 日引发韩国股市大幅抛售，Kospi 指数盘中最多跌 7%，三星电子和 SK 海力士一度均跌至少 8%。 Meta 的举措暗示大型科技公司可能在 AI 基础设施上投入过剩，引发了市场对全行业算力过剩及未来硬件采购放缓的担忧。对于半导体行业，尤其是三星和 SK 海力士等韩国存储巨头而言，这一转变叠加苹果将供应链向中国芯片厂多元化的趋势，正威胁其需求增长和竞争地位。 此次抛售幅度之大，致使韩国交易所触发了熔断机制，暂时中止了 Kospi 期货的程序化交易。Meta 潜在的算力变现策略与苹果可能转向长江存储（YMTC）等中国供应商采购面向中国市场的内存芯片，双重因素叠加加剧了投资者对韩国半导体双寡头前景的焦虑。

telegram · @zaihuapd · Jul 2, 02:29

**背景**: 大型科技公司一直在进行大规模的 AI 基础设施军备竞赛，大量采购 GPU（特别是英伟达的产品）以及来自三星和 SK 海力士的高带宽存储（HBM）芯片，用于训练大语言模型。云计算是通过互联网出租计算资源的业务，目前由亚马逊（AWS）、微软（Azure）和谷歌（GCP）主导。如果 Meta 从纯粹的 AI 算力消费者转变为卖家，它将直接与这些成熟的云服务商竞争，同时暗示其内部 AI 训练需求可能正在趋于饱和。熔断机制是证券交易所用于在极端市场波动期间暂时停止交易的监管手段，旨在防止恐慌性抛售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/kospi-today-korea-stock-market-index-samsung-sk-hynix-chips-2026-7">Korea 's Kospi Falls As Investors Look Beyond the... - Business Insider</a></li>
<li><a href="https://www.koreatimes.co.kr/economy/20260304/krx-activates-circuit-breaker-on-kospi-kosdaq-halting-trade-for-20-minutes">KRX activates circuit breaker on KOSPI, KOSDAQ, halting trade ...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Meta`, `#Cloud Computing`, `#Semiconductors`, `#AI Market`

---

<a id="item-11"></a>
## [OpenAI 提议让美国政府持有主要 AI 公司 5% 股份](https://www.bloomberg.com/news/articles/2026-07-02/openai-proposes-giving-the-us-government-a-5-stake-ft-says) ⭐️ 8.0/10

OpenAI 提议让美国政府持有公司 5% 的股份，CEO Sam Altman 等高管建议可通过一个政府载体统一持有 OpenAI、Anthropic、Google 和 Meta 等美国主要 AI 公司各 5% 的股份。该提案旨在让公众直接分享 AI 热潮带来的经济收益。 该提案代表了美国政府与 AI 行业关系的潜在范式转变，模糊了这一最具战略重要性的技术领域中公私部门之间的界限。如果被采纳，它可能重塑 AI 治理格局，创造新的监管动态，并为全球各国政府与变革性科技公司的互动方式树立先例。 该提案设想建立一个统一的政府载体，同时持有多家主要 AI 公司的股权，这引发了关于监管冲突、控制权和竞争公平性的重大问题。目前尚不清楚 Google 和 Meta 等其他公司是否会接受这种安排，也未提供关于股权如何估值以及将赋予何种治理权的细节。

telegram · @zaihuapd · Jul 2, 06:02

**背景**: OpenAI 目前正处于从非营利组织向营利性结构转型的过程中，这已经引发了关于该公司造福人类这一最初使命的争论。AI 技术的快速商业化创造了巨大的财富，并引发了对经济不平等的担忧，因为 AI 带来的收益集中在少数科技公司及其投资者手中。全球各国政府正在努力解决如何在保持竞争力的同时监管 AI 的问题，而新治理模式的提案——包括持有公共股权——反映出人们越来越希望确保更广泛的公众能从 AI 驱动的经济转型中受益。

**标签**: `#AI Governance`, `#OpenAI`, `#Tech Policy`, `#AI Industry`, `#Equity Stake`

---

<a id="item-12"></a>
## [Anthropic 洽谈由三星代工自研 AI 芯片](https://www.theinformation.com/articles/anthropic-talks-samsung-manufacture-custom-ai-chip) ⭐️ 8.0/10

Anthropic 已开始开发自有 AI 芯片，并正在与三星电子洽谈潜在的制造合作。该项目旨在让 Anthropic 更好地掌控支撑其 Claude 模型的计算基础设施。 这一举措标志着 Anthropic 的重大战略转变，顺应了顶级 AI 实验室向定制芯片进行垂直整合以减少对 Nvidia GPU 依赖的行业大趋势。获得专属的芯片供应链可能会大幅降低推理成本，使 Anthropic 在日益激烈的 AI 军备竞赛中获得竞争优势。 该项目目前仍处于早期阶段，与 OpenAI 和 Google 等已经在自研服务器芯片上取得重大进展的竞争对手相比，Anthropic 进入定制芯片领域的时间相对较晚。三星正被考虑作为制造这些芯片的潜在代工合作伙伴。

telegram · @zaihuapd · Jul 2, 15:57

**背景**: 随着 AI 模型变得越来越大、越来越复杂，对计算能力的需求急剧上升，使得 AI 芯片成为该行业的关键瓶颈。Nvidia 凭借其备受追捧的 GPU 在这一领域占据主导地位，这促使 Google（凭借其 TPU）和 OpenAI 等主要 AI 公司设计自己的定制芯片。通过开发内部芯片，AI 实验室旨在专门针对自己的模型优化性能，同时降低成本并减轻依赖单一芯片供应商带来的供应链风险。

**标签**: `#Anthropic`, `#AI Chips`, `#AI Infrastructure`, `#Samsung`, `#Custom Silicon`

---