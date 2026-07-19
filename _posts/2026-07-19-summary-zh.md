---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> From 110 items, 19 important content pieces were selected

---

1. [Kimi K3 时刻：开源权重模型挑战美国前沿实验室](#item-1) ⭐️ 9.0/10
2. [Sunday Robotics 发布 ACT-2 模型，宣称在陌生家庭叠衣成功率超 99%](#item-2) ⭐️ 9.0/10
3. [月之暗面发布 Kimi K3：2.8T 开源模型登顶前端编程 Arena](#item-3) ⭐️ 9.0/10
4. [GPT-5.6 通过提示词解决凸优化领域 30 年悬而未决的问题](#item-4) ⭐️ 8.0/10
5. [Anthropic 宣布 Claude Fable 5 永久保留在订阅计划中](#item-5) ⭐️ 8.0/10
6. [荣耀发布 AgenticOS 操作系统，Robot Phone 搭载四自由度机械云台](#item-6) ⭐️ 8.0/10
7. [开源 AI 进展：腾讯具身智能突破与编码能力差距缩小](#item-7) ⭐️ 8.0/10
8. [开放权重模型逼近前沿，部署治理成新焦点](#item-8) ⭐️ 8.0/10
9. [英伟达 CEO 黄仁勋东京行：敲定国家级 AI 工厂合作，送粉丝红豆糕](#item-9) ⭐️ 8.0/10
10. [Anthropic 将 Claude Fable 5 推送至 Max 和 Team Premium 订阅用户](#item-10) ⭐️ 8.0/10
11. [腾讯在 WAIC 2026 发布具身智能全栈方案及 ADP 4.0 海外版](#item-11) ⭐️ 8.0/10
12. [月之暗面有望最快六个月内赴港上市](#item-12) ⭐️ 8.0/10
13. [安谋科技发起“开源 AIOS 联盟”，联合国内主要芯片厂商](#item-13) ⭐️ 8.0/10
14. [SpaceX 与五角大楼谈判提供 AI 算力，交易或达数十亿美元](#item-14) ⭐️ 8.0/10
15. [OpenRouter 被传收到收购意向，估值或超 13 亿美元](#item-15) ⭐️ 8.0/10
16. [台积电宣布 A14（1.4nm）制程将于 2028 年投产](#item-16) ⭐️ 8.0/10
17. [特朗普政府拟设类似 FINRA 的独立机构审查顶尖 AI 模型](#item-17) ⭐️ 8.0/10
18. [SK 海力士 CEO 预警：2027 年将迎史上最严重内存短缺](#item-18) ⭐️ 8.0/10
19. [商汤发布 SenseNova U1 Pro 多模态智能体基座](#item-19) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3 时刻：开源权重模型挑战美国前沿实验室](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

月之暗面（Moonshot AI）发布了 Kimi K3，这是一个拥有 2.8 万亿参数的混合专家（MoE）多模态模型，具备 100 万 token 的上下文窗口，并采用了全新的 Kimi Delta Attention（KDA）和注意力残差架构。此次发布引发了广泛讨论，焦点在于模型蒸馏和开源权重模型如何迅速瓦解美国前沿 AI 实验室的竞争壁垒。 Kimi K3 代表了一个关键时刻：前沿级别的 AI 能力正在通过开源权重实现商品化和平民化，打破了地域限制。这挑战了只有资金雄厚的美国实验室才能在 AI 能力上保持持续领先地位的假设，并引发了人们对闭源模型商业策略长期可行性的质疑。 Kimi K3 采用混合专家架构，拥有 2.8 万亿参数，支持文本、图像和视频输入以及 100 万 token 的上下文窗口，专为长周期智能体任务设计，支持可切换的最大努力思考模式。要使用完整的 100 万上下文，需要订阅每月 79 美元或更高级别的套餐，而入门级每月 15 美元的套餐完全不支持 K3。

hackernews · sbochins · Jul 18, 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**背景**: 知识蒸馏是一种机器学习技术，通过训练一个更小、更高效的模型来复制更大、更强模型的行为和输出，从而以更低的成本实现知识转移。开源权重模型则公开发布训练好的神经网络参数，允许任何人在本地下载、运行并基于该模型进行开发。这两种方法的结合意味着，一旦前沿实验室发布了一个强大的模型（即使仅通过 API），竞争对手就有可能将其能力蒸馏成更廉价的开源权重替代品，从而加速尖端 AI 的商品化进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K 3 - Kimi API Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为前沿 AI 能力的商品化是不可避免的，只是有人指出这一天的到来比预期更快。用户对 Kimi K3 的定价层级和资源消耗提出了实际疑虑，有用户报告称在执行类似任务时，Kimi K3 比 OpenAI 消耗了更多的时间和用量配额。部分评论者对潜在的监管反弹表示担忧，将其与 Napster 进行类比，推测西方政府最终可能将开源权重前沿模型归类为国家安全风险。

**标签**: `#AI`, `#LLM`, `#Kimi K3`, `#Open Weights`, `#Distillation`

---

<a id="item-2"></a>
## [Sunday Robotics 发布 ACT-2 模型，宣称在陌生家庭叠衣成功率超 99%](https://www.ithome.com/0/978/617.htm) ⭐️ 9.0/10

美国初创公司 Sunday Robotics 发布了新一代机器人 AI 模型 ACT-2，该模型应用于其轮式家庭机器人 Memo，据称在陌生家庭环境中叠衣服的成功率超过 99%，且无需重新训练。公司还提出了一套名为 Solve 的机器人行业新评估标准，以促进机器人任务测试的透明度。 这一突破解决了家庭机器人领域关键的零样本迁移瓶颈，即机器人传统上难以将实验室中学到的任务泛化到全新的、不可预测的环境中。通过在复杂的家庭环境中展示可靠的泛化能力，ACT-2 有望大幅加速自主家庭机器人的商业化进程。 ACT-2 采用了两阶段训练方法：首先通过佩戴定制的 200 美元传感器手套采集人类示范来学习基本动作，然后通过自建测试平台上的自主练习快速提升能力。虽然目前叠衣服是唯一达到 Solve 可靠性标准的任务，但该模型也正在学习吸尘、整理玩具和制作咖啡等更多技能。

rss · IT HOME · Jul 19, 00:06

**背景**: 机器人领域的零样本泛化是指机器人利用预训练中获得的知识，在从未接受过专门训练的环境中或面对未知物体时执行任务的能力。ACT（Action Chunking with Transformers）模型架构最初由 Tony Zhao 在斯坦福大学开发，是一种从遥操作数据中预测短序列动作的模仿学习方法。具身智能（Embodied AI）专注于将人工智能集成到机器人等物理系统中，以与现实世界进行交互和操作；由于家庭环境缺乏结构化且充满不可预测性，因此被认为是该领域极具挑战性的场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.patsnap.com/resources/blog/articles/foundation-models-for-zero-shot-robotics-40-patents-2/">Foundation models for zero - shot robotics : 40+ patents | PatSnap</a></li>
<li><a href="https://github.com/tonyzhaozh/act">GitHub - tonyzhaozh/act</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">Embodied AI: What Is It and How to Build It?</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#ACT-2`, `#Zero-shot Generalization`, `#Frontier Tech`

---

<a id="item-3"></a>
## [月之暗面发布 Kimi K3：2.8T 开源模型登顶前端编程 Arena](https://t.me/zaihuapd/42637) ⭐️ 9.0/10

月之暗面发布了全球首个 2.8 万亿参数的开源模型 Kimi K3，该模型基于全新的 Kimi Delta Attention（KDA）与 Attention Residuals 架构构建。K3 具备原生视觉能力和 100 万 token 的上下文窗口，并以 1679 分在第三方基准 Frontend Code Arena 中首次登顶，超越了 Fable 5 和 GPT-5.6 Sol。 此次发布代表了开源前沿 AI 的重大飞跃，证明了开源模型在前端编程等高价值专业领域能够超越顶尖的闭源系统。庞大的参数规模、注重效率的新颖架构以及 100 万 token 上下文窗口的结合，为开源模型在智能体和多模态智能方面所能达到的高度树立了新的标杆。 Kimi K3 在基于人类偏好的 Frontend Code Arena 中获得 1679 分，在 7 个评测领域中有 6 项排名第一，仅在游戏领域落后。其底层架构采用 3:1 的比例交替使用 Kimi Delta Attention 层和完整的 Multi-Head Latent Attention 层，从而在计算成本和模型表达能力之间实现了最佳平衡。

telegram · @zaihuapd · Jul 18, 02:29

**背景**: Kimi Delta Attention（KDA）是一种混合线性注意力模块，它通过更细粒度的门控机制扩展了 Gated DeltaNet，能够更有效地利用有限状态的 RNN 内存，从而满足智能体对效率的需求。Attention Residuals（AttnRes）是另一种架构改进，它用可学习的 softmax 注意力机制取代了标准的固定权重残差连接，改善了深度网络跨时间和深度处理信息的方式。Frontend Code Arena 是 Arena.ai 上的一个排行榜，根据人类对真实前端编程任务的偏好对 AI 模型进行排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://officechai.com/ai/kimi-k3-beats-fable-5-gpt-5-6-sol-on-frontend-code-arena/">Kimi K3 Beats Fable 5, GPT 5.6 Sol On Frontend Code Arena</a></li>
<li><a href="https://wispaper.ai/en/blog/attention-residuals-20260320/eng">Attention Residuals</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Source AI`, `#Moonshot AI`, `#Code Generation`, `#Multimodal AI`

---

<a id="item-4"></a>
## [GPT-5.6 通过提示词解决凸优化领域 30 年悬而未决的问题](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 8.0/10

用户成功通过提示词引导 GPT-5.6 解决了凸优化领域一个悬而未决 30 年的猜想，据报道使用 Sol Pro 版本仅耗时 148 分钟。然而，该用户此前已用早期 GPT 版本研究该问题长达一年，并将所有先前的研究成果和解题技巧都输入到了提示词中。 这展示了 AI 辅助数学研究能力的重大飞跃，表明在前沿大语言模型配合专家级提示词工程的情况下，可以参与解决长期悬而未决的开放性问题。这也预示着数学家和理论计算机科学家的研究方式可能发生转变，低至中等难度的问题的解决过程有望被自动化。 该问题涉及为球面域上的凸 Lipschitz 函数优化问题建立时间复杂度的上界。这一成果是使用 ChatGPT Pro（Sol Pro）完成的，据推测该版本是一个多智能体系统，能够并行运行多个 LLM 并选择最佳答案，而非使用 Ultra 版本。

hackernews · mbustamanter · Jul 18, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，专注于在凸集上最小化凸函数，许多此类问题存在多项式时间算法。定理证明已成为评估 AI 高级推理能力的基准，诸如 DeepTheorem 等系统正在推动 LLM 在形式化数学推理方面的能力。为优化算法建立复杂度边界——包括上界和下界——是理论计算机科学中的基本问题，决定了问题在规模扩大时能被多高效地解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2505.23754">DeepTheorem: Advancing LLM Reasoning for Theorem Proving ...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，这一成果更多体现了专家引导下的人机协作而非 AI 自主发现，指出用户一年的前期工作已嵌入提示词中。部分讨论涉及对数学研究职业的影响，将其与 AI 对初级软件开发者的影响进行类比——认为数学领域中低难度和中等难度的问题可能不再值得人工研究。此外还有关于 ChatGPT Pro（多智能体并行选择）与 Ultra 版本之间技术差异的讨论。

**标签**: `#AI Reasoning`, `#Mathematics`, `#Theorem Proving`, `#Convex Optimization`, `#LLMs`

---

<a id="item-5"></a>
## [Anthropic 宣布 Claude Fable 5 永久保留在订阅计划中](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic 于 7 月 20 日撤销了将 Claude Fable 5 限制为仅限 API 使用的决定，将该模型以 50% 的用量限制永久纳入 Max 和 Team Premium 订阅计划。Pro 和 Team Standard 用户将通过使用额度继续保留访问权限，并获得一次性 100 美元的赠金，但基础版 20 美元/月的计划仍不包含 Fable 5。 这一逆转突显了前沿模型提供商之间激烈的竞争正在直接塑造定价和访问策略，因为 Anthropic 无法证明在不包含其最佳模型的情况下收取高额订阅费是合理的。它表明来自 OpenAI 的 GPT-5.6 和月之暗面的 Kimi 3 等竞争对手的市场压力，迫使 AI 实验室在计算成本优化与客户留存之间优先考虑后者。 Claude Fable 5 是 Anthropic 目前最强大的通用 Mythos 级模型，具备 100 万 token 的上下文窗口，专为处理大型、长时间运行和自主的知识工作任务而优化。将其转为仅限 API 访问的最初计划是出于计算能力限制的考虑，这引发了 Anthropic 是否需要减少训练资源以释放 GPU 来服务该模型的疑问。

rss · Simon Willison · Jul 18, 06:00

**背景**: Anthropic 此前计划将 Claude Fable 5 从订阅层级中移除，仅通过 API 定价提供，这一决定是出于 GPU 和计算能力的考量。这意味着每月支付 100 或 200 美元的订阅用户将无法使用 Anthropic 的最佳模型，社区将此称为 'Fablepocalypse'（Fable 末日）。然而，OpenAI 于 2026 年 7 月 9 日发布了 GPT-5.6 Sol，该模型在编程基准测试中以更少的 token 和时间超越了 Fable 5，而月之暗面拥有 2.8 万亿参数的 Kimi K3 也带来了进一步的竞争压力。这些因素共同使 Anthropic '高价订阅却不提供最佳模型'的方案变得无法维持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 指出，许多用户在原定的订阅访问截止日期前为了最大化使用 Fable 5 而焦虑失眠，并对避免了 'Fablepocalypse' 表示如释重负。他还推测 Anthropic 是否需要缩减其模型训练工作，以将 GPU 资源重新分配给为订阅用户提供 Fable 5 服务。

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#AI Industry`, `#Frontier Models`

---

<a id="item-6"></a>
## [荣耀发布 AgenticOS 操作系统，Robot Phone 搭载四自由度机械云台](https://aihot.virxact.com/items/cmrr2piat01mybi18orun4ikt) ⭐️ 8.0/10

荣耀在 2026 世界人工智能大会上发布了 AgenticOS 操作系统，这是一款意图驱动的多模态智能体系统，拥有行业首个系统级 Agent 架构。将于 8 月发布的 Robot Phone 搭载第五代骁龙 8 至尊版芯片，首发 AgenticOS 内核，并配备行业最小的四自由度钛合金机械云台。 这标志着具身智能、多模态智能体与消费级硬件的重大融合，推动智能手机从被动工具向主动智能伙伴转变。系统级 Agent 架构通过支持跨场景的多智能体协同，可能从根本上改变用户与设备的交互方式。 AgenticOS 具备意图驱动、自然交互、主动智能和天生跨端四大核心特征，支持全局多智能体协同和全场景自适应沉淀。Robot Phone 的四自由度云台体积比主流方案缩小 70%，能够物理移动摄像头模组实现电影级自动取景，并搭载 2 亿像素主摄。

rss · AI Hot · Jul 19, 00:30

**背景**: 智能体 AI 操作系统是一种软件基础设施层，负责管理自主 AI 智能体的完整生命周期，包括调度、内存管理、工具编排和多智能体协同。与传统操作系统要求用户手动启动应用并逐步操作不同，智能体操作系统是意图驱动的——用户只需表达需求，系统便会自主编排智能体来完成任务。荣耀 Robot Phone 的电动云台能够物理转动摄像头模组，而非仅依赖传感器级别的防抖，体现了移动影像领域的具身智能方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dezeen.com/2026/03/04/honor-robot-phone-smartphone-with-articulating-arm-technology/">Honor's Robot Phone is a smartphone with an articulating arm</a></li>
<li><a href="https://gagadget.com/en/718695-honor-robot-phone-enters-mass-production-with-a-motorized-gimbal-and-200mp-camera/">Honor Robot Phone enters mass production with a motorized gimbal ...</a></li>

</ul>
</details>

**标签**: `#Agentic AI`, `#Operating System`, `#Embodied AI`, `#Consumer Hardware`, `#Multimodal`

---

<a id="item-7"></a>
## [开源 AI 进展：腾讯具身智能突破与编码能力差距缩小](https://aihot.virxact.com/items/cmrr2vrf701pfbi18zokznw0d) ⭐️ 8.0/10

腾讯 Robotics X 实验室发布了多款具身智能基座模型，其中 HyVLA-0.5 在日化工厂实测作业中成功率超过 95%。与此同时，开放权重 AI 模型在编码基准测试中已接近闭源模型水平，但生产落地率仍落后。 这些进展表明具身智能正从实验室演示迈向真实工业部署，有望彻底改变制造业和物流行业。开放权重模型与闭源模型在编码能力上的差距缩小，也暗示着 AI 民主化趋势可能重塑行业竞争格局。 HyVLA-0.5 基于自研的亚毫米级高精度指套式 UMI 数据采集软硬件进行训练，构建了超过 10000 条演示数据集。腾讯还开源了 Hy-Embodied-VLM-1.0 和 Hy-Embodied-RxBrain-1.0，支持端侧高效部署。

rss · AI Hot · Jul 19, 00:16

**背景**: 具身智能是指集成到物理机器人中的 AI 系统，能够感知、推理并与真实世界交互。开放权重模型是指核心参数公开发布的 AI 模型，任何人都可以下载并在自己的基础设施上运行，而闭源模型则只能通过 API 访问。视觉-语言-动作（VLA）模型如 HyVLA 将视觉理解、语言理解和动作生成整合到一个端到端架构中，使机器人能够执行复杂的操作任务。SWE-bench 基准测试已成为评估 AI 编码能力的关键指标，顶级开放权重模型如 DeepSeek V4 Pro 目前已能匹敌前沿闭源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.agentren.cn/2026/0716/20649.shtml">腾讯发布两大具身智能基座模型，VLM与RxBrain提升机器人对现实世界的理解能力</a></li>
<li><a href="https://m.aitntnews.com/newDetail.html?newId=26211">腾讯Robotics X开源HyVLA-0.5：基于亚毫米级指套UMI与真机强化，摆脱繁重遥操</a></li>
<li><a href="https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/">The Open Weight Models that Matter: June 2026 — OpenRouter Blog</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Open-Source AI`, `#Robotics`, `#LLM Security`, `#Tencent`

---

<a id="item-8"></a>
## [开放权重模型逼近前沿，部署治理成新焦点](https://aihot.virxact.com/items/cmrr2vrf701pgbi18nhdbtxed) ⭐️ 8.0/10

Mozilla 的一份报告指出，开放权重 AI 模型在编码等任务上已逼近顶尖闭源模型的性能，但在生产环境中的采用仍存在差距。行业竞争焦点正从模型权重本身转向部署基础设施、Agent harness 能力、权限管理和合规性。 这标志着一个重大的范式转变：AI 竞争的主战场正从基础模型质量转向周边软件生态系统和治理框架。组织现在必须全面评估开放权重模型——综合考虑算力效率、运维成本和数据主权——而不是简单比较单次推理的 token 成本。 报告强调，决策者应首先明确自身对数据主权和供应商独立性的硬约束，然后再评估组织的维护能力。Agent harness——即围绕模型管理工具调用、记忆和执行环境的软件脚手架——已成为关键差异化因素，因为它使模型能够执行多步骤、面向工具的任务。

rss · AI Hot · Jul 19, 00:16

**背景**: 开放权重 AI 模型允许用户下载模型权重——即训练过程中学到的关键数值——在自己的基础设施上运行和定制，但它们并非完全开源。Agent harness 是围绕大语言模型的软件基础设施，通过管理工具、记忆、状态持久化和反馈循环，将模型转变为 AI Agent。AI 领域的数据主权指在 AI 部署的任何地方对数据、模型和决策保持完全控制权，这正日益推动本地部署和开放权重模型的采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models : Open Source vs Open Weights vs...</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>
<li><a href="https://www.forbes.com/councils/forbesbusinesscouncil/2026/07/15/the-sovereign-ai-mirage-why-data-not-infrastructure-is-the-pathway-to-control/">The Sovereign AI Mirage: Why Data Is The Pathway To Control</a></li>

</ul>
</details>

**标签**: `#Open-Weight Models`, `#AI Governance`, `#AI Agents`, `#AI Deployment`, `#Industry Analysis`

---

<a id="item-9"></a>
## [英伟达 CEO 黄仁勋东京行：敲定国家级 AI 工厂合作，送粉丝红豆糕](https://aihot.virxact.com/items/cmrr2piau01n2bi1811473opw) ⭐️ 8.0/10

Nvidia CEO Jensen Huang announced a partnership with Japan's Noetra to build a 25,000-GPU 'AI factory' for the robotics industry, while also meeting with local tech leaders.

rss · AI Hot · Jul 18, 23:53

**标签**: `#Nvidia`, `#AI Infrastructure`, `#Robotics`, `#Jensen Huang`, `#Japan`

---

<a id="item-10"></a>
## [Anthropic 将 Claude Fable 5 推送至 Max 和 Team Premium 订阅用户](https://aihot.virxact.com/items/cmrr0kbwf0124bi18p52upzrx) ⭐️ 8.0/10

Anthropic 宣布从 7 月 20 日起，将 Claude Fable 5 模型提供给 Max 和 Team Premium 订阅用户，使用限额为 50%。Pro 和 Team Standard 用户可通过用量积分调用该模型，官方为此赠送了 100 美元的积分。 此次推送使 Anthropic 迄今为止最强大的公开模型能够被更广泛的付费用户使用，加剧了高端 AI 订阅市场的竞争。分阶段推广和积分补偿策略反映了前沿模型给提供商带来的巨大计算需求压力。 Claude Fable 5 被描述为已确保可安全用于通用场景的 Mythos 级模型，其能力超越了 Anthropic 此前公开发布的任何模型。由于需求旺盛，推广采取分阶段进行，部分用户指出 Kimi K3 等竞品可能同样具有吸引力。

rss · AI Hot · Jul 18, 23:28

**背景**: Claude Fable 5 是 Anthropic 开发的 Mythos 系列大语言模型的一部分，该系列起源于 Claude Mythos Preview。最初的 Mythos Preview 模型由于在寻找软件漏洞方面能力过于强大而未向公众发布，这促使 Anthropic 开发了安全可公开的 Fable 5 版本。该模型专为自主知识工作和编程而构建，支持文本、图像和文件输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5">Claude Fable 5 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 用户对此次推送的评价呈现两极分化，部分用户对使用限制和分阶段访问表示不满。社区中一个值得注意的反面观点是，竞品模型 Kimi K3 可能更具吸引力，这凸显了当前 AI 领域的激烈竞争。

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#AI Models`, `#AI Industry News`

---

<a id="item-11"></a>
## [腾讯在 WAIC 2026 发布具身智能全栈方案及 ADP 4.0 海外版](https://36kr.com/newsflashes/3900908700436103?f=rss) ⭐️ 8.0/10

在 2026 世界人工智能大会（WAIC）上，腾讯升级发布了贯穿云底座、模型层、平台层与应用层的具身智能全栈方案。同时，腾讯云企业级智能体开发平台 ADP 4.0 海外版正式上线，面向个人用户的 WorkBuddy 也作为独立 App 发布，覆盖 iOS、Android 和鸿蒙三大平台。 此次发布标志着腾讯大举进军具身智能机器人和全球企业级 AI 智能体市场，其端到端解决方案有望大幅缩短机器人制造商和企业的开发周期。消费级工具与企业级平台的同步推出，使腾讯在整个 AI 智能体生态中成为全方位的竞争者。 腾讯的具身智能方案包含多款基座模型，并推出了业内首个云端 EaaS（Embodied-AI-as-a-Service，具身智能即服务）服务。ADP 4.0 平台已落地 30 多个行业，覆盖智能客服、知识管理、媒体生产等场景，并同步推出了「十大行业百大场景生态计划」。

rss · 36kr · Jul 18, 09:30

**背景**: 具身智能是指将人工智能系统与物理实体（如机器人）相结合，使其能够感知、理解并与真实世界进行交互。全栈方案意味着覆盖从云计算基础设施、基座模型到开发平台和终端应用的各个层面。像 ADP 这样的企业级智能体开发平台，允许企业构建结合大语言模型、搜索增强、工作流和多智能体协同的定制化智能助手。WorkBuddy 是腾讯推出的跨平台通用智能体应用，面向个人效率场景，能够自主规划并执行复杂的多模态任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jiemian.com/article/14788666.html">闪电快讯｜腾讯升级发布 具 身 智 能 全 栈 方 案 ，WorkBuddy推出App...</a></li>
<li><a href="https://www.yangtse.com/news/ch/202607/t20260718_373627.html">聚焦WAIC｜腾讯升级发布 具 身 智 能 全 栈 方 案 ，ADP 4.0海外版正式上线</a></li>
<li><a href="https://news.mydrivers.com/1/1137/1137365.htm">腾 讯 升 级 发 布具身 智 能 全栈方案 ADP 4.0海外版正式上线｜2026 WAIC</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#AI Agents`, `#Tencent`, `#Robotics`, `#Enterprise AI`

---

<a id="item-12"></a>
## [月之暗面有望最快六个月内赴港上市](https://36kr.com/newsflashes/3900806713951873?f=rss) ⭐️ 8.0/10

中国 AI 初创公司月之暗面已通知投资者调整公司架构并筹备赴港 IPO，有望最快在六个月内完成上市。此前，该公司于 7 月 16 日发布了全球参数规模最大的开源模型 Kimi K3，拥有 2.8 万亿参数，据称在 Code Arena 基准测试中超越了 Claude 和 GPT 等模型。 月之暗面的 IPO 将标志着中国头部 AI 初创公司中最早的一批公开上市之一，有望为国内 AI 行业设定估值基准。同时发布前沿级别的开源模型，表明该公司向公开市场投资者展示技术竞争力的战略意图。 Kimi K3 拥有 2.8 万亿参数，是全球最大的开源模型，支持视觉理解并具备 100 万 token 的上下文窗口。完整模型权重计划于 7 月 27 日前公开发布，该公司声称其性能已逼近海外顶级闭源模型。

rss · 36kr · Jul 18, 07:45

**背景**: 月之暗面是一家知名的中国 AI 初创公司，以其 Kimi AI 助手而闻名，该助手因支持超长上下文文本处理在中国市场获得了大量用户。该公司是众多资金雄厚的中国 AI 企业之一，致力于构建前沿大语言模型。Code Arena 是一个 AI 编程模型评测平台，通过对代码质量、推理能力和准确性进行盲测对比来评估不同模型。IPO（首次公开募股）是私人公司首次向公众发行股票的过程，从机构和散户投资者处筹集资金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinastarmarket.cn/detail/2429127">月 之 暗 面 Kimi K 3 上线！ 系全球最大规 模 开 源 模 型 支持视觉理解、100...</a></li>
<li><a href="https://inews.hket.com/article/4162481/【Kimi+K3】月之暗面推Kimi+K3、2.8萬億參數全球最大開源模型　性能逼近海外頂級閉源模型">【 Kimi K 3 】 月 之 暗 面 推 Kimi ... | 香港經濟日報HKET</a></li>
<li><a href="https://lmarena.ai/?chat-modality=code">Code Arena - Compare AI Coding Models</a></li>

</ul>
</details>

**标签**: `#Moonshot AI`, `#Kimi`, `#IPO`, `#Open Source Models`, `#AI Industry`

---

<a id="item-13"></a>
## [安谋科技发起“开源 AIOS 联盟”，联合国内主要芯片厂商](https://www.ithome.com/0/978/628.htm) ⭐️ 8.0/10

安谋科技在 2026 世界人工智能大会期间宣布发起“开源 AIOS 联盟”，目前已吸引超 20 家生态伙伴入驻。联盟成员涵盖瑞芯微、紫光展锐、全志科技等国内领先芯片厂商，以及面壁智能、RT-Thread、AutoCore 等模型及软硬件方案提供商和清华大学等顶尖高校。 这一举措代表了中国在边缘 AI 硬件、大语言模型和具身智能交叉领域的重要生态建设。通过联合芯片厂商、软件提供商和学术机构，该联盟旨在构建统一的 AI 操作系统，有望重塑新一代 AI 产品的发展，特别是在机器人和智能设备领域。 开源 AIOS 系统聚焦四大技术模块：AI 模型能力、传感与运控、AI 任务编排和记忆系统。联盟覆盖了从芯片与 IP、大模型、AI 硬件、具身本体到软件方案的国内 AI 产学研全链路。

rss · IT HOME · Jul 19, 01:19

**背景**: AIOS（AI 操作系统）是一个新兴概念，将大语言模型嵌入操作系统中，以促进 AI 智能体的开发和部署，提供内存管理、调度和工具使用等基础设施。联盟合作伙伴之一的 RT-Thread 是一款流行的开源实时操作系统（RTOS），专为物联网和嵌入式设备设计，最初于 2006 年创建。另一合作伙伴 AutoCore 则专注于自动驾驶和智能移动计算平台的中间件和软件栈开发。该联盟旨在满足专门处理边缘设备上 AI 工作负载的操作系统日益增长的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agiresearch/AIOS">GitHub - agiresearch/ AIOS : AIOS : AI Agent Operating System · GitHub</a></li>
<li><a href="https://osrtos.com/rtos/rt-thread/">RT - Thread - Open Source RTOS</a></li>
<li><a href="https://autocore.ai/en/acos">AutoCore - Leader in Intelligent Mobile Computing Platform Products...</a></li>

</ul>
</details>

**标签**: `#AIOS`, `#Edge AI`, `#Arm China`, `#Embodied AI`, `#AI Hardware`

---

<a id="item-14"></a>
## [SpaceX 与五角大楼谈判提供 AI 算力，交易或达数十亿美元](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX 正与美国国防部进行谈判，拟向五角大楼提供用于运行人工智能模型的数据中心算力，交易金额可能高达数十亿美元。知情人士透露谈判仍在进行中，存在破裂的可能性，但若达成协议，将是 SpaceX 与五角大楼深化关系的又一重大交易。 这笔交易标志着 SpaceX 正成为 AI 基础设施生态系统中的一位重要新参与者，从其核心航空航天业务扩展到高需求的云计算市场。若达成协议，将大幅提升五角大楼在国家安全和军事行动中的 AI 能力，同时使 SpaceX 与亚马逊、谷歌、微软和甲骨文等成熟云服务商在国防计算领域并驾齐驱。 五角大楼近期已批准 SpaceX 以及亚马逊、谷歌、微软和甲骨文等公司在机密政府环境中运行 AI 模型及相关技术。SpaceX 近月还与 AI 公司 Anthropic 和谷歌签署了类似的算力供应协议，并计划大幅扩展其云计算业务。

telegram · @zaihuapd · Jul 18, 01:44

**背景**: 美国国防部一直在加速推进人工智能的采用，涵盖情报分析、后勤保障、自主系统和战场决策等领域。确保拥有足够的计算基础设施来训练和运行大规模 AI 模型已成为国家安全的战略优先事项。SpaceX 以其火箭发射和卫星互联网（Starlink）业务闻名，但一直在向数据中心和云计算服务领域多元化发展，利用其在大规模工程和基础设施部署方面的专业能力。

**标签**: `#AI Infrastructure`, `#SpaceX`, `#National Security`, `#Cloud Computing`, `#Frontier Tech`

---

<a id="item-15"></a>
## [OpenRouter 被传收到收购意向，估值或超 13 亿美元](https://www.theinformation.com/articles/startup-openrouter-fields-multi-billion-dollar-takeover-interest) ⭐️ 8.0/10

AI 模型路由平台 OpenRouter 已被多家大型科技公司接洽，表达潜在收购意向，估值可能超过其 2024 年 5 月 B 轮融资后约 13 亿美元的投后估值。该公司在该轮融资中筹集了 1.13 亿美元，由 Alphabet 旗下 CapitalG 领投，估值较 2023 年 6 月 A 轮的 5.47 亿美元翻了一倍多。 OpenRouter 已成为 AI 生态系统中的关键中间件层，为约 800 万用户提供超过 400 个模型的路由服务，每月处理约 100 万亿 token，使其成为极具战略价值的收购目标。大型科技公司在此估值水平上表达收购意向，表明 AI 基础设施和路由层正成为各公司争夺 LLM 分发管道控制权的关键战场。 OpenRouter 平台目前服务约 800 万用户，路由超过 400 个模型，每月处理约 100 万亿 token，截至 2026 年初年化收入约达 5000 万美元。该公司的统一 API 允许开发者通过单一接口访问来自 OpenAI、Google、Anthropic 等厂商的模型，并根据任务类型、成本和性能需求智能动态地选择最佳模型。

telegram · @zaihuapd · Jul 18, 03:45

**背景**: LLM 路由是一种中间件概念，类似于 AI 查询的空中交通管制员，根据任务复杂度、成本限制和延迟要求等因素，动态地将每个请求引导至最合适的模型。这种方式使开发者能够避免供应商锁定，通过将简单查询发送给更便宜的模型、将昂贵模型留给复杂任务来优化成本，并在新模型发布时保持单一集成点。OpenRouter 已将自身定位为该领域的领先独立平台，提供与 OpenAI SDK 兼容的统一 API，可访问来自不同供应商的数百个模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">The unified interface for LLMs. Find the best models & prices for your...</a></li>
<li><a href="https://medium.com/@kosiashara/llm-routing-smarter-faster-and-cheaper-ai-c95f716506e5">LLM Routing : Smarter, Faster, and Cheaper AI | by Kosi... | Medium</a></li>
<li><a href="https://blog.n8n.io/llm-routing/">LLM routing strategies for quality in AI applications – n8n Blog</a></li>

</ul>
</details>

**标签**: `#OpenRouter`, `#AI Infrastructure`, `#Acquisition`, `#LLM Routing`, `#AI Industry`

---

<a id="item-16"></a>
## [台积电宣布 A14（1.4nm）制程将于 2028 年投产](https://t.me/zaihuapd/42643) ⭐️ 8.0/10

台积电正式宣布其下一代 A14（1.4nm 级）制程技术计划于 2028 年量产，并最早于 2027 年开始风险生产。与即将推出的 N2 制程相比，A14 在相同功耗下速度提升高达 15%，在相同速度下功耗降低达 30%，同时逻辑密度提高 20%以上。 作为半导体制造的绝对前沿，A14 制程将直接决定下一代 AI 模型和超级计算机的未来算力、能效和扩展极限。台积电预计 A14 的产量将超过 2nm 制程，在 AI 芯片需求激增之际，进一步巩固其对英特尔和三星等竞争对手的技术领先地位。 A14 结合了台积电第二代 GAA（环绕栅极）纳米片晶体管和全新的标准单元架构，以实现性能和密度的提升。台积电还计划在 2026 年末推出介于 N2 和 A14 之间的 A16 制程作为过渡，据报道 A14 目前未面临任何开发障碍。

telegram · @zaihuapd · Jul 18, 05:00

**背景**: N2 和 A14 等制程节点指的是半导体制造技术的代际，纳米级数字越小通常意味着晶体管密度越高、功耗越低。台积电目前的最先进制程是 N3（3nm），N2（2nm）计划于今年晚些时候量产，标志着该公司向 GAA 晶体管架构的过渡。A14 制程代表 1.4nm 级别，将利用 DTCO（设计技术协同优化）技术进行光学微缩，并为未来向 A13 和 A12 等更先进制程的平稳迁移奠定基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers">TSMC confirms significant yield and performance improvements in A 14 ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/tsmc-projects-mass-production-of-advanced-a14-chips-by-2028/articleshow/132460002.cms">TSMC projects mass production of advanced A 14 chips by 2028 - The...</a></li>
<li><a href="https://wccftech.com/tsmc-1-4nm-process-faces-no-obstacles-as-risk-production-to-start-in-2027/">TSMC ’s Facing No Development Obstacles With Its Next-Generation...</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#Semiconductors`, `#AI Infrastructure`, `#Chips`, `#Advanced Manufacturing`

---

<a id="item-17"></a>
## [特朗普政府拟设类似 FINRA 的独立机构审查顶尖 AI 模型](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 8.0/10

特朗普政府正考虑设立一个独立的、由行业资助的 AI 监管机构，参照金融业监管局（FINRA）的模式来审查顶尖人工智能模型的安全性。该提案由财政部长斯科特·贝森特牵头制定，目前正由白宫幕僚长苏茜·威尔斯审阅，拟创建一个向证券交易委员会（SEC）汇报的机构，让华尔街和硅谷在联合制定安全标准方面拥有更大发言权。 这代表美国 AI 治理的重大潜在转变，从临时性政府干预转向针对前沿 AI 模型的结构化行业共同监管框架。OpenAI、Anthropic 和 Google DeepMind 等顶尖 AI 实验室将直接受到影响，因为新机构可能取代令硅谷不满的临时管控措施，同时回应华尔街对网络安全的担忧。 该提案尚未经总统特朗普审阅，相关框架仍在讨论中，具体内容可能会有重大调整。这一方向与 Google DeepMind 首席执行官德米斯·哈萨比斯本周提出的设立行业资助独立监管机构的建议一致，而此前 Anthropic 和 OpenAI 均曾对美国政府要求修改或限制发布最新模型提出异议。

telegram · @zaihuapd · Jul 18, 05:45

**背景**: FINRA（金融业监管局）是美国政府授权的自律监管组织，负责监管经纪公司和交易市场，由其监管的行业而非纳税人提供资金。前沿 AI 模型是指由顶尖实验室开发的最先进、最强大的人工智能系统，其潜在风险正日益受到各国政府的关注和管控。该提案拟将金融业的共同监管模式应用于 AI 行业，由企业协助资助并参与制定约束其自身最强大模型的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yicai.com/brief/103280864.html">报道：美国考虑设立类似 FINRA 的 监 管 机构，来审查顶尖AI模型</a></li>
<li><a href="https://brokercheck.finra.org/">brokercheck. finra .org</a></li>

</ul>
</details>

**标签**: `#AI Regulation`, `#AI Policy`, `#Frontier Models`, `#Governance`, `#OpenAI`

---

<a id="item-18"></a>
## [SK 海力士 CEO 预警：2027 年将迎史上最严重内存短缺](https://t.me/zaihuapd/42645) ⭐️ 8.0/10

SK 海力士 CEO 郭鲁正警告称，尽管积极扩产，全球内存行业仍将在 2027 年面临史上最严重的供应短缺，客户需求预计在 2030 年后仍将超过供应能力。此番警告发出当天，SK 海力士在纳斯达克首日上市，股价收涨 13.3%报 168.85 美元，2025 年营业利润达到创纪录的 47 万亿韩元（约 310 亿美元）。 作为全球领先的 HBM（高带宽内存）制造商——这种内存对 AI 加速器至关重要——SK 海力士的预警表明 AI 硬件供应链面临仅靠积极扩产无法解决的根本性瓶颈。即将到来的短缺可能制约全球 AI 算力基础设施的扩张，从前沿模型训练到数据中心建设都将受到影响，这一局面可能持续到本十年末。 郭鲁正透露，公司正在评估美国、日本及东南亚作为海外晶圆厂候选地，将优先选择土地、电力与人力成本最具优势的地区。SK 海力士 2025 年第二季度营业利润预计将进一步增至 65.5 万亿韩元，此次纳斯达克上市筹集了约 40 万亿韩元，用于龙仁和清州晶圆厂的扩建。

telegram · @zaihuapd · Jul 18, 06:30

**背景**: 高带宽内存（HBM）是一种采用硅通孔（TSV）技术的 3D 堆叠 DRAM，每堆叠可提供超过 1 TB/s 的极高带宽，使其成为 AI 加速器和高性能计算不可或缺的组件。SK 海力士是 HBM 的主导供应商，随着 NVIDIA 等公司对 GPU 内存的需求激增，HBM 已成为 AI 硬件供应链中的关键瓶颈。与可以相对快速扩产的常规内存不同，HBM 的生产需要复杂的制造工艺以及与先进逻辑芯片的紧密集成，这限制了供应端响应 AI 需求激增的速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://logicity.in/en/blog/ai-memory-shortage-could-last-until-2027-samsung-and-sk-hynix-warn">AI Memory Shortage Could Last Until 2027, Samsung and... | Logicity</a></li>
<li><a href="https://www.linkedin.com/pulse/week7-insatiable-demand-high-bandwidth-memory-ai-mayank-varshney-vodtc">Week#7 : Insatiable Demand for High Bandwidth Memory by AI</a></li>
<li><a href="https://en.sedaily.com/finance/2026/07/10/sk-hynix-debuts-on-nasdaq-with-record-foreign-ipo-targets">SK hynix Debuts on Nasdaq with Record Foreign IPO, Targets Yongin...</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Memory Shortage`, `#SK Hynix`, `#AI Infrastructure`, `#Semiconductors`

---

<a id="item-19"></a>
## [商汤发布 SenseNova U1 Pro 多模态智能体基座](https://mp.weixin.qq.com/s/hGo5TvUpxRodVtfnXDM7ew) ⭐️ 8.0/10

7 月 18 日，商汤科技正式发布面向长程任务的交付级原生多模态智能体基座——日日新 SenseNova U1 Pro。该模型具备专业设计美感、原生 8K 超清输出、极致图文细节控制以及长程 Agentic 闭环思维四大核心交付能力，可广泛用于商业创作场景。 此次发布标志着原生多模态智能体的重要升级，专门针对长程 Agentic 任务和高分辨率商业图像与视频生成。这使商汤在快速演进的多模态 AI 领域中占据了有利竞争位置，而该领域中理解与生成的统一正成为实际应用的关键。 U1 Pro 在过去两个月内进行了三次快速迭代，截至今年 6 月 U1 用户人均日生图量达到 107 张，GitHub Star 合计超过 8500。在发布现场，商汤展示了由 U1 Pro 生成的 WAIC 九周年水墨长卷及《沙影之刃》视频分镜，呈现了从图像到视频创作前端的系统级交付能力。

telegram · @zaihuapd · Jul 19, 01:20

**背景**: 长程 Agentic 任务是指需要 AI 智能体在较长时间内保持上下文并做出决策的复杂多步骤工作流程，代表了从简单的提示-响应交互向自主任务完成的转变。原生多模态模型在单一架构内整合了理解和生成能力，而非依赖不同模态的独立专用模型。业界正逐渐形成共识，即统一多模态理解与生成是迈向更通用 AI 系统的关键路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qbitai.com/2025/05/281590.html">多 模 态 =AGI...</a></li>
<li><a href="https://www.qimingvc.com/cn/news/启明星-智谱glm-5开源：从代码到工程，agentic-engineering时代最好的开源模型">启明星 | 智谱GLM-5开源：从代码到工 程 ， Agentic Engineering...</a></li>

</ul>
</details>

**标签**: `#Multimodal AI`, `#AI Agents`, `#SenseTime`, `#Generative AI`, `#Computer Vision`

---