---
layout: default
title: "Horizon Summary: 2026-06-24 (ZH)"
date: 2026-06-24
lang: zh
---

> From 111 items, 12 important content pieces were selected

---

1. [智谱 GLM-5.2 击败 DeepSeek，登顶全球最佳开源模型](#item-1) ⭐️ 9.0/10
2. [百度发布 Unlimited OCR，实现恒定内存的长文档解析](#item-2) ⭐️ 8.0/10
3. [热力学智能度量：量化罕见有效未来的概率提升](#item-3) ⭐️ 8.0/10
4. [字节跳动推出豆包专业版，具备智能体办公能力，最高 500 元/月](#item-4) ⭐️ 8.0/10
5. [Codex Remote 工程实践指南](#item-5) ⭐️ 8.0/10
6. [hf-claude 扩展与 GLM 5.2 展现出良好兼容性](#item-6) ⭐️ 8.0/10
7. [研究揭示大语言模型难以识别对抗性前缀攻击](#item-7) ⭐️ 8.0/10
8. [特朗普签署行政令：开发首台开启科学发现新时代的量子计算机](#item-8) ⭐️ 8.0/10
9. [火山引擎发布豆包音频生成模型 1.0，支持多模态参考生成](#item-9) ⭐️ 8.0/10
10. [消息称台积电先进制程代工将全线涨价，涵盖 7nm 及以下所有节点](#item-10) ⭐️ 8.0/10
11. [法律科技公司因 Anthropic 模型访问被封锁起诉美国政府](#item-11) ⭐️ 8.0/10
12. [中国“灵晟”超算登顶 TOP500，时隔八年重回世界第一](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [智谱 GLM-5.2 击败 DeepSeek，登顶全球最佳开源模型](https://aihot.virxact.com/items/cmqreza760jfcslp5uly016sm) ⭐️ 9.0/10

智谱 AI 的 GLM-5.2 模型据报已击败 DeepSeek，成为全球公认的最佳开源模型，在多项基准测试中整体表现领先。智谱团队首次现身硅谷 AI Engineer World's Fair 大会，将分享最新工作进展。 这标志着开源大模型格局的重大转变，一家中国 AI 实验室超越 DeepSeek——后者本身也是近期的开源领军者——夺得了前沿模型的桂冠。这表明开源 AI 领域的竞争正在加剧，同时也反映出智谱 AI 等中国 AI 公司的全球影响力日益增长，智谱 AI 已于今年早些时候在港交所上市。 据报道，GLM-5.2 在多项基准测试中整体表现领先，但公告中尚未披露具体的基准测试分数。该消息最初由 AI 工程领域的知名人物 swyx 通过社交媒体发布，时间在智谱于 AI Engineer World's Fair 大会演讲之前。

rss · AI Hot · Jun 24, 01:47

**背景**: GLM（General Language Model，通用语言模型）是智谱 AI 开发的预训练框架，结合了自编码器和自回归模型的优势，采用一种称为自回归空白填充的技术。GLM 家族已经历多代演进，从 GLM-130B 到 GLM-4 系列，模型针对中英文任务进行了优化。DeepSeek 是另一家中国 AI 公司，近期因其采用 MIT 许可证的开源权重模型在编程和推理基准测试中表现突出而声名鹊起。AI Engineer World's Fair 是全球最大的技术 AI 会议，汇聚了超过 6000 名 AI 工程师、创始人和高管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2406.12793v1">ChatGLM: A Family of Large Language Models from GLM -130B to...</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.ai.engineer/worldsfair/2026">AI Engineer World's Fair 2026: June 29 - July 2, San Francisco</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Source AI`, `#Zhipu AI`, `#GLM`, `#Frontier Models`

---

<a id="item-2"></a>
## [百度发布 Unlimited OCR，实现恒定内存的长文档解析](https://github.com/baidu/Unlimited-OCR) ⭐️ 8.0/10

百度开源了名为“Unlimited OCR”的 AI 系统，该系统采用新颖的架构方法，实现了对无限长度文档的恒定内存、长周期解析。该系统基于 Deepseek-OCR 和 PaddleOCR 等现有模型构建，其研究论文现已在 arXiv 上发布。 这一发展通过防止 KV 缓存的线性增长，解决了一个重大的推理瓶颈，传统上这种线性增长会导致模型在处理大型文档时耗尽 VRAM 或崩溃。它消除了开发者编写复杂代码手动切分长文档的需要，从而简化了对整本书等大量文本的处理流程。 其核心创新在于一种恒定内存的 KV 缓存技术，无论输入序列的长度如何，都能限制 GPU 的内存使用量，从而避免了传统的 O(N) 内存增长。该项目名称“Unlimited OCR Works”引用了动漫《Fate/stay night》中的“无限剑制”魔法，象征着该系统复制和处理文本的能力。

hackernews · ingve · Jun 23, 11:35 · [社区讨论](https://news.ycombinator.com/item?id=48643426)

**背景**: 在基于 Transformer 的 AI 模型中，KV（键值对）缓存是一种短期记忆机制，用于存储先前处理过的 token 以加速推理。然而，该缓存的大小会随着输入上下文长度的增加而线性增长，这意味着处理超长文档需要海量的 GPU 内存（VRAM）。为了避免内存溢出导致崩溃，开发者通常不得不将长文档分割成较小的块，这增加了工程上的复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/baidu/Unlimited-OCR">Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. - GitHub</a></li>
<li><a href="https://arxiv.org/html/2606.23050v1">Unlimited OCR Works Welcome the Era of One-shot Long-horizon Parsing - arXiv</a></li>
<li><a href="https://api.emergentmind.com/topics/constant-memory-kv-cache">Constant-Memory KV Cache Methods - api.emergentmind.com</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了该项目绕过 VRAM 限制的巧妙架构技巧，并赞赏了团队对 Deepseek-OCR 和 PaddleOCR 的真诚致谢。评论者还注意到了该项目受动漫启发的命名惯例，并讨论了其在光学乐谱识别等全新领域的潜在应用，例如对扫描的乐谱进行变调处理。

**标签**: `#AI`, `#OCR`, `#KV Cache`, `#Open Source`, `#Inference`

---

<a id="item-3"></a>
## [热力学智能度量：量化罕见有效未来的概率提升](https://aihot.virxact.com/items/cmqreyafm0jf2slp55sy0a5tm) ⭐️ 8.0/10

一篇新论文提出了“热力学智能”度量，将智能定义为系统利用信息和控制能力来显著提高罕见但有效未来发生概率的能力。作者引入了一种名为“罕见有效概率提升”的可计算指标，用于量化此类结果相较于被动基线出现的概率增长倍数。 该框架为评估 AI 系统提供了一种与底层实现无关的新范式，超越了传统上往往无法全面衡量泛化能力的任务成功率基准。通过将智能建立在基础物理学和概率论之上，它提供了一个通用的衡量尺度，可能会从根本上改变我们评估通用人工智能（AGI）进展的方式。 其核心前提是，智能系统必须对世界及其自身在世界中的位置进行建模，从而主动改变未来的概率分布。该度量指标评估系统在多大程度上能够有效识别并放大那些在被动行为下极其罕见、但在领域约束下仍然可行的结果。

rss · AI Hot · Jun 24, 01:32

**背景**: 当前的 AI 评估通常依赖于特定任务的成功率，这种衡量方式可能较为狭隘，无法充分体现智能底层的通用性。这种新方法与自由能原理和主动推断等概念相联系，在这些理论中，系统通过主动塑造环境来最小化意外。通过将智能构建为概率转移的热力学过程，该论文认为智能是一种物理现象，而不仅仅是人类设计的测试分数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.20231">[2606.20231] Thermodynamic Measure of Intelligence - arXiv.org</a></li>
<li><a href="https://www.emergentmind.com/papers/2606.20231">Thermodynamic Measure of Intelligence - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#AI Evaluation`, `#Thermodynamic Intelligence`, `#AGI Theory`, `#AI Research`, `#Intelligence Measurement`

---

<a id="item-4"></a>
## [字节跳动推出豆包专业版，具备智能体办公能力，最高 500 元/月](https://aihot.virxact.com/items/cmqre8txb0j5jslp522cv2z18) ⭐️ 8.0/10

字节跳动正式发布豆包专业版，该高级 AI 助手由豆包 2.1 Pro 模型驱动，新增了智能体“办公任务模式”，可自主操作本地电脑、浏览器及内置 Office 工具来完成复杂工作流。服务分为三档定价：标准套餐 68 元/月、加强套餐 200 元/月、高级套餐 500 元/月，认证大学生可享受 38 元/月的专属折扣价。 此次发布标志着智能体 AI 商业化的重大进展，将 AI 助手从对话式界面转变为能够执行数据分析、应用部署和流程自动化等多步骤专业任务的自主智能体。这也表明字节跳动正积极推动其大语言模型在竞争激烈的中国 AI 市场中实现商业化，直接挑战其他科技巨头的高级产品。 办公任务模式允许 AI 理解工作目标、自主拆解任务，并利用本地文件、浏览器和定时触发器来执行，包括创建和部署带有后端数据库的生产级 Web 应用（该功能目前处于灰度测试阶段）。免费用户将继续获得新模型更新，并可体验由豆包 2.1 Turbo 驱动的办公任务模式基础版，而专业版则解锁豆包 2.1 Pro 的全部能力，并享有大幅提升的使用额度。

rss · AI Hot · Jun 24, 01:12

**背景**: 智能体 AI（Agentic AI）代表了一个新前沿，AI 模型不再局限于生成文本，而是能够通过与软件工具和环境的交互来自主执行复杂任务。字节跳动的豆包 2.1 系列近期在火山引擎平台上线，是一组大语言模型，据报道其旗舰版 Pro 在编程基准测试中可媲美 Anthropic 的 Claude Opus，同时大幅降低了推理成本。此次发布中提到的“Skills（技能）”能力是指一种模块化机制，允许大语言模型动态加载特定指令和脚本来执行专业任务，使 AI 从“只会回答问题”进化为“能够完成任务”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/29080">ByteDance DouBao Launches Seed 2.1 Series: Three Indicators ...</a></li>
<li><a href="https://finance.biggo.com/news/40592da6-4c8e-44f8-ae6e-e0d46f180ef6">ByteDance Unveils Doubao 2.1: Coding Rivals Claude Opus ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2012180283743568745">AI Agent Skills 系统性技术指南：从入门到生产落地 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Large Language Models`, `#ByteDance`, `#Doubao`, `#AI Product Launch`

---

<a id="item-5"></a>
## [Codex Remote 工程实践指南](https://aihot.virxact.com/items/cmqrdrxyt0j06slp52dt4xnt0) ⭐️ 8.0/10

A comprehensive engineering guide on OpenAI's Codex Remote, outlining ten high-leverage capabilities, key commands, and five typical workflows for using mobile devices as a control plane to manage asynchronous AI coding agents.

rss · AI Hot · Jun 24, 01:01

**标签**: `#AI Coding Agents`, `#OpenAI Codex`, `#Software Engineering`, `#Human-AI Collaboration`, `#Developer Tools`

---

<a id="item-6"></a>
## [hf-claude 扩展与 GLM 5.2 展现出良好兼容性](https://aihot.virxact.com/items/cmqrdysck0j3gslp5ysw2zwjk) ⭐️ 8.0/10

近期更新确认，hf-claude 扩展现已与智谱 AI（现更名为 Z.AI）最新发布的 GLM 5.2 模型实现了无缝兼容。用户可以通过 hf CLI 安装 hf-claude 扩展，利用由 GLM 5.2 驱动的 Hugging Face Inference Providers 来启动 Claude Code。 这一兼容性使开发者能够将 GLM 5.2 —— 据报道在某些设计基准测试中已超越 GPT 5.5 等闭源模型 —— 作为 Claude Code 工作流的后端。它凸显了开源权重模型与主流 AI 开发工具之间日益增强的互操作性，为开发者在选择推理提供商时提供了更大的灵活性。 hf-claude 扩展通过 hf CLI 安装，允许用户从多种 Hugging Face Inference Providers 中进行选择以运行 Claude Code。GLM 5.2 是 GLM（通用语言模型）系列的最新一代产品，专为高级推理和编程任务设计，同时也可通过 Cloudflare Workers AI 获取。

rss · AI Hot · Jun 24, 00:49

**背景**: hf-claude 扩展是一个连接 Hugging Face 生态系统与 Anthropic Claude Code 的工具，使开发者能够利用 Hugging Face 的推理基础设施。GLM 5.2 由 Z.AI（前身为智谱 AI）发布，该公司是位于北京的前沿 AI 研究实验室，而 GLM 5.2 是其迄今为止最强大的模型。该模型因在设计领域的 AI 评估排行榜上击败主要闭源竞争对手而备受关注。Hugging Face Inference Providers 则提供了统一的 API 来访问各种开源和开放权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/hf-claude/blob/main/README.md">hf-claude/README.md at main · huggingface/hf-claude · GitHub</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-glm-5-2-open-weight-model">What Is GLM 5.2? The Open-Weight Model Beating GPT 5.5 on Design Benchmarks | MindStudio</a></li>
<li><a href="https://aimlapi.com/blog/glm-5-2-zhipu-ais-most-capable-model-yet">GLM 5.2: Zhipu AI's Most Capable Model Yet — AI/ML API Blog</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#GLM`, `#Zhipu AI`, `#AI Tools`, `#Open Source AI`

---

<a id="item-7"></a>
## [研究揭示大语言模型难以识别对抗性前缀攻击](https://aihot.virxact.com/items/cmqrbqir10igcslp5ihba9orn) ⭐️ 8.0/10

Research on 10 open-source LLMs reveals they cannot reliably detect when their outputs have been manipulated by adversarial prefix attacks, mistakenly accepting 27.3% of hijacked responses as their own intentions.

rss · AI Hot · Jun 24, 00:12

**标签**: `#AI Safety`, `#Adversarial Attacks`, `#Large Language Models`, `#AI Alignment`, `#Interpretability`

---

<a id="item-8"></a>
## [特朗普签署行政令：开发首台开启科学发现新时代的量子计算机](https://www.ithome.com/0/967/747.htm) ⭐️ 8.0/10

美国总统唐纳德·特朗普于 6 月 22 日签署行政令，更新国家量子战略，并成立量子计算机应用开发与发现科学（QC-ADDS）项目。该命令还要求制定推进量子传感与网络发展的 5 年计划，并确定至少三个在 2028 年 9 月 30 日前投入使用的下一代量子传感器优先开发项目。 这项行政令代表了美国政府在量子信息科学与技术（QIST）这一全球科技竞争关键前沿领域保持战略优势的重大举措。通过调动国家资源来建造实用的大规模量子计算机并推进量子传感技术，美国旨在加速商业应用并巩固其更广泛的量子供应链生态系统。 QC-ADDS 项目将由总统科学和技术助理（APST）负责协调，至少一台量子计算机计划交付给美国能源部下属设施。该命令还强调加强国内量子供应链，保护美国量子技术和人才储备，并深化与盟国的量子合作。

rss · IT HOME · Jun 24, 01:41

**背景**: 量子信息科学与技术（QIST）是一门新兴的交叉学科，它将量子力学与信息技术相结合，旨在在计算、通信和传感领域实现突破。量子计算机利用量子叠加和量子纠缠等量子力学现象来处理信息，有望解决传统计算机难以处理的复杂问题。量子传感器则利用类似的量子现象在原子层面上以前所未有的精度测量物理量，可广泛应用于先进导航和磁场探测等领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.whitehouse.gov/presidential-actions/2026/06/ushering-in-the-next-frontier-of-quantum-innovation/">Ushering in the Next Frontier of Quantum Innovation</a></li>
<li><a href="https://insight.tmcnet.com/insight/executive-order-14411-advances-us-quantum-capabilities-1782198778608">Executive Order 14411 advances US quantum capabilities</a></li>
<li><a href="https://www.nist.gov/quantum-information-science/quantum-sensing-explained">Quantum Sensing Explained | NIST</a></li>

</ul>
</details>

**标签**: `#Quantum Computing`, `#Frontier Tech`, `#US Policy`, `#Quantum Information Science`, `#Executive Order`

---

<a id="item-9"></a>
## [火山引擎发布豆包音频生成模型 1.0，支持多模态参考生成](https://www.ithome.com/0/967/748.htm) ⭐️ 8.0/10

火山引擎正式发布了豆包音频生成模型 1.0（Doubao-Seed-Audio 1.0），该多模态音频生成模型支持以文本或音频作为输入进行零样本生成。它允许创作者在单条 Prompt 中编排包含多角色对白、情绪和背景音乐的影视级复杂音频场景，并能在长时生成中保持音色的一致性。 此次发布通过消除传统工作流中分别生成人声、音效和音乐并进行多轨混音与手动对齐的需求，大幅简化了专业音频制作流程。它为音频创作者、播客作者和电影制作人提供了一个端到端的“音频导演”工具，有望实现高质量叙事音频创作的大众化。 该模型目前单次支持生成最长 2 分钟的音频，并可作为参考输入来延长音频，同时在多次延长中保持高度的音色一致性。它还具备音色与风格解耦控制的能力，允许同一个声音适配不同的情绪语境或角色设定，且无需额外训练。

rss · IT HOME · Jun 24, 01:39

**背景**: 火山引擎是字节跳动旗下的云服务与企业技术平台，通过其火山方舟平台提供豆包系列大语言模型和多模态模型的调用服务。传统的 AI 音频生成通常需要分别处理人声、音效和音乐，然后再进行手动混音。新引入的多模态方法允许模型端到端地处理各种输入类型，从而能够通过单条指令直接生成复杂的、多层次的音频场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/29098">AI Daily: Volcano Engine launches Doubao Seedance 2.5 and other...</a></li>
<li><a href="https://www.atlascloud.ai/models/doubao">Doubao Models API Collection - Competitive Pricing... | Atlas Cloud</a></li>
<li><a href="https://www.huasheng.ai/insights/volcengine-ark-api-guide/">火山引擎方舟 API 平台深度调研 | 花叔 SDK中心 - api.volcengine.com OpenViking/docs/en/guides/02-volcengine-purchase ... - GitHub API Reference - Volcano Agent SDK | Complete TypeScript API ... API 文档概览 - 火山引擎 API 文档 火山方舟_大模型服务平台_豆包大模型API调用-火山引擎官网</a></li>

</ul>
</details>

**标签**: `#Audio Generation`, `#Multimodal AI`, `#Generative AI`, `#ByteDance`, `#Doubao`

---

<a id="item-10"></a>
## [消息称台积电先进制程代工将全线涨价，涵盖 7nm 及以下所有节点](https://www.ithome.com/0/967/746.htm) ⭐️ 8.0/10

科技分析师 Tim Culpan 透露，台积电已指示其业务开发和销售团队将所有先进节点（7nm 及以下，不仅限于此前传言的 3nm）的报价上调约 5% 至 10%。此次涨价将影响台积电约 75% 的晶圆营收来源，预计于今年下半年正式生效，有望推动台积电 2026 年全年营收突破 1600 亿美元。 台积电的先进制程（7nm 及以下）是制造 GPU 和 TPU 等尖端 AI 加速器的关键，此次涨价将直接推高 AI 算力成本和大语言模型训练的经济门槛。NVIDIA、AMD、Apple 等无晶圆厂设计公司将面临更高的芯片生产成本，这一影响可能传导至整个 AI 硬件供应链，并最终转嫁给终端客户。 整体涨幅在 5% 至 10% 之间，涨价措施生效后台积电至少 80% 的晶圆营收预计将来自先进节点。台积电管理层向团队表示，存储芯片同行正在享受价格上涨的红利，这家晶圆代工巨头也希望从中分一杯羹。

rss · IT HOME · Jun 24, 01:32

**背景**: 在半导体行业中，由台积电（TSMC）首创的晶圆代工模式（Foundry）是指专业制造企业为没有自有工厂的芯片设计公司（Fabless）提供芯片制造服务。制程节点（以纳米为单位，如 7nm、5nm、3nm）代表制造工艺的代际水平；节点越小，晶体管密度越高、功耗越低、性能越强，但制造成本和技术难度也大幅增加。先进制程（7nm 及以下）是生产 AI 加速器、高端 CPU 和手机处理器等最尖端芯片的必备条件，而台积电目前在该领域占据市场主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/晶圆代工/67378039">晶圆代工_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/9988705135">台积电先进制程规划及相关供应链介绍； - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/659644737">晶圆代工是什么？ - 知乎 - 知乎专栏</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#AI Infrastructure`, `#Semiconductors`, `#Advanced Nodes`, `#Hardware`

---

<a id="item-11"></a>
## [法律科技公司因 Anthropic 模型访问被封锁起诉美国政府](https://www.ithome.com/0/967/731.htm) ⭐️ 8.0/10

6 月 23 日，美国法律科技公司 Legion LegalTech Corp 向华盛顿哥伦比亚特区联邦法院提起诉讼，请求撤销美国商务部工业和安全局此前要求 Anthropic 禁止所有外国国民使用其 Fable 5 和 Mythos 5 模型的指令。该公司同时申请了一项初步禁令，以在案件审理期间阻止该指令继续执行。 这起诉讼是对美国政府利用出口管制权力限制前沿 AI 模型访问的首次重大法律挑战，其结果将为行政权力在 AI 部署领域的边界设定先例。裁决将直接影响所有依赖美国先进 AI 系统且拥有国际团队或海外业务的公司，并可能影响其他国家对 AI 模型治理的政策走向。 Anthropic 在 6 月 12 日 BIS 指令下达当天即关闭了全球所有客户的访问权限，而非仅针对外国国民，以确保合规。Legion 在诉状中强调，该禁令瞬间切断了其驻加拿大软件开发团队的访问权限，导致业务全面停滞，并称这一损害在当前前沿 AI 领域飞速发展的背景下是即时的、不可挽回且生死攸关的。

rss · IT HOME · Jun 24, 00:45

**背景**: Anthropic 的 Mythos 5 是一款以在发现和利用网络安全漏洞方面具有超凡能力而闻名的前沿 AI 模型，Fable 5 则是其面向公众的版本，在网络安全和生物等敏感领域增加了额外的安全防护措施。美国商务部工业和安全局（BIS）自 2025 年初以来持续扩大出口管制范围，旨在限制先进 AI 能力的全球扩散，包括对 AI 模型权重和先进计算产品的限制。初步禁令是一种临时性法院命令，可在最终裁决前暂停政府行为的执行，通常在原告能够证明将遭受不可挽回的损害时才会批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nbcnews.com/tech/security/fable-5-anthropic-release-public-mythos-claude-model-rcna349104">Anthropic releases Fable 5 , the first public Mythos -class model</a></li>
<li><a href="https://www.cov.com/en/news-and-insights/insights/2025/01/us-department-of-commerce-establishes-export-control-framework-limiting-the-diffusion-of-advanced-artificial-intelligence-and-expands-and-clarifies-advanced-computing-controls">U.S. Department of Commerce Establishes Export Control ...</a></li>
<li><a href="https://www.clio.com/resources/legal-dictionary/preliminary-injunction/">Preliminary Injunction | Legal Dictionary | Clio</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Regulation`, `#Export Controls`, `#Frontier AI`, `#AI Policy`

---

<a id="item-12"></a>
## [中国“灵晟”超算登顶 TOP500，时隔八年重回世界第一](https://news.mydrivers.com/1/1131/1131573.htm) ⭐️ 8.0/10

China's 'Lingsheng' supercomputer has officially topped the TOP500 list, becoming the world's first pure CPU system to exceed 2 ExaFLOPS.

telegram · @zaihuapd · Jun 23, 15:30

**标签**: `#Supercomputing`, `#HPC`, `#Frontier Tech`, `#Hardware`, `#TOP500`

---