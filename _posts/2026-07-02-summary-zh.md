---
layout: default
title: "Horizon Summary: 2026-07-02 (ZH)"
date: 2026-07-02
lang: zh
---

> From 111 items, 14 important content pieces were selected

---

1. [DeepSeek V4 在 InferenceX 上的部署与推理性能探讨](#item-1) ⭐️ 9.0/10
2. [英伟达 Blackwell 平台将 DeepSeek 推理单 Token 成本降至五分之一](#item-2) ⭐️ 9.0/10
3. [从零构建的合成细胞首次成功生长并分裂](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出基于 x402 协议的加密微交易货币化网关](#item-4) ⭐️ 8.0/10
5. [Anthropic 的 Claude "Fable 5" 引发关于 AI 安全与经济性的激烈讨论](#item-5) ⭐️ 8.0/10
6. [Anthropic 发布 Claude Sonnet 5：更便宜的智能体模型，但升级不均衡](#item-6) ⭐️ 8.0/10
7. [DSpark 与 JetSpec 对比：面向因果一致性的推测解码技术](#item-7) ⭐️ 8.0/10
8. [Safari 技术预览版 247 引入 MCP 服务器，支持 AI 驱动的网页开发](#item-8) ⭐️ 8.0/10
9. [Seedance 2.0 生成逼真的 2000 年代韩国社区生活视频](#item-9) ⭐️ 8.0/10
10. [空中智能初创企业 SPARO 半年内连获四轮数亿元融资](#item-10) ⭐️ 8.0/10
11. [北大孵化「纳开量子」获数千万元种子轮融资，推进中性原子量子计算工程化](#item-11) ⭐️ 8.0/10
12. [快手可灵 AI 将完成 30 亿美元融资，投后估值 180 亿美元](#item-12) ⭐️ 8.0/10
13. [联合国专家组警告：AI 能力进步速度已超过科学认知](#item-13) ⭐️ 8.0/10
14. [Claude Code 2.1.91 被指隐蔽遥测，暗检中国时区与代理](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 在 InferenceX 上的部署与推理性能探讨](https://aihot.virxact.com/items/cmr2ptdtc0a7ssl8zcvrdlly2) ⭐️ 9.0/10

SemiAnalysis 与 InferenceX 团队讨论了 DeepSeek V4 的部署工作，涵盖模型架构变化、全新的 MegaKernel 技术方案，以及在包括华为昇腾 NPU 在内的多种硬件加速器上的初始推理性能。这是业界首次对 DeepSeek 最新前沿模型在多厂商推理环境中的实际表现进行详细技术分析。 DeepSeek V4 是最具影响力的开源前沿模型家族的最新迭代，其在多种加速器上的部署标志着 AI 基础设施正走向硬件无关化。华为昇腾 NPU 的参与尤为重要，因为它证明了在美国出口管制背景下，非 NVIDIA 硬件同样能够有竞争力地运行最前沿的模型。 讨论重点介绍了 MegaKernel——一种端到端 GPU 融合方案，可将整个 LLM 解码步骤编译为单次 kernel 启动，相比传统方法可将推理延迟降低 1.2 至 6.7 倍。DeepSeek V4 系列相比 V3 还引入了关键架构升级，不过不同加速器上的具体基准测试数据在讨论时仍为初步结果。

rss · AI Hot · Jul 1, 23:30

**背景**: DeepSeek 已迅速成为最受关注的 AI 实验室之一，其 V2 和 V3 模型开创了混合专家架构，以显著降低的推理成本实现了前沿级别的性能。MegaKernel 是由斯坦福和 NVIDIA 研究团队提出的最新技术，旨在解决 LLM 推理中的关键瓶颈：每个 token 需要启动大量小型 GPU kernel 所带来的开销。华为昇腾 NPU 系列，尤其是 910C 及后续型号，已成为中国最具可行性的国产 GPU 替代方案，提供专为大规模深度学习工作负载设计的高密度计算和内存带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17">Compiling LLMs into a MegaKernel : A Path to Low-Latency Inference</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-ascend-npu-roadmap-examined-company-targets-4-zettaflops-fp4-performance-by-2028-amid-manufacturing-constraints">Huawei Ascend NPU roadmap examined — company targets 4 ZettaFLOPS FP4 performance by 2028, amid manufacturing constraints | Tom's Hardware</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek -ai/ DeepSeek - V 4 -Pro · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI Infrastructure`, `#Model Inference`, `#SemiAnalysis`, `#Hardware Accelerators`

---

<a id="item-2"></a>
## [英伟达 Blackwell 平台将 DeepSeek 推理单 Token 成本降至五分之一](https://blogs.nvidia.com/blog/inference-software-lowest-token-cost/) ⭐️ 9.0/10

英伟达在 Blackwell 平台上持续优化推理软件栈，仅用一个月时间就将 DeepSeek 模型的单 Token 生成成本降至原先的五分之一。来自 PyTorch 社区的数据显示，在 GB300 离散式部署下，SGLang 引擎的吞吐量从 4 月初的约 2,200 Tokens/秒/GPU 飙升至 6 月的约 11,200 Tokens/秒/GPU，实现了 5 倍增长。 推理成本降低 5 倍从根本上改变了大语言模型的部署经济学，使高性能 AI 服务的成本大幅下降、可及性显著提升。这证明了仅靠软件层面的优化——而非单纯依赖硬件升级——就能带来数量级的性能飞跃，进一步巩固了英伟达作为 AI 基础设施主导者的护城河。 这一性能飞跃得益于多项内核与运行时的深度优化，包括算子融合、显存压缩、量化精度路径、改进的内存预算、可中断计算图支持以及推理稳定性修复。英伟达表示，若后续叠加分解式服务、新浮点精度与多 Token 预测等高级优化技术，系统级吞吐量最高有望提升至 20 倍，同时保持约 50 Tokens/秒的流畅用户交互体验。

telegram · @zaihuapd · Jul 1, 10:36

**背景**: SGLang 是一个开源的大语言模型服务框架，旨在从单 GPU 到大规模分布式集群的各种配置上实现低延迟、高吞吐量的推理。英伟达 Blackwell Ultra（GB300）是一种机架级 AI 计算平台，采用液冷架构，集成了 72 颗 Blackwell Ultra GPU 和 36 颗基于 Arm 架构的 Grace CPU。多 Token 预测是一种新兴技术，模型从共享前缀同时预测多个未来 Token，而非逐个生成，从而加速推理并提升学习效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance serving ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">Designed for AI Reasoning Performance & Efficiency | NVIDIA GB300 NVL72</a></li>
<li><a href="https://medium.com/@himankvjain/accelerating-language-models-with-multi-token-prediction-9f0167232f5b">Accelerating Language Models with Multi - Token Prediction | Medium</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#NVIDIA`, `#Blackwell`, `#Inference Optimization`, `#DeepSeek`

---

<a id="item-3"></a>
## [从零构建的合成细胞首次成功生长并分裂](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/) ⭐️ 8.0/10

由 Kate Adamala 博士领导的研究团队成功创建了一种名为 "SpudCell" 的合成细胞，该细胞能够生长和分裂，克服了合成生物学领域长期存在的瓶颈。其关键创新在于绕过了天然细胞用于分裂的复杂细胞骨架重组过程，转而采用了一种完全不同的机制。 这一成就代表了合成生物学领域的范式转变里程碑，因为细胞分裂此前对完全人工构建的生命体来说是一道不可逾越的障碍。它为可编程的生物制造、先进的药物递送系统，以及深入理解生命的最低需求打开了大门。 该合成细胞利用了从病毒和大肠杆菌中借用的基因组件，这引发了关于手性以及如何为完全从零开始的构建获取同手性氨基酸的有趣问题。值得注意的是，这份长达 190 页的论文手稿曾被《Cell》期刊拒稿，一位审稿人甚至有争议地声称 SpudCell "不是真正的生物学"。

hackernews · defrost · Jul 1, 14:20 · [社区讨论](https://news.ycombinator.com/item?id=48747304)

**背景**: 合成生物学长期以来一直致力于创造最小的人工细胞，其中的里程碑包括 JCVI-syn3.0 细菌细胞——它仅包含 473 个基因，是已知自我复制生物中最小的基因组。尽管之前的突破成功合成了基因组并实现了 DNA 复制，但实现真正的细胞分裂仍然困难重重，因为天然细胞依赖由蛋白质纤维组成的复杂细胞骨架网络来物理性地一分为二。在合成生物学家找到完全绕过细胞骨架需求的新方法之前，从零开始复制这种高度复杂的进化机制一直是一个难以克服的障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jcvi.org/research/first-minimal-synthetic-bacterial-cell">First Minimal Synthetic Bacterial Cell | JCVI</a></li>
<li><a href="https://www.cell.com/cell/fulltext/S0092-8674(21)00293-2">Genetic requirements for cell division in a genomically minimal cell: Cell</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调，该研究方法巧妙地绕过了困扰该领域多年的细胞骨架瓶颈，但也有人指出主要研究者采取了非常规的宣传策略。一位具备技术背景的评论者提出了关于团队如何获取同手性氨基酸的合理疑问，因为基因是从病毒和大肠杆菌中借用的，而非完全从零构建。讨论中还建议参考《Science News》的报道，以获取关于论文被拒和 embargo 策略争议的更客观全面的视角。

**标签**: `#synthetic-biology`, `#frontier-tech`, `#biotech`, `#bioengineering`, `#science`

---

<a id="item-4"></a>
## [Cloudflare 推出基于 x402 协议的加密微交易货币化网关](https://blog.cloudflare.com/monetization-gateway/) ⭐️ 8.0/10

Cloudflare 推出了货币化网关，利用 x402 协议为其全球网络上的任何资源实现基于稳定币的自动化微交易。该网关允许提供商按请求对 API、数据集、网页和 AI 产品进行收费，x402 握手在 Cloudflare 覆盖的 330 多个城市中完成，从而实现极低延迟。 这为自主 AI 智能体独立发现、协商并支付资源访问费用提供了缺失的金融基础设施，无需人工干预或预先配置 API 密钥。借助 Cloudflare 的庞大用户规模来标准化机器原生支付，这有可能最终让长久以来承诺的智能体驱动微交易在商业上变得可行。 x402 协议建立在极少使用的 HTTP 402「需要付款」状态码之上，允许服务器返回支付要求，客户端可自动使用稳定币完成支付。该网关作为 Cloudflare 的扩展功能运行，在边缘节点处理支付握手，因此资源提供商无需自行构建计费或认证基础设施。

hackernews · soheilpro · Jul 1, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=48746914)

**背景**: HTTP 402 是自互联网早期就保留的状态码，含义为「需要付款」，但从未被正式规范，几十年来基本未被使用。x402 协议重新启用了这一状态码作为机器间支付的约定，使 HTTP 服务器能够请求付款，客户端则以可验证的加密货币支付进行响应。随着 AI 智能体变得更加自主，它们需要一种无需人工管理账户、信用卡或 API 密钥即可进行金融交易的方式——由于最低交易成本和手动注册要求，信用卡等传统支付渠道无法有效填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/monetization-gateway/">Announcing the Monetization Gateway : charge for any resource...</a></li>
<li><a href="https://cryptobriefing.com/cloudflare-monetization-gateway-asset-payments/">Cloudflare introduces Monetization Gateway for AI agent...</a></li>
<li><a href="https://shatale.com/blog/what-is-x402-protocol">What Is the x 402 Protocol ? HTTP 402 and Machine-Native... — Shatale</a></li>

</ul>
</details>

**社区讨论**: 社区对这一潜力普遍感到兴奋，许多人指出智能体付费访问的微交易一直是长久以来的梦想，而传统支付渠道永远无法实现。然而，也有人提出了关于实际采用障碍的重大担忧，包括法律合规性（加密支付的发票和增值税问题）、区分机器人流量与人类用户以保留免费体验的困难，以及 Stripe 等现有巨头可能更容易占领这一市场的怀疑态度。

**标签**: `#AI Agents`, `#Microtransactions`, `#Cloudflare`, `#Infrastructure`, `#Crypto`

---

<a id="item-5"></a>
## [Anthropic 的 Claude "Fable 5" 引发关于 AI 安全与经济性的激烈讨论](https://twitter.com/claudeai/status/2072402636813607381) ⭐️ 8.0/10

一条在 Hacker News 上引发高度关注的讨论帖围绕 Anthropic 最新发布的 Claude 模型（被称为 "Fable 5"）展开，激起了关于过于激进的 AI 安全限制、API token 定价的可持续性，以及专有前沿模型权重的物理安全性的讨论。 用户报告称，该模型的安全过滤器会标记无害内容（例如原创哲学写作），使其在某些创意或分析任务中变得"毫无用处"。此外，从固定费率订阅向按使用量计费的 API 定价模式的转变，正迫使开发者重新思考他们的 token 消耗策略。

hackernews · mfiguiere · Jul 1, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=48752030)

**背景**: 像 Anthropic 这样的 AI 实验室采用"对齐"技术来防止模型生成有害内容，但过于严格的过滤器会降低用户体验，这个过程有时被称为"去势"（defanging）。LLM 的经济模型依赖于"token"（文本片段）进行计费，高昂的计算成本使得重度用户的 API 访问变得昂贵。此外，"模型权重"是 AI 系统的核心知识产权；在分布式数据中心中保护它们是一项公认的挑战，因为一旦泄露，专有技术将暴露给竞争对手和敌对势力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rand.org/pubs/research_reports/RRA2849-1.html">Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models | RAND</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/05/01/ai-model-weights-are-the-new-crown-jewels-they-demand-a-new-security-model/">Council Post: AI Model Weights Are The New Crown Jewels. They Demand A New Security Model</a></li>
<li><a href="https://zhaolongzhong.com/blog/llm-token-economies">zhaolongzhong.com/blog/ llm - token - economies</a></li>

</ul>
</details>

**社区讨论**: 用户意见出现分化：一些人认为模型的安全限制使其在实际中毫无用处，而另一些人则辩论，鉴于部署所需的广泛访问权限，真正保护模型权重的可行性有多大。对于向昂贵的 API 定价模式转变，用户也存在明显的不满情绪，同时由于地缘政治姿态和"末日论调"，人们对美国 AI 实验室的信任度普遍下降。

**标签**: `#Anthropic`, `#AI Safety`, `#LLM`, `#AI Security`

---

<a id="item-6"></a>
## [Anthropic 发布 Claude Sonnet 5：更便宜的智能体模型，但升级不均衡](https://aihot.virxact.com/items/cmr2rvrd30aqesl8zhqheemex) ⭐️ 8.0/10

据报道，Anthropic 发布了 Claude Sonnet 5，将其定位为运行 AI 智能体的更具成本效益的模型，每 token 价格低于 Opus。然而，该模型的改进并不均衡，在 CyberGym 基准测试上表现不如 Sonnet 4.6，且每任务成本比 Opus 4.8 高约 15%，比 Sonnet 4.6 高出 2 倍。 此次发布凸显了每 token 定价与实际智能体任务成本之间日益增长的矛盾，更低的 token 费率并不一定意味着复杂智能体工作流的整体开支会减少。不均衡的性能表现也表明，前沿模型的扩展在某些领域（如网络安全任务）可能正在遭遇边际收益递减。 Claude Sonnet 5 在 CyberGym 基准测试上出现了倒退，该测试是一种操作性智能体评估，会将 AI 置于模拟网络安全场景中，而非要求其编写函数或解释概念。另外，Claude Code 被指控自 2.1.91 版本起，通过根据检测到的时区和代理 URL 更改系统提示中的日期格式和 Unicode 变体，对来自中国关联设置的请求进行隐写指纹标记。

rss · AI Hot · Jul 2, 00:30

**背景**: CyberGym 是一种归类于智能体评估的操作型基准测试，它将 AI 模型置于模拟的真实网络安全环境中，而非测试静态编码或解释任务。AI 智能体记忆系统已从简单的检索增强机制发展为完整的数据管理系统，支持在智能体执行过程中进行持久化存储、检索和动态生命周期治理。Claude Code 是 Anthropic 的智能体编码工具，在终端中运行，旨在帮助开发者更快地将想法转化为代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://thereallo.dev/blog/claude-code-prompt-steganography">Claude Code Is Steganographically Marking Requests</a></li>
<li><a href="https://arxiv.org/abs/2606.24775">[2606.24775] Are We Ready For An Agent - Native Memory System ?</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#LLM Release`, `#AI Agents`, `#AI Models`

---

<a id="item-7"></a>
## [DSpark 与 JetSpec 对比：面向因果一致性的推测解码技术](https://aihot.virxact.com/items/cmr2r0ak00aiksl8z2za72kd5) ⭐️ 8.0/10

DSpark 和 JetSpec 两种新型推测解码技术几乎同时出现，都致力于解决轻量级草稿模型在并行提案时面临的因果一致性问题。DSpark 面向高并发场景，通过轻量级马尔可夫校正头与基于置信度的预算控制来优化；JetSpec 则面向低延迟场景，将因果性直接构建进并行草稿头中。 这两种方法代表了突破并行推测草稿中关键瓶颈的最新进展，能够直接提升 LLM 推理吞吐量并降低延迟。它们分别从吞吐量和延迟两个角度解决因果一致性问题，推动了生产环境中高效 LLM 服务的前沿发展。 在 Qwen3-8B 模型和 AIME25 基准测试中，预算为 7 时，DSpark 将接受长度从 DFlash 的 4.07 提升至 5.01。JetSpec 在预算为 16 时接受长度达到 7.23，预算为 128 时达到 9.82，高于同等预算下 DFlash 的 7.34 和 DDTree 的 8.66。

rss · AI Hot · Jul 2, 00:10

**背景**: 推测解码通过使用更小、更快的草稿模型生成初步 token 预测，再由更大的目标模型进行并行验证，从而加速 LLM 推理。DFlash 和 DDTree 等最新进展已从传统的自回归草稿转向使用块扩散模型进行并行草稿，以实现更大的加速。然而，当多个 token 被并行草拟时，确保因果一致性——即后续 token 正确依赖于前面的 token——成为一个重大挑战，这正是 DSpark 和 JetSpec 旨在解决的核心问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2211.17192">Fast Inference from Transformers via Speculative Decoding</a></li>
<li><a href="https://arxiv.org/abs/2602.06036">[2602.06036] DFlash: Block Diffusion for Flash Speculative Decoding</a></li>
<li><a href="https://maloyan.xyz/blog/dflash-ddtree-block-diffusion-speculative-decoding">DFlash and DDTree : 8x Faster LLM Inference ... | Narek Maloyan Blog</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Speculative Decoding`, `#AI Research`, `#Optimization`, `#Causal Consistency`

---

<a id="item-8"></a>
## [Safari 技术预览版 247 引入 MCP 服务器，支持 AI 驱动的网页开发](https://aihot.virxact.com/items/cmr2sx3it0aytsl8zu2s12j8y) ⭐️ 8.0/10

苹果 Safari 技术预览版 247 新增了内置的 MCP（Model Context Protocol）服务器，使 AI 编程智能体能够直接与浏览器的开发者工具交互。配置完成后，AI 智能体可以检查网页、读取控制台日志和网络请求、抓取截图，并与页面元素进行交互，实现自动化调试和测试。 苹果在 Safari 中采用 MCP 标志着该协议获得了重要的行业认可，为 AI 编程智能体与浏览器网页开发工作流之间搭建了桥梁。这将推动跨浏览器兼容性测试、性能分析和可访问性检查的 AI 自动化，大幅加速网页开发生命周期。 MCP 服务器支持的用例包括网站调试、识别 Safari 特有的兼容性问题、性能分析、可访问性审计以及验证页面与 UI 状态。开发者需要先配置 MCP 连接，AI 智能体才能访问这些浏览器开发者工具功能。

rss · AI Hot · Jul 2, 00:04

**背景**: MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 系统（如大语言模型）与外部工具、数据源和服务的集成方式。Safari 技术预览版是苹果的实验性浏览器版本，在正式版 Safari 发布之前提供即将推出的网页技术和开发者工具的早期体验。通过将两者结合，苹果正将 Safari 定位为一款原生支持新兴 AI 驱动开发工具生态的浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://developer.apple.com/safari/technology-preview/">Safari Technology Preview - Safari - Apple Developer</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#MCP`, `#Apple Safari`, `#Web Development`, `#AI Tooling`

---

<a id="item-9"></a>
## [Seedance 2.0 生成逼真的 2000 年代韩国社区生活视频](https://aihot.virxact.com/items/cmr2rem460ak8sl8z05bd14bi) ⭐️ 8.0/10

字节跳动的 AI 视频生成模型 Seedance 2.0 展示了其先进的能力，生成了一段描绘 2000 年代初韩国社区生活的超真实视频。该模型成功模拟了复杂的物理摄像机伪影，包括 DV 摄像机美学、自动对焦搜索、运动模糊以及自然的环境音效。 这次展示意义重大，因为它展现了 AI 视频生成技术在真实感方面的最先进水平，超越了纯净的数字渲染，能够令人信服地复制不完美的模拟时代物理媒介。在复杂的视觉伪影之外还能生成同步的环境音效，代表了多模态 AI 的重大飞跃，模糊了 AI 生成内容与真实档案素材之间的界限。 该视频通过详细的提示词生成，准确地模仿了 2000 年代初 DV 摄像机固有的手持抖动、自动对焦搜索、曝光波动和运动模糊。它还融合了鸟鸣、风声和社区闲聊等自然产生的环境音，实现了极具说服力的家庭录像美学。

rss · AI Hot · Jul 1, 23:52

**背景**: Seedance 是由字节跳动开发的 AI 视频生成器，以其电影级的画质、对提示词的忠实度以及原生音视频生成能力而闻名。DV 摄像机美学指的是 1990 年代末和 2000 年代初早期数码摄像机特有的明显视觉缺陷，如颗粒感、色彩偏移和对焦问题。现代多模态 AI 模型正越来越多地接受测试，不仅要生成纯净的视觉效果，还要准确地重现这些具有历史感的模拟风格缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.seeddance.io/">Seedance AI Video Generator – No Queue, No Watermark</a></li>
<li><a href="https://seadance.io/">SeaDance AI — Seedance 2 . 0 Multimodal AI Video Generation ...</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#Generative AI`, `#Seedance`, `#Multimodal AI`, `#Frontier Tech`

---

<a id="item-10"></a>
## [空中智能初创企业 SPARO 半年内连获四轮数亿元融资](https://36kr.com/p/3877830625046535?f=rss) ⭐️ 8.0/10

硅羽科技（SPARO）由全球顶尖机器人学者、前大疆高级科学家张富于 2026 年 2 月创立，在短短半年内连续完成四轮数亿元融资。该公司正在构建由多模态感知、端到端小脑以及世界导航模型大脑组成的全栈技术体系，致力于打造自主空中智能体。 包括阿里巴巴在内的顶级投资机构的大规模快速押注，标志着无人机行业正从以硬件参数为核心的工程竞争，转向以 AI 驱动的自主智能能力为核心的新阶段。如果技术成功落地，SPARO 将使飞行器能够在无 GPS 等复杂环境中可靠运行，从而解锁物流、巡检和工业作业等领域的全新商业应用场景。 SPARO 的技术栈通过深度耦合激光雷达、视觉和惯导等多源信息，在无 GPS 条件下实现厘米级定位，同时其端到端控制系统将避障响应延迟压缩至 5 毫秒以内，保障高速飞行安全。公司正同时推进整机产品以验证全链路可靠性，以及可即插即用赋能多旋翼、eVTOL 和固定翼等各类平台的空中智能模块。

rss · 36kr · Jul 2, 01:33

**背景**: 传统无人机高度依赖 GPS 信号和人工遥控，这使其作业能力主要局限于开阔环境中的观察任务。“空中智能体”的概念代表了具身智能与航空领域的结合，要求飞行器不仅能感知周围环境，还要能理解空间语义、预测动态变化，并与环境产生物理交互。SPARO 提到的世界导航模型超越了传统 SLAM（同步定位与建图）技术——SLAM 仅解决“我在哪和周围什么样”的问题，而世界导航模型则旨在解决“这个空间如何运作以及接下来会发生什么”的深层认知问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://post.smzdm.com/p/adogorxx/">多 模 态 大 模 型在低空 无 人 机 场景中的能力评估_ 无 人 机 _什么值得买</a></li>
<li><a href="https://sunnymasuping.github.io/2024/03/02/sensing/">多 模 态 感 知 技 术 概述 - 马苏平的博客</a></li>
<li><a href="https://36kr.com/p/2714495949771399">具身智能的月亮与六便士-36氪</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#Autonomous Drones`, `#Aerial Intelligence`, `#Startup Funding`

---

<a id="item-11"></a>
## [北大孵化「纳开量子」获数千万元种子轮融资，推进中性原子量子计算工程化](https://36kr.com/p/3877814169530630?f=rss) ⭐️ 8.0/10

由北京大学孵化的国内首家 nK 级中性原子量子计算公司「纳开量子」近期完成了数千万元的首轮融资，本轮融资由高瓴创投领投。该公司宣称是国内唯一能将多种原子工程化冷却至 10nK 以下的团队，所募资金将主要用于推进专用量子模拟计算机和通用量子计算机的研发与交付。 中性原子技术因其原子的天然全同性和高度可扩展性，被广泛认为是实现大规模通用量子计算最有希望的路径之一。此次获得大额风险投资验证了该硬件路线在中国的商业可行性，将加速下一代算力基础设施的发展，从而推动材料科学和制药等领域复杂系统模拟的突破。 该公司利用光晶格技术对超冷原子进行精准操控，在国内实现了领先的冷却能力。尽管中性原子在比特数扩展性上具有压倒性优势（轻松达到上千甚至上万个比特），但团队目前正致力于攻克运行保真度和系统连续运行时间这两个关键短板，以打造实用的量子计算机。

rss · 36kr · Jul 2, 01:16

**背景**: 量子计算旨在以远超经典计算机的速度执行复杂计算，目前全球正在探索多种硬件路线，包括超导、离子阱和中性原子等。中性原子系统利用激光捕获和操控单个原子，利用其全同的量子特性来创建高度可扩展的量子比特阵列。该领域公司的最终目标是实现容错通用量子计算机，但近期的应用主要集中在面向科学研究的专用量子模拟器上。

**标签**: `#Quantum Computing`, `#Frontier Tech`, `#Neutral Atoms`, `#Funding`, `#Hardware Infrastructure`

---

<a id="item-12"></a>
## [快手可灵 AI 将完成 30 亿美元融资，投后估值 180 亿美元](https://www.ithome.com/0/971/440.htm) ⭐️ 8.0/10

快手旗下的 AI 视频生成部门可灵 AI 即将完成一轮 30 亿美元融资，投后估值达 180 亿美元，腾讯为本轮投资方之一。该估值较今年 4 月最初设定的 200 亿美元目标有所下调，快手计划在未来 12 个月内启动可灵 AI 赴港上市程序。 这是生成式 AI 领域规模最大的单笔融资之一，显示出投资者对 AI 视频生成这一前沿技术的巨大信心。可灵 AI 已成为全球市场的有力竞争者，截至 3 月年化收入运行率达 5 亿美元，全球用户突破 1 亿，使中国在该领域与美国 Runway、OpenAI Sora 等对手形成有力竞争。 可灵 AI 约四分之三的收入来自海外市场，2025 年第一季度收入达 6.5 亿元人民币，同比增长 300%。IPO 募集资金将主要用于扩充算力、建设数据中心及引进人才，而可灵所在的全球视频内容创作市场规模预估达 1400 亿美元，未来三年预计年均增长 10%。

rss · IT HOME · Jul 2, 01:32

**背景**: 可灵 AI 是由总部位于北京的快手开发的一款生成式 AI 视频创作服务，快手是中国最大的短视频平台之一。该工具允许用户通过文本和图像参考生成电影级视频序列，其 2025 年 2 月发布的最新 3.0 系列模型提供了更强的叙事控制力和视觉一致性。可灵在全球市场上与 Runway（提供 Gen-4.5 模型）、字节跳动的 Seedance 等产品在快速增长的 AI 视频生成领域展开竞争。快手于 5 月披露已开始评估可灵 AI 的重组方案以引入外部投资者，为本次融资及 eventual IPO 铺路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kling_AI">Kling AI - Wikipedia</a></li>
<li><a href="https://runwayml.com/">Runway | Building AI to Simulate the World</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Video Generation`, `#AI Funding`, `#Kling AI`, `#Tech IPO`

---

<a id="item-13"></a>
## [联合国专家组警告：AI 能力进步速度已超过科学认知](https://www.ithome.com/0/971/436.htm) ⭐️ 8.0/10

7 月 1 日，由 40 名顶尖专家组成的联合国 AI 独立科学小组发布了首份报告，警告 AI 能力的进步速度已经超过科学界的认知和各国政府调整政策的速度。该小组由知名 AI 科学家约书亚·本吉奥担任联合主席，指出越来越多证据表明 AI 可能出现欺骗行为，且目前针对高度自主 AI 系统的控制手段仍然严重不足。 这份报告代表了一个主要国际机构对全球 AI 治理辩论的重大干预，强调不受约束的 AI 部署会带来从心理伤害到灾难性滥用的多重风险。报告还突显了 AI 发展中严重的全球不平等问题，美国掌握了全球前 500 台 AI 超级计算机中 75% 的算力，而发展中国家在普及方面明显滞后。 报告指出，目前全球每周有超过 10 亿人使用对话式 AI，但现有模型仅覆盖全球 7000 多种语言中的极小部分，导致在医疗翻译等关键领域出现严重错误。本吉奥特别警告，科学界无法保证 AI 不会在自主运行或被恶意使用者利用的情况下造成灾难性后果。

rss · IT HOME · Jul 2, 01:22

**背景**: 联合国 AI 独立科学小组的成立旨在为政策制定者提供基于证据的 AI 发展和治理指导。小组联合主席约书亚·本吉奥被公认为“AI 教父”之一，近年来成为倡导 AI 安全研究的领军人物。“对齐”概念——即确保 AI 系统的行为符合人类价值观——随着模型能力日益增强和高度自主化，仍然是一个尚未解决的科学难题。

**标签**: `#AI Safety`, `#AI Governance`, `#United Nations`, `#Frontier AI`, `#AI Policy`

---

<a id="item-14"></a>
## [Claude Code 2.1.91 被指隐蔽遥测，暗检中国时区与代理](https://t.me/zaihuapd/42285) ⭐️ 8.0/10

一名发布逆向分析的用户声称，Claude Code 2.1.91 版本会隐蔽检查系统时区是否设为 Asia/Shanghai 或 Asia/Urumqi，并检测代理 URL 是否指向中国域名或中国 AI 实验室。该工具据称通过修改日期格式和在 "Today's date is" 字符串中使用 Unicode 撇号，将检测结果编码进发送至 Anthropic API 的系统提示词中。 若被证实，这将构成对用户信任的重大侵犯，因为嵌入系统提示词中的隐蔽遥测可能使 Anthropic 能够根据地理位置和网络配置对用户进行秘密画像。鉴于围绕 AI 技术访问的地缘政治紧张局势，以及对特定地区用户可能产生歧视性行为的潜在风险，这些指控尤为敏感。 据称的编码机制在技术上非常隐蔽，利用日期格式的变化和 Unicode 字符选择（如不同的撇号变体）在提示词文本本身中不可见地传输元数据。这种隐写方法意味着该遥测不会出现在标准网络流量分析中，如果不进行深度代码检查则极难被发现。

telegram · @zaihuapd · Jul 1, 04:42

**背景**: Claude Code 是 Anthropic 的代理式编程工具，在终端中运行并与 Anthropic API 交互以辅助开发者完成编程任务。软件中的遥测是指从用户设备自动收集并传输数据给提供商的做法，这在开发者社区中一直是隐私关注的焦点。系统提示词是发送给 AI 模型的基础指令，用于塑造其行为，在用户不知情的情况下修改这些提示词会引发严重的透明度和伦理问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/ claude - code : Claude Code is an agentic coding ...</a></li>
<li><a href="https://www.reddit.com/r/privacy/comments/nrpzwm/what_exactly_is_the_problem_with_telemetry/">what exactly is the problem with telemetry? : r/privacy - Reddit</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude Code`, `#AI Security`, `#Telemetry`, `#Reverse Engineering`

---