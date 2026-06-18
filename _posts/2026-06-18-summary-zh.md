---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 122 items, 12 important content pieces were selected

---

1. [Z.ai 发布 GLM-5.2：全新的领先开源权重纯文本大语言模型](#item-1) ⭐️ 10.0/10
2. [Transformer 共同作者 Noam Shazeer 加入 OpenAI](#item-2) ⭐️ 10.0/10
3. [美国暂缓将 DeepSeek 列入黑名单，同时将 100 多家企业列为安全风险](#item-3) ⭐️ 8.0/10
4. [泄露文件显示 OpenAI 每年亏损数十亿美元](#item-4) ⭐️ 8.0/10
5. [虚幻引擎 5.8 加入 MCP 插件，支持 Claude Code 自然语言建模](#item-5) ⭐️ 8.0/10
6. [Meta 将 30-50%的核心工程师转岗做 AI 数据标注](#item-6) ⭐️ 8.0/10
7. [Anthropic 推出 Claude Design 重大更新：导入设计系统、画布编辑器与 Claude Code 同步](#item-7) ⭐️ 8.0/10
8. [深入解析 Midjourney Scanner 技术内幕](#item-8) ⭐️ 8.0/10
9. [Midjourney 宣布首款硬件产品：全身超声波扫描仪](#item-9) ⭐️ 8.0/10
10. [UCSD 教授黄碧薇创办 Aether AI 完成 2000 万美元融资，押注因果世界模型](#item-10) ⭐️ 8.0/10
11. [蔚来全新世界模型开启推送，超 70 万用户同步升级](#item-11) ⭐️ 8.0/10
12. [Anthropic 5 月企业 AI 市场份额首次超越 OpenAI](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Z.ai 发布 GLM-5.2：全新的领先开源权重纯文本大语言模型](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 10.0/10

Z.ai 于 6 月 16 日在 MIT 许可证下发布了 GLM-5.2，该模型总参数量达 753B（通过混合专家架构激活 40B 参数），并拥有高达 100 万 token 的上下文窗口。它在 Artificial Analysis 智能指数中以 51 分的成绩登顶开源权重模型榜首，超越了 MiniMax-M3 和 DeepSeek V4 Pro 等竞争对手。 此次发布大幅缩小了免费开源权重模型与昂贵的闭源前沿模型之间的性能差距，以仅相当于 Claude Opus 十分之一左右的成本提供了接近前沿的能力。这展示了开源 AI 生态系统的快速发展步伐，使开发者和研究人员能够在不受供应商锁定的情况下，获取最先进的推理和编程能力。 GLM-5.2 是一个纯文本模型，Artificial Analysis 指出它相当消耗 token，在每个基准测试任务中约使用 43k 输出 token，而其前身 GLM-5.1 为 26k。尽管缺乏图像输入能力，它在 Code Arena WebDev 排行榜上前端开发类别中仍位列第二，并可通过 OpenRouter 等提供商获取，输入价格约为每百万 token 1.40 美元，输出约为每百万 token 4.40 美元。

rss · Simon Willison · Jun 17, 23:58

**背景**: 混合专家（MoE）是一种将模型参数拆分为多个“专家”的架构，在推理时仅激活一小部分专家，从而在不按比例增加计算成本的情况下提供高性能。“开源权重”是指公开发布已训练参数的 AI 模型，允许开发者在本地运行和微调模型，但这与真正的“开源”AI 不同，因为通常不包含训练数据和代码。上下文窗口决定了大语言模型在单次请求中能处理多少文本，100 万 token 的窗口使模型能够同时分析海量文档或代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source: What's the Real Difference? - neysa.ai</a></li>
<li><a href="https://www.morphllm.com/llm-context-window">What Is an LLM Context Window ? The Developer's Guide (2026)</a></li>

</ul>
</details>

**社区讨论**: 社区对该模型的性能和性价比充满热情，指出它以极低的价格提供了接近前沿的质量。然而，也有关于推理效率的显著担忧，一位用户报告称，在一个相对简单的编程任务中，该模型在写出第一个文件之前花费了超过 15 分钟和 45k 个 token。其他人也指出，虽然模型价格低廉，但其在推理过程中的高 token 消耗可能使其与中等算力的闭源模型相比，实际性价比不如最初看起来那么高。

**标签**: `#Large Language Models`, `#Open-Weights`, `#Artificial Intelligence`, `#Mixture of Experts`, `#Z.ai`

---

<a id="item-2"></a>
## [Transformer 共同作者 Noam Shazeer 加入 OpenAI](https://x.com/sama/status/2067427421083652131) ⭐️ 10.0/10

传奇 AI 研究员、Character.AI 联合创始人 Noam Shazeer 正式宣布离开 Google 并加入 OpenAI。Sam Altman 对此表示热烈欢迎，称 Shazeer 是自 OpenAI 创立以来他最想合作的人之一，认为十年的等待是值得的。 Shazeer 是 2017 年奠基性论文《Attention Is All You Need》的共同作者，该论文提出的 Transformer 架构是几乎所有现代大语言模型的基石，这使他成为 AI 领域最具影响力的人物之一。他的加入标志着 OpenAI 在前沿 AI 人才方面的重大整合，将数十年的深度学习专长直接注入其研究体系。 Shazeer 曾于 2024 年 8 月作为 Character.AI 授权协议的一部分回归 Google，但他在 Google 的任期十分短暂。在 Google 期间，他共同领导了 Gemini 项目，并曾为 Google AdSense 开发核心算法，展现出研究深度与产品工程能力的罕见结合。

rss · AI Hot · Jun 18, 02:01

**背景**: Noam Shazeer 于 2000 年加入 Google，在搜索、广告和 AI 领域做出了基础性贡献，包括 2017 年共同撰写了彻底改变自然语言处理领域的 Transformer 论文。2021 年，他与 Daniel De Freitas 共同创立了 Character.AI，在 ChatGPT 出现之前就推出了首批基于 Transformer 的聊天机器人服务之一。Character.AI 凭借用户与可定制 AI 角色对话的功能获得了巨大人气，但最终与 Google 达成了授权协议。Shazeer 的职业生涯涵盖了现代深度学习的整个发展脉络，从 Google 早期的神经网络研究到前沿模型的开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noam_Shazeer">Noam Shazeer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Character.ai">Character.ai</a></li>
<li><a href="https://www.noamshazeer.com/">Noam Shazeer | AI Scientist, Google Gemini Co-Lead</a></li>

</ul>
</details>

**社区讨论**: Sam Altman 幽默地表示，他们无法解释为什么叫 'Noam' 的人如此擅长 AI，只能将其归功于神恩。AI 社区的整体反应充满了兴奋和震撼，许多人将此视为 OpenAI 在顶级 AI 研究人才竞争格局中的一次重大胜利。

**标签**: `#OpenAI`, `#Noam Shazeer`, `#AI Talent`, `#Frontier AI`, `#Industry News`

---

<a id="item-3"></a>
## [美国暂缓将 DeepSeek 列入黑名单，同时将 100 多家企业列为安全风险](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

美国政府决定不将中国 AI 公司 DeepSeek 列入实体清单黑名单，同时将 100 多家其他企业列为安全风险。尽管美国对中国 AI 技术的快速发展持续担忧，并已对多家中国科技企业实施出口管制措施，但仍做出了这一决定。 DeepSeek 未被列入黑名单意义重大，因为该公司一直是全球 AI 竞赛中的主要颠覆者，据报道其 V3 模型的训练成本仅为 600 万美元，而 OpenAI 的 GPT-4 耗资 1 亿美元。这一决定表明美国在 AI 竞争中采取了更为细致的策略——在国家安全关切与认识到过度限制可能无法有效减缓中国 AI 进步之间寻求平衡。 被列入实体清单并不意味着完全禁止所有贸易；它主要限制美国公司向清单上的实体销售商品和服务，但仍允许从这些实体购买。值得注意的是，近前沿模型 GLM 5.2 的制造商 Z.ai 自 2025 年 1 月起就已在实体清单上，但中国 AI 公司对美国商品的主要依赖——英伟达 GPU——本就已受到出口限制。

hackernews · giuliomagnifico · Jun 17, 03:55 · [社区讨论](https://news.ycombinator.com/item?id=48565498)

**背景**: DeepSeek 由梁文锋于 2023 年 7 月创立，由对冲基金幻方出资，在 2025 年 1 月以 DeepSeek-R1 模型震惊了 AI 行业，该模型以极低的训练成本匹敌了 OpenAI 的 GPT-4 和 o1。该公司通过混合专家架构等创新，以及在现有芯片出口限制下使用性能较弱的 AI 芯片、整体使用更少的芯片来实现这一突破。美国实体清单由商务部工业与安全局维护，限制向被认定对美国国家安全或外交政策利益构成风险的外国实体出口特定物品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Entity_List">Entity List - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些用户赞赏 DeepSeek 在编程任务中的实用性，认为它价格实惠且适合日常开发工作，而另一些人则对美国的贸易限制表示不满，认为其虚伪且难以执行。一位具备技术背景的评论者指出，被列入实体清单对中国 AI 公司的实际影响有限，因为它们对美的主要依赖——英伟达 GPU——本就已受到出口限制，还有用户表示在编程工作流中更倾向于使用 DeepSeek 而非 Google Gemini 等替代方案。

**标签**: `#DeepSeek`, `#AI-Geopolitics`, `#Export-Controls`, `#AI-Labs`, `#Regulation`

---

<a id="item-4"></a>
## [泄露文件显示 OpenAI 每年亏损数十亿美元](https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/) ⭐️ 8.0/10

泄露的财务文件显示，OpenAI 每年正承受数十亿美元的巨额亏损，主要原因是天文数字的研发支出和高昂的运营成本。文件还显示，虽然 ChatGPT 拥有超过 9 亿的周活跃用户，但其中只有约 5000 万是付费订阅用户。 这些亏损凸显了前沿 AI 实验室面临的巨大财务压力，并对当前大语言模型商业模式的长期可持续性提出了严重质疑。如果投资者失去耐心，这些单位经济效益可能会重塑更广泛的 AI 行业，可能减缓开发周期或迫使行业转向更便宜、更高效的模型。 泄露的数据显示，SG&A（销售、一般及行政）费用约占收入的 55%，评论者指出这对于一家科技公司来说异常高。研发成本占据了支出的最大份额，据报道该公司每个付费客户的销售和营销支出约为 100 美元。

hackernews · greenchair · Jun 17, 21:31 · [社区讨论](https://news.ycombinator.com/item?id=48577208)

**背景**: 像 OpenAI 开发的前沿 AI 模型代表了目前最先进的 AI 系统，在训练和推理阶段都需要大量的计算资源。训练这些模型的成本涉及数千个 GPU 长时间运行，而由于模型规模和延迟要求，推理成本仍然很高。IDC 等公司的行业分析表明，企业通常将 AI 基础设施成本低估 30-70%，对于持续高利用率的工作负载，本地基础设施的每百万 token 成本可比云定价低 8 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/ai-infrastructure-costs-what-you-need-know-before-scaling-fuaaf">AI Infrastructure Costs : What You Need to Know Before Scaling...</a></li>
<li><a href="https://byteiota.com/ai-infrastructure-roi-crisis-why-72-fail-gartner-2026/">AI Infrastructure ROI Crisis: Why 72% Fail (Gartner 2026) | byteiota</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**社区讨论**: 评论者对于这些亏损是令人担忧还是可控存在严重分歧。一些人强调 55%的 SG&A 比率不可持续，研发成本虽然可以削减但永远不会降到零；另一些人则认为单位经济效益比预期要好，盈利只是大规模扩张的问题。一个反复出现的担忧是，当 DeepSeek 等更便宜的替代品存在时，将 9 亿免费用户转化为付费订阅者的困难，还有一位评论者戏称 OpenAI 实际上是在以非营利组织的方式运营。

**标签**: `#OpenAI`, `#AI Economics`, `#Frontier Models`, `#Tech Industry`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [虚幻引擎 5.8 加入 MCP 插件，支持 Claude Code 自然语言建模](https://x.com/xiaohu/status/2067430287336992907) ⭐️ 8.0/10

Unreal Engine 5.8 introduces an experimental MCP plugin that enables developers to generate complex 3D scenes, cities, and environmental lighting using natural language prompts via Claude Code.

rss · AI Hot · Jun 18, 02:12

**标签**: `#Unreal Engine`, `#Claude`, `#MCP`, `#Generative AI`, `#3D Modeling`

---

<a id="item-6"></a>
## [Meta 将 30-50%的核心工程师转岗做 AI 数据标注](https://x.com/deedydas/status/2067428043195621454) ⭐️ 8.0/10

据报道，Meta 已将其核心团队中 30-50%的软件工程师重新分配到名为"Agent Data Optimization"的部门担任数据标注员。这些工程师的主要任务是对 AI 生成的 GitHub 代码仓库进行审查并提供人类反馈，以优化智能体（Agent）的训练数据。 这一举措标志着顶级 AI 实验室在获取高质量训练数据方面发生了重大战略转变，表明专家级的人类反馈正变得极其宝贵。它凸显了一个行业趋势：随着 AI 模型开始处理智能体编程等日益复杂的任务，企业宁愿牺牲昂贵的工程人才，也要生成下一代突破所需的专用 RLHF 数据。 这些工程师专门负责评估 AI 生成的代码仓库，这需要深厚的编程专业知识，而非基础的标注技能。这表明 Meta 正在积极训练自主编程智能体，并需要高度专业的技术反馈来提升其性能。

rss · AI Hot · Jun 18, 02:03

**背景**: 基于人类反馈的强化学习（RLHF）是一种机器学习技术，它通过基于人类评估训练出的奖励模型来引导 AI 模型的行为。随着 AI 开发转向构建能够执行编写和调试代码等多步骤任务的自主智能体，训练数据的质量变得至关重要。智能体训练数据需要专家级的人类来评估复杂的工具使用流程和逐步推理过程，这使得基础的众包标注无法满足前沿模型开发的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/">What is RLHF? - Reinforcement Learning from Human Feedback Explained - AWS</a></li>
<li><a href="https://toloka.ai/">Toloka Training data for AI agents and LLMs</a></li>

</ul>
</details>

**标签**: `#Meta`, `#RLHF`, `#Data Labeling`, `#AI Agents`, `#AI Industry`

---

<a id="item-7"></a>
## [Anthropic 推出 Claude Design 重大更新：导入设计系统、画布编辑器与 Claude Code 同步](https://x.com/rohanpaul_ai/status/2067424399603696030) ⭐️ 8.0/10

Anthropic 对 Claude Design 进行了重大更新，新增了从代码仓库或设计文件导入团队现有设计系统的功能，使输出能够匹配实际的品牌规范。此次更新还引入了支持拖拽和调整大小的新交互式画布编辑器，以及与 Claude Code 的直接同步功能，从而在无需手动重建的情况下打通设计与工程。 此次更新通过确保生成的设计遵循现实世界的品牌指南，而非仅依赖模型自身的审美判断，显著增强了 AI 驱动的 UI/UX 工作流。与 Claude Code 的无缝集成消除了设计与工程团队之间的传统摩擦，有望改变产品界面的原型设计和构建方式。 新的画布编辑器允许直接对元素进行拖拽、调整大小和对齐等操作，通过避免重新生成整个模型，大幅减少了 token 浪费。此次更新还修复了早期版本中 token 消耗过重的问题，Anthropic 还计划将 Claude Design 与 Canva、Adobe、Vercel、Replit、PDF 和 PowerPoint 等工具打通。

rss · AI Hot · Jun 18, 01:49

**背景**: Claude Design 是 Anthropic Labs 推出的一款产品，允许用户通过对话式 AI 创建设计、交互式原型和演示文稿。Claude Code 是 Anthropic 的智能体编码系统，能够跨整个项目运作，理解代码库、编辑文件并自主执行多文件更改。设计系统是由可复用组件组成的集合，受明确标准指导，帮助团队一致地构建产品；此次更新确保了 AI 生成的输出能够尊重这些已有的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-design-anthropic-labs">Introducing Claude Design by Anthropic Labs \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/14604416-get-started-with-claude-design">Get started with Claude Design | Claude Help Center</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI Design`, `#UI/UX`, `#AI Coding`

---

<a id="item-8"></a>
## [深入解析 Midjourney Scanner 技术内幕](https://x.com/midjourney/status/2067422898407837797) ⭐️ 8.0/10

Midjourney 发布了一篇技术深潜文章，探讨了其全新推出的 'Scanner' 功能的内部工作原理，该功能旨在分析和解读图像。这标志着 Midjourney 的核心能力从纯粹的图像生成领域，正式扩展到了多模态图像分析领域。 这一进展标志着 Midjourney 的战略升级，从一个纯粹的生成式 AI 工具演变为一个能够同时创建和理解视觉内容的综合性多模态平台。这也使得该公司能够更直接地与其他在复杂图像解读任务中表现出色的领先多模态 AI 视觉模型展开竞争。 Scanner 功能代表了向双向多模态 AI 的转变，使得系统不仅能够根据文本生成图像，还能对现有的视觉输入进行逆向工程或深度分析。虽然最初的公告中具体的架构细节仍然有限，但该功能利用了最先进的视觉模型技术来进行全面的图像评估。

rss · AI Hot · Jun 18, 01:43

**背景**: 多模态 AI 是指能够同时处理和理解来自多种感官模式或数据类型（包括图像、视频和文本）信息的人工智能系统。在生成式 AI 的语境下，这种能力使模型能够执行复杂的任务，例如评估图像质量、解读视觉内容，以及生成关于给定图像所含内容的详细文本描述。领先的 AI 实验室一直在快速推进这些视觉模型的发展，不断突破跨各种领域的自动化图像分析边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://garystafford.medium.com/evaluating-image-quality-using-nine-different-multimodal-generative-ai-vision-models-a1044de936e3">Quantitative and Qualitative Image Analysis Using Nine Different Multimodal Generative AI Vision Models | by Gary A. Stafford | Medium</a></li>
<li><a href="https://cloud.google.com/use-cases/multimodal-ai">Multimodal AI | Google Cloud</a></li>

</ul>
</details>

**标签**: `#Midjourney`, `#Computer Vision`, `#Image Analysis`, `#Generative AI`, `#Multimodal AI`

---

<a id="item-9"></a>
## [Midjourney 宣布首款硬件产品：全身超声波扫描仪](https://x.com/testingcatalog/status/2067422213112762831) ⭐️ 8.0/10

Midjourney 正式宣布了其首款硬件产品——一台全身超声波扫描仪，这标志着该公司从核心的 AI 图像生成业务迈出了重大转型的一步。除了这款扫描仪之外，公司还透露目前正在开发另外 4 个硬件项目和 4 个新软件项目。 这一公告标志着全球领先的 AI 图像生成实验室之一向医疗 AI 和实体硬件领域的重大战略转移。一台全身超声波扫描仪能够将前沿硬件与 AI 驱动的图像分析相结合，从而推动高级诊断的普及，这有可能会彻底改变预防性医疗保健。 Midjourney 的首席执行官 David Holz 此前曾暗示过进军硬件领域的雄心，公司于 6 月 17 日在旧金山举办了一场线下发布会以揭晓这一雄心勃勃的项目。虽然具体的技术规格和发布日期尚未公开，但预计该设备将利用人工智能来解析全身复杂的超声波数据。

rss · AI Hot · Jun 18, 01:40

**背景**: 超声波技术利用高频声波来生成人体内部的实时图像，传统上需要针对不同的深度和器官使用专门的探头。最近的行业进展（例如手持式的 Butterfly iQ+）已经利用硅芯片实现了该技术的微型化，但要打造一台全面的全身扫描仪仍是一项巨大的工程挑战。Midjourney 主要以其业界领先的生成式 AI 图像模型而闻名，因此这次向实体医疗设备的跨越显得非常出人意料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/midjourney-hardware-first-physical-ai-device">Midjourney Hardware: What We Know About the First Physical AI Device</a></li>
<li><a href="https://updates.midjourney.com/hardware-announcement-livestream/">Hardware announcement livestream</a></li>
<li><a href="https://www.nice.org.uk/advice/mib254/chapter/The-technology">The technology | Butterfly iQ+ for diagnostic ultrasound imaging | NICE</a></li>

</ul>
</details>

**标签**: `#Midjourney`, `#AI Hardware`, `#Frontier Tech`, `#Medical AI`, `#Biotech`

---

<a id="item-10"></a>
## [UCSD 教授黄碧薇创办 Aether AI 完成 2000 万美元融资，押注因果世界模型](https://x.com/AYi_AInotes/status/2067419296712524251) ⭐️ 8.0/10

UCSD Professor Biwei Huang's startup Aether AI has raised $20 million to build causal world models that automatically extract physical rules from video data, aiming to establish a fourth-generation AI paradigm.

rss · AI Hot · Jun 18, 01:29

**标签**: `#Causal AI`, `#World Models`, `#AI Funding`, `#Frontier AI`, `#AGI`

---

<a id="item-11"></a>
## [蔚来全新世界模型开启推送，超 70 万用户同步升级](https://www.ithome.com/0/965/777.htm) ⭐️ 8.0/10

蔚来已开始向超过 70 万用户推送全新版本的自动驾驶世界模型，甚至 4 年前购车的老车主也能获得升级。升级后的系统引入了包含监督微调（SFT）和闭环强化学习的三层训练框架，并在国内首次实现直接输出方向盘和加减速踏板控制信号，取代了传统的采样轨迹输出方式。 此次推送代表了汽车行业向端到端人工智能架构的重大转变，通过缩短控制路径显著降低了延迟，并提升了自动驾驶的精准度。通过将这一先进框架成功部署到庞大的老旧车队中，蔚来证明了其车载计算硬件的可扩展性，并为智能汽车行业的长期用户价值树立了新标杆。 新版本采用监督微调（SFT）技术，利用高质量行为数据进行精细雕刻，在保证高安全下限和合规性的同时实现类人的驾驶表现。值得注意的是，该系统在不依赖高精地图的前提下实现了行业领先的选路准确性，并在国内车企自研系统中首个实现了对潮汐车道和天空路牌的实时识别与理解。

rss · IT HOME · Jun 18, 02:24

**背景**: 自动驾驶中的“世界模型”是指人工智能系统对物理世界运作规律的内部模拟与理解，使其具备长时序规划与预判能力。端到端人工智能框架直接从传感器输入处理到车辆控制输出，取代了传统的模块化架构。闭环强化学习则通过让模型在模拟环境中从行为后果中学习，进一步优化策略，从而弥合了数据训练与真实物理世界应用之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/KQA76PO60547KOTE.html">163.com/dy/article/KQA76PO60547KOTE.html</a></li>
<li><a href="https://chejiahao.autohome.com.cn/info/25363780">困扰DeepSeek... | 汽车之家</a></li>

</ul>
</details>

**标签**: `#Autonomous Driving`, `#World Model`, `#End-to-End AI`, `#NIO`, `#Smart Vehicles`

---

<a id="item-12"></a>
## [Anthropic 5 月企业 AI 市场份额首次超越 OpenAI](https://techcrunch.com/2026/06/16/anthropics-latest-feud-with-the-trump-admin-may-actually-help-it-sales-data-suggests/) ⭐️ 8.0/10

根据 Ramp 的数据，Anthropic 5 月份在企业 AI 支出市场的份额首次超过 OpenAI，企业订阅占比升至 41%，而 OpenAI 为 39.5%。这一里程碑发生在同月，特朗普政府以出口管制为由，要求 Anthropic 禁止非美国用户访问其最新模型 Mythos 5 和 Fable 5。 这标志着企业 AI 领域主导地位的一个潜在转折点，表明 Anthropic 的 Claude 生态系统在企业采用方面正在对 OpenAI 取得实质性进展。与白宫的争端反而可能助推了 Anthropic 的销售这一悖论，凸显了地缘政治紧张局势和监管行动正在重塑 AI 行业的竞争格局。 Ramp 经济学家指出，Anthropic 被国防部列为供应链风险的那个月，正是其企业采用量最高的月份。目前企业主要使用的仍是已公开的 Claude Opus 系列，因此 Mythos 5 和 Fable 5 下架对整体业务的影响尚难量化，对 Anthropic 预期 IPO 的潜在影响也仍不确定。

telegram · @zaihuapd · Jun 17, 09:30

**背景**: Ramp 是一个企业支出管理平台，处理数十亿美元的商业交易，已成为追踪企业 AI 采用趋势的关键数据来源。Anthropic 的 Mythos 5 和 Fable 5 是基于 Mythos Preview 同一基础构建的前沿模型，Anthropic 曾称 Mythos Preview 在无限制状态下过于危险而不宜公开发布。特朗普政府越来越多地利用出口管制来限制非美国用户访问先进 AI 模型，将前沿 AI 能力视为国家安全问题。Anthropic 因其以安全为核心的 AI 开发理念而广受认可，这也使其模型对企业客户具有特别的吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/anthropic-vs-openai-business-adoption-2026-ramp-data">Anthropic vs OpenAI Business Adoption in 2026: What the RAMP Data ...</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/950026/anthropic-fable-mythos-ban-ai-shutdown">All the news about Anthropic ’s new AI fight with the White... | The Verge</a></li>
<li><a href="https://gizmodo.com/anthropics-mythos-safeguards-stoke-fears-of-a-permanent-underclass-2000770107">Anthropic 's Mythos Safeguards Stoke Fears of a ‘Permanent...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#OpenAI`, `#Enterprise AI`, `#AI Market Share`, `#AI Regulation`

---