---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> From 107 items, 10 important content pieces were selected

---

1. [Opus 5.5 智能体发现两种室温磁性半导体候选材料](#item-1) ⭐️ 9.0/10
2. [特朗普宣布成立超级智能部队 SIF](#item-2) ⭐️ 9.0/10
3. [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 性能优化与快速重启守护进程](#item-3) ⭐️ 8.0/10
4. [Reflection.ai 发布 501B 参数开源权重 MoE 模型 Beam](#item-4) ⭐️ 8.0/10
5. [OpenAI 洽谈 300 亿美元融资，估值达 1.4 万亿美元](#item-5) ⭐️ 8.0/10
6. [Q Labs 发布 Dust：无需反向传播的 Transformer 预训练方法](#item-6) ⭐️ 8.0/10
7. [月之暗面完成上市前最后一轮融资：估值约 500 亿美元，计划明年一季度赴港 IPO](#item-7) ⭐️ 8.0/10
8. [美国 NIST/CAISI 评估称 DeepSeek V4 Pro 落后美国前沿约 8 个月](#item-8) ⭐️ 8.0/10
9. [OpenAI 将在欧盟为 AI 生成文本添加隐形水印](#item-9) ⭐️ 8.0/10
10. [OpenAI 将 GPT-6 Astra 等模型默认速度提升约 50%](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Opus 5.5 智能体发现两种室温磁性半导体候选材料](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) ⭐️ 9.0/10

Anthropic 的 Claude Opus 5.5 智能体通过运行量子力学密度泛函理论（DFT）模拟自主筛选晶体候选材料，并识别出两种被预测在室温下具有磁性的半导体材料。这项工作由 Vals AI 发布，是 AI 智能体驱动科学发现的一次示范。 室温磁性半导体一直是材料科学的目标，因为它们能实现同时控制电荷和自旋的自旋电子学器件，但现有材料通常只在低温下工作。这展示了前沿 AI 智能体加速高成本材料筛选计算的能力，是“AI for Science”大趋势中的一个高信号案例。 智能体在两个近似层级上运行 DFT 模拟：较快的 PBE+U 和较慢但更精确的 HSE06，报道的带隙和自旋窗口数据来自 HSE06。需要注意，这些仅是计算预测，尚未经过实验合成或验证。

hackernews · outlier99 · Oct 5, 21:00 · [社区讨论](https://news.ycombinator.com/item?id=49970667)

**背景**: 密度泛函理论（DFT）是计算带隙和磁序等材料性质的标准量子力学方法，但它以缓慢和高计算成本著称，大规模筛选代价高昂。磁性半导体在常规半导体的电荷控制之外还能控制自旋，可支撑自旋电子学，但已知材料通常只在低温下表现出微弱磁性。利用 AI 自动化 DFT 工作流程在大量候选晶体中进行筛选，可以大幅扩展研究人员可探索的搜索空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/science.adl0823">Is it possible to create magnetic semiconductors that ... - AAAS</a></li>
<li><a href="https://www.eetasia.com/ai-powering-new-materials-discovery-for-the-2nm-era/">AI Powering New Materials Discovery for the 2nm Era - EE Times Asia</a></li>
<li><a href="https://arxiv.org/pdf/2508.14111">From AI for Science to Agentic Science : A Survey on Autonomous ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应既有赞赏也有怀疑：有人援引 LK-99 闹剧呼吁高度谨慎，也有人认为此类 AI 驱动的发现将越来越频繁，并改变新颖性的标准。一些评论者质疑运行经典模拟是否算得上“发现”，还有人批评标题对 LLM 产出使用“发现/找到”等字眼，认为用“报告”更准确。一位懂物理的评论者还指出，原文只提铁磁和反铁磁两种磁体的介绍方式有问题。

**标签**: `#AI agents`, `#materials science`, `#scientific discovery`, `#Claude Opus`, `#DFT simulation`

---

<a id="item-2"></a>
## [特朗普宣布成立超级智能部队 SIF](https://x.com/WhiteHouse/status/2106731532694028310) ⭐️ 9.0/10

Trump announces the creation of a 'Superintelligence Force' (SIF) to coordinate federal efforts and ensure US leadership in superintelligence.

telegram · @zaihuapd · Oct 5, 03:56

**标签**: `#AI policy`, `#superintelligence`, `#US government`, `#AGI`, `#governance`

---

<a id="item-3"></a>
## [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 性能优化与快速重启守护进程](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM v0.31.0 包含来自 307 位贡献者的 717 次提交，重点是 DeepSeek-V4.1-Flash 性能优化：FlashMLA mega attention 搭配 NVFP4 压缩 KV 缓存成为 SM100 默认配置，并引入融合 MoE 内核和 MXFP8/NVFP4 量化。本次发布还通过新的 `vllm preload` 命令行工具引入了快速重启的权重缓存守护进程，以及基于 CRIU 的实验性引擎快照功能。 vLLM 是使用最广泛的开源大模型推理引擎之一，这些优化将直接转化为 DeepSeek 等前沿模型在 Blackwell GPU 上更低的延迟和更高的吞吐。快速重启守护进程解决了大模型启动耗时长这一重要运维痛点，可提升生产推理集群的可用性。 值得注意的技术细节包括解码器边界处对 TP all-reduce、mHC 输入准备和 MoE finalize 的融合；SM100/SM103 上的小批量 WO-A 融合（含逆 RoPE 和 MXFP8 量化）；以及通过 `--all2all-backend moonep` 启用的 MoonEP 均衡 EP all2all 后端。破坏性变更包括移除 `tokenizer_mode="slow"`、逐请求多模态参数需 `--trust-request-mm-kwargs` 才能使用，以及用 `fp8_per_tensor` 替代 `quantization="fp8"`。

github · vllm-project/vllm · Oct 5, 06:44

**背景**: vLLM 是一个以 PagedAttention 和高吞吐大模型服务著称的开源推理引擎。DeepSeek 系列模型采用多头潜在注意力（MLA）来压缩 KV 缓存，FlashMLA 则是针对该注意力变体在 NVIDIA 硬件上优化的内核。MXFP8 和 NVFP4 是低精度量化格式（NVFP4 通常比 MXFP4 更能保持精度），可在 Blackwell（SM100）GPU 上降低显存占用并提升速度；融合 MoE 内核将专家选择和 GEMM 等多个操作合并，以减少内核启动和通信开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-04-22-fp8-kvcache">The State of FP8 KV-Cache and Attention Quantization in vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#deepseek`, `#gpu-optimization`, `#open-source`

---

<a id="item-4"></a>
## [Reflection.ai 发布 501B 参数开源权重 MoE 模型 Beam](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

2026 年 10 月 5 日，Reflection AI 发布了首个开源权重模型 Beam：一个总参数量 5010 亿（激活参数 230 亿）的稀疏混合专家（MoE）模型，专为编码、推理和智能体（agentic）任务打造。该模型在 23.8 万亿精选 token 上进行预训练并投入大量强化学习，公司宣称其能以更低计算成本匹敌领先的中国开源模型。 Beam 为目前由中国实验室（如 DeepSeek）主导的开源权重领域增添了一个重量级的西方竞争者，为开发者提供了一个可自由下载的前沿级编码与智能体模型。这也表明美国初创公司正转向开源权重发布，以在成本和可及性上竞争。 Beam 的 230 亿激活参数明显高于同类稀疏模型（例如 DeepSeek V4.1 Flash 在预填充时激活 80 亿、解码时 160 亿），但其 23.8 万亿预训练 token 少于 DeepSeek 的约 45 万亿。Reflection 在一个几天前刚发布的 X 经纬度网格谜题上演示了泛化能力，宣称覆盖率达 95.5%，介于 Opus 5（92.5%）与 Fable 之间。

hackernews · Philpax · Oct 5, 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 混合专家（MoE）架构允许模型拥有庞大的总参数量，但每个 token 只激活其中一小部分“专家”，相比同等规模的稠密模型可大幅降低推理成本。开源权重模型免费公开训练所得的数值参数，但不同于同时公开训练数据和代码的开源模型。位于布鲁克林的初创公司 Reflection AI 此前发布过 Reflection 70B，该模型因被发现底层调用 Claude 并用正则表达式从输出中删除“Claude”字样而陷入争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reflection.ai/blog/introducing-beam">Introducing Beam: Reflection’s 501B open-weight model</a></li>
<li><a href="https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/">Reflection debuts Beam, an open-weight AI model to rival ...</a></li>
<li><a href="https://www.unite.ai/reflection-ai-unveils-beam-a-501b-parameter-open-weight-model/">Reflection AI Unveils Beam, a 501B-Parameter Open-Weight Model</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人欢迎又一款开源权重模型的发布，但也有人因 Reflection 过往的透明度问题深感怀疑——有用户提及 Reflection 70B 事件以及承诺却从未兑现的事后复盘。技术对比指出 Beam 的激活参数更多、预训练 token 却比 DeepSeek V4.1 Flash 更少，还有评论者认为它仍然不如更小的免费中国模型。

**标签**: `#open-weight models`, `#mixture-of-experts`, `#LLM release`, `#AI`, `#agentic AI`

---

<a id="item-5"></a>
## [OpenAI 洽谈 300 亿美元融资，估值达 1.4 万亿美元](https://aihot.news/items/ykt1e2tjgms4ubafg3kuq3klg) ⭐️ 8.0/10

据彭博社报道，OpenAI 正在磋商一轮 300 亿美元融资，投前估值固定为约 1.4 万亿美元，阿布扎比的 MGX 将牵头组建阿联酋基金财团，贝莱德也计划随团参与。老股东 Thrive Capital、a16z 及加州大学捐赠基金均在商讨追加投资，而 OpenAI 以专注 AI 安全工作为由将 IPO 推迟至至少明年。 若完成，这将成为史上最大规模的私募融资之一，巩固 OpenAI 作为全球最高估值私有公司的地位，并进一步加深中东主权资本对前沿 AI 的投入。该交易也表明 OpenAI 短期内更倾向巨额私募融资而非上市，将重塑 AI 行业资本市场的预期。 几家阿联酋基金合计出资最高可达 100 亿美元，且 OpenAI 不同寻常地直接给出 1.4 万亿美元的固定投前估值，而非由投资方竞价确定，目前尚未敲定领投方。本轮融资将使 OpenAI 的估值较 3 月上一轮（融资 1220 亿美元、估值 8520 亿美元）接近翻倍，而 MGX 今年早些时候刚募得近 500 亿美元用于布局 AI 基础设施。

rss · AI Hot · Oct 6, 02:29

**背景**: 前沿 AI 的研发和运维每年需要数百亿美元的计算基础设施投入，促使 OpenAI 和 Anthropic 等公司向资金雄厚的中东投资者寻求支持。MGX 是一家由阿联酋阿布扎比副酋长塔赫农·本·扎耶德·阿勒纳哈扬担任董事会主席的基金，此前已投资过 OpenAI 和 Anthropic。Thrive Capital 由 Joshua Kushner 创立，与 Andreessen Horowitz（a16z）同为 OpenAI 老股东。投前估值指公司在新增融资前的价值，决定新投资人能获得的股权比例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7615966482778701834">300 亿美元，3800 亿估值：Anthropic...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thrive_Capital">Thrive Capital</a></li>
<li><a href="https://followin.io/zh-Hans/feed/16784528">揭秘20亿美元入股币安的 MGX ： 阿 联酋国父之子掌舵</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI融资`, `#阿联酋基金`, `#贝莱德`, `#AI产业`

---

<a id="item-6"></a>
## [Q Labs 发布 Dust：无需反向传播的 Transformer 预训练方法](https://aihot.news/items/hcjnclio2ah5xfepty2ey1ib5) ⭐️ 8.0/10

Q Labs Research 发布了 Dust，据称是首个在预训练 GPT 式 Transformer 语言模型上能与反向传播相竞争的零阶优化方法。Dust 在每个 token 上独立扰动激活（即节点扰动），将每个 token 视为虚拟种群的一员，使得一次前向传播即可并行评估所有扰动，从而完全无需反向传播。 几十年来，反向传播一直是深度学习事实上的标准训练算法，但它存在显存开销高、权重传输问题以及梯度消失/爆炸等局限。一种无需反向传播且具竞争力的预训练方法可能挑战大模型训练的基础假设，并为更省显存或更符合生物学机制的学习方式开辟道路。 Dust 采用对激活（而非权重）进行节点扰动的策略，利用序列维度让每个 token 充当一个虚拟种群成员并行评估。该方法在大种群规模下能很好地逼近反向传播，但代价是需要显著多于标准训练的计算量。

rss · AI Hot · Oct 6, 02:07

**背景**: 零阶优化是一种无导数方法，通过函数值的有限差分来估计梯度，近来因可作为避免反向传播、显存高效的大模型微调方式而受到关注。此前零阶方法主要用于微调而非预训练，因为在没有导数的情况下估计梯度通常需要远多于梯度方法的函数求值次数。Dust 的关键创新在于将序列中的每个 token 变成一个独立的扰动样本，使得对一批数据的一次前向传播就能提供大规模的虚拟种群估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qlabs.sh/research/dust">Dust: Pretraining Transformers Without Backpropagation</a></li>
<li><a href="https://arxiv.org/abs/2602.17155">[2602.17155] Powering Up Zeroth-Order Training via Subspace ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10115-025-02370-0">Navigating beyond backpropagation: on alternative training ...</a></li>

</ul>
</details>

**标签**: `#AI research`, `#training methods`, `#zero-order optimization`, `#Transformers`, `#pretraining`

---

<a id="item-7"></a>
## [月之暗面完成上市前最后一轮融资：估值约 500 亿美元，计划明年一季度赴港 IPO](https://www.ithome.com/1/009/971.htm) ⭐️ 8.0/10

据彭博社报道，月之暗面已完成上市前最后一轮私募融资，估值约 500 亿美元，较今年夏天上一轮的 315 亿美元明显上升，并计划最早于明年第一季度在香港 IPO，募资上限为 50 亿美元。公司已以保密方式向港交所递交申请，委任美国银行担任整体协调人，中金公司、德意志银行和高盛为保荐银行。 月之暗面是中国头部 AI 企业，今年 7 月发布的 Kimi K3 开源大模型在多项评测中可与 OpenAI 和 Anthropic 的头部模型抗衡，使其 IPO 成为港股 AI 热潮中最受期待的交易之一。此次上市可能为中国前沿 AI 实验室的公开市场估值树立标杆，并影响整个行业的融资环境。 公司年度经常性收入（ARR）据报道已达 10 亿美元（6 月时为 3 亿美元），预计 12 月将升至 20 亿美元，支撑了估值的快速上升。主要风险在于监管机构已对 DeepSeek 和月之暗面启动数据安全调查，且各项工作仍在磋商阶段，IPO 时间表存在变数。

rss · IT HOME · Oct 6, 03:38

**背景**: 月之暗面是一家总部位于北京的 AI 实验室，由曾任清华大学教授、先后任职于 Meta 和谷歌的杨植麟于 2023 年初创立，投资方包括阿里巴巴、腾讯和五源资本。其今年 7 月开源的 Kimi K3 模型参数规模约 2.8 万亿，曾登顶 Hugging Face 趋势榜，证明开源模型也能与前沿闭源模型竞争。ARR（年度经常性收入）是衡量订阅制业务可预测年度经常性收入的关键指标，投资人常用其快速增长来论证 AI 公司的高估值。近期港股 AI 驱动的新股融资活动接连刷新纪录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/3914177904661639">刚刚， Kimi K 3 开 源 ，2.8万亿参数砸向全球，硅谷巨头看傻了-36氪</a></li>
<li><a href="https://stripe.com/zh-us/resources/more/what-is-annual-recurring-revenue-a-guide-for-saas-businesses">什么是年度经常性收入 (ARR)？| Stripe</a></li>
<li><a href="https://www.mg21.com/moonshot.html">中国通用人工智能 公 司 ： 月 之 暗 面 Moonshot AI</a></li>

</ul>
</details>

**标签**: `#Moonshot AI`, `#Kimi`, `#IPO`, `#AI industry`, `#funding`

---

<a id="item-8"></a>
## [美国 NIST/CAISI 评估称 DeepSeek V4 Pro 落后美国前沿约 8 个月](https://t.me/zaihuapd/44220) ⭐️ 8.0/10

美国国家标准与技术研究院（NIST）下属的人工智能标准与创新中心（CAISI）发布评估报告，称中国开源模型 DeepSeek V4 Pro 的综合能力比美国最先进模型落后约 8 个月。在 CAISI 选取的基准上，其 Elo 得分为 800，低于 GPT-5.5（999），与 Opus 4.6（800）持平，接近 GPT-5.4 mini（749）。 这是美国官方对中美 AI 能力差距的评估，将直接影响 AI 政策与出口管制方面的讨论。鉴于 DeepSeek 此前缩小差距的速度超出预期，权威机构量化出的 8 个月差距对政策制定者、研究人员和产业界都是重要参考。 报告特别指出 DeepSeek V4 Pro 在 ARC-AGI-2（侧重组合规则与新颖问题求解的抽象推理基准）和 PortBench 上表现较弱。排名采用 Elo 系统，将模型间两两比较转化为单一可比分数，但基准的选择本身可能影响结论。

telegram · @zaihuapd · Oct 5, 07:32

**背景**: CAISI 是 NIST 下属的人工智能标准与创新中心，于 2025 年 6 月由 AI 安全研究所更名而来，是美国政府内部产业界进行 AI 测试与协作研究的主要对接机构。Elo 评分最初用于国际象棋排名，自 2023 年 Chatbot Arena 开始众包人类两两对比评判后，已成为大模型统一排名的常用方法。ARC-AGI-2 由 ARC Prize 基金会（Chollet 等人）维护，以组合规则测试抽象推理能力，被广泛视为高难度前沿基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nist.gov/caisi">Center for AI Standards and Innovation ( CAISI ) | NIST</a></li>
<li><a href="https://casrai.org/guides/what-is-caisi">What Is CAISI ? NIST 's AI Standards Center — CASRAI</a></li>
<li><a href="https://benchmarklist.com/benchmarks/arc_agi_2/">ARC - AGI - 2 Benchmark Scores & AI Model... | BenchmarkList</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI evaluation`, `#NIST/CAISI`, `#frontier models`, `#benchmarks`

---

<a id="item-9"></a>
## [OpenAI 将在欧盟为 AI 生成文本添加隐形水印](https://openai.com/index/eu-text-provenance/) ⭐️ 8.0/10

OpenAI 宣布未来几周将在欧盟地区符合条件的 ChatGPT 和 Codex 文本输出中加入机器可识别的隐形水印，以符合《欧盟人工智能法案》的透明度要求。API 用户可为部分模型选择开启水印（默认关闭），OpenAI 还向研究人员和专业机构开放文本水印检测器的申请使用。 这是大型 AI 实验室首次大规模部署隐形文本水印之一，将直接影响《欧盟人工智能法案》第 50 条透明度义务在实践中的落实方式。它为内容溯源和 AI 治理树立了先例，影响开发者、发布者以及检测 AI 生成内容的研究人员。 水印对人类不可见但可被机器识别，将在欧盟自动应用于符合条件的输出，而 API 水印为可选开启且默认关闭。检测工具仅面向经审核的研究人员和专业机构开放；值得注意的是，已有第三方工具宣称可清除基于不可见字符的水印，这是一场持续的攻防博弈。

telegram · @zaihuapd · Oct 5, 15:25

**背景**: 《欧盟人工智能法案》第 50 条对 AI 系统施加透明度义务，要求 AI 生成内容可被识别，该义务自 2026 年 8 月 2 日起适用，欧盟委员会已发布合规指南。水印技术通过在生成文本中嵌入统计或字符级模式，使检测器能够验证内容来源。Anthropic 也宣布为 Claude 输出添加隐形水印以符合同一法律，而 C2PA 的 Content Credentials 等行业标准则为媒体内容提供开放溯源规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations">Guidelines on transparency obligations for providers and ...</a></li>
<li><a href="https://artificialintelligenceact.eu/article/50/">Article 50: Transparency Obligations for Providers and ...</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI watermarking`, `#EU AI Act`, `#AI governance`, `#content provenance`

---

<a id="item-10"></a>
## [OpenAI 将 GPT-6 Astra 等模型默认速度提升约 50%](https://x.com/thsottiaux/status/2107158998495748264) ⭐️ 8.0/10

OpenAI 的 Tibo 宣布，GPT-6 Astra 和 GPT-6.1 Sol 的订阅默认推理速度提升约 50%，从 30 TPS 提高到 50 TPS。该更新覆盖所有产品及使用 Sign in with ChatGPT 的合作方应用，用户无需任何操作，预计两小时内可感知。 更快的默认推理速度让前沿模型的响应体验显著提升，直接改善数百万 ChatGPT 用户及接入合作方应用的使用体验。配合更高效、减少 token 消耗的分词器，还能降低完成任务的等效计算与成本，增强 OpenAI 在前沿 AI 部署上的竞争力。 此次提速是订阅用户的默认设置，自动生效而非可选功能，同时覆盖 OpenAI 自家产品和通过 Sign in with ChatGPT 接入的第三方应用。配套的分词器优化意味着模型完成相同任务所需 token 更少，在感知速度提升的同时也降低了按 token 计费的成本。

telegram · @zaihuapd · Oct 5, 17:38

**背景**: TPS（每秒生成 token 数）衡量语言模型在首个 token 之后流式输出文本的速度，是聊天和编程应用中响应体验的关键指标。GPT-6 是 OpenAI 最新的前沿模型系列，其中 GPT-6 Astra 于 2026 年 9 月 4 日公开发布，在推理、编程、计算机使用和科学领域具备顶尖能力。Sign in with ChatGPT 是 OpenAI 的身份认证机制，允许用户将 ChatGPT 身份带入支持的外部应用。分词器将文本转换为模型处理和计费所依据的 token，因此分词效率直接影响速度和成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6">GPT-6 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://www.gmicloud.ai/en/blog/ttft-llm-speed-metrics">TTFT vs Tokens Per Second : LLM Inference Speed ... | GMI Cloud</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#inference-speed`, `#AI-models`, `#infrastructure`

---