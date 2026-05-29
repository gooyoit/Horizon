---
layout: default
title: "Horizon Summary: 2026-05-29 (ZH)"
date: 2026-05-29
lang: zh
---

> From 112 items, 11 important content pieces were selected

---

1. [Claude Opus 4.8](#item-1) ⭐️ 9.0/10
2. [Anthropic raises $65B in Series H funding at $965B post-money valuation](#item-2) ⭐️ 9.0/10
3. [LeCun 团队数学证明 LeJEPA 何时能学习真实世界模型](#item-3) ⭐️ 9.0/10
4. [llm-anthropic 0.25.1 新增 Claude Opus 4.8 支持](#item-4) ⭐️ 8.0/10
5. [Claude Opus 4.8 自主撰写经济学论文并进行方法论自评](#item-5) ⭐️ 8.0/10
6. [阶跃星辰开源 Step 3.7 Flash 模型，生成速度达每秒 400 Tokens](#item-6) ⭐️ 8.0/10
7. [华为全面升级星河 AI 网络，Token 生产效率提升 2 至 5 倍](#item-7) ⭐️ 8.0/10
8. [高通与字节跳动达成 AI ASIC 芯片合作](#item-8) ⭐️ 8.0/10
9. [英伟达计划每年在台湾投入 1500 亿美元建设 AI 生态](#item-9) ⭐️ 8.0/10
10. [中国将为人形机器人分配数字 ID](#item-10) ⭐️ 8.0/10
11. [比亚迪发布 4nm 智驾芯片“璇玑 A3”](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 9.0/10

Anthropic releases Claude Opus 4.8, a modest but tangible upgrade to the Opus 4.5 family, while also previewing 'Claude Mythos,' a new higher-intelligence model class currently being tested with select organizations for cybersecurity use cases.

hackernews · @zaihuapd · May 28, 16:49 · [社区讨论](https://news.ycombinator.com/item?id=48311647)

**标签**: `#anthropic`, `#claude-opus`, `#frontier-ai`, `#llm-release`, `#claude-mythos`

---

<a id="item-2"></a>
## [Anthropic raises $65B in Series H funding at $965B post-money valuation](https://www.anthropic.com/news/series-h) ⭐️ 9.0/10

Anthropic announces a $65 billion Series H funding round at a $965 billion valuation, backed by massive revenue growth that reportedly surpasses competitors like OpenAI.

hackernews · meetpateltech · May 28, 18:09 · [社区讨论](https://news.ycombinator.com/item?id=48313048)

**标签**: `#Anthropic`, `#AI Funding`, `#Frontier AI`, `#Industry`, `#Venture Capital`

---

<a id="item-3"></a>
## [LeCun 团队数学证明 LeJEPA 何时能学习真实世界模型](https://x.com/rohanpaul_ai/status/2060169541121151217) ⭐️ 9.0/10

Yann LeCun 团队的新论文通过数学证明，LeJEPA 模型只有在真实的隐藏变量呈现高斯云结构时，才能可靠地恢复这些变量。当隐藏变量是独立高斯变量，且配对视图由一个稳定的噪声过程生成时，LeJEPA 的最优解能够以旋转或翻转等价的形式恢复这些变量。 这项研究为自监督 AI 模型何时能真正理解世界的底层结构提供了理论基础，而不仅仅是提取在测试集上碰巧有效的特征。它推进了 LeCun 大力倡导的 JEPA 框架，该框架被认为是构建能够学习世界模型的 AI 系统的关键路径，也是迈向更通用 AI 的重要一步。 LeJEPA 引入了草图化各向同性高斯正则化（SIGReg），这是一种新颖的目标函数，能够将学习到的嵌入约束到最优的各向同性高斯分布，从而最小化下游预测风险。该论文由 Randall Balestriero 等人撰写，定位为一个精简、可扩展且理论扎实的自监督表示学习框架，无需依赖启发式方法。

rss · AI Hot · May 29, 01:21

**背景**: 联合嵌入预测架构（JEPA）是 Yann LeCun 倡导的一类自监督学习框架，它通过从上下文输入预测目标输入的表示来学习，而不是直接生成像素或词元。与重建原始数据的生成模型不同，JEPA 在学习的嵌入空间中运作，旨在捕获世界的底层结构和语义。I-JEPA 是其图像变体，通过从同一图像的其他块预测图像块的表示来学习，无需依赖手工设计的数据增强。LeCun 认为，JEPA 风格的架构对于构建能够学习世界模型并对物理世界进行推理的 AI 系统至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.08544">[2511.08544] LeJEPA: Provable and Scalable Self-Supervised Learning ...</a></li>
<li><a href="https://github.com/galilai-group/lejepa">GitHub - galilai-group/lejepa</a></li>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self - Supervised Learning from Images with...</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#World Models`, `#Self-Supervised Learning`, `#JEPA`, `#Yann LeCun`

---

<a id="item-4"></a>
## [llm-anthropic 0.25.1 新增 Claude Opus 4.8 支持](https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 llm-anthropic 插件的 0.25.1 版本，新增了对新发布的 Claude Opus 4.8 模型的支持、用于加速 token 生成的快速模式选项（`-o fast 1`），并将默认最大输出 token 数从固定的 8,192 改为各模型自身的最大值。 此次发布使使用这一流行开源 LLM CLI 工具的开发者能够通过简单的插件更新立即访问 Anthropic 最新的前沿模型 Claude Opus 4.8。快速模式的集成还允许组织在对延迟敏感的工作流中获得高达 2.5 倍的输出加速。 快速模式选项（`-o fast 1`）仅对已在 Anthropic 账户中启用该功能的组织可用，且采用更高的定价。移除 8,192 max_tokens 上限意味着用户不再需要为更长的输出手动覆盖默认值，因为每个模型现在默认使用其自身的最大输出能力。

rss · Simon Willison · May 28, 23:54

**背景**: llm-anthropic 是 Simon Willison 开发的 LLM CLI 工具的插件，该工具是一个开源命令行实用程序，允许开发者向各种大型语言模型 API 发送提示并将结果记录到 SQLite 数据库中。Claude Opus 4.8 是 Anthropic 在 Claude Opus 系列中最新发布的高能力模型。快速模式目前处于测试阶段，是一种优先考虑速度而非成本效率的 API 配置，在支持的 Opus 模型上可提供高达 2.5 倍的每秒输出 token 数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/fast-mode">Fast mode (beta: research preview) - Claude API Docs</a></li>
<li><a href="https://simonwillison.net/2023/May/18/cli-tools-for-llms/">llm , ttok and strip-tags— CLI tools for working with ChatGPT and other...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#LLM Tools`, `#Open Source`, `#Software Release`

---

<a id="item-5"></a>
## [Claude Opus 4.8 自主撰写经济学论文并进行方法论自评](https://x.com/emollick/status/2060168513176658003) ⭐️ 8.0/10

Claude Opus 4.8 在 Claude Code 中基于匿名数据自主撰写了一篇经济学研究论文，随后由 GPT-5.5 Pro 担任审稿人并指出了其中的错误。在回应审稿意见后，Claude 对论文的稳健性进行了量化自评，在 1-10 的因果识别度量表上给出 4.5 分，承认远未达到准实验标准（约 7 分），并将结论谨慎地定性为"条件关联一致"而非因果识别。 这一案例展示了前沿 AI 模型执行学术研究的完整闭环——撰写、同行评审和方法论自我批评，并展现出许多人类研究者都难以企及的认识论谦逊。这表明先进的 AI 智能体可能很快成为社会科学研究中的标准协作工具，在加速发表周期的同时，也引发了关于署名权、同行评审诚信以及人类学者未来角色的深刻问题。 Claude 的自评分数在稳健性检验后从 3.5 提升至 4.5（满分 10 分），但它正确地认识到这仍远低于经济学中可信因果推断所需的准实验门槛（约 7 分）。论文最终采用了谨慎的表述——"条件关联一致"——展示了模型将结论主张与方法论严谨程度相匹配的能力，这是实证经济学中一项重要的学术规范。

rss · AI Hot · May 29, 01:17

**背景**: 在实证经济学中，因果识别是确立变量间因果关系（而非仅仅是相关性）的黄金标准。准实验设计——如双重差分法、断点回归和工具变量——是在无法实现真正随机化时近似随机实验的方法，被认为是发表于顶级经济学期刊的必要条件。稳健性检验是检验研究结果在替代设定下是否依然成立的补充性分析，是衡量研究可信度的关键指标。Claude Code 是 Anthropic 推出的智能编程工具，能够理解代码库、编辑文件并自主运行命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI Agents`, `#Scientific Research`, `#Automated Peer Review`, `#Frontier AI`

---

<a id="item-6"></a>
## [阶跃星辰开源 Step 3.7 Flash 模型，生成速度达每秒 400 Tokens](https://www.ithome.com/0/956/860.htm) ⭐️ 8.0/10

中国 AI 初创公司阶跃星辰（StepFun）发布了开源的 Step 3.7 Flash 模型，最高生成速度可达每秒 400 Tokens。该模型是一个拥有 1980 亿参数的混合专家（MoE）视觉语言模型，支持原生图像和视频输入，上下文窗口达 256K。 此次发布显著提升了开源多模态 AI 模型的标杆，将前沿推理能力与卓越的推理速度相结合，可媲美甚至超越许多闭源替代方案。它增强了开源大模型生态系统，为开发者提供了一个强大且企业级的复杂智能体和多模态工作流工具。 Step 3.7 Flash 基于稀疏混合专家（MoE）架构构建，针对结合感知、搜索和多步推理的企业级工作流进行了优化。其前代 Step 3.5 Flash 已在 SWE-bench Verified 上取得 74.4% 的成绩，在 Terminal-Bench 2.0 上达到 51.0%，表明这一更新版本在编程和智能体能力方面表现强劲。

rss · AI Hot · May 29, 01:03

**背景**: 阶跃星辰（StepFun）是一家中国 AI 初创公司，开发了 Step 系列大语言模型，在各类 AI 应用场景中提供具有竞争力的实际部署表现。混合专家（MoE）是一种架构，每次输入仅激活模型参数的一个子集，从而在保持高效推理速度的同时支持更大的总参数量。视觉语言模型通过原生处理图像和视频与文本，扩展了传统的纯文本大模型能力，实现了多模态的理解与生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/run-step-3-7-flash-on-nvidia-gpus-with-enterprise-ready-multimodal-ai/">Run Step 3.7 Flash on NVIDIA GPUs with Enterprise-Ready Multimodal AI | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/stepfun-ai/Step-3.5-Flash">stepfun-ai/Step-3.5-Flash · Hugging Face</a></li>
<li><a href="https://github.com/stepfun-ai/Step-3.5-Flash">GitHub - stepfun-ai/Step-3.5-Flash: Fast, Sharp & Reliable Agentic Intelligence · GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#LLM`, `#StepFun`, `#Inference Speed`

---

<a id="item-7"></a>
## [华为全面升级星河 AI 网络，Token 生产效率提升 2 至 5 倍](https://www.ithome.com/0/956/878.htm) ⭐️ 8.0/10

Huawei has comprehensively upgraded its AI network solutions to significantly boost Token production efficiency by 2 to 5 times through NPU-storage integration, while also introducing advanced quantum-safe security measures to protect AI assets.

rss · IT HOME · May 29, 01:41

**标签**: `#AI Infrastructure`, `#Networking`, `#Huawei`, `#Data Center`, `#Quantum Security`

---

<a id="item-8"></a>
## [高通与字节跳动达成 AI ASIC 芯片合作](https://t.me/zaihuapd/41616) ⭐️ 8.0/10

高通已与字节跳动就 AI ASIC 芯片达成合作协议，字节跳动将采购数百万颗定制芯片，用于支持其 AI 服务算力需求。这笔合作还将帮助字节跳动把内部芯片设计转化为可量产的半导体产品。 这笔大规模订单标志着高通正式进军 AI 加速器市场，直接挑战英伟达等现有巨头在定制 AI 芯片领域的地位。对字节跳动而言，获得专属 ASIC 芯片供应有助于减少对受限英伟达 GPU 的依赖，并为其 AI Agent 等业务提供强大的算力支撑。 高通此前曾在 4 月底宣布将于今年向某超大规模云服务商交付首款 ASIC，此次与字节跳动的合作很可能就是该计划的一部分。目前高通代表拒绝置评，字节跳动发言人也未回应置评请求。

telegram · @zaihuapd · May 28, 07:09

**背景**: ASIC（专用集成电路）是一种为特定任务全定制的半导体芯片，相比通用型 GPU 在能效方面表现更优。虽然 GPU 因其对各种算法的灵活性仍在 AI 数据中心占据主导地位，但 ASIC 在大规模特定 AI 工作负载中能提供更优化的性能。谷歌（TPU）和亚马逊（Trainium/Inferentia）等大型科技公司越来越多地开发定制 ASIC，以降低成本并减少对第三方芯片供应商的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/955/674.htm">消息称高通与字节跳动达成 AI ASIC 芯片合作，采购量在数百万颗级别 - IT之家</a></li>
<li><a href="https://www.163.com/dy/article/KU0VCDE5051180F7.html">曝字节为高通首批AI ASIC芯片客户，百万颗订单，高通大涨8%|英伟达|台积电|智能手机|知名企业|高带宽内存_网易订阅</a></li>
<li><a href="https://36kr.com/p/3530164578147461">高通新发AI推理芯片，瞄准每年3000亿美元市场-36氪</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Hardware`, `#ByteDance`, `#Qualcomm`, `#ASIC`

---

<a id="item-9"></a>
## [英伟达计划每年在台湾投入 1500 亿美元建设 AI 生态](https://arstechnica.com/tech-policy/2026/05/nvidia-ceo-wants-taiwan-to-be-center-of-ai-revolution-not-us/) ⭐️ 8.0/10

英伟达 CEO 黄仁勋宣布台湾是 AI 革命的中心，并计划每年在台湾投入约 1500 亿美元，较此前每年 100 亿至 150 亿美元的规模大幅提升。相关投入将覆盖 AI 芯片生产、系统制造和供应链合作。 这一投资规模的十倍增长表明英伟达在全球 AI 硬件需求激增之际，正进一步深化对台湾制造生态的战略投入。此举进一步巩固了台湾在全球 AI 供应链中不可替代的地位，并可能显著加速全球 AI 基础设施的建设步伐。 英伟达在台北的新总部预计今年动工、2030 年启用，计划容纳 4000 名员工。核心制造合作伙伴包括台积电、鸿海、纬创和广达，这些企业仍是英伟达 AI 供应链的关键环节。

telegram · @zaihuapd · May 28, 07:33

**背景**: 台湾拥有全球最先进的半导体制造能力，其中台积电生产了英伟达绝大多数 AI GPU，包括 H100 和 Blackwell 架构芯片。鸿海、纬创和广达等企业在服务器和系统组装领域占据重要地位，构成了 AI 数据中心硬件生产的骨干。自 2022 年底 ChatGPT 问世以来，随着 AI 训练和推理计算需求激增，英伟达对台湾制造体系的依赖显著加深。

**标签**: `#Nvidia`, `#AI Infrastructure`, `#Taiwan`, `#TSMC`, `#AI Chips`

---

<a id="item-10"></a>
## [中国将为人形机器人分配数字 ID](https://www.scmp.com/tech/policy/article/3354747/china-give-every-humanoid-robot-digital-id-push-boost-industry-standards) ⭐️ 8.0/10

China is launching a national platform to assign unique digital IDs to AI-powered humanoid robots, enabling full lifecycle tracking from production to recycling to boost industry standards and risk monitoring.

telegram · @zaihuapd · May 28, 09:08

**标签**: `#humanoid robots`, `#embodied AI`, `#robotics regulation`, `#China tech policy`, `#digital ID`

---

<a id="item-11"></a>
## [比亚迪发布 4nm 智驾芯片“璇玑 A3”](https://finance.sina.com.cn/roll/2026-05-28/doc-inhznenn1371824.shtml) ⭐️ 8.0/10

5 月 28 日，比亚迪总裁王传福在“敢为”智能化战略发布会上正式发布了“璇玑 A3”4nm 智驾芯片，该芯片已开启规模化量产，三颗芯片总算力超过 2100 TOPS，支持 L3 和 L4 级别自动驾驶。 这标志着全球最大汽车制造商之一大举进军先进 AI 芯片设计领域，降低了对第三方芯片供应商的依赖，增强了比亚迪在竞争激烈的自动驾驶赛道上的垂直整合能力。 比亚迪称璇玑 A3 在同类产品中单位算力功耗最低，功耗比同类产品低约 20%，结合自研算法优化使算力利用率提升 100%。该公司已推出超过 2000 款芯片产品，并拥有 5 座晶圆工厂。

telegram · @zaihuapd · May 28, 13:01

**背景**: TOPS（每秒万亿次操作）是衡量 AI 芯片性能的标准指标，表示芯片每秒能处理多少万亿次神经网络推理运算。SAE 将自动驾驶分为从 L0（无自动化）到 L5（完全自动化）六个等级；L3 允许在特定条件下由车辆自动驾驶，但需要人类在必要时接管，而 L4 则可在限定运营域内实现高度自动化。4nm 制程是目前汽车芯片领域最先进的半导体制造工艺之一，能够实现更高的晶体管密度、更强的性能和更优的能效表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eletric-vehicles.com/byd/byd-unveils-first-in-house-4nm-autonomous-driving-chip/">BYD Unveils First In-House 4 nm Autonomous Driving Chip | EV</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/tops-in-computing/">What is TOPS in computing and How it Affects AI Performance | Lenovo US</a></li>
<li><a href="https://www.tomtom.com/newsroom/explainers-and-insights/different-levels-of-autonomous-driving/">What are the Different Autonomous Driving Levels ?</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#AI chips`, `#BYD`, `#L4 autonomy`, `#hardware`

---