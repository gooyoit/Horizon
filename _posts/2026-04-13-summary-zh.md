---
layout: default
title: "Horizon Summary: 2026-04-13 (ZH)"
date: 2026-04-13
lang: zh
---

> From 76 items, 15 important content pieces were selected

---

1. [使用 MLX 在 macOS 上实现 Gemma 4 音频转录](#item-1) ⭐️ 9.0/10
2. [Anthropic 推出 Claude 托管代理 Beta 版](#item-2) ⭐️ 9.0/10
3. [智元机器人等在南通成立新机器人公司](#item-3) ⭐️ 8.0/10
4. [智谱 AI 港股盘中股价突破 1000 港元](#item-4) ⭐️ 8.0/10
5. [易加仿生完成天使轮融资，推进仿生飞行鸟产品化](#item-5) ⭐️ 8.0/10
6. [开发者发布基于 SNI 的 AI API 加速代理工具 eproxy](#item-6) ⭐️ 8.0/10
7. [招聘高级 AI 应用工程师开发企业级智能体](#item-7) ⭐️ 8.0/10
8. [开发者分享正在付费使用的 AI 编程工具](#item-8) ⭐️ 8.0/10
9. [微软称 AI 智能体将拓展而非侵蚀软件收入](#item-9) ⭐️ 8.0/10
10. [广汽发布融合千问大模型的星河智舱 ADiGO Intelligence](#item-10) ⭐️ 8.0/10
11. [小鹏发布面向“物理 AI 时代”的旗舰 SUV GX](#item-11) ⭐️ 8.0/10
12. [特斯拉车内摄像头新增驾驶员年龄估算功能](#item-12) ⭐️ 8.0/10
13. [苹果开发首款 AI 智能眼镜，与 Meta 竞争](#item-13) ⭐️ 8.0/10
14. [智谱 AI 的 GLM-Coding 平台出现登录和短信验证问题](#item-14) ⭐️ 7.0/10
15. [吉利银河星耀 7 定档 4 月 16 日预售，搭载 H3 智驾与 e-AWD 四驱](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [使用 MLX 在 macOS 上实现 Gemma 4 音频转录](https://simonwillison.net/2026/Apr/12/mlx-audio/#atom-everything) ⭐️ 9.0/10

Simon Willison 展示了一种使用 uv、MLX 和 mlx-vlm 在 macOS 上通过 Google 的 Gemma 4 E2B 模型本地转录音频文件的命令行方法。该方案成功处理了一个 14 秒的 WAV 文件，生成了基本准确的转录文本。 这表明像 Gemma 4 这样的前沿多模态 AI 模型可以在消费级 Apple 硬件上高效运行，无需依赖云端，从而实现私有、离线的语音转文本功能。它凸显了基于 Apple MLX 框架在 Mac 上进行本地 AI 推理的生态系统正在快速发展。 该方法通过 mlx-vlm 使用 10.28 GB 的 Gemma 4 E2B 模型，mlx-vlm 是一个支持在 Apple Silicon 上运行视觉-语言及音频-语言模型的库。转录命令指定了提示词、最大生成 token 数和温度参数，并完全在设备端通过 Python 3.13 和 uv 工具运行。

rss · Simon Willison · Apr 12, 23:57

**背景**: Gemma 4 是 Google 最新推出的轻量级开源 AI 模型系列，其中 E2B 版本专为边缘设备优化。MLX 是 Apple 专为 Apple Silicon 高效计算设计的机器学习框架。mlx-vlm 在 MLX 基础上扩展，支持能理解图像、音频、视频与文本的多模态模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-E2B">google/gemma-4-E2B · Hugging Face</a></li>
<li><a href="https://opensource.apple.com/projects/mlx/">Apple Open Source</a></li>
<li><a href="https://pypi.org/project/mlx-vlm/">mlx - vlm · PyPI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemma`, `#MLX`, `#audio transcription`, `#multimodal AI`

---

<a id="item-2"></a>
## [Anthropic 推出 Claude 托管代理 Beta 版](https://platform.claude.com/docs/en/managed-agents/overview) ⭐️ 9.0/10

Anthropic 正式推出 Claude 托管代理的公开测试版，这是一个全托管服务，支持自主执行编码、网页浏览和文件操作等复杂且长时间运行的任务。开发者无需自行构建代理循环或运行时基础设施即可部署 AI 代理。 该发布大幅降低了部署生产级 AI 代理的门槛，通过开箱即用的安全、可扩展且经过优化的基础设施，推动实际应用场景落地。此举使 Anthropic 在实用型自主 AI 系统领域处于领先地位。 该服务在安全的云端沙箱中运行，支持在任务执行过程中实时干预，并内置提示词缓存与性能优化功能。当前 API 限制为每分钟最多 60 次创建请求和 600 次读取请求；多代理协作与长期记忆功能尚处于研究预览阶段。

telegram · zaihuapd · Apr 12, 07:38

**背景**: AI 代理是围绕大语言模型（LLM）构建的自主系统，能够感知环境、规划行动、使用工具并记住过往交互，常被概括为：代理 = LLM + 记忆 + 规划 + 工具使用。要在生产环境中可靠运行此类代理，需处理沙箱隔离、状态管理和异步执行等复杂基础设施，而大多数开发者必须从零搭建。Anthropic 的托管代理将这一复杂性抽象为一个托管平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Managed_Agents">Claude Managed Agents</a></li>
<li><a href="https://intheworldofai.com/p/anthropic-claude-managed-agents">Claude Managed Agents : Anthropic's AI Worker Revolution</a></li>
<li><a href="https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems">What Is the AI Agent Loop? The Core Architecture Behind Autonomous AI Systems | developers</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Claude`, `#Anthropic`, `#Autonomous Systems`, `#AI Infrastructure`

---

<a id="item-3"></a>
## [智元机器人等在南通成立新机器人公司](https://36kr.com/newsflashes/3764629631959559?f=rss) ⭐️ 8.0/10

中天机器人（南通）有限公司近日成立，注册资本 2000 万元人民币，由中天科技、智元机器人关联公司智元创新（上海）科技股份有限公司及北京辉羲智能信息技术有限公司共同持股，专注于智能与工业机器人的研发、制造和销售。 此次合资整合了光纤通信龙头（中天科技）、人形机器人新锐（智元机器人）和具身智能芯片企业（辉羲智能），有望推动中国智能制造与 AI 机器人深度融合，标志着硬件、人工智能与工业自动化领域的协同加速。 公司法定代表人为谢书鸿，经营范围明确涵盖工业机器人制造与智能机器人研发。值得注意的是，股东辉羲智能正在推进 R1 具身智能芯片的量产（计划 2025 年交付），未来可能为该合资公司产品提供核心算力支持。

rss · 36kr · Apr 13, 02:19

**背景**: 智元机器人由前华为工程师彭志辉创立，专注人形机器人，近期开源了自研轻量化机器人中间件 AimRT，用于实时通信。辉羲智能由清华团队领衔，聚焦“具身智能”——即能与物理世界交互的 AI 系统，并围绕自研 R1 芯片构建全栈计算平台。中天科技是中国光纤与智能电网领域的重要企业，正拓展至机器人驱动的工业自动化领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zhiyuan-robot.com/article/188/detail/42.html">技术解读丨一文读懂智元机器人自研中间件AimRT-技术解读丨一文读懂智元机器人自研中间件AimRT</a></li>
<li><a href="https://rhino.auto/">辉羲智能 | 用创新计算平台服务智慧出行</a></li>
<li><a href="https://airoboticinfo.com/ai-robot-news/huixi-intelligence-embodied-ai-funding">辉羲智能获8亿融资：清华团队打造具身智能芯片大脑，智元机器人战略入...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI hardware`, `#industrial automation`, `#frontier tech`, `#smart manufacturing`

---

<a id="item-4"></a>
## [智谱 AI 港股盘中股价突破 1000 港元](https://36kr.com/newsflashes/3764629254013445?f=rss) ⭐️ 8.0/10

智谱 AI 在港交所的股价盘中突破 1000 港元，公司最新市值超过 4300 亿港元。 这一里程碑反映了市场对智谱 AI 大模型技术及其商业化前景的高度认可，也表明在全球 AI 竞争背景下，投资者对中国头部 AI 企业的热情持续升温。 尽管当前资本市场对 AI 公司的关注正从概念转向业绩，智谱 AI 仍凭借其 GLM 系列大模型（如 ChatGLM、CodeGeeX 和 CogView）及 Bigmodel.ai 模型即服务平台获得强劲估值支撑。

rss · 36kr · Apr 13, 02:18

**背景**: 智谱 AI 源自清华大学计算机系，专注于认知智能大模型研发，曾推出双语千亿级大模型 GLM-130B，并基于此构建了 ChatGLM 等产品。公司通过 Bigmodel.ai 平台提供“模型即服务”（MaaS），是中国生成式 AI 领域与 MiniMax、月之暗面等并列的头部企业之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.shujujiaoyi.com/news/156086.html">清华大学智能大模型智谱AI - 数据交易导航</a></li>
<li><a href="https://docs.feishu.cn/v/wiki/ZcIPwtqGWiFOL8kQtkfcUhRrnug/a2">智谱AI的大模型技术亮点</a></li>
<li><a href="https://www.tmtpost.com/7936085.html">即将上市的Kimi，会复刻MiniMax走势吗？ -钛媒体官方网站</a></li>

</ul>
</details>

**标签**: `#AI`, `#大模型`, `#智谱`, `#资本市场`, `#前沿科技`

---

<a id="item-5"></a>
## [易加仿生完成天使轮融资，推进仿生飞行鸟产品化](https://36kr.com/newsflashes/3764584480637446?f=rss) ⭐️ 8.0/10

专注于消费级仿生飞行鸟的中国初创公司“易加仿生”已完成天使轮融资。所筹资金将用于加速产品研发迭代、实现规模化量产，并拓展全球消费者市场。 此举标志着将前沿仿生机器人技术推向大众消费市场的重要一步，融合了 AI 驱动的自主性、扑翼空气动力学与消费级硬件。若成功，有望推动仿生无人机在娱乐、教育乃至监控等领域的广泛应用。 该公司聚焦国内全平台电商及海外市场，强调面向终端消费者的商业化路径，而非工业或军用场景。其技术可能采用轻量化材料、扑翼推进系统，并通过智能手机控制，类似于现有的扑翼无人机产品。

rss · 36kr · Apr 13, 01:33

**背景**: 仿生飞行鸟通过扑翼而非螺旋桨模拟真实鸟类飞行，具有噪音低、动作自然的特点。该领域融合了机器人学、空气动力学与仿生设计，早期如 Bionic Bird 等公司已验证其消费级可行性。近年来微型电机、电池能量密度和控制算法的进步，使此类设备逐步具备大规模商用条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bionicbird.com/">Bionic bird - Biomimetic drones</a></li>
<li><a href="https://chirpforbirds.com/nature-advocacy/biomimicry-and-birds/?srsltid=AfmBOor1k0HxVg9tymEvCMQt-CIiTjuUDKn0hpMqE5zUhXga2qn78iBc">Biomimicry and Birds - Chirp Nature Center</a></li>

</ul>
</details>

**标签**: `#robotics`, `#biomimicry`, `#frontier tech`, `#consumer hardware`, `#autonomous systems`

---

<a id="item-6"></a>
## [开发者发布基于 SNI 的 AI API 加速代理工具 eproxy](https://www.v2ex.com/t/1205415#reply0) ⭐️ 8.0/10

一位开发者发布了 eproxy，这是一个本地代理工具，通过注入服务器名称指示（SNI）信息，将流量经由 NNR 或 GoRelay 等端口级加速服务转发，从而无需修改系统 hosts 文件即可加速访问 sub2api 等远程 AI 模型 API。 该工具通过精准的流量路由，显著改善了用户在访问远端服务器上延迟敏感型 AI 模型时的体验。它解决了 AI 基础设施中的一个常见痛点：传统的全局域名重定向（通过 hosts 文件）无法满足针对特定端口的加速需求。 eproxy 在本地监听（例如 http://127.0.0.1:9718），并将请求转发至加速节点（如 8.8.8.8:12345），同时注入正确的 SNI（如 demo.test.com）。目前已知在 Windows 平台上系统代理模式会失效，但 TUN 模式可正常使用。

rss · V2EX · Apr 13, 02:21

**背景**: 服务器名称指示（SNI）是 TLS 协议的一个扩展，允许客户端在初始握手阶段指明要连接的主机名，使单个 IP 地址能托管多个 HTTPS 站点。支持 SNI 的代理可利用该信息在不解密的情况下路由加密流量。NNR 和 GoRelay 等服务提供网络中转（转发）功能，可降低国际连接的延迟，但通常需要精确配置 SNI 才能正确处理 HTTPS 端点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/miyurudassanayake/sni-injector">GitHub - miyurudassanayake/sni-injector: SNI Injecting tool ...</a></li>
<li><a href="https://blog.compass-security.com/2025/03/bypassing-web-filters-part-1-sni-spoofing/">Bypassing Web Filters Part 1: SNI Spoofing</a></li>
<li><a href="https://hostloc.com/thread-1281489-1-1.html">【已出】出 2 个便宜的性价比不错的转发(nnr,gorelay)-美国VPS综合讨论-全球主机交流论坛 - Powered by Discuz!</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#proxy tool`, `#network optimization`, `#LLM deployment`, `#developer tool`

---

<a id="item-7"></a>
## [招聘高级 AI 应用工程师开发企业级智能体](https://www.v2ex.com/t/1205414#reply0) ⭐️ 8.0/10

一则招聘信息正在寻找具备提示工程、大语言模型（包括 GPT-5.4、Claude 3.7 和 Gemini 2.5 Pro）经验，并能在 Coze、Dify 和 FastGPT 等低代码平台上部署企业级 AI 智能体的高级 AI 应用工程师。 该职位反映了业界对能够将前沿大语言模型能力与实际业务自动化相结合的工程师日益增长的需求，表明基于低代码平台的智能体工作流正加速进入企业主流应用。 候选人必须能独立在 Coze、Dify 或 FastGPT 上构建并上线生产级 AI 智能体，精通主流大模型的提示工程，并能在一周内理解陌生业务流程并绘制出可被 AI 提效的替代漏斗图。

rss · V2EX · Apr 13, 02:19

**背景**: AI 智能体是由大语言模型驱动的自主或半自主系统，可执行客户服务、数据处理或工作流自动化等任务。Coze、Dify 和 FastGPT 等低代码平台允许开发者和非技术人员通过可视化界面设计、测试和部署这些智能体，无需大量编码。这些工具通常集成了检索增强生成（RAG）、模型编排和可观测性功能，以支持企业级应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/coze-dev/coze-studio">GitHub - coze-dev/coze-studio: An AI agent development ...</a></li>
<li><a href="https://github.com/langgenius/dify">GitHub - langgenius/dify: Production-ready platform for agentic workflow development. · GitHub</a></li>
<li><a href="https://github.com/labring/FastGPT">GitHub - labring/FastGPT: FastGPT is a knowledge-based ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Large Language Models`, `#Prompt Engineering`, `#Low-Code AI`, `#Enterprise AI`

---

<a id="item-8"></a>
## [开发者分享正在付费使用的 AI 编程工具](https://www.v2ex.com/t/1205409#reply1) ⭐️ 8.0/10

一位 V2EX 用户发起了一项投票，询问开发者目前正在为哪些 AI 编程助手付费，包括 Claude Code、GitHub Copilot、Cursor 和 Windsurf。该投票使用 TapTo.Vote 平台收集用户对这些工具的付费使用情况。 了解开发者愿意为哪些 AI 编程工具付费，可以揭示市场采用趋势以及这些工具在实际软件工程工作流中的价值认知。这一洞察有助于塑造 AI 辅助开发的未来，并为用户和厂商提供竞争格局的参考。 该投票特别关注*付费*使用情况，不包括免费版本，并涵盖了 Windsurf 等新兴工具以及 GitHub Copilot 等成熟产品。投票还推广了发帖人开发的多语言投票平台 tapto.vote。

rss · V2EX · Apr 13, 02:10

**背景**: GitHub Copilot（微软出品）和 Claude Code（Anthropic 出品）等 AI 编程助手利用大语言模型来建议或生成代码、运行终端命令并浏览代码库。Cursor 和 Windsurf 是原生支持 AI 的集成开发环境（IDE），具备类似智能体的功能，可进行多文件编辑并理解上下文。这些工具旨在通过减少样板代码和自动化常规任务来提升开发者效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://windsurf.com/">Windsurf - The best AI for Coding</a></li>
<li><a href="https://tapvoter.com/">TapVoter - Free Elections, Polls, Quizzes & Surveys</a></li>

</ul>
</details>

**标签**: `#AI`, `#developer-tools`, `#coding-assistants`, `#Claude`, `#GitHub-Copilot`

---

<a id="item-9"></a>
## [微软称 AI 智能体将拓展而非侵蚀软件收入](https://www.ithome.com/0/938/426.htm) ⭐️ 8.0/10

微软高管拉杰什·贾提出，AI 智能体将作为独立用户需要自己的软件许可证，不仅不会减少企业软件收入，反而可能带来增长。他指出每个 AI 智能体都可视为 SaaS 许可模式中的一个“席位”，数量甚至可能超过人类员工。 这一观点挑战了普遍担忧——即 AI 自动化会通过取代人类用户而减少软件许可需求。若该模式被行业广泛采纳，将重塑 SaaS 的变现方式，并在 AI 时代显著提升企业软件厂商的收入。 贾举例说明：一家原本为 20 名员工购买 20 个 Microsoft 365 许可证的公司，未来可能缩减至 10 名员工但配备 50 个 AI 智能体，仍需 50 个许可证。其核心前提是智能体具备独立执行能力，因此应单独计费。

rss · IT HOME · Apr 13, 02:18

**背景**: 企业级 SaaS（软件即服务）平台如 Microsoft 365、Salesforce 和 Workday 传统上采用“按席位付费”模式，即根据用户数量收费。随着企业开始部署 AI 智能体——能够自主执行日程安排、数据分析或客户服务等任务的程序——人们开始争论：这些智能体应被视为人类用户的延伸，还是应作为独立实体单独授权？这一争论涉及软件定价、身份管理以及数字劳动力本质等核心问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnblockchain.cn/index.php/article/24808">软件价值万亿大重组 | 登链社区 | 区块链技术社区</a></li>
<li><a href="https://support.huaweicloud.com/usermanual-marketplace/zh-cn_topic_0000002079770885.html">创建 SaaS 按 需规格和添加 按 需套餐包操作指导_发布 SaaS ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#enterprise AI`, `#SaaS`, `#Microsoft`, `#AI business models`

---

<a id="item-10"></a>
## [广汽发布融合千问大模型的星河智舱 ADiGO Intelligence](https://www.ithome.com/0/938/401.htm) ⭐️ 8.0/10

广汽在 2026 广汽科技日上发布了星河智舱 ADiGO Intelligence 端云一体架构，深度融合阿里千问大模型，具备多模态感知、基于记忆的多智能体协同和情感表达等能力。 此举将前沿大语言模型深度应用于智能座舱，推动人车交互向更自然、主动和个性化的方向演进，有望为智能汽车时代的座舱体验树立新标杆。 该系统基于超 375 万辆车的真实运行数据，多模态端到端响应延迟低于 1.6 秒，可同时协同 15 个 AI 技能（如路线规划、餐厅取号、停车预约）实现“一次指令、全部搞定”，并支持上传照片生成专属“AI 萌宠”，同时接入阿里“吃住行游乐购”全生态服务。

rss · IT HOME · Apr 13, 01:29

**背景**: ADiGO 是广汽集团长期发展的智能网联汽车平台。将千问等大语言模型融入汽车系统，反映了行业趋势：汽车正从交通工具演变为 AI 驱动的个人助理。多模态 AI 融合视觉、语音与场景数据以理解用户意图，而长时记忆增强架构则支持跨会话的上下文感知交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/938/401.htm">广汽发布星河智舱 ADiGO Intelligence ...</a></li>
<li><a href="https://www.donews.com/news/detail/7/6508500.html">2026...</a></li>

</ul>
</details>

**标签**: `#AI models`, `#smart cabin`, `#multimodal AI`, `#automotive AI`, `#large language models`

---

<a id="item-11"></a>
## [小鹏发布面向“物理 AI 时代”的旗舰 SUV GX](https://www.ithome.com/0/938/399.htm) ⭐️ 8.0/10

小鹏汽车宣布将于 4 月 15 日举办技术发布会，推出全新旗舰大六座 SUV GX。该车在安全、底盘、智驾和空间四大领域深度融合 AI 技术，并提供纯电（BEV）和增程（EREV）两种动力版本。 GX 将“物理 AI”——即与物理世界交互的人工智能——深度应用于量产车型，标志着具身智能在汽车领域的关键落地。其搭载的 L4 级线控转向系统首次在 50 万元以内车型量产，有望推动高阶自动驾驶硬件的普及。 GX 车身尺寸为 5265/1999/1800 毫米，轴距 3115 毫米，全球首发博世新一代线控转向系统，原生支持 L4 级自动驾驶并集成超 100 项功能。纯电版 CLTC 续航达 750 公里，增程版纯电续航 320 公里，全系标配双电机四驱。

rss · IT HOME · Apr 13, 01:26

**背景**: “物理 AI”指能在物理世界中运行并与之交互的人工智能系统，如机器人或自动驾驶汽车，而非仅存在于数字环境中的软件。在汽车领域，这包括感知、决策和执行一体化的 AI 系统，使车辆能在真实环境中感知、推理并行动。线控系统（如线控转向）取消了方向盘与车轮之间的机械连接，通过电信号控制转向，为软件定义汽车动态性能和高阶自动驾驶奠定基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/physical-ai">What is physical AI? - IBM</a></li>
<li><a href="https://carnewschina.com/2026/03/19/xpeng-gx-begins-global-mass-production-featuring-bosch-next-generation-steer-by-wire-system/">XPeng GX begins global mass production featuring Bosch next ...</a></li>
<li><a href="https://www.bosch-mobility.com/en/solutions/steering/steer-by-wire/">Steer-by-wire - Bosch Mobility</a></li>

</ul>
</details>

**标签**: `#Physical AI`, `#Autonomous Driving`, `#Smart Vehicles`, `#AI Integration`, `#New Energy Vehicles`

---

<a id="item-12"></a>
## [特斯拉车内摄像头新增驾驶员年龄估算功能](https://x.com/greentheonly/status/2042490378067013665) ⭐️ 8.0/10

特斯拉在 2026.8.6 版本软件更新中，通过后视镜上方的车内摄像头引入了本地化面部分析功能，用于估算驾驶员年龄。该功能默认在车端处理图像数据，仅在用户授权且发生安全关键事件时才会向特斯拉共享数据。 该功能可通过基于驾驶员年龄限制对完全自动驾驶（FSD）等高级功能的访问来提升安全性，并支持未来无人驾驶出租车场景中的乘员身份验证。这也体现了特斯拉在边缘 AI 领域的持续投入，以实现注重隐私的实时驾驶员监控。 该年龄估算功能目前尚未向用户开放，似乎主要用于内部的驾驶员监控和访问控制。特斯拉强调在设备端处理数据以保护隐私，这与其减少对云端依赖、处理敏感数据的整体策略一致。

telegram · zaihuapd · Apr 12, 04:04

**背景**: 特斯拉长期以来利用车内摄像头进行驾驶员监控，尤其是在启用 Autopilot 或 FSD 时，以确保驾驶员保持注意力。设备端 AI 处理可在不将原始视频上传至云端的情况下实现实时分析，在保障隐私的同时支持快速响应的安全系统。通过面部分析估算年龄是计算机视觉中的常见任务，广泛应用于零售、医疗和安防领域，但在汽车场景中用于功能访问控制尚属新颖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/04/09/tesla-cracks-down-fsd-hack-devices-remotely-disables-access/">Tesla cracks down on FSD hacking devices, remotely shuts down ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666389925000236">AI-assisted facial analysis in healthcare: From disease ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#computer vision`, `#autonomous vehicles`, `#edge AI`, `#driver monitoring`

---

<a id="item-13"></a>
## [苹果开发首款 AI 智能眼镜，与 Meta 竞争](https://www.bloomberg.com/news/newsletters/2026-04-12/apple-ai-smart-glasses-features-styles-colors-cameras-giannandrea-leaving-mnvtz4yg) ⭐️ 8.0/10

苹果正在开发其首款集成 AI 的智能眼镜（代号 N50），配备多种镜框款式、独特的垂直椭圆形相机系统，并深度整合 Apple Intelligence 和 Siri。该产品计划于 2027 年发布，支持拍摄照片和视频、免提交互，并通过计算机视觉实现环境感知。 此举标志着苹果正式进军 AI 可穿戴设备市场，直接挑战 Meta 的 Ray-Ban 智能眼镜，并预示着向无屏、环境式计算的转变，由端侧 AI 驱动。这也把 Apple Intelligence 生态从手机和电脑扩展到日常佩戴设备中。 眼镜将提供至少四种高端醋酸纤维镜框款式，包括类似 Ray-Ban Wayfarer 和库克常戴的纤薄矩形设计，颜色有黑色、海洋蓝和浅棕色等。虽无显示屏，但通过计算机视觉为 Siri 和 Apple Intelligence 提供上下文数据，并与 iOS 27 同步以编辑和分享媒体内容。

telegram · zaihuapd · Apr 13, 01:32

**背景**: Apple Intelligence 是苹果于 2024 年 6 月推出的生成式人工智能系统，已集成到 iOS 18、iPadOS 18 和 macOS Sequoia 中，结合设备端与云端处理，支持写作辅助、图像生成、通知摘要及 ChatGPT 集成等功能。可穿戴设备中的计算机视觉能实时理解环境，对辅助技术和情境感知型 AI 交互至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.computer.org/publications/tech-news/community-voices/ai-powered-wearables-assistive-technology">How AI-Powered Wearables Are Redefining Assistive Technology</a></li>

</ul>
</details>

**标签**: `#AI wearables`, `#smart glasses`, `#Apple Intelligence`, `#computer vision`, `#frontier tech`

---

<a id="item-14"></a>
## [智谱 AI 的 GLM-Coding 平台出现登录和短信验证问题](https://www.v2ex.com/t/1205418#reply0) ⭐️ 7.0/10

有用户报告在尝试登录智谱 AI 的 GLM-Coding 平台时无法收到短信验证码，并反复遇到“系统未知错误”的提示。该问题导致用户无法访问托管在 bigmodel.cn/glm-coding 上的编程助手服务。 该问题影响开发者使用这家中国领先 AI 公司提供的核心 AI 编程工具，可能中断开发工作流并影响平台可靠性。随着智谱 AI 围绕 GLM 模型家族扩展其企业级服务，稳定的服务可用性对用户信任至关重要。 错误信息明确显示“获取验证码失败，请重试”和“系统未知错误”。该问题似乎源于服务器或短信网关端，而非用户输入或设备设置问题。

rss · V2EX · Apr 13, 02:26

**背景**: 智谱 AI 是一家知名的中国人工智能公司，以其 GLM（通用语言模型）系列而闻名，包括 GLM-4 和更新的 GLM-5.1。GLM-Coding 是其针对编程任务微调的专用模型版本，通过 BigModel 平台（bigmodel.cn）提供。该平台提供免费套餐（如 GLM-4.5-Flash），并集成了编程、智能体和推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chozan.co/zhipu-ai/">Zhipu AI Explained: GLM Capabilities, Use Cases, and Risks - ChoZan</a></li>
<li><a href="https://bigmodel.cn/">Zhipu ai open platform</a></li>
<li><a href="https://vibecoding.app/blog/zhipu-ai-glm-pricing-2026">Zhipu AI GLM Pricing (2026): Plans, API Costs & Free</a></li>

</ul>
</details>

**标签**: `#AI`, `#Zhipu AI`, `#GLM`, `#coding assistant`, `#technical issue`

---

<a id="item-15"></a>
## [吉利银河星耀 7 定档 4 月 16 日预售，搭载 H3 智驾与 e-AWD 四驱](https://www.ithome.com/0/938/403.htm) ⭐️ 7.0/10

吉利宣布银河星耀 7 将于 4 月 16 日开启预售，新车搭载千里浩瀚 H3 智能驾驶辅助系统和 e-AWD 智电四驱系统。 此次发布凸显吉利将 AI 驱动的智能驾驶与高效电驱系统融入主流电动车的战略，有望推动智能出行功能在平价车型中的普及。 星耀 7 车身尺寸为 4958×1915×1505mm，轴距 2852mm，综合功率 312 千瓦，峰值扭矩 526 牛·米，零百加速 5.4 秒；配备 26 个高感知传感器和算力超 20 万 DMIPS 的芯片，支持高速 NOA 领航辅助和全场景自动泊车。

rss · IT HOME · Apr 13, 01:37

**背景**: 千里浩瀚 H3 是吉利五级智驾体系（H1 至 H9）中的中级方案，支持高速和城市通勤 NOA 功能。e-AWD 智电四驱系统通过后驱模块（RDM）、电控限滑差速器（eLSD）等组件实现扭矩智能分配，通常采用 Haldex 湿式多片离合器结构，在保证响应速度的同时降低能耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/千里浩瀚H3智驾系统/66240533">千里浩瀚H3智驾系统 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/eAWD/2755880">eAWD_百度百科</a></li>
<li><a href="https://chejiahao.autohome.com.cn/info/25098546">e-AWD智电四驱+全场景爆胎稳行，星耀7让驾控与安全兼得</a></li>

</ul>
</details>

**标签**: `#AI in automotive`, `#autonomous driving`, `#electric vehicles`, `#intelligent mobility`, `#ADAS`

---