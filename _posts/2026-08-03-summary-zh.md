---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> From 103 items, 7 important content pieces were selected

---

1. [国家超算互联网上线 DeepSeek-V4-Flash 正式版 API](#item-1) ⭐️ 9.0/10
2. [Karpathy 的 Pelican：LLM 从文本生成 3D 动画](#item-2) ⭐️ 8.0/10
3. [AI 行业公开信辩论开放权重模型监管政策](#item-3) ⭐️ 8.0/10
4. [传闻谷歌计划 2028 年部署 1200~1500 万颗 TPU v9 芯片以赶超 NVIDIA](#item-4) ⭐️ 8.0/10
5. [姚顺雨入腾讯 300 天、英伟达 RoboTTT 将机器人上下文扩至 8K、GitHub Agent 提示注入漏洞](#item-5) ⭐️ 8.0/10
6. [BestBlogs 第 106 期：20 篇 AI 精选文章推荐](#item-6) ⭐️ 8.0/10
7. [SkillSmith：通过前缀键值缓存教授冻结 LLM 新技能](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [国家超算互联网上线 DeepSeek-V4-Flash 正式版 API](https://aihot.virxact.com/items/cmscgyldf07c7roeumrvibjl7) ⭐️ 9.0/10

China's National Supercomputing Internet has officially launched the API for the new DeepSeek-V4-Flash model, boasting agentic capabilities and performance on par with top closed-source models.

rss · AI Hot · Aug 2, 23:23

**标签**: `#DeepSeek`, `#Large Language Models`, `#AI API`, `#Frontier AI`, `#Artificial Intelligence`

---

<a id="item-2"></a>
## [Karpathy 的 Pelican：LLM 从文本生成 3D 动画](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

Andrej Karpathy 展示了 LLM 直接从文本提示生成 3D 动画的能力，展现了模型将自然语言描述转化为功能性 3D 图形代码的能力。这个被称为「Pelican」的演示超越了静态图像生成，要求模型生成可执行代码来渲染动态空间场景。 这一演示突显了一种评估 LLM 空间推理和世界建模能力的新颖基准，这些能力是 AI 研究的关键前沿领域。通过要求模型理解物理关系并将其转化为代码，此类任务暴露了 AI 在真正理解物理世界方面与简单模式匹配之间的差距。 生成的 3D 动画目前质量较为粗糙，但其重点在于建立一种新的评估范式，而非产出精美的作品。该演示也引发了可重复性的问题，因为使用的具体提示词并未公开分享，而且此类基准将模型能力与围绕模型的工具框架混为一谈。

hackernews · delichon · Aug 2, 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: AI 中的空间推理是指模型感知、表示和操纵跨维度空间关系的能力。世界模型是构建物理环境内部表示并预测环境如何随时间变化的机器学习系统。包括 Yann LeCun 和李飞飞在内的顶尖 AI 研究者越来越关注世界模型作为实现更强 AI 的路径，李飞飞创立了 World Labs，LeCun 则成立了 AMI Labs 来构建理解物理世界的系统。现有的空间推理基准如 SpartQA 和 ScanQA 测试空间理解的特定方面，但从文本生成功能性 3D 动画代表了一种更全面且更具挑战性的测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/world-models-could-unlock-the-next-revolution-in-artificial-intelligence/">World models could unlock the next revolution in artificial intelligence | Scientific American</a></li>
<li><a href="https://www.emergentmind.com/topics/spatial-reasoning-benchmarks">Spatial Reasoning Benchmarks</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调，虽然输出质量较差，但真正的价值在于建立了一种暴露模型对物理世界理解程度的新基准。一些用户用不同输入复现了实验，例如从小说描述生成 3D 场景，而另一些人则因缺乏共享提示词而提出可重复性方面的担忧，并指出此类演示同时评估了模型及其工具框架，而非单独衡量原始模型能力。

**标签**: `#AI`, `#LLM`, `#Spatial Reasoning`, `#3D Generation`, `#World Models`

---

<a id="item-3"></a>
## [AI 行业公开信辩论开放权重模型监管政策](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

微软牵头并于 7 月 24 日发布了一封公开信，获得包括 NVIDIA、Amazon 和 OpenAI 在内的 235 家公司签署，主张保护开放权重模型并为其蒸馏技术的合法性辩护。Anthropic 拒绝签署该信并发布了自身的立场文件，而另一封由 1,324 名前沿 AI 公司员工签署的公开信则呼吁政府支持有意识地控制自动化 AI 开发的前进步伐。 这些相互竞争的公开信揭示了 AI 行业内部在模型可访问性未来方面的深刻分歧，各方在潜在监管行动前夕直接向美国政策制定者进行游说。这场辩论的结果将决定 AI 生态系统是由少数封闭的专有提供商主导，还是允许广泛的社区去检查、修改并基于强大的基础模型进行构建。 微软支持的公开信明确为蒸馏技术（即使用一个模型的输出来训练另一个模型）辩护，认为这是一种合法的模型开发手段而非盗用。相比之下，Anthropic 首席执行官 Dario Amodei 呼吁打击工业规模的蒸馏操作，并列举了网络攻击、生物攻击以及威权政府窃取 AI 能力的风险。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型是指其核心参数（权重和偏置）被公开发布的 AI 模型，允许任何人在本地下载、运行和微调。然而，它们与真正的开源 AI 有显著区别，因为它们通常不包含用于创建模型的原始训练数据或完整的源代码。美国政府目前正在辩论是否出于国家安全和安全考虑而限制这些模型，这引起了依赖开放权重来促进创新和竞争的公司的警觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://www.anthropic.com/news/position-open-weights-models">Our position on open-weights models \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Open Weights`, `#AI Governance`, `#Open Source`, `#Industry News`

---

<a id="item-4"></a>
## [传闻谷歌计划 2028 年部署 1200~1500 万颗 TPU v9 芯片以赶超 NVIDIA](https://aihot.virxact.com/items/cmscj3qvo09m5roeubelwf0wn) ⭐️ 8.0/10

台湾媒体援引一份市场分析报告称，谷歌计划在 2028 年部署 1200 万至 1500 万颗自研 TPU v9 AI ASIC 芯片，规模有望赶上甚至超过英伟达届时约 1240 万颗的 AI GPU 出货量。报告还指出，TPU v9 将采用 4 计算裸片的 chiplet 架构，大幅提升对先进制程和封装产能的需求。 这一大规模部署标志着 AI 硬件格局的重大转变，谷歌自身的算力规模将足以匹敌大多数 AI 公司所依赖的整个 NVIDIA GPU 生态系统。所需的庞大芯片数量也将迫使谷歌在台积电之外寻找代工产能，从而为英特尔代工和三星创造重大新商机，可能重塑半导体代工行业的格局。 TPU v9 预计将采用 4 计算裸片的 chiplet 设计，这种方案将处理器拆分为多个更小的裸片以提高良率和制造灵活性，但同时也大幅增加了对先进封装技术的需求。由于台积电的产能无法单独满足这一庞大需求，谷歌很可能需要将供应链分散到多家代工厂，此前谷歌向英特尔和三星下单 TPU 芯片的传闻也印证了这一策略。

rss · AI Hot · Aug 3, 00:50

**背景**: TPU（Tensor Processing Unit）是谷歌专门为机器学习工作负载设计的定制 ASIC 芯片，与通用 GPU 相比，在训练和推理方面都具有更高的效率。Chiplet 架构将大型单片芯片拆分为多个较小的功能裸片（如计算裸片和 I/O 裸片）并封装在一起，使制造商能够混合使用不同的制程节点并提高生产良率。虽然 NVIDIA 的 GPU 凭借成熟的软件生态系统主导着 AI 硬件市场，但谷歌、亚马逊和 Meta 等主要云服务提供商正越来越多地投资定制芯片，以降低成本、保障供应并加强对自身 AI 基础设施的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chiplet">Chiplet - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchitoperations/news/366642002/New-Google-TPUs-multiply-AI-infrastructure-efficiency">New Google TPUs multiply AI infrastructure efficiency | TechTarget</a></li>
<li><a href="https://hashrateindex.com/blog/what-is-an-ai-asic-guide-ai-chips/">What Is an AI ASIC ? The Complete Guide</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Google TPU`, `#AI Infrastructure`, `#Semiconductors`, `#Compute`

---

<a id="item-5"></a>
## [姚顺雨入腾讯 300 天、英伟达 RoboTTT 将机器人上下文扩至 8K、GitHub Agent 提示注入漏洞](https://aihot.virxact.com/items/cmscit1eq09dxroeur8qxq6js) ⭐️ 8.0/10

姚顺雨加入腾讯 300 天后，混元团队重新聚焦，微信 VLM 与混元将长期并存。英伟达与斯坦福联合提出了 RoboTTT，将机器人策略的上下文扩展至 8000 个时间步。此外，GitHub Agentic Workflows 中被披露存在名为'GitLost'的严重提示注入漏洞，攻击者只需在公开 Issue 中嵌入隐藏指令即可窃取私有仓库数据。 这些进展凸显了人工智能的三个关键前沿：大型科技公司重组其模型战略以获取竞争优势、机器人领域实现更长时序自主性的重大突破，以及 AI Agent 融入开发者基础设施后日益紧迫的安全风险。GitHub 的漏洞尤其令人警醒，因为利用该漏洞无需任何凭证或编程技能，暴露了 Agentic AI 系统如何成为攻击媒介。 RoboTTT 由来自 NVIDIA、斯坦福大学和德克萨斯大学奥斯汀分校的研究人员共同开发，知名学者李飞飞和林棨熹（Jim Fan）参与其中。GitHub 漏洞影响由 Claude、Copilot、Codex 或 Gemini 等 AI Agent 驱动的 Agentic Workflows，这些工作流使用 Markdown 而非手写 YAML 编写。以 AgentBench 评估框架闻名的姚顺雨，正在领导腾讯 AI 战略的重新聚焦。

rss · AI Hot · Aug 3, 00:15

**背景**: 腾讯混元是一套强调多模态能力和实际应用集成的旗舰 AI 模型系列，在 DeepSeek 等高性价比开源模型带来压力的市场中竞争。在机器人领域，目前大多数机器人基础模型仅在单步或短历史视觉运动上下文中运行，限制了其执行复杂长时序任务的能力；RoboTTT 通过扩展上下文长度来解决这一问题。提示注入是一类漏洞，恶意指令被嵌入 AI 模型处理的数据中，诱骗其执行非预期操作——当 Agent 拥有访问敏感工具或数据的权限时尤为危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/gear/robottt/">RoboTTT: Context Scaling for Robot Policies</a></li>
<li><a href="https://www.securityweek.com/critical-vulnerability-exposes-github-agentic-workflows-to-prompt-injection/">Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt ...</a></li>
<li><a href="https://mcp.directory/blog/gitlost-github-agent-security-2026">GitLost: GitHub Agent Prompt Injection — MCP.Directory</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Robotics`, `#AI Security`, `#Large Language Models`, `#Industry News`

---

<a id="item-6"></a>
## [BestBlogs 第 106 期：20 篇 AI 精选文章推荐](https://aihot.virxact.com/items/cmscgnvm8074oroeut4rwnhip) ⭐️ 8.0/10

BestBlogs 第 106 期精选了 20 篇 AI 文章，围绕 Jeff Dean 提出的「1%法则」展开——该法则认为，虽然模型能力正变得易于接近，但产品成败取决于规格、上下文、工具、记忆、评测与编排。本期亮点包括 GPT-5.6 Sol 推理优化使成本降低 20%、Kimi K3 精确规模达 2.78 万亿参数，以及 Gemini Robotics 2 的全身控制能力。 本期通讯精选了前沿 AI 领域最关键的发展动态，帮助工程师和研究人员在海量信息中高效获取高价值内容。精选话题覆盖了从大规模模型扩展、推理成本降低到具身智能的完整 AI 技术栈，反映了行业正从纯粹的能力构建向实际工程化和产品化转型的趋势。 Kimi K3 通过 latent-MoE（混合专家）架构实现了 2.78 万亿参数的规模，其精确参数量和激活数通过公开的张量形状计算得出，并可通过专家流式加载在仅 29GB 内存上运行。本期还涵盖了涉及 Claude Code、MCP（模型上下文协议）和基于 Skill 的开发实践等工程工作流。

rss · AI Hot · Aug 2, 23:06

**背景**: Jeff Dean 的「1%法则」认为，达到 AI 模型的基础能力相对容易，但产品成功的另外 99%取决于上下文管理、工具集成和评测流程等工程细节。MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 应用与外部数据源、工具和工作流的连接方式——常被比喻为「AI 应用的 USB-C 接口」。Gemini Robotics 2 由 Google DeepMind 开发，是一个视觉-语言-动作模型，能够使机器人推理并执行行走、蹲下和操作物体等动作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body... — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#AI Newsletter`, `#Frontier Models`, `#AI Engineering`, `#Robotics`, `#Inference Optimization`

---

<a id="item-7"></a>
## [SkillSmith：通过前缀键值缓存教授冻结 LLM 新技能](https://aihot.virxact.com/items/cmscacbvt026mroeutmzco995) ⭐️ 8.0/10

Google DeepMind 提出了 SkillSmith，一种将前缀键值缓存（KV cache）视为输入模态，为冻结的大型语言模型生成新技能的方法。通过前向传播，SkillSmith 在推理时为 Gemma 3 4B 等模型创建新的前缀 KV 缓存，无需任何重新训练或权重更新。 这种方法大幅降低了模型适应的成本和复杂性，因为可以在不进行昂贵的基于梯度的训练的情况下，为冻结模型添加新能力。它为高度模块化的 LLM 系统打开了大门，在该系统中技能可以在推理时动态组合和替换，推动了高效模型适应性的边界。 SkillSmith 通过单次前向传播而非反向传播来生成前缀 KV 缓存，使技能创建过程极其高效。该方法在冻结的 Gemma 3 4B 模型上进行了演示，将生成的 KV 缓存视为结构化前缀，以调节模型在特定下游任务上的行为。

rss · AI Hot · Aug 2, 20:38

**背景**: 在 LLM 推理过程中，键值缓存（KV cache）存储了之前处理过的 token 的中间注意力状态，使模型在生成后续 token 时能够避免冗余计算。前缀缓存是一种广为人知的优化技术，通过在多个请求之间重用共享提示前缀的 KV 缓存来降低延迟。传统上，将冻结的 LLM 适应到新任务依赖于软提示或适配器模块等技术，这些技术仍需要基于梯度的训练。SkillSmith 更进一步，仅通过前向传播就生成了这些前缀表示，完全消除了训练的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/design/prefix_caching/">Automatic Prefix Caching - vLLM</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/prefix-caching">Prefix caching | LLM Inference Handbook</a></li>

</ul>
</details>

**标签**: `#Google DeepMind`, `#LLM Inference`, `#Key-Value Cache`, `#AI Research`, `#Model Adaptation`

---