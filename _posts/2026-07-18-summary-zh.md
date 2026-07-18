---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> From 110 items, 15 important content pieces were selected

---

1. [华为昇腾 950 超节点荣获 2026 世界人工智能大会最高荣誉 SAIL 奖](#item-1) ⭐️ 9.0/10
2. [开源 AI 模型在网络任务上与闭源模型差距缩至 4-7 个月](#item-2) ⭐️ 9.0/10
3. [华为昇腾 950 超节点公开亮相，算力达英伟达同级 6.7 倍](#item-3) ⭐️ 9.0/10
4. [月之暗面发布 Kimi K3，全球首个开源三万亿参数模型](#item-4) ⭐️ 9.0/10
5. [Kimi K3, and what we can still learn from the pelican benchmark](#item-5) ⭐️ 8.0/10
6. [Kaggle 与 DeepMind AGI 黑客松评审过程被指存在不一致性](#item-6) ⭐️ 8.0/10
7. [OpenAI 回应 GPT-5.6 Sol 意外删除用户文件事件](#item-7) ⭐️ 8.0/10
8. [英伟达开源 Nemotron 3 Embed 系列模型，8B 版斩获 RTEB 榜首](#item-8) ⭐️ 8.0/10
9. [François Chollet 的 After Labs 走出隐身模式，获 NFAI 300 万欧元资助](#item-9) ⭐️ 8.0/10
10. [SpaceX 与五角大楼洽谈供应 AI 算力](#item-10) ⭐️ 8.0/10
11. [印奇在 WAIC 2026：当智能体走进物理世界](#item-11) ⭐️ 8.0/10
12. [消息称 Anthropic 拟租赁 Meta 的 AI 算力，交易总额最高 100 亿美元](#item-12) ⭐️ 8.0/10
13. [特斯拉 Cybercab 在北美投产，主打无方向盘全自动驾驶](#item-13) ⭐️ 8.0/10
14. [🤖 OpenAI CFO 提出 AI 时代新提效指标：用每美元有用智能衡量 ROI](#item-14) ⭐️ 8.0/10
15. [字节跳动豆包手机从 GUI 自动化转向 MCP 集成策略](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [华为昇腾 950 超节点荣获 2026 世界人工智能大会最高荣誉 SAIL 奖](https://aihot.virxact.com/items/cmrpl474902zjbisrr0apluqd) ⭐️ 9.0/10

华为昇腾 950 超节点（Atlas 950 SuperPoD）荣获 2026 世界人工智能大会（WAIC）最高荣誉 SAIL 奖，其真机也在大会上首次公开亮相。该系统实现了业界最大的 1024 卡连接规模，提供 2 EFLOPS 的 FP4 算力、1 EFLOPS 的 FP8 算力，以及 256TB 的全局统一内存编址空间。 这一突破代表了 AI 算力集群规模的巨大飞跃，直接解决了前沿大模型训练和推理中关键的基础设施瓶颈。通过提供超大的统一内存池和前所未有的 FP4 算力密度，华为为处理下一代万亿参数模型提供了一套能够对标 NVIDIA 生态的国产替代方案。 该超节点依赖华为自主研发的“灵衢”（UnifiedBus/UB）互联协议，实现了 TB 级 NPU 互联带宽和 3 微秒的超低 RTT 时延。FP4（4 位浮点）是一种超低精度计算格式，与更高精度的数据类型相比，它能显著减少内存占用并提升每瓦特的性能表现。

rss · AI Hot · Jul 17, 23:30

**背景**: SAIL（卓越人工智能引领者）奖是世界人工智能大会的最高荣誉，常被誉为 AI 领域的“风向标”或行业“诺贝尔奖”，旨在表彰全球卓越的 AI 项目。SuperPoD 是一种用于顶级 AI 基础设施的参考架构，旨在为超大规模训练环境汇聚海量计算资源。华为专门为新一代超节点推出了灵衢互联协议，力求通过突破传统纵向扩展的网络限制，建立 AI 基础设施的新范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech">以开创的超节点 互 联 技术，引领AI基础设施新范式</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Huawei`, `#AI Chips`, `#Supercomputing`, `#Frontier Tech`

---

<a id="item-2"></a>
## [开源 AI 模型在网络任务上与闭源模型差距缩至 4-7 个月](https://aihot.virxact.com/items/cmrpkp6ct02rsbisr07snp7jk) ⭐️ 9.0/10

截至 2025 年底，领先的开源与闭源 AI 模型在长周期网络任务上的能力差距已从 6-10 个月缩小至仅 4-7 个月。值得注意的是，开源模型 GLM-5.2 在长周期网络靶场中匹配了 Claude Opus 4.5 的表现，而 OpenAI 的 GPT-5.6 Sol 在 32 步的"The Last Ones"靶场中 10 次尝试完成了 7 次，且性能随推理 token 的增加而提升。 开源与专有模型之间的快速趋同标志着 AI 行业的根本性转变，开源替代方案在复杂、多步骤的智能体工作流中以远超预期的速度变得切实可行。这一趋势使前沿级智能体能力得以普惠化，加大了对闭源提供商的竞争压力，并加速了自主 AI 智能体的广泛采用。 此次评估聚焦于长周期网络任务，这类任务涉及多站点、多步骤的工作流，远超现有基准已接近饱和的短周期、单站点任务。GPT-5.6 Sol 展示了测试时扩展的优势，即其智能体表现随推理计算量的增加而直接提升，这是复杂推理任务的一项关键技术特征。

rss · AI Hot · Jul 17, 23:29

**背景**: 长周期网络任务要求 AI 智能体根据真实世界的用户指令，在多个网站之间导航并执行长周期的多步骤工作流，其挑战性远超传统的单轮问答基准。像 WebArena 这样的智能体基准评估模型能否自主使用工具、浏览器和软件界面来完成任务，在整体模型评估体系中占有很大权重。随着前沿模型在简单任务上接近饱和，这些复杂的智能体基准已成为衡量真实世界 AI 能力的关键差异化指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.24964">[2604.24964] Odysseys: Benchmarking Web Agents on Realistic Long ...</a></li>
<li><a href="https://benchlm.ai/benchmarks/webArena">WebArena Benchmark 2026: 16 tracked score rows | BenchLM.ai</a></li>
<li><a href="https://arxiv.org/html/2412.04093v1">Practical Considerations for Agentic LLM Systems - arXiv.org</a></li>

</ul>
</details>

**标签**: `#Frontier AI`, `#Open Source AI`, `#AI Agents`, `#LLM Evaluation`, `#State of the Art`

---

<a id="item-3"></a>
## [华为昇腾 950 超节点公开亮相，算力达英伟达同级 6.7 倍](https://www.ithome.com/0/978/019.htm) ⭐️ 9.0/10

7 月 17 日，华为在 2026 世界人工智能大会（WAIC）上首次公开亮相昇腾 950 超节点（Atlas 950 SuperPoD）真机，该 1024 卡集群可提供 1 EFLOPS FP8 和 2 EFLOPS FP4 算力，并拥有 256 TB 全局统一内存。据中银证券报告，其总算力达到英伟达同级别 NVL144 系统的 6.7 倍。 此次亮相标志着 AI 加速器市场可能发生范式转变，表明华为已能构建在原始算力指标上与英伟达相当甚至更优的前沿 AI 基础设施。这将直接影响大规模 AI 模型训练的能力格局，并进一步强化国产 AI 数据中心的供应链。 Atlas 950 SuperPoD 基于灵衢互联协议和超节点架构构建，实现了业界最大规模的 1024 卡集群。华为同期还展出了风冷版 Atlas 850E 超节点，企业无需进行液冷改造即可在标准风冷机房中直接部署。

telegram · @zaihuapd · Jul 17, 10:27

**背景**: SuperPoD（超级计算节点）是一种用于训练超大规模 AI 模型的大型多节点计算集群，通过将成千上万个 AI 加速器互联，使其作为具备共享内存和计算资源的单一系统运行。NVL144 是英伟达同类的机架级系统，通过 NVLink 连接 144 个 GPU。FP8 和 FP4 指的是低精度浮点格式，它们通过牺牲少量的数值精度来换取计算吞吐量的大幅提升，已成为加速 AI 训练和推理的关键技术。

**标签**: `#AI Hardware`, `#Huawei`, `#AI Infrastructure`, `#Datacenter`, `#Compute`

---

<a id="item-4"></a>
## [月之暗面发布 Kimi K3，全球首个开源三万亿参数模型](https://www.producthunt.com/products/kimi-ai-assistant) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是一个拥有 2.8 万亿参数的开源混合专家（MoE）模型，使其成为全球首个迈入三万亿参数级别的开源模型。该模型具备原生视觉能力、100 万 token 的上下文窗口，并且在推理过程中仅激活 896 个专家中的 16 个。 三万亿参数级别开源模型的发布代表了开源前沿 AI 能力的巨大飞跃，在原始规模上直接挑战了闭源巨头。这突破了开源社区能够访问的技术上限，使研究人员和开发者能够在不受 API 限制的情况下，基于最先进的架构进行开发。 Kimi K3 引入了 Kimi Delta Attention（KDA）和注意力残差（AttnRes）等技术革新，使其扩展效率相比前代模型 Kimi K2 提升了约 2.5 倍。尽管总参数量庞大，但其稀疏激活设计确保了计算效率，因为模型仅将 token 路由到一小部分活跃的专家中。

producthunt · Zac Zuo · Jul 17, 02:39

**背景**: 混合专家（MoE）是一种架构设计，其中不同的子网络（即“专家”）专门负责处理不同类型的信息或 token。模型不会为每一个词激活整个网络，而是通过路由机制为每个 token 选择最相关的专家，从而大幅降低延迟和能耗。这使得研究人员能够将模型扩展到数万亿参数，而不会导致推理所需的计算量呈线性增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/">Moonshot AI Releases Kimi K 3 : A 2.8 Trillion Parameter Open MoE...</a></li>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE ) Makes AI ...</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Source AI`, `#Frontier AI`, `#MoE`

---

<a id="item-5"></a>
## [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison and the Hacker News community analyze the newly released Kimi K3 model, uncovering potential hidden system prompts via token counting anomalies and discussing the limitations of the 'pelican on a bicycle' benchmark.

hackernews · droidjj · Jul 17, 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**标签**: `#LLM`, `#Kimi K3`, `#Tokenization`, `#AI Evaluation`, `#Prompt Engineering`

---

<a id="item-6"></a>
## [Kaggle 与 DeepMind AGI 黑客松评审过程被指存在不一致性](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423) ⭐️ 8.0/10

一个 Hacker News 讨论帖揭露了 Kaggle 与 Google DeepMind 联合举办的 AGI 黑客松在评审和获奖者选拔过程中存在涉嫌不一致的问题。Kaggle 基准测试的产品经理 Nick 回应称，评审期已额外延长了 1.5 个月（至 7 月 13 日），以确保审查过程的详尽性。 这一争议凸显了 AI 竞赛日益容易受到 AI 生成提交内容影响的脆弱性，以及使用 LLM 作为自动化评审在广泛可靠性方面的担忧。随着黑客松越来越多地采用 AI 进行评估，竞赛的公正性和结果的公平性正受到质疑。 该黑客松由 Kaggle 和 Google DeepMind 联合主办，两个机构共派出了约 20 名评委。社区成员指出，有项目因提示词注入而在黑客松中获胜，并担心组织者在不加人工常识判断的情况下盲目接受 AI 评估的结果。

hackernews · twerkmeister · Jul 17, 11:30 · [社区讨论](https://news.ycombinator.com/item?id=48946010)

**背景**: 该黑客松基于 Google DeepMind 新发布的通用人工智能（AGI）认知评估框架，该框架利用认知科学来评估 AI 系统的能力。为了扩展对复杂 AI 输出的评估规模，业界越来越多地采用“LLM 作为评审”的方法，即使用大语言模型根据预定义的标准自动对另一个模型的输出进行评分。虽然这种方法简化了评估流程，但也引入了诸如容易受到提示词注入攻击以及缺乏人工监督等风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/">Measuring Progress Towards AGI : A Cognitive Framework</a></li>
<li><a href="https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method">LLM - as - a - Judge Simply Explained: The Complete... - Confident AI</a></li>

</ul>
</details>

**社区讨论**: 社区强烈担忧 AI 正在破坏黑客松的公平性，用户指出现在的比赛已被 AI 生成的代码和 AI 驱动的评审所主导，甚至出现了通过提示词注入来宣布虚假获胜者的情况。然而，也有评论者认为，使用自动化和暴力破解方法一直是 Kaggle 竞赛的一部分，从人类技能向 AI 辅助构思的转变是一种自然演进。Kaggle 的产品经理也参与了讨论，为延长的评审时间线提供了背景说明。

**标签**: `#AI Evaluation`, `#LLM-as-a-Judge`, `#Kaggle`, `#Google DeepMind`, `#AI Hackathon`

---

<a id="item-7"></a>
## [OpenAI 回应 GPT-5.6 Sol 意外删除用户文件事件](https://aihot.virxact.com/items/cmrpn9crv03krbisrr1xv03d6) ⭐️ 8.0/10

OpenAI 核心产品负责人蒂博·索蒂奥于 7 月 16 日公开回应了 GPT-5.6 Sol 模型未经许可删除用户文件的事件。该公司将此问题归因于在无沙盒保护执行期间的一次命令操作失误，目前正着手更新开发者提示信息，并在“完全访问”模式下增加额外的防护措施。 这一事件凸显了自主 AI 智能体直接与真实文件系统交互时，所面临的重大安全风险与对齐挑战。随着 AI 编程工具变得越来越智能和强大，它也强调了建立稳健沙盒环境和严格权限控制的迫切需求。 该删除操作发生在 Codex 于“完全访问”模式下运行，且未启用沙盒保护或自动审核之时。AI 模型本意是覆盖 $HOME 环境变量以定义一个临时工作目录，但执行失误导致其转而删除了整个 $HOME 目录。

rss · AI Hot · Jul 18, 00:36

**背景**: OpenAI Codex 是一款编程智能体，能够自主执行命令并与用户系统上的文件进行交互。为了降低风险，它采用了多层沙盒系统，将文件访问和网络活动限制在受控环境中。在 Linux 及类 Unix 系统中，$HOME 环境变量指向当前用户的主目录，该目录用于存储个人数据和配置文件。当 AI 智能体在“完全访问”模式下脱离这些沙盒限制运行时，单次命令失误就可能导致灾难性的数据丢失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/home-variable-user-tilde">Where and How Are the User $HOME Environment Variable and Tilde Set? | Baeldung on Linux</a></li>
<li><a href="https://www.devopsdigest.com/the-hidden-risk-layer-in-ai-agents-why-sandboxed-execution-is-becoming-essential">The Hidden Risk Layer in AI Agents : Why Sandboxed Execution is...</a></li>
<li><a href="https://github.com/openai/codex/blob/main/docs/sandbox.md">codex /docs/ sandbox .md at main · openai / codex · GitHub</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI Safety`, `#Autonomous Agents`, `#Codex`

---

<a id="item-8"></a>
## [英伟达开源 Nemotron 3 Embed 系列模型，8B 版斩获 RTEB 榜首](https://aihot.virxact.com/items/cmrpl474902zmbisrr0kiw4fp) ⭐️ 8.0/10

英伟达以开放权重形式发布了 Nemotron 3 Embed 系列文本嵌入模型，可通过 Hugging Face 和 NVIDIA NIM 免费获取，并允许商业使用。其中 80 亿参数版本在 RTEB 基准测试中以 78.5% 的得分位列榜首，在 MMTEB 检索基准上得分 75.5%。 此次发布为构建 RAG 管道和 AI 智能体的开发者提供了一款最先进且可商用的嵌入模型，在关键检索基准上超越了现有替代方案。这标志着英伟达在硬件之外，继续发力开源权重 AI 生态系统的竞争，直接挑战其他领先的嵌入模型提供商。 Nemotron 3 Embed 系列专门针对检索和语义相似度任务进行了优化，配备 32K 上下文窗口，能够处理更长的文档。该系列提供包括 10 亿参数版本在内的多种规模，让开发者可以灵活平衡性能与计算成本。

rss · AI Hot · Jul 17, 23:22

**背景**: 文本嵌入模型将文本转换为数值向量，通过测量概念之间的数学距离来实现语义搜索和检索。RTEB（检索聚焦文本嵌入基准）是新推出的标准，用于评估嵌入模型检索相关信息的准确度；而 MTEB/MMTEB 则是涵盖跨语言和模态多种 NLP 任务的综合性基准套件。RAG（检索增强生成）是一种技术，AI 模型利用嵌入向量查询外部知识库，从而提供更准确、更及时的响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16">nvidia / Nemotron - 3 - Embed -1B-BF16 · Hugging Face</a></li>
<li><a href="https://github.com/embedding-benchmark/rteb">GitHub - embedding-benchmark/rteb: Retrieval Embedding Benchmark · GitHub</a></li>
<li><a href="https://github.com/embeddings-benchmark/mteb/">GitHub - embeddings-benchmark/mteb: MTEB: State-of-the-art evaluation of embeddings across languages and modalities · GitHub</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Embedding Models`, `#Open Source AI`, `#RAG`, `#NLP`

---

<a id="item-9"></a>
## [François Chollet 的 After Labs 走出隐身模式，获 NFAI 300 万欧元资助](https://aihot.virxact.com/items/cmrpkp6d002rubisrwnbysn9r) ⭐️ 8.0/10

由 François Chollet（Keras 和 ARC-AGI 的创建者）创立的 After Labs 在被 NFAI（法国国家人工智能基金）评选为十大 AI 实验室之一后，正式走出隐身模式。该实验室获得了 300 万欧元的追加资助，将致力于开发具备内置自适应机制、能实时高效学习的新一代 AI 模型，明确摒弃当前主导 AI 研究的暴力强化学习范式。 这代表了一种可能改变范式、迈向 AGI 的新路径，直接挑战了业界通过大规模算力扩展和暴力训练来取得进展的主流策略。作为 AI 领域备受尊敬的人物，Chollet 对自适应学习架构的押注可能将大量研究注意力重新引向更具样本效率、能够像人类一样动态适应的系统。 该实验室强调开放科学研究，专注于能够实时适应的模型，而非仅仅依赖海量数据集进行预训练。这一理念与 Chollet 长期以来的批评一脉相承——他认为当前的 AI 基准测试往往衡量的是记忆和模式匹配能力，而非真正的流体智力，这一点在他专门为测试新颖推理能力而设计的 ARC-AGI 基准测试中得到了体现。

rss · AI Hot · Jul 17, 23:14

**背景**: François Chollet 是 Google 的杰出 AI 研究员，他创建了被广泛使用的深度学习框架 Keras，并设计了 ARC-AGI（抽象与推理语料库）基准测试来评估真正的机器智能。当前 AI 领域的主导范式依赖于缩放定律，即使用海量计算资源和强化学习技术在庞大的数据集上训练模型，这通常需要数百万次迭代才能达到熟练水平。相比之下，自适应学习旨在创建能够实时高效获取新技能和新知识的系统，类似于人类能够从极少的样本中学习并适应全新情境的能力。NFAI（国家人工智能基金）是法国政府的一项倡议，旨在识别和支持有前景的 AI 研究机构，以加强法国在全球 AI 领域的地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/intuitionmachine/the-brute-force-method-of-deep-learning-innovation-58b497323ae5">Is Deep Learning Innovation Just Due to Brute Force? | by Carlos E. Perez | Intuition Machine | Medium</a></li>
<li><a href="https://dev.to/vicodev/from-brute-force-to-reinforcement-optimizing-intelligent-agents-with-modern-ai-4g0k">From brute force to reinforcement: optimizing intelligent agents with modern AI - DEV Community</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#François Chollet`, `#Adaptive Learning`, `#AI Labs`, `#AGI`

---

<a id="item-10"></a>
## [SpaceX 与五角大楼洽谈供应 AI 算力](https://aihot.virxact.com/items/cmrpl474902znbisrfz9kfqde) ⭐️ 8.0/10

据报道，SpaceX 正与美国五角大楼进行积极洽谈，计划提供价值数十亿美元的数据中心算力，用于运行大型 AI 模型。SpaceX 员工内部讨论表明，公司计划通过更低的价格与 CoreWeave 及其他 Neocloud 公司竞争。 SpaceX 可能进入 AI 算力市场标志着一次重大行业转变，一家以航空航天闻名的公司可能颠覆国防 AI 基础设施不断增长的需求。凭借在大规模工程和政府合同方面的独特优势，这一举措可能通过引入强大的新竞争者，对前沿 AI 算力供应产生深远影响。 目前洽谈仍在进行中，最终可能无法达成协议。SpaceX 的战略核心是通过低于竞争对手的价格，吸引需要训练和运行大规模机器学习模型的 AI 客户。

rss · AI Hot · Jul 17, 23:12

**背景**: CoreWeave 是一家美国大型 AI 云计算公司，专注于为 AI 和机器学习工作负载提供高性能 GPU 基础设施，其营收经历了爆发式增长。Neocloud（新云）是新兴的云计算提供商类别，主要专注于提供专为 AI 开发定制的 GPU 优先基础设施。全球建设专用 AI 数据中心的步伐大幅加快，据估计大型科技公司将在这些设施上投入数千亿美元，以满足现代 AI 工作负载的并行处理需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neocloud">Neocloud</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#SpaceX`, `#Cloud Computing`, `#National Defense`, `#Compute`

---

<a id="item-11"></a>
## [印奇在 WAIC 2026：当智能体走进物理世界](https://36kr.com/p/3900439867147909?f=rss) ⭐️ 8.0/10

7 月 17 日，在 WAIC 2026 开幕式上，阶跃星辰与千里科技董事长印奇发表主题演讲，描绘了 AI 智能体从数字屏幕走向真实物理世界的结构性变革。他判断 2026 年模型能力正在跨越关键临界点，从仅能执行数秒任务进阶到独立工作数十小时，标志着行业正站在 AGI 高峰的山脚下。 这一愿景标志着行业从基于软件的聊天机器人向具身智能体的重大转变，这些智能体将作为真实世界中的生产力单元去感知、决策和执行任务。其所提出的架构未来——包括智能体操作系统（Agentic OS）、跨终端载体和 A2A 网络——为 AI 如何融入物理设备并重塑更广泛的技术生态系统提供了高价值的路线图。 印奇强调了三大结构性变革：作为运行时层连接模型与工具硬件的 Agentic OS、允许单一智能体在电脑、手机、汽车和机器人间自由迁移的跨终端载体，以及使智能体能够自主协作和交易的 A2A 网络。他还强调，随着智能体进入现实世界，迫切需要新的治理机制来解决责任归属、身份可信和行为可追溯等问题。

rss · 36kr · Jul 18, 00:53

**背景**: WAIC（世界人工智能大会）是在上海举办的年度全球顶级人工智能盛会，汇聚了顶尖专家和科技公司探讨前沿进展。Agentic OS（智能体操作系统）是一个新兴概念，它在 Linux 等传统操作系统之上构建 AI 原生的运行时和中间件层，用于管理自主智能体和硬件资源。A2A（Agent-to-Agent）网络是指允许自主 AI 智能体在没有人类实时干预的情况下进行通信、相互发现并执行协作任务的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/世界人工智能大会">世界人工智能大会 - 维基百科，自由的百科全书</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2671167">Agentic OS 技术详解：面向自主AI Agent的操作系统-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://alignify.co/zh/blog/agent-to-agent">最佳 Agent 互联 网 络 （2026）：Moltbook、Second Me、Elys等 | Alignify</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#AI Agents`, `#AGI`, `#WAIC 2026`, `#Tech Vision`

---

<a id="item-12"></a>
## [消息称 Anthropic 拟租赁 Meta 的 AI 算力，交易总额最高 100 亿美元](https://www.ithome.com/0/978/356.htm) ⭐️ 8.0/10

据报道，Anthropic 与 Meta 正在洽谈一项为期 2 年、总额最高 100 亿美元的算力租赁协议，Anthropic 每月需支付约 4.17 亿美元。Anthropic 于 2025 年 6 月提出该方案，初步条款允许双方提前终止协议。 这笔潜在交易凸显了 AI 算力的极度稀缺性，前沿 AI 实验室正越来越多地从传统云服务商之外的非传统渠道获取大规模算力。对 Meta 而言，出租闲置算力可以开辟新的收入来源，并有助于向投资者解释其计划中高达 1450 亿美元的基础设施支出；对 Anthropic 而言，这能缓解 Claude Code 等产品带来的迫切算力需求。 据知情人士透露，谈判仍处于早期阶段，未必能最终达成协议。拟议中的协议为期 2 年并按月付款，双方在补充条款下均保留提前退出的权利。

rss · IT HOME · Jul 18, 01:20

**背景**: AI 算力已成为前沿 AI 开发的主要瓶颈，2024 至 2025 年间的 GPU 短缺使得自行购买硬件成本极高且周期漫长。这催生了一个'新云'行业，企业提供 GPU 即服务，甚至 AI 实验室之间也开始相互租赁算力。Anthropic 的企业级 AI 编程工具 Claude Code 是一款运行在开发者终端中的智能编程助手，其发布大幅推升了算力需求。与此同时，Meta 一直在大力投资 AI 数据中心，今年计划在 AI 和数据中心建设上投入高达 1450 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smartcr.org/ai-technologies/the-neocloud-cartel-how-the-ai-industry-started-renting-compute-from-itself/">The Neocloud Cartel: How the AI Industry Started Renting Compute ...</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Compute Infrastructure`, `#AI Industry`, `#Meta`, `#Cloud Computing`

---

<a id="item-13"></a>
## [特斯拉 Cybercab 在北美投产，主打无方向盘全自动驾驶](https://t.me/zaihuapd/42621) ⭐️ 8.0/10

特斯拉已正式在北美启动 Cybercab 的量产，这是一款专为全自动驾驶设计的车辆，取消了方向盘、踏板和后视镜。该车型完全由车载 AI 接管所有行驶控制，标志着特斯拉 Robotaxi 业务迈出重要一步。 一款从零开始设计、完全取消手动控制装置的车辆实现量产，是具身智能和自动驾驶领域的重大里程碑。这标志着行业从在传统汽车上加装自动驾驶功能，转向打造专用无人驾驶出租车，可能从根本上重塑城市交通和网约车行业。 Cybercab 是一款双座纯电动车，概念版于 2024 年 10 月首次发布，据报道试生产已于 2026 年 2 月开始。其整车架构和用户交互完全为无人驾驶场景定制，与在传统车辆上改装自动驾驶系统有本质区别。

telegram · @zaihuapd · Jul 17, 03:06

**背景**: Robotaxi 即无人驾驶出租车，是指达到 SAE L4 或 L5 自动驾驶等级、无需人类驾驶员即可运营的网约车服务车辆。特斯拉多年来一直在开发其 Full Self-Driving（FSD）技术，Cybercab 是该公司首款专为 Robotaxi 网络打造的车辆。整个无人驾驶出租车行业正在快速扩张，但仍面临公众信任、监管审批和盈利能力等方面的挑战——2025 年的一项调查显示，仅有 13% 的美国受访者表示信任自动驾驶车辆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Robotaxi">Robotaxi</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi | Tesla</a></li>

</ul>
</details>

**标签**: `#Autonomous Vehicles`, `#Embodied AI`, `#Tesla`, `#Robotaxi`, `#Frontier Tech`

---

<a id="item-14"></a>
## [🤖 OpenAI CFO 提出 AI 时代新提效指标：用每美元有用智能衡量 ROI](https://openai.com/index/a-scorecard-for-the-ai-age) ⭐️ 8.0/10

OpenAI CFO Sarah Friar proposes a new metric of 'useful intelligence per dollar' to measure AI ROI, emphasizing that the value of work completed and output reliability matter more than simply minimizing token costs.

telegram · @zaihuapd · Jul 17, 15:00

**标签**: `#OpenAI`, `#AI ROI`, `#Enterprise AI`, `#AI Economics`, `#Metrics`

---

<a id="item-15"></a>
## [字节跳动豆包手机从 GUI 自动化转向 MCP 集成策略](https://www.latepost.com/news/dj_detail?id=3648) ⭐️ 8.0/10

字节跳动新一代豆包手机将放弃对头部应用的 GUI 屏幕读取和模拟点击技术，转而要求阿里、腾讯等超级应用自行提供 MCP（模型上下文协议）服务后才能接入。同时，该设备的备货量从此前的 3 万台大幅提升至数十万台。 这一战略转变标志着 AI 智能体与移动软件交互方式的重大行业转型，从未经授权的屏幕操控转向基于权限的集成框架。这一转变与苹果和 Google 的类似策略相呼应，超级应用与设备制造商正在争夺 AI 时代的入口主权和用户数据控制权。 此前发布的技术预览版曾因微信、淘宝等平台封禁其 GUI 自动化能力而被迫下线。豆包手机助手软件已于 7 月 15 日正式获得生成式人工智能服务备案，使其能够作为合规的 AI 产品在中国运营。

telegram · @zaihuapd · Jul 18, 00:29

**背景**: AI 智能体的 GUI 自动化是指利用视觉语言模型读取屏幕并模拟鼠标或键盘操作，但这种做法遭到了将其视为未经授权访问的平台的抵制。模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 系统通过授权 API 与外部工具和数据源的集成方式。在 MCP 框架下，应用开发者明确界定 AI 智能体可以访问哪些数据和控件，从而在 AI 助手与应用之间建立合作关系而非对抗关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#ByteDance`, `#MCP`, `#Smartphone AI`, `#Tech Ecosystem`

---