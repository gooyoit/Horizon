---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> From 103 items, 7 important content pieces were selected

---

1. [Sky Computing Lab 在 ICML 2026 展示五项 AI 加速研究](#item-1) ⭐️ 9.0/10
2. [阿里云李飞飞阐述面向智能体时代的全栈就绪战略](#item-2) ⭐️ 8.0/10
3. [日本公布 AI 机器人战略修订版，目标 2040 年部署 1000 万台机器人](#item-3) ⭐️ 8.0/10
4. [Anthropic 新模型工具调用倒退：Opus 4.8 与 Sonnet 5 在非主流 schema 上更不可靠](#item-4) ⭐️ 8.0/10
5. [NVIDIA 推出 GPU 收益分成计划，助力 AI 初创公司](#item-5) ⭐️ 8.0/10
6. [SK 海力士启动 280 亿美元美股上市，有望成史上第二大 IPO](#item-6) ⭐️ 8.0/10
7. [三星电子 Q2 营业利润预计同比暴涨 18 倍，AI 存储芯片需求持续引爆业绩](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Sky Computing Lab 在 ICML 2026 展示五项 AI 加速研究](https://aihot.virxact.com/items/cmr8k54uw02sqsl0d4rmfo2gi) ⭐️ 9.0/10

Sky Computing Lab 在 ICML 2026 首尔大会上发布了五项重要研究项目，包括多模态基准 MADQA、实现最高 10 倍加速的扩散语言模型 d3LLM，以及在 GPU 上实现 4 位注意力量化的 Attn-QAT。此外还推出了用于并行解码的 Jacobi Forcing 和在线调整草稿模型的 OnlineSpec，带来了显著的推理加速效果。 这些项目从多模态智能体评估到低比特量化，在多个关键领域全面推动了 AI 推理速度和效率的边界。扩散语言模型、并行解码和 4 位注意力方面的突破，直接解决了当前限制大规模 AI 部署的计算瓶颈问题。 d3LLM 通过伪轨迹蒸馏实现加速，而 Jacobi Forcing 将预训练自回归模型转换为因果并行解码器，在编码和数学任务上实现 4 倍真实加速。Attn-QAT 是首个针对注意力的 4 位量化感知训练系统性研究，在 RTX 5090 上实现 1.5 倍加速且无需推理时异常值缓解。

rss · AI Hot · Jul 6, 01:26

**背景**: 扩散模型是一类学习逆转加噪过程的生成模型，传统上用于图像生成，如今正被应用于文本生成领域，形成扩散语言模型。并行解码旨在通过同时解码多个 token，来突破传统自回归大语言模型逐 token 生成的序列化瓶颈。4 位量化通过降低模型精度来减少内存占用并提升速度，但由于注意力机制具有重尾激活分布以及 FP4 格式极小的动态范围，其量化一直尤为困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.00040">[2603.00040] Attn-QAT: 4-Bit Attention With Quantization ...</a></li>
<li><a href="https://haoailab.com/blogs/cllm/">Consistency Large Language Models: A Family of Efficient Parallel Decoders | Hao AI Lab @ UCSD</a></li>
<li><a href="https://medium.com/the-low-end-disruptor/what-is-diffusion-llm-and-why-it-matters-749033d1efb1">What is Diffusion LLM and why it matters | by Zheng... | Medium</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#LLM Acceleration`, `#Diffusion Models`, `#ICML 2026`, `#Model Quantization`

---

<a id="item-2"></a>
## [阿里云李飞飞阐述面向智能体时代的全栈就绪战略](https://aihot.virxact.com/items/cmr8jfeih02rgsl0d12n1bui2) ⭐️ 8.0/10

在新加坡举办的首届国际 Qwen 大会 2026 上，阿里云 CTO 李飞飞介绍了公司的全栈就绪战略，详细阐述了支撑智能体时代的四大基石。此次发布还伴随了 QwenCloud 和 Qwen3.7-Max 模型的推出，是阿里云面向智能体计算更广泛愿景的一部分。 这一战略标志着一家主要云服务商致力于构建专门为 AI 智能体优化的集成式端到端基础设施，而智能体代表了超越独立聊天机器人的下一次技术演进。通过在模型训练、服务和智能体执行方面提供可扩展且高性价比的解决方案，阿里云将自身定位为希望在生产环境中部署自主 AI 系统的企业的关键赋能者。 四大基石涵盖了 AI 智能体部署的全生命周期，从模型训练和推理服务到实际应用中的智能体执行。该战略将可扩展性和成本效益作为核心设计原则，充分利用阿里云现有的基础设施能力，包括容器服务、无服务器计算和专用 AI 硬件。

rss · AI Hot · Jul 6, 01:22

**背景**: AI 智能体是能够感知环境、做出决策并采取行动以实现特定目标的自主系统，代表了从被动 AI 模型向主动寻求目标的软件的转变。Qwen 模型系列是阿里巴巴的旗舰大语言模型家族，涵盖从开源 Apache 2.0 许可模型到企业级专有版本（如 Qwen-Max）的多种变体。Qwen 大会 2026 是阿里云展示其全面 AI 生态系统战略的平台，包括新推出的 QwenCloud 平台和 Qwen3.7-Max 模型，使公司在全球 AI 基础设施竞争中占据有利位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://omdia.tech.informa.com/om145535/qwen-conference-2026-is-a-window-into-alibaba-clouds-vision-for-the-agentic-era">Qwen Conference 2026 is a window into Alibaba Cloud’s vision for the agentic era Omdia</a></li>
<li><a href="https://www.alibabacloud.com/blog/qwen-conference-2026-a-first-look-at-the-exhibition-highlights_603119">Qwen Conference 2026: A First Look at the Exhibition Highlights! - Alibaba Cloud Community</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Alibaba Cloud`, `#AI Infrastructure`, `#AI Agents`, `#Qwen`, `#Full-Stack AI`

---

<a id="item-3"></a>
## [日本公布 AI 机器人战略修订版，目标 2040 年部署 1000 万台机器人](https://aihot.virxact.com/items/cmr8j82w402k1sl0dqsqextjc) ⭐️ 8.0/10

日本经济产业省于 6 月 30 日公布了《人工智能机器人战略》修订版，计划到 2040 年在 18 个领域部署 1000 万台 AI 机器人。政府将在未来 5 年内向由软银、NEC、本田、索尼等共同创立的 Noetra 公司提供合计 1 万亿日元（约 62 亿美元）资金，用于多模态基础模型和物理 AI 基础架构的开发。 这是全球范围内政府层面对物理 AI 和机器人基础设施最大规模的投入之一，旨在让日本利用其在机器人领域的传统优势，应对人口老龄化和少子化导致的严重劳动力短缺。该计划也标志着日本推动 AI 主权的战略意图，通过自主开发多模态基础模型而非完全依赖外国技术来构建国家竞争力。 仅 2026 财年的拨款就达 3873 亿日元（约 24 亿美元），Noetra 计划与日本国立研究开发法人产业技术综合研究所（AIST）合作在本财年发布首个基础模型。1000 万台机器人将部署于餐饮、食品制造、医疗等 18 个领域，后续版本将基于制造商数据逐年迭代改进。

rss · AI Hot · Jul 6, 01:07

**背景**: 物理 AI 是指能够利用运动技能理解和与现实世界交互的 AI 模型，通常部署在机器人或自动驾驶车辆等自主机器中。与纯软件 AI 不同，物理 AI 需要整合感知、行动和环境反馈，使机器人能够从真实环境条件中学习并适应。日本长期以来一直是全球工业机器人领域的领导者，但面临前所未有的人口危机——拥有世界上最老龄化的人口和持续低迷的出生率，这使得自动化成为国家战略优先事项。Noetra 公司是由日本多家大型企业新近合作成立的合资企业，旨在整合国内多模态 AI 领域的专业能力，与美国和中国的 AI 平台竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.asahi.com/sp/ajw/articles/16686174">Noetra selected for 1-trillion-yen project to create physical AI</a></li>
<li><a href="https://letsdatascience.com/news/japan-targets-sovereign-ai-model-and-10-million-robots-83b74c54">Japan Targets Sovereign AI Model and 10 Million Robots</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#AI Robotics`, `#Embodied AI`, `#Government Policy`, `#Physical AI`, `#Multimodal AI`

---

<a id="item-4"></a>
## [Anthropic 新模型工具调用倒退：Opus 4.8 与 Sonnet 5 在非主流 schema 上更不可靠](https://aihot.virxact.com/items/cmr8j4nr602iwsl0dhripqxmh) ⭐️ 8.0/10

An analysis reveals that newer Claude models exhibit degraded tool-calling reliability on non-standard schemas due to RL post-training priors learned from forgiving environments, highlighting that strict modes or constrained decoding are necessary.

rss · AI Hot · Jul 6, 00:53

**标签**: `#LLM`, `#Anthropic`, `#Tool Calling`, `#RLHF`, `#AI Evaluation`

---

<a id="item-5"></a>
## [NVIDIA 推出 GPU 收益分成计划，助力 AI 初创公司](https://aihot.virxact.com/items/cmr8h8vz4026lsl0dgldnodmn) ⭐️ 8.0/10

NVIDIA 推出了一项收益分成与信用支持计划，允许 AI 初创公司以未来产品和云收入的分成换取 GPU 计算资源，而无需提前支付费用。在该模式下，NVIDIA 不仅从 neocloud 提供商处获得标准硬件销售收入，还能持续抽取这些 GPU 所产生云收入的一定比例。 该计划从根本上将 GPU 从一次性硬件销售转变为长期经常性收入资产，在加深 NVIDIA 财务护城河的同时，降低了 AI 初创公司获取前沿训练和推理资源的门槛。它还强化了 NVIDIA 的生态锁定效应，因为初创公司和 neocloud 在财务上与 NVIDIA 的持续收入流紧密绑定。 该计划主要面向 neocloud GPU 提供商，它们借助 NVIDIA 的信用支持和收益分成结构采购基础设施，再将 GPU 租给需要训练、微调和大规模推理的 AI 初创公司。NVIDIA 已在 2026 年初承诺超 400 亿美元的 AI 生态投资，包括向 OpenAI 投资 300 亿美元，以及向 Corning Inc. 和 IREN Ltd. 投资数十亿美元。

rss · AI Hot · Jul 6, 00:16

**背景**: Neocloud 是一类新兴的云计算提供商，专注于提供 GPU 租赁服务，定位为 AWS 和 Google Cloud 等传统超大规模云厂商的替代方案。它们通常采用按需付费的定价模式、配备最新的 NVIDIA 硬件，并通过轻量级虚拟化实现接近原生的性能，因此在需要灵活获取高性能计算资源的 AI 开发者中广受欢迎。AI 产品开发的激增推动了对 GPU 资源的巨大需求，为 NVIDIA 创造了在传统硬件销售之外进一步变现计算基础设施的机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hothardware.com/news/nvidia-new-gpu-revenue-sharing-model">NVIDIA Disrupts Tech Supply Chain With New GPU Revenue Sharing Model | HotHardware</a></li>
<li><a href="https://www.thundercompute.com/blog/neoclouds-the-new-gpu-clouds-changing-ai-infrastructure">What is a Neocloud? The Rise of GPU-only Clouds (July 2026) | Thunder Compute</a></li>
<li><a href="https://mlq.ai/news/nvidia-launches-revenue-share-program-offering-ai-startups-gpu-access-without-upfront-payment/">Nvidia Launches Revenue-Share Program Offering AI Startups GPU Access Without Upfront Payment | MLQ News</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI Infrastructure`, `#GPU Compute`, `#AI Startups`, `#Venture Capital`

---

<a id="item-6"></a>
## [SK 海力士启动 280 亿美元美股上市，有望成史上第二大 IPO](https://www.ithome.com/0/972/896.htm) ⭐️ 8.0/10

SK 海力士正在纳斯达克启动规模约 280 亿美元的美国上市计划，通过美国存托凭证（ADR）发行 1779 万股新股，最终发行价将于周四敲定，周五正式挂牌交易。此次募资规模预计位列全球史上第二大 IPO，仅次于上月 SpaceX 创下的 857 亿美元纪录。 SK 海力士是英伟达和谷歌等企业 AI 加速器所用 HBM 芯片的全球最大供应商，此次 IPO 直接反映了大量资本正涌入 AI 硬件基础设施领域。该公司还宣布将投入 100 万亿韩元（约 4403 亿元人民币）新建多座芯片工厂，标志着为满足 AI 驱动的需求激增而进行前所未有的产能扩张。 每 10 份美国存托凭证对应 1 股普通股，发行价区间将参照 SK 海力士首尔交易所股价。受益于全球投资者对人工智能概念股的追捧，该公司股价年内累计涨幅超 270%，业绩表现远超主要竞争对手三星电子和美光科技。

rss · IT HOME · Jul 6, 01:09

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，通过将存储芯片垂直堆叠在处理器附近，而非使用传统的平面内存布局，从而提供大幅提升的数据带宽。HBM 已成为 AI 训练和推理的关键瓶颈组件，因为英伟达等 GPU 加速器需要巨大的内存带宽才能高效处理大语言模型。SK 海力士在 HBM3 及下一代 HBM 芯片领域占据市场主导地位，使其相对于三星和美光等竞争对手拥有显著优势。美国存托凭证（ADR）允许外国公司在美国交易所上市，使美国投资者可以像交易本国股票一样交易外国股票。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.fidelity.com/learning-center/investment-products/stocks/understanding-american-depositary-receipts">Understanding American Depositary Receipts (ADRs) - Fidelity</a></li>
<li><a href="https://www.appeconomyinsights.com/p/micron-rides-the-ai-boom">High - Bandwidth Memory is driving the up-cycle</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#SK Hynix`, `#HBM`, `#Semiconductors`, `#AI Infrastructure`

---

<a id="item-7"></a>
## [三星电子 Q2 营业利润预计同比暴涨 18 倍，AI 存储芯片需求持续引爆业绩](https://www.ithome.com/0/972/890.htm) ⭐️ 8.0/10

受人工智能产业持续扩张拉动存储芯片供给紧张、芯片价格走高影响，三星电子第二季度营业利润预计同比暴涨约 18 倍，达到 8.6 万亿韩元，再创历史新高。花旗证券研报指出，第二季度 DRAM、NAND 闪存平均售价环比分别大涨 44% 和 53%。 这一空前的利润暴涨表明，AI 基础设施的热潮已超越高带宽内存（HBM），广泛影响包括普通 DRAM 和 NAND 闪存在内的整个存储芯片生态系统。供需失衡正在重塑全球半导体格局，三星、SK 海力士和美光市值均突破 1 万亿美元大关，并计划投入数千万亿韩元扩充产能。 本轮高景气不仅由 HBM 拉动，智能体（Agentic AI）等各类 AI 应用因需执行更复杂、多步骤的任务，同步大幅推高了普通 DRAM 和 NAND 闪存的需求。分析师提示，若三星员工奖金准备金计提（累计或突破 40 万亿韩元）超出预期，二季度最终业绩或将不及市场一致预期；摩根大通也警告 AI 相关资本开支的可持续性是当前存储芯片牛市最大隐患。

rss · IT HOME · Jul 6, 00:57

**背景**: 高带宽内存（HBM）是由三星和 SK 海力士联合研发的 3D 堆叠技术高性能 DRAM，两家韩国芯片巨头共同掌握全球 95%以上的 HBM 产能，是 AI 时代最关键的供应命脉。HBM 采用垂直堆叠和硅插层技术大幅提升存储容量和带宽，使其成为神经网络训练和推理等高数据吞吐任务的理想选择。智能体 AI（Agentic AI）代表了从对话式 AI 向自主系统的范式转变，利用多个专业化 AI 智能体协作来完成复杂、多步骤的目标。与早期聚焦模型训练的 AI 应用不同，智能体系统在推理过程中需要显著更多的内存和存储来执行实时决策和数据调取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>
<li><a href="https://36kr.com/p/3313095089120008">还傻傻分不清AI Agent和Agentic AI？康奈尔大学最新综述来了，一文读懂-36氪</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Memory Chips`, `#HBM`, `#Hardware`, `#Agentic AI`

---