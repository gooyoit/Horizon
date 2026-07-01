---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> From 115 items, 15 important content pieces were selected

---

1. [Anthropic 发布 Claude Sonnet 5，专为自主智能体任务优化](#item-1) ⭐️ 10.0/10
2. [美国商务部解除对 Anthropic Claude Fable 5 和 Mythos 5 的出口管制](#item-2) ⭐️ 10.0/10
3. [Claude Sonnet 5 发布：性能接近 Opus，但新分词器暗藏涨价](#item-3) ⭐️ 10.0/10
4. [Google DeepMind 发布最快、最便宜的多模态图像模型 Nano Banana 2 Lite](#item-4) ⭐️ 9.0/10
5. [Tenstorrent 发布 TT-Ascalon S RISC-V 内核，专为代理式 AI 优化](#item-5) ⭐️ 9.0/10
6. [Meta AI 发布 Brain2Qwerty v2：无需手术的脑电波解码系统](#item-6) ⭐️ 9.0/10
7. [华为在 HDC 2026 上开源盘古 2.0 模型，参数量达 505B](#item-7) ⭐️ 9.0/10
8. [谷歌发布 Nano Banana 2 Lite 和 Gemini Omni Flash，实现 4 秒出图与 10 秒视频生成](#item-8) ⭐️ 9.0/10
9. [Anthropic 发布 Claude Sonnet 4.6，编程与计算机使用能力大幅提升](#item-9) ⭐️ 9.0/10
10. [Claude Code 被发现在请求中嵌入隐写标记](#item-10) ⭐️ 8.0/10
11. [Anthropic 推出 Claude Science，面向科学研究的 AI 工作台](#item-11) ⭐️ 8.0/10
12. [Leanstral 1.5 发布：面向 Lean 4 自动定理证明的 119B MoE 模型](#item-12) ⭐️ 8.0/10
13. [Etched 推理加速器芯片 Sohu 完成流片，获 8 亿美元融资和超 10 亿美元订单](#item-13) ⭐️ 8.0/10
14. [特斯拉首台量产 Cybercab 无人驾驶电动车在奥斯汀开启工程测试](#item-14) ⭐️ 8.0/10
15. [Anthropic 获美政府批准，恢复 Mythos 5 模型对关键基础设施的部署](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Sonnet 5，专为自主智能体任务优化](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 10.0/10

Anthropic 宣布发布 Claude Sonnet 5，这是一款专为自主智能体任务、规划和工具使用而优化的全新 AI 模型。该模型能够自主使用浏览器和终端等工具，其能力水平在几个月前还需要更大、更昂贵的模型才能实现。 此次发布代表了 AI 行业向智能体化 AI 的更广泛转变，即模型能够利用实时数据和迭代决策独立执行链式任务，无需持续的人工指导。通过将高级智能体能力引入中端 Sonnet 系列，Anthropic 可能会让自主智能体辅助开发变得更加普及，但社区也指出与竞争模型相比存在显著的成本性能权衡。 社区基准测试显示，Claude Sonnet 5 的性能大约与 GLM-5.2 相当，但成本是其 2 倍，速度也是其 2 倍，在常识问答（0/3 得分）、组合工具调用任务（45/100）和解谜（77/100）方面存在明显弱点。每任务成本分析表明，在中等努力级别以上，Opus 在相同成本下始终表现更好，系统卡片还显示在 CyberGym 漏洞发现方面，Sonnet 5 实际上不如 Sonnet 4.6。

hackernews · marinesebastian · Jun 30, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: 智能体化 AI 是指能够独立执行链式任务、整合多种数据源、并在无需持续人工指导的情况下采取行动的自主 AI 系统。工具使用（或函数调用）是一项关键能力，允许大语言模型作为响应的一部分调用外部工具、API 或数据库，使智能体能够搜索网页、查询数据库、发送邮件或控制软件。Anthropic 的 Claude 模型系列包括不同层级——Sonnet（中端）和 Opus（高端），每个层级为不同使用场景提供不同的成本性能比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@usamasafdar.us/agentic-ai-how-autonomous-ai-agents-are-transforming-workflows-cef7a7b9efbf">Agentic AI : How Autonomous AI Agents Are Transforming... | Medium</a></li>
<li><a href="https://benchlm.ai/llm-agent-benchmarks">LLM Agent & Tool-Use Benchmarks — Function Calling, MCP ...</a></li>
<li><a href="https://grokipedia.com/page/Tool_use_in_large_language_models">Tool use in large language models</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体偏批评性，多位用户质疑为何要使用 Sonnet 5 而非在更低努力级别下使用 Opus，因为在中等努力级别以上 Opus 的单位成本表现更好。基准测试者指出其以两倍成本匹配 GLM-5.2 的性能，还有人观察到，专为完全自主智能体开发优化的模型在实际被许多开发者使用的智能体辅助开发工作流中可能表现更差。

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#AI Agents`, `#Frontier AI`

---

<a id="item-2"></a>
## [美国商务部解除对 Anthropic Claude Fable 5 和 Mythos 5 的出口管制](https://simonwillison.net/2026/Jun/30/anthropic/#atom-everything) ⭐️ 10.0/10

2026 年 6 月 30 日，Anthropic 宣布美国商务部已正式解除对其 Claude Fable 5 和 Mythos 5 模型的出口管制，并将于次日起恢复访问权限。这扭转了 2026 年 6 月初实施的史无前例的针对特定公司的出口限制。 这一事件标志着一项重大监管政策的逆转，直接影响前沿 AI 系统的全球可用性，恢复了国际社会对当前最强大模型的访问。它还凸显了依赖美国 AI 技术的企业所面临的巨大监管不确定性，因为出口管制可以在几乎没有预警的情况下被实施和解除。 Claude Fable 5 是更强大的 Mythos 5 模型的广泛发布、带有安全防护的版本，涉及网络安全和生物学等敏感领域的查询会被自动路由到另一个模型（Opus 4.8）。根据商务部的信函，Anthropic 通过与美国政府密切协调，主动检测和应对与模型相关的安全风险，从而恢复了访问权限。

rss · Simon Willison · Jun 30, 23:58

**背景**: 2026 年 6 月 12 日，美国商务部采取了史无前例的步骤，将出口管制直接扩展到 AI 模型，发布了一封限制访问 Anthropic 前沿模型的信函。Claude Fable 5 和 Mythos 5 于 2026 年 6 月发布，是 Anthropic 最强大的模型系列，专为高要求的推理和长周期智能体任务而构建。这些管制措施是更广泛监管环境的一部分，商务部一直在调整拜登时代的 AI 扩散规则等政策，以管理先进 AI 技术的全球传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mayerbrown.com/en/insights/publications/2026/06/commerce-department-extends-export-controls-to-advanced-ai-models-authorizes-release-to-specific-trusted-partners">Commerce Department Extends Export Controls to Advanced AI ...</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍持怀疑态度，用户认为对信任的损害已经造成，在不可预测的监管波动下，企业无法安全地在美国前沿模型之上构建关键功能。一些评论者指出，来自更便宜的中国 AI 模型的竞争压力可能迫使政府做出了让步，而另一些人则认为所声称的安全理由只是政治作秀，模型本身并没有发生真正的技术变化。

**标签**: `#Anthropic`, `#Claude`, `#AI Regulation`, `#Export Controls`, `#Frontier AI`

---

<a id="item-3"></a>
## [Claude Sonnet 5 发布：性能接近 Opus，但新分词器暗藏涨价](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 10.0/10

Anthropic 发布了 Claude Sonnet 5，该模型性能接近 Opus 4.8 但价格更低，拥有 100 万 token 的上下文窗口、12.8 万最大输出 token，并默认开启自适应思考功能。然而，该模型采用了新的分词器，相同英文文本产生的 token 数量比 Sonnet 4.6 多约 30%，这意味着尽管标价相同，实际使用成本却大幅上升。 Sonnet 5 是 Anthropic 模型产品线的重要一步，缩小了中端模型与旗舰模型之间的性能差距，同时通过将网络安全能力控制在 Mythos 5 等受限模型之下，成功规避了美国政府的安全监管。分词器的变化对开发者和企业至关重要，因为它从根本上改变了基于 Claude API 构建的应用的成本结构。 重要的 API 变更包括不再支持 temperature、top_p 和 top_k 采样参数，这意味着开发者无法再手动控制输出的随机性。分词器的影响因语言而异：英文文本成本增加 1.42 倍，西班牙文 1.33 倍，Python 代码 1.28 倍，而简体中文的成本与之前基本持平。

rss · Simon Willison · Jun 30, 21:23

**背景**: 系统卡是 AI 实验室发布的结构化文档，用于披露模型的能力、安全评估和负责任的部署决策，常用于证明符合新兴的 AI 法规。前沿 AI 模型是当前最强大的模型，监管机构密切关注那些可能具有危险能力的模型，尤其是在网络安全和生物领域。Anthropic 的 Mythos 5 因其强大的网络攻击能力仅限量发布，而 Sonnet 5 在这些领域的能力较低，因此可以广泛部署而不会遇到监管障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/system-card">System card</a></li>
<li><a href="https://beginnersinai.org/glossary-what-is-frontier-model/">What is Frontier Model ? — AI Glossary - Beginners in AI</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#Frontier AI`, `#LLM`, `#AI Safety`

---

<a id="item-4"></a>
## [Google DeepMind 发布最快、最便宜的多模态图像模型 Nano Banana 2 Lite](https://simonwillison.net/2026/Jun/30/nano-banana-2-lite/#atom-everything) ⭐️ 9.0/10

Google DeepMind 发布了 Gemini 3.1 Flash Lite Image（俗称“Nano Banana 2 Lite”），这是其针对速度和规模进行优化的最快、最便宜的图像生成模型。Simon Willison 的早期测试表明，该模型能在几秒钟内生成复杂的密集插图场景，并且与上一代相比在文本渲染方面有所提升。 此次发布大幅降低了依赖多模态图像生成的高并发、低延迟应用的门槛。通过提供一个高效且经济的模型，Google 使开发者能够将复杂的视觉生成大规模整合到智能体工作流和消费级应用中。 该模型生成图像的时间不到 5 秒，而基础的 Nano Banana 2 模型大约需要 30 秒，但目前它缺乏以编程方式强制设定宽高比的功能。虽然它能很好地处理复杂的提示词并保持良好的文本渲染，但在复杂插图中仍然难以实现完全精确的拼写。

rss · Simon Willison · Jun 30, 22:15

**背景**: Gemini 3.1 Flash-Lite 是 Google 为低延迟、高吞吐量任务提供高性价比模型战略的一部分。它支持包括文本、图像、视频和音频在内的多种输入，是一个真正的多模态系统。开发者可以使用 Google AI Studio（一个用于构建生成式 AI 应用的网络环境）对这些模型进行原型设计和测试。“Nano Banana”这个名称是社区对 Google 近期高质量图像生成模型的非正式昵称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite">Gemini 3.1 Flash-Lite | Gemini API | Google AI for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Studio">Google AI Studio</a></li>

</ul>
</details>

**社区讨论**: 获得早期访问权限的用户称赞了该模型令人印象深刻的生成速度和改进的面部相似度渲染，认为它是基础模型的可靠精简版本。然而，用户对 Google 碎片化的账户生态系统表示了明显的不满，这使得 Workspace 用户通过 AI Studio 访问该模型变得不必要地困难。此外，一些评论者对该模型在房地产列表中被滥用的潜在可能表示了怀疑，并指出报告中缺乏与 ChatGPT 等竞争对手的直接比较。

**标签**: `#Generative AI`, `#Google DeepMind`, `#Gemini`, `#Image Generation`, `#Multimodal AI`

---

<a id="item-5"></a>
## [Tenstorrent 发布 TT-Ascalon S RISC-V 内核，专为代理式 AI 优化](https://aihot.virxact.com/items/cmr1flg1i02f7slnlidhmmuve) ⭐️ 9.0/10

Tenstorrent 发布了全新的 RISC-V CPU 内核 TT-Ascalon S，该内核以旗舰核心 Ascalon X 一半的面积实现了其 70% 的性能，单位面积性能达到 1.4 倍。该公司还展示了其 Galaxy Blackhole 超级集群在运行 Kimi K2.6 模型时达到每用户 900 Token/s（GPU 的三倍），在 DeepSeek-R1-0528 671B 上达到每用户 400+ Token/s。 此次发布标志着 AI 算力基础设施的重大转变，证明了专为代理式 AI 工作负载优化的 RISC-V CPU 在大语言模型推理和视频生成任务中能够大幅超越传统 GPU。出色的性能数据表明，专用 RISC-V 架构有望打破 GPU 主导的 AI 硬件市场格局，并实现更具成本效益的大语言模型部署。 TT-Ascalon S 是一款乱序超标量 4 宽解码内核，符合 RVA23 配置文件，配备单个 256 位矢量单元、32KB 指令缓存和 64KB 数据缓存，每 GHz 在 SPECint2006 中可得 15 分。单个集群可扩展至 8 核，拥有可配置的共享 L2 缓存，该设计专门针对 AI 智能体运行时典型的混合型、分支密集、工具关联的执行模式进行了优化。

rss · AI Hot · Jul 1, 01:42

**背景**: RISC-V 是一种开放标准的指令集架构（ISA），作为 x86 和 ARM 等专有架构的替代方案正获得越来越多的关注，尤其是在面向特定工作负载的定制芯片领域。RVA23 配置文件是 RISC-V 的一项规范，定义了一组强制性的扩展和要求，以确保不同硬件实现之间的软件兼容性，这对于构建成熟的生态系统至关重要。代理式 AI 是指能够自主规划、执行多步骤任务并使用外部工具的 AI 系统，其产生的工作负载模式相比传统的深度学习训练或批量推理更加分支密集和异构化。由著名芯片架构师 Jim Keller 领导的 Tenstorrent 一直在开发高性能 RISC-V CPU 和 AI 加速器，作为其在数据中心和 AI 基础设施市场竞争战略的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://riscv.org/ecosystem-news/2025/04/risc-v-rva23-a-major-milestone/">RISC - V RVA 23 —A Major Milestone – RISC - V International</a></li>
<li><a href="https://xpu.pub/2025/10/09/tenstorrent-ascalon/">Tenstorrent Licenses RISC-V CPU and NPU IP - XPU.pub</a></li>
<li><a href="https://www.exxactcorp.com/blog/deep-learning/agentic-ai-platforms-hardware-infrastructure">Agentic AI Platforms Hardware Infrastructure | Exxact Blog</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#RISC-V`, `#Tenstorrent`, `#AI Infrastructure`, `#Agentic AI`

---

<a id="item-6"></a>
## [Meta AI 发布 Brain2Qwerty v2：无需手术的脑电波解码系统](https://aihot.virxact.com/items/cmr1dmph001xfslnljs65wubx) ⭐️ 9.0/10

Meta AI 发布了 Brain2Qwerty v2，这是一种利用脑磁图（MEG）数据并结合微调大语言模型的非侵入式深度学习系统，能够实时将脑电波解码为文本。该系统基于 9 名志愿者约 22,000 个句子的训练数据，平均词准确率达到 61%，最佳参与者达 78%，远超此前非侵入式方法仅 8% 的准确率。 这在非侵入式脑机接口（BCI）领域实现了巨大的能力飞跃，大幅缩小了与需要植入电极的侵入式手术技术之间的性能差距。该研究证明了解码精度随数据量呈对数线性提升，为患有语言障碍的患者乃至更广泛人群提供了一条通向实用、安全的脑转文本通信的可行路径。 该系统采用在 MEG 记录上训练的端到端深度学习架构——MEG 用于捕捉神经活动产生的磁场——并利用大语言模型微调来提升语言预测能力。Meta 已开源 v1 和 v2 的训练代码，合作方 BCBL 也公开了 v1 数据集，以加速社区研究。

rss · AI Hot · Jul 1, 00:58

**背景**: 脑机接口（BCI）旨在建立人脑与外部设备之间的直接通信通道，这对于因渐冻症（ALS）或中风等疾病而丧失说话或打字能力的患者尤为重要。目前高性能的 BCI 通常需要通过侵入式手术将电极直接植入大脑，存在显著的医疗风险。EEG 和 MEG 等非侵入式方法无需手术即可透过头骨记录脑信号，但头骨会严重衰减信号，使得高精度解码极为困难。Brain2Qwerty v2 通过将高分辨率 MEG 传感与现代深度学习及语言模型相结合，突破了这一限制。

**标签**: `#Brain-Computer Interface`, `#Meta AI`, `#Deep Learning`, `#Neuroscience`, `#Frontier Tech`

---

<a id="item-7"></a>
## [华为在 HDC 2026 上开源盘古 2.0 模型，参数量达 505B](https://t.me/zaihuapd/42259) ⭐️ 9.0/10

在 2026 华为开发者大会上，华为发布了 openPangu 2.0 开源大语言模型系列，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，均支持 512K 上下文窗口。该模型原生适配华为昇腾算力架构和鸿蒙生态系统，计划从 6 月 30 日起分阶段开源包括预训练代码在内的七大组件。 发布拥有 505B 参数和超长 512K 上下文窗口的开源模型，是对西方 AI 实验室主导地位的最重大挑战之一，尤其是该模型深度集成了华为国产昇腾芯片和鸿蒙系统。余承东大胆宣称盘古将从中国第一走向世界第一，彰显了华为在美国半导体制裁下构建自主可控、具备全球竞争力 AI 生态系统的雄心。 openPangu 2.0 系列包括 505B 参数的 Pro 模型和更高效的 92B 参数 Flash 模型，两者均支持 512K token 上下文窗口，可处理超长文档。余承东在主题演讲中坦言，华为将大量算力分配给了国内其他企业使用，自身保留的数量很有限，但他同时强调，在全中国乃至全世界都不了解大模型时，华为就率先推出了盘古大模型。

telegram · @zaihuapd · Jun 30, 06:01

**背景**: 华为盘古大语言模型的推出时间远早于当前的 AI 热潮，盘古 3.0 已于 2023 年 7 月的 HDC 大会上发布，并针对金融、制造、矿山、气象等企业级领域进行了定制。盘古架构采用三层设计：L0 基础模型、L1 行业定制模型和 L2 场景化模型。华为昇腾 AI 芯片，包括最新推出的算力达 1.56 PFLOPS 的 950PR 推理芯片，构成了旨在降低对 Nvidia GPU 依赖的硬件底座，以应对美国出口管制。鸿蒙系统是华为自主研发的分布式操作系统，覆盖手机、平板、电脑和物联网设备，为 AI 部署打造了软硬件垂直整合的生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huawei_PanGu">Huawei PanGu - Wikipedia</a></li>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Open Source`, `#Huawei`, `#Pangu`, `#LLM`

---

<a id="item-8"></a>
## [谷歌发布 Nano Banana 2 Lite 和 Gemini Omni Flash，实现 4 秒出图与 10 秒视频生成](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/) ⭐️ 9.0/10

谷歌发布了其最快、最具成本效益的图像生成模型 Nano Banana 2 Lite（又称 Gemini 3.1 Flash-Lite Image），文本生成图像延迟仅为 4 秒，每 1K 张图像成本为 0.034 美元。同时，公司首次向开发者开放了 Gemini Omni Flash，支持通过文本、图像和视频输入生成视频并进行自然语言编辑，视频输出价格为每秒 0.10 美元。 这些发布代表了多模态生成式 AI 的重大进步，将超低延迟与有竞争力的定价相结合，使高质量媒体生成能够大规模地服务于开发者和消费者。通过整合到谷歌更广泛的生态系统中，包括 AI Studio、Gemini API 以及搜索 AI Mode 等消费端产品，这些模型将在快速发展的生成媒体市场中展开强有力的竞争。 Nano Banana 2 Lite 现已在 Google AI Studio、Gemini API 和 Gemini Enterprise Agent Platform 上开放使用，并计划接入搜索 AI Mode 和 Gemini 应用等消费端产品。Gemini Omni Flash 目前生成 10 秒视频，API 中暂不支持音频参考和场景延展，在视频参考与跨场景角色一致性方面仍存在限制。

telegram · @zaihuapd · Jun 30, 16:14

**背景**: Nano Banana 是谷歌基于 Gemini 驱动的图像生成模型系列，其中 2 Lite 版本基于 Gemini 3.1 Flash-Lite 架构构建，以实现最高速度和效率。Gemini Omni Flash 代表了谷歌向统一多模态模型的推进，能够从任何输入模态创建和编辑视频，将 Gemini 的语言理解能力与生成媒体能力相结合。Gemini Enterprise Agent Platform 是 Vertex AI 的最新演进形态，作为谷歌云构建、部署和扩展 AI 智能体及应用程序的综合平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/">Start building with Nano Banana 2 Lite and Gemini Omni Flash</a></li>
<li><a href="https://deepmind.google/models/gemini-image/flash-lite/">Gemini 3.1 Flash-Lite Image – Nano Banana 2 Lite — Google ...</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-lite-and-gemini-omni-flash-available/">Nano Banana 2 Lite and Gemini Omni Flash available | Google ...</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Google`, `#Gemini`, `#Video Generation`, `#Multimodal Models`

---

<a id="item-9"></a>
## [Anthropic 发布 Claude Sonnet 4.6，编程与计算机使用能力大幅提升](https://t.me/zaihuapd/42277) ⭐️ 9.0/10

Anthropic 发布了 Claude Sonnet 4.6 模型，现已作为 Free 和 Pro 用户的默认版本，提供 1M token 上下文窗口，并在编程、长文本推理及计算机使用能力方面实现显著提升。该模型已在 API 及主流云平台同步上线，定价与前代保持一致。 此次发布代表了前沿 AI 的重要进展，尤其在智能体计算机使用能力方面——该能力允许模型像人类用户一样通过图形界面操作软件。1M token 上下文窗口与更强编程能力的结合，使 Claude Sonnet 4.6 成为开发者构建复杂、长时间运行 AI 智能体应用的有力工具。 该模型的计算机使用能力在 OSWorld 基准测试中取得显著进步，该测试评估多模态智能体在桌面环境中完成导航、编辑和工作流等开放式任务的表现。1M token 上下文窗口于 2026 年 3 月 13 日正式可用，单次请求最多可处理 100 万 token 的输入并生成最多 128k token 的输出。

telegram · @zaihuapd · Jun 30, 17:58

**背景**: 计算机使用是一种新兴的 AI 能力，模型通过用户界面——截取屏幕截图、点击按钮、选择菜单、输入文本——来操作软件，而非仅依赖 API。OSWorld 基准测试于 NeurIPS 2024 上提出，是一个标准化评估环境，用于测试 AI 智能体在跨操作系统桌面环境中的真实任务表现。上下文窗口是指 AI 模型在单次交互中能处理的文本量；1M token 窗口大约相当于数十万单词，使模型能够处理整个代码库、长篇文档或大量对话历史而不会丢失早期上下文信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://os-world.github.io/">OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks ...</a></li>
<li><a href="https://github.com/xlang-ai/OSWorld">GitHub - xlang-ai/OSWorld: [NeurIPS 2024] OSWorld ...</a></li>
<li><a href="https://www.innovatrixinfotech.com/blog/context-windows-explained-1-million-tokens-architecture">1 Million Token Context Window: What It Means for Builders | Innovatrix Infotech</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#AI Agents`, `#Frontier AI`

---

<a id="item-10"></a>
## [Claude Code 被发现在请求中嵌入隐写标记](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

thereallo.dev 的一篇博客文章揭示，Anthropic 的 Claude Code 工具在其发送的请求中隐秘地嵌入了隐写标记，可能用于追踪使用情况和检测未经授权的模型蒸馏。这些隐藏标记是通过对该工具在用户机器上行为的逆向工程被发现的。 这一发现引发了对 API 透明度、用户信任以及 AI 实验室可能采取的隐蔽手段来保护知识产权的严重关切。它还凸显了前沿 AI 提供商（试图防止模型蒸馏）与可能试图复制专有模型的用户之间不断升级的技术军备竞赛。 隐写标记的嵌入方式可以通过逆向工程检测到，一些评论者指出，作为一种隐蔽追踪机制，其实现方式令人惊讶地粗糙。与 OpenAI 的开源 Codex CLI 不同，Claude Code 是一个专有的闭源工具，使得此类隐藏行为更难被审计。

hackernews · kirushik · Jun 30, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 模型蒸馏是将大型、复杂的 AI 模型的知识转移到更小、更高效的模型中的过程，使竞争对手有可能以更低的成本复制专有模型的能力。隐写术是指在其他数据中隐藏信息的做法——在本文语境中，指在文本提示中嵌入不可见或几乎不可见的标记，用于识别 API 请求的来源。Claude Code 是 Anthropic 的代理式编码系统，可在整个代码库中运行，执行多文件更改并自主完成开发任务，这使其成为蒸馏尝试的特别有价值的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://github.com/kovart/invisible-text">GitHub - kovart/invisible-text: Detect, replace, and clean ...</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些用户认为，无论出于何种商业理由，Anthropic 对追踪行为缺乏透明披露都是不可接受的；而另一些人则认为，这种隐写术明显是针对进行模型蒸馏的中国公司，不会损害普通开发者。多位评论者指出其实现方式出人意料地粗糙，一些人则主张将 Codex CLI 等开源替代方案或本地 AI 模型作为更值得信赖的选择。

**标签**: `#AI`, `#Anthropic`, `#Steganography`, `#AI Safety`, `#Model Distillation`

---

<a id="item-11"></a>
## [Anthropic 推出 Claude Science，面向科学研究的 AI 工作台](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 推出了 Claude Science，这是一款可定制的 AI 研究工作台，集成了科学家最常用的工具、软件包、数据库和计算资源。该产品运行本地服务器并提供基于浏览器的 Web UI，使其能够在制药公司等高度封闭的企业和机构环境中安全运行。 这代表了前沿 AI 实验室向科学研究和数据科学市场的重大进军，直接解决了历史上阻碍 AI 在制药和生物技术领域应用的数据安全难题。通过实现与机构高性能计算集群的安全集成并生成可审计的研究成果，Claude Science 有望从根本上简化计算生物学、化学和数据密集型科学学科中的复杂研究流程。 其架构与 Anthropic 的其他产品（如 Claude Code）显著不同，它运行一个本地服务器，由基于浏览器的 UI 进行连接，而不是将 UI 与特定主机紧密耦合。这种设计选择专门针对禁止将外部设备直接连接到敏感源数据的环境，同时仍然提供对机构计算集群和计算工具的访问。

hackernews · lebovic · Jun 30, 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 企业科学研究中的 AI 应用，尤其是在制药领域，一直受到严格的数据治理和安全要求的严重限制，这些要求阻止了将专有数据发送到基于云的 API。本地服务器架构通过在机构自身的安全网络内运行来解决这一问题，使 AI 能够访问内部数据库和高性能计算（HPC）集群，而数据不会离开本地。这种方法使 AI 工具能够参与计算生物学和药物发现等敏感工作流程，同时保持合规性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://www.reuters.com/science/anthropic-unveils-claude-science-ai-platform-scientific-research-2026-06-30/">Anthropic unveils 'Claude Science' for scientific research</a></li>
<li><a href="https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/">Claude Science is Anthropic’s newest flagship product</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了巧妙的本地服务器架构是打入高度封闭的制药环境的战略举措，在这些环境中通常禁止直接数据访问。一位计算生物学家在基于 RNAi 的生物农药设计上对其进行了测试，指出它的表现像一个天真的博士一年级学生，但成功完成了任务，并在受到批评时认识到了自身的局限性。一些用户对该产品严重偏向数据科学（pandas、图表、Jupyter）而非更广泛的科学应用表示了轻微的失望，尽管他们承认了 HPC 集群集成的价值。

**标签**: `#AI`, `#Anthropic`, `#Scientific Research`, `#Data Science`, `#Bioinformatics`

---

<a id="item-12"></a>
## [Leanstral 1.5 发布：面向 Lean 4 自动定理证明的 119B MoE 模型](https://aihot.virxact.com/items/cmr1frw1802hhslnli0u3w7ch) ⭐️ 8.0/10

Leanstral 1.5 已正式发布，这是一个总参数量 119B、激活参数 6.5B 的混合专家（MoE）模型，专为 Lean 4 中的自动定理证明和自动形式化进行了优化。该模型提供 256k 上下文窗口，免费使用，并支持 Chat Completions、Function Calling、Agents、Structured Outputs、OCR 和 Embeddings 等丰富的 API 功能。 此次发布标志着大规模语言模型在数学推理和形式化验证这一高度专业化领域的重要应用。通过将大规模 MoE 架构与 256k 的超长上下文窗口相结合，Leanstral 1.5 有望大幅加速自动定理证明领域的研究，并降低数学家使用 AI 辅助形式化的门槛。 该模型采用稀疏混合专家架构，在推理过程中仅激活 119B 总参数中的 6.5B，以在性能和计算效率之间取得平衡。它专门针对函数式编程语言和定理证明器 Lean 4（版本 4.26.0）进行了调优，使其能够处理复杂的形式证明工程任务。

rss · AI Hot · Jul 1, 01:46

**背景**: Lean 4 是一种函数式编程语言和交互式定理证明器，允许数学家和计算机科学家以严格的数学方式验证证明。自动形式化是一项具有挑战性的任务，旨在将自然语言数学陈述自动翻译为机器可检查的形式化规范和证明。混合专家（MoE）是一种机器学习技术，它将模型划分为多个子网络（专家），在处理任何给定输入时仅激活部分专家，从而实现大模型的高效扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/theorem_proving_in_lean4/">Theorem Proving in Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autoformalization">Autoformalization</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>

</ul>
</details>

**标签**: `#Automated Theorem Proving`, `#Large Language Models`, `#Auto-formalization`, `#Mistral AI`, `#AI Reasoning`

---

<a id="item-13"></a>
## [Etched 推理加速器芯片 Sohu 完成流片，获 8 亿美元融资和超 10 亿美元订单](https://aihot.virxact.com/items/cmr1flg1j02ffslnlxsw3ru2c) ⭐️ 8.0/10

AI 芯片初创企业 Etched 宣布其专为 Transformer 架构设计的推理加速器芯片 Sohu 已完成 A0 步进流片，采用台积电 N4P 制程工艺。该公司同时获得了 8 亿美元的 B 轮融资和超过 10 亿美元的客户订单，首批机架产品预计于 2026 年夏天出货。 Sohu 代表了一种押注：将 Transformer 架构直接固化到芯片中，可以在 AI 推理工作负载上大幅超越通用 GPU。如果成功，这种方法将显著降低运行万亿参数稀疏 MoE 模型的成本和能耗，并挑战 Nvidia 在 AI 算力基础设施领域的主导地位。 Sohu 芯片的数学模块电压比大多数竞品低 50%以上，能够以超过 80%的算力效率运行 1T 规模的稀疏 MoE 模型。该芯片采用片上 SRAM 与片外 HBM 相结合的缓存设计，配合高带宽互联技术，兼顾低延迟与大容量，解决了竞品芯片在高负载下因发热降频导致实际吞吐量不足理论峰值一半的问题。

rss · AI Hot · Jul 1, 01:21

**背景**: 流片（Tape-out）是芯片设计的最终步骤，即将完成的光掩模发送给制造商进行生产，A0 步进是首个物理版本。稀疏混合专家模型（Sparse MoE）是一种将模型扩展到海量参数（如万亿级）的架构，但每个 token 只激活部分专家网络，因此比密集模型更具计算效率。Etched 的 Sohu 是一种专用集成电路（ASIC），将 Transformer 特定的运算直接硬编码到芯片中，而通用 GPU 则需要处理多样化的计算任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://startupfortune.com/etched-bets-800-million-that-transformer-silicon-will-outlast-the-gpu-era/">Etched bets $800 million that transformer silicon will ...</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://anysilicon.com/tapeout/">What is Tapeout ? - AnySilicon</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#AI Infrastructure`, `#Inference Accelerator`, `#Hardware`, `#Etched`

---

<a id="item-14"></a>
## [特斯拉首台量产 Cybercab 无人驾驶电动车在奥斯汀开启工程测试](https://36kr.com/newsflashes/3876435817000964?f=rss) ⭐️ 8.0/10

特斯拉已正式在美国得克萨斯州奥斯汀启动其首台量产版 Cybercab 无人驾驶电动车的工程测试。这标志着 Cybercab 从 2024 年 10 月首次亮相的概念原型车，正式进入量产实车在真实环境中进行验证的阶段。 由行业巨头对专用 Robotaxi 进行实车测试，标志着具身智能（Embodied AI）系统向真实世界部署迈出了关键里程碑。这释放了全无人驾驶商业化落地的实质性进展信号，有望深刻重塑城市出行方式以及更广泛的自动驾驶产业格局。 Cybercab 是一款专为全自动驾驶设计的双座车辆，其最大特点是取消了方向盘和踏板，完全依赖特斯拉的自动驾驶技术。尽管此次工程测试是重要进展，但在大规模推出商业 Robotaxi 服务之前，特斯拉仍需克服重大的技术和监管障碍。

rss · 36kr · Jul 1, 01:54

**背景**: 特斯拉 Cybercab 是一款专用的自动驾驶车辆，旨在构成特斯拉未来 Robotaxi 网络的核心。它依赖于特斯拉纯视觉的完全自动驾驶（FSD）架构，该架构利用先进的神经网络处理实时摄像头数据，这与使用激光雷达的竞争对手有所不同。这一项目代表了具身智能的一项重要应用，即人工智能被嵌入物理机器中，以自主感知、导航并与物理世界进行交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi - Tesla</a></li>

</ul>
</details>

**标签**: `#Autonomous Vehicles`, `#Tesla`, `#Robotaxi`, `#Embodied AI`, `#Self-Driving`

---

<a id="item-15"></a>
## [Anthropic 获美政府批准，恢复 Mythos 5 模型对关键基础设施的部署](https://t.me/zaihuapd/42260) ⭐️ 8.0/10

6 月 27 日，美国政府通知 Anthropic，其最强网络安全模型 Mythos 5 可重新部署给一批运营和守卫美国关键基础设施的组织。Anthropic 正在迅速为这些组织恢复访问权限，同时继续与政府协商，争取扩大 Mythos 5 的适用范围并恢复相关 Fable 5 模型的访问。 此次批准标志着 AI 治理领域的一个重要里程碑，展示了被认定为过于强大而不宜无限制发布的前沿 AI 模型，如何在政府监管下被选择性部署用于国家安全目的。这为公私合作管理先进 AI 能力以保护关键基础设施树立了先例。 Mythos 5 是一个拥有 10 万亿参数的模型，是 Anthropic 迄今发布的最大模型，专门针对网络安全工作流程；而 Fable 5 是基于 Mythos 架构的模型，专为自主知识工作和编程设计，具备 100 万 token 的上下文窗口。自 6 月 12 日起访问受限后，Anthropic 一直与美国政府进行谈判，该公司此前也曾表示这些模型过于强大，不宜无限制部署。

telegram · @zaihuapd · Jun 30, 07:04

**背景**: Anthropic 开发的 Mythos 5 和 Fable 5 模型是其前沿 AI 产品线的一部分，其中 Mythos 5 专注于网络安全应用，Fable 5 则专为高级知识工作和编程任务设计。此前，美国政府出于对其能力的担忧，曾命令 Anthropic 撤销某些用户（包括外国公民）对这些模型的访问权限。这一事件凸显了 AI 快速发展与国家安全考量之间日益加剧的紧张关系，各国政府正在努力解决如何监管那些可能被用于防御性和进攻性网络操作的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aichief.com/news/anthropic-relaunches-mythos-5/">Anthropic Relaunches Mythos 5</a></li>
<li><a href="https://smartchunks.com/anthropic-claude-mythos-5-10-trillion-parameters/">Anthropic ’s 10-Trillion-Parameter Claude 5 Pressures... | Smart Chunks</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Cybersecurity AI`, `#AI Governance`, `#Critical Infrastructure`, `#AI Deployment`

---