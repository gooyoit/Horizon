---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> From 116 items, 11 important content pieces were selected

---

1. [OpenAI 自研 Jalapeño 芯片号称超越 Nvidia Blackwell](#item-1) ⭐️ 9.0/10
2. [SemiAnalysis 揭秘 OpenAI 自研 Jalapeño 推理芯片](#item-2) ⭐️ 9.0/10
3. [OpenAI 首款自研芯片 Jalapeño 每瓦吞吐量达 GB300 的 1.7 倍](#item-3) ⭐️ 9.0/10
4. [英伟达首测 Vera Rubin NVL72：DeepSeek 每兆瓦吞吐最高提升 30 倍](#item-4) ⭐️ 9.0/10
5. [OpenAI 首款自研推理芯片 Jalapeño 能效与延迟超越英伟达 GB300](#item-5) ⭐️ 9.0/10
6. [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](#item-6) ⭐️ 8.0/10
7. [评测框架无中立：同一模型得分从 31%波动至 89%](#item-7) ⭐️ 8.0/10
8. [Anthropic 冲击史上最大 IPO：以 30 万亿美元 TAM 支撑 2 万亿美元估值](#item-8) ⭐️ 8.0/10
9. [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入轨道](#item-9) ⭐️ 8.0/10
10. [Qwen 预告 Qwen3.8-Flash-Next，8 月 26 日基于 Qwen4 新架构开源](#item-10) ⭐️ 8.0/10
11. [GPT-5.6 Sol 设计定制 CPU，在 Turing Complete 中成功运行《毁灭战士》](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 自研 Jalapeño 芯片号称超越 Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI 与 Broadcom 合作推出了其首款专为 LLM 推理设计的自研芯片 Jalapeño，并声称在测试中性能超越 Nvidia 的 Blackwell 处理器。SemiAnalysis 对该芯片的首批实测结果进行了详细的技术分析，显示其在推理吞吐量、延迟和能效方面达到业界领先水平。 如果这些说法属实，这将标志着 AI 芯片领域的重大转变：最大的 AI 客户开始用专门定制的推理 ASIC 取代 Nvidia GPU，以降低每 token 成本。这表明推理（预计将占约 4000 亿美元 AI 加速器市场的 60–70%）正在成为新的竞争焦点，对 Nvidia 的主导地位构成威胁，也为挑战者打开了大门。 Jalapeño 专门针对 LLM 推理而非通用 GPU 计算进行优化，采用极低精度格式（低至 FP4）以最大化每瓦特吞吐量。评论者指出其裸片尺寸与 Nvidia Rubin 大致相当，但 NVFP4 PFLOPS 约为后者的三分之一，这表明其优势来自工作负载特化而非原始算力密度。

hackernews · bmulholland · Aug 25, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: Nvidia 的 Blackwell 架构是 Hopper 的继任者，采用台积电 4NP 工艺，集成 2080 亿个晶体管，一直是前沿 AI 训练和推理的事实标准。定制推理芯片本质上是 ASIC——与通用 GPU 不同，它们针对每 token 成本、延迟和功耗进行硬性优化，这正是 OpenAI 等超大规模厂商与 Broadcom 等伙伴合作自研芯片的原因。推理正日益成为主导性工作负载，因为每个已部署的模型每天要进行数十亿次推理，而训练只需进行一次。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://openai.com/index/jalapeno-first-results/">Jalapeño’s first results show industry-leading ... - OpenAI</a></li>
<li><a href="https://valueaddvc.com/blog/inference-chips-vs-training-chips-why-the-next-semiconductor-race-is-different">Inference vs Training Chips 2026: 60–70% of $400B Market</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者将其比作早期 3dfx/Riva 的 GPU 时代，讨论专用推理芯片能否长期存在以及谁将最终主导市场。有人指出在每焦耳 token 数上人类仍比 LLM 高效约 22 倍；也有人认为硬件的持续进步必然导致 token 价格暴跌，且 OpenAI/Anthropic 的规模已足以将模型权重直接固化到定制芯片中。

**标签**: `#AI chips`, `#OpenAI`, `#Nvidia`, `#AI infrastructure`, `#inference hardware`

---

<a id="item-2"></a>
## [SemiAnalysis 揭秘 OpenAI 自研 Jalapeño 推理芯片](https://aihot.virxact.com/items/cmt9bfoos0f9urolynullwmwe) ⭐️ 9.0/10

SemiAnalysis 发布长文披露 OpenAI 与 Broadcom 合作研发的自研 Jalapeño 芯片，称其面向数十万亿参数模型与百万级 token 上下文设计。报告称 Jalapeño 的每兆瓦 token 吞吐已超越英伟达公布的 Vera Rubin 数据，OpenAI 也在 Hot Chips 2026 上公布了首批基准测试结果。 如果每瓦性能的说法成立，OpenAI 可以减少对英伟达的前沿推理算力依赖，将利润和控制权转向自研芯片。报告还质疑 CUDA 的长期主导地位，认为能自写代码的 AI 会削弱保护英伟达生态的传统软件护城河。 Jalapeño 以能效为核心优化，设计目标是让数千颗芯片协同工作，作为单一推理机服务百万 token 上下文的超大模型。基准测试基于 SemiAnalysis 的 InferenceX 框架进行，该芯片专为 LLM 推理而非训练打造。

rss · AI Hot · Aug 25, 23:27

**背景**: OpenAI 与 Broadcom 合作开发 Jalapeño，并与 AMD 合作，作为在英伟达 GPU 之外多元化算力供应战略的一部分。英伟达 Vera Rubin 是其下一代机架级平台，面向智能体 AI 和推理模型，推理已成为持续性的生产工作负载。英伟达的竞争优势长期建立在 CUDA 软件生态之上，其高昂的迁移成本锁定了开发者；而谷歌 TPU 等超大规模厂商的自研芯片一直是这一护城河的主要挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/">OpenAI’s Jalapeño chip is built for fast inference at scale ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI芯片`, `#AI基础设施`, `#英伟达`, `#推理`

---

<a id="item-3"></a>
## [OpenAI 首款自研芯片 Jalapeño 每瓦吞吐量达 GB300 的 1.7 倍](https://aihot.virxact.com/items/cmt9cr3s70g6wrolymqgk0373) ⭐️ 9.0/10

OpenAI 与博通联合设计的首款自研推理芯片 Jalapeño 公布了首批性能数据：在 GPT-OSS 120B、DeepSeek R1 670B 和 Kimi K2.5 1T 三款模型测试中，每瓦 AI 吞吐量较 NVIDIA GB200/GB300 高出 1.5 至 1.9 倍，端到端延迟仅为对比系统的约 28% 至 59%。 这标志着 OpenAI 正式进军自研芯片领域，直接挑战 NVIDIA 在 AI 推理市场的主导地位，类似于谷歌的 TPU 战略。更高的每瓦性能意味着更低的推理成本和更高的利润率，随着推理成为 AI 数据中心的主要工作负载，这一点至关重要。 Jalapeño 是专为大规模语言模型推理打造的 ASIC，早期测试显示相比主流 AI GPU 可节省约 50% 的推理成本，由台积电代工制造。测试覆盖了从 120B 到 1T 参数规模的模型，报告的延迟优势（仅为对比系统的 28%-59%）表明其在原始吞吐量之外也有显著提升。

rss · AI Hot · Aug 25, 23:25

**背景**: 继谷歌的 TPU 战略之后，各大 AI 实验室越来越倾向于通过自研芯片来降低对 NVIDIA 的依赖并削减推理成本。“每瓦 Token 吞吐量”已成为 AI 数据中心的核心能效指标，因为电力是刚性约束，直接决定 NVIDIA 所称的“AI 工厂”或“Token 工厂”的收入与盈利能力。Jalapeño 于 2026 年 6 月 24 日在旧金山发布，是 OpenAI 与博通联合设计的成果，对标 NVIDIA Blackwell 代的 GB200/GB300 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jexcloud.com/zh/blog/2026-0625-openai-jalapeno-chip-broadcom-inference.html">OpenAI Jalapeño 芯 片 全解｜JEXCLOUD</a></li>
<li><a href="https://t.cj.sina.com.cn/articles/view/7879923015/1d5ae154701901gfbu">OpenAI 亮出底牌：首枚自研 芯 片 Jalapeño 来了-云开发者社区-云</a></li>
<li><a href="https://baike.baidu.com/item/每瓦吞吐量/67404166">每瓦吞吐量 - 百度百科</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI芯片`, `#AI基础设施`, `#推理芯片`, `#NVIDIA`

---

<a id="item-4"></a>
## [英伟达首测 Vera Rubin NVL72：DeepSeek 每兆瓦吞吐最高提升 30 倍](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 9.0/10

英伟达首次公布下一代机柜 Vera Rubin NVL72 的片上实测数据：运行 DeepSeek-V4-Pro 智能体编码任务时，每兆瓦吞吐量较 GB300 最高提升 30 倍，每百万 Token 成本最高下降 35 倍。同期还宣布 Groq 3 LPX 推理加速芯片进入量产（运行 Gemma 4 31B 输出 3400 Token/秒），并发布智能体专用 Vera CPU，SpaceXAI 计划部署 Vera CPU 并于 2028 年将优化版机柜送上太空。 这是英伟达后 Blackwell 机柜级平台的首批真实能效数据，直击 AI 基础设施两大瓶颈——功耗与每 Token 成本，而智能体工作负载正令推理需求激增。专用推理芯片（Groq 3 LPX）与智能体 CPU 的组合，显示出英伟达对抗 Google、Amazon 及自研芯片竞争者、捍卫 AI 算力霸主地位的策略。 Vera Rubin NVL 72 将 72 颗 Rubin GPU 与 36 颗 Vera CPU 通过 NVLink 6 交换、ConnectX-9 SuperNIC、BlueField-4 DPU 及液冷整合为单一机柜，作为一颗巨型 GPU 运行。Vera CPU 号称效率是传统机柜级 CPU 的两倍、性能快 50%，面向智能体 AI 背后的代码执行、工具调用、沙箱与编排任务；Groq 3 LPX 机柜部署可扩展至 256 颗通过芯片直连的 LP30 加速器。

telegram · @zaihuapd · Aug 25, 14:48

**背景**: 英伟达的 GB200/GB300 NVL72 等机柜级系统已主导前沿 AI 训练与推理；Vera Rubin 是下一代产品，标志着英伟达从销售 GPU 卡片转向销售集成式机柜级 AI 超级计算机。随着 AI 智能体执行涉及工具调用与代码执行的长链多步任务，推理（而非训练）正成为主要算力成本，推动了对专用推理加速器和面向智能体编排的 CPU 的需求。Google（TPU）、Amazon 及 Groq 等竞争者都在推专用推理硬件，而数据中心电力日益成为瓶颈，令英伟达必须提升每兆瓦吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>
<li><a href="https://benquan.hk/article-vera-rubin-nvl72.html">NVIDIA Vera Rubin NVL 72 Deep Dive 2026 | BENQUAN Global</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai">NVIDIA Launches Vera CPU, Purpose-Built for Agentic AI | NVIDIA Newsroom</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI infrastructure`, `#Vera Rubin`, `#DeepSeek`, `#inference hardware`

---

<a id="item-5"></a>
## [OpenAI 首款自研推理芯片 Jalapeño 能效与延迟超越英伟达 GB300](https://openai.com/index/jalapeno-first-results/) ⭐️ 9.0/10

OpenAI 公布了与博通合作开发的首款自研推理芯片 Jalapeño 的首批测试数据：在 GPT-OSS 120B、DeepSeek R1 670B 和 Kimi K2.5 1T 三款模型上，单位功耗的 AI 工作产出是英伟达 GB300 的 1.5 至 1.9 倍，端到端延迟低 1.7 至 3.6 倍。芯片额定功耗 700 瓦、实测持续功耗不超过 550 瓦，OpenAI 计划今年年底前在自有算力设施中部署。 这是 OpenAI 首次以实际数据证明其降低对英伟达依赖的能力，所宣称的能效优势有望大幅降低大规模模型推理的成本和功耗。这也标志着头部 AI 实验室自研推理芯片的行业趋势正在加速，将给英伟达的数据中心 GPU 业务带来更大竞争压力。 对比基准是英伟达 GB300，但未与刚开始出货的新一代 Vera Rubin 平台比较；Jalapeño 仅用于推理，不用于模型训练。OpenAI 表示第二代芯片已在深入开发中，第三代也正在设计。

telegram · @zaihuapd · Aug 25, 16:08

**背景**: AI 推理（运行已训练好的模型来响应用户请求）已成为 AI 服务商最主要且对成本最敏感的工作负载，因此催生了针对推理优化的专用芯片需求。OpenAI 与定制芯片（ASIC）设计领域的领先厂商博通合作开发 Jalapeño，走的是谷歌（TPU）和亚马逊（Trainium/Inferentia）自研芯片、掌控算力供应链的老路。英伟达 GB300 属于 Blackwell Ultra 世代，是目前数据中心 AI 负载的领先 GPU 产品。

**标签**: `#OpenAI`, `#AI芯片`, `#AI基础设施`, `#推理芯片`, `#英伟达`

---

<a id="item-6"></a>
## [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 8.0/10

2026 年 8 月 25 日，苹果发布了 M6 芯片和迄今最强大的 M5 Ultra 芯片，用于新款 Mac mini 和 Mac Studio。M6 引入了双 16 核神经网络引擎（Neural Engine），AI 峰值算力较前代提升最多 2 倍；M5 Ultra 则采用新一代 UltraFusion 封装技术，将两颗双 die 的 M5 Max 芯片互联，是苹果 M 系列首次采用四 die 架构。 此次发布表明苹果正明确围绕端侧 AI 重塑其芯片路线图，而本地大模型推理和 AI 原生工作流正成为消费级硬件的关键差异化因素。据彭博社报道，苹果将跳过 M6 Pro、Max 和 Ultra 版本，全力加速以 AI 为核心的 M7 世代开发，因此这是一次战略转向，而非单纯的常规芯片升级。 M6 的双神经网络引擎可被系统框架同时调用，使应用的模型执行速度更快，加速端侧 AI 工作流。价格不菲：顶配 M5 Ultra、256GB 内存和 16TB 存储的 Mac Studio 售价 18299 美元，各档位的内存升级价格约为每 GB 25 美元。

hackernews · @zaihuapd · Aug 25, 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: 苹果自研芯片集成了 CPU、GPU 和神经网络引擎（Neural Engine），其中神经网络引擎是专为 AI 模型所依赖的矩阵运算优化的专用硬件。自 2020 年 M1 发布以来，苹果通过 Pro、Max 和 Ultra 层级不断扩展该架构，Ultra 芯片利用 UltraFusion 封装技术将两颗 Max die 融合为一颗大芯片。M5 Ultra 的四 die 设计将这一思路进一步扩展，融合了两颗双 die 的 M5 Max。据报道，苹果 2026 年之后的路线图指向基于 chiplet 的 CPU/GPU/神经网络引擎组合，以及 2027-2028 年采用 1.4nm GAA 晶体管等先进制程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in performance and AI ...</a></li>
<li><a href="https://www.macrumors.com/2026/08/25/apple-debuts-m5-ultra/">Apple Debuts M 5 Ultra as Most Powerful Chip Ever - MacRumors</a></li>
<li><a href="https://www.techrepublic.com/article/news-apple-m6-m7-ai-mac-roadmap/">Apple Overhauls Chip Roadmap, Ditches M6 Pro and Max for M7 Generation</a></li>

</ul>
</details>

**社区讨论**: 评论者对实际性能提升印象深刻，一位 M1 Pro 老用户表示在店里试用 M5 Pro 时感觉速度显著提升，但仍在 macOS 与 Linux 之间纠结。多人指出彭博社关于苹果跳过 M6 Pro/Max/Ultra、专注 AI capable M7 的报道才是真正的重点。还有人关注价格，估算顶配 512GB 内存的 Mac Studio 可能接近 24699 美元；也有评论者认为经通胀调整后，与当年的 Mac SE/30 相比，如今机器的性价比令人惊叹。

**标签**: `#apple`, `#silicon`, `#ai-compute`, `#hardware`, `#neural-engine`

---

<a id="item-7"></a>
## [评测框架无中立：同一模型得分从 31%波动至 89%](https://aihot.virxact.com/items/cmt9ad4ek0efjrolydq33dqw7) ⭐️ 8.0/10

一篇新论文表明，评测框架的配置（选项顺序、提示词措辞、答案解析方式）会导致模型得分剧烈波动：12 个开源模型在 3,679 道题的 26 种同等合理配置下测试，某 31B 模型的得分可从 31%波动至 89%。 这一发现动摇了排行榜排名的可信度：配置敏感的题目承载了相邻模型间 95.7%的差距，且 4 个不同模型在某种配置下都能排第一。研究还表明基准压缩方法筛选出的恰恰是最易受配置影响的脆弱题目，使其目的落空。 该研究在题目完全相同的情况下仅改变框架层面的选择（选项排序、提示词措辞、答案提取方式），从而将框架影响与模型能力分离。旨在用题目子集重建完整基准分数的基准压缩方法，最终选中的恰恰是那些得分在不同配置间最不稳定的题目。

rss · AI Hot · Aug 25, 23:13

**背景**: 评测框架（evaluation harness）是端到端运行模型评测的标准化基础设施：它格式化提示词、向模型输入题目、解析回答并计算得分。EleutherAI 的 LM Evaluation Harness 等框架是 HuggingFace 和各大实验室广泛使用的行业标准，用于在 MMLU、GSM8K 等基准上测试模型。基准压缩方法则试图将大型基准套件缩减为能近似完整套件分数的小型子集，这被建模为一个分数重建的优化问题。这篇论文表明，即使是“同等合理”的框架选择也会引入足以淹没真实模型差异的方差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eleuther.ai/projects/large-language-model-evaluation">Evaluating LLMs — EleutherAI</a></li>
<li><a href="https://paperswithcode.co/paper/2510.10457">Rethinking LLM Evaluation : Can We Evaluate ... | Papers with Code</a></li>
<li><a href="https://deepeval.com/blog/what-is-an-eval-harness">Eval harness: What it is, how to use it, and why you should care | DeepEval - The LLM Evaluation Framework</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#LLM benchmarks`, `#benchmark reliability`, `#AI research`, `#model evaluation`

---

<a id="item-8"></a>
## [Anthropic 冲击史上最大 IPO：以 30 万亿美元 TAM 支撑 2 万亿美元估值](https://www.ithome.com/0/994/327.htm) ⭐️ 8.0/10

据华尔街日报报道，Anthropic 在 IPO 招股书中提出超过 30 万亿美元的潜在市场规模（TAM），超过 SpaceX 的 28.5 万亿美元，成为商业史上最庞大的市场叙事。公司计划于 2026 年秋季挂牌上市，目标募资高达 1,000 亿美元，估值锚定在约 2 万亿美元。 这将是历史上规模最大的 IPO 之一，表明资本市场对前沿 AI 抱有极强的信心，并可能重塑 AI 公司的估值逻辑。创纪录的 TAM 叙事也为 AI 初创公司向投资者描绘增长空间设定了新的激进标杆。 据报道，30 万亿美元的测算并非基于现有软硬件销售额，而是统计了未来全球所有可被 AI 模型替代或完成的工作的全部经济价值。Anthropic 2026 年第二季度营收达 116 亿美元并首次实现调整后营业利润为正，但分析师警告，数据中心建设受阻和海外低价模型竞争可能考验投资者对超高估值的容忍度。

rss · IT HOME · Aug 26, 00:36

**背景**: TAM（总可寻址市场）指产品或服务在实现 100% 市场份额时理论上可获得的最大年度收入，是公司向投资者展示增长空间的战略工具，而非收入预测。Anthropic 由 OpenAI 前成员于 2021 年创立，是一家总部位于旧金山的 AI 安全公司，旗舰产品是 Claude 系列大语言模型。SpaceX 此前在 5 月提交的文件中宣称 28.5 万亿美元的 TAM，其中 26.5 万亿美元来自 AI 相关业务机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investglass.com/total-addressable-market-tam-definition-calculation-methods-and-b2b-saas-examples/">Total Addressable Market (TAM): Definition, Calculation Methods, and B2B SaaS Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#frontier AI`, `#investment`

---

<a id="item-9"></a>
## [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入轨道](https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067) ⭐️ 8.0/10

据报道，SpaceX 计划在 2027 年将一套英伟达 Vera Rubin NVL72 机架级 AI 系统送入轨道，用于验证太空数据中心技术。该系统包含 72 颗 Rubin GPU 和 36 颗 Vera CPU，功耗超过 100 千瓦，这将是首次在太空部署如此大规模的机架级 AI 超算。 如果成功，这将是迈向太空 AI 数据中心的重要一步——太空设施可利用充足的太阳能并省去水冷，从而缓解地面能源对 AI 算力扩张的制约。这也标志着航天产业与 AI 基础设施建设正在加速融合。 NVL72 通常需要复杂的液冷和供电设施，而太空中唯一的散热方式是热辐射，散热成为最大难题。SpaceX 尚未公布具体发射时间、轨道高度以及供电和冷却方案，且现代芯片并非为太空辐射环境设计，可靠性存疑。

telegram · @zaihuapd · Aug 25, 08:03

**背景**: Vera Rubin NVL72 是英伟达下一代机架级 AI 超算，通过 NVLink 将 72 颗 Rubin GPU 和 36 颗 Vera CPU 组成统一共享内存架构，单机架算力约 3.6 EFLOPS，推理成本相比 Blackwell 降低约十分之九。轨道数据中心被认为可以利用不间断太阳能并将废热直接辐射到太空真空，但面临严苛的物理限制：散热器面积受斯特藩-玻尔兹曼定律约束，且太空辐射可能损坏未加固的商业芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://spectrum.ieee.org/orbital-data-centers-heat">Why Thermodynamics Rules Future Orbital Data ... - IEEE Spectrum</a></li>
<li><a href="https://hashrateindex.com/blog/nvidia-vera-rubin-nvl72-specs-breakdown/">NVIDIA Vera Rubin NVL72: Full Specs & Platform Breakdown</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#SpaceX`, `#NVIDIA`, `#orbital datacenter`, `#frontier tech`

---

<a id="item-10"></a>
## [Qwen 预告 Qwen3.8-Flash-Next，8 月 26 日基于 Qwen4 新架构开源](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 8.0/10

Qwen 在魔搭社区和 Hugging Face 上线了 Qwen3.8-Flash-Next 的预告页，这是一个基于下一代 Qwen4 架构的多模态 MoE 模型，预计 8 月 26 日 23 时（UTC+8）开放下载，将提供标准版和 FP8 两个版本。 这是外界首次得以窥见 Qwen4 架构，而 Qwen 是最受关注的开源模型系列之一，此举表明 Qwen 正在追求架构创新而非单纯堆参数。提前开源可以让社区在 Qwen4 系列正式发布前准备好工具链、推理框架和微调流程。 该模型被明确描述为“Qwen4 架构的预览”，官方表示提前开源是为了让社区为 Qwen4 系列做准备。除标准版外还提供官方 FP8 版本，显示其对低显存部署的重视，FP8 相比 FP16 可将权重显存占用大致减半。

telegram · @zaihuapd · Aug 25, 12:59

**背景**: MoE（混合专家）架构将模型拆分为多个专家子网络，每个 token 只激活其中一部分，从而在提升模型能力的同时保持较低的推理开销。FP8 是一种 8 位浮点格式，可对权重、激活值和 KV 缓存进行量化，在几乎不损失精度的情况下降低显存占用并加速推理。Qwen 是阿里巴巴的开源模型系列，一直是开源大模型领域的领军者，此次发布延续了此前 Qwen3-Next 等实验性模型的做法，在大版本更新前先预览架构变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Upcoming release · Hugging Face</a></li>
<li><a href="https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/">FP8: Efficient model inference with 8-bit floating point numbers</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA ...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#open-source models`, `#MoE`, `#multimodal`, `#LLM release`

---

<a id="item-11"></a>
## [GPT-5.6 Sol 设计定制 CPU，在 Turing Complete 中成功运行《毁灭战士》](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment) ⭐️ 8.0/10

AI 爱好者 Angel (@Angaisb_) 展示了由 GPT-5.6 Sol 从基础逻辑门设计的定制 CPU「Codex-R32」，在教育解谜游戏 Turing Complete 的沙盒模式中成功启动并运行 1993 年的经典游戏《毁灭战士》。游戏画面叠加在处理器门级电路的实时脉冲示意图上。 该演示展示了前沿 AI 编程代理自主完成全栈硬件设计任务的能力——从逻辑门搭建可工作的 CPU 架构，一直到运行编译后的软件，这是 AI 驱动数字设计能力的一个里程碑。虽然这只是沙盒演示而非研究突破，但它表明 AI 工具有望加速硬件设计教育与原型开发。 该 CPU 运行的是基于 C 语言的 PureDOOM 移植版（一个单头文件、无依赖的 Doom 源码移植），被编译为 RV32IM（32 位 RISC-V 整数指令集加乘法扩展）机器码并直接在仿真硬件上执行。面对网友调侃「下一步跑《孤岛危机》」，Angel 让 AI 代答：没问题——先造一块 GPU、加几 GB 内存，再画一张从太空可见的电路图。

telegram · @zaihuapd · Aug 25, 15:23

**背景**: Turing Complete 是一款教育解谜游戏，玩家从 NAND 门开始逐层搭建计算机，并在沙盒模拟器中设计自己的 CPU 架构和指令集。RV32IM 是 32 位 RISC-V 指令集，涵盖整数运算及乘除法扩展，是轻量级嵌入式核心的常见目标。PureDOOM 是一个单头文件、无依赖的 Doom 源码移植，专为在几乎任何设备上运行而设计。「在 X 上运行毁灭战士」已成为一个经久不衰的网络梗，用来庆祝这款游戏被移植到各种离谱平台上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/computing/articles/ai-coder-gets-doom-running-110949882.html">AI coder gets Doom running on a custom CPU designed by GPT-5. ...</a></li>
<li><a href="https://github.com/Daivuk/PureDOOM">GitHub - Daivuk/PureDOOM: Pure DOOM - Single Header Doom Source Port · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 网友调侃下一步应该跑《孤岛危机》，Angel 便让 AI 回应说需要先造一块 GPU、加几 GB 内存，再画一张从太空可见的电路图。整体反响将这次演示视为 AI 硬件设计能力的一次令人印象深刻的技术与视觉盛宴。

**标签**: `#AI`, `#GPT-5.6`, `#CPU design`, `#AI coding agent`, `#hardware simulation`

---