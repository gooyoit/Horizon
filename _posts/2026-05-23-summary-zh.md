---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 114 items, 10 important content pieces were selected

---

1. [Anthropic 的 Glasswing 项目在 AI 漏洞发现中实现超 90%的真正例率](#item-1) ⭐️ 9.0/10
2. [Nemotron-Labs 扩散语言模型实现光速级文本生成](#item-2) ⭐️ 9.0/10
3. [Google Gemini 用户突破 9 亿，推出 AI 代理功能与新模型](#item-3) ⭐️ 9.0/10
4. [字节跳动开源 Lance：3B 统一多模态模型](#item-4) ⭐️ 9.0/10
5. [AI 应用新趋势：架构分化、组织重构与性能突破](#item-5) ⭐️ 8.5/10
6. [DeepSeek 将 V4 Pro 降价永久化，同时大幅下调缓存命中价格](#item-6) ⭐️ 8.0/10
7. [一个人，一门课，一个 AI 自动化工厂](#item-7) ⭐️ 8.0/10
8. [谷歌 SensorFM：基于万亿分钟可穿戴数据的基础模型](#item-8) ⭐️ 8.0/10
9. [Demis 称奇点可能仅数年之遥](#item-9) ⭐️ 8.0/10
10. [Anthropic 即将完成逾 300 亿美元融资轮](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 的 Glasswing 项目在 AI 漏洞发现中实现超 90%的真正例率](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 的 Glasswing 项目发布了初始更新，显示其由全新 Claude Mythos Preview 模型驱动的 AI 模型能够大规模发现生产代码中的有效安全漏洞。在由独立安全研究公司评估的 1,752 个高严重或严重等级漏洞中，90.6%（1,587 个）被确认为真正例，其中 1,094 个被验证为高严重或严重等级。 这代表了前沿 AI 应用于主动网络安全防御的重大能力展示，有可能让防御者在攻击者利用关键软件缺陷之前就发现并修复它们，从而获得持久优势。来自独立研究人员的验证结果大大增强了 AI 在漏洞发现方面能够显著超越传统静态分析工具这一说法的可信度。 该项目与负责关键基础设施的组织合作，使用 Anthropic 专为安全分析调优的最新前沿模型 Claude Mythos Preview。六家独立安全研究公司参与了发现的验证工作，提供了超越 Anthropic 自身评估的外部可信度。

hackernews · louiereederson · May 22, 19:31 · [社区讨论](https://news.ycombinator.com/item?id=48240419)

**背景**: Glasswing 项目是 Anthropic 为 AI 时代保护全球最关键软件安全的倡议，其认识到同样能增强网络攻击的 AI 能力也可以在防御性安全研究中发挥巨大价值。传统的漏洞发现依赖于静态分析工具、代码检查器和模糊测试，这些方法能捕获常见模式但往往遗漏复杂的、依赖上下文的漏洞。真正例率衡量的是一个工具报告的发现中有多少是真实的漏洞，这是评估任何自动化安全工具实用性的关键指标。AI 在网络安全中的双重用途性质意味着，自动化漏洞发现的进步必须在赋能防御者与降低攻击性滥用风险之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.anthropic.com/project/glasswing">Project Glasswing</a></li>
<li><a href="https://www.picussecurity.com/resource/blog/anthropics-project-glasswing-paradox">What Is Project Glasswing? Anthropic's AI Misuse Research Initiative Explained</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一但总体偏正面：几位评论者赞扬了高真正例率，并分享了他们使用 Codex Security 等 AI 安全工具的积极体验，称其为"不可或缺的"且准确率约为 90%。然而，质疑依然存在，一位评论者引用了 curl 维护者 Daniel Steinberg 的反馈，认为 Mythos 并未显著超越现有工具，另一位评论者则指出许多代码库在转向昂贵的基于 LLM 的解决方案之前甚至还没有采用基本的静态分析和代码检查工具。

**标签**: `#AI security`, `#Anthropic`, `#vulnerability discovery`, `#frontier AI applications`, `#code analysis`

---

<a id="item-2"></a>
## [Nemotron-Labs 扩散语言模型实现光速级文本生成](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion) ⭐️ 9.0/10

NVIDIA's Nemotron-Labs introduces a diffusion-based language model architecture designed to dramatically accelerate text generation speeds and improve throughput compared to traditional autoregressive models.

rss · AI Hot · May 23, 00:02

**标签**: `#Diffusion Models`, `#NLP`, `#NVIDIA`, `#LLM`, `#AI Research`

---

<a id="item-3"></a>
## [Google Gemini 用户突破 9 亿，推出 AI 代理功能与新模型](https://x.com/GeminiApp/status/2057974680242512071) ⭐️ 9.0/10

谷歌宣布 Gemini 应用月活跃用户已突破 9 亿，并发布了一项重大升级，将其从被动工具转变为主动式 AI 代理。此次更新引入了 Gemini 3.5 Flash 模型、Gemini Omni 视频生成模型、全新的"Neural Expressive"设计语言，以及 Daily Brief 和 Gemini Spark 两项代理功能。 此次升级标志着 AI 助手领域的重大转变，从简单的问答交互走向能够主动管理用户数字生活的自主代理。凭借 9 亿用户的庞大基数，谷歌正在利用其规模优势重新定义主流消费者日常与 AI 交互的方式。 Gemini 3.5 Flash 以 Flash 系列的速度提供了媲美大型旗舰模型的智能水平，在 Artificial Analysis 智能指数中得分 55，远高于同类模型 36 的平均分。Gemini Omni 是一个统一的多模态系统，原生处理文本、图像、视频和音频，用户可通过自然对话生成和编辑视频。Gemini Spark 则作为全天候个人代理，在用户授权下主动管理各项任务。

rss · AI Hot · May 22, 23:59

**背景**: Google Gemini 是谷歌的旗舰 AI 助手，与 OpenAI 的 ChatGPT 等前沿 AI 产品竞争。"Neural Expressive"设计语言标志着对传统聊天记录界面的突破，采用流畅动画、鲜艳色彩、新字体和触觉反馈，打造更具动态感的交互体验。AI 代理的概念——能够代表用户自主执行多步骤任务的系统——已成为行业关键趋势，各大实验室竞相构建超越简单问答、能在用户数字环境中真正采取行动的 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>
<li><a href="https://gemini.google/overview/video-generation/">Gemini Omni – Create & edit videos as easy as having a ...</a></li>
<li><a href="https://www.urdesignmag.com/google-gemini-neural-expressive-redesign-2026/">Google Gemini's Neural Expressive Redesign Ends the Chat Log ...</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#AI Agents`, `#Generative AI`, `#Multimodal AI`, `#Frontier Models`

---

<a id="item-4"></a>
## [字节跳动开源 Lance：3B 统一多模态模型](https://mp.weixin.qq.com/s/Xbfq72cr1796RZxJIs3L1A) ⭐️ 9.0/10

字节跳动发布了轻量级多模态模型 Lance，激活参数量仅 3B，在单一架构中原生统一了图像理解、视频理解、图像生成、视频生成和跨模态编辑五大能力。模型权重已在 Hugging Face 上以 Apache 2.0 许可开放。 Lance 证明了仅 3B 参数的轻量模型即可在图像和视频的理解与生成任务上取得竞争力表现，大幅降低了开发者和研究者的硬件门槛。其 Apache 2.0 许可和开放权重的发布方式，使其在快速发展的多模态 AI 领域中具备极高的商业和社区应用潜力。 Lance 采用共享上下文与双流专家架构，分别由 Qwen2.5-VL 编码器处理理解任务、Wan2.2 编码器处理生成任务，并通过模态感知位置编码解决序列边界混淆问题。该模型在 GenEval 图像生成和 VBench 视频生成等基准测试上取得了领先结果。

telegram · @zaihuapd · May 22, 06:40

**背景**: 统一多模态模型的目标是在单一模型中同时处理理解（如图像描述、视频问答）和生成（如文生图、文生视频）任务，而非依赖多个专用模型。Qwen2.5-VL 是 Qwen 系列中的视觉语言模型，以强大的视觉识别、文档解析和长视频理解能力著称。Wan2.2 是一个开源的混合专家（MoE）视频生成模型，专为电影级 AI 视频创作而设计。将这两个编码器结合在双流架构中，使 Lance 能够分别发挥各自优势，同时保持紧凑的参数规模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.13923">[2502.13923] Qwen2.5-VL Technical Report</a></li>
<li><a href="https://huggingface.co/collections/Qwen/qwen25-vl">Qwen2.5-VL - a Qwen Collection</a></li>
<li><a href="https://wan22.io/">Wan 2 . 2 - Open Source MoE Video Generation | Every Shot... | wan22.io</a></li>

</ul>
</details>

**标签**: `#multimodal-model`, `#open-source-ai`, `#bytedance`, `#video-generation`, `#image-generation`

---

<a id="item-5"></a>
## [AI 应用新趋势：架构分化、组织重构与性能突破](https://x.com/hongming731/status/2057993813239775331) ⭐️ 8.5/10

This article highlights three key AI trends: the architectural divergence of AI agents into long-context and low-latency paths, organizational shifts towards agile 'jazz band' structures for AI development, and Zhipu's release of the high-speed GLM-5.1 model achieving 400 tokens/s.

rss · AI Hot · May 23, 01:15

**标签**: `#AI Agents`, `#Large Language Models`, `#Zhipu AI`, `#AI Architecture`, `#AI Industry Trends`

---

<a id="item-6"></a>
## [DeepSeek 将 V4 Pro 降价永久化，同时大幅下调缓存命中价格](https://api-docs.deepseek.com/quick_start/pricing) ⭐️ 8.0/10

DeepSeek 宣布，在 2026 年 5 月 31 日 75%促销折扣结束后，deepseek-v4-pro 模型 API 定价将永久维持在原价的 1/4。此外，所有模型的输入缓存命中价格已降至原发布价格的 1/10，自 2026 年 4 月 26 日起生效，且无截止日期。 此举巩固了 DeepSeek 作为定价最激进的前沿 AI 模型提供商的地位，对 OpenAI、Google 和 Anthropic 等竞争对手施加了巨大的竞争压力。尤其是超低的缓存命中定价，可能会重塑开发者在提示词缓存方面的应用架构方式，使长上下文和重复工作负载场景的使用成本大幅降低。 DeepSeek V4 Pro 是一个混合专家（MoE）模型，总参数量为 1.6 万亿，激活参数量为 490 亿，支持 100 万 token 的上下文窗口。V4 Flash 的缓存命中价格现在仅为输入价格的 2%，而 V4 Pro 更是低至 0.8%，这些数字与任何竞争对手相比都极低，也引发了关于单位经济效益可持续性的疑问。

hackernews · Tiberium · May 22, 15:59 · [社区讨论](https://news.ycombinator.com/item?id=48237663)

**背景**: DeepSeek V4 Pro 目前被认为是最好的开源 AI 模型，基于混合专家（MoE）架构构建，每次推理仅激活总参数的一个子集，从而以较低的计算成本实现强大的性能。在 LLM API 定价生态系统中，提供商区分"缓存未命中"价格（用于新的、未见过的输入 token）和"缓存命中"价格（用于匹配先前缓存提示词的 token），缓存命中的价格要便宜得多。DeepSeek 一直坚持以前沿级模型能力以竞争对手价格的一小部分提供的策略，其部分资金来源是其隐私政策中声明的使用用户输入来训练模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing">Models & Pricing | DeepSeek API Docs</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V 4 Pro - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek -ai/ DeepSeek - V 4 - Pro · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞 DeepSeek 的开源贡献和价格实惠，但也有人对如此低价的可持续性表示怀疑。一位评论者指出，同一模型在第三方提供商处托管的价格要高得多，这引发了关于 DeepSeek 的低价是否通过使用用户输入进行训练来补贴的疑问。其他人则强调超低的缓存命中定价对应用经济学的影响尤为显著，还有几位用户对 DeepSeek 传闻中即将推出的编程代理产品表示期待。

**标签**: `#DeepSeek`, `#AI Pricing`, `#Frontier Models`, `#LLM API`, `#AI Industry`

---

<a id="item-7"></a>
## [一个人，一门课，一个 AI 自动化工厂](https://x.com/shao__meng/status/2057997802735796293) ⭐️ 8.0/10

Wix 副总裁推出免费课程「Zero to Claude Code」，已吸引超过 17,000 名学员，支持 7 种语言，整个平台由一人使用 Claude Code 构建并运营。平台日处理约 640 万请求且错误率极低，并实现了学员报 Bug 后自动修复、社区功能需求自动实现的全流程 AI 闭环自动化。 这是目前最具说服力的真实生产案例之一，证明了一个普通人借助 Claude Code 等自主 AI 编程代理，就能构建并维护一个可扩展的生产级软件平台。这预示着软件开发领域的范式转变，传统的工程团队模式可能被 AI 代理工作流大幅替代甚至颠覆。 该平台最引人注目的技术亮点是其 AI 闭环运营模式：当学员通过社区提交 Bug 报告或功能需求时，Claude Code 会自主完成分类、修复和部署，几乎无需人工干预。该课程面向零基础用户，从终端使用基础开始教学，最终帮助学员在生产环境中使用 Claude Code 发布软件。

rss · AI Hot · May 23, 01:31

**背景**: Claude Code 是 Anthropic 推出的代理式编程系统，它在开发者现有环境中运行，能够自主编写、调试和部署代码，但在修改文件或运行命令前仍需获得人类的明确许可。「Vibe Coding」由 Andrej Karpathy 于 2025 年 2 月提出，指的是一种 AI 辅助开发实践，用户用自然语言描述意图，AI 自动生成相应代码，使非程序员也能构建功能完整的软件。软件开发中的代理式工作流是指 AI 代理能够执行完整的开发周期——从需求分析到代码生成、测试，再到创建生产级拉取请求——人类在合并前对输出进行审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://medium.com/quantumblack/agentic-workflows-for-software-development-dc8e64f4a79d">Agentic workflows for software development | by QuantumBlack, AI by McKinsey | QuantumBlack, AI by McKinsey | Medium</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI Agents`, `#Autonomous Software Development`, `#Vibe Coding`, `#Anthropic`

---

<a id="item-8"></a>
## [谷歌 SensorFM：基于万亿分钟可穿戴数据的基础模型](https://x.com/rohanpaul_ai/status/2057978365664272796) ⭐️ 8.0/10

谷歌研究院提出了 SensorFM，这是一个基于超过 500 万人产生的逾 1 万亿分钟可穿戴传感器数据训练的基础模型，能够学习通用生理模式而非依赖人工设计的特征。该模型在 35 项健康预测任务中的 34 项上超越了传统基于特征工程的基线方法，并展现出明确的扩展规律——模型规模越大、数据越多，性能越强。 这项研究证明了在语言和视觉领域已被验证的扩展规律同样适用于生理传感器数据，有望将可穿戴设备从简单的追踪器转变为智能健康监测系统。它可能催生新一代数字健康教练、临床监测工具和个人健康应用，利用深度学习到的表征来处理多种健康任务。 SensorFM 从原始传感器数据中提取有意义的结构化表征，并将其复用于多种健康预测任务，超越了将数据压缩为简单汇总指标的传统方法。研究团队的下一步计划包括纳入新的传感器数据类型（如代谢健康和睡眠分析数据），并实现与模型的自然语言交互。

rss · AI Hot · May 23, 00:14

**背景**: 传统的可穿戴健康监测依赖特征工程，即由领域专家从原始传感器数据中手动设计特定指标（如平均心率、步数），再输入机器学习模型。基础模型受 GPT 等大语言模型成功的启发，通过自监督预训练直接从海量原始数据中学习丰富的表征，然后可以微调或应用于下游任务。谷歌研究院此前已通过其大型传感器模型（LSM）工作探索了这一方向，使用来自 16.5 万用户的 4000 万小时去标识化多模态传感器数据进行训练，以研究可穿戴领域的扩展特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pharmaphorum.com/news/google-wearable-ai-can-learn-language-our-bodies">Google wearable AI can 'learn the language of our bodies' | pharmaphorum</a></li>
<li><a href="https://research.google/blog/scaling-wearable-foundation-models/">Scaling wearable foundation models - Google Research</a></li>
<li><a href="https://arxiv.org/abs/2410.13638">[2410.13638] Scaling Wearable Foundation Models - arXiv.org Sensor Foundation Models | Girish Narayanswamy Beyond Sensor Data: Foundation Models of Behavioral Data from ... Insulin resistance prediction from wearables and routine ... Scaling Wearable Foundation Models – Ubicomp Lab – Ubiquitous ... Scaling Wearable Foundation Models</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#Foundation Model`, `#Google Research`, `#Wearable Technology`, `#Digital Health`

---

<a id="item-9"></a>
## [Demis 称奇点可能仅数年之遥](https://x.com/kimmonismus/status/2057975137518158253) ⭐️ 8.0/10

Google DeepMind CEO Demis Hassabis states that the technological singularity, driven by the arrival of true AGI, could be only years away and will be the most important technology in history.

rss · AI Hot · May 23, 00:01

**标签**: `#AGI`, `#Singularity`, `#Demis Hassabis`, `#DeepMind`, `#AI Predictions`

---

<a id="item-10"></a>
## [Anthropic 即将完成逾 300 亿美元融资轮](https://36kr.com/newsflashes/3821194878947715?f=rss) ⭐️ 8.0/10

据报道，Anthropic PBC 最快将于下周完成超过 300 亿美元的融资轮，公司估值超过 900 亿美元，有望成为全球估值最高的人工智能初创公司。红杉资本、Dragoneer Investment Group、Altimeter Capital 和 Greenoaks Capital Partners 预计将联合领投本轮融资，每家公司计划投资约 20 亿美元。 这笔巨额融资将使 Anthropic 在初创公司估值方面超越竞争对手 OpenAI，显著重塑前沿 AI 公司的竞争格局。如此规模的融资轮凸显了构建前沿 AI 模型所需的巨大资金需求，也表明尽管市场存在不确定性，投资者对 AI 领域的信心依然强劲。 四家联合领投方——红杉资本、Dragoneer Investment Group、Altimeter Capital 和 Greenoaks Capital Partners——每家承诺投资约 20 亿美元，显示出顶级风投公司的高度集中下注。据报道，超过 900 亿美元的估值较 Anthropic 此前的融资轮有大幅溢价。

rss · 36kr · May 23, 01:30

**背景**: Anthropic PBC 于 2021 年由前 OpenAI 研究员创立，包括 Daniela Amodei（总裁）和 Dario Amodei（首席执行官）兄妹，总部位于旧金山。该公司以开发 Claude 系列大语言模型而闻名，并以公益企业的形式运营，强调以安全为核心的 AI 研发理念。Anthropic 与 OpenAI、Google DeepMind 等前沿 AI 实验室在构建先进 AI 系统的竞争中直接对抗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.britannica.com/money/Anthropic-PBC">Anthropic | History, Controversies, & Claude AI | Britannica ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Funding`, `#Frontier AI`, `#Venture Capital`

---