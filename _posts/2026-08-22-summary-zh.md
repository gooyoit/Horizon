---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> From 116 items, 6 important content pieces were selected

---

1. [DeepSeek 为 v4 Flash 推出实验性视觉能力](#item-1) ⭐️ 8.0/10
2. [本周最佳论文：EnvHarness 与 SPADE](#item-2) ⭐️ 8.0/10
3. [Azure 接收首批生产级 NVIDIA Vera Rubin 系统](#item-3) ⭐️ 8.0/10
4. [Marin 启动 535B-A23B MoE 模型的全程开源训练](#item-4) ⭐️ 8.0/10
5. [Meta Muse Spark 1.2 贡献者版本上线 OpenRouter](#item-5) ⭐️ 8.0/10
6. [法庭文件披露 Anthropic “巴拿马计划”砍书扫描数百万册训练 Claude](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 为 v4 Flash 推出实验性视觉能力](https://api-docs.deepseek.com/guides/vision/) ⭐️ 8.0/10

DeepSeek 已在其 API 上线 deepseek-v4-flash-vision-exp，为 v4 Flash 模型系列增加多模态图像理解能力，并同步更新了官方文档和定价。图像会根据尺寸转换为 token，并与文本 token 一起计费。 DeepSeek 是领先的开源 AI 实验室，为其高性价比的 v4 Flash 系列添加视觉能力，让这一被广泛使用的低成本模型具备了多模态能力。这对于浏览器自动化等智能体工作流尤其重要，因为读取截图（此前相较 Claude Sonnet 是明显短板）是关键能力。 图像在推理前会被自动调整尺寸：低于约 384×384 像素的图像会被放大，更大的图像则被缩小至总像素数约等于 800×800——这对 OCR 或整页文档读取构成限制。社区测试结果好坏参半：它未能通过 Qwen3.8 27B 几乎答对的基础时钟读数测试，表明其视觉推理能力仍弱于截图解读能力。

hackernews · dares2573 · Aug 21, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=49386163)

**背景**: DeepSeek V4 Flash 是一个效率优化的混合专家（MoE）模型，总参数量 284B、激活参数 13B，支持 100 万 token 上下文窗口，在编程基准上表现顶尖，在推理和智能体任务上接近闭源领先模型。视觉语言模型（VLM）在文本模型基础上扩展了图像理解能力，通常通过视觉问答和视觉推理基准来评估。'exp' 实验性标签表明这是一个早期版本，能力可能尚不成熟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash 0423 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区态度谨慎乐观：用户欢迎其在 Playwright/浏览器自动化工作流中的截图读取能力，并指出之前的 0731 版本在无法真正看到图像时会虚构图像分析工具。担忧包括 800×800 缩放上限影响 OCR 和文档处理，另有用户报告该模型未能通过 Qwen3.8 27B 几乎答对的简单时钟读数测试。

**标签**: `#DeepSeek`, `#multimodal-AI`, `#vision-models`, `#open-source-AI`, `#model-release`

---

<a id="item-2"></a>
## [本周最佳论文：EnvHarness 与 SPADE](https://aihot.virxact.com/items/cmt3ljayq0veiro6tcgnxxbsw) ⭐️ 8.0/10

一份周度 AI 研究摘要（第 34 周）评选出两篇本周最佳 arXiv 论文：EnvHarness（arXiv:2608.19880），用于唤醒静态环境以进行智能体学习；以及 SPADE（arXiv:2608.19197），一个让单个 LLM 同时设计和求解自身可执行训练环境的自我博弈强化学习框架。 两篇论文都针对训练 LLM 智能体的核心瓶颈：缺乏丰富且自适应的训练环境。EnvHarness 与 SPADE 代表了互补的两条路线——增强现有静态环境与完全合成新环境——有望大幅扩展智能体训练的数据和信号规模。 EnvHarness 通过可堆叠的插件层（Stage、Contract、Chain）封装冻结的环境，把通常用在冻结 LLM 上的 harness 技巧应用到循环的另一侧。SPADE 则让单个 LLM 扮演两个角色——编写长程可执行 Python 训练环境的“环境设计者”，以及在环境中行动并提升的“推理智能体”。

rss · AI Hot · Aug 21, 23:11

**背景**: 用强化学习训练 LLM 智能体需要能提供有意义反馈的交互式环境，但大多数现有环境是静态的且很快会被“用尽”。自我博弈因 AlphaGo 等系统而广为人知，它让 AI 通过为自己生成挑战来提升，从而无需人工设计课程。近期研究将这一思路应用于 LLM：让模型以可执行代码的形式生成自己的训练任务或环境，从而获得几乎无限的自适应训练信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://envharness.com/">EnvHarness : Awakening Static Worlds for Agent Learning</a></li>
<li><a href="https://arxiv.org/abs/2608.19197">[2608.19197] SPADE: Self-Play in Adaptive Synthetic Executable Environments</a></li>
<li><a href="https://spade-rl.github.io/">SPADE: Self-Play in Adaptive Synthetic Executable Environments</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#self-play`, `#synthetic environments`, `#arXiv`, `#AI research`

---

<a id="item-3"></a>
## [Azure 接收首批生产级 NVIDIA Vera Rubin 系统](https://aihot.virxact.com/items/cmt3klouv0uojro6t0yx9vot5) ⭐️ 8.0/10

微软 Azure 已在其数据中心接收首批生产级 NVIDIA Vera Rubin 系统，CEO Satya Nadella 发文宣布了这一里程碑，并感谢 NVIDIA 合作伙伴及 Azure 硬件与数据中心团队。 Vera Rubin 是 NVIDIA 接替 Blackwell 的下一代 GPU 平台，AI 性能据称最高提升 4 倍，每兆瓦性能也大幅改善，Azure 率先部署生产级系统将让微软在前沿 AI 训练与推理算力上占据先机。 Rubin 平台将 Rubin GPU 与全新的 Vera CPU 及 HBM4 内存搭配；NVIDIA 的 DGX Rubin NVL8 配置可提供 400 petaFLOPS 的 NVFP4 性能和 176 TB/s 的 GPU 内存带宽。该消息来自 Nadella 的社交媒体帖子，篇幅简短且为二手来源，Azure 客户的具体部署规模和可用时间尚未公布。

rss · AI Hot · Aug 21, 23:00

**背景**: NVIDIA 以科学家命名其 GPU 架构；继 Hopper 和 Blackwell 之后，Vera Rubin（以天文学家薇拉·鲁宾命名）是下一代架构，其中 'Vera' 同时指与 Rubin GPU 搭配的 NVIDIA 新一代 Arm 架构服务器 CPU。Rubin 面向 '智能体 AI' 时代，号称每兆瓦的智能体性能最高提升 10 倍，并采用带宽大幅提升的 HBM4 内存。Azure 等云厂商围绕 NVIDIA 平台定制服务器机架，由于前沿 AI 模型训练受算力制约，各厂商竞相率先部署新一代 GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-rubin-nvl8/">Infrastructure for Agentic AI at Scale | NVIDIA DGX Rubin NVL8</a></li>
<li><a href="https://codelucky.com/nvidia-rubin-gpu-architecture-explained/">NVIDIA Rubin GPU Architecture : 4x Faster AI Than... - CodeLucky</a></li>
<li><a href="https://www.civo.com/blog/nvidia-r100-vs-nvidia-b200-gpu">NVIDIA Vera Rubin vs . NVIDIA Blackwell (B200) GPU | Civo</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#NVIDIA`, `#Azure`, `#Vera Rubin`, `#datacenter`

---

<a id="item-4"></a>
## [Marin 启动 535B-A23B MoE 模型的全程开源训练](https://aihot.virxact.com/items/cmt3jqms70u34ro6t6wrq3ek9) ⭐️ 8.0/10

Marin 团队已在 11 台 GB200 NVL72 机器上启动训练一个总参数量 535B、激活参数量 23B 的混合专家（MoE）模型，计划用约 3 个月时间在 18.75T tokens 上训练（约 2.7e24 FLOPs）。整个训练过程完全开源，其中预训练占 80% 算力，中期训练占 20%，之后还将进行后训练。 这是迄今规模最大的完全透明的前沿级训练之一，实时公开代码、数据、实验乃至失误。它让研究社区前所未有地深入了解一个现代大型 MoE 模型从缩放定律验证到最终后训练的完整构建过程。 在主训练之前，团队已通过从 1.6B-A61M 到 27.7B-A1.2B 的四级缩放阶梯验证并预测了主运行的表现。GB200 NVL72 是机架级系统，配备 72 块 Blackwell GPU 和 36 颗 Grace CPU，通过 NVLink 互连，专为万亿参数级模型训练设计。

rss · AI Hot · Aug 21, 22:42

**背景**: 混合专家（MoE）是一种使用多个专门化子模型（“专家”）的架构，每个 token 只激活其中一部分，从而在总参数量很大的同时大幅降低每次推理的计算量。Marin 是一个从零构建基础模型的开放研究社区与软件平台，以程序化、实时的方式记录数据整理、预训练、后训练和评估的每一个步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/marin-community/marin">GitHub - marin-community/marin: Open-source framework for the ...</a></li>
<li><a href="https://marin.community/">Marin</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL72 | NVIDIA</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#LLM training`, `#MoE`, `#scaling laws`, `#compute infrastructure`

---

<a id="item-5"></a>
## [Meta Muse Spark 1.2 贡献者版本上线 OpenRouter](https://aihot.virxact.com/items/cmt3jj4fm0tz7ro6t75i27ppa) ⭐️ 8.0/10

Meta 的 Muse Spark 1.2 贡献者（contributor）版本现已上线 OpenRouter，输入价格为每百万 token $0.10，输出为每百万 token $0.20。该版本以低于 GPT-5.6 Luna 的价格提供 GPT-5.6 Terra 级别的性能。 这一激进定价加剧了 Meta 与 OpenAI 之间在前沿模型上的价格战，让开发者能通过 OpenRouter 的统一 API 以更低成本获得接近前沿的性能。这也表明在 Muse Spark 1.2 将 Meta 拉回前沿竞争区间后，Meta 正持续发力高端市场。 贡献者版本有一个重要的隐私注意事项：提示词和输出可能被 Meta 用于改进其产品，因此不适合敏感业务场景。作为参考，OpenAI 的 GPT-5.6 系列分为三档：Sol（旗舰）、Terra（性能与成本平衡，价格减半）和 Luna（主打速度与低成本，价格约为 GPT-5.5 的 20%）。

rss · AI Hot · Aug 21, 22:37

**背景**: OpenRouter 是一个统一 API 网关，开发者可以通过单一接口访问多家供应商的 AI 模型，通常价格更有竞争力且可用性更高。Meta 于 2026 年 8 月发布 Muse Spark 1.2，重新回到前沿 AI 模型供应商行列，并已开源 Muse Glimmer 等相关模型权重。OpenAI 的 GPT-5.6 系列按 Sol、Terra、Luna 三档发布，确立了性价比基准，而 Meta 此次定价正是针对这一格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ghostcms.tenten.co/learning/muse-spark-1-2-agent-system/">Muse Spark 1 . 2 讓 Meta 重回前沿 | Tenten AI</a></li>
<li><a href="https://blog.wentuo.ai/gpt-5-6-sol-terra-luna-comparison-guide.html">解读GPT-5.6三大版本：Sol、Terra、Luna怎么选最划算</a></li>
<li><a href="https://aihot.virxact.com/story/d809047a-1c8d-416e-90fd-82e8f058ef05">Meta 将发布 Muse Spark 1 . 2 权重 · AIHOT</a></li>

</ul>
</details>

**标签**: `#Meta`, `#AI模型`, `#OpenRouter`, `#模型发布`, `#API定价`

---

<a id="item-6"></a>
## [法庭文件披露 Anthropic “巴拿马计划”砍书扫描数百万册训练 Claude](https://t.me/zaihuapd/43305) ⭐️ 8.0/10

《华盛顿邮报》报道的解密法庭文件显示，Anthropic 于 2024 年启动内部“巴拿马计划”，投入数千万美元批量购买并“破坏性扫描”（切掉书脊）数百万本实体书，为 Claude 构建训练数据。文件还证实其此前曾从 LibGen 等“影子图书馆”下载盗版书籍，并于 2026 年 7 月获联邦法官批准达成 15 亿美元的集体诉讼和解。 这是界定 AI 公司如何合法获取训练数据的标志性案件：法官认定扫描书籍用于训练可构成合理使用，但获取方式仍可能侵权。15 亿美元和解（每位作者每本书约 3000 美元）为整个行业的数据实践树立了重大先例。 内部文件显示 Anthropic 刻意强调“不想让外界知道”该扫描行动，且批量采购侧重于“较冷门”和高质量书籍。法官区分了合法购买后扫描的书籍（可能属合理使用）与从 LibGen 下载的盗版内容（构成侵权），后者成为和解的基础。

telegram · @zaihuapd · Aug 21, 04:52

**背景**: LibGen（Library Genesis）是一个提供学术文章和图书免费盗版访问的“影子图书馆”，曾被广泛用于收集 AI 训练数据。作者们就 Anthropic 使用盗版书籍训练 Claude 提起集体版权诉讼，Anthropic 于 2025 年同意支付 15 亿美元，旧金山联邦法官于 2026 年 7 月批准该和解。“破坏性扫描”指切掉书脊后将书页送入高速扫描仪，实体书被销毁但可获得高质量数字文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Panama">Project Panama - Wikipedia</a></li>
<li><a href="https://apnews.com/article/ai-anthropic-copyright-settlement-claude-books-bartz-74b140444023898aeba8579b6e9f0d63">Judge approves a $1.5B Anthropic settlement over pirated ...</a></li>
<li><a href="https://www.reuters.com/world/us-judge-approves-anthropics-15-billion-settlement-copyright-lawsuit-2026-07-20/">US judge approves Anthropic's $1.5 billion settlement of ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#training data`, `#copyright litigation`, `#AI governance`

---