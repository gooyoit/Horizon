---
layout: default
title: "Horizon Summary: 2026-03-24 (ZH)"
date: 2026-03-24
lang: zh
---

> From 86 items, 12 important content pieces were selected

---

1. [iPhone 17 Pro 在设备上运行 400B 参数大语言模型](#item-1) ⭐️ 9.0/10
2. [西湖大学团队发布实时复刻人类动作的“泰坦 o1”机器人](#item-2) ⭐️ 9.0/10
3. [Claude 通过“电脑使用”功能直接操控 Mac](#item-3) ⭐️ 9.0/10
4. [科技公司以 LLM token 消耗量考核员工绩效](#item-4) ⭐️ 8.0/10
5. [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](#item-5) ⭐️ 8.0/10
6. [苹果 WWDC 2026 定档 6 月 8 日，聚焦 AI](#item-6) ⭐️ 8.0/10
7. [大语言模型代理尝试自主机器学习研究](#item-7) ⭐️ 7.0/10
8. [批评“AI 垃圾内容”是对同事时间的不尊重](#item-8) ⭐️ 7.0/10
9. [珀乐互动完成天使轮融资，以 AI+IP 重塑数字内容生态](#item-9) ⭐️ 7.0/10
10. [开发者通过自定义 API 端点将 Cursor 额度消耗降低 10 倍](#item-10) ⭐️ 7.0/10
11. [发布新型多智能体任务协作管理工具](#item-11) ⭐️ 7.0/10
12. [腾讯内测 AI 问股小程序](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [iPhone 17 Pro 在设备上运行 400B 参数大语言模型](https://twitter.com/anemll/status/2035901335984611412) ⭐️ 9.0/10

一项演示声称 iPhone 17 Pro 成功通过从 SSD 流式加载权重的方式，在设备上运行了一个 4000 亿参数的大语言模型（LLM）。该模型采用混合专家（MoE）架构和激进的量化技术，以适应移动硬件的限制。 如果得到验证，这将是端侧 AI 的重大突破，使用户无需依赖云端即可使用强大、私密且支持离线的大语言模型。这表明苹果可能将前沿 AI 直接集成到消费设备中，重塑人们对移动智能的期待。 据称该模型采用苹果的“LLM in a Flash”技术从 SSD 流式加载权重，仅需约 5.5GB 内存，生成速度约为每秒 0.6 个 token。尽管参数量达 4000 亿，但其为混合专家（MoE）模型，每次推理仅激活部分专家（如 170 亿参数），并辅以重度量化以降低计算负担。

hackernews · anemll · Mar 23, 14:30

**背景**: 混合专家（MoE）是一种大语言模型架构，通过将计算分散到多个“专家”子网络中，并通过路由机制为每个输入 token 仅激活少数专家，从而在不显著增加计算量的前提下提升模型容量。量化技术通过降低数值精度（例如从 16 位浮点数降至 4 位整数）来缩小模型体积并加速在资源受限设备上的推理。苹果 2023 年发表的《LLM in a Flash》论文提出，可利用高速闪存作为内存的延伸，无需一次性将全部模型权重加载到内存中即可运行超大模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>
<li><a href="https://glenrhodes.com/running-a-400b-parameter-model-locally-on-a-macbook-using-flash-based-inference-streaming/">Running a 400B parameter model locally on a MacBook using flash-based inference streaming - Glen Rhodes</a></li>

</ul>
</details>

**社区讨论**: 社区评论质疑标题具有误导性，因其强调总参数量而非实际激活参数量，并指出像 Qwen3.5-397B-A17B 这类 MoE 模型在推理时表现更接近 170 亿参数模型。另有用户提到当前苹果芯片设备存在严重发热和降频问题，并认为该演示很可能基于苹果的《LLM in a Flash》论文所提出的技术。

**标签**: `#LLM`, `#On-Device AI`, `#Mixture of Experts`, `#Apple`, `#AI Hardware`

---

<a id="item-2"></a>
## [西湖大学团队发布实时复刻人类动作的“泰坦 o1”机器人](https://www.ithome.com/0/931/964.htm) ⭐️ 9.0/10

西湖大学孵化企业西湖机器人发布了人形机器人“泰坦 o1”，其搭载自主研发的 GAE（通用动作专家）“通用小脑”模型，可实时远程复刻人类动作，无需预训练或编程。用户仅需穿上动捕服或通过电脑操作，即可让一台或多台机器人同步模仿动作。 该技术将具身智能与实用机器人结合，通过直观的实时遥操作，有望革新消防、采矿、高空作业等高危行业。同时，它推动了“大动作模型”作为机器人控制新范式的发展，使机器人从预设程序迈向具备类人运动智能的自适应系统。 GAE 模型作为“通用小脑”，可实时协调全身动作，并具备“跨本体”能力，适用于不同结构和尺寸的机器人。该系统无需任务特定训练，团队宣称其技术领先国际同行至少六个月。

rss · IT HOME · Mar 24, 01:34

**背景**: 具身智能（Embodied AI）强调智能体通过传感器和执行器与物理世界交互，需融合感知、决策与运动控制。大动作模型（Large Action Models, LAMs）是新兴 AI 系统，旨在生成复杂协调的物理行为，类似于大语言模型生成文本。“大小脑”架构将高层推理（“大脑”）与底层运动协调（“小脑”）分离，模仿生物神经机制以提升机器人敏捷性与响应能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://robohorizon.cn/zh/videos/robot-shixian-moni-renti/">机器人影子人类：AI实时模仿人体动作 | RoboHorizon Robot Magazine -...</a></li>
<li><a href="https://www.linkedin.com/posts/grishinrobotics_real-time-shadowing-can-turn-a-robot-demo-activity-7378491418933301248-_OZi">Westlake Robotics unveils GAE, a real-time shadow function ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1982101283356841191">Human Data EP06—Mocap+Video：GAE - 知乎</a></li>

</ul>
</details>

**标签**: `#AI Robotics`, `#Embodied AI`, `#Humanoid Robots`, `#Large Action Models`, `#Research`

---

<a id="item-3"></a>
## [Claude 通过“电脑使用”功能直接操控 Mac](https://www.ithome.com/0/931/960.htm) ⭐️ 9.0/10

Anthropic 推出了“电脑使用”（Computer Use）功能的研究预览版，使 Claude 3.5 Sonnet 能够通过移动光标、点击按钮和输入文本来自主控制 macOS 系统。该功能通过两款新桌面应用实现：用于通用任务的 Claude Cowork 和用于编程的 Claude Code，并配套推出 Dispatch 功能，允许用户通过手机远程启动电脑任务。 这标志着迈向真正自主 AI 智能体的重要一步——AI 不再只是对话工具，而成为能主动执行任务的“数字打工人”。它预示着人机交互范式的转变：AI 可在无需持续人工干预的情况下，跨应用完成多步骤的复杂工作流。 该功能目前仅限 macOS 系统，且仅对 Claude Pro 和 Max 订阅用户开放，并在沙盒环境中运行以确保安全。Dispatch 支持跨设备控制，但需桌面应用处于运行状态，且 Cowork 一次只能操作一个文件夹。

rss · IT HOME · Mar 24, 01:30

**背景**: 传统大语言模型（如 Claude）仅能处理文本和图像，无法直接与操作系统交互。“电脑使用”功能通过结合计算机视觉与动作执行能力，使 AI 能像人类一样感知屏幕内容并操作界面。Claude 3.5 Sonnet 是首个在公开测试中提供此能力的前沿 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use, a new Claude 3.5 Sonnet, and ...</a></li>
<li><a href="https://claude.com/product/cowork">Cowork : Claude Code power for knowledge work | Claude by Anthropic</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/03/20/claude-dispatch-lets-you-control-claude-cowork-with-your-phone/">Anthropic Update Lets You Control Claude Cowork With Your Phone</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Human-Computer Interaction`, `#Claude`, `#Autonomous Systems`, `#Frontier AI`

---

<a id="item-4"></a>
## [科技公司以 LLM token 消耗量考核员工绩效](https://gizmodo.com/tech-employees-are-reportedly-being-evaluated-by-how-fast-they-burn-through-llm-tokens-2000736627) ⭐️ 8.0/10

据报道，Meta、OpenAI 和 Shopify 正根据员工消耗的 LLM token 数量评估其工作效率，并通过内部排行榜追踪使用情况，高用量员工可获得奖励。 这一做法标志着 AI 原生企业衡量生产力方式的转变，将绩效指标直接与生成式 AI 使用量挂钩，可能影响整个科技行业的成本控制、创新激励和职场文化。 据报道，一名 OpenAI 工程师累计消耗 2100 亿 token，而 GPT-5.4 上线后日处理量达 5 万亿 token；token 统计包含输入（prompt）和输出（completion），反映模型总负载与成本。

telegram · zaihuapd · Mar 23, 08:42

**背景**: 在大语言模型（LLM）中，“token”是文本的基本处理单位，可以是一个词、标点或子词。Token 使用量直接关联计算成本和延迟，因此成为衡量运营效率的关键指标。企业正越来越多地监控 token 消耗，以优化 AI 支出和系统性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/state-of-ai">State of AI 2025: 100T Token LLM Usage Study | OpenRouter</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-02-06-track-token-usage-prompt-costs-model-latency-opentelemetry/view">How to Track Token Usage, Prompt Costs, and Model Latency with OpenTelemetry</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/introducing-gpt-5-4/">Introducing GPT - 5 . 4 | OpenAI</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI Industry`, `#Performance Metrics`, `#Generative AI`, `#Token Usage`

---

<a id="item-5"></a>
## [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 8.0/10

OpenAI 于 3 月 6 日向英国竞争与市场管理局（CMA）提交政策建议，敦促监管机构明确将 ChatGPT 等 AI 聊天机器人纳入 Google 在 Android 和 Chrome 中的搜索选择页面。OpenAI 认为这些服务在功能上已与传统及 AI 增强型搜索引擎形成竞争。 此举标志着 OpenAI 力图在 AI 重塑信息发现方式的背景下，与传统搜索引擎争夺平等地位。同时，它也促使监管机构重新定义大语言模型时代的“搜索”概念，可能影响全球数字竞争政策走向。 OpenAI 建议采用透明且动态的流行度标准来决定入选资格，并将选择页面从文本搜索扩展至语音、视觉和 AI 辅助搜索等入口。其特别指出 ChatGPT 与 Google 的 AI Overviews 和 AI Mode 在功能上已相当。

telegram · zaihuapd · Mar 23, 14:50

**背景**: Google 的搜索选择页面源于欧盟反垄断裁决，要求其在 Android 设备上允许用户选择默认搜索引擎。AI Overviews 是 Google 推出的一项功能，利用生成式 AI 对搜索结果进行摘要，是其将大语言模型深度整合进搜索服务的一部分。如今，ChatGPT 等大语言模型支持多轮对话式信息检索，在功能上已对传统关键词搜索构成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://search.google/ways-to-search/ai-overviews/">Google AI Overviews - Search anything, effortlessly</a></li>
<li><a href="https://support.google.com/websearch/answer/14901683?hl=en">Find information in faster & easier ways with AI Overviews in Google Search - Computer - Google Search Help</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#LLM`, `#Search Engines`, `#Regulation`, `#OpenAI`

---

<a id="item-6"></a>
## [苹果 WWDC 2026 定档 6 月 8 日，聚焦 AI](https://www.apple.com/newsroom/2026/03/apples-worldwide-developers-conference-returns-the-week-of-june-8/) ⭐️ 8.0/10

苹果宣布 2026 年全球开发者大会（WWDC）将于 6 月 8 日至 12 日在线举行，重点展示其各平台的人工智能整合、新软件发布及开发者工具；6 月 8 日还将在 Apple Park 举办小规模线下活动。 随着苹果日益重视人工智能，WWDC 2026 可能成为其将生成式 AI 与端侧智能深度融入 iOS、macOS 及开发者工作流的关键节点，有望重塑其生态系统的用户体验与应用开发模式。 大会将于 6 月 8 日以主题演讲和平台 State of the Union 开幕，随后一周提供超 100 场技术视频课程及与苹果工程师的互动实验室；50 名 Swift 学生挑战赛优胜者将受邀赴库比蒂诺参加为期三天的特别体验。

telegram · zaihuapd · Mar 23, 17:37

**背景**: WWDC 是苹果每年发布新软件、开发者工具和平台战略的重要活动。近年来，苹果转向以隐私为中心的端侧 AI 处理，区别于竞争对手依赖云端的方案。2024 和 2025 年的 WWDC 已引入 Siri 增强、预测文本等基础 AI 功能，2026 年有望大幅扩展这些能力。

**标签**: `#AI`, `#Apple`, `#WWDC`, `#Software Update`, `#Developer Tools`

---

<a id="item-7"></a>
## [大语言模型代理尝试自主机器学习研究](https://ykumar.me/blog/eclip-autoresearch/) ⭐️ 7.0/10

一篇博客文章详细描述了一项实验：使用大语言模型（LLM）代理在机器学习项目（eCLIP）中自主迭代，循环修改代码、训练模型并评估结果。该代理主要执行了超参数调优，而非引入新颖的架构变更。 这项探索揭示了当前基于大语言模型的研究自动化的实际局限性——适用于渐进式改进，但尚不具备高层次科学推理能力或成本效益高的创新能力。它有助于理解 AI 代理在短期内如何辅助而非取代人类研究人员。 该系统的核心是一个提示文件（program.md），指示代理迭代改进 train.py、运行训练、评估并记录结果，同时偏好简洁性。社区对 GitHub 提交历史的分析表明，大多数更改仅为微小的超参数调整，引发了对令牌成本效益的质疑。

hackernews · ykumards · Mar 23, 18:40

**背景**: 大语言模型驱动的自主代理将 LLM 作为“大脑”，通过与代码解释器、文档和 API 等工具交互来规划、推理和执行任务。在 AutoML 中，LLM 可辅助数据生成、模型选择和流程优化，但完全自主仍处于实验阶段。近期如 AutoM3L 等框架通过协调多个专用 LLM 模块实现语言驱动的机器学习自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2023-06-23-agent/">LLM Powered Autonomous Agents | Lil'Log</a></li>
<li><a href="https://arxiv.org/pdf/2306.08107">AutoML in the Age of Large Language Models:</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1590105/full">Frontiers | Evaluation of large language model-driven AutoML in data and model management from human-centered perspective</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，尽管大语言模型偶尔能提供有用见解，但大多数建议不切实际或基于维护不佳的库。多人观察到该代理的行为类似于基础的超参数优化，并质疑其计算成本是否值得所带来的微小收益。

**标签**: `#LLM`, `#AI Agents`, `#AutoML`, `#Research Automation`, `#Prompt Engineering`

---

<a id="item-8"></a>
## [批评“AI 垃圾内容”是对同事时间的不尊重](https://simonwillison.net/2026/Mar/23/neurotica/#atom-everything) ⭐️ 7.0/10

Neurotica 在社交媒体上提出“slop”（垃圾内容）一词，用以描述未经编辑的原始 AI 输出，指出其消耗他人时间的成本高于生成成本，并批评在职场中不加甄别地分享此类内容是一种不尊重行为。 这一批评揭示了人机协作中日益严重的伦理与实践问题：低投入的 AI 内容常态化会降低沟通质量并浪费集体时间，尤其在重视信任与清晰度的专业环境中影响显著。 “Slop”特指看似流畅但空洞无物的 AI 生成文本；若不经人工审核直接分享，会将认知负担转嫁给接收者，违背了协作中的基本尊重原则。

rss · Simon Willison · Mar 23, 23:31

**背景**: Gemini 或 GPT 等生成式 AI 模型虽能快速生成流畅文本，但常缺乏真正的理解、细微差别或事实依据。原始输出可能包含错误、泛泛而谈的表述或无关信息。在职场中，这类输出常被未经编辑直接使用，引发对责任、质量和效率的担忧。“AI slop”一词因此流行，用于描述充斥数字空间的低价值、高产量内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://slopdetector.org/slop/what-is-ai-slop">What Is AI Slop? Definition, Examples & Why It Matters (2026)</a></li>
<li><a href="https://www.linkedin.com/posts/stephen-collins-2b8207aa_youd-never-trust-raw-user-input-in-production-activity-7345454102904041472-vyw7">You’d never trust raw user input in production. So why are you piping...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#generative AI`, `#LLMs`, `#slop`, `#human-AI collaboration`

---

<a id="item-9"></a>
## [珀乐互动完成天使轮融资，以 AI+IP 重塑数字内容生态](https://36kr.com/p/3735324365094918?f=rss) ⭐️ 7.0/10

成立于 2025 年的 AI 数字内容公司珀乐互动已完成数千万元人民币天使轮融资，由星连资本领投、春华创投跟投。公司正通过自研多模态工具「剧灵 AI」和「珀乐视界」、与智谱 AI 等大模型厂商的深度合作，以及 AI 动画短剧《明日周一》等商业化项目，推进其“AI+IP”战略。 这一进展标志着生成式 AI 与娱乐产业知识产权（IP）管理的深度融合，初创企业不再仅提供工具，而是在重塑数字内容的创作、确权与变现模式。珀乐互动对版权合规和 Token 化数字资产的重视，可能为媒体行业的 AIGC 应用树立伦理与可扩展性标杆。 珀乐互动将智谱 AI、生数科技等头部大模型底座深度整合进技术中台，采用“艺术家原创手绘+AI 提效”模式构建高质量数据飞轮，并已通过 API 向某头部平台开放服务超万名创作者。其即将推出的“全模态互动叙事平台”计划引入 Token 机制，实现 IP 资产的全球化流转。

rss · 36kr · Mar 24, 02:00

**背景**: “AI+IP”指将人工智能（尤其是大语言模型和多模态模型）深度融入影视、游戏、文学等知识产权的开发与运营。AIGC（人工智能生成内容）平台在提升内容生产效率的同时，也引发对版权归属和数据来源的关切。多模态 AI 能同时处理文本、图像、音频和视频，为泛娱乐场景提供更丰富的交互体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cn.chinadaily.com.cn/a/202503/28/WS67e667bea31008317a2af380.html">AI+IP 深度融合：百度智能云赋能千亿级IP衍生市场创新发展</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202401291619258531_1.pdf">中航证券-人工智能行业大 模 型专题报告百 模 渐欲迷人眼AI...</a></li>

</ul>
</details>

**标签**: `#AI+Entertainment`, `#AIGC`, `#LLM`, `#Digital Content`, `#Startup Funding`

---

<a id="item-10"></a>
## [开发者通过自定义 API 端点将 Cursor 额度消耗降低 10 倍](https://www.v2ex.com/t/1200621#reply1) ⭐️ 7.0/10

一位开发者通过实测分析了 Cursor 的额度消耗规律，并展示了如何通过配置自定义 OpenAI 兼容 API 端点（如使用 OpenRelay 工具）绕过官方配额限制，尤其适用于高消耗的 Agent 模式任务。 该方法使开发者能更可持续、低成本地使用 Cursor 等 AI 编程助手，避免因额度耗尽导致服务降级，同时获得使用其他或更新大语言模型的灵活性。这也反映了 AI 工具生态中社区驱动优化的日益重要趋势。 用户发现 Agent 模式每个复杂任务消耗 15–30 次快速请求，迅速耗尽 Cursor Pro 每月 500 次的配额。通过将 Chat 和 Agent 请求路由到本地 OpenRelay 代理（聚合 33 个平台的免费额度），官方额度使用量减少约 70%，并避免了降级到慢速模式。

rss · V2EX · Mar 24, 02:00

**背景**: Cursor 是一款 AI 驱动的代码编辑器，提供行内补全（Tab）、聊天辅助和 Agent 模式——后者是一种能自主规划、编辑文件、运行命令并迭代任务的智能代理。其“快速请求”配额用于高优先级推理，耗尽后会降级为慢速响应。许多 AI 平台提供 OpenAI 兼容的 API 端点，允许第三方工具通过与 OpenAI /v1/chat/completions 相同的接口集成不同大模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/cn/docs/agent/overview">概述 | Cursor Docs</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/13553491637">Cursor效率之道：Agent模式＋7大高级技巧详解 - 知乎</a></li>
<li><a href="https://loudu.cn/reference/openai.html">OpenAI 兼 容 性 | Ollama学习指南</a></li>

</ul>
</details>

**标签**: `#AI Coding Assistant`, `#LLM`, `#Developer Tools`, `#API Integration`, `#Cost Optimization`

---

<a id="item-11"></a>
## [发布新型多智能体任务协作管理工具](https://www.v2ex.com/t/1200619#reply0) ⭐️ 7.0/10

一位开发者发布了一款名为 Agenet 的新型网页工具，支持基于任务的多 AI 智能体协作，每个任务拥有独立上下文。该工具集成了 Claude、Codex 和 OpenClaw 三种智能体。 该工具突破了当前单一聊天窗口与智能体交互的局限，通过结构化、任务隔离的工作流提升可用性。这对构建可扩展、有组织的多智能体系统具有实际意义，而此类系统正是复杂 LLM 应用落地的关键。 每个任务拥有独立上下文并调用专属智能体；目前支持 Claude、Codex 和 OpenClaw。在线试用地址为 https://agenet.elsetech.app，但未公开技术架构或 API 细节。

rss · V2EX · Mar 24, 01:48

**背景**: 多智能体协作指协调多个具备自主性和专用角色的 AI 智能体，通过分布式决策共同完成复杂任务，效果优于单一智能体。此类工具旨在解决上下文隔离与工作流编排等关键挑战。OpenClaw 是一个开源个人 AI 智能体，可通过 WhatsApp、Telegram 等平台执行任务，并确保用户数据完全由本地控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html">Multi-agent collaboration - AWS Prescriptive Guidance</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is multi-agent collaboration? - IBM</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM`, `#Tooling`, `#Multi-Agent Systems`, `#Developer Tools`

---

<a id="item-12"></a>
## [腾讯内测 AI 问股小程序](https://mp.weixin.qq.com/s/JdwMZQiiY2_lRGZxux_Fkw) ⭐️ 7.0/10

腾讯正在内测名为“AI 问股”的微信小程序，依托大语言模型解答证券相关问题，目前仅对申请成为内测体验官的受邀用户开放。 此举标志着腾讯依托其庞大的微信生态，战略性进军 AI 驱动的财富管理领域，可能改变与东方财富、同花顺等平台在互联网财富管理市场的竞争格局。 该小程序旨在补足腾讯自选股、理财通等现有金融产品的智能服务环节，目前处于内测阶段，需申请资格方可使用。

telegram · zaihuapd · Mar 23, 04:47

**背景**: 大语言模型（LLM）正越来越多地应用于金融领域，用于解读复杂数据、生成投资洞察并辅助决策。在中国，微信小程序作为超级应用生态内的轻量化工具，无需单独下载即可快速部署 AI 金融服务，已成为金融科技产品的重要载体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pm-research.com/content/iijpormgmt/51/2/162">Large Language Models for Financial and Investment Management ...</a></li>
<li><a href="https://digitalcreative.cn/blog/china-mini-programs-ecosystems-wechat-alipay-douyin">The Mini Program Multiverse: Explore China's Super App Ecosystems</a></li>

</ul>
</details>

**标签**: `#AI Finance`, `#Large Language Models`, `#Wealth Tech`, `#Tencent`, `#Product Launch`

---