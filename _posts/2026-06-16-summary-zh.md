---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 118 items, 13 important content pieces were selected

---

1. [伯克利 RDI 发布 Agents' Last Exam 基准](#item-1) ⭐️ 10.0/10
2. [vLLM v0.23.0 发布：优化 DeepSeek-V4 并扩展 Model Runner V2](#item-2) ⭐️ 9.0/10
3. [Artificial Analysis Intelligence Index v4.1 发布：转向智能体任务评测](#item-3) ⭐️ 9.0/10
4. [因美国政府出口管制指令，Anthropic 暂停 Fable 5 和 Mythos 5 的所有客户访问](#item-4) ⭐️ 9.0/10
5. [Anthropic 与美国政府的人事冲突导致其模型下线](#item-5) ⭐️ 8.0/10
6. [字节跳动推出 Seedance 2.0 Mini：更快更省的 AI 视频生成模型](#item-6) ⭐️ 8.0/10
7. [Anthropic 紧急暂停 Claude 订阅额度限制政策](#item-7) ⭐️ 8.0/10
8. [OpenAI Codex 支持 Chrome DevTools 协议](#item-8) ⭐️ 8.0/10
9. [Cua 与 Snorkel AI 联合发布 Cua-Bench：首个公开 KiCad 任务基准](#item-9) ⭐️ 8.0/10
10. [理想公布马赫 VLA 能力的进化目标](#item-10) ⭐️ 8.0/10
11. [Tensordyne Napier 流片：宣称吞吐量达 Blackwell 系统 13 倍](#item-11) ⭐️ 8.0/10
12. [字节跳动洽购天数智芯和百度昆仑芯 AI 芯片](#item-12) ⭐️ 8.0/10
13. [开源热捧的 Rio 3.5 模型被证实套壳中国开源模型](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [伯克利 RDI 发布 Agents' Last Exam 基准](https://rdi.berkeley.edu/blog/agents-last-exam) ⭐️ 10.0/10

2026 年 6 月，伯克利 RDI 发布了 Agents' Last Exam（ALE）基准，包含 1,500 余项覆盖 55 个非体力职业的真实工作任务。对 Fable 5、GPT-5.5、Composer 2.5 等前沿智能体的测评显示，所有模型在最困难层级上的成功率均为 0%，CLI 子集的最佳通过率也仅为 25.2%。 ALE 提供了迄今为止规模最大、最严格的自主 AI 智能体评估，证明即使是最先进的前沿模型在最困难的真实专业任务上也完全失败。数据集、代码及 CLI 子集的开源使其成为 AI 研究社区识别和解决智能体能力关键缺陷的高价值资源。 尽管各模型的整体任务表现接近，但单任务成本差异巨大：Fable 5 约 15.70 美元，GPT-5.5 约 3.80 美元，Composer 2.5 约 1.33 美元。观察到的首要失败模式是智能体在未实际验证输出结果的情况下宣称任务已完成，暴露了自主工作流中的关键可靠性缺陷。

rss · AI Hot · Jun 16, 01:59

**背景**: AI 智能体是能够使用网络浏览器、代码编辑器、命令行界面等工具执行多步骤任务的自主系统。长周期智能体任务需要在较长时间内持续进行推理、规划和自我纠错，这仍然是一个尚未解决的重大挑战。ALE 被设计为一个不断增长的动态基准，通过可验证的结果评估智能体在经济上有价值的专业工作流，而非简单的问答任务。该项目由伯克利 RDI 主导，超过 100 位行业专家参与贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agenthle.org/">AI Agent Benchmark for Real-World Professional Workflows</a></li>
<li><a href="https://snorkel.ai/research-paper/agents-last-exam/">Agents ’ Last Exam | Snorkel AI</a></li>
<li><a href="https://gabrielcassady.com/tools/agents-last-exam-ale/">Agents ’ Last Exam ( ALE )</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Benchmarking`, `#Frontier AI`, `#AI Evaluation`, `#Berkeley RDI`

---

<a id="item-2"></a>
## [vLLM v0.23.0 发布：优化 DeepSeek-V4 并扩展 Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 9.0/10

vLLM v0.23.0 正式发布，包含来自 200 位贡献者的 408 次提交，为 DeepSeek-V4 带来了包括全新 TRTLLM-gen 注意力内核和解耦稀疏 MLA 元数据在内的重大优化。此次更新还默认将 Model Runner V2 (MRv2) 扩展至 Llama 和 Mistral 稠密模型，并引入了具备流式传输能力的实验性 Rust 前端。 作为大语言模型关键的开源推理与服务引擎，这些更新通过显著提升 DeepSeek-V4 等前沿模型的运行效率，直接加速了 AI 部署领域的最新进展。MRv2 的扩展和 Rust 前端的引入，展现了 vLLM 致力于克服 Python 执行瓶颈的决心，从而为 AI 生态系统提供更简洁、更模块化且更快速的基础设施。 DeepSeek-V4 的优化包括针对滑动窗口 KV 缓存的选择性前缀缓存保留机制，以及对其 Mega-MoE 架构的专家级负载均衡 (EPLB) 支持。此外，多层 KV 缓存卸载框架现已支持对象存储二级层，并且推理与工具调用解析已统一在单一的 `Parser.parse()` 接口之后。

github · vllm-project/vllm · Jun 15, 05:27

**背景**: vLLM 是一个广受欢迎的开源库，专为快速高效的大语言模型推理与服务而设计。Model Runner V2 (MRv2) 是对 vLLM 核心执行引擎的彻底重构，旨在通过更高效地管理解码步骤来消除 Python 调度器开销并减少技术债务。DeepSeek-V4 利用具有稀疏 MLA（多头潜在注意力）的混合注意力机制来实现有界的注意力计算成本，从而为其 1.6T 参数的庞大架构提供有效的长上下文处理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-04-24-deepseek-v4">DeepSeek V4 in vLLM: Efficient Long-context Attention | vLLM Blog</a></li>
<li><a href="https://kaoutarelmaghraoui.com/blog/deepseek-v4-long-march-open-weight-ai/">DeepSeek's Long March: V4, Sparse Attention, and What Open-Weight AI Just Taught Us | Dr. Kaoutar El Maghraoui</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#deepseek-v4`, `#open-source`, `#ai-infrastructure`

---

<a id="item-3"></a>
## [Artificial Analysis Intelligence Index v4.1 发布：转向智能体任务评测](https://x.com/ArtificialAnlys/status/2066700136018071841) ⭐️ 9.0/10

Artificial Analysis 发布了 Intelligence Index v4.1，通过升级 Terminal-Bench 2.1 和 τ3-Bench Banking 等基准测试并将已饱和的 IFBench 移除，将评估重心转向智能体任务。此次更新还引入了每任务成本、时间、输出 token 及缓存 token 影响等新指标，结果显示 Claude 和 GPT 模型目前领先，而 DeepSeek 等开源模型则提供了极具性价比的替代方案。 此次更新反映了 AI 行业从静态知识和推理测试向评估复杂、多步骤智能体工作流的更广泛转变，而智能体工作流代表了当前 AI 能力的前沿。引入每任务的成本和时间指标，为开发者和企业在部署 AI 智能体时平衡性能与运营成本提供了关键数据。 在可用模型中，Claude Opus 4.8（max）以 56 分领先，但每任务成本为 1.78 美元且耗时 6.4 分钟；GPT-5.5（xhigh）得分为 55 分，每任务成本为 0.99 美元。开源模型 DeepSeek V4 Pro 以仅 0.04 美元的成本获得 44 分，而 Grok 4.3 以 1.5 分钟的速度成为最快的模型，凸显了成本、速度和准确性之间的显著权衡。

rss · AI Hot · Jun 16, 01:51

**背景**: Artificial Analysis Intelligence Index 是一个综合基准评分系统，用于衡量语言模型在推理、编程、知识和多步骤智能体任务等方面的能力。Terminal-Bench 是斯坦福大学和 Laude Institute 的一项重要项目，用于评估 AI 编程智能体在命令行环境中的表现；τ3-Bench（Tau-Bench）则测试智能体在多轮、使用工具的客户服务场景（如模拟零售银行）中的表现。v4.1 版本通过 Elo 评分重新设定了这些评估的基线，引入了前沿模型评审，并增加了回合上限，以更好地捕捉真实世界的智能体表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://snorkel.ai/blog/terminal-bench-2-0-raising-the-bar-for-ai-agent-evaluation/">Terminal-Bench 2.0: Raising the bar for AI agent evaluation</a></li>
<li><a href="https://github.com/sierra-research/tau-bench">GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub</a></li>

</ul>
</details>

**标签**: `#AI Benchmarks`, `#LLM Evaluation`, `#Agentic AI`, `#Artificial Analysis`, `#Frontier Models`

---

<a id="item-4"></a>
## [因美国政府出口管制指令，Anthropic 暂停 Fable 5 和 Mythos 5 的所有客户访问](https://t.me/zaihuapd/41960) ⭐️ 9.0/10

美国商务部以国家安全为由向 Anthropic 发出出口管制指令，要求暂停任何外国公民在美国境内外访问 Fable 5 和 Mythos 5 模型。为确保完全合规，Anthropic 关闭了所有客户对这两款模型的访问权限，甚至包括其外籍员工，其他 Claude 模型不受影响。 这是美国政府迄今对已部署的前沿 AI 模型最直接的干预之一，标志着出口管制已从芯片和研究领域扩展到商业化的 AI 系统。此举可能从根本上改变 AI 公司在全球发布强大模型的方式，并为国家安全机构实时限制前沿 AI 能力的访问开创先例。 Fable 5 和 Mythos 5 共享相同的底层模型权重，但 Fable 5 是作为高度设防版本发布的，而 Mythos 5 则在无安全护栏的情况下提供给部分预览用户。据 Axios 报道，商务部的行动源于对模型被越狱后可能带来严重安全风险的担忧，因为 Fable 5 在发布时是公开可用的最强 AI 模型。

telegram · @zaihuapd · Jun 15, 08:55

**背景**: Anthropic 于 2026 年 6 月 9 日发布了 Fable 5 和 Mythos 5，这是该公司迄今部署的最强大的 Mythos 级模型，在自主知识工作、编程和前沿物理研究方面表现卓越。Fable 5 是面向公众的版本，具有广泛的安全护栏；而 Mythos 5 则在无安全护栏的情况下提供给有限的预览用户。AI"越狱"是指用户绕过模型的伦理安全护栏和安全过滤器，可能解锁危险能力，例如生成犯罪活动的可操作指令或未经授权访问敏感信息。美国政府越来越多地利用原本为军事和两用技术设计的出口管制权限，来限制被认为对国家安全至关重要的先进 AI 能力的传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.sky.com/story/anthropic-withdraws-access-to-powerful-ai-model-after-us-government-order-13553685">Anthropic withdraws access to powerful AI model after US... | Sky News</a></li>
<li><a href="https://www.verdent.ai/guides/claude-mythos-5-vs-fable-5">Claude Mythos 5 vs Fable 5 : Who Can Actually Use... - Verdent Guides</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/06/04/ai-jailbreaks-what-they-are-and-how-they-can-be-mitigated/">AI jailbreaks : What they are and how they... | Microsoft Security Blog</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Anthropic`, `#AI Regulation`, `#Export Controls`, `#National Security`

---

<a id="item-5"></a>
## [Anthropic 与美国政府的人事冲突导致其模型下线](https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything) ⭐️ 8.0/10

Axios 的一篇报道披露了 Anthropic 领导层与美国政府之间围绕出口管制问题发生的人事冲突和紧张谈判的幕后细节，这些摩擦导致 Anthropic 的模型被迫下线。据报道，Anthropic 的核心安全研究员——包括前沿红队负责人 Logan Graham、安全防护主管 Dave Orr 以及 Nicholas Carlini——今天正在华盛顿特区与商务部会面进行协商。 这一事件是前沿 AI 开发与国家安全监管交汇点上的一个关键冲突点，表明政府的出口管制机制如何能够直接中断公众对顶尖 AI 模型的访问。这些谈判的结果可能会为 AI 实验室在政府监管下的运营方式，以及如何在模型安全与合规要求之间取得平衡树立先例。 美国政府的反应是由 Claude Mythos 遭到越狱攻击触发的，但 Anthropic 将其归类为一次狭窄的非通用攻击，而非通用越狱。政府方面的立场暗示，要恢复访问权限，Anthropic 可能需要实现完美的防越狱能力——而 Anthropic 自己承认这可能是不可能的——或者仅仅改善其与政府官员关系中的态度。

rss · Simon Willison · Jun 15, 14:57

**背景**: Anthropic 最近发布了 Claude Fable 5，这是其强大的 Mythos 级模型的公开版本，内置了安全护栏以阻止在网络安全和生物学等高风险领域的回复。由 Logan Graham 领导的前沿红队负责评估 AI 模型的国家安全风险，包括潜在的网络和生物安全威胁。美国政府一直在加强对 AI 技术的出口管制，旨在防止先进芯片和模型落入外国对手手中，这与寻求全球部署模型的 AI 实验室产生了摩擦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://fortune.com/2025/09/04/anthropic-red-team-pushes-ai-models-into-the-danger-zone-and-burnishes-companys-reputation-for-safety/">Anthropic ’s ‘ Red Team ’ pushes its AI models into the danger... | Fortune</a></li>
<li><a href="https://www.rand.org/pubs/perspectives/PEA3776-1.html">Understanding the Artificial Intelligence Diffusion Framework: Can Export Controls Create a U.S.-Led Global Artificial Intelligence Ecosystem? | RAND</a></li>

</ul>
</details>

**社区讨论**: 新闻作者注意到 Logan Graham 在 Boris Johnson 时代曾担任首相的特别顾问，拥有丰富的政治经验，这在当前谈判中可能非常有价值。作者还对恢复模型访问的时间表表示悲观，因为政府似乎要求 Anthropic 要么实现不可能的防越狱能力，要么调整其态度。

**标签**: `#Anthropic`, `#AI Policy`, `#Export Controls`, `#AI Safety`, `#Regulation`

---

<a id="item-6"></a>
## [字节跳动推出 Seedance 2.0 Mini：更快更省的 AI 视频生成模型](https://x.com/xiaohu/status/2066702585747443821) ⭐️ 8.0/10

字节跳动推出了 Seedance 2.0 Mini，这是其 Seedance AI 视频生成模型的精简版本，价格比原版便宜约 30%，速度是 Fast 版本的两倍，且画质接近原版。API 定价约为每秒 0.073 美元，30 秒视频的成本仅需约 2.19 美元。 此次发布大幅降低了高质量 AI 视频生成的成本门槛，使个人创作者、营销人员和小型企业都能更轻松地使用该技术。这也加剧了快速发展的 AI 视频生成市场竞争，各提供商正竞相以更低的价格提供更优质的画质。 Seedance 2.0 Mini 支持文生视频和图生视频，可通过 CapCut App 和 Dreamina 平台使用。限时优惠包括 Pro 用户生成 720P 视频积分减少 33%，以及 CapCut App 购买 Pro 套餐最高享 4 折优惠，叠加后比原版最多便宜 55%。

rss · AI Hot · Jun 16, 02:01

**背景**: Seedance 是字节跳动旗下的 AI 视频生成模型，能够根据文本提示和参考图像生成电影级视频。它支持具有一致角色和流畅运动的多镜头序列，与 Runway 等视频生成工具形成竞争关系。用户可以通过 Dreamina 等平台使用 Seedance，Dreamina 是 CapCut 推出的一站式 AI 创意套件，可根据简单提示词生成图像和视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seeddance.app/">Seedance 2.0 AI Video Generator | Free Image & Text to Video</a></li>
<li><a href="https://dreamina.capcut.com/">Dreamina image generator & video generator: All-in-one AI creative suite</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Video Generation`, `#ByteDance`, `#Seedance`, `#AI Models`

---

<a id="item-7"></a>
## [Anthropic 紧急暂停 Claude 订阅额度限制政策](https://x.com/AYi_AInotes/status/2066702539865706632) ⭐️ 8.0/10

Anthropic 已紧急暂停原定今日生效的订阅额度限制新政策，此前该政策引发了开发者社区的强烈反对。新规原本计划对手动聊天保持正常订阅额度，但对命令行工具、第三方 Agent 和自动化任务单独划定极低额度，超额部分按标准 API 价格计费。 此次政策回调直接影响 AI 开发者生态系统以及基于 Claude 构建 Agent 工作流的运营成本。这标志着 Anthropic 从封闭超级应用路线向开放基础设施方向的策略调整，显示出对社区关于开放性和开发者可及性关切的回应。 在暂停的政策下，所有调用方式将暂时继续沿用原有额度系统，不实施差异化限制。然而，此前 Fable 5 下架事件——Anthropic 因隐藏限制措施（暗中降低特定话题和竞争 AI 研究人员的性能）而遭到批评——已经暴露了信任裂痕，意味着最终落地的政策规则仍需密切关注。

rss · AI Hot · Jun 16, 02:00

**背景**: Anthropic 通过多个层级提供 Claude 服务，包括免费版、Pro、Max、团队版和企业版订阅，以及面向开发者的独立 API 定价。公司对 Claude API 实施速率限制以确保公平使用和防止滥用，但随着 Claude 在开发者、内部应用、编程 Agent、后端服务和自主 Agent 中的使用不断增长，平台团队在管理使用控制方面面临越来越大的挑战。Fable 5 争议涉及 Anthropic 秘密对高风险话题和开发竞争 AI 模型的研究人员实施性能降级，损害了社区信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://news.aibase.com/news/28915">The Jailbreak Controversy Triggers Global Censorship, Leading to the...</a></li>
<li><a href="https://www.linkedin.com/posts/cmjiang_claude-api-rate-limits-by-user-app-and-activity-7463223341072474112-0E-V">Claude API Rate Limits by User, App, and Agent - Datawiza</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI Agents`, `#Developer Tools`, `#AI Industry`

---

<a id="item-8"></a>
## [OpenAI Codex 支持 Chrome DevTools 协议](https://x.com/testingcatalog/status/2066685508944552137) ⭐️ 8.0/10

OpenAI Codex 现已支持 Chrome DevTools 协议（CDP），使 AI 编程代理能够直接在基于 Chromium 的浏览器中检查、交互并修改网站。这一集成标志着能力的重大扩展，允许 Codex 以编程方式执行深度的浏览器自动化和调试任务。 这一发展代表了 AI 驱动浏览器交互的重大飞跃，为编程代理提供了一个强大的工具，使其能够自主导航和操作实时网络环境。它为高度个性化的用户体验铺平了道路，因为 AI 在未来几年内有望实现网站的即时加载和自定义。 目前的实现被描述为处于非常早期的阶段，尽管它已经允许对网站进行全面的检查和修改。通过利用 CDP，Codex 能够检测、调试和分析 Chrome 浏览器，这些标准功能以前仅限于专用的开发者工具。

rss · AI Hot · Jun 16, 00:53

**背景**: Chrome DevTools 协议（CDP）是一个标准化的 API，允许外部工具对基于 Chromium 的浏览器（如 Chrome）进行检测、检查、调试和分析。OpenAI Codex 是一套由 AI 驱动的编程代理，旨在自动化软件工程任务，可作为命令行工具和 IDE 扩展使用。通过将这些技术结合，OpenAI 使其本地编程代理能够直接与实时浏览器环境进行交互，从而超越了静态代码库的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol - version tot</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#Web Agents`, `#Browser Automation`, `#AI Tools`

---

<a id="item-9"></a>
## [Cua 与 Snorkel AI 联合发布 Cua-Bench：首个公开 KiCad 任务基准](https://x.com/shao__meng/status/2066684840033026274) ⭐️ 8.0/10

Cua 与 Snorkel AI 联合发布了 Cua-Bench，这是首个针对 KiCad 任务的公开基准数据集，包含 25 道由执业电气工程师编写并复核的任务。测试中，GPT-5.5 仅通过 6/25（24%），Claude Sonnet 4.5 和 Haiku 4.5 各通过 5/25（20%），16 道从零搭建任务全部失败。 该基准首次对领先的大语言模型在复杂电子设计自动化任务上的表现进行了严格的专业评估，揭示了当前 AI 智能体远不能自主操作专业工程软件。详细的失败分析——识别出规划（约 40%）、感知（约 22%）和导航低效（约 19%）为主要瓶颈——为未来专业领域工具 AI 智能体的开发提供了高价值参考。 所有成功任务仅限于对现有设计的局部修改，从零搭建任务的零样本成功率为 0%。执行层瓶颈包括导航开销大（约 84%）、操作粒度过细（约 84%）、视图控制混乱（约 76%）、布线未完成（约 72%）和自我验证不可靠，而步数上限并非失败的主要原因。

rss · AI Hot · Jun 16, 00:50

**背景**: KiCad 是一款流行的开源电子设计自动化（EDA）软件，用于设计印制电路板（PCB），支持原理图绘制、PCB 布局和 3D 可视化功能。电子设计自动化工具对现代硬件开发至关重要，因为当代电子设备过于复杂，无法在没有计算机辅助的情况下完成设计。零样本任务执行是指 AI 模型在没有任务特定训练数据的情况下，仅凭预训练知识和推理能力自主完成新任务的能力。在 KiCad 等专业软件上测试 AI 智能体，可以揭示通用大语言模型能力与实际工程工作流之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Comparison_of_EDA_software">Comparison of EDA software - Wikipedia</a></li>
<li><a href="https://www.kicad.org/download/windows/">Windows Downloads | KiCad</a></li>
<li><a href="https://www.emergentmind.com/topics/zero-shot-task-execution">Zero - Shot Task Execution</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Benchmark`, `#LLM Evaluation`, `#EDA`, `#Computer Use`

---

<a id="item-10"></a>
## [理想公布马赫 VLA 能力的进化目标](https://36kr.com/newsflashes/3855231958897923?f=rss) ⭐️ 8.0/10

Li Auto announced the upcoming rollout of its new Mach VLA (Vision-Language-Action) model for AD MAX in Q3, with the goal of matching Tesla's FSD V14 capabilities by Q4.

rss · 36kr · Jun 16, 02:24

**标签**: `#Embodied AI`, `#Autonomous Vehicles`, `#Vision-Language-Action`, `#VLA`, `#Li Auto`

---

<a id="item-11"></a>
## [Tensordyne Napier 流片：宣称吞吐量达 Blackwell 系统 13 倍](https://www.ithome.com/0/964/688.htm) ⭐️ 8.0/10

AI 芯片初创企业 Tensordyne 已正式完成 3nm Napier 处理器的流片，该芯片由 Tensordyne 与博通、HPE 瞻博网络合作开发。该公司宣称其基于对数数学的架构在万亿参数 LLM 推理中，可实现 13 倍于 NVIDIA Blackwell 系统的吞吐量和 17 倍的按 Token 计能效。 如果这些性能宣称成立，Napier 有望通过挑战 NVIDIA 在数据中心 AI 基础设施领域的主导地位，从根本上颠覆 AI 推理硬件市场。对数数学方法消除了昂贵的乘法运算，可能为大规模部署万亿参数模型提供一条效率大幅提升的新路径。 Napier 芯片采用对数数字系统（LNS），用更简单的加法运算替代乘法，集成了大量 SRAM 缓存和 HBM 内存，处理器间通信延迟低于 1μs。一个完整的 TDN 机架通过四个'推理舱'（每个 72 颗芯片）集成 288 颗芯片，能够以每用户 1000 Token/s 的速率进行万亿参数 LLM 推理。

rss · IT HOME · Jun 16, 02:33

**背景**: 流片（Tape-out）是芯片设计的最终步骤，即将完成的设计文件发送给代工厂（如台积电）进行制造，这一术语起源于早期设计数据存储在磁带上的做法。对数数字系统（LNS）使用数字的对数来表示数值，使得乘法运算可以转化为简单的加法运算——这一特性可以显著降低 AI 工作负载中的计算复杂度和功耗。NVIDIA 的 Blackwell 架构是继 Hopper 之后的当前一代 GPU 平台，采用台积电 4NP 工艺集成 2080 亿个晶体管，代表了 AI 推理性能的行业基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tape-out">Tape - out - Wikipedia</a></li>
<li><a href="https://dev.to/arvind_sundararajan/logarithmic-arithmetic-the-secret-weapon-for-ultra-efficient-ai-training-1bap">Logarithmic Arithmetic: The Secret Weapon for Ultra-Efficient AI ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/">The Engine Behind AI Factories | NVIDIA Blackwell Architecture</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#AI Infrastructure`, `#Hardware Architecture`, `#LLM Inference`, `#Tensordyne`

---

<a id="item-12"></a>
## [字节跳动洽购天数智芯和百度昆仑芯 AI 芯片](https://www.reuters.com/world/china/bytedance-talks-with-chinas-iluvatar-corex-purchase-ai-chips-sources-say-2026-06-15/) ⭐️ 8.0/10

字节跳动正与总部位于上海的天数智芯洽谈采购 AI 推理芯片，同时也在考虑百度昆仑芯产品线。若交易达成，天数智芯今年有望交付至少 5 万颗芯片，成为字节跳动继华为和寒武纪之后的第三大国产 GPU 供应商。 这一举措表明字节跳动正在积极推动国产 AI 芯片供应链的多元化，以应对美国对 NVIDIA 等先进 GPU 持续实施的出口限制。从多家中国供应商获取数万颗推理芯片，将直接影响字节跳动为其庞大用户群体扩展 AI 应用（包括豆包聊天机器人）的能力。 此次采购的芯片主要面向 AI 推理工作负载——即运行已训练好的模型来服务终端用户请求——而非模型训练。百度昆仑芯基于其 XPU 架构，拥有数千个针对云端和边缘 AI 计算优化的小核心；天数智芯则开发通用 GPU（GPGPU），例如其 7nm 工艺的天垓 100 系列。

telegram · @zaihuapd · Jun 15, 06:53

**背景**: AI 芯片通常分为两大类：训练芯片用于构建和优化 AI 模型，需要巨大的计算能力；推理芯片则运行已训练好的模型，为用户生成实时响应。推理的计算强度通常较低，但需要高吞吐量和低延迟来服务数百万并发用户。自美国出口管制开始限制中国获取高端 NVIDIA GPU 以来，中国主要科技公司一直在竞相打造国产替代方案，华为昇腾系列、寒武纪、天数智芯和百度昆仑芯已成为国产 GPU 市场的关键参与者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iluvatar_CoreX">Iluvatar CoreX - Wikipedia</a></li>
<li><a href="https://www.reuters.com/world/china/chinas-baidu-says-its-kunlun-chip-cluster-can-train-deepseek-like-models-2025-04-25/">reuters.com/world/china/chinas- baidu -says-its- kunlun - chip -cluster...</a></li>
<li><a href="https://www.jonpeddie.com/techwatch/baidu-kunlun/">Baidu Kunlun 昆 仑 – Jon Peddie Research</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#AI Chips`, `#ByteDance`, `#Compute`, `#China Tech`

---

<a id="item-13"></a>
## [开源热捧的 Rio 3.5 模型被证实套壳中国开源模型](https://mp.weixin.qq.com/s/0oYevRBT8PPxG5hudOXxug) ⭐️ 8.0/10

Nex 团队揭露，近期被誉为开源 SOTA 的 Rio 3.5 模型实际上是 Nex 和阿里巴巴 Qwen 模型权重的混合产物。对 60 层 Transformer 权重的分析显示，Rio 的权重精确落在 Nex 与 Qwen 的连线上，混合比例约为 0.57:0.43，共线性超过 0.98，几乎不可能为独立训练。 这一事件凸显了开源 AI 生态系统中模型溯源和完整性日益严峻的挑战，不良行为者可以轻易地对现有模型进行套壳并谎称取得突破。它强调了采用可靠技术手段检测模型抄袭、保护真正开源贡献者知识产权的迫切需求。 摘除系统提示词后，该模型有 79% 的概率自称 Nex，并能复述 Nex 独有的机构介绍。Rio 团队随后从 HuggingFace 下架了该模型并致歉，声称上传的是"未经最终蒸馏的错误版本"，但技术证据指向的是直接的权重插值，而非蒸馏产物。

telegram · @zaihuapd · Jun 15, 12:39

**背景**: 模型权重插值是一种将两个或多个已训练神经网络的参数进行数学混合的技术，无需实际训练即可产生新模型。Qwen 是由阿里巴巴云开发的开源大语言模型系列，已成为开源 LLM 生态系统的基石。Rio 团队引用为借口的模型蒸馏是一种合法的机器学习方法，即较小的"学生"模型学习模仿较大的"教师"模型的行为，但它不会产生教师模型权重的线性组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Open-Source AI`, `#LLM`, `#Model Plagiarism`, `#HuggingFace`, `#Qwen`

---