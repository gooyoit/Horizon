---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> From 103 items, 8 important content pieces were selected

---

1. [vLLM 发布 v0.26.0：带来 DeepSeek-V4 优化及新模型支持](#item-1) ⭐️ 9.0/10
2. [面向 Claude 5 代模型的上下文工程新规则](#item-2) ⭐️ 9.0/10
3. [特斯拉 Robotaxi 车队率先搭载 FSD v15 早期版本，模型参数扩大 10 倍](#item-3) ⭐️ 9.0/10
4. [特斯拉完成近 20 亿美元收购未公开 AI 硬件公司](#item-4) ⭐️ 8.5/10
5. [Google AI Edge 端侧模型分工策略与 Nunchaku 4-bit 推理集成至 Hugging Face Diffusers](#item-5) ⭐️ 8.0/10
6. [Anthropic 自研 AI 芯片项目向 SK 海力士寻求存储芯片供应](#item-6) ⭐️ 8.0/10
7. [眸深智能完成近亿元融资，打造基于“世界动作模型”的端侧具身大脑](#item-7) ⭐️ 8.0/10
8. [🤖 梁文锋因内部言论遭外泄感到不满，暂停 DeepSeek 新一轮融资](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM 发布 v0.26.0：带来 DeepSeek-V4 优化及新模型支持](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 正式发布，包含了来自 212 位贡献者的 411 次提交，为跨多种硬件平台（包括 AMD 和 XPU）的 DeepSeek-V4 引入了重大性能优化。此次更新还增加了对全新 Inkling 模型家族的全栈支持、用于生成模型的 fp32 `lm_head`、灵活的注意力后端，以及更加成熟的 KV 卸载功能。 作为大语言模型（LLM）推理和服务的关键开源引擎，这些更新通过最大化前沿混合专家模型的效率，直接推动了 AI 基础设施的尖端发展。推测解码和自定义路由内核等高级推理技术的引入，确保了大规模企业和研究应用能够实现更快速、更具成本效益的部署。 显著的技术改进包括用于大幅加速 DeepSeek-V4 端到端每个输出标记时间（E2E TPOT）的专用路由内核和 `fused_topk_bias`，以及针对新 Inkling 模型的分段 CUDA 图支持和 Hopper FA4 相对注意力机制。该版本还允许开发人员针对每个 KV 缓存组选择不同的注意力后端，并引入了用于二级对象存储的分层事件处理机制。

github · vllm-project/vllm · Jul 25, 10:38

**背景**: vLLM 是一款广受欢迎的开源推理和部署引擎，旨在最大化大语言模型的吞吐量和内存效率。DeepSeek-V4 是一个强大的全新混合专家模型系列，每个标记仅激活其总参数的一小部分，并利用先进的混合注意力布局来处理超长上下文。优化 MoE 架构的推理需要专门的内核来高效路由标记和管理内存，这使得像 vLLM 这样的社区项目在实际部署中变得不可或缺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/">vLLM — Fast, Memory-Efficient LLM Inference & Serving</a></li>
<li><a href="https://arxiv.org/abs/2606.19348">[2606.19348] DeepSeek-V4: Towards Highly Efficient Million ...</a></li>
<li><a href="https://learnaivisually.com/ai-explained/vllm-v0-20-fa4-packing">vLLM v0.20 — FlashAttention 4 packing — What does it mean?</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#open-source`, `#ai-infrastructure`, `#deepseek`

---

<a id="item-2"></a>
## [面向 Claude 5 代模型的上下文工程新规则](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 9.0/10

Anthropic 发布了一篇文章，概述了专为下一代 Claude 模型量身定制的上下文工程新策略，重点探讨如何为 AI 智能体在上下文窗口中优化信息的管理与筛选。该指南引入了处理智能体记忆、推理透明度和指令设计的更新技术，与以往的提示工程实践有所不同。 随着大语言模型日益向智能体化发展，有效管理上下文（包括哪些信息进入上下文窗口以及如何组织这些信息）正成为决定智能体可靠性和性能的关键因素。这一转变将上下文工程从小众的提示技巧提升为生产级 AI 系统的核心学科，影响着开发者如何架构智能体记忆和交互流程。 上下文工程涵盖了在 LLM 推理过程中筛选最佳 token 集合的策略，包括管理短期和长期智能体记忆、检索增强生成（RAG），以及进入上下文窗口的外部信息。从业者提出的一个显著担忧是，随着模型越来越依赖自动化记忆和隐藏的推理轨迹，操作者对决策过程的可见性降低，使得调试不需要的智能体行为变得更加困难。

hackernews · mellosouls · Jul 25, 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: 上下文工程是指在 LLM 推理过程中筛选和维护最佳 token（信息）集合的一系列策略，它超越了传统的提示工程，涵盖了可能出现在上下文窗口中的所有信息。AI 智能体记忆是系统跨任务和交互存储及回忆过去经验的能力，与 RAG 和上下文工程等相关概念有所区别。思维链（CoT）推理通过添加中间推理步骤使 LLM 的预测更具可解释性，但更新的模型正越来越多地隐藏这些轨迹，引发了透明度方面的担忧。随着模型能力的增强和智能体化的发展，管理它们所处理信息的复杂性已显著增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-memory">What Is AI Agent Memory? | IBM</a></li>
<li><a href="https://arxiv.org/html/2506.21812v1">Towards Transparent AI: A Survey on Explainable Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一，多位评论者对 Anthropic 的建议表示怀疑。主要担忧包括：过度依赖 Claude 的自动记忆功能，该功能在缺乏透明推理轨迹的情况下做出难以理解的跳跃性判断；怀疑该指南旨在通过将配置从可移植的 markdown 文件转移到 Anthropic 专用工具中来增加供应商锁定；以及观察到这些建议似乎是常识，或者与从业者在实践中观察到的情况不符。一位评论者幽默地指出，设计一种具有明确关键词的专用语言来编码需求，本质上是在重新发明传统编程。

**标签**: `#AI`, `#LLMs`, `#Prompt Engineering`, `#Anthropic`, `#AI Agents`

---

<a id="item-3"></a>
## [特斯拉 Robotaxi 车队率先搭载 FSD v15 早期版本，模型参数扩大 10 倍](https://www.ithome.com/0/981/618.htm) ⭐️ 9.0/10

此次部署展示了特斯拉利用 Robotaxi 车队作为真实世界测试平台，在向消费者发布前验证重大 AI 模型升级的策略，有望加速无人监督自动驾驶的商业化进程。模型参数 10 倍的扩展意味着 AI 模型从海量驾驶数据中学习的能力将大幅提升，可能显著改善决策能力和安全性能。 Robotaxi 车辆采用的是标准版 HW4 硬件，仅增加了 Project Halo 通信模块和摄像头清洗喷淋装置，与消费者购买的车型几乎相同。FSD v15 将不支持旧版 HW3 硬件车辆，后者将获得 FSD v14 Lite 作为最后一个主要版本更新，而 v15 的正式版计划于今年晚些时候或明年初发布。

rss · IT HOME · Jul 25, 23:57

**背景**: 特斯拉的完全自动驾驶（FSD）是一套先进的驾驶辅助系统，旨在通过基于视觉的神经网络方法实现完全自动驾驶，依赖摄像头而非激光雷达。Hardware 4（HW4）又称 AI4，是特斯拉最新的自动驾驶计算机，具备更强的神经处理能力、升级的摄像头和改进的雷达。Robotaxi 服务是特斯拉的商业自动驾驶出行网络，目前在奥斯汀、迈阿密、奥兰多和坦帕等城市进行无人监督运营。扩展 AI 模型参数是深度学习中的关键技术，更大的模型在充足数据训练下通常能展现出更好的模式识别和决策能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notateslaapp.com/news/4484/tesla-robotaxis-are-already-running-fsd-v15">Tesla Robotaxis Are Running FSD V15 - Not a Tesla App</a></li>
<li><a href="https://teslanorth.com/2026/04/09/tesla-fsd-v15-musk-teases-unsupervised-safety-with-10x-larger-ai-model/">Tesla FSD v15: Musk Teases “Unsupervised” Safety With 10x Larger AI Model | TeslaNorth.com</a></li>
<li><a href="https://grokipedia.com/page/Tesla_Hardware_4">Tesla Hardware 4 — Grokipedia</a></li>

</ul>
</details>

**标签**: `#Autonomous Vehicles`, `#Tesla FSD`, `#Embodied AI`, `#Robotics`, `#Frontier AI`

---

<a id="item-4"></a>
## [特斯拉完成近 20 亿美元收购未公开 AI 硬件公司](https://aihot.virxact.com/items/cms1301qr00xzro0wl0xe6as5) ⭐️ 8.5/10

特斯拉在最新的 10-Q 季度报告中披露，公司已于第二季度完成对一家未公开名称的 AI 硬件公司的收购，交易对价约为 19.5 亿美元的普通股和股权奖励。其中 2.22 亿美元专门用于收购关键专利及已开发技术资产，剩余 17.3 亿美元与业绩目标挂钩。 此次收购对特斯拉而言极为罕见，因为公司历来坚持垂直整合战略，依赖内部研发而非外部并购，历史上仅收购过约 10 家公司。斥资 2.22 亿美元购买专利资产表明，目标公司掌握着特斯拉无法自行研发或从马斯克旗下其他企业获取的关键知识产权，可能将大幅加速其下一代 FSD 系统和 Optimus 人形机器人的发展。 业界猜测最有可能的收购对象是两家公司：一是由特斯拉 Dojo 超级计算机团队前成员创立、专注于大语言模型推理 AI 加速器的 DensityAI；二是由知名芯片架构师吉姆·凯勒联合创立、专注于半导体制造工具和小型晶圆厂技术的 Atomic Semi。交易结构中大部分对价与业绩目标挂钩，表明大部分价值取决于被收购团队在技术部署方面的持续交付能力。

rss · AI Hot · Jul 26, 00:40

**背景**: 特斯拉的 FSD（Full Self-Driving）是一套高级辅助驾驶系统，目前处于 L2+级别，需要驾驶员保持注意力监督，但公司计划通过数据积累和模型训练逐步进化至无需监督的 L4 自动驾驶。Optimus 是特斯拉的人形机器人项目，与 FSD 共用视觉神经网络和自研 AI 芯片，马斯克曾表示它将贡献特斯拉未来 80%的价值。这两个项目都需要越来越强大的定制 AI 芯片来实现实时端侧计算，因此专用芯片技术成为特斯拉长期战略规划中的关键资产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/特斯拉自动驾驶">特斯拉自动驾驶 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/特斯拉人形机器人Optimus/67666697">特斯拉人形机器人Optimus_百度百科</a></li>
<li><a href="https://www.readmusk.com/optimus">擎天柱 Optimus:特斯拉机器人(人形机器人)量产与进展 · 读懂马斯克</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#AI Hardware`, `#Robotics`, `#Autonomous Driving`, `#M&A`

---

<a id="item-5"></a>
## [Google AI Edge 端侧模型分工策略与 Nunchaku 4-bit 推理集成至 Hugging Face Diffusers](https://aihot.virxact.com/items/cms1340wa011cro0w07md5o4g) ⭐️ 8.0/10

Google AI Edge 提出了端侧模型分层分工策略：1B-4B 参数的小模型负责通用推理，50M-500M 参数的微型模型通过微调完成低延迟动作。此外，Nunchaku 的 SVDQuant 4-bit 推理引擎已集成至 Hugging Face Diffusers，推理速度最高提升 1.8 倍。 这两项进展都致力于解决在资源受限的边缘设备上高效部署 AI 的关键挑战，这些设备的算力和内存都十分有限。智能模型编排与极致量化技术的结合，将显著加速端侧生成式 AI 在移动和嵌入式平台上的普及。 SVDQuant 是一种训练后量化技术，通过低秩分支吸收异常值，在保持视觉保真度的同时实现权重和激活值的 4-bit 量化。Nunchaku 引擎融合了低秩和低比特分支内核，以减少内存使用并消除冗余的数据移动，用户现在可以通过简单的 pip install 直接在 Diffusers 中加载预量化流水线。

rss · AI Hot · Jul 26, 00:30

**背景**: 端侧 AI 在模型大小、推理速度和输出质量之间存在固有的权衡，使得在本地运行大模型十分困难。量化技术通过降低模型参数的精度（例如从 16-bit 降至 4-bit）来缩小模型体积并加速推理，但过度量化通常会引入导致质量下降的异常值。作为 ICLR 2025 Spotlight 论文提出的 SVDQuant 技术通过将异常值从激活值转移到权重，并利用低秩分支加以吸收来解决这一问题。Hugging Face Diffusers 是运行扩散模型的广泛使用的库，集成 Nunchaku 后用户不再需要单独部署推理引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Nunchaku-AI/Nunchaku">GitHub - nunchaku-ai/nunchaku: [ICLR2025 Spotlight] SVDQuant ...</a></li>
<li><a href="https://huggingface.co/blog/nunchaku-diffusers">Bringing Nunchaku 4-bit Diffusion Inference to Diffusers</a></li>
<li><a href="https://arxiv.org/abs/2411.05007">[2411.05007] SVDQuant: Absorbing Outliers by Low-Rank ... SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit ... SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit ... SVDQuant / Nunchaku - Sol-Engine Documentation dbw6/svdquant | DeepWiki</a></li>

</ul>
</details>

**标签**: `#On-Device AI`, `#Model Optimization`, `#Inference Acceleration`, `#Hugging Face`, `#Google AI`

---

<a id="item-6"></a>
## [Anthropic 自研 AI 芯片项目向 SK 海力士寻求存储芯片供应](https://aihot.virxact.com/items/cms1301qr00y2ro0wd3iuhx50) ⭐️ 8.0/10

SK 集团会长崔泰源在旧金山的一场 AI 活动上透露，Anthropic 已就其自研芯片项目向 SK 海力士寻求存储半导体供应。此前 The Information 曾报道，Anthropic 已启动自研 AI 芯片的早期开发，并正与三星电子洽谈采用其 2nm 制程工艺及先进封装技术的定制项目。 Anthropic 进军自研芯片，标志着这家前沿 AI 实验室正战略性地减少对 NVIDIA GPU 的依赖，以获得对计算基础设施更大的掌控权。通过与三星 2nm 制程和 SK 海力士存储芯片建立先进制造合作关系，Anthropic 有望在训练和部署大语言模型的成本与效率方面获得竞争优势。 该项目目前仍处于早期开发阶段，正在考虑采用三星的 2nm 晶圆代工制程和先进封装技术进行制造。SK 海力士作为对 AI 工作负载至关重要的高带宽存储器（HBM）领域的领导者，极有可能为 Anthropic 的定制逻辑芯片设计提供配套的存储组件。

rss · AI Hot · Jul 26, 00:15

**背景**: 随着 AI 模型规模的快速扩张，Google、Amazon 和 Meta 等大型 AI 公司越来越多地投资自研 AI 芯片（ASIC），以优化性能并减少对昂贵的 NVIDIA GPU 的依赖。2nm 制程节点代表了半导体制造的最前沿，相比前几代在晶体管密度和能效方面有显著提升。先进封装技术（如芯粒设计和 3D 堆叠）通过紧密集成逻辑和存储组件，对于最大化现代 AI 加速器的性能同样至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia">The custom AI ASIC state of play (May 2026) - Tom's Hardware</a></li>
<li><a href="https://anysilicon.com/the-ultimate-guide-to-semiconductor-packaging/">The Ultimate Guide to Semiconductor Packaging - AnySilicon</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Chips`, `#AI Infrastructure`, `#Semiconductors`, `#Hardware`

---

<a id="item-7"></a>
## [眸深智能完成近亿元融资，打造基于“世界动作模型”的端侧具身大脑](https://36kr.com/p/3911162147640456?f=rss) ⭐️ 8.0/10

具身智能初创公司「眸深智能」已获得近亿元人民币的 Pre-A 轮追加融资，使其估值在今年上半年增长了超 10 倍。该公司推出了 STI-WM（时空一体世界动作模型），通过结合互联网视频、动捕数据和真机数据的新颖训练配方，将对真机训练数据的需求降低了 90%。 眸深智能通过将动作处理为离散的 Token，走出了与主流 VLA（视觉-语言-动作）架构不同的路线，实现了复杂机器人任务的零样本泛化。其软硬协同的设计方法将端侧推理成本从 20 万元大幅降至 1 万元，有望加速经济型自主机器人的大规模部署。 核心团队拥有海思、英特尔和英伟达的专家背景，使他们能够将千亿参数模型压缩至百亿级别，同时将推理延迟从 200 毫秒降至 10 毫秒。他们已将模型原生适配海思（昇腾）和地平线等国产芯片，并且其原创的 MLD 和 MotionGPT 技术已被英伟达 DAIR 实验室多次引用。

rss · 36kr · Jul 26, 01:00

**背景**: VLA（视觉-语言-动作）模型目前是机器人领域的主流方法，通过统一视觉、语言和动作数据来学习通用策略。眸深智能替代性的“世界动作模型”方法使用隐空间扩散模型来生成自然的人体动作，并将连续动作离散化为基本单元（类似于大语言模型中的词汇），以实现更好的长序列规划。通过预测下一个“动作 Token”，系统能够自主组合出复杂行为，而无需逐帧编程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuyun97.github.io/embodied-ai-learning/vla/">VLA (视觉-语言-动作)模型发展深度调研报告 | 具身星图</a></li>
<li><a href="https://arxiv.org/abs/2510.07077">[2510.07077] Vision-Language-Action Models for Robotics: A ...</a></li>
<li><a href="https://numfer.com/ChenFengYe/motion-latent-diffusion">motion - latent - diffusion : Text-to- Motion with Diffusion</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#Edge AI`, `#VLA Models`, `#Funding`

---

<a id="item-8"></a>
## [🤖 梁文锋因内部言论遭外泄感到不满，暂停 DeepSeek 新一轮融资](https://www.bloomberg.com/news/articles/2026-07-25/deepseek-said-to-tell-backers-of-funding-pause-after-viral-posts) ⭐️ 8.0/10

DeepSeek has paused its massive new funding round reportedly due to founder Liang Wenfeng's displeasure over leaked internal comments, while simultaneously preparing for a potential IPO as early as 2026.

telegram · @zaihuapd · Jul 26, 01:17

**标签**: `#DeepSeek`, `#AI Funding`, `#Frontier AI`, `#IPO`, `#AI Industry`

---