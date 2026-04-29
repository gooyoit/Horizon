---
layout: default
title: "Horizon Summary: 2026-04-29 (ZH)"
date: 2026-04-29
lang: zh
---

> From 89 items, 25 important content pieces were selected

---

1. [蚂蚁集团开源百灵 Ling-2.6-flash，提供多版本量化模型](#item-1) ⭐️ 9.0/10
2. [谷歌与五角大楼签署 2 亿美元机密 AI 协议](#item-2) ⭐️ 9.0/10
3. [Qwen 开源高性能线性注意力内核库 FlashQLA](#item-3) ⭐️ 9.0/10
4. [NVIDIA 发布 Nemotron 3 Super：1200 亿参数开源 MoE 多智能体 AI 模型](#item-4) ⭐️ 9.0/10
5. [泄露的 OpenAI Codex 指令限制提及特定生物](#item-5) ⭐️ 8.0/10
6. [推出 Talkie：一个基于 1931 年前文本训练的 130 亿参数复古语言模型](#item-6) ⭐️ 8.0/10
7. [TermCat 新增 Claude Code 插件面板](#item-7) ⭐️ 8.0/10
8. [OpenHermit：开源平台专为管理上百个 AI 智能体而生](#item-8) ⭐️ 8.0/10
9. [OpenAI Codex 更新频率激增，应对 AI 编程工具竞争](#item-9) ⭐️ 8.0/10
10. [全新一代红旗 H9 发布：首搭华为乾崑智驾 ADS 5 与图像级激光雷达](#item-10) ⭐️ 8.0/10
11. [追觅发布三款搭载全固态电池与 2000 TOPS 算力的电动车](#item-11) ⭐️ 8.0/10
12. [中国以国家安全为由禁止外资收购 Manus 项目](#item-12) ⭐️ 8.0/10
13. [DeepSeek 大幅下调 API 价格，V4-Pro 限时优惠](#item-13) ⭐️ 8.0/10
14. [谷歌测试 AI 驱动的 YouTube 对话式搜索“Ask YouTube”](#item-14) ⭐️ 8.0/10
15. [Anthropic AI 智能体实测二手交易，成果与乌龙并存](#item-15) ⭐️ 8.0/10
16. [教育部新增 38 种本科专业，含具身智能等交叉学科](#item-16) ⭐️ 8.0/10
17. [剪映、即梦 AI 因 AI 内容标识不规范被处罚](#item-17) ⭐️ 8.0/10
18. [LiteLLM Proxy 存在严重 SQL 注入漏洞](#item-18) ⭐️ 8.0/10
19. [Warp 开源基于终端的智能开发环境](#item-19) ⭐️ 8.0/10
20. [Git Pitcher 将 GitHub 仓库转换为 AI 智能体计划](#item-20) ⭐️ 8.0/10
21. [伊格莱西亚斯更青睐专业 AI 软件而非 DIY“氛围编程”](#item-21) ⭐️ 7.0/10
22. [可回收火箭密集验证开启，商业航天迈向规模化量产元年](#item-22) ⭐️ 7.0/10
23. [AI 智能体难以应对遗留代码库](#item-23) ⭐️ 7.0/10
24. [AI Chrome 插件自动提取日程事件](#item-24) ⭐️ 7.0/10
25. [地平线余凯：拒绝内卷，以用户体验驱动“外卷”](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [蚂蚁集团开源百灵 Ling-2.6-flash，提供多版本量化模型](https://www.ithome.com/0/944/768.htm) ⭐️ 9.0/10

蚂蚁集团正式开源百灵大模型 Ling-2.6-flash，这是一款总参数量达 104B 的指令微调语言模型，采用混合线性架构，并提供 BF16、FP8 和 INT4 等多种量化版本。该模型两周前曾以 Elephant Alpha 的匿名身份在 OpenRouter 上线，现已根据开发者反馈完成多轮优化。 此次开源大幅降低了高性能大语言模型的部署门槛，通过高推理速度、卓越的 token 效率以及适配不同硬件的量化版本，让前沿 AI 技术更易于被开发者和企业采用。这也彰显了蚂蚁集团在全球开源大模型生态中的日益重要地位。 Ling-2.6-flash 在 4 张 H20 GPU 上推理速度最高可达 340 tokens/s，prefill 吞吐量是 Nemotron-3-Super 的 2.2 倍；在 Artificial Analysis 评测中仅消耗 1500 万 tokens，约为竞品的十分之一；尽管激活参数仅为 7.4B，但在 SWE-bench Verified、PinchBench 等面向智能体的评测中表现接近或达到 SOTA 水平。

rss · IT HOME · Apr 29, 01:27

**背景**: 大语言模型（LLM）通常需要大量计算资源，导致部署成本高昂。模型量化（如 BF16、FP8、INT4）通过降低数值精度来减少显存占用并加速推理，同时尽量保持性能。混合线性架构结合了不同神经网络模块（例如 Mamba 与 Transformer 块），以在推理速度和模型能力之间取得平衡。蚂蚁集团百灵大模型团队致力于研发可实际落地的基础模型，服务于真实应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/aolan123/article/details/142484865">Mamba+Transformer 混 合 架 构 多 模 态 大 模 型 _多 模 态mamba-CSDN博客</a></li>
<li><a href="https://www.iaiol.com/teng-xun-hun-yuan-ying-wei-da-dou-fa-hun-he-jia-gou-mo-xing-mamba-transformer-yao-jue-qi-ma">腾讯 混 元、英伟达都发 混 合 架 构 模 型 ，Mamba-Transformer... | AI在 线</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Open Source`, `#Model Quantization`, `#Frontier Tech`

---

<a id="item-2"></a>
## [谷歌与五角大楼签署 2 亿美元机密 AI 协议](https://www.theinformation.com/articles/google-signs-classified-ai-deal-pentagon-amid-employee-opposition) ⭐️ 9.0/10

谷歌已与美国国防部签署一份价值 2 亿美元的机密协议，将其 Gemini 人工智能模型用于包括任务规划和武器目标定位在内的敏感军事用途。此举紧随五角大楼终止与 Anthropic 的合作之后，后者因拒绝放宽 AI 安全限制而被列为供应链风险。 这标志着前沿人工智能大规模进入国防领域，引发了关于 AI 安全性、自主武器以及科技公司参与军事行动伦理的关键问题。同时表明美国政府正因地缘政治和伦理争议而加速 AI 供应商多元化。 协议允许 AI 用于“任何合法政府用途”，但禁止在无人监督下用于国内大规模监控或自主武器；然而谷歌无权否决政府的合法决策。OpenAI 也签署了类似协议，而 Anthropic 因拒绝削弱安全限制而被排除在外。

telegram · @zaihuapd · Apr 28, 11:47

**背景**: 美国国防部正根据其《数据、分析和人工智能应用战略》积极推动先进 AI 融入军事行动，强调负责任使用和风险管理。谷歌、OpenAI 和 Anthropic 等公司开发的“前沿模型”能力强大，既具变革潜力，也带来重大安全隐忧。2018 年谷歌员工曾因“Maven 项目”抗议公司与军方合作，凸显内部对军事 AI 的抵制情绪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cmes.org/library/recom/20b926a373c94064a0019df692dd897e.html">美国国防部发布《数据、分析和AI应用战略》</a></li>
<li><a href="https://www.bannedbook.org/bnews/itnews/20260303/2292941.html">科技工作者敦促撤销将Anthropic列为供应链风险 - 禁闻网</a></li>
<li><a href="https://www.huxiu.com/article/4838181.html">美国国防部与Anthropic谈判破裂，OpenAI迅速填补合作空缺</a></li>

</ul>
</details>

**标签**: `#AI`, `#military AI`, `#frontier technology`, `#AI policy`, `#national security`

---

<a id="item-3"></a>
## [Qwen 开源高性能线性注意力内核库 FlashQLA](https://qwen.ai/blog?id=flashqla) ⭐️ 9.0/10

Qwen 团队开源了基于 TileLang 构建、专为 Gated Delta Network 优化的高性能线性注意力内核库 FlashQLA，在 NVIDIA Hopper GPU 上实现了前向计算 2–3 倍、反向计算 2 倍的速度提升。 FlashQLA 通过先进的内核优化显著提升了长序列和端侧智能体 AI 模型的训练与推理效率，降低了计算开销。这一进展有助于高效注意力机制在下一代大语言模型中的广泛应用。 FlashQLA 利用算子融合、代数优化和 warpgroup 特化内核来重叠计算与数据搬运，提高 SM 利用率。它还针对 Gated Delta Network 的门控衰减特性引入自动卡内上下文并行，特别适用于小批量和长序列场景。

telegram · @zaihuapd · Apr 28, 14:11

**背景**: 线性注意力机制通过线性或次二次复杂度的近似方法替代标准的二次复杂度 softmax 注意力，从而高效处理长序列。Gated Delta Network（GDN）是一种新型线性注意力模型，结合输入依赖门控与 Delta 规则以增强记忆能力。TileLang 是一种用于高性能内核开发的领域专用语言，已应用于 BitBLAS 和 AttentionEngine 等项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with Delta Rule - arXiv</a></li>
<li><a href="https://github.com/tile-ai/tilelang">GitHub - tile -ai/ tilelang : Domain-specific language designed to...</a></li>
<li><a href="https://spaceservices.org/learn/efficient-attention-mechanisms">FlashAttention, Linear Attention & Long... | Space Services Research</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#attention mechanisms`, `#model optimization`, `#open source`

---

<a id="item-4"></a>
## [NVIDIA 发布 Nemotron 3 Super：1200 亿参数开源 MoE 多智能体 AI 模型](https://t.me/zaihuapd/41118) ⭐️ 9.0/10

NVIDIA 发布了 Nemotron 3 Super，这是一款拥有 1200 亿参数的开源大语言模型，采用混合专家（MoE）架构，并融合了 Mamba 层与 Transformer 层，专为多智能体 AI 系统设计，支持 100 万 token 的上下文窗口。 此次发布标志着高性能、可扩展模型在多智能体 AI 研究和应用领域的重大进展，而多智能体系统被视为通向通用人工智能的关键前沿。宽松的开源许可也鼓励开发者和研究人员进行更广泛的创新与定制。 尽管该模型总参数量达 1200 亿，但得益于 MoE 架构，推理时仅激活 120 亿参数。相比上一代 Nemotron Super 模型，其吞吐量最高提升 5 倍，准确率最高提升 2 倍。

telegram · @zaihuapd · Apr 29, 00:00

**背景**: 混合专家（MoE）是一种神经网络架构，针对每个输入仅激活部分“专家”子网络，从而在保持高模型容量的同时降低推理计算成本。Mamba-Transformer 混合架构结合了 Mamba（一种状态空间模型）在长序列处理上的高效性与 Transformer 在上下文建模方面的优势，特别适合需要长上下文推理的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://gregrobison.medium.com/architectural-evolution-in-large-language-models-a-deep-dive-into-jambas-hybrid-transformer-mamba-c3efa8ca8cae">Architectural Evolution in Large Language Models: A Deep Dive into Jamba’s Hybrid Transformer-Mamba Design | by Greg Robison | Medium</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models - arXiv</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Multi-Agent Systems`, `#Mixture of Experts`, `#Frontier Technology`

---

<a id="item-5"></a>
## [泄露的 OpenAI Codex 指令限制提及特定生物](https://simonwillison.net/2026/Apr/28/openai-codex/#atom-everything) ⭐️ 8.0/10

一份据称属于 GPT-5.5 的 OpenAI Codex 基础指令被泄露，明确禁止模型讨论哥布林、小精灵、浣熊、巨魔、食人魔、鸽子及其他生物，除非用户查询明确相关。 这揭示了 OpenAI 如何通过系统提示内部约束模型行为，为 AI 安全实践提供了罕见视角，并展示了提示工程在控制模型输出范围和降低幻觉风险中的关键作用。 该限制出现在 codex-rs 仓库的 models.json 文件中，被标注为 GPT-5.5 版本的“base_instructions”——但 OpenAI 尚未正式确认此版本。列表既包含神话生物，也包括浣熊和鸽子等真实动物，暗示其可能出于广泛的内容审核或对齐目标。

rss · Simon Willison · Apr 28, 22:02

**背景**: 系统提示是语言模型在与用户交互前接收的隐藏指令，用于定义其行为、语气和约束条件。它们不同于用户输入的提示，对确保模型输出符合安全、准确性和政策要求至关重要。OpenAI Codex 是一款专为代码生成和理解设计的大语言模型，但新版本可能具备更广泛的能力。“GPT-5.5”这一名称目前属于推测，并非 OpenAI 官方发布的产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/simplr_sh/mastering-system-prompts-for-llms-2d1d">Mastering System Prompts for LLMs - DEV Community</a></li>
<li><a href="https://medium.com/@larry_6938/the-importance-of-system-prompts-for-llms-4b07a765b9a6">The Importance of System Prompts for LLMs | by Larry Tao | Medium</a></li>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>

</ul>
</details>

**标签**: `#openai`, `#ai`, `#llms`, `#system-prompts`, `#prompt-engineering`

---

<a id="item-6"></a>
## [推出 Talkie：一个基于 1931 年前文本训练的 130 亿参数复古语言模型](https://simonwillison.net/2026/Apr/28/talkie/#atom-everything) ⭐️ 8.0/10

一个名为“Talkie”的新型 130 亿参数语言模型已发布，仅使用 1931 年之前出版的英文文本进行训练。该模型包含基础版本和经过指令微调的版本，均以宽松的 Apache 2.0 开源许可证发布。 这一发布推动了历史语言建模、AI 与复古知识对齐以及在公共领域数据上训练高性能模型可行性的研究。它还为探索模型如何在其训练截止日期之后进行外推（例如预测未来事件或重新发现科学突破）开辟了新途径。 基础模型在 2600 亿个 1931 年前的英文文本 token 上训练，这些数据在美国均已进入公有领域。指令微调版本使用了从历史参考文献中提取的合成数据，并依赖现代大语言模型（Claude Sonnet 4.6 和 Opus 4.6）进行偏好优化和多轮对话优化，可能引入时代错位的知识污染。

rss · Simon Willison · Apr 28, 02:47

**背景**: 指令微调是一种监督式微调技术，旨在让大语言模型更有效地遵循人类指令，从而在聊天机器人等交互式应用中更加实用。Apache 2.0 许可证是一种宽松的开源许可证，允许商业使用、修改和再分发，且无限制性条款，这在通常使用自定义许可证的主流 AI 模型中较为罕见。仅使用无版权数据训练模型（有时称为“纯素模型”）旨在避免与受版权保护或专有训练数据相关的法律和伦理问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@veer15/the-hitchhikers-guide-to-instruction-tuning-large-language-models-d6441dbf1413">The Hitchhiker’s Guide to Instruction Tuning Large Language Models</a></li>
<li><a href="https://www.mindstudio.ai/blog/gemma-4-apache-2-license-commercial-use">What Is Gemma 4's Apache 2.0 License? Why It Matters More Than the Model Itself | MindStudio</a></li>
<li><a href="https://arxiv.org/abs/2308.10792">[2308.10792] Instruction Tuning for Large Language Models : A Survey</a></li>

</ul>
</details>

**标签**: `#AI`, `#language models`, `#open-source AI`, `#historical NLP`, `#instruction tuning`

---

<a id="item-7"></a>
## [TermCat 新增 Claude Code 插件面板](https://www.v2ex.com/t/1209271#reply0) ⭐️ 8.0/10

开源 SSH 终端工具 TermCat 新增了名为“Claude Code Power”的插件，可在终端侧边栏实时显示 Claude Code 会话状态，并支持一键切换多套环境配置。 该集成将 AI 辅助编程与系统运维结合，在熟悉的终端界面中直观展示 Claude Code 的内部运行状态并简化配置管理，有助于提升开发者效率、减少上下文切换。这体现了智能体（agentic）AI 工具正深度融入开发者核心工作流的趋势。 该插件仅读取 ~/.claude/ 目录下的文件，不修改配置、不注入钩子；支持跨平台进程检测（Unix 系统用 lsof/ps，Windows 用 PowerShell/CIM）；除启动按钮外，其他操作仅填充命令到输入行，需用户按回车确认执行；若仅更换模型，可通过 /model 命令热切换而无需重启 Claude Code。

rss · V2EX · Apr 29, 01:51

**背景**: Claude Code 是 Anthropic 推出的智能体式 AI 编程助手，运行于终端中，可通过自然语言执行调试、重构、Git 操作等多步任务，支持插件、MCP（Model Context Protocol）服务器和自定义技能。TermCat 是基于 Electron 的终端工具，集成了 SSH、SFTP 和 AI 驱动的运维自动化功能，用户只需描述目标（如“排查 Nginx 502”），AI 代理即可规划步骤、执行命令并在关键操作前请求用户确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/plugins">Create plugins - Claude Code Docs</a></li>
<li><a href="https://github.com/anthropics/claude-code/blob/main/plugins/README.md">claude-code/plugins/README.md at main · anthropics/claude-code</a></li>

</ul>
</details>

**标签**: `#AI Developer Tools`, `#SSH Terminal`, `#Claude Integration`, `#AI Operations`, `#Open Source`

---

<a id="item-8"></a>
## [OpenHermit：开源平台专为管理上百个 AI 智能体而生](https://www.v2ex.com/t/1209270#reply0) ⭐️ 8.0/10

一位开发者发布了开源 AI 智能体平台 OpenHermit，通过将内部状态（如记忆、技能、密钥）与外部工作区文件分离，实现可扩展且安全的多智能体运维。该平台使用 PostgreSQL 集中管理状态，并内置 Telegram、Slack 和 CLI 等通信渠道。 当前的个人 AI 智能体框架缺乏对大量智能体进行安全高效管理的基础设施。OpenHermit 通过引入基于数据库的结构化状态管理填补了这一空白，这对团队协作、SaaS 产品或生产级 AI 智能体集群部署至关重要。 内部状态存储在 PostgreSQL 中，密钥使用 AES-256-GCM 加密，并按 agent_id 隔离；外部工作区文件保留在独立的 Docker 容器中。平台采用 TypeScript、Hono 和 Drizzle ORM 构建，采用 MIT 许可证，但仍处于早期开发阶段，文档和测试覆盖尚不完善。

rss · V2EX · Apr 29, 01:50

**背景**: Claude Code 或 OpenClaw 等 AI 智能体通常将所有状态（记忆、会话、技能）以本地文件形式存储，适用于单用户场景但难以扩展。Anthropic 提出的模型上下文协议（MCP）为 AI 智能体提供了标准化的工具集成方式，使其能安全地与外部系统交互。随着组织开始部署多个专业智能体，类似 LLM 领域的 DevOps 运维基础设施需求变得迫切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol - Anthropic</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.ibm.com/think/topics/model-context-protocol">What is Model Context Protocol (MCP)? - IBM</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open-source`, `#agent infrastructure`, `#LLM operations`, `#multi-agent systems`

---

<a id="item-9"></a>
## [OpenAI Codex 更新频率激增，应对 AI 编程工具竞争](https://www.v2ex.com/t/1209262#reply0) ⭐️ 8.0/10

OpenAI 的 Codex 现在每两三天就发布一个新版本，更新内容包括修复漏洞或版本号提升（如“5.5”）。这种加速节奏似乎与 Cursor 等 AI 编程工具带来的竞争压力同步。 快速迭代表明 OpenAI 正在优先应对快速发展的 AI 辅助编程市场，其中像 Cursor 这样的工具（据报道估值达 600 亿美元）正在重塑开发者的工作流和期望。这可能标志着 OpenAI 为应对商业威胁而转向更敏捷的模型部署策略。 更新有时使用小数版本号（如“5.5”），并常包含漏洞修复；用户还报告了配额限制和重置周期频繁且未提前通知的变动。由于缺乏对更新内容的清晰说明，依赖 Codex 进行生产开发的用户感到困惑。

rss · V2EX · Apr 29, 01:44

**背景**: OpenAI Codex 是一个能根据自然语言提示生成代码的 AI 系统，曾为 GitHub Copilot 等工具提供支持。近年来，Cursor 等专用 AI 编程助手因深度集成大语言模型并提供实时、上下文感知的编程支持而广受欢迎。AI 编程领域已成为前沿 AI 公司争夺开发者心智份额和商业化落地的关键战场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-3-codex/">Introducing GPT-5.3-Codex - OpenAI</a></li>
<li><a href="https://www.reddit.com/r/codex/comments/1rqm7ll/codex_rate_limits_changed_from_1_week_to_2_weeks/">Codex rate limits changed from 1 week to 2 weeks, renewal cycle pushed a day for me.</a></li>

</ul>
</details>

**社区讨论**: 原帖推测 OpenAI 可能因 Cursor 被传获马斯克给出 600 亿美元估值而加快动作。社区成员注意到异常频繁的更新和不一致的沟通，既对改进感到兴奋，也对系统不稳定表示困扰。

**标签**: `#AI`, `#Codex`, `#OpenAI`, `#code generation`, `#frontier tech`

---

<a id="item-10"></a>
## [全新一代红旗 H9 发布：首搭华为乾崑智驾 ADS 5 与图像级激光雷达](https://www.ithome.com/0/944/756.htm) ⭐️ 8.0/10

全新一代红旗 H9 正式发布，首次搭载华为最新乾崑智驾 ADS 5 系统、双光路图像级 896 线激光雷达和基于鸿蒙座舱的 HarmonySpace 智能座舱，并采用源自中式宫殿礼序美学的豪华设计。 此举标志着前沿人工智能自动驾驶技术深度融入中国高端自主品牌车型，凸显华为在智能汽车生态中的影响力日益增强。该车搭载全球量产线束规格最高的激光雷达，显著提升高阶自动驾驶所需的环境感知能力。 新车配备 40 颗高感知传感器，在 120km/h 时速下可稳定识别 120 米外 14 厘米高的微小障碍物，并支持一键隐私模式（切断全车对外网络及数据采集）。动力方面搭载红旗自研 2.0T 纵置两档混动系统，配四挡空气悬架。

rss · IT HOME · Apr 29, 00:52

**背景**: 华为乾崑智驾（ADS）是面向车企提供的模块化智能驾驶解决方案，ADS 5 为 2026 年推出的最新一代。896 线激光雷达将感知能力从传统的“点云级”提升至“图像级”，可实现更精细的环境建模。鸿蒙智舱 HarmonySpace 是基于鸿蒙操作系统的智能座舱平台，支持 MoLA 架构的智能语音助手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huawei_Intelligent_Automotive_Solution">Yinwang - Wikipedia</a></li>
<li><a href="https://m.ithome.com/html/942815.htm">“睁眼”看世界：华为乾崑 896 ...</a></li>
<li><a href="https://www.moomoo.com/news/post/68927320/seres-aims-to-delineate-the-technical-boundaries">Seres aims to delineate the technical boundaries. - Moomoo</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#AI in automotive`, `#Huawei ADS`, `#smart vehicles`, `#frontier tech`

---

<a id="item-11"></a>
## [追觅发布三款搭载全固态电池与 2000 TOPS 算力的电动车](https://finance.sina.com.cn/tech/2026-04-28/doc-inhvzfsh8617513.shtml) ⭐️ 8.0/10

追觅在旧金山发布三款全新电动车：零百加速 1.8 秒的超跑、全球首款搭载 60Ah 全固态电池和 2000 TOPS AI 算力的 SUV，以及配备响应时间仅 150 毫秒的固体火箭助推系统的概念车，计划于 2027 年量产交付。 这些车型展示了全固态电池、超高 AI 算力自动驾驶平台和新型推进系统的重大突破，有望推动整个电动车行业向更高性能、更安全能源和更强智能驾驶方向发展。若成功量产，将加速全固态电池和高算力 AI 平台的商业化落地。 该 SUV 首发全球首款 60Ah 全固态电池，全系标配 2160 线激光雷达和 2000 TOPS AI 芯片；火箭概念版采用双固体燃料助推器，但未公布量产计划；超跑配备四电机系统（总功率 1399kW），风阻系数低至 0.185。

telegram · @zaihuapd · Apr 28, 03:04

**背景**: 全固态电池使用固态电解质替代传统液态电解质，具有更高能量密度、更快充电速度和更高安全性。2000 TOPS（每秒万亿次运算）是当前自动驾驶领域顶尖的 AI 算力水平，与英伟达在 CES 2026 上展示的 DRIVE Thor 平台相当。车载火箭助推技术目前仍属实验性质，主要用于前沿性能探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.itiger.com/news/2601035700">CES2026|英伟达自动驾驶芯片算力突破2000TOPS，专家：更适配高端车型</a></li>
<li><a href="https://www.163.com/dy/article/KRD395O80556BPY5.html">刚刚！比亚迪固态电池通过车规验证！能量密度翻倍、10分钟充80% - 网易</a></li>
<li><a href="https://www.facebook.com/groups/myevoc/posts/2834513860271022/">Guess by the end of this decade, solid state could be the LFP equivalent... - Facebook</a></li>

</ul>
</details>

**标签**: `#electric vehicles`, `#AI hardware`, `#solid-state battery`, `#frontier technology`, `#autonomous driving`

---

<a id="item-12"></a>
## [中国以国家安全为由禁止外资收购 Manus 项目](https://t.me/zaihuapd/41102) ⭐️ 8.0/10

中国国家发展改革委已正式作出决定，以国家安全为由禁止外资收购 Manus 项目，并要求相关方撤销该交易。 此举标志着中国在前沿人工智能领域的一次重要监管干预，表明中国正加强对可能影响国家安全或战略竞争力的先进 AI 技术的外资控制审查。 该决定由国家发改委下属的外商投资安全审查工作机制办公室依据《外商投资安全审查办法》作出；公告未披露外国收购方的具体身份及交易细节。

telegram · @zaihuapd · Apr 28, 03:43

**背景**: 中国于 2020 年正式实施《外商投资安全审查办法》，要求对可能影响国家安全的关键领域（如人工智能、半导体和基础设施）的外资交易进行审查。该机制类似于美国的 CFIUS，但透明度较低。Manus AI 以开发先进推理模型著称，属于此类审查重点关注的“前沿技术”范畴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investmentpolicy.unctad.org/investment-laws/laws/570/china-foreign-investment-security-review-measures">China - Foreign Investment Security Review Measures | Investment Laws Navigator</a></li>
<li><a href="https://www.bakermckenzie.com/-/media/files/insight/publications/2021/01/foreign_investment_security_review_measures.pdf?la=en">[PDF] MEASURES FOR SECURITY REVIEW OF FOREIGN INVESTMENTS （Adopted at the 13th Commission Affairs Meeting of the National Developmen - Baker McKenzie</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#foreign investment`, `#national security`, `#Manus AI`, `#frontier technology`

---

<a id="item-13"></a>
## [DeepSeek 大幅下调 API 价格，V4-Pro 限时优惠](https://t.me/zaihuapd/41103) ⭐️ 8.0/10

DeepSeek 已将其所有 API 模型的输入缓存命中价格降至首发价的十分之一，并对 V4-Pro 模型推出限时优惠。 此次调价大幅降低了使用 DeepSeek 大语言模型的成本，尤其利好缓存复用率高的应用场景，使前沿 AI 技术对开发者和研究人员更加可及。 九折优惠仅适用于命中缓存的输入 token，并非全部用量；V4-Pro 的促销活动有时间限制，具体信息可查阅 DeepSeek 官方 API 文档。

telegram · @zaihuapd · Apr 28, 04:31

**背景**: 深度求索（DeepSeek）是一家中国 AI 公司，以其开源权重和自研大语言模型（如 DeepSeek-V2、DeepSeek-V3 系列）而知名。API 定价通常对输入、输出和缓存机制分别计费，以优化推理成本。输入缓存会存储已处理过的提示词，当相同或相似输入重复出现时，可避免重复计算，从而降低延迟和费用。

**标签**: `#AI`, `#API Pricing`, `#DeepSeek`, `#Large Language Models`, `#Frontier Tech`

---

<a id="item-14"></a>
## [谷歌测试 AI 驱动的 YouTube 对话式搜索“Ask YouTube”](https://www.theverge.com/streaming/919441/google-ask-youtube-ai-chatbot-search) ⭐️ 8.0/10

谷歌正在美国向 YouTube Premium 用户测试名为“Ask YouTube”的新 AI 功能，提供对话式搜索体验，可生成视频摘要、推荐内容并支持连续追问。该功能融合了对长视频、Shorts 和文本的多模态理解，生成带时间戳的信息回复。 此举标志着生成式 AI 在视频发现领域的重大应用，可能改变用户在全球最大视频平台上查找和互动内容的方式。这也体现了谷歌将对话式 AI 深度整合到其消费产品中以提升参与度和信息检索效率的整体战略。 该功能目前仅限美国 18 岁以上的 YouTube Premium 用户使用，但谷歌计划未来向非会员开放。初步测试显示其能提升搜索效率，但仍可能出现事实性错误，例如在介绍硬件产品历史时存在偏差。

telegram · @zaihuapd · Apr 28, 06:01

**背景**: 对话式 AI 允许用户通过自然语言对话而非关键词搜索与系统交互。YouTube 作为谷歌旗下平台，拥有超过 25 亿月活跃登录用户，并已逐步引入 AI 用于内容推荐和审核。“Ask YouTube”基于谷歌在大语言模型和多模态 AI 方面的进展，能够处理视频中的视觉与文本信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2ppaE1MLUVCRXl0a284bGRkYkh5Z0FQAQ?hl=en-PK&gl=PK&ceid=PK:en">Google tests AI conversational search feature Ask YouTube - Overview</a></li>
<li><a href="https://www.techbuzz.ai/articles/google-is-testing-ai-chatbot-search-for-youtube">Google is testing AI chatbot search for YouTube | The Tech Buzz</a></li>

</ul>
</details>

**标签**: `#AI`, `#conversational AI`, `#YouTube`, `#Google`, `#generative AI`

---

<a id="item-15"></a>
## [Anthropic AI 智能体实测二手交易，成果与乌龙并存](https://futurism.com/artificial-intelligence/claude-give-ai-agents-money-project-deal) ⭐️ 8.0/10

Anthropic 开展了名为“Project Deal”的实验，让基于 Claude 的 AI 智能体代表员工进行二手物品议价交易，共完成 186 笔真实交易。该实验既展示了 AI 在经济活动中的潜力，也暴露了其当前局限性。 该实验标志着自主 AI 系统在现实市场中代表人类行动的重要进展，是迈向实用化智能体的关键一步。但同时也凸显了可靠性、监管以及 AI 驱动商业缺乏法律框架等紧迫问题。 69 名参与者各提供 100 美元和闲置物品；使用更强模型的 AI 达成更优交易，但使用弱模型的用户往往毫无察觉。典型失误包括 AI 帮主人买回原本属于自己的滑雪板，或为“送自己礼物”而购入 19 个二手乒乓球。

telegram · @zaihuapd · Apr 28, 07:31

**背景**: “智能体 AI”（Agentic AI）指能在复杂环境中自主感知、决策并行动的系统，无需人类持续干预。与主要生成内容的传统 AI 不同，智能体 AI 专注于目标导向行为，如谈判、规划或交易。Anthropic 是一家以 AI 安全为核心的研究机构，开发了 Claude 系列大语言模型，正逐步将其应用于类智能体任务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://awesomeagents.ai/news/anthropic-project-deal-agent-commerce/">Stronger AI Agents Win More Deals - Users Never... | Awesome Agents</a></li>
<li><a href="https://opentools.ai/news/anthropics-project-deal-ai-agents-trade-real-goods-and-losers-cant-tell">Anthropic 's Project Deal : AI Agents Trade Real Goods and ..</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Claude`, `#Anthropic`, `#agentic AI`, `#AI economics`

---

<a id="item-16"></a>
## [教育部新增 38 种本科专业，含具身智能等交叉学科](https://mp.weixin.qq.com/s/T5yv1EVEL1mDSb1_58TO2g) ⭐️ 8.0/10

中国教育部批准新增 38 个本科专业，自 2026 年起招生，其中“具身智能”首次被纳入新设立的交叉学科门类。哈尔滨工业大学等 9 所高校获准开设具身智能专业。 此举将前沿人工智能研究——特别是 AI 与物理实体（如机器人）的融合——正式纳入高等教育体系，表明中国正战略性推动学术培养与前沿科技及实体经济需求对接。这体现了国家在 AI、机器人与认知科学交叉领域培养人才的优先方向。 具身智能专业归属于交叉学科门类，该门类现包含 15 种专业（11 种原有、4 种新增）。当前本科专业目录共涵盖 13 个学科门类、92 个专业类、883 种专业，“十四五”期间高校专业调整比例累计超 30%。

telegram · @zaihuapd · Apr 28, 08:52

**背景**: 具身智能指通过与物理或仿真环境交互来学习和行动的人工智能系统，融合感知、推理与动作，常依托机器人或虚拟智能体实现。其理论基础源于“具身认知”，认为智能源于身体与环境的互动。随着大模型局限性显现，该方向被视为通向更通用、适应性更强 AI 的重要路径，在全球范围内快速发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_cognition">Embodied cognition - Wikipedia</a></li>
<li><a href="https://github.com/TianxingChen/Embodied-AI-Guide/blob/main/files/具身智能基础技术路线-YunlongDong.pdf">Embodied-AI-Guide/files/具身智能基础技术路线-YunlongDong.pdf at main - GitHub</a></li>
<li><a href="https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81858/">基于具身智能加速即时物流机器人研发：从大语言动作模型训练到数字孪生验证 - NVIDIA</a></li>

</ul>
</details>

**标签**: `#AI`, `#embodied intelligence`, `#frontier technology`, `#education policy`, `#robotics`

---

<a id="item-17"></a>
## [剪映、即梦 AI 因 AI 内容标识不规范被处罚](https://www.cac.gov.cn/2026-04/28/c_1779119736411711.htm) ⭐️ 8.0/10

4 月 28 日，国家网信办通报对“剪映”“猫箱”App 及“即梦 AI”网站依法查处，因其未有效落实人工智能生成合成内容的标识规定。 此举表明中国正严肃推进生成式 AI 透明度监管，确保用户能清晰识别 AI 生成内容，对维护信息可信度、防止误导和强化平台责任具有重要意义。 涉事平台已被约谈、责令整改、警告，并对相关责任人从严处理；监管部门明确指出，不得以技术创新为由规避合规义务。

telegram · @zaihuapd · Apr 28, 09:29

**背景**: 中国《人工智能生成合成内容标识办法》自 2025 年 9 月起实施，要求对 AI 生成内容同时采用显式（可见）和隐式（机器可读）标识。该规定旨在保障公众利益、保护用户权益，并在生成式 AI 快速普及的背景下确保合成内容的可追溯性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://regulations.ai/regulations/RAI-CN-NA-CONTENT-2025">《人工智能生成合成内容标识办法》 - China | Regulations.AI - The ...</a></li>
<li><a href="https://www.chinalawandpractice.com/2025/04/30/measures-for-labeling-artificial-intelligence-generated-and-synthetic-content/">Measures for Labeling Synthetic Content Generated by Artificial Intelligence | chinalawandpractice.com</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#generative AI`, `#content moderation`, `#AI policy`, `#China tech`

---

<a id="item-18"></a>
## [LiteLLM Proxy 存在严重 SQL 注入漏洞](https://mp.weixin.qq.com/s/ytNWdqGECo0fmWwPQGqy8A) ⭐️ 8.0/10

LiteLLM 的 Proxy 组件被发现存在一个严重的预认证 SQL 注入漏洞（CVE-2026-42208），攻击者无需有效凭证即可通过错误日志提取存储的大模型 API 密钥。该问题已在 v1.83.7-stable 版本中修复。 该漏洞直接危及 AI 基础设施的安全，泄露 OpenAI、Anthropic 等主流大模型提供商的 API 密钥。由于 LiteLLM 被广泛用于统一调用大模型接口，暴露在外的实例可能导致未授权使用、数据泄露或费用滥用。 攻击者通过构造恶意 Bearer token 触发认证失败时的 SQL 查询，导致错误日志泄露数据库内容。建议用户升级至 v1.83.7-stable 并轮换所有已存储的 API 密钥，或通过设置 'disable_error_logs: true' 关闭错误日志。

telegram · @zaihuapd · Apr 28, 14:44

**背景**: LiteLLM 是一个开源库，提供统一接口以通过单一 API 调用不同厂商的大语言模型（LLM）。其 Proxy 组件支持请求路由、速率限制和密钥管理，常作为服务部署在 AI 工作流中。SQL 注入漏洞通常因用户输入未被正确过滤就用于数据库查询而产生，可能导致攻击者读取或篡改后端数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sysdig.com/blog/cve-2026-42208-targeted-sql-injection-against-litellms-authentication-path-discovered-36-hours-following-vulnerability-disclosure">CVE-2026-42208: Targeted SQL injection against LiteLLM's authentication path discovered 36 hours following vulnerability disclosure | Sysdig</a></li>
<li><a href="https://www.tenable.com/cve/CVE-2026-42208">CVE-2026-42208 | Tenable®</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#LLM Infrastructure`, `#SQL Injection`, `#API Keys`, `#Vulnerability Disclosure`

---

<a id="item-19"></a>
## [Warp 开源基于终端的智能开发环境](https://github.com/warpdotdev/warp) ⭐️ 8.0/10

Warp 已开源其客户端代码库，该终端开发环境集成了由 GPT、Claude、Codex 和 Gemini 驱动的 AI 编码代理。其 UI 框架采用 MIT 许可证，其余代码采用 AGPL v3 许可证。 此举让开发者能更广泛地使用 AI 增强型终端，通过智能命令建议、代码生成和工作流自动化大幅提升开发效率。随着越来越多开发者采用大语言模型工具，Warp 的开源模式鼓励社区贡献，并支持与多种 AI 后端的互操作。 客户端支持内置 AI 代理，并允许集成 Claude Code 和 Gemini CLI 等外部 CLI 模型。OpenAI 被列为创始赞助商，AI 代理在由 GPT 系列模型驱动的托管工作流系统中运行。

telegram · @zaihuapd · Apr 28, 17:04

**背景**: Warp 是一款现代化终端应用，旨在通过将 AI 能力直接集成到命令行界面来提升开发者工作流。与传统终端不同，Warp 将命令视为结构化块，并利用大语言模型辅助编码、调试和 Shell 交互。随着 GitHub Copilot 或 Cursor 等工具将大语言模型嵌入开发环境，AI 在软件工程中的应用正加速普及。

**标签**: `#AI coding assistant`, `#developer tools`, `#open source`, `#LLM integration`, `#frontier tech`

---

<a id="item-20"></a>
## [Git Pitcher 将 GitHub 仓库转换为 AI 智能体计划](https://www.producthunt.com/products/git-pitcher) ⭐️ 8.0/10

Git Pitcher 是一款新型开发者工具，可将任意 GitHub 仓库逆向工程为结构化的、适合 AI 智能体使用的计划。这使得智能体 AI 系统能够自动分析和执行代码库。 该工具弥合了现有代码库与新一代 AI 智能体之间的鸿沟，后者需要结构化计划才能有效运行。它加速了软件开发中的 AI 驱动自动化，并降低了在真实仓库上部署智能体工作流的门槛。 Git Pitcher 输出的计划符合现代智能体 AI 框架（如 NVIDIA 所述）所强调的推理与规划能力。该工具专为集成到 AI 智能体开发流水线而设计，而非供人类直接使用。

producthunt · K.M Fazle Rabbi · Apr 28, 02:34

**背景**: AI 智能体是能够推理、规划并执行以完成复杂任务的自主系统。要在软件项目上有效运行，它们通常需要代码库的结构化表示（如任务树、依赖图或执行路线图），而非原始源代码。像 Git Pitcher 这样的工具旨在从 GitHub 等平台上的现有仓库中自动生成这些表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/">AI Agents: Built to Reason, Plan, Act - NVIDIA</a></li>
<li><a href="https://www.anaplan.com/blog/what-makes-ai-agent-enterprise-ready-five-requirements-for-business/">What Makes an AI Agent Enterprise-Ready? 5 Requirements | Anaplan Blog</a></li>
<li><a href="https://www.airtable.com/articles/ai-readiness">AI Readiness: How to Get Your Organization Agent Ready - Airtable</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Developer Tools`, `#GitHub`, `#Automation`, `#AI Development`

---

<a id="item-21"></a>
## [伊格莱西亚斯更青睐专业 AI 软件而非 DIY“氛围编程”](https://simonwillison.net/2026/Apr/28/matthew-yglesias/#atom-everything) ⭐️ 7.0/10

马修·伊格莱西亚斯公开表示，他更倾向于由专业团队开发的 AI 增强型软件产品，而非使用 AI 工具进行 DIY 式的“氛围编程”。他在 2026 年 4 月的一条推文中表达了这一观点，并称这是在观察 AI 辅助开发趋势五个月后的结论。 这一观点凸显了关于 AI 在软件开发中角色的日益激烈的争论：AI 究竟应通过非正式编程赋能个人业余开发者，还是应增强专业工程工作流。它也强调了在 AI 编程工具日益普及的时代，人们对软件质量、安全性和可维护性的担忧。 伊格莱西亚斯明确拒绝“氛围编程”——这一术语由安德烈·卡帕西于 2025 年提出，指通过提示驱动、迭代生成代码且极少审查的 AI 编程方式——而支持由专业团队负责任地使用 AI 辅助开发的商业软件。他的立场与批评者一致，后者警告称，氛围编程因缺乏充分监督，可能引入漏洞和安全隐患。

rss · Simon Willison · Apr 28, 13:25

**背景**: “氛围编程”于 2025 年初兴起，当时 GitHub Copilot、Claude Code 等 AI 编程助手能力显著提升。该术语由 AI 研究员安德烈·卡帕西提出，描述了一种开发者依赖直觉和与大语言模型快速迭代、而非遵循严格软件工程实践的编程风格。该词被柯林斯词典评为 2025 年度词汇，反映了其文化影响力。与此同时，“智能体工程”（agentic engineering）指的是一种结构化方法——如西蒙·威利森所记录的那样——通过精心设计的提示和验证模式，引导 AI 智能体生成可靠且可维护的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://grokipedia.com/page/Vibe_coding">Vibe coding</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering_Patterns">Agentic Engineering Patterns</a></li>

</ul>
</details>

**标签**: `#ai-assisted-programming`, `#ai`, `#vibe-coding`, `#software-development`, `#agentic-engineering`

---

<a id="item-22"></a>
## [可回收火箭密集验证开启，商业航天迈向规模化量产元年](https://36kr.com/newsflashes/3787190594558981?f=rss) ⭐️ 7.0/10

4 月下旬，中国迎来可回收火箭密集验证窗口，长征十号乙、朱雀三号等多型火箭接连开展回收技术验证，同时国家《商业航天标准体系（1.0 版）》正式落地。 可回收火箭技术的工程化落地有望使发射成本指数级下降，推动低轨星座等大规模商业应用；配套标准体系的出台则为产业链投资提供政策确定性，加速全链条价值重估。 新一代四米级全液氧煤油可重复使用火箭长征十二号乙已计划于今年上半年首飞，专为满足低轨星座组网等商业发射需求而研制，凸显中国商业火箭研发的快速迭代能力。

rss · 36kr · Apr 29, 01:09

**背景**: 可回收火箭技术由 SpaceX 等公司率先实现，通过回收并重复使用助推器大幅降低入轨成本。近年来，中国航天科技集团（长征系列）和民营航天企业（如蓝箭航天的朱雀系列）加快了垂直起降回收技术研发。国家出台《商业航天标准体系》标志着政府正系统性引导产业从技术验证走向规模化商业运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chinese_space_program">Chinese space program - Wikipedia</a></li>
<li><a href="https://www.moomoo.com/news/post/66786333/update-on-china-s-commercial-space-launch-schedule-long-march">Update on China's Commercial Space Launch Schedule: Long March 12B to Make Maiden Flight in the First Half of the Year, Hyperbola-3 to Embark on Mission by Year-End - Moomoo</a></li>

</ul>
</details>

**标签**: `#commercial航天`, `#reusable rockets`, `#space technology`, `#frontier tech`, `#industrial policy`

---

<a id="item-23"></a>
## [AI 智能体难以应对遗留代码库](https://www.v2ex.com/t/1209273#reply0) ⭐️ 7.0/10

一位开发者质疑在拥有百万行以上代码、缺乏文档且依赖复杂的十年老系统上使用 AI 智能体的可行性。他们还批评当前 AI 生成的代码无视现有规范，重复造轮子。 这揭示了 AI 落地中的关键鸿沟：尽管 AI 在新项目中表现良好，但在企业普遍存在的遗留系统中却力不从心。误用可能导致技术债、集成故障和资源浪费。 所述遗留系统缺乏文档，依赖各种补丁、定时任务和临时脚本，必须通过实际调试才能理解其行为——在这种条件下，AI 智能体无法可靠运行，必须依赖大量人工审查和测试。

rss · V2EX · Apr 29, 01:52

**背景**: 软件工程中的 AI 智能体正越来越多地用于代码生成、缺陷修复和测试自动化，但它们通常假设代码结构清晰且有良好文档。而遗留系统往往历经数十年构建，使用过时技术栈并依赖团队内部知识，缺乏这些前提条件。Thoughtworks 和 Martin Fowler 等人近期推出的 CodeConcise 等工具尝试利用生成式 AI 进行现代化改造，但挑战依然巨大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackernoon.com/why-ai-struggles-with-legacy-code-and-institutional-knowledge">Why AI Struggles With Legacy Code and Institutional Knowledge - HackerNoon</a></li>
<li><a href="https://www.thoughtworks.com/en-us/insights/blog/legacy-modernization/legacy-modernization-in-the-age-of-ai">Legacy modernization in the age of AI | Thoughtworks United States</a></li>
<li><a href="https://martinfowler.com/articles/legacy-modernization-gen-ai.html">Legacy Modernization meets GenAI - Martin Fowler</a></li>

</ul>
</details>

**社区讨论**: 原帖反映了从业者的普遍疑虑：他们观察到 AI 在实际团队中被误用，尤其当开发者只追求速度而忽视可维护性，并在生成不符合规范的代码后准备离职跑路。

**标签**: `#AI Agents`, `#Legacy Code`, `#Software Engineering`, `#AI Limitations`, `#Code Generation`

---

<a id="item-24"></a>
## [AI Chrome 插件自动提取日程事件](https://www.v2ex.com/t/1209261#reply0) ⭐️ 7.0/10

一位开发者发布了名为 TimeLens-AI Calendar 的 Chrome 插件，利用 AI 从邮件或网页中提取日程信息，并通过 CalDAV 同步到系统日历。用户只需框选网页或邮件中的相关内容，插件即可解析并添加日程。 该工具通过实用型 AI 自动化解决了常见痛点——手动将邮件或网页中的活动添加到日历，提升了多端日历同步体验，可为重度日历用户节省时间。 插件会将截图上传至 AI 服务进行识别，但不会存储图片；仅保留解析后的日程数据用于 CalDAV 同步，且用户可随时删除。它兼容所有支持 CalDAV 的日历客户端，并为前 100 名测试用户提供终身免费权限。

rss · V2EX · Apr 29, 01:42

**背景**: CalDAV 是基于 WebDAV 的标准化协议，允许客户端跨设备和服务访问与同步日历数据。它被 Apple 日历、Thunderbird 及许多自建日历服务广泛支持，实现了不同平台间的互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mdn/translated-content/blob/main/files/zh-cn/glossary/caldav/index.md?plain=1">translated-content/files/zh-cn/glossary/caldav/index.md at main - GitHub</a></li>
<li><a href="https://wener.me/notes/service/storage/webdav">WebDAV - Wener Live & Life</a></li>

</ul>
</details>

**标签**: `#AI`, `#productivity tools`, `#Chrome extension`, `#calendar automation`, `#applied AI`

---

<a id="item-25"></a>
## [地平线余凯：拒绝内卷，以用户体验驱动“外卷”](https://www.ithome.com/0/944/786.htm) ⭐️ 7.0/10

在 2026 北京车展期间，地平线创始人余凯反对汽车行业“内卷”，提出通过 AI 驱动的用户体验创造价值，使原本 16 万元的车能以 19 万元售出，且用户心甘情愿买单。 这一观点挑战了中国汽车行业普遍存在的降价和同质化竞争趋势，将 AI 定位为创造用户价值的核心驱动力，有望打破“三输”困局，实现车企、供应商与消费者的多方共赢。 余凯强调，真正的价值来自真实的用户体验，而非“画中画电视”之类的噱头；地平线通过开放生态支持高度定制化，如同提供法餐或意餐，而非千篇一律的“麦当劳套餐”。

rss · IT HOME · Apr 29, 01:52

**背景**: 在中国汽车行业，“内卷”指企业间陷入无实质创新的恶性价格战，导致利润压缩、技术停滞。地平线机器人（Horizon Robotics）是中国领先的汽车 AI 芯片公司，专注于为高级驾驶辅助系统（ADAS）和自动驾驶提供芯片与解决方案，已与多家主流车企合作推动智能汽车发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.moomoo.com/news/post/68081773/passenger-car-association-in-march-retail-sales-in-the-national">Passenger Car Association: In March, retail sales in the national ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#automotive AI`, `#Horizon Robotics`, `#intelligent vehicles`, `#frontier tech`

---