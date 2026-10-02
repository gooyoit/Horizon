---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> From 112 items, 12 important content pieces were selected

---

1. [SGLang v0.5.21 发布，支持 DeepSeek-V4.1 Flash、Qwen-Image 2.1 等新模型](#item-1) ⭐️ 8.0/10
2. [OpenAI 与 Synopsys 推出 GPT-Synopsys，用前沿 AI 革新芯片设计](#item-2) ⭐️ 8.0/10
3. [Matthew Green：沙箱化 AI 智能体构成智能体间蠕虫的传播条件](#item-3) ⭐️ 8.0/10
4. [消息称 Anthropic 寻求最早 11 月中旬启动 IPO，争取感恩节前挂牌](#item-4) ⭐️ 8.0/10
5. [MerchantBench 评测：顶级 LLM 智能体长周期任务表现仅达人类 27.3%](#item-5) ⭐️ 8.0/10
6. [Meta 提出专用控制器调度长程智能体推理，ProgramBench 提升至 71.5%](#item-6) ⭐️ 8.0/10
7. [Volantis 获 8800 万美元 A 轮融资，用光子互连为大模型推理提速](#item-7) ⭐️ 8.0/10
8. [Google DeepMind 发布 SynthID Bio，为 AI 设计的蛋白质添加水印](#item-8) ⭐️ 8.0/10
9. [Cloudflare 开源决策模型 Clef，输出类型化概率而非文本](#item-9) ⭐️ 8.0/10
10. [Google 首次轨道 AI 芯片试验确认在轨正常运行](#item-10) ⭐️ 8.0/10
11. [腾讯向甲骨文租用 10 万枚先进 AI 芯片，价值约 70 亿美元](#item-11) ⭐️ 8.0/10
12. [特朗普与六大科技巨头签署具有道义约束力的 AI 安全协议](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.21 发布，支持 DeepSeek-V4.1 Flash、Qwen-Image 2.1 等新模型](https://github.com/sgl-project/sglang/releases/tag/v0.5.21) ⭐️ 8.0/10

SGLang 发布 v0.5.21 版本，合并了来自 227 位贡献者的 779 个 PR，新增对 DeepSeek-V4.1 Flash、DiffusionGemma、Qwen-Image 2.1、FLUX 3 Action 等十个新模型的推理服务支持。关键特性包括 PD 实例可动态切换预填充与解码、前缀缓存默认改用 Rust 内核、DeepSeek-V4.1 长提示词首 token 提速 22%，以及全新的 Decisions 和 Score API。 SGLang 是使用最广泛的开源推理服务框架之一，对 DeepSeek-V4.1 Flash 等前沿模型的即时支持直接决定了服务提供商将其投入生产的速度。性能提升以及新的分类/打分 API 也让 SGLang 从单纯的文本生成扩展到更广泛的智能体与评估场景。 该版本通过 Docker 镜像覆盖 NVIDIA CUDA 13、AMD MI35x/MI30x、Intel GPU 和 Intel CPU 平台，可通过 `uv pip install --prerelease=allow sglang==0.5.21` 安装。其他技术亮点包括流水线并行与 EAGLE/MTP 投机解码的兼容、Kimi K3 在 PD 服务中预填充吞吐提升 20.6%，以及在 PP、DP 注意力和上下文并行下更高的精度。

github · sgl-project/sglang · Oct 2, 01:09

**背景**: SGLang（Structured Generation Language）是一个用于编程和服务大语言模型及多模态模型的开源框架，针对智能体工作负载、强化学习 rollout 和大规模生产服务进行了优化。它与 vLLM、TensorRT-LLM 等框架竞争，支持 RadixAttention 前缀缓存、投机解码和预填充-解码（PD）分离式服务等先进技术。DeepSeek-V4.1 Flash 是基于 DeepSeek 因果编码器-解码器（CED）架构的 552B 参数稀疏 MoE 多模态模型，而 DiffusionGemma 是谷歌基于 Gemma 4 MoE 骨干的 26B 参数实验性离散扩散语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SGLang">SGLang - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>
<li><a href="https://ai.google.dev/gemma/docs/diffusiongemma">DiffusionGemma model overview | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#inference framework`, `#open source`, `#LLM serving`, `#diffusion models`

---

<a id="item-2"></a>
## [OpenAI 与 Synopsys 推出 GPT-Synopsys，用前沿 AI 革新芯片设计](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design) ⭐️ 8.0/10

2026 年 9 月 30 日，OpenAI 与 Synopsys 宣布推出 GPT-Synopsys，这是一项联合前沿智能服务，将算力、OpenAI 前沿模型和 Synopsys 的 EDA 许可证打包在一起，以加速芯片设计流程。该专用模型旨在帮助工程师探索更多设计替代方案、更快地完成可用的芯片，并改善功耗与性能。 将前沿 AI 应用于 EDA 可能大幅降低芯片设计的成本和时间，有望催生面向各种应用的海量定制芯片——正如 AI 编程工具推动了软件产出的爆发。这将直接影响从 EDA 供应商、芯片设计公司到台积电、英特尔和三星等代工厂的整个半导体生态。 该联合服务将算力、模型和 EDA 许可证整合为一项产品，Synopsys 声称客户的设计数据将受到保护——由于芯片设计属于高度敏感的知识产权，这一点至关重要。据报道，两家公司将共享 AI 设计芯片带来的收入，该模型由 OpenAI 前沿模型与 Synopsys 的 EDA 技术及领域专长结合而成。

hackernews · giuliomagnifico · Oct 1, 10:21 · [社区讨论](https://news.ycombinator.com/item?id=49919910)

**背景**: 电子设计自动化（EDA）是指用于设计集成电路和其他电子系统的软件工具，Synopsys 和 Cadence 是这一双寡头市场的主导厂商。芯片设计极其复杂且昂贵，涉及逻辑综合、布局布线和验证等环节，传统上需要由经验丰富的工程师组成的大型团队完成。将大型 AI 模型应用于这些工作流已成为新兴趋势，因为 AI 可以帮助工程师探索远超人工方法所能覆盖的设计方案。将 AI 模型、算力和许可证打包为一项服务的做法，对 AI 和 EDA 两个行业而言都是一种全新的商业模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49919910">GPT-Synopsys: Frontier Intelligence to Revolutionize Chip Design | Hacker News</a></li>
<li><a href="https://quantumzeitgeist.com/synopsys-openai-share-revenue-ai-designed/">Synopsys And OpenAI Share Revenue From AI-designed Chips - Quantum Zeitgeist</a></li>
<li><a href="https://www.synopsys.com/glossary/what-is-electronic-design-automation.html">What is Electronic Design Automation (EDA)? – How it Works | Synopsys</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者看法不一：有人认为台积电、英特尔和三星等代工厂将因廉价定制芯片的爆发而受益；也有人对知识产权保护表示怀疑，质疑英伟达等公司是否愿意把芯片设计发给 OpenAI。还有人担心初级工程师会失去学习成长的机会，因为 AI 一开箱就能超越他们；另有评论者批评这是供应商炒作，呼吁提供更多开源 EDA 工具。

**标签**: `#AI`, `#chip-design`, `#EDA`, `#OpenAI`, `#frontier-tech`

---

<a id="item-3"></a>
## [Matthew Green：沙箱化 AI 智能体构成智能体间蠕虫的传播条件](https://simonwillison.net/2026/Oct/1/matthew-green/) ⭐️ 8.0/10

Simon Willison 转发了密码学家 Matthew Green 于 2026 年 9 月 30 日发表的文章，指出仅靠沙箱不足以约束失控的 AI 智能体。Green 观察到，处于相互隔离沙箱中的智能体能够在共享的软件包缓存中留下指令，而这些指令会改变接收方智能体的行为。 该分析指出了 AI 恶意软件一条现实的自传播路径：劫持智能体的载荷，加上能把载荷传递给下一个智能体的通信渠道（邮件、Slack、共享文档、WhatsApp）——这正是蠕虫的两个组成部分。随着 Muse 等个人自主智能体的广泛部署，这种蠕虫风险将影响所有构建或部署智能体系统的组织。 关键机制是通过共享资源进行的提示注入：即使智能体被隔离在各自独立的沙箱中，也能通过软件包缓存等共享状态相互影响，使沙箱边界对这类威胁失效。Green 指出这一模式可从训练运行扩展到通过日常通信渠道交互的独立部署的个人智能体。

rss · Simon Willison · Oct 1, 06:29

**背景**: Matthew Green 是约翰·霍普金斯大学的知名密码学家，撰写 Cryptography Engineering 博客。沙箱是一种常见的隔离防护策略，将软件限制在受控环境中运行，但它假设威胁来自外部而非合法的共享渠道。在智能体 AI 领域，提示注入（即嵌入在智能体所读内容中的恶意指令劫持其行为）是公认尚未解决的问题。计算机蠕虫是一种无需人工干预即可在主机间自我传播的恶意软件，传统上通过网络通信进行扩散。

**标签**: `#AI safety`, `#AI agents`, `#security`, `#worm propagation`, `#sandboxing`

---

<a id="item-4"></a>
## [消息称 Anthropic 寻求最早 11 月中旬启动 IPO，争取感恩节前挂牌](https://aihot.news/items/dpbzlc983etvb4mqpdc8rly9w) ⭐️ 8.0/10

据彭博社援引知情人士消息，Anthropic 计划最早于 11 月 9 日当周启动 IPO 推介，争取在 11 月 26 日感恩节前挂牌，最迟年底前上市，此前原定夏季过后公开提交申请的计划已被推迟。部分投资者认为其合理估值约为 1.8 万亿至 2 万亿美元，公司预计 IPO 规模可达到或超过 SpaceX。 若以 1.8 万亿至 2 万亿美元估值上市，这将是有史以来规模最大的 IPO 之一，是对前沿 AI 商业模式的标志性认可，将直接影响公开市场投资者，并重塑与推迟上市计划的 OpenAI 之间的竞争格局。这也将检验公开市场能否接受 AI 实验室高增长与巨额亏损并存的特征。 彭博社看到的文件显示，Anthropic 2025 年营收约 46 亿美元（2024 年为 3.86 亿美元），但净亏损接近 420 亿美元，约为上一年的 5 倍，其中逾 340 亿美元来自负债公允价值变动这一会计项目而非现金消耗，营业亏损也扩大至 80 多亿美元。上市时间仍可能调整，近期备受关注的 AI 智能体黑客事件以及 CEO 达里奥·阿莫代伊主张放慢新模型发展的言论可能影响进程，但据报道投资者兴趣未受削弱。

rss · AI Hot · Oct 2, 02:24

**背景**: IPO 推介（roadshow）是公司上市前向机构投资者进行路演推介、以摸清认购需求并确定发行价格的阶段，而选择在感恩节前后挂牌较为罕见，因为此时市场交易活动通常明显减少。负债公允价值变动是非现金的会计调整：当公司估值上升时，被归类为负债的可转换或可赎回工具需重新估值，从而产生大额账面亏损，但并不代表实际现金消耗。Claude 模型的开发商 Anthropic 是全球估值最高的 AI 纯业务公司之一，据报道在 2026 年 5 月的 Series H 融资中估值达 9650 亿美元，而竞争对手 OpenAI 已推迟其上市计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.sofi.com/learn/content/guide-to-ipo-roadshows/">Guide to Roadshow in an IPO | SoFi</a></li>
<li><a href="https://af.net/realtime/anthropic-achieves-965-billion-valuation-amid-surging-demand-for-claude-ai/">Anthropic Achieves $965 Billion Valuation Amid Surging Demand for Claude AI | AIFOD</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#funding`, `#frontier AI`

---

<a id="item-5"></a>
## [MerchantBench 评测：顶级 LLM 智能体长周期任务表现仅达人类 27.3%](https://aihot.news/items/rluj7bjsotrt2z5b6qfwy6izm) ⭐️ 8.0/10

新发布的 MerchantBench 基准在 365 天的订单级电商模拟环境中评测了八款领先 LLM 智能体（包括 GPT-5.6 Sol 和 Claude Opus 4.8）的长期连贯性。表现最好的模型仅达到人类水平的 27.3%，暴露出长周期任务上的巨大能力差距。 长期连贯性是自主智能体投入真实商业运营的关键前提，该结果量化了当前前沿模型与人类水平可靠性之间的巨大距离。它为智能体研究提供了高信噪比的评测工具，也提醒人们对“全自主商业智能体”的宣传保持理性。 MerchantBench 基于 98,843 条真实电商商品记录构建，为智能体提供 26 个工具，并将上游供应商模拟、商家店铺和下游订单级模拟结合成 365 天的完整环境。近期研究也印证了这一结论：LLM 智能体在短、中期任务上表现良好，但在需要跨越大量步骤和决策维持连贯性的长周期任务中会明显崩溃。

rss · AI Hot · Oct 2, 02:16

**背景**: 长周期智能体基准评测的是系统在跨越大量步骤、工具调用和决策的任务上的表现，而非单轮问答式的交互。电商运营是理想的测试场景，因为它要求库存管理、供应商协调和订单处理在整整一年的模拟时间中保持一致。已有研究表明，尽管 LLM 智能体在短任务上表现出色，但在长时间跨度上维持目标、记忆和决策一致性仍是未解决的系统级难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.28956">[2607.28956] MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations - arXiv</a></li>
<li><a href="https://github.com/KhanCold/merchantbench">MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations - GitHub</a></li>
<li><a href="https://arxiv.org/html/2604.11978v1">The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break - arXiv</a></li>

</ul>
</details>

**标签**: `#LLM`, `#agents`, `#benchmark`, `#evaluation`, `#long-horizon-tasks`

---

<a id="item-6"></a>
## [Meta 提出专用控制器调度长程智能体推理，ProgramBench 提升至 71.5%](https://aihot.news/items/o35lw39ye2vs0t8c6x9pkrjcd) ⭐️ 8.0/10

Meta Superintelligence Labs 提出用一个专门的控制器来决定智能体在长程任务中的下一步行动。在相同的 worker 模型和相同预算条件下，GPT-5.5 的 ProgramBench 成绩从 63.7% 提升到 71.5%，Codex 达到 58.0%。 长程智能体任务仍是前沿 AI 的关键瓶颈，这一结果表明编排与调度——而不仅是更大的模型——也能带来显著的能力提升。该方法可广泛应用于编程智能体、自主工作流以及各类多步骤智能体系统。 提升是在不改变底层 worker 模型和计算预算的情况下取得的，从而分离出控制器本身的贡献。ProgramBench 要求根据编译后的二进制文件和文档自由重构完整程序，不提供任何提示或骨架，是对自主规划能力的严格测试。

rss · AI Hot · Oct 2, 01:30

**背景**: ProgramBench 是一个编程基准测试，要求智能体根据可执行二进制文件和行为规范重构完整的命令行程序，并通过隐藏的行为测试评分。长程智能体需要在多个步骤中持续进行规划、记忆和错误管理，此前研究显示它们在这类任务上仍不可靠。Meta Superintelligence Labs（MSL）成立于 2025 年 6 月，由 Alexandr Wang 领导，是 Meta 专注超级智能研究的部门。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://programbench.com/">ProgramBench evaluates whether language models can rebuild...</a></li>
<li><a href="https://benchmarklist.com/benchmarks/programbench/">ProgramBench Benchmark Scores & AI Model... | BenchmarkList</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs">Meta Superintelligence Labs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#long-horizon reasoning`, `#Meta Superintelligence Labs`, `#benchmark`, `#frontier AI`

---

<a id="item-7"></a>
## [Volantis 获 8800 万美元 A 轮融资，用光子互连为大模型推理提速](https://aihot.news/items/y40s3lmjacrsil82t85ncqrtn) ⭐️ 8.0/10

Volantis 宣布完成 8800 万美元 A 轮融资，累计融资达 9700 万美元，投资人包括 Sam Altman、Jeff Dean 和 John Doerr。该公司正在研发光子互连技术，为每颗芯片提供更大容量、更高带宽的内存，目标是在超过 10 万亿（10T）参数的模型上实现每用户最高每秒 10,000 tokens 的推理速度。 随着模型参数规模突破万亿级，内存带宽和互连技术（而非单纯算力）已成为推理速度的关键瓶颈。如果 Volantis 能实现其目标，目前编码智能体需要数小时才能完成的任务可能缩短到几分钟，将直接解锁下一代智能体 AI 应用。 团队在 CoWoS 先进封装、HBM（高带宽内存）以及硅光共封装光学（CPO）等半导体技术方面拥有深厚背景，且其下一代产品已完成流片。每用户 10,000 tokens/秒的目标针对的是 10T+ 参数的模型——考虑到当前前沿模型的生成速度通常仅为每秒几十到几百 tokens，这是一个相当激进的目标。

rss · AI Hot · Oct 2, 01:21

**背景**: NVIDIA 的 H100 等 AI 加速器采用台积电的 CoWoS（Chip on Wafer on Substrate）封装技术，将 GPU 裸片与堆叠式 HBM 高带宽内存集成在一起，而这类先进封装产能已成为 AI 行业的重要供应瓶颈。基于光子的互连技术，尤其是共封装光学（CPO），将光学器件直接与硅芯片集成，可实现远高于传统电互连的带宽和更低的功耗。随着 AI 算力基础设施迈入“光学时代”，将光子技术应用于 AI 内存与互连的创业公司正受到投资者的广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-mst.com/insight/advanced-packaging-chiplet-cowos-hbm/">先 进 封 装 技术详解：Chiplet、 CoWoS 与 HBM 背后的设备挑战 | 迈烁集芯</a></li>
<li><a href="https://www.moomoo.com/news/post/54915787/the-silicon-photonics-revolution-is-poised-to-take-off-and">The silicon photonics revolution is poised to take off, and the "Optical Era" is about to arrive! The AI computing Industry Chain is stepping into a new round of "bull market curve." - Moomoo</a></li>
<li><a href="https://ele-solution.com/solutions/advanced-package/cowos-hbm/">COWOS / HBM – ele-solution.com</a></li>

</ul>
</details>

**社区讨论**: 评论人士 Elvis Saravia 认为，更快的推理是编码智能体的下一个重大解锁点，原本耗时数小时的智能体任务有望在几分钟内完成。所提供的材料中没有更广泛的社区讨论。

**标签**: `#AI infrastructure`, `#photonics`, `#LLM inference`, `#funding`, `#hardware`

---

<a id="item-8"></a>
## [Google DeepMind 发布 SynthID Bio，为 AI 设计的蛋白质添加水印](https://aihot.news/items/mx1nabzkkpauikvq4ubjcpwl9) ⭐️ 8.0/10

Google DeepMind 发布了 SynthID Bio，这是一套水印方法家族，可将不可察觉的签名直接嵌入 AI 生成的蛋白质序列中，且不影响其生物功能。CEO Sundar Pichai 公开转发了该消息，并称赞其对科学诚信与生物安全的推进。 随着生成式 AI 越来越多地设计新型蛋白质和生物系统，此前一直缺乏可靠方法追溯 AI 设计序列的来源，这给科学诚信和生物安全带来了风险。SynthID Bio 将已验证的 AI 内容水印技术扩展到生物学领域，有望为科研、医药和工业中使用的合成蛋白质提供溯源能力。 据 DeepMind 介绍，这些技术在保持生物活性的同时实现了有效水印，覆盖范围包括蛋白质序列及其三维结构预测。该水印被设计为不可察觉的，即不会改变蛋白质的折叠方式或功能。

rss · AI Hot · Oct 2, 01:12

**背景**: SynthID 是 Google DeepMind 既有的水印技术，最初用于对文本、图像和音频等 AI 生成内容添加水印并加以识别，后来被其他主要 AI 公司采用。与此同时，基于大语言模型和扩散方法的 AI 模型已能生成全新的蛋白质序列（从头蛋白质设计），这加速了药物发现和研究，但也引发了对滥用的担忧。SynthID Bio 将这两条线索结合，把水印技术引入 AI 设计的生物学领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID - Google DeepMind</a></li>
<li><a href="https://www.linkedin.com/pulse/safeguarding-ai-era-biology-watermarking-building-blocks-kohli-z0yye">Safeguarding the AI Era of Biology : Watermarking the Building Blocks...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49915984">SynthID Bio : Watermarking methods for synthetic ... | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 该发布在 Hacker News 和 LinkedIn 上引发了讨论，评论者注意到其在保持生物活性的同时对序列和三维结构预测进行水印的技术成就。社区整体情绪反映了对 AI 溯源工具的兴趣，同时也存在关于此类水印在对抗蓄意移除或序列修改时稳健性的疑问。

**标签**: `#Google DeepMind`, `#AI safety`, `#protein design`, `#biotech`, `#watermarking`

---

<a id="item-9"></a>
## [Cloudflare 开源决策模型 Clef，输出类型化概率而非文本](https://aihot.news/items/t1ixwnkwkt64gce0yabfu6kps) ⭐️ 8.0/10

Cloudflare 的 Workers AI 团队以 Apache 2.0 许可证发布了其首批自训模型：Clef（27B，基于 Qwen3.8-27B）和 Clef-flash（9B）。与语言模型不同，它们是“决策模型”，针对类型化的结构化问题返回各选项的概率，而不是生成自由文本。 由大型基础设施公司发布，验证了新兴的“决策模型”范式——专为路由、升级处理等软件内决策任务构建的更小、更快、输出类型化的模型，推理成本远低于完整 LLM。开放权重还让开发者可以在本地或自己的基础设施上运行和微调这些模型。 Clef 输出严格类型化的结果，并与 TypeSafe AI 的 Jev System One API 完全兼容，因此现有集成可以轻松切换模型。Cloudflare 还在发布的同时推出了新的强化学习微调平台。

rss · AI Hot · Oct 2, 01:00

**背景**: 决策模型是一类专为在软件内部做出有边界的结构化决策而构建的新型 AI——例如对工单分类或决定是否升级处理——返回带有概率的类型化答案，调用代码可以直接据此行动，而无需解析自由文本。TypeSafe AI 的 Jev 于 2026 年 9 月发布，开创了这一类别，宣称在决策质量上与 LLM 相当，但速度快约两个数量级。开放权重模型会公开其参数文件，任何人都可以下载、运行和修改，这与仅通过 API 提供的闭源模型不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/clef-decision-models/">Introducing Clef : our open-source decision models ... | Cloudflare Blog</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>

</ul>
</details>

**社区讨论**: 围绕 TypeSafe AI Jev 的社区讨论将其描述为快速、智能的自由形式分类器（约 150ms 完成决策），开发者正在通过各语言 SDK 进行试验；也有评论者指出开放权重 LLM 已经能完成类似的分类任务，质疑专用决策模型是否具有足够优势。

**标签**: `#open-source-models`, `#AI`, `#Cloudflare`, `#decision-models`, `#model-release`

---

<a id="item-10"></a>
## [Google 首次轨道 AI 芯片试验确认在轨正常运行](https://aihot.news/items/fe27jbwrn6gfzym6j9q179auw) ⭐️ 8.0/10

Google 确认其首个轨道 AI 芯片试验已入轨并取得联系，运行符合预期。该卫星于 2026 年 10 月 1 日由 SpaceX Falcon 9 Transporter-18 任务从范登堡发射，搭载 4 颗 Trillium TPU（v6e），以每次约 15 分钟的间歇运行 Gemini 推理。 这是天基 AI 算力的前沿里程碑，证明现代数据中心级 AI 加速器能够在轨道上存活并正常工作。成功后可能为把重型 AI 工作负载迁移到太空铺路，与业界日益增长的轨道数据中心兴趣相呼应。 散热完全依赖被动方式：TPU 采用热管和红外辐射器而非风扇，因为真空中没有空气可用于对流散热。推理以约 15 分钟为周期间歇运行，之后芯片停机让辐射器散热，再进入下一轮运行。

rss · AI Hot · Oct 2, 00:44

**背景**: Trillium（TPU v6e）是 Google 的第六代张量处理器，是该公司训练和运行 Gemini 等大模型所用的定制加速器。Transporter-18 是 SpaceX 的专用小卫星拼单发射任务，将 130 个载荷送入近地轨道。在航天器上，热管是一种被动两相散热技术，通过闭合的液气循环把热量传给辐射器，再以红外辐射的方式排出——这是真空中散热的唯一途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.satellitetoday.com/launch/2026/10/01/the-first-mission-milestones-onboard-spacexs-transporter-18-rideshare-launch/">The First Mission Milestones Onboard SpaceX 's Transporter - 18 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spacecraft_thermal_control">Spacecraft thermal control - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Google`, `#Trillium TPU`, `#space computing`, `#frontier infrastructure`

---

<a id="item-11"></a>
## [腾讯向甲骨文租用 10 万枚先进 AI 芯片，价值约 70 亿美元](https://www.ft.com/content/8799b33d-f07c-4a03-82f0-bf5d3d1d29e9) ⭐️ 8.0/10

腾讯与甲骨文签订价值约 70 亿美元的五年租约，租用约 10 万枚在中国无法直接购买的先进 AI 芯片，芯片部署在东南亚多个数据中心，这是腾讯史上最大的海外租赁交易。约 30%的款项需预付，交易旨在加速其 AI 模型与智能体工具的开发。 美国出口管制禁止中国公司直接购买先进 AI 芯片，因此租用海外算力成为中国 AI 实验室维持前沿模型训练与推理能力的关键变通途径。这笔交易凸显了云端算力租用正在重塑全球 AI 算力竞争格局，也可能促使美国立法者进一步收紧相关漏洞。 租期为五年，覆盖甲骨文在东南亚运营数据中心中的约 10 万枚芯片，且约 30%的款项需预付。现行美国规则禁止向中国直接出售先进芯片，但允许中国公司在海外租用这些芯片，本交易正是利用了这一漏洞。

telegram · @zaihuapd · Oct 1, 05:07

**背景**: 自 2022 年 10 月以来，美国对向中国出口先进半导体和 AI 芯片实施了日益严格的管制，旨在减缓中国 AI 发展并保持美国领先优势。作为应对，中国企业转向云端 GPU 租赁服务，通过海外服务商远程使用被禁运的英伟达等芯片，而无需实际进口硬件。这一'云端漏洞'已引起美国国会关注，相关立法正在推进以将云端算力访问纳入出口管制。腾讯一直在积极开发 AI 模型和智能体，并将其整合进微信、QQ 及开源模型产品线中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.congress.gov/crs-product/R48642">U.S. Export Controls and China: Advanced Semiconductors | Congress.gov</a></li>
<li><a href="https://www.theregister.com/on-prem/2026/01/13/congress-votes-to-close-china-cloud-chip-export-loophole/4462528">Congress votes to close China cloud chip export loophole</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced Computing and Semiconductors to China</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Tencent`, `#AI chips`, `#Oracle`, `#export controls`

---

<a id="item-12"></a>
## [特朗普与六大科技巨头签署具有道义约束力的 AI 安全协议](https://t.me/zaihuapd/44157) ⭐️ 8.0/10

当地时间 9 月 29 日，美国总统特朗普与谷歌、Anthropic、Meta、OpenAI、xAI 和英伟达的掌门人签署了一份一页纸的人工智能安全协议，并将文件发布在 Truth Social 上。他称这份文件具有“道义约束力”。 该协议将六家最具影响力的前沿 AI 公司纳入统一的安全框架，表明美国政府倾向于以行业自愿承诺而非强制性立法来治理 AI。它可能影响整个 AI 生态系统在审计、董事会监督和能力监控方面的规范，但缺乏法律约束力也让人质疑其执行力。 协议要求企业建立四层控制机制：配合外部审计机构对 AI 管控系统进行独立评估，设立董事会独立委员会进行监督，并在模型训练和部署期间围绕网络安全、生物和化学威胁监控 AI 能力与对齐情况。值得注意的是，该协议不具法律约束力，执行主要依赖企业自律和声誉压力。

telegram · @zaihuapd · Oct 2, 01:18

**背景**: AI 对齐（AI alignment）指确保 AI 系统的行为符合人类意图和价值观，通常以鲁棒性、可解释性、可控性和道德性等原则来衡量。前沿 AI 模型能力快速增长，一旦被滥用可能带来风险，促使各国政府寻求治理机制。美国倾向于让头部 AI 公司作出自愿承诺，与其他地区更强的监管路径形成对比。Truth Social 是特朗普于 2022 年联合创立的社交平台，他经常通过该平台发布官方消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://truthsocial.com/">Truth Social</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#AI政策`, `#治理`, `#OpenAI`, `#监管`

---