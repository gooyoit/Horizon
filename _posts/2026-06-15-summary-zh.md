---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 108 items, 12 important content pieces were selected

---

1. [科技早报：Llama 5 遭禁、LeCun 十亿美元押注 JEPA、华为 950DT 大幅降低推理成本](#item-1) ⭐️ 9.0/10
2. [华为在 HDC 2026 上开源盘古 2.0 模型](#item-2) ⭐️ 9.0/10
3. [🤖 因美政府发函限制，Anthropic 已关闭两款 Mythos 模型对所有客户的访问  美国政府以国家安全权限向 Anthropic 发出出口管制指令，要求](#item-3) ⭐️ 9.0/10
4. [智源研究院院长王仲远：世界模型的四条技术路线与未来](#item-4) ⭐️ 8.5/10
5. [Loop Engineering：让 AI 智能体自动循环执行任务的新范式](#item-5) ⭐️ 8.0/10
6. [Databricks 推出 Omnigent：开源 AI 编码 Agent 元编排框架](#item-6) ⭐️ 8.0/10
7. [Claude Code 综合指南：25 项功能与策略详解](#item-7) ⭐️ 8.0/10
8. [世界杯门票价格低于 Fable 5 单次提示词花费](#item-8) ⭐️ 8.0/10
9. [Nadella：没有生态的「前沿 AI 模型」不可持续](#item-9) ⭐️ 8.0/10
10. [黄仁勋提出 AI"五层蛋糕"论：能源是终极之战](#item-10) ⭐️ 8.0/10
11. [清华大学团队揭示记忆重激活调控睡眠机制，成果发表于 Science](#item-11) ⭐️ 8.0/10
12. [2026 年一季度美国 75 个数据中心项目被阻，总值约 1300 亿美元](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [科技早报：Llama 5 遭禁、LeCun 十亿美元押注 JEPA、华为 950DT 大幅降低推理成本](https://x.com/hongming731/status/2066320766698996179) ⭐️ 9.0/10

一份每日科技简报指出，Anthropic 模型 Fable 5 发布 72 小时内即被红队研究者 Pliny 利用 Unicode 同形字替换和分解-重组攻击突破其 Constitutional AI 安全架构，随后被美国政府以国家安全为由实施出口管制禁令。与此同时，图灵奖得主 Yann LeCun 融资约 10 亿美元创办新公司押注 JEPA 世界模型路线，华为昇腾 950DT 芯片与 DeepSeek V4 协同将 AI 推理成本降低 75%，字节跳动已锁单。 这些动态揭示了前沿 AI 领域的三大关键张力：当前 LLM 安全架构面对复杂越狱手法的脆弱性、从自回归语言模型向世界模型的重大路线转变，以及日益激烈的硬件竞争正在快速推动 AI 推理商品化。它们共同表明，AI 下一阶段的发展将同等程度地受到安全突破和专用硬件的影响。 Fable 5 的越狱采用了三层手法：Unicode 同形字替换（对开源 LLM 的成功率达 42%–59%）、分解-重组攻击，以及利用已越狱的弱模型协助。JEPA（联合嵌入预测架构）通过在嵌入空间中预测抽象表征而非像素级细节来运作，相比生成式方法展现出 1.5 至 6 倍的训练效率提升。

rss · AI Hot · Jun 15, 00:43

**背景**: Constitutional AI 是一种对齐框架，通过预定义的规则集在训练阶段学习和运行时分类器实时评估两个层面引导模型行为。JEPA 由 Yann LeCun 提出，是一种预测性世界模型架构，通过学习观测和预测的联合嵌入，旨在克服 LLM 缺乏因果建模和物理理解的局限。Unicode 同形字攻击利用不同 Unicode 字符之间的视觉相似性，创建对人类看起来正常但被 AI 系统以不同方式处理的文本，实际防御手段包括 Unicode 标准化（NFKC）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/">Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru</a></li>
<li><a href="https://www.promptfoo.dev/docs/red-team/strategies/homoglyph/">Homoglyph Encoding Strategy | Promptfoo</a></li>
<li><a href="https://medium.com/@genai.works/claude-ais-constitutional-framework-a-technical-guide-to-constitutional-ai-704942e24a21">Claude AI ’s Constitutional Framework: A Technical Guide to... | Medium</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#JEPA`, `#AI Chips`, `#Frontier AI`, `#Tech News`

---

<a id="item-2"></a>
## [华为在 HDC 2026 上开源盘古 2.0 模型](https://t.me/zaihuapd/41948) ⭐️ 9.0/10

在华为开发者大会 2026 上，华为发布了开源盘古 openPangu 2.0 模型，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，均支持 512K 上下文。华为计划从 6 月 30 日起陆续开源预训练代码等 7 大组件。 此次发布代表了前沿规模 AI 领域的一项重大开源贡献，505B 参数模型配合超大上下文窗口足以媲美全球顶尖模型。其特殊意义在于模型针对华为昇腾芯片和鸿蒙系统进行了优化，有力强化了中国本土 AI 生态，降低了对国外算力基础设施的依赖。 余承东在演讲中坦言，华为算力大量支持了国内其他企业需求，自身留的数量很有限。openPangu 2.0 模型专门针对昇腾算力进行了亲和性优化，并适配鸿蒙系统。

telegram · @zaihuapd · Jun 14, 08:05

**背景**: 华为盘古系列预训练大模型由华为云联合伙伴推出，最初包括 NLP 和 CV 大模型，旨在提高 AI 开发效率。昇腾计算平台是华为基于自研达芬奇架构 NPU 芯片打造的 AI 基础设施，与传统冯·诺伊曼架构 GPU 不同，它将存储和处理一体化。鸿蒙系统是华为自主研发的智能终端操作系统，已获得 EAL5+ 安全认证，并持续完善原生应用生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xie.infoq.cn/article/2a0986fbcad8769b735880a58">让AI... - InfoQ 写作平台</a></li>
<li><a href="https://e.huawei.com/cn/products/computing/ascend">昇腾计算-华为Ascend-AI计算-华为企业业务</a></li>
<li><a href="https://www.vzkoo.com/read/202312264b6e77f3f372c6ed418c91ff.html">2023年华为算力专题报告：昇腾鲲鹏构筑国内算力第二极 - 报告精读 - 未来智库</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Open Source`, `#Huawei`, `#Large Language Models`, `#AI Infrastructure`

---

<a id="item-3"></a>
## [🤖 因美政府发函限制，Anthropic 已关闭两款 Mythos 模型对所有客户的访问  美国政府以国家安全权限向 Anthropic 发出出口管制指令，要求](https://t.me/zaihuapd/41949) ⭐️ 9.0/10

The US government issued an export control directive on national security grounds, prompting Anthropic to suspend all customer access to its Fable 5 and Mythos 5 models due to potential risks if jailbroken.

telegram · @zaihuapd · Jun 14, 09:06

**标签**: `#AI Regulation`, `#Anthropic`, `#National Security`, `#Export Controls`, `#AI Safety`

---

<a id="item-4"></a>
## [智源研究院院长王仲远：世界模型的四条技术路线与未来](https://36kr.com/p/3853016586359817?f=rss) ⭐️ 8.5/10

智源研究院院长王仲远系统梳理了当前全球世界模型的四条技术路线：以语言为中心、以像素为中心、以三维结构为中心以及以视觉表征为中心（如 JEPA）。他还透露智源正在尝试第五种融合路线，即将语言和视觉压缩进统一的「潜空间表征」中，以驱动悟·Physis 和悟界·RoboBrain Orca 等系统。 这一分类法为当前对“世界模型”定义充满分歧的 AI 和机器人行业提供了清晰的脉络。它表明顶尖研究机构认为现有的 VLA 模型不足以实现真正的物理世界理解，下一代 AI 的重大突破将依赖于具备因果推理和长时序物理预测能力的模型。 王仲远明确指出，像 Sora 这样的视频生成模型并不是真正的世界模型，因为它们缺乏物理因果逻辑；同时，3D 重建也不等同于理解物理状态。他认为世界模型目前大约处于 2012 年的深度学习阶段，可能需要三年甚至更长时间才能构建出具备泛化和主动探索能力的真正机器人大脑。

rss · 36kr · Jun 15, 01:50

**背景**: 视觉-语言-动作（VLA）模型通过整合视觉感知和语言理解来控制机器人动作，但它们无法准确预测重力和力度等物理后果。为了解决这一问题，研究人员正在开发“世界模型”，旨在让 AI 理解物理规律和因果关系，充当具身智能的“大脑”。目前知名的路线包括杨立昆提出的 JEPA（在抽象表征空间而非像素层面进行预测），以及李飞飞团队 World Labs 推出的 Marble 模型（专注于生成和模拟 3D 空间环境）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/">Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru</a></li>
<li><a href="https://www.worldlabs.ai/blog/marble-world-model">Marble: A Multimodal World Model | World Labs</a></li>
<li><a href="https://www.labellerr.com/blog/vision-language-action-vla-models-2/">How Vision - Language - Action Models Powering Humanoid Robots</a></li>

</ul>
</details>

**标签**: `#World Models`, `#Embodied AI`, `#VLA`, `#Robotics`, `#BAAI`

---

<a id="item-5"></a>
## [Loop Engineering：让 AI 智能体自动循环执行任务的新范式](https://mp.weixin.qq.com/s/omwt7d9BSFX7kotW9vo9bQ) ⭐️ 8.0/10

Industry leaders from OpenClaw and Claude Code have outlined 'Loop Engineering,' a new paradigm where AI agents autonomously loop through tasks until meeting verifiable completion conditions defined by developers.

rss · AI Hot · Jun 15, 02:05

**标签**: `#AI Agents`, `#Loop Engineering`, `#Autonomous Coding`, `#Software Engineering`, `#AI Workflow`

---

<a id="item-6"></a>
## [Databricks 推出 Omnigent：开源 AI 编码 Agent 元编排框架](https://x.com/shao__meng/status/2066326398252499391) ⭐️ 8.0/10

Databricks 发布了 Omnigent，这是一个采用 Apache 2.0 协议的开源 meta-harness，位于 Claude Code 和 Codex 等 AI 编码 Agent 之上，提供统一的编排接口。它具备三大核心能力：组合（通过 YAML 切换和定义可移植的 Agent）、控制（有状态成本策略、安全审批策略及操作系统沙箱），以及协作（通过 URL 共享实时会话）。 这为 AI 编码 Agent 引入了类似 Kubernetes 的抽象层，将会话、策略和成本与具体的底层 harness 解耦。随着团队越来越多地同时使用多种编码 Agent（如侧重快速反馈的 Claude Code 和侧重持续自主性的 Codex），它满足了行业对统一治理、成本控制和安全执行的迫切需求。 Omnigent 支持通过一行配置在不同 harness 之间切换，并允许在同一 Agent 内组合不同的子 Agent。其控制功能包括有状态成本策略（如每消费 100 美元暂停）、与 harness 解耦的安全策略（如在执行 npm 后进行 git push 需要审批）以及操作系统级沙箱。

rss · AI Hot · Jun 15, 01:06

**背景**: 在 AI 编码 Agent 领域，“harness”指的是包裹语言模型的执行环境和工具集，决定了模型如何与代码、文件和操作系统进行交互。不同的 Agent（如 Claude Code 和 Codex）拥有不同的 harness 设计——例如，Claude Code 针对快速反馈循环进行了优化，而 Codex 则专为持续的自主推理而构建。“Meta-harness（元框架）”则更进一步，它作为一个位于多个独立 harness 之上的框架，允许 AI 系统从单一控制台管理、编排甚至优化跨不同 Agent 的工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theneuron.ai/explainer-articles/meta-harness-is-automated-agent-engineering-the-next-frontier/">Meta - Harness Makes the Case for Automated AI Agents</a></li>
<li><a href="https://composio.dev/content/claude-code-vs-openai-codex">Claude Code vs Codex: What I Learned After 100+ Hours With Both (2026) | Composio</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/">Introducing the Agent Governance Toolkit: Open-source runtime ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Databricks`, `#Open Source`, `#AI Infrastructure`, `#Coding Agents`

---

<a id="item-7"></a>
## [Claude Code 综合指南：25 项功能与策略详解](https://www.marktechpost.com/2026/06/14/claude-code-guide-2026-25-features-with-examples-demo) ⭐️ 8.0/10

一篇详细的指南发布了，涵盖了 Anthropic 的 Claude Code 智能体编码助手的 25 项功能、社区技术和第三方工具。该指南将这些能力分为官方功能、社区驱动技术和第三方扩展，帮助开发者优化软件工程工作流。 Claude Code 代表了智能体 AI 工具的新范式，能够通过自然语言自主阅读代码库、规划操作、执行命令并处理 git 工作流。掌握子智能体、MCP 服务器和上下文压缩等高级功能，使前沿 AI 开发者能够大幅加速日常编码任务并构建更复杂的自主流水线。 重要的官方功能包括 CLAUDE.md 记忆文件、斜杠命令（/init、/compact、/review）、钩子、MCP 服务器、计划模式、权限模式以及支持 Python 和 TypeScript 编程的 Agent SDK。社区技术涵盖结构化上下文文件夹、动态工作流和模块化技能管道，而 Mem Search 等第三方工具则扩展了智能体的外部记忆层。

rss · AI Hot · Jun 15, 01:04

**背景**: Claude Code 是由 Anthropic 开发的智能体编码工具，运行于终端、IDE 或桌面应用中，采用智能体循环机制——阅读代码库、规划操作、使用真实开发工具执行，并根据结果调整策略。模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 系统连接外部数据源和工具的方式。Agent SDK 为开发者提供了与 Claude Code 相同的工具、智能体循环和上下文管理能力，支持创建自定义的自主 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://platform.claude.com/docs/en/agent-sdk/overview">Agent SDK overview - Claude API Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#Agentic AI`, `#Anthropic`, `#AI Coding Tools`, `#Developer Tools`

---

<a id="item-8"></a>
## [世界杯门票价格低于 Fable 5 单次提示词花费](https://x.com/SemiAnalysis_/status/2066324956435075339) ⭐️ 8.0/10

SemiAnalysis 透露，先进的 Fable 5 "ultracode"模型为一个小型内部代码库编写文档时，单次提示词的花费竟然超过了一张美国国家队世界杯比赛的门票价格。这一具体数据揭示了当前最强大的前沿 AI 模型在单次请求上令人咋舌的推理成本。 这一惊人的对比强调，尽管整体上每 token 的推理成本已大幅下降，但运行最强大前沿模型处理复杂、长上下文任务的绝对成本依然极高。它凸显了一个日益扩大的经济鸿沟：只有资金雄厚的组织才能负担得起部署顶级 AI，这可能在精英 AGI 级能力与广大开发者社区之间造成永久性的差距。 据报道，Fable 5 模型在 API 上的定价约为每百万输入 token 10 美元、每百万输出 token 50 美元，但复杂的智能体任务在单次会话中可能消耗海量 token。所提及的具体任务是为一个小型内部代码库生成文档，这意味着该模型使用了大量上下文窗口和多步推理，导致成本迅速累积。

rss · AI Hot · Jun 15, 01:00

**背景**: AI 推理成本已成为行业关注的核心问题，2026 年推理支出已占 AI 云基础设施成本的 55%以上，并首次超过训练支出。据报道，虽然 LLM 推理的每 token 成本在三年内下降了约 1000 倍，但由于上下文窗口扩大、思维链推理和多步工具调用，复杂智能体工作流所需的总算力增长得更快。Fable 5 是一款通过 Claude Code（2.1.170 或更高版本）访问的前沿级模型，代表了模型智能的顶层水平，因其增强的能力而享有溢价定价。SemiAnalysis 是一家受人尊敬的半导体和 AI 基础设施研究公司，以对计算经济学和 AI 价值链的深度技术分析而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claudefa.st/blog/guide/development/fable-5-usage-credits">Claude Fable 5 Pricing & Usage Credits Explained</a></li>
<li><a href="https://byteiota.com/ai-inference-costs-55-of-cloud-spending-in-2026/">AI Inference Costs: 55% of Cloud Spending in 2026 | byteiota</a></li>
<li><a href="https://medium.com/all-about-claude/claude-fable-5-in-claude-code-my-first-48-hours-03d51858b687">Claude Fable 5 in Claude Code: My First 48 Hours | by Mohit... | Medium</a></li>

</ul>
</details>

**标签**: `#AI Inference`, `#Frontier Models`, `#Compute Costs`, `#SemiAnalysis`, `#AGI`

---

<a id="item-9"></a>
## [Nadella：没有生态的「前沿 AI 模型」不可持续](https://x.com/shao__meng/status/2066316641332552181) ⭐️ 8.0/10

微软 CEO Satya Nadella 发表战略框架文章，指出可持续的企业 AI 需要在人类资本与「token 资本」（组织自建的 AI 能力）之间构建具有复利效应的学习闭环。他提出了一套可落地的架构：可替换的通用模型加上不可丢失的组织经验，并通过私有评测环境和私有强化学习环境以真实业务结果驱动模型进化。 这一框架直接挑战了当前的主流假设——即 AI 竞争优势来自于拥有或使用最强大的单一前沿模型。Nadella 的愿景将战略重心转向构建广泛的「前沿生态」，让价值流向各行业与国家，并警告若少数模型攫取全部回报将重演产业空心化的覆辙。 Nadella 将这一学习闭环比作具有复利效应的「爬山机」，其中私有评测和私有强化学习环境是捕获组织知识并将其反馈到模型适应中的关键基础设施。他强调通用模型应被视为可替换的商品化组件，而组织的专有数据、评测框架和知识库才是真正持久的资产。

rss · AI Hot · Jun 15, 00:27

**背景**: 「Token 资本」是 Nadella 近期在与 Reid Hoffman 的讨论中推进的概念，将 AI token 不仅仅视为一项成本支出，而是组织必须有意积累并产生复利效应的资本资产——类似于金融资本或知识产权。私有评测是指组织利用自身专有业务数据构建评测基准，而非仅依赖公开排行榜，从而能够根据特定领域的真实业务结果来衡量 AI 性能。私有强化学习环境则更进一步，创建了定制化的模拟空间，让 AI 智能体能够针对组织的实际工作流、工具和数据进行试错学习。这些共同构成了 Nadella 所说的人类判断力与 AI 能力之间复利循环的基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/satya-nadella-ceos-need-thinking-token-capital-reid-hoffman-1mnkc">Satya Nadella: CEOs need to be thinking about token capital.</a></li>
<li><a href="https://podcastalpha.substack.com/p/satya-nadella-microsoft-ceo-on-token">Satya Nadella - Microsoft CEO - on token capital, the ...</a></li>

</ul>
</details>

**标签**: `#AI Strategy`, `#Enterprise AI`, `#Satya Nadella`, `#AI Ecosystem`, `#Token Capital`

---

<a id="item-10"></a>
## [黄仁勋提出 AI"五层蛋糕"论：能源是终极之战](https://x.com/berryxia/status/2066314393441485130) ⭐️ 8.0/10

Jensen Huang outlines a five-layer AI industry architecture, emphasizing that energy, chips, and data centers form the critical foundational moat rather than just the model layer, projecting a future $20 trillion annual ecosystem.

rss · AI Hot · Jun 15, 00:18

**标签**: `#AI Infrastructure`, `#Jensen Huang`, `#Data Centers`, `#AI Energy`, `#AI Industry Strategy`

---

<a id="item-11"></a>
## [清华大学团队揭示记忆重激活调控睡眠机制，成果发表于 Science](https://www.ithome.com/0/964/240.htm) ⭐️ 8.0/10

清华大学与北京智源人工智能研究院联合团队在 Science 上发表研究，首次证实睡眠中的记忆重激活可以主动调控睡眠状态。研究发现，负向记忆印迹细胞的重激活会将大脑从非快速眼动睡眠推向觉醒状态，导致睡眠碎片化；而正向记忆印迹细胞的重激活则能促进并维持非快速眼动睡眠。 该研究首次在神经机制层面揭示了记忆与睡眠之间的双向调控关系，解释了为什么压力和负面经历会导致睡眠质量下降。研究还将记忆印迹细胞确定为抑郁症等精神疾病相关睡眠障碍的潜在治疗靶点，为未来的临床干预提供了全新方向。 研究团队结合双光子在体成像技术与脑电、肌电记录，在单细胞分辨率下追踪了小鼠基底外侧杏仁核中的记忆印迹细胞活动。他们发现，正向和负向记忆印迹细胞连接着不同的下游脑区——正向印迹细胞倾向于投射到促进睡眠的脑区，而负向印迹细胞则更强地连接到促进觉醒的脑区。

rss · IT HOME · Jun 15, 01:49

**背景**: 记忆印迹细胞是一群特定的神经元，负责编码和存储特定经历，本质上是记忆在大脑中的物理痕迹。非快速眼动睡眠是睡眠的主要阶段，包含最深、最具恢复性的睡眠期，在此期间身体修复组织并巩固记忆。双光子成像技术是一种先进的显微成像方法，允许研究人员在活体动物中以高分辨率观察单个神经元的活动。基底外侧杏仁核是大脑中处理情绪记忆的关键区域，尤其与恐惧和负面经历密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://life.tsinghua.edu.cn/info/1131/7427.htm">生命学院钟毅团队发现海马体中介导主动遗忘的记忆印迹细胞-清华大学生...</a></li>
<li><a href="https://m.haodf.com/neirong/wenzhang/9391537537.html">睡 眠 的4个阶段 - 好大夫在线</a></li>

</ul>
</details>

**标签**: `#Neuroscience`, `#Brain Research`, `#Sleep Regulation`, `#Memory Reactivation`, `#Frontier Tech`

---

<a id="item-12"></a>
## [2026 年一季度美国 75 个数据中心项目被阻，总值约 1300 亿美元](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs) ⭐️ 8.0/10

2026 年第一季度，美国社区和立法者成功阻止或推迟了至少 75 个价值约 1300 亿美元的数据中心项目，数量已与 2025 年全年持平。草根反对组织在三个月内从 396 个激增至 833 个，遍布 49 个州，同时各州议会和联邦议员也提出了大量针对数据中心建设的监管法案。 这波被阻项目代表了美国 AI 基础设施扩张的重大瓶颈，直接限制了 AI 实验室和云服务商扩展前沿模型所需的计算能力。无论是在资金规模还是地理覆盖范围上，这种前所未有的反对浪潮都标志着公众对数据中心建设态度的根本性转变，可能重塑全球 AI 算力的竞争格局。 大型数据中心每天冷却用水可达 500 万加仑，相当于一个 1 万至 5 万人口城镇的用水量，而 AI 专用设施的消耗更高。据美国环保署估计，数据中心目前占美国科技公司能源消耗的约 40%，且反对声音已跨越党派界限，覆盖州和联邦各级政府。

telegram · @zaihuapd · Jun 14, 03:03

**背景**: 数据中心是云计算和 AI 工作负载的物理基础设施，容纳数千台需要持续供电运行和冷却的服务器。生成式 AI 的快速发展大幅加速了对新数据中心容量的需求，因为训练和运行大型语言模型需要巨大的计算资源。这种激增对当地电网和供水系统造成了前所未有的压力，尤其是因为最常用的蒸发冷却方法需要消耗大量淡水。美国各地的社区越来越关注与这些设施相关的公用事业费用上涨、环境恶化和资源枯竭问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://zipdo.co/data-center-energy-consumption-statistics/">Data Center Energy Consumption Statistics | 2026 Edition</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Data Centers`, `#Energy Consumption`, `#Regulation`, `#AI Compute`

---