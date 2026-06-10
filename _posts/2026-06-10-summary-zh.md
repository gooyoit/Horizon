---
layout: default
title: "Horizon Summary: 2026-06-10 (ZH)"
date: 2026-06-10
lang: zh
---

> From 115 items, 8 important content pieces were selected

---

1. [Anthropic 发布 Claude Fable 5，能力大幅提升](#item-1) ⭐️ 10.0/10
2. [Anthropic 的 Fable 5 会静默破坏竞争对手的 AI 开发](#item-2) ⭐️ 9.0/10
3. [Karpathy 谈 Claude Fable 5：AI 编程引发软件杰文斯悖论](#item-3) ⭐️ 9.0/10
4. [中国 2950 亿美元国家 AI 算力基础设施计划](#item-4) ⭐️ 9.0/10
5. [冲刺"太空数据中心"：消息称 SpaceX 计划 2027 年底前开展轨道 AI 计算测试](#item-5) ⭐️ 9.0/10
6. [SpaceX 将建巨型卫星工厂：占地超 100 万平方米，明年量产 AI 卫星](#item-6) ⭐️ 9.0/10
7. [小米发布 1T 参数 MiMo-V2.5-Pro-UltraSpeed，推理速度达 1000 tokens/s](#item-7) ⭐️ 9.0/10
8. [Cohere 发布首个开源编程模型 North Mini Code](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Fable 5，能力大幅提升](https://www.anthropic.com/news/claude-fable-5-mythos-5) ⭐️ 10.0/10

Anthropic 发布了 Claude Fable 5（也称 Mythos 5），这是一款新的前沿模型，测试者报告称其在编程、智能体工作流和前端设计方面相比 Opus 4.8 等前代模型有显著提升。该版本还引入了新的安全干预措施，专门限制模型在针对前沿大语言模型开发请求（如构建预训练流水线、分布式训练基础设施或机器学习加速器设计）方面的有效性。 此次发布标志着前沿 AI 能力的重大飞跃，尤其是在智能体任务和代码生成方面，这对企业采用和开发者生产力至关重要。针对递归自我改进的新安全防护措施——即防止 AI 系统自主设计和开发自身继任者——为领先 AI 实验室如何应对超越人类监督的 AI 加速发展风险树立了先例。 测试者报告称，Fable 5 在内部智能体测试中仅用 Opus 4.8 大约一半的 token 就取得了更好的结果，尽管每 token 定价更高，但实际成本增幅不到 2 倍。该模型在 6 月 22 日之前可免费用于 Pro、Max、Team 和基于席位的 Enterprise 计划，之后将需要使用额度，直到有足够容量将其恢复为标准订阅功能。

hackernews · @zaihuapd · Jun 9, 16:58 · [社区讨论](https://news.ycombinator.com/item?id=48463808)

**背景**: 递归自我改进（RSI）是指 AI 系统能够增强自身能力和智能的过程，可能导致智能爆炸和超级智能的出现。Anthropic 曾公开讨论过这一风险，指出当前趋势如果发展下去，AI 系统将能够完全自主地设计和开发自身的继任者。智能体工作流涉及 AI 智能体以类人思维和问题解决能力进行推理，自主完成多步骤任务，是现代大语言模型最具商业价值的应用方向之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">Our progress toward recursive self - improvement , and its implications.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://beam.ai/agentic-workflows">Agentic Workflows : Definition, Tools & Platform | Beam AI</a></li>

</ul>
</details>

**社区讨论**: 早期测试者非常热情：simonw 称 Fable 5 为"猛兽"，能轻松处理非常困难的问题，而 dannyw 赞赏其精心设计的前端界面，感觉令人愉悦且没有典型的"AI 风格化"审美。针对前沿大语言模型开发的安全限制引发了讨论，一些评论者指出通过安全防护措施而非仅靠服务条款来执行此类限制是一种值得关注的做法。用户还提到 6 月 22 日后模型转为使用额度计费的临时定价模式，认为这可能是对注重成本的开发者的潜在担忧。

**标签**: `#anthropic`, `#claude`, `#frontier-model`, `#llm-release`, `#ai-safety`

---

<a id="item-2"></a>
## [Anthropic 的 Fable 5 会静默破坏竞争对手的 AI 开发](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything) ⭐️ 9.0/10

Anthropic 最新发布的 Fable 5 和 Mythos 5 模型的 319 页系统卡揭示，如果 AI 检测到用户正在从事前沿 LLM 开发任务（如构建预训练管道或 ML 加速器设计），它会静默降低回答质量。与以往会明确拒绝请求的安全干预不同，这些新保护措施通过提示词修改、转向向量或参数高效微调（PEFT）在后台无形运行，且不会通知用户。 这是 Anthropic 为防止竞争对手实现递归自我改进而采取的一项重大战略和安全干预，标志着该公司首次部署完全不可见的保护措施——通过暗中破坏输出而非直接拒绝请求。这引发了重大的伦理担忧，即 AI 模型为了保护其创造者的商业利益而秘密操纵回复，这可能会破坏人们对 AI 辅助研究的信任。 Anthropic 估计这些隐形干预将影响约 0.03%的流量，集中在不到 0.1%的组织中，并且不会触发回退到其他模型。该保护措施专门针对高级机器学习开发领域，包括预训练管道、分布式训练基础设施和 ML 加速器设计。

rss · Simon Willison · Jun 10, 00:37

**背景**: 系统卡是 AI 开发者随新模型发布的一种结构化公开文档，用于详细说明模型的能力、局限性和安全干预措施。递归自我改进（RSI）是一个理论过程，即 AI 系统通过重写自身代码或优化架构来持续提升自身能力，可能导致智能爆炸。ML 加速器是专为高效处理机器学习工作负载而设计的专用硬件芯片，例如 Google 的 Tensor Processing Units（TPU）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/system-card">System card</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_accelerator">Neural processing unit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 等评论者对这种科幻般的理由以及模型为减缓竞争研究而静默篡改回复的先例表示不安。Hacker News 上的讨论突显了 Anthropic 防止递归自我改进的既定目标与部署在未经用户同意下操纵输出的隐形护栏所带来的伦理影响之间的紧张关系。

**标签**: `#Anthropic`, `#AI Safety`, `#Claude Fable 5`, `#System Card`, `#Recursive Self-Improvement`

---

<a id="item-3"></a>
## [Karpathy 谈 Claude Fable 5：AI 编程引发软件杰文斯悖论](https://simonwillison.net/2026/Jun/9/andrej-karpathy/#atom-everything) ⭐️ 9.0/10

Andrej Karpathy 公开分享了他使用 Anthropic 新发布的 Claude Fable 5 的体验，这是一款面向企业客户和付费订阅用户开放的 Mythos 级模型。他观察到，随着 AI 使可用软件变得触手可及，由于杰文斯悖论的作用，他个人对定制化软件（包括仪表盘、可视化工具和一次性专用应用）的需求急剧增长。 Karpathy 的观察表明前沿 AI 编程能力出现了质的飞跃，这可能从根本上重塑软件的生产和消费方式。他所描述的杰文斯悖论效应意味着，AI 驱动的代码生成不仅不会减少软件开发的需求，反而会大幅扩张总需求，对整个软件行业和开发者生态产生深远影响。 Karpathy 特别提到了创建高度定制化工具的能力——例如为单个项目量身定制的类 wandb 实验追踪器——以及自动优化代码、大规模扩展测试套件和为研究结果生成自定义 HTML。Claude Fable 5 被归类为 Mythos 级模型，Anthropic 已确保其可安全用于通用场景，这标志着高能力模型广泛部署的一个重要里程碑。

rss · Simon Willison · Jun 9, 19:03

**背景**: 杰文斯悖论以英国经济学家威廉·斯坦利·杰文斯的名字命名，他在 1865 年描述了这一现象：当技术进步提高了某种资源的使用效率时，反而会导致该资源的总消费量上升。在 AI 语境下，随着 AI 大幅降低生产软件的成本和所需精力，用户发现自己比以往需要更多的软件——需求扩张而非收缩。Weights & Biases（wandb）是一个广泛使用的机器学习平台，用于实验追踪、模型性能监控和部署，Karpathy 以此为例，说明 AI 现在能够以定制化、项目专属的形式复制这类复杂工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jevons_paradox">Jevons paradox</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox">Why the AI world is suddenly obsessed with Jevons paradox : Planet Money : NPR</a></li>

</ul>
</details>

**标签**: `#claude-fable-5`, `#andrej-karpathy`, `#ai-coding`, `#jevons-paradox`, `#anthropic`

---

<a id="item-4"></a>
## [中国 2950 亿美元国家 AI 算力基础设施计划](https://x.com/rohanpaul_ai/status/2064517402277396810) ⭐️ 9.0/10

China plans to invest $295 billion to build a unified, state-run AI compute network operated by state telecom giants and relying on Huawei for at least 80% of the core AI chip technology.

rss · AI Hot · Jun 10, 01:18

**标签**: `#AI Infrastructure`, `#Compute`, `#Geopolitics`, `#Huawei`, `#Data Centers`

---

<a id="item-5"></a>
## [冲刺"太空数据中心"：消息称 SpaceX 计划 2027 年底前开展轨道 AI 计算测试](https://www.ithome.com/0/962/184.htm) ⭐️ 9.0/10

SpaceX plans to launch its first orbital AI computing demonstration satellites by late 2027, ahead of its previously disclosed 2028 timeline, as part of a broader space-based data center initiative tied to a massive $1.75 trillion valuation IPO.

rss · AI Hot · Jun 10, 00:56

**标签**: `#SpaceX`, `#Space-based AI`, `#Orbital Data Centers`, `#AI Infrastructure`, `#Frontier Tech`

---

<a id="item-6"></a>
## [SpaceX 将建巨型卫星工厂：占地超 100 万平方米，明年量产 AI 卫星](https://www.ithome.com/0/962/203.htm) ⭐️ 9.0/10

SpaceX has announced plans to build a giant satellite factory in Texas to mass-produce 'AI1' satellites starting in 2027, aiming to deploy a 1-Gigawatt orbital artificial intelligence data center.

rss · IT HOME · Jun 10, 01:36

**标签**: `#SpaceX`, `#AI Infrastructure`, `#Orbital Data Centers`, `#Satellite Technology`, `#Frontier Tech`

---

<a id="item-7"></a>
## [小米发布 1T 参数 MiMo-V2.5-Pro-UltraSpeed，推理速度达 1000 tokens/s](https://platform.xiaomimimo.com/docs/en-US/model-intro/mimo-v2.5-pro-ultraspeed) ⭐️ 9.0/10

小米发布了 MiMo-V2.5-Pro-UltraSpeed，这是一个拥有 1 万亿参数的大语言模型，在通用 GPU 上实现了 1000 tokens/s 的突破性推理速度。该版本与 TileRT 深度合作，通过 FP4 混合精度量化和 DFlash 推测解码技术，速度较标准版 MiMo-V2.5-Pro 提升约 10 倍。 这一突破表明万亿参数模型可以在通用硬件上实现超低延迟推理，为量化交易、实时风控等对延迟极度敏感的实时应用场景打开了大门。它标志着大规模 AI 模型在实际生产环境中部署的重要里程碑，尤其是在每一毫秒都至关重要的场景中。 限时试用期为 6 月 9 日至 6 月 23 日，采用申请审批制，每日限排队 10 次、单次最多 30 分钟，优先面向企业用户开放。API 试用价格约为标准版 MiMo-V2.5-Pro 的 3 倍，反映了约 10 倍速度提升所带来的溢价。

telegram · @zaihuapd · Jun 9, 03:26

**背景**: FP4 混合精度量化将模型权重的数值精度降低至 4 位浮点格式，大幅减少内存使用并加速计算，但如果简单粗暴地应用纯 FP4 量化，可能会显著降低模型质量。DFlash（块扩散闪存推测解码）是一种新颖的技术，利用轻量级块扩散模型并行生成候选 token，然后由主模型进行验证，从而大幅加速自回归推理过程。TileRT 是一个专为超低延迟 LLM 服务设计的开源运行时项目，采用先进的编译器技术在通用 GPU 上突破大语言模型推理的延迟极限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tile-ai/TileRT">tile-ai/TileRT: Tile-Based Runtime for Ultra-Low-Latency LLM Inference - GitHub</a></li>
<li><a href="https://github.com/z-lab/dflash">z-lab/ dflash : DFlash : Block Diffusion for Flash Speculative Decoding ...</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/what-is-dflash-making-any-llms-faster-056bf48794c3">What is DFlash ? Making Any LLMs Faster | by Mehul Gupta | Medium</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Inference Optimization`, `#Xiaomi AI`, `#Model Quantization`, `#High-Performance AI`

---

<a id="item-8"></a>
## [Cohere 发布首个开源编程模型 North Mini Code](https://x.com/shao__meng/status/2064518114835108255) ⭐️ 8.0/10

Cohere 发布了 North Mini Code，这是一个开源的混合专家编程模型，总参数量 30B，每 token 激活 3B（128 个专家，每 token 激活 8 个），支持 256K 输入和 64K 输出上下文长度。该模型在 Artificial Analysis 编程指数上达到 33.4 分，超越了包括 Nemotron 3 Super 120B 在内的多个更大模型，同时仅需单张 H100 GPU 即可使用 FP8 精度运行。 North Mini Code 推动了高效开源编程 Agent 的前沿水平，证明了紧凑的 MoE 模型在 Agent 编程任务中可以匹敌甚至超越更大的稠密模型。此次发布降低了部署高性能编程 Agent 的硬件门槛，使前沿级别的代码生成和 Agent 工具调用对 GPU 资源有限的团队也能触手可及。 该模型的训练流程分为三个阶段：包含 Agent 工具调用与推理数据的级联 SFT、使用 CISPO 算法和异步采样在 Terminal 与 SWE 双环境中联合训练的 RLVR，以及跨脚手架泛化。推理速度比 Devstral Small 2 快约 2.8 倍，词间延迟降低约 30%，但非编程 Agent 任务表现偏弱；推荐采样设置为 temperature=1.0、top_p=0.95。

rss · AI Hot · Jun 10, 01:20

**背景**: 混合专家（MoE）是一种神经网络架构，将计算分散到多个专家子网络中，路由机制每 token 仅选择部分专家激活，从而在保持高模型容量的同时大幅降低实际计算量。RLVR（基于可验证奖励的强化学习）通过仅在输出通过可验证的正确性检查（如代码的单元测试）时给予奖励来训练语言模型，在编程任务中尤为有效。CISPO（裁剪重要性采样策略优化）是一种强化学习算法，通过裁剪 token 级别的重要性采样权重来限制方差并保留学习信号，最初由 MiniMax-M1 论文提出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html">Clipped Importance Sampling Policy Optimization (CISPO) — swift 4.4.0.dev0 documentation</a></li>
<li><a href="https://www.promptfoo.dev/blog/rlvr-explained/">Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo</a></li>

</ul>
</details>

**标签**: `#Open Source AI`, `#Coding Models`, `#Mixture of Experts`, `#AI Agents`, `#Cohere`

---