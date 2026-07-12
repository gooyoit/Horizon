---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 112 items, 11 important content pieces were selected

---

1. [OpenAI GPT-5.6 Sol Ultra 不到一小时证明 50 年历史数学猜想](#item-1) ⭐️ 10.0/10
2. [OpenAI 发布 GPT-5.6 系列，旗舰模型 Sol 全面升级](#item-2) ⭐️ 10.0/10
3. [人形机器人远程完成全球首例活体动物手术](#item-3) ⭐️ 9.0/10
4. [Sam Altman 称 GPT-5.6 的医学回复比人类医生更少出错](#item-4) ⭐️ 9.0/10
5. [vLLM v0.25.0 将 Model Runner V2 设为默认路径并移除 PagedAttention](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab 发布技术白皮书：以可定制模型权重构建以人为本的 AI](#item-6) ⭐️ 8.0/10
7. [BestBlogs 7 月 12 日早报：PIPO 架构、百炼网关、AMD 运行 DeepSeek V4](#item-7) ⭐️ 8.0/10
8. [微软和 Meta 向 CoreWeave 与 Nebius 承诺 1222 亿美元 AI 算力投资](#item-8) ⭐️ 8.0/10
9. [智谱 CEO 唐杰发内部信，阐述后 Coding 时代 AGI 路线图](#item-9) ⭐️ 8.0/10
10. [智谱创始人唐杰启动:“摸高计划”：不登顶就是失败](#item-10) ⭐️ 8.0/10
11. [Claude Code 桌面版新增内置沙盒浏览器](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI GPT-5.6 Sol Ultra 不到一小时证明 50 年历史数学猜想](https://www.ithome.com/0/975/646.htm) ⭐️ 10.0/10

7 月 10 日，OpenAI 宣布其 GPT-5.6 Sol Ultra 模型在不到一小时内，独立生成了图论领域悬而未决 50 多年的“循环双覆盖猜想”的完整证明。该模型利用了包含 64 个并行子智能体的多智能体架构，其中包含负责寻找逻辑漏洞的对抗智能体，且全程在禁止联网的情况下完成了证明。 如果得到数学界验证，这标志着大型语言模型首次独立解决了一个被列入维基百科“未解决数学问题”列表的重大数学难题。这展示了 AI 推理和自主解决问题能力的空前飞跃，将 AI 的角色从人类协作者转变为独立的科学研究者。 该证明将原猜想归约为三次图问题，利用了 8-流定理，并通过 GF(3)（三元有限域）上的线性代数构造边标记来完成推导。据估算其计算成本约在 275 至 485 美元之间，但目前该证明缺乏正式的同行评审，没有引用任何已有文献，且尚未经过 Lean 等形式化证明工具的机器验证。

rss · IT HOME · Jul 12, 00:44

**背景**: 循环双覆盖猜想由 George Szekeres（1973 年）和 Paul Seymour（1979 年）分别独立提出，该猜想断言对于任意无桥图，都存在一组循环使得图中的每一条边都恰好出现在两个循环中。它是图论中最著名的公开难题之一。并行子智能体执行是一种多智能体模式，由一个协调 AI 系统生成多个专门的子智能体，同时针对同一问题的不同方法展开工作，从而大大增强了系统探索多种解决方案的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover">Cycle double cover - Wikipedia</a></li>
<li><a href="https://www.ai21.com/glossary/ai-agent/what-is-parallel-subagent-execution/">What is Parallel Subagent Execution? | AI 21</a></li>

</ul>
</details>

**社区讨论**: 数学家 Thomas Bloom 赞扬该证明非常漂亮且简洁，并指出 AI 最大的优势在于拥有远超人类的耐心去不断尝试各种细微变化，而不是提出全新的数学概念。然而，他和其他专家仍保持谨慎态度，指出了证明中缺乏文献引用的问题，并强调上传 PDF 与通过严格的同行评审截然不同，特别是考虑到该猜想历史上曾多次出现存在漏洞的错误证明。

**标签**: `#AI`, `#Frontier AI`, `#Mathematical Reasoning`, `#Multi-Agent Systems`, `#OpenAI`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.6 系列，旗舰模型 Sol 全面升级](https://t.me/zaihuapd/42497) ⭐️ 10.0/10

OpenAI 发布了 GPT-5.6 模型系列，旗舰模型 Sol 提供最强能力，Terra 平衡性能与成本，Luna 面向高并发低成本场景。该系列引入了 max/ultra 推理模式、多智能体协作和 Programmatic Tool Calling，以更少 token 和更低成本完成复杂任务。 此次发布标志着前沿 AI 能力的重大飞跃，尤其在代码、科研、设计和网络安全领域，同时大幅优化了性能成本比。多智能体协作和程序化工具调用的引入，表明 AI 正向更自主、面向工作流的系统转变，能够端到端地编排复杂任务。 GPT-5.6 将默认指向 Sol 模型，该模型在知识工作和复杂推理方面提供最强综合能力。Programmatic Tool Calling 允许模型编写 Python 脚本，在沙箱环境中编排整个工作流，支持多次工具调用及前后处理逻辑，无需将每个中间结果返回给模型。

telegram · @zaihuapd · Jul 11, 13:34

**背景**: Programmatic Tool Calling 是一种高级技术，LLM 通过编写和执行代码来编排工具工作流，而非逐个处理每次工具调用——这能降低多步任务的延迟和 token 消耗。LLM 中的多智能体协作是指多个 AI 智能体协同解决复杂任务，从孤立的模型交互转向以协作为中心的结构化方法。分层模型策略（旗舰型、平衡型、轻量型）反映了行业内提供不同性能成本权衡的模型家族以服务多样化场景的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling?ref=blog.lai.so">Programmatic tool calling - Claude Docs</a></li>
<li><a href="https://arxiv.org/abs/2501.06322">[2501.06322] Multi-Agent Collaboration Mechanisms: A Survey of LLMs</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is Multi-Agent Collaboration? | IBM</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#Frontier AI`, `#Large Language Models`, `#Multi-Agent`

---

<a id="item-3"></a>
## [人形机器人远程完成全球首例活体动物手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生通过远程操控宇树 G1 人形机器人，成功在活猪身上完成了微创胆囊切除手术，这是通用人形机器人首次被用于活体动物手术。该临床前试验结果已发表在《自然》期刊上。 这一突破表明，低成本的通用人形机器人能够执行目前仅由达芬奇等昂贵专用手术机器人完成的复杂外科手术。加州大学圣地亚哥分校的研究人员表示，这种方案未来有望将远程手术能力部署到农村、战场甚至太空等资源有限的环境中。 宇树 G1 基础款起售价约为 13500 美元，配备灵巧手后约 67000 美元，远低于造价在 50 万至数百万美元之间的专用手术机器人。G1 高约 1.5 米、重约 27 公斤，占用空间小，适合在手术室中使用。

telegram · @zaihuapd · Jul 11, 02:29

**背景**: 由 Intuitive 公司制造的达芬奇手术系统是目前机器人辅助微创手术的金标准，但其高昂的造价使许多医院和地区望而却步。远程手术技术允许外科医生在控制台前操纵机械臂，远程复制手部动作，从而实现医生与患者物理分离的手术操作。宇树 G1 是一款通用人形机器人，最初面向研究和敏捷性任务设计，具备 23 个自由度和力位混合控制能力。将这样一个多功能、量产化的平台改造用于手术，有望大幅降低机器人手术系统的准入门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intuitive.com/en-us/products-and-services/da-vinci">Da Vinci Robotic Surgical Systems | Intuitive</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8075759/">Telesurgery and Robotics: An Improved and Efficient Era - PMC</a></li>

</ul>
</details>

**标签**: `#Humanoid Robotics`, `#Embodied AI`, `#Teleoperation`, `#Medical Robotics`, `#Frontier Tech`

---

<a id="item-4"></a>
## [Sam Altman 称 GPT-5.6 的医学回复比人类医生更少出错](https://twitter.com/sama/status/tweet-2075985056846451123) ⭐️ 9.0/10

OpenAI 首席执行官 Sam Altman 表示，医生们在评估中发现，即将发布的 GPT-5.6 模型生成的回复比人类医生撰写的回复缺陷更少。这一说法直接引用了这款未发布前沿模型的医学推理能力，暗示其在专家级表现上实现了重大飞跃。 医疗保健是人工智能应用中风险最高的领域之一，在基于文本的医学推理方面超越人类医生的准确性将是该行业的一个分水岭。如果得到验证，这一能力可能会从根本上改变全球的临床决策支持、医学教育和分诊系统。 据报道，GPT-5.6 提供了 Sol、Terra 和 Luna 等多种模型变体，其中 Sol Ultra 在 TerminalBench 2.1 上达到了 91.9%。然而，Altman 的推文并未说明评估方法、样本量、测试的医学专科，以及对比是否使用了获得委员会认证的医生。

twitter · Sam Altman · Jul 11, 16:46

**背景**: 前沿 AI 模型代表了最先进的通用人工智能系统，在推理、规划和多模态生成方面展现出强大的能力。在医疗领域，AI 模型在医学执照考试和临床病例评估等基准测试中不断取得进步，尽管实际部署仍需应对复杂的监管、伦理和患者安全等问题。OpenAI 一直在将其最新模型定位用于专业专家领域，GPT-5.6 已在编程、科学和网络安全等增强能力方面进行了预览展示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#GPT-5`, `#Healthcare AI`, `#Frontier Models`

---

<a id="item-5"></a>
## [vLLM v0.25.0 将 Model Runner V2 设为默认路径并移除 PagedAttention](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 (MRv2) 设为所有密集模型的默认执行路径，并正式移除了传统的 PagedAttention 实现。该版本还引入了全新的流式解析器引擎、面向异构词表的通用投机解码，并新增了对 LLaVA-OneVision-2 和 GLM-5 等模型的支持。 该版本是这一关键开源 AI 推理引擎的重大架构里程碑，从根本上提升了执行效率和模块化程度。通过使 Transformers 后端达到与原生 vLLM 同等的速度并增强投机解码功能，它显著优化了生产级 AI 基础设施的部署成本和延迟。 此次更新为 MRv2 带来了实时嵌入、多模态前缀双向注意力以及兼容完整 CUDA 图的动态投机解码等功能。此外，Rust 前端日趋成熟，增加了对 HTTPS/mTLS 和数据并行 (DP) 监督器的支持，同时 Transformers 后端也获得了 FP8 MoE 支持。

github · vllm-project/vllm · Jul 11, 20:06

**背景**: vLLM 是一个广受欢迎的开源库，专为大型语言模型 (LLM) 的快速高效推理和服务而设计。PagedAttention 是 vLLM 最初的基础技术，受操作系统分页机制启发来管理注意力的键值内存，但随着时间推移积累了技术债务。Model Runner V2 (MRv2) 是对 vLLM 执行核心的全面重构，基于第一性原理构建，旨在实现更简洁、更模块化和更高效的运行。投机解码是一种优化技术，它使用较小的草稿模型并行预测 token，从而降低受限于内存的推理延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/">Speculative Decoding - vLLM</a></li>

</ul>
</details>

**标签**: `#vllm`, `#ai-infrastructure`, `#inference`, `#open-source`, `#llm`

---

<a id="item-6"></a>
## [Thinking Machines Lab 发布技术白皮书：以可定制模型权重构建以人为本的 AI](https://aihot.virxact.com/items/cmrh31svh018lbid4ddim1j5g) ⭐️ 8.0/10

由前 OpenAI 首席技术官 Mira Murati 创立的 Thinking Machines Lab 发布了题为《值得构建的未来是人性化的》的技术白皮书，将人类参与、模型所有权和去中心化对齐定位为核心技术挑战。文章将这些概念与交互模型及 Tinker 的 LoRA 微调技术挂钩，使团队能够自行训练并保留专属的模型权重。 这一方法代表了从中心化、一刀切式 AI 模型向去中心化生态系统的重要哲学与技术转变，在该生态中各组织可以拥有并对齐自己的 AI 系统。通过利用 LoRA 等高效微调技术，这一愿景实现了 AI 定制的民主化，有望重塑企业部署和控制 AI 解决方案的方式。 该技术提案特别强调了 LoRA（低秩适应），这是一种基于适配器的技术，允许在不修改所有参数的情况下对大型语言模型进行高效微调，从而大幅降低计算成本。这使得实用的去中心化对齐成为可能，各个团队可以创建既保留基础模型能力又反映其特定价值观和需求的专业化模型。

rss · AI Hot · Jul 12, 00:46

**背景**: LoRA（低秩适应）是深度学习中一种流行的微调方法，它通过冻结原始模型权重并注入可训练的秩分解矩阵，使预训练模型能够适应更具体的任务。这种方法使得各组织在计算上能够可行地定制像 LLM 这样的大规模模型。与传统中心化控制不同，去中心化 AI 对齐旨在确保所有人都能访问 AI，并通过促进分布式开发和人在回路系统来避免垄断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)">Fine - tuning (deep learning) - Wikipedia</a></li>
<li><a href="https://www.vincentweisser.com/dagi">Decentralized AGI Alignment - Navigating the Complex Path towards a Positive Future - Vincent Weisser</a></li>

</ul>
</details>

**标签**: `#Thinking Machines Lab`, `#Human-Centered AI`, `#Model Customization`, `#LoRA Fine-tuning`, `#AI Alignment`

---

<a id="item-7"></a>
## [BestBlogs 7 月 12 日早报：PIPO 架构、百炼网关、AMD 运行 DeepSeek V4](https://aihot.virxact.com/items/cmrh27uzb0139bid4wm340xk2) ⭐️ 8.0/10

小红书提出了 PIPO 架构，在 Qwen 基座上实现长链路 LLM 推理输入减半、单步输出翻倍；阿里巴巴百炼网关利用 RocketMQ LiteTopic 将大模型限流比降低了 10 倍。此外，LMSYS 展示了通过 ROCm Miles 堆栈将 DeepSeek V4 Flash RL 训练移植到 AMD Instinct MI355X GPU 上。 这些进展共同推动了 LLM 效率、基础设施可扩展性和硬件多样性的边界——这是 AI 行业的三大关键瓶颈。PIPO 的输入压缩和百炼网关的限流改进直接降低了推理成本，而在 AMD 硬件上运行 DeepSeek V4 则证明 NVIDIA 生态的可行替代方案正在快速成熟。 PIPO 在 Qwen 基座上进行了验证，并在 AIME 2025 基准测试中显示出可衡量的提升，专门针对并行处理输入 token 的预填充阶段。DeepSeek V4 向 AMD MI355X 的移植通过 ROCm Miles 堆栈中的稳定多节点并行策略在四个节点上完成了验证，证明了非 NVIDIA 训练集群的生产就绪能力。

rss · AI Hot · Jul 11, 23:29

**背景**: LLM 推理分为两个阶段：预填充阶段并行处理所有输入 token，解码阶段逐个生成输出 token，后者往往无法充分利用 GPU 算力。Apache RocketMQ 5.5.0 引入了 LiteTopic 作为一种轻量级消息模型，旨在通过事件驱动分发和会话持久化来处理数百万个 AI Agent 会话。AMD 的 ROCm 是一个开源软件栈，相当于 NVIDIA CUDA 的竞品，MI355X 是 AMD 最新的 Instinct 系列数据中心 GPU，旨在直接与 NVIDIA 的 Hopper 和 Blackwell 架构竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alibabacloud.com/blog/apache-rocketmq-5-5-0-open-source-litetopic-dedicated-channel-for-millions-of-ai-sessions_603233">Apache RocketMQ 5.5.0 Open Source LiteTopic : Dedicated Channel...</a></li>
<li><a href="https://www.lmsys.org/blog/2026-07-10-rocm-miles-dsv4/">Bringing DeepSeek-V4 Flash RL Training to AMD Instinct... - LMSYS Org</a></li>

</ul>
</details>

**标签**: `#LLM Optimization`, `#AI Agents`, `#DeepSeek`, `#AI Infrastructure`, `#Local AI`

---

<a id="item-8"></a>
## [微软和 Meta 向 CoreWeave 与 Nebius 承诺 1222 亿美元 AI 算力投资](https://aihot.virxact.com/items/cmrgxlh33000jbiunakl0v2ml) ⭐️ 8.0/10

微软和 Meta 已向 CoreWeave 和 Nebius 等 neocloud 提供商承诺了高达 1222 亿美元的资金，以获取最前沿的 AI 算力，其中 CoreWeave 预计 2026 财年营收为 126 亿美元，Nebius 为 34 亿美元。这些 neocloud 具备快速部署优势，CoreWeave 可在收到芯片后两周内提供算力，并计划率先在 6 月初运行 NVIDIA 的 Vera Rubin 系统。 这一巨额承诺约相当于 AWS 过去十二个月营收的 90%，表明领先的 AI 实验室愿意锁定前所未有的资金以确保优先获得最新 GPU 基础设施。然而，neocloud 高度依赖涉及 NVIDIA 股权投资、超大规模云服务商合同和 GPU 抵押债务的循环融资模式，引发了可能影响整个 AI 算力供应链的系统性可持续性担忧。 NVIDIA 已分别向 CoreWeave 和 Nebius 各投资 20 亿美元，两家公司计划到 2030 年各自部署超过 5 GW 的数据中心容量。仅 2025 年 GPU 抵押债务就达到 650 亿美元，批评者警告这种 neocloud 以 GPU 为抵押借款购买更多 NVIDIA 芯片的循环融资模式，与 2008 年动摇市场的抵押贷款支持证券有着令人不安的相似之处。

rss · AI Hot · Jul 11, 22:07

**背景**: Neocloud 是专注于 GPU 即服务（GPUaaS）的专业云提供商，提供现代 AI 工作负载所需的高性能计算、网络和存储能力。与传统超大规模云服务商不同，neocloud 优先考虑最新 GPU 架构的部署速度，因此对竞相训练前沿模型的 AI 实验室极具吸引力。NVIDIA 的 Vera Rubin 系统将于 2026 年下半年全面投产，在原始性能和成本效率上代表了对 Blackwell 的下一代飞跃。循环融资模式的运作方式如下：NVIDIA 投资 neocloud，后者利用 GPU 抵押债务购买更多 NVIDIA 硬件，同时微软和 Meta 等超大规模云服务商签署巨额合同，为保证进一步借贷提供收入保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://247wallst.com/investing/2026/06/17/wall-street-is-doing-to-gpus-what-it-did-to-mortgages-before-2008/">Wall Street Is Doing to GPUs What It Did to Mortgages... - 24/7 Wall St.</a></li>
<li><a href="https://drivenets.com/resources/education-center/what-are-neocloud-providers/">Understanding Neocloud offering GPU-as-a-Service (GPUaaS)</a></li>
<li><a href="https://genera.video/blog/nvidia-vera-rubin-ai-system">Nvidia Vera Rubin : 5x Faster Than Blackwell and... | Genera AI</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Neoclouds`, `#Compute Scaling`, `#Datacenters`, `#AI Investment`

---

<a id="item-9"></a>
## [智谱 CEO 唐杰发内部信，阐述后 Coding 时代 AGI 路线图](https://36kr.com/newsflashes/3891162734689031?f=rss) ⭐️ 8.0/10

2026 年 7 月 11 日，智谱创始人唐杰发布主题为《巨浪已来》的内部信，正式宣布公司将战略重心从短期商业化变现转向 AGI 的三大核心前沿领域：长程任务、完全自治的智能体系统以及自我进化。这一公告发布之际，智谱的市值自 IPO 以来已飙升 10 倍，在成功发布并开源 GLM-5.2 模型后，成功跻身万亿港元俱乐部。 这封内部信提供了洞察中国顶尖 AI 实验室战略路线图的高价值信号，表明顶级 AI 竞赛正从聊天范式和代码能力向自主、长周期的 AI 系统转移。通过明确提出“摸高”计划并选择在基础 AGI 研究上投入而非追求即时应用变现，智谱正押注于一条由自我进化模型和自主智能体彻底重塑行业边界与操作系统的演进路径。 唐杰将 AGI 定义为全人类智慧水平的总和，具备创造出“相对论”级别原创知识的能力，并明确了必须翻越的三座技术高峰。公司将“AI 训练 AI”视为自我进化的终极目标，即模型自己编写代码、清洗数据并自我训练，从而最大化迭代速度并在能力上拉开代际差距。

rss · 36kr · Jul 11, 11:35

**背景**: 智谱目前的市场成功很大程度上归功于其在 2025 年初对 Coding 和 Reasoning 能力的早期押注，此前业界意识到在 DeepSeek R1 发布后，Chat 范式已基本达到极限。这一战略转向取得了巨大成功，最终促成了 GLM-5.2 的发布，这是一款专为编程和智能体工作负载构建的旗舰开源模型，拥有 100 万个 Token 的上下文窗口，足以媲美 Claude 和 GPT 系列等西方顶尖模型。长程任务代表了 AI 研究的一个重要前沿，要求系统在数周、数月甚至数年的 extended periods（延长期）内，在无需人类持续干预的情况下规划并执行复杂目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eigent.ai/blog/glm-5-2">GLM - 5 . 2 : Zhipu AI 's 1M-Token Open-Weight Coding Model</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">deepseek -ai/ DeepSeek - R 1 · Hugging Face</a></li>
<li><a href="https://www.c-sharpcorner.com/article/what-are-long-horizon-ai-agents-and-how-do-they-work-in-real-life/">What Are Long - Horizon AI Agents and How Do They Work in Real Life?</a></li>

</ul>
</details>

**标签**: `#Zhipu AI`, `#AGI`, `#Autonomous Agents`, `#AI Strategy`, `#Frontier AI`

---

<a id="item-10"></a>
## [智谱创始人唐杰启动:“摸高计划”：不登顶就是失败](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 8.0/10

Zhipu AI founder Tang Jie announced an internal 'Touch High' initiative focused on achieving AGI by conquering long-range tasks, autonomous agents, self-training, and investing heavily in mechanistic interpretability for model safety.

telegram · @zaihuapd · Jul 11, 13:59

**标签**: `#AGI`, `#Zhipu AI`, `#Mechanistic Interpretability`, `#AI Safety`, `#AI Strategy`

---

<a id="item-11"></a>
## [Claude Code 桌面版新增内置沙盒浏览器](https://x.com/ClaudeDevs/status/2075635283211772279) ⭐️ 8.0/10

Anthropic 在 Claude Code 桌面应用程序中直接新增了内置的沙盒浏览器。这使得 AI 代理能够自主打开、阅读并与网站、设计文件和本地开发服务器进行交互，而无需用户切换上下文或手动复制粘贴内容。 此次更新通过打破代码执行与网络交互之间的壁垒，显著增强了 Claude Code 的代理能力。开发者现在可以依赖 AI 在本地服务器上直观地验证 UI 变更，或直接从基于网页的文档中获取上下文，从而简化整个开发工作流程。 该浏览器在安全的沙盒环境中运行，以确保网络内容的安全执行。用户可以自行配置 AI 是否在多次交互中保留浏览会话，从而更好地控制状态和数据持久化。

telegram · @zaihuapd · Jul 11, 14:34

**背景**: Claude Code 是 Anthropic 推出的一款智能体编程工具，旨在帮助开发者理解代码库、编辑文件和运行终端命令。AI 沙盒提供了一个隔离且安全的环境，使 AI 代理能够在不危及主机系统的情况下执行浏览器自动化等任务。通过将沙盒浏览器直接集成到编程环境中，Anthropic 免去了开发者在处理 Web 相关任务时对外部浏览器自动化工具或复杂容器配置的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://blogs.novita.ai/can-i-use-an-ai-sandbox-for-browser-automation/">Can I Use an AI Sandbox for Browser Automation? - Novita</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI Agents`, `#Anthropic`, `#Web Interaction`, `#Developer Tools`

---