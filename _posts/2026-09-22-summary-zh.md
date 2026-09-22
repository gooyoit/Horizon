---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> From 113 items, 9 important content pieces were selected

---

1. [xAI 发布 Grok 4.7，参数量增加 40%，价格不变](#item-1) ⭐️ 9.0/10
2. [马斯克宣布 xAI 发布 Grok 4.7](#item-2) ⭐️ 9.0/10
3. [小米发布并开源 MiMo v2.6 MoE 模型，附带实时 RL 训练仪表盘](#item-3) ⭐️ 8.0/10
4. [Jev introduces a new shape of LLM - System One, aka Decision Models](#item-4) ⭐️ 8.0/10
5. [Alexandr Wang 透露 Meta 的 muse 项目已研发多时](#item-5) ⭐️ 8.0/10
6. [FuriosaAI 披露第三代 AI 推理加速器规格：算力与带宽均提升 32 倍](#item-6) ⭐️ 8.0/10
7. [小鹏推送 XOS 6.3.0，第二代 VLA 号称实现 4D 时空理解](#item-7) ⭐️ 8.0/10
8. [Meta 发布 A-MLE 智能体框架，自动化广告排序模型的 ML 实验流程](#item-8) ⭐️ 8.0/10
9. [FuriosaAI 披露第三代 AI 推理加速器：算力与带宽均提升 32 倍](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [xAI 发布 Grok 4.7，参数量增加 40%，价格不变](https://x.ai/news/grok-4-7) ⭐️ 9.0/10

xAI 发布了继 Grok 4.6 之后的新旗舰模型 Grok 4.7，专注于编程、智能体任务和知识工作。据报道，该模型参数量比 Grok 4.6 多 40%，但价格保持不变：输入每 token 2 美元，输出每 token 6 美元。 这是一次重要的前沿 AI 模型发布，加剧了与竞争对手（如传闻即将发布的 Anthropic Opus 5.5）的竞争。模型大幅扩大但价格不变，表明 xAI 愿意牺牲利润率来在编程和智能体市场保持竞争力。 用户反映 Grok 4.7 明显更慢，实际使用成本更高，因为它似乎通过消耗更多推理 token 来提升基准测试分数。Simon Willison 的测试发现不同推理强度级别的 token 用量不一致（低和中档用量接近，而 xhigh 反而低于 high），且通过 OpenRouter 和 xAI 直连 API 的结果有所不同。

hackernews · @zaihuapd · Sep 21, 15:50 · [社区讨论](https://news.ycombinator.com/item?id=49788838)

**背景**: Grok 是 xAI 的大语言模型系列，'weights'（权重）是模型训练中学到的内部参数，决定了模型理解和生成文本的能力——权重越多通常能力越强，但推理成本也越高。此次发布比原计划推迟了约两周，且恰好在传闻中 Anthropic Opus 5.5 发布前一天，有人认为这是 xAI 在应对更强竞争时的防御性举措。社区对基准测试普遍持怀疑态度，因为模型可能针对标准化测试优化得分，但在实际编程和智能体工作流中的提升并不成比例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4 . 7 | SpaceXAI</a></li>
<li><a href="https://openrouter.ai/x-ai/grok-4.7">Grok 4 . 7 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://zenmux.ai/x-ai/grok-4.7">x - ai / grok - 4 . 7 | ZenMux AI Model Routing</a></li>

</ul>
</details>

**社区讨论**: 社区评价褒贬不一：有用户认为 Grok 4.6 在编程和智能体工作流中已低于他们的'智能门槛'，而 4.7 更慢更贵，实际提升不明朗。也有人推测发布延期和利润率牺牲说明 xAI 对结果不满意，并预期 Opus 5.5 会全面超越它。较乐观的声音则欢迎更快的发布节奏，期待随着团队充分利用其庞大算力，Grok 5 会带来更大飞跃。

**标签**: `#xAI`, `#Grok-4.7`, `#LLM-release`, `#frontier-AI`, `#benchmarks`

---

<a id="item-2"></a>
## [马斯克宣布 xAI 发布 Grok 4.7](https://aihot.news/items/cmuc0cupc0458rots04b8hvfg) ⭐️ 9.0/10

埃隆·马斯克在 X 上发帖宣布发布 xAI 的最新前沿模型 Grok 4.7。最初的公告中并未包含技术细节、基准测试分数或可用性信息。 xAI 发布新的前沿模型直接关系到各大顶级 AI 实验室之间的竞争，可能改变推理、编程和智能体能力方面的排行榜格局。关注前沿 AI 进展的开发者、企业和研究者都在等待基准测试结果和 API 可用性信息。 这次公告极为简短——只有一条帖子，没有附带模型卡、基准测试结果、定价或发布时间表。在 xAI 发布官方文档之前，读者应将其具体能力视为未经证实的信息。

rss · AI Hot · Sep 22, 01:23

**背景**: Grok 是 xAI 的大语言模型系列，以较少的内容审查著称，并可实时访问 X（Twitter）数据。前沿模型是指特定时期最先进的 AI 系统，通过海量数据训练，在推理、编程、多模态理解等众多任务上达到业界领先水平。由马斯克创立的 xAI 正与 OpenAI、Google DeepMind 和 Anthropic 竞争开发这些尖端系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://hubery.ai/en/chat/grok/">Grok AI Online Free — Grok 4 by xAI — Hubery.ai</a></li>

</ul>
</details>

**标签**: `#xAI`, `#Grok`, `#LLM`, `#model-release`, `#frontier-AI`

---

<a id="item-3"></a>
## [小米发布并开源 MiMo v2.6 MoE 模型，附带实时 RL 训练仪表盘](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米于 9 月 22 日发布并开源 MiMo-V2.6 系列：Flash（总参数 309B / 激活 15B）和 Pro（总参数 1.02T / 激活 42B），均为覆盖编程、电脑操作、3D 和智能体任务的原生全模态模型。尤为罕见的是，团队还公开了实时仪表盘（mimo.xiaomi.com/rl），在耗资数百万美元的强化学习后训练过程中直播奖励曲线、基准分数和累计成本。 这可能是开源模型团队迄今按算力计规模最大的单次强化学习训练之一，其透明度——实时训练遥测加详细技术报告——远超 OpenAI 或 Anthropic 的做法。这进一步强化了中国实验室（DeepSeek、Qwen、小米）以高性价比推动开源前沿模型的趋势。 训练采用 MixRL 联合训练中等难度、可验证的代码与智能体任务，而游戏、3D 和主观评测等难验证或超长任务则单独训练，再通过 MOPD 合并能力。团队还开源了由 MiMo 训练轨迹蒸馏的 Qwen 模型、7000 个多样化环境和完整强化学习框架；Pro-UltraSpeed 版本宣称在同等质量下输出速度最高提升 20 倍。

hackernews · @zaihuapd · Sep 21, 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: MiMo 是小米的大语言模型系列，2025 年 4 月以 MiMo-7B 起步，现已发展为旗舰推理模型线。混合专家（MoE）架构将模型拆分为多个专家子网络，每个 token 只激活其中一部分，因此 MiMo-V2.6-Pro 虽有 1.02T 总参数，每次前向传播仅需激活 42B，大幅提升计算效率。强化学习后训练是用奖励信号在可验证任务（如代码）上打磨模型以提升推理能力的阶段，也是 DeepSeek R1 背后的方法。小米公开实时 RL 仪表盘展示奖励曲线和成本计数，这是西方主要实验室目前都不做的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intelligentliving.co/mimo-v2-6-rl-training/">MiMo-V2.6 RL Training: Xiaomi Livestreams $3M+ AI Run in Real Time</a></li>
<li><a href="https://cho.sh/mini/news/ai-2/xiaomi-mimo-dashboard">Xiaomi publishes a live post-training RL dashboard for MiMo v2.6, showing benchmark scores step by step | cho.sh</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了罕见的训练透明度，有人称实时 RL 仪表盘是极佳的学习与教学工具。讨论还涉及对美国模型更看好高性价比中国模型的情绪，以及关于中国大规模电力和电网建设是否会在 AI 竞赛中带来美国砸钱也难以弥补的长期优势的争论。

**标签**: `#open-source-llm`, `#mixture-of-experts`, `#reinforcement-learning`, `#xiaomi`, `#model-release`

---

<a id="item-4"></a>
## [Jev introduces a new shape of LLM - System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

Simon Willison reviews Jev from TypeSafe AI, a new 'System One' model type that outputs typed floating-point decisions with confidence scores instead of text, offering frontier intelligence at high speed and low cost.

rss · Simon Willison · Sep 21, 23:09

**标签**: `#LLM`, `#AI models`, `#decision models`, `#TypeSafe AI`, `#Simon Willison`

---

<a id="item-5"></a>
## [Alexandr Wang 透露 Meta 的 muse 项目已研发多时](https://aihot.news/items/cmuc0fior0488rotslngjtdai) ⭐️ 8.0/10

Meta 首席 AI 官 Alexandr Wang 公开了一份他在 2025 年 9 月为 Meta 董事会撰写的文档节选，显示 muse AI 项目已研发超过一年，如今正推向公众。他感谢 @natfriedman 和整个团队长期以来的投入。 这标志着 Meta 超级智能实验室一次重要的前沿 AI 发布，是 Wang 领导下 Meta 对 AI 业务全面重构后的首个产品，使其在与 OpenAI、Google 和 Anthropic 的前沿模型竞争中更加激进。 Muse 系列的首个模型 Muse Spark 是原生多模态推理模型，支持工具调用、视觉思维链和多智能体编排，并可通过 Meta Model API 使用。Wang 公开董事会文档的做法较为罕见，让外界得以窥见 Meta 内部的 AI 路线图。

rss · AI Hot · Sep 22, 01:38

**背景**: Alexandr Wang 是 Scale AI 的联合创始人兼前 CEO，于 2025 年 6 月加入 Meta 担任首任首席 AI 官，并领导 Meta 超级智能实验室（MSL）。Meta 将 Muse 定位为其“个人超级智能”愿景的一部分，借助庞大的全球用户群提供个性化的 AI 服务。Muse Spark 被描述为 Meta 模型“扩展阶梯”上的第一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-msl/">Introducing Muse Spark: Scaling Towards Personal ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alexandr_Wang">Alexandr Wang - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Meta`, `#AI models`, `#Alexandr Wang`, `#frontier AI`, `#product launch`

---

<a id="item-6"></a>
## [FuriosaAI 披露第三代 AI 推理加速器规格：算力与带宽均提升 32 倍](https://aihot.news/items/cmubzsljm03mrrotswx4v20vp) ⭐️ 8.0/10

韩国 AI 芯片初创企业 FuriosaAI 公布了与 Broadcom 合作开发的第三代 AI 推理加速器的技术细节，算力达 32 PFLOPS，HBM 内存带宽达 48TB/s，均为第二代 RGND 芯片的 32 倍。 随着大语言模型带来的推理需求爆发式增长，内存带宽和算力密度已成为数据中心经济性的关键瓶颈。32 倍的代际提升使 FuriosaAI 有望成为推理加速器市场上 NVIDIA 的有力挑战者，也表明 AI 基础设施领域的竞争正在加剧。 除了算力和带宽提升 32 倍外，新芯片的 HBM 内存容量达 576GB（为 RGND 的 12 倍），物理尺寸约为上一代的 8 倍，暗示其可能采用多芯片封装或晶圆级设计。

rss · AI Hot · Sep 22, 01:21

**背景**: FuriosaAI 是一家总部位于首尔的初创企业，专注于为数据中心设计高性能、高能效的 AI 加速器（NPU），可应用于大语言模型、生成式 AI 和计算机视觉等负载。其第二代芯片 RGND 是此前的旗舰推理加速器。HBM（高带宽内存）是一种 3D 堆叠内存技术，由于大模型推理往往更多受限于内存带宽而非原始算力，HBM 已成为 AI 芯片的关键组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/005/531.htm">韩 AI 芯片企业 FuriosaAI 披露新一代推理加速器规格：32 倍算力、32 ...</a></li>
<li><a href="https://furiosa.ai/">Homepage — FuriosaAI</a></li>
<li><a href="https://www.163.com/dy/article/L7E0NOMM0511B8LM.html">FuriosaAI披露新一代加速器规格：32倍算力、32倍内存带宽|堆栈|拓扑|...</a></li>

</ul>
</details>

**标签**: `#AI芯片`, `#推理加速器`, `#FuriosaAI`, `#Broadcom`, `#AI基础设施`

---

<a id="item-7"></a>
## [小鹏推送 XOS 6.3.0，第二代 VLA 号称实现 4D 时空理解](https://aihot.news/items/cmubzsljm03mtrots18u5nike) ⭐️ 8.0/10

小鹏汽车开始推送 XOS 6.3.0，搭载第二代 VLA（视觉-语言-动作）系统，官方称其将感知能力从 3D 空间识别升级为 4D 时空理解。新版本首次上车 X-Foresight 预测世界模型（可预判未来 6 秒）以及可记忆前 30 秒世界的 Infini-VLA 长时序架构；第二代 VLA Lite 同步推送，单图灵 Max 车型正式升级。 将时序预测和长时记忆引入量产自动驾驶系统，是具身智能领域的重要进展，弥补了仅对当下场景做反应的系统的关键短板。这也表明中国车企正将世界模型、长上下文记忆等研究级技术（如基于 KV cache 的时序记忆）落地到量产乘用车上。 据报道，Infini-VLA 借鉴大语言模型的 KV cache 技术构建时序记忆，在相同车端算力下实现 30 秒记忆和约 3 倍的响应提速。X-Foresight 可预判未来 6 秒，使系统不再只是识别当前场景几何，而是能预判其他交通参与者的轨迹。

rss · AI Hot · Sep 22, 01:12

**背景**: VLA（视觉-语言-动作）模型将视觉理解、语言推理和控制输出统一在单一策略中，实现可推理、可解释的端到端自动驾驶。世界模型是一类学习驾驶环境演化规律、能够'想象'未来场景的 AI 系统，可提升轨迹预测和决策能力。传统感知系统构建的是 3D 空间快照，缺乏显式的时序推理；加入时间维度（即'4D 时空'）后，车辆可以理解并预判场景随时间的演变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leitech.ai/article/79045">Memory for 30 Seconds + 6-Second Prediction! XPeng Unveils ...</a></li>
<li><a href="https://x.com/ZhihuFrontier/status/2099421488948687031">Zhihu Frontier on X: " Infini-VLA: XPeng Treats the Driving ...</a></li>
<li><a href="https://arxiv.org/abs/2501.11260">[2501.11260] A Survey of World Models for Autonomous Driving World model-based end-to-end scene generation for accident ... Awesome World Models for Autonomous Driving - GitHub Research on World Models for Connected Automated Driving ... GAIA-3: Scaling World Models to Power Safety and Evaluation A Survey of World Models for Autonomous Driving - ADS</a></li>

</ul>
</details>

**标签**: `#autonomous-driving`, `#VLA`, `#world-model`, `#XPeng`, `#embodied-AI`

---

<a id="item-8"></a>
## [Meta 发布 A-MLE 智能体框架，自动化广告排序模型的 ML 实验流程](https://aihot.news/items/cmuby98mu04miro9iti6amw42) ⭐️ 8.0/10

Meta 发布了 A-MLE（Agentic ML Exploration），一个已在其生产环境广告排序模型组合上部署的自主 LLM 智能体系统。该智能体可自动化完整的机器学习迭代循环：提出想法、运行实验、恢复失败任务、比较结果，并在不同模型之间迁移经验。 A-MLE 代表了自主 AI 研究智能体在工业规模的落地，将机器学习进步转化为全球最大广告系统之一的迭代吞吐量问题。这标志着 LLM 智能体不再仅辅助写代码，而是直接驱动生产系统的实验循环。 相关论文将工业级机器学习进步定义为迭代吞吐量问题，但有评论者指出其证据难以推广到 Meta 特定环境之外。A-MLE 是在多个广告排序模型组合上系统性探索机器学习技术，而非孤立地优化单一模型。

rss · AI Hot · Sep 22, 00:42

**背景**: Meta 等公司的广告排序模型是决定展示哪些广告的大规模机器学习系统，需要持续进行实验（特征工程、架构调整、训练改进）来提升效果。传统上这一迭代过程由机器学习工程师手动完成，限制了可测试想法的数量。近期基于 LLM 的智能体研究（如 ML-Agent、MLE-STAR）已探索让 LLM 自主运行机器学习实验，但多数先前工作停留在学术基准而非生产部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.08248">Agentic ML Exploration ( A - MLE ) for Ads Ranking</a></li>
<li><a href="https://www.linkedin.com/posts/dair-ai_another-brilliant-paper-from-meta-this-activity-7503701060239142912-j6Mq">Another brilliant paper from Meta . This one is worth reading if you work...</a></li>
<li><a href="https://www.emergentmind.com/topics/mle-star">MLE -STAR: Agentic AutoML System</a></li>

</ul>
</details>

**社区讨论**: LinkedIn 上的评论者（如 DAIR.AI）认为它将工业级机器学习进步重新定义为迭代吞吐量问题的做法很有说服力，但也提醒其证据在 Meta 环境之外难以推广。

**标签**: `#AI agents`, `#LLM`, `#Meta`, `#autoML`, `#ML experimentation`

---

<a id="item-9"></a>
## [FuriosaAI 披露第三代 AI 推理加速器：算力与带宽均提升 32 倍](https://www.ithome.com/1/005/531.htm) ⭐️ 8.0/10

韩国 AI 芯片初创企业 FuriosaAI 公布了与博通合作开发的第三代 AI 推理加速器规格：采用两颗光罩极限级 2nm 计算裸晶和一颗独立 I/O 裸晶，配备 12 个 48GB HBM4 内存堆栈，算力达 32 PFLOPS，内存容量 576GB，带宽达 48TB/s。该芯片还支持 PCIe Gen7，机架内采用 SUE 全连接拓扑。 这些规格相比上一代 RNGD 芯片在算力和内存带宽上均实现了 32 倍的跨越，使 FuriosaAI 有望在快速增长的 AI 推理市场上与英伟达等巨头竞争。与博通的合作以及 2nm 工艺的选择，展示了初创企业如何借助芯粒设计和尖端制程来挑战行业既有玩家。 该芯片物理尺寸约为第二代 RNGD 的 8 倍，HBM 容量为其 12 倍（576GB 对比约 48GB）。它将计算与 I/O 拆分为独立裸晶，这种芯粒化设计与 AMD、英特尔的服务器芯片类似，并采用 SUE 全连接拓扑实现机架内多芯片扩展。

rss · IT HOME · Sep 22, 01:21

**背景**: FuriosaAI 是一家位于首尔的初创企业，其上一代产品 RNGD（"Renegade"）是一颗已实现量产的数据中心 AI 推理加速器。AI 推理（即运行已训练好的模型生成输出）越来越受内存带宽制约，因此 HBM4 堆栈和 48TB/s 带宽成为下一代加速器设计的核心。将多个裸晶（计算裸晶加 I/O 裸晶）组合的芯粒架构，可以让设计者突破单片光罩极限尺寸，并更具成本效益地混合使用不同工艺节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.ithome.com/tags/FuriosaAI">FuriosaAI _ FuriosaAI 最新动态_IT之家</a></li>
<li><a href="https://aipure.ai/tw/products/furiosaai">FuriosaAI ：評論、功能、價格、指南和替代方案</a></li>

</ul>
</details>

**标签**: `#AI芯片`, `#推理加速器`, `#HBM4`, `#FuriosaAI`, `#AI基础设施`

---