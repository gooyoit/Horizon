---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> From 110 items, 13 important content pieces were selected

---

1. [OpenAI 联手 Broadcom 发布首款自研推理芯片 'Jalapeno'](#item-1) ⭐️ 9.0/10
2. [Computer use in Gemini 3.5 Flash](#item-2) ⭐️ 9.0/10
3. [Ling Team 提出 UFP4：FP4 预训练中 E1M2/INT4 配合 RHT 优于 E2M1](#item-3) ⭐️ 9.0/10
4. [Anthropic 指控阿里巴巴发动大规模“蒸馏攻击”窃取 Claude 能力](#item-4) ⭐️ 9.0/10
5. [快手系凌川科技完成全国产 3D 堆叠芯片流片，获数亿元融资](#item-5) ⭐️ 8.0/10
6. [高通发布 Dragonfly 数据中心产品组合：含 HBC 架构、C1000 CPU 和 AI300 加速器](#item-6) ⭐️ 8.0/10
7. [2025 中国开源年度报告：OpenHarmony 登顶全球影响力榜首](#item-7) ⭐️ 8.0/10
8. [《The Coming Loop》：AI 循环工程的两层困境](#item-8) ⭐️ 8.0/10
9. [智元总裁彭志辉：资本不再只为机器人 Demo 买单](#item-9) ⭐️ 8.0/10
10. [🤖 特朗普称不再视 Anthropic 为国安威胁，或放松 AI 模型限制  特朗普在接受 Axios 采访时表示，不再将人工智能公司 Anthropic 视为](#item-10) ⭐️ 8.0/10
11. [台积电先进制程代工将全线涨价](#item-11) ⭐️ 8.0/10
12. [消息称字节跳动与博通合作开发 5nm AI 芯片](#item-12) ⭐️ 8.0/10
13. [美光 2026 财年第三季度创纪录：营收同比暴增 346%，AI 需求驱动](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 联手 Broadcom 发布首款自研推理芯片 'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 正式宣布了其首款自研定制芯片——代号为 'Jalapeno' 的推理芯片，该芯片由 Broadcom 协助设计，并由 TSMC 代工制造。据报道，该芯片从设计到量产仅用时九个月，OpenAI 声称在此过程中使用了自家的 AI 模型来加速设计与优化流程。 此举标志着 OpenAI 正式进军定制芯片领域，加入了 Google 和 Meta 等超大规模科技公司的战略行列，旨在减少在推理工作负载中对昂贵的 Nvidia GPU 的依赖。在规模化运行时，定制 ASIC 相比通用 GPU 可降低 40–65% 的总体拥有成本，这使得这一举措对 OpenAI 长远的推理经济效益和算力扩展目标至关重要。 Jalapeno 芯片专门作为推理加速器使用，而非训练芯片，这意味着它针对运行已训练好的模型进行了优化，而非用于模型开发。已确认 TSMC 为该芯片的代工商（而非 Intel），且整个项目在短短九个月的加速时间表内完成。

hackernews · jamdesk · Jun 24, 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 工作负载分为两个阶段：训练阶段，即模型通过处理海量数据集来学习（通常使用 GPU）；以及推理阶段，即训练好的模型将所学知识应用于真实输入（如用户查询）。虽然像 Nvidia 这样的通用 GPU 具有高度灵活性并在训练中占据主导地位，但在持续的推理任务中它们会消耗过多的能源。这推动大型科技公司开发专用集成电路（ASIC）——即为特定推理工作负载量身定制的芯片，在超大规模部署中能提供更高的效率和更低的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techstoriess.com/custom-ai-chips-vs-gpus-the-great-silicon-pivot-of-2026/">Custom AI Chips vs GPUs: The Great Silicon Pivot of 2026 - TechStoriess.com</a></li>
<li><a href="https://investorplace.com/hypergrowthinvesting/2026/04/the-rise-of-custom-ai-chips-is-breaking-nvidias-grip/">The Rise of Custom AI Chips Is Breaking Nvidia's Grip | InvestorPlace</a></li>
<li><a href="https://naddod.medium.com/inference-chip-guide-the-foundation-of-scalable-ai-applications-d18f2c22b36c">Inference Chip Guide: The Foundation of Scalable AI Applications | by NADDOD | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，鉴于整个行业向定制芯片的转变，Google 早期对自研 TPU 的押注现在看来极具先见之明。部分质疑声音指向 OpenAI 关于使用自家模型加速芯片设计的说法，用户质疑这是否具有实质意义，抑或只是营销噱头。还有几位评论者讨论了更激进的方案，如 Taalas 和 Cerebras 将模型权重直接固化在芯片中以实现极致效率，并与 OpenAI 更为常规的 ASIC 路线进行了对比。

**标签**: `#AI Hardware`, `#OpenAI`, `#Broadcom`, `#Inference Chips`, `#AI Infrastructure`

---

<a id="item-2"></a>
## [Computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 9.0/10

Google introduces 'computer use' capabilities for Gemini 3.5 Flash, enabling the model to autonomously interact with graphical user interfaces, browsers, and desktop applications.

hackernews · swolpers · Jun 24, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48662999)

**标签**: `#AI`, `#Google Gemini`, `#Agentic AI`, `#Computer Use`, `#Frontier Models`

---

<a id="item-3"></a>
## [Ling Team 提出 UFP4：FP4 预训练中 E1M2/INT4 配合 RHT 优于 E2M1](https://aihot.virxact.com/items/cmqsspyhw05ydslfuwx48elnq) ⭐️ 9.0/10

Ling Team proposes UFP4, a novel FP4 pre-training quantization method that utilizes E1M2/INT4 formats with Random Hadamard Transform (RHT) to overcome the shrinkage bias of the standard E2M1 format, achieving better convergence and quantization quality.

rss · AI Hot · Jun 25, 01:00

**标签**: `#AI Research`, `#Quantization`, `#FP4 Training`, `#Large Language Models`, `#Low-Precision Computing`

---

<a id="item-4"></a>
## [Anthropic 指控阿里巴巴发动大规模“蒸馏攻击”窃取 Claude 能力](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic has accused Alibaba of conducting the largest known 'distillation attack' to date, using millions of fraudulent interactions to extract capabilities from Anthropic's advanced Claude models.

telegram · @zaihuapd · Jun 25, 01:36

**标签**: `#AI Security`, `#Model Distillation`, `#Anthropic`, `#Alibaba`, `#AI Policy`

---

<a id="item-5"></a>
## [快手系凌川科技完成全国产 3D 堆叠芯片流片，获数亿元融资](https://aihot.virxact.com/items/cmqsus6gm06gqslfuykafgdmy) ⭐️ 8.0/10

快手系 AI 芯片公司凌川科技于 2024 年 3 月独立运营后，完成了数亿元 A+轮融资，并于 4 月成功完成采用全国产 3D 堆叠技术的下一代芯片流片。该公司首创 3D 近存架构，针对 3D 芯片的散热、一致性和可靠性等关键痛点进行了专项优化设计。 这一进展标志着中国在半导体供应链本土化方面取得重要突破，证明全国产 3D 堆叠技术能够成功应用于数据中心 AI 工作负载。此次流片成功验证了华为提出的韬（τ）定律——一种多层级协同优化框架——在互联网数据中心商业产品中的实际落地可行性。 该公司现有的 SL200 视频智能 SoC 芯片已在快手部署数万颗，稳定服务 7 亿用户，为团队的芯片设计能力提供了成熟的商业验证。本轮融资由啟赋资本领投，百度风投、新国都等多家机构参与，资金将主要用于下一代芯片研发、SL200 量产扩产及海外市场拓展。

rss · AI Hot · Jun 25, 01:53

**背景**: 韬（τ）定律由华为何庭波于 2026 年 5 月在国际电路与系统研讨会上发表，是一种超越摩尔定律的多层级协同优化框架，从晶体管、电路、晶片和系统四个层级进行优化。与聚焦晶体管尺寸缩小的摩尔定律不同，韬定律强调全栈协同优化，其理论框架已通过华为麒麟 2026 芯片的实测性能数据得到验证。3D 堆叠技术将多个芯片裸片垂直集成以提高密度和互连速度，其中 3D 近存架构将处理单元靠近内存放置以降低数据传输延迟，这对带宽密集型视频 AI 工作负载至关重要。流片是芯片设计的最终步骤，即将完成的设计文件发送给半导体代工厂进行制造，标志着从设计到物理生产的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zaobao.com.sg/news/china/story20260525-9105489">【早知】“ 韬 定 律 ”是什么？ | 联合早报</a></li>
<li><a href="https://news.pedaily.cn/202605/564396.shtml">详解华为“ 韬 定 律 ”：对半导体行业究竟意味着什么？_ 投资界</a></li>
<li><a href="https://news.mydrivers.com/1/1131/1131701.htm">快手造 芯 ！ 全国产 3 D 堆 叠 芯 片 已流 片 --快科 技 --科 技 改变未来</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#AI Infrastructure`, `#3D Stacking`, `#Hardware`, `#Funding`

---

<a id="item-6"></a>
## [高通发布 Dragonfly 数据中心产品组合：含 HBC 架构、C1000 CPU 和 AI300 加速器](https://aihot.virxact.com/items/cmqsus6gm06gyslfu95t2ox1b) ⭐️ 8.0/10

高通在投资者日发布了全面的 Dragonfly 数据中心解决方案，包括采用 TSV 技术堆叠 LPDDR DRAM 的新型 HBC（高带宽计算）内存架构、拥有 250+ Oryon 内核且频率超过 5GHz 的 C1000 CPU（目标 2028 年上市），以及采用 HBC Gen 2 的 AI300 推理平台（2028 年送样）。搭载 HBC Gen 1 的 AI250 加速器单卡内存读写速率达 133TB/s，预计 2027 年中启动样品测试。 高通的 Dragonfly 产品组合代表其大举进军 AI 数据中心市场，以一种从根本上不同于 HBM 的内存架构直接挑战 Nvidia 和 AMD 等现有巨头，承诺提供更高的能效和更低的总体拥有成本（TCO）。高通已获得 Meta 的多代 CPU 大单以及微软 Azure 对 HBC 平台的部署承诺，显示出可靠的市场吸引力。 HBC 采用分离式架构，将芯片拆分为主 SoC 和 HBC 堆栈，通过标准 2D 有机基板互连，堆栈底部为近内存加速器单元，上方以 TSV 技术堆叠 LPDDR DRAM Die。C1000 CPU 支持 PCIe Gen 7 和 CXL 规范，AI300 则通过 UALink 和 ESUN 进行纵向扩展，横向扩展同时利用铜缆和光纤，高通宣称其每 W 带宽较当今 GPU 提升 4-8 倍。

rss · AI Hot · Jun 25, 01:12

**背景**: HBM（高带宽内存）已成为 AI 加速器的主流内存技术，但其制造成本高昂且工艺复杂，为替代架构创造了机会。TSV（硅通孔）是一种先进封装技术，通过硅芯片创建垂直电气连接，实现内存芯片的 3D 堆叠以获得更高密度和带宽。高通的 Oryon 是一种基于 ARM 架构的定制 CPU 内核，最初为高端 PC 和移动处理器开发，现正适配数据中心工作负载。高通此前曾退出数据中心 CPU 市场，如今正凭借 AI 优化设计重新进入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L08DLD8C05198NMR.html">高通全面进军AI数据中心：Meta签多代CPU大单、微软部署HBC芯片，预计明年贡献数十亿收入|英特尔|cpu|知名企业_网易订阅</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/硅穿孔">硅穿孔 - 维基百科，自由的百科全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Oryon">Oryon - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Qualcomm`, `#Datacenter`, `#AI Inference`, `#Semiconductors`

---

<a id="item-7"></a>
## [2025 中国开源年度报告：OpenHarmony 登顶全球影响力榜首](https://aihot.virxact.com/items/cmqsus6gm06h1slfuy5ncn4y6) ⭐️ 8.0/10

开源社发布的《2025 中国开源年度报告》显示，OpenHarmony 以 60089 的 OpenRank 值登顶全球开源项目影响力榜首。报告还指出，AI 大模型相关仓库年均增长率超过 210%，vLLM 跻身全球项目前 15 名，而中国开发者贡献度增速领先美国超过 10 个百分点。 该报告标志着全球开源格局的重大转变，按照当前态势，中国开发者贡献度有望在七年内超越美国。AI 大模型仓库的爆发式增长以及 DeepSeek R1 等模型展现出的成本效率（训练成本仅 550 万美元），凸显了中国在 AI 生态系统和开源前沿模型领域日益增强的竞争力。 GitHub 平台上中国活跃开发者超过 210 万，位居全球第三，而中国 OpenRank 总贡献度为 254963，位列全球第二。在 10 亿以上参数模型中，Meta 下载量占比 23.2%，阿里 Qwen 系列占 20%，DeepSeek 占 3.8%。在企业开源影响力方面，微软居首，华为位列第二。

rss · AI Hot · Jun 25, 01:02

**背景**: OpenRank 是由 X-lab 实验室开发的开源评估算法，通过贡献网络来衡量开发者和项目的影响力，超越了简单的提交次数统计，能够评估开源活动的实际影响。OpenHarmony 是一款采用多内核架构的开源操作系统，专为物联网设备、智能手机和其他联网硬件设计。vLLM 是一个高性能、高内存效率的大语言模型推理引擎，已成为在生产环境中部署开源大语言模型的关键基础设施组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://open-digger.cn/en/docs/user_docs/metrics/openrank">OpenRank Algorithm | OpenDigger</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-source`, `#AI models`, `#DeepSeek`, `#Qwen`, `#developer ecosystem`

---

<a id="item-8"></a>
## [《The Coming Loop》：AI 循环工程的两层困境](https://aihot.virxact.com/items/cmqssdqf805v1slfux2jw7fpx) ⭐️ 8.0/10

文章提出了一个分析 AI agent 循环的结构性框架，将其分为双层系统：内层 agent loop（模型自行判断任务完成）和外层 harness loop（外部系统验证是否真正完成并续接会话）。文章警告，迭代式 AI 编码会叠加 LLM 特有的代码缺陷——如过度防御性编程和回避不变量——使系统的每一层都让人类越来越难以理解。 随着智能体编码工作流成为行业常态，该分析揭示了真正的危险并非无限循环本身，而是它们所造成的系统性复杂性叠加和深层认知依赖。工程师可能面临一种困境：一旦失去产出代码的同类 AI 系统的访问权，便无法维护和审查这些代码，从根本上挑战了人类对软件系统的长期监督能力。 文章指出，AI 循环的有效应用场景有一个共性：它们要么不产生新代码（如移植、重构），要么产出的代码不需要长期维护（如性能探索）。软件系统的核心隐喻从可理解的"机器"转变为不可预测的"有机体"，由此引出一个紧迫问题：如何在循环驱动的未来中保留人类的判断力和工程规范。

rss · AI Hot · Jun 25, 00:47

**背景**: 在现代 AI 辅助开发中，Claude Code、Cursor 和 Devin 等工具通过一个"harness"（运行时框架）来运作，该框架负责协调用户、LLM 与外部工具之间的交互。Harness 管理着所谓的"agent loop"（智能体循环），反复执行模型调用和工具操作，直到模型发出任务完成的信号。来自微软和卡内基梅隆大学等机构的研究已经记录了一种名为"认知债务"的现象：过度依赖 AI 工具会逐步削弱开发者的信心和批判性分析生成代码的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vibereference.com/ai-development/agents-vs-harnesses">AI Agents vs Harnesses : The 5-Concept Stack — VibeReference</a></li>
<li><a href="https://pub.towardsai.net/harness-in-ai-agents-765ff91ccaeb">Harness in AI Agents . A harness in AI agents is the... | Towards AI</a></li>
<li><a href="https://www.linkedin.com/pulse/smart-ai-vs-cognitive-dependency-how-transform-marc-israel-9fqff">Smart AI vs Cognitive Dependency : How to Transform AI into...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Software Engineering`, `#AI Safety`, `#Autonomous Coding`, `#AI Cognitive Impact`

---

<a id="item-9"></a>
## [智元总裁彭志辉：资本不再只为机器人 Demo 买单](https://www.ithome.com/0/968/259.htm) ⭐️ 8.0/10

在 MWC26 上海大会上，智元联合创始人兼首席技术官彭志辉表示，AI 行业正从数字世界应用转向具身智能的规模化部署时代。他提出了“XYZ 三条曲线”发展框架，并预测具身智能将在约 5 年后迎来“GPT 时刻”，同时强调物理世界的机器人将成为未来 AI Token 的最大消耗群体。 这一观点标志着 AI 基础设施和投资方向的重大战略转变，暗示未来的算力需求将由持续的、多模态的物理世界推理所驱动，而非单纯的文本和图像生成。它同时也反映了行业的广泛共识：机器人企业必须从技术演示转向在真实场景中创造切实的商业价值，才能持续获得资金支持。 彭志辉详细介绍了具身智能产业发展的“XYZ 曲线”框架：X 曲线（当前阶段）以通过表演验证底层技术为主；Y 曲线（即将进入的阶段）涉及大规模真实场景落地并形成数据飞轮；Z 曲线（约 5 年后）则代表海量数据积累引发质变的普及期。他还指出，特斯拉、英伟达和波士顿动力等巨头都在全面转向物理世界智能生态建设和商业价值挖掘。

rss · IT HOME · Jun 25, 01:15

**背景**: 具身智能（Embodied AI）是相对于传统“非具身”AI 模型的一种范式转变，致力于开发能够在真实世界环境中持续进行感知、决策、行动和学习的物理系统（如人形机器人）。在 AI 行业中，“Token”代表大模型在推理过程中处理数据的基本单位，是衡量 AI 算力消耗的通用指标。智元机器人（AgiBot）是一家总部位于上海的中国知名人形机器人公司，由前华为“天才少年”、知名科技博主彭志辉（网名“稚晖君”）等人联合创立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wangjunjian.com/posts/2026-04-13-embodied_ai_survey">具 身 智 能 （ Embodied AI ）技术综述：从基础理论到工程实践</a></li>
<li><a href="https://en.wikipedia.org/wiki/AgiBot">AgiBot - Wikipedia</a></li>
<li><a href="https://medium.com/@aalig/the-true-cost-of-ai-tokens-a-business-opportunity-analysis-for-the-modern-enterprise-bc657f6ea481">The True Cost of AI Tokens : A Business Opportunity... | Medium</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Humanoid Robots`, `#AI Agents`, `#AI Infrastructure`, `#AgiBot`

---

<a id="item-10"></a>
## [🤖 特朗普称不再视 Anthropic 为国安威胁，或放松 AI 模型限制  特朗普在接受 Axios 采访时表示，不再将人工智能公司 Anthropic 视为](https://t.me/zaihuapd/42148) ⭐️ 8.0/10

President Trump indicated he no longer views Anthropic as a national security threat and suggested easing restrictions on their advanced models following a recent meeting with the company's CEO.

telegram · @zaihuapd · Jun 24, 03:45

**标签**: `#AI Policy`, `#Anthropic`, `#AI Regulation`, `#Governance`, `#Frontier AI`

---

<a id="item-11"></a>
## [台积电先进制程代工将全线涨价](https://36kr.com/newsflashes/3866472254411779) ⭐️ 8.0/10

台积电已陆续向客户通知晶圆代工涨价，涨幅约 5%至 10%，范围不仅涵盖此前传闻的 3nm 制程，更扩展至 7nm 及以下所有先进制程。此次涨价影响范围涵盖台积电约 75%的晶圆营收来源。 台积电在先进芯片制造领域占据主导地位，这些芯片对于训练和部署前沿 AI 模型至关重要，因此涨价将直接增加 NVIDIA、苹果、AMD 等主要 AI 实验室和科技巨头的计算成本。这一涨价可能波及整个 AI 供应链，从 AI 加速器到消费电子产品的成本都可能上升，同时压缩无晶圆厂芯片设计公司的利润空间。 5%至 10%的涨价适用于 7nm 及以下所有制程节点，这些节点合计占台积电晶圆代工营收的约四分之三。台积电最接近的竞争对手三星代工在同等制程节点的价格低 20%至 33%，但由于台积电在制造良率方面的优势，按良品率调整后的单颗可用芯片成本可能仍然更有竞争力。

telegram · @zaihuapd · Jun 24, 05:45

**背景**: 半导体制程节点（如 3nm、5nm、7nm）是指用于制造芯片的工艺技术，数字越小通常代表晶体管密度越高、功耗越低。台积电于 2022 年底开始 3nm（N3）工艺的量产，相比上一代 5nm 工艺，晶体管密度提升最高 35%，功耗降低最高 50%。这些先进制程节点对于制造高性能 AI 加速器（如 NVIDIA 的 GPU）和旗舰移动处理器至关重要。台积电在先进制程代工服务领域几乎处于垄断地位，随着 AI 驱动的需求激增，其拥有强大的定价权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3_nm_process">3 nm process - Wikipedia</a></li>
<li><a href="https://siliconanalysts.com/market-data/wafer-price-comparison">Foundry Wafer Price Comparison — Historical Data... | Silicon Analysts</a></li>
<li><a href="https://www.smbom.com/news/38168">TSMC Plans 10% Increase in Wafer Foundry Prices - SmBom</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#Semiconductors`, `#AI Infrastructure`, `#Supply Chain`, `#Chips`

---

<a id="item-12"></a>
## [消息称字节跳动与博通合作开发 5nm AI 芯片](https://t.me/zaihuapd/42153) ⭐️ 8.0/10

路透社报道称，字节跳动正与美国博通公司合作开发一款定制 5nm AI 处理器，计划由台积电制造。虽然设计工作据称进展顺利，但该项目尚未达到标志从设计转向制造的"流片"里程碑，且字节跳动已官方否认了这一传闻。 如果消息属实，这一合作将是字节跳动在美国出口管制和 AI 基础设施竞争加剧的背景下，确保高端 AI 芯片供应的重大战略举措。定制 AI 芯片可以减少字节跳动对英伟达的严重依赖，使其在支撑推荐算法和大语言模型的算力基础上获得更多自主权。 据报道，该芯片采用 5nm 制程工艺，虽然设计进展顺利，但标志设计阶段结束、制造阶段开始的"流片"尚未开始。字节跳动此前曾拨款 20 亿美元购买英伟达芯片，也采购过华为昇腾 910B 芯片，凸显了其在 AI 算力方面的多元化采购策略。

telegram · @zaihuapd · Jun 24, 07:01

**背景**: 5nm 制程是一种先进的半导体制造工艺，与较旧的工艺节点相比，能够实现更高的晶体管密度、更强的性能和更低的功耗。"流片"是芯片行业的关键术语，指设计流程的最后一步，完成后将最终设计交付给代工厂（如台积电）进行物理制造。华为昇腾 910B 是一款国产 AI 加速芯片，已作为中国市场上英伟达 GPU 的重要替代方案崭露头角，尤其是在美国对先进芯片实施出口限制的背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.techerati.com/news-hub/samsung-successfully-develops-5nm-semiconductor-process/">Samsung successfully develops 5 nm semiconductor process</a></li>
<li><a href="https://www.doit.com.cn/p/527695.html">华 为 昇 腾 +DeepSeek：国产AI推理引擎的破局之战</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#ByteDance`, `#Broadcom`, `#AI Infrastructure`, `#Hardware`

---

<a id="item-13"></a>
## [美光 2026 财年第三季度创纪录：营收同比暴增 346%，AI 需求驱动](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

美光科技公布了 2026 财年第三季度创纪录的业绩，营收达 414.6 亿美元，同比增长 346%，远超分析师预期的 358.4 亿美元。公司季度净利润达 282.4 亿美元（约合每天净赚 3.1 亿美元），Non-GAAP 毛利率从去年同期的 39%飙升至 84.9%，并预计下季度营收将达 500 亿美元。 这些业绩凸显了 AI 基础设施的爆发式需求如何将存储芯片制造商转变为半导体行业中最赚钱的公司之一。美光数据中心营收同比增长 653%至 115.2 亿美元，公司已签署 16 份长期战略协议锁定未来 3-5 年订单，表明内存紧缺将持续至 2027 年以后。 HBM4 已进入大规模量产，下一代 HBM4E 预计于 2027 年投产。美光营业利润率高达 81.2%，四大业务板块全面爆发：云内存增长 306%至 137.7 亿美元，移动与客户端增长 254%，汽车与嵌入式业务翻了两番。

telegram · @zaihuapd · Jun 24, 22:22

**背景**: 高带宽存储器（HBM）是一种先进的 3D 堆叠 DRAM 架构，可提供极高的数据带宽和能效，是 AI 加速器和高性能计算的关键组件。HBM 最初由三星、AMD 和 SK 海力士开发，目前由美光、三星、SK 海力士等主要存储芯片制造商生产。随着 AI 模型规模呈指数级增长，对 HBM 的需求急剧上升，因为 AI GPU 需要巨大的内存带宽来为日益强大的计算核心提供数据。HBM 的每一代升级（目前正从 HBM3 向 HBM4 及未来的 HBM4E 演进）都带来更高的带宽和容量，直接支撑更强大的 AI 训练和推理系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.wevolver.com/article/high-bandwidth-memory">High Bandwidth Memory : Concepts, Architecture, and Applications</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#High Bandwidth Memory (HBM)`, `#Micron`, `#Data Center`, `#Hardware`

---