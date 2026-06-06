---
layout: default
title: "Horizon Summary: 2026-06-06 (ZH)"
date: 2026-06-06
lang: zh
---

> From 115 items, 6 important content pieces were selected

---

1. [AI 简报：Anthropic、Google 和阿里巴巴发布重大进展](#item-1) ⭐️ 9.0/10
2. [Anthropic 呼吁全球放缓前沿 AI 开发](#item-2) ⭐️ 9.0/10
3. [谷歌与 SpaceX 签署月付 9.2 亿美元算力租赁协议，涵盖 11 万块英伟达 GPU](#item-3) ⭐️ 8.5/10
4. [Google 发布 QAT 优化的 Gemma 4 模型，助力端侧推理](#item-4) ⭐️ 8.0/10
5. [Makora AI 推出顺序蒙特卡洛推测解码方法](#item-5) ⭐️ 8.0/10
6. [iOS 27 版 Siri 大升级：屏幕感知、跨应用操作与独立应用](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 简报：Anthropic、Google 和阿里巴巴发布重大进展](https://x.com/rohanpaul_ai/status/2063043429425381848) ⭐️ 9.0/10

Anthropic 披露 Claude 现在编写了其 80% 的新生产代码，标志着大规模 AI 辅助编程的重要验证。Google 通过 LLM 规划与逐步验证方法，将形式数学求解性能从不到 10% 提升至 70%，同时开源了多模态 Gemma 4 12B 模型。阿里巴巴发布了 Qwen3.7-Plus，这是一款支持文本、图像和视频输入的闭源多模态模型，定价为每百万 token 输入 $0.40 / 输出 $1.60。 这些进展共同表明，前沿 AI 实验室正在编码自动化、数学推理和多模态智能等多个关键维度上同时取得快速突破。Gemma 4 12B 等开源模型与 Qwen3.7-Plus 等极具竞争力的定价模型相结合，正在加剧竞争并推动强大 AI 能力的普及。 Gemma 4 12B 采用无编码器的统一架构，通过轻量级线性层将图像块直接投影到 LLM 的嵌入空间中，使其能够在消费级 16GB GPU 上本地运行，同时支持音频和视频分析。Qwen3.7-Plus 提供 100 万 token 的上下文窗口和最大 65,536 token 的输出长度，在 Artificial Analysis 智能指数上得分 53，远高于同类模型 23 的平均水平。

rss · AI Hot · Jun 5, 23:40

**背景**: 形式数学推理要求 AI 系统用 Lean4 等语言生成可机器验证的证明，这比生成自然语言数学解释要困难得多。Gemma 是 Google 面向开发者的开源权重 AI 模型系列，Gemma 4 代表了具备原生多模态能力的最新一代。Qwen 是阿里云的旗舰大语言模型系列，Qwen 3.7 代是其最新迭代，包含纯文本和多模态两种变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12 B</a></li>
<li><a href="https://qwen3lm.com/qwen3.7-plus/">Qwen 3 . 7 Plus : The Balanced Multimodal Flagship | Qwen 3 . 7</a></li>
<li><a href="https://artificialanalysis.ai/models/qwen3-7-plus">Qwen 3 . 7 Plus - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**标签**: `#Frontier AI`, `#LLM`, `#Multimodal`, `#AI Coding`, `#Mathematical Reasoning`

---

<a id="item-2"></a>
## [Anthropic 呼吁全球放缓前沿 AI 开发](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 9.0/10

Anthropic 发布了一篇题为《When AI Builds Itself》的博客文章，呼吁全球主要 AI 实验室建立协调的、可验证的机制来放缓或暂时暂停前沿 AI 开发，理由是递归自我改进的迫近风险。该提议以 INF 条约等军控协议为蓝本，坚持多边可验证的暂停而非单方面暂停，但在华盛顿和硅谷均遭到显著质疑。 这是来自顶级前沿 AI 实验室最引人注目的治理提案之一，直接针对 AI 系统自主自我改进超越人类监管的生存性风险。它引发的辩论——AI 安全倡导者与将其视为竞争策略的人之间的对立——将影响全球 AI 监管的未来以及中美之间的战略平衡。 Anthropic 承认其已将越来越多的 AI 开发工作委托给 AI 系统自身完成，加速了研发进度，使递归自我改进成为近期而非理论性的担忧。该提案发布之际，Anthropic 刚以近万亿美元估值完成融资并提交了 IPO 保密文件，批评者因此质疑其呼吁的时机与动机。

telegram · @zaihuapd · Jun 5, 03:00

**背景**: 递归自我改进（RSI）是指 AI 系统重写自身代码以增强能力的过程，可能引发智能爆炸，导致超越人类控制的超级智能。前沿 AI 模型是目前开发中最先进、最强大的 AI 系统，2026 年的竞争格局已从双雄争霸扩展到包括 OpenAI、Google、Anthropic 等多家公司。暂停 AI 开发的理念已得到 Pause AI 等草根运动的倡导，但迄今尚未达成任何具有约束力的国际政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://nairametrics.com/2026/06/05/anthropic-calls-for-coordinated-mechanism-to-pause-ai-development/">Anthropic calls for coordinated mechanism to pause AI development</a></li>

</ul>
</details>

**社区讨论**: 该提案在华盛顿和硅谷引发了尖锐批评，怀疑者认为 Anthropic 夸大风险，借安全之名打压竞争对手。批评者还警告放缓研发可能让中国获得战略优势，而 AI 安全的支持者则认为这一呼吁是对日益自主的系统进行负责任治理的必要且迟来的举措。

**标签**: `#AI Safety`, `#Anthropic`, `#AI Governance`, `#Recursive Self-Improvement`, `#AGI`

---

<a id="item-3"></a>
## [谷歌与 SpaceX 签署月付 9.2 亿美元算力租赁协议，涵盖 11 万块英伟达 GPU](https://www.ithome.com/0/960/770.htm) ⭐️ 8.5/10

谷歌与 SpaceX 签署了一项多年期云计算合作协议，从 2026 年 10 月至 2029 年 6 月，谷歌每月向 SpaceX 支付约 9.2 亿美元（约合 62.46 亿元人民币），租用至少 11 万块英伟达 GPU 及配套 CPU 和内存等算力资源，主要用于高密度 AI 训练和推理场景。 这笔交易凸显了 AI 行业对算力的极端需求，头部企业愿意投入数百亿美元锁定 GPU 产能。对谷歌而言，该合作能缓解算力供应紧张与扩容周期压力；对 SpaceX 而言，则为其 AI 基础设施业务新增了一条重要收入来源，并为其未来的 IPO 提供了有力的叙事筹码。 该协议为期约 33 个月，总金额可能超过 300 亿美元，是迄今公开披露的最大规模 AI 基础设施租赁交易之一。租赁内容包括至少 11 万块英伟达 GPU 及配套的 CPU 和内存，专门面向高密度 AI 训练和推理场景。

rss · IT HOME · Jun 6, 00:08

**背景**: AI 训练是将海量数据输入模型以学习规律的过程，需要巨大的计算能力和 GPU 资源；AI 推理则是使用已训练的模型进行预测的过程，在大规模部署时同样需要庞大的基础设施。高密度 AI 计算是指为极端计算工作负载优化的数据中心配置，通常每个服务器机架需要 30kW 至 50kW 以上的电力供应，并配备先进的散热方案，以支持大量高功耗 GPU（如英伟达 H100）的集群运行。AI 基础设施的激增需求已造成全球性 GPU 短缺，迫使大型科技公司寻求非常规的合作与租赁安排来确保足够的算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gottogpower.com/how-to-tackle-the-challenges-of-ai-driven-high-density-data-centers/">How To Tackle The Challenges Of AI -Driven High - Density Data Centers</a></li>
<li><a href="https://www.digitalocean.com/resources/articles/ai-inference-vs-training">AI Inference vs Training: Key Differences Explained</a></li>
<li><a href="https://www.accio.com/plp/high-density-ai-server-rack-data-center">High Density AI Server Rack Data Center Solutions</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Google`, `#SpaceX`, `#Nvidia GPUs`, `#Cloud Computing`

---

<a id="item-4"></a>
## [Google 发布 QAT 优化的 Gemma 4 模型，助力端侧推理](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) ⭐️ 8.0/10

Google 发布了经过量化感知训练（QAT）优化的 Gemma 4 模型版本，包括 2B 和 12B 变体，使其能够在手机和笔记本电脑上高效进行本地推理，并显著降低内存占用。Q4_0 量化后的 Gemma 4 12B 模型仅需 6.7GB 显存，可轻松运行在消费级硬件上。 此次发布直接解决了 AI 部署中最大的瓶颈之一——在消费级硬件上本地运行高性能模型，而无需依赖云端 API。它使隐私保护、低延迟的边缘 AI 应用成为可能，对于实时场景、离线使用以及对数据安全敏感的组织尤为关键。 QAT 模型支持包括文本、音频和图像在内的多模态输入，其中 2B 模型在 LiteRT 格式下仅重 3.2GB。Q4_0 量化的 12B 模型需要 6.7GB 显存，确认可在 16GB 设备上运行，但这同时也意味着只有量化版本——而非完整的 BF16 模型——能在此类硬件上运行。

hackernews · theanonymousone · Jun 5, 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48414653)

**背景**: 量化感知训练（QAT）是一种在训练过程中模拟低精度计算的技术，使模型能够学习补偿因降低数值精度（例如从 16 位 BF16 降至 4 位整数）而带来的信息损失。这与训练后量化（PTQ）形成对比，后者在训练完成后才进行压缩，通常会导致更大的精度下降。Gemma 是 Google 的轻量级开源 AI 模型系列，基于与 Google Gemini 模型相同的研究和技术构建，Gemma 4 支持文本、音频和图像输入，覆盖超过 140 种语言，上下文窗口最高达 256K token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is Quantization Aware Training ? | IBM</a></li>
<li><a href="https://ai.google.dev/gemma/docs">Gemma models overview | Google AI for Developers</a></li>
<li><a href="https://deepmind.google/models/gemma/">Gemma — Google DeepMind</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Gemma 生态系统的快速进展表示了强烈热情，有用户成功在 Mac 上使用 LiteRT 通过 GPU 后端本地运行了这些模型。值得注意的是，一些评论者指出 Unsloth 的替代量化方案在精度上可能比 Google 官方 QAT 版本更接近未量化的 BF16 模型。此外，也有人猜测发布时机——恰好在 Apple WWDC 之前——认为这些模型可能会在 Apple 与 Google 合作改进 Siri 的计划中亮相。

**标签**: `#AI Models`, `#Quantization`, `#On-Device AI`, `#Google Gemma`, `#Edge Computing`

---

<a id="item-5"></a>
## [Makora AI 推出顺序蒙特卡洛推测解码方法](https://x.com/SemiAnalysis_/status/2063063463304253711) ⭐️ 8.0/10

Makora AI 提出了一种新颖的顺序蒙特卡洛（SMC）推测解码方法，用于大语言模型推理，该方法将多个草案 token 并行保持存活，而不是在验证失败时直接丢弃。这种方法从根本上重新思考了传统的拒绝-重试机制，通过维护一组候选 token 序列，可以恢复原本会被浪费的有用部分匹配。 这一创新可以显著提高大语言模型的服务效率，减少标准推测解码中因拒绝草案 token 而造成的计算浪费。如果成功，它将降低大规模 AI 部署的推理延迟和成本，使所有依赖快速 LLM 响应生成的应用受益。 该方法借鉴了顺序蒙特卡洛技术（也称为粒子滤波器），维护一组带权重的粒子（候选序列），并在每一步根据其似然进行重采样。与标准推测解码中位置 k 处的不匹配导致从位置 k 开始的所有 token 被丢弃不同，这种 SMC 方法可以同时分支和传播多个假设，保留部分进展。

rss · AI Hot · Jun 6, 01:00

**背景**: 推测解码是一种用于大语言模型的推理优化技术，它使用一个更小、更快的草案模型来提议多个未来 token，然后由更大的目标模型并行验证。在标准推测解码中，未通过验证的 token 会被拒绝，过程回退到最后一个被接受的 token，这意味着所有花在被拒绝 token 上的计算都被浪费了。顺序蒙特卡洛（SMC）方法是一族蒙特卡洛算法，常用于贝叶斯推理和信号处理，通过随时间演化一组带权重的粒子来近似概率分布。通过将 SMC 与推测解码相结合，Makora AI 旨在将草案 token 选择过程视为一个概率推理问题，其中可以同时探索和优化多条候选路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/looking-back-at-speculative-decoding/">Looking back at speculative decoding - Google Research</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Particle_filter">Particle filter - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Speculative Decoding`, `#Sequential Monte Carlo`, `#AI Optimization`, `#Machine Learning`

---

<a id="item-6"></a>
## [iOS 27 版 Siri 大升级：屏幕感知、跨应用操作与独立应用](https://www.ithome.com/0/960/782.htm) ⭐️ 8.0/10

彭博社马克·古尔曼报道，苹果 iOS 27 将带来大幅升级的 Siri，具备屏幕感知、跨应用任务执行、个人上下文理解以及图像生成和多轮对话等完整聊天机器人功能。Siri 还将拥有独立应用并驻留在灵动岛中，预计于 2026 年 6 月 8 日在 WWDC 上预览。 此次升级将 Siri 从基础语音助手转变为能够理解屏幕内容、跨应用串联任务并访问深度个人数据的完整 AI 智能体，使其成为在数十亿苹果设备上与 ChatGPT 和 Claude 竞争的原生对手。Siri 与 iOS 硬件的深度整合和本地数据访问权限赋予了它第三方聊天机器人难以复制的结构性优势。 iOS 27 的 Siri 将支持接入 ChatGPT、Claude 和 Gemini 等第三方 AI 模型，用户可为 Siri、书写工具和图像生成功能设置默认服务。在隐私方面，苹果采用本地加私有云的混合方案，但部分请求可能通过 Google Cloud 调用授权版 Gemini 模型处理，用户可设置在 30 天等间隔后自动删除 Siri 聊天记录。

rss · IT HOME · Jun 6, 01:41

**背景**: 端侧 AI（On-Device AI）是指直接在移动设备硬件上运行大语言模型而无需连接云端，具有低延迟、更强隐私保护和离线可用等优势。灵动岛是苹果在 iPhone 14 Pro 上引入的屏幕顶部交互区域，可动态扩展以显示提醒、后台活动和系统通知。AI Agent 技术在 2026 年快速发展，正从被动工具调用迈向具备多模态感知和跨应用任务执行能力的自主多步决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/699195496">大模型端侧部署(On-Device AI) - 知乎</a></li>
<li><a href="https://juejin.cn/post/7152403379262586916">产品经理必学！ 灵 动 岛 产品 设 计 规范01.iPhone14Pro...</a></li>
<li><a href="https://blog.csdn.net/qq_39914918/article/details/160878221">2026年AI Agent技术最新进展：从工具调用到自主决策的范式跃迁_agent...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri`, `#AI Agents`, `#On-Device AI`, `#iOS`

---