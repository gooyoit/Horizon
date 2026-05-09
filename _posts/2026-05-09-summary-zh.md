---
layout: default
title: "Horizon Summary: 2026-05-09 (ZH)"
date: 2026-05-09
lang: zh
---

> From 103 items, 12 important content pieces were selected

---

1. [DeepSeek 据报将以约 450 亿美元估值进行首轮融资](#item-1) ⭐️ 9.0/10
2. [Anthropic 团队成员主张用 HTML 替代 Markdown 作为 Claude 输出格式](#item-2) ⭐️ 8.0/10
3. [Isomorphic Labs 拟在新一轮融资中筹集逾 20 亿美元](#item-3) ⭐️ 8.0/10
4. [阿波罗与黑石考虑参与博通 350 亿美元 AI 芯片融资](#item-4) ⭐️ 8.0/10
5. [Arm 自研 AGI CPU 客户需求突破 20 亿美元](#item-5) ⭐️ 8.0/10
6. [DeepSeek 大范围开放“识图模式”，正式跨入图文交互时代](#item-6) ⭐️ 8.0/10
7. [中国日均 AI Token 调用量突破 140 万亿](#item-7) ⭐️ 8.0/10
8. [日月光与楠梓电投资 352 亿新台币建设高雄先进封装厂](#item-8) ⭐️ 8.0/10
9. [OpenAI 推出 Codex Chrome 扩展，实现浏览器自动化操作](#item-9) ⭐️ 8.0/10
10. [Anthropic 拟筹集数百亿新资金，估值逼近万亿美元](#item-10) ⭐️ 8.0/10
11. [OpenAI Codex 框架在自主编码与人工审查之间取得平衡](#item-11) ⭐️ 8.0/10
12. [OpenAI 倡导通过思维链监控防范 AI 不对齐](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 据报将以约 450 亿美元估值进行首轮融资](https://t.me/zaihuapd/41289) ⭐️ 9.0/10

中国 AI 公司 DeepSeek 据报正洽谈其首次大规模外部融资，拟募资最高 500 亿元人民币，公司估值可能达到约 450 亿美元。中国国家集成电路产业投资基金（俗称"大基金"）据称正洽谈领投此轮融资。 如果融资落地，这将是中国 AI 公司有史以来最大规模的单轮融资，标志着国资背景资金正在更深介入中国 AI 核心公司。此举也凸显了中美之间在 AI 和半导体自主可控领域日益加剧的地缘竞争。 DeepSeek 此前一直由其母公司——中国对冲基金幻方量化独家资助，此次将是其自 2023 年成立以来首次进行外部融资。据报道的 450 亿美元估值，对于一家声称仅花费约 600 万美元训练 V3 模型的公司而言是一个巨大的飞跃。

telegram · @zaihuapd · May 8, 14:59

**背景**: DeepSeek 是一家总部位于杭州的 AI 公司，由对冲基金幻方量化的联合创始人梁文锋于 2023 年 7 月创立。该公司在 2025 年 1 月因 DeepSeek-R1 模型以极低的训练成本达到与 OpenAI GPT-4 相当的性能而引发全球关注，被观察人士称为美国 AI 领域的"斯普特尼克时刻"。国家集成电路产业投资基金（"大基金"）是中国政府引导基金，旨在推动中国半导体产业实现自主可控，目前已设立三期，注册资本总额达数千亿元人民币。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/National_Integrated_Circuit_Industry_Investment_Fund">National Integrated Circuit Industry Investment Fund</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI Funding`, `#Frontier AI`, `#China AI`, `#Semiconductors`

---

<a id="item-2"></a>
## [Anthropic 团队成员主张用 HTML 替代 Markdown 作为 Claude 输出格式](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything) ⭐️ 8.0/10

Anthropic Claude Code 团队成员 Thariq Shihipar 发表文章，详细论证了让 Claude 输出 HTML 而非 Markdown 能为代码审查等复杂任务带来更丰富、更具交互性和视觉结构化的结果。Simon Willison 随后用 GPT-5.5 对 copy.fail Linux 安全漏洞生成了 HTML 格式的解释文档，产出了样式精美、可交互的技术说明页面。 这一观点挑战了长期以来认为 Markdown 是 LLM 最佳输出格式的假设——该假设在 GPT-4 时代因 token 限制而确立，当时 Markdown 的简洁性至关重要。如果 HTML 输出成为最佳实践，它可能从根本上改变开发者与 AI 编程助手的交互方式，实现包含 SVG 图表、交互式组件和页内导航的更丰富解释。 该方法利用了 Claude 的 Artifacts 功能，该功能支持包含 CSS 和 JavaScript 的单页 HTML 网站，使 LLM 能够生成带有嵌入式 SVG 图表、按严重程度颜色编码的标注、交互式组件和结构化导航的输出。一个实际的提示词示例要求 Claude 通过创建 HTML artifact 来审查 PR，在实际 diff 上添加行内边距注释，并按严重程度对发现进行颜色编码。

rss · Simon Willison · May 8, 21:00

**背景**: 自 GPT-4 时代以来，Markdown 一直是 LLM 的默认输出格式，因为它在 token 效率方面表现优异——每个格式标签都会消耗 token，而 Markdown 更轻量的语法在上下文窗口限制约为 8,192 个 token 时节省了宝贵的空间。Claude 于 2024 年推出的 Artifacts 功能允许用户提示 Claude 创建使用 HTML、CSS 和 JavaScript 的交互式单页应用，并直接在 Claude 界面中渲染，支持迭代优化。随着上下文窗口的大幅增长，HTML 的 token 开销已不再那么令人担忧，这重新开启了哪种格式更适合复杂输出需求的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them">What are artifacts and how do I use them? | Claude Help Center</a></li>
<li><a href="https://medium.com/@wetrocloud/why-markdown-is-the-best-format-for-llms-aa0514a409a7">Why Markdown is the best format for LLMs | by Wetrocloud - Data Extraction for the Web | Medium</a></li>
<li><a href="https://simonwillison.net/2024/Oct/21/claude-artifacts/">Everything I built with Claude Artifacts this week</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Prompt Engineering`, `#LLM Output Formats`, `#Anthropic`, `#AI Coding`

---

<a id="item-3"></a>
## [Isomorphic Labs 拟在新一轮融资中筹集逾 20 亿美元](https://36kr.com/newsflashes/3801377962090247?f=rss) ⭐️ 8.0/10

从谷歌 DeepMind 分拆出来的 AI 驱动药物研发公司 Isomorphic Labs 正深入洽谈，计划在新一轮融资中筹集超过 20 亿美元。曾主导该公司去年首轮融资的风投机构 Thrive Capital 预计将再次牵头本轮融资，Alphabet 也将参与其中。 这笔巨额融资表明投资者对将前沿 AI 应用于药物研发的信心日益增强，这是人工智能最具前景且资本密集的应用领域之一。Thrive Capital 和 Alphabet 的共同参与凸显了 AI 驱动生物技术的战略重要性，各大科技公司和风投机构正竞相加速制药创新。 Isomorphic Labs 由 Demis Hassabis 于 2021 年创立，是 Alphabet 旗下的子公司，利用 DeepMind 的 AlphaFold 技术高精度预测蛋白质结构，从而发现新的药物递送路径。该公司总部位于伦敦，作为 DeepMind 的分拆机构运营，Hassabis 同时担任两家组织的 CEO。

rss · 36kr · May 9, 01:21

**背景**: Isomorphic Labs 基于 DeepMind 突破性的 AlphaFold 技术，该技术通过从氨基酸序列精确预测三维蛋白质结构，彻底改变了结构生物学领域。AI 驱动的药物研发旨在利用机器学习来识别疾病靶点、生成新化合物并预测安全性，从而变革传统制药流程，有望缩短新药上市时间并降低成本。该领域已吸引科技巨头和制药公司的广泛关注，因为传统药物开发通常需要十余年时间，每种获批药物的成本高达数十亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://www.isomorphiclabs.com/">Reimagining Drug Discovery Process with AI - Isomorphic Labs</a></li>
<li><a href="https://www.nature.com/articles/s41591-024-03434-4">Artificial intelligence in drug development | Nature Medicine</a></li>

</ul>
</details>

**标签**: `#AI Drug Discovery`, `#Isomorphic Labs`, `#Google DeepMind`, `#Biotech AI`, `#Venture Capital`

---

<a id="item-4"></a>
## [阿波罗与黑石考虑参与博通 350 亿美元 AI 芯片融资](https://36kr.com/newsflashes/3801359034113538?f=rss) ⭐️ 8.0/10

据报道，阿波罗全球管理公司和黑石集团正在与博通洽谈参与约 350 亿美元的私募信贷融资，该笔资金将专门用于支持博通开发面向人工智能任务的芯片。知情人士透露，目前谈判仍在进行中，具体条款可能发生变化。 这将是迄今规模最大的私募信贷融资之一，标志着机构投资者对 Nvidia GPU 主导地位之外的 AI 硬件建设抱有巨大信心。博通是为超大规模云厂商提供定制 AI 芯片（ASIC）和网络基础设施的关键企业，这笔资金有望显著扩展整个行业的前沿 AI 算力。 这笔融资采用私募信贷形式，即由非银行贷款机构提供的私下协商贷款，相比传统银行融资或公开债券市场，能为博通提供更灵活、可定制的条款。即使按私募信贷的标准来看，约 350 亿美元的融资规模也极为罕见，凸显了先进 AI 芯片开发的高度资本密集特性。

rss · 36kr · May 9, 01:08

**背景**: 博通已成为 AI 硬件领域的重要力量，为谷歌等超大规模云厂商设计定制 AI 芯片（ASIC），据报道还在与 OpenAI 合作开发定制芯片。与主导通用 AI GPU 市场的 Nvidia 不同，博通专注于为特定 AI 工作负载量身定制的专用芯片，以及连接 AI 服务器集群的关键网络交换设备。私募信贷近年来日益流行，由非银行贷款机构直接向企业提供贷款，条款比传统银行贷款更加灵活。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ssga.com/us/en/intermediary/insights/what-is-private-credit-and-why-investors-are-paying-attention">What is private credit? And why investors are paying attention</a></li>
<li><a href="https://www.fool.com/investing/2026/04/13/are-broadcoms-custom-ai-chips-key-to-the-future-of/">Are Broadcom 's Custom AI Chips the Key to the... | The Motley Fool</a></li>
<li><a href="https://medium.com/@mparekh/ai-broadcom-an-alternate-for-ai-chips-rtz-572-c34f701016f4">AI : Broadcom an alternate for AI chips . RTZ #572 | Medium</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Broadcom`, `#AI Chips`, `#Private Equity`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [Arm 自研 AGI CPU 客户需求突破 20 亿美元](https://www.ithome.com/0/948/023.htm) ⭐️ 8.0/10

Arm 在 FY2026 第四季度财报电话会议上表示，客户对其首款自研 AGI CPU 在 FY2027–2028 的总需求已突破 20 亿美元，较 3 月 24 日发布时增长了一倍多。公司预计该芯片将在 FY2027 第四季度创造近 1 亿美元的首批收入，自研 CPU 业务到 2031 财年累计收入将达到 150 亿美元。 这表明业界正在大规模投资专为 AI 和 AGI 工作负载定制的数据中心芯片，标志着 Arm 从单纯的 IP 授权向自研芯片的战略转型。需求的激增凸显了 AI 算力的严重短缺，以及超大规模客户越来越愿意采用基于 Arm 架构的定制处理器来构建 AI 基础设施。 Arm AGI CPU 采用双芯粒设计，内存和 I/O 位于同一颗芯片上，支持 96 通道 PCIe Gen 6、CXL 3.0 以及最高 DDR5-8800 内存。Arm 表示软件支持已经就绪，机架设计也是现成的，因此该芯片可以快速部署到数据中心中。

rss · IT HOME · May 9, 00:57

**背景**: Arm Holdings 传统上一直向高通、苹果和亚马逊等公司授权其处理器 IP，而非自行设计和销售芯片。AGI CPU 代表了 Arm 首次进入自主生产芯片的领域，专为数据中心中代理式 AI 时代而构建。Arm 的 Neoverse 平台是一系列专为数据中心和高性能计算设计的 64 位 CPU 核心，是该公司现有的基础设施工作负载产品，而 CSS（计算子系统）则提供预集成的 IP 解决方案以加速合作伙伴的芯片开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Arm-AGI-CPU">Arm Announces AGI CPU For AI Data Centers - Phoronix</a></li>
<li><a href="https://en.wikipedia.org/wiki/ARM_Neoverse">ARM Neoverse</a></li>
<li><a href="https://www.arm.com/markets/computing-infrastructure/arm-total-design">Arm Total Design: Custom Compute Systems for AI, 5G & Cloud...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Arm`, `#Datacenter Chips`, `#AGI`, `#Semiconductors`

---

<a id="item-6"></a>
## [DeepSeek 大范围开放“识图模式”，正式跨入图文交互时代](https://www.ithome.com/0/948/020.htm) ⭐️ 8.0/10

DeepSeek has widely rolled out its new 'Image Recognition Mode' to users, enabling advanced multimodal capabilities such as complex visual reasoning, cultural meme interpretation, artifact identification, and UI-to-code generation.

rss · IT HOME · May 9, 00:55

**标签**: `#DeepSeek`, `#Multimodal AI`, `#Vision-Language Model`, `#AI Product Launch`, `#Generative AI`

---

<a id="item-7"></a>
## [中国日均 AI Token 调用量突破 140 万亿](https://www.ithome.com/0/948/018.htm) ⭐️ 8.0/10

截至 2026 年 3 月，中国日均 AI Token（词元）调用量已突破 140 万亿，较两年前飙涨超 100000%，增长超千倍。这一爆发式增长主要由国内外多款大模型接连上新以及 AI 智能体（Agent）的快速普及所带动。 这一惊人的增长表明中国的 AI 应用已从试验阶段进入大规模部署阶段，对算力基础设施产生了巨大需求。算力租赁市场预计 2026 年将达到 2600 亿元规模，高端 GPU 出租率超过 90%，显示出结构性供给紧张，将深刻影响整个行业的投资和基础设施规划。 当前算力租赁行业处于高景气、结构性紧缺阶段，尤其是高端 GPU 的出租率已超过 90%。专家表示，从当前的供需情况来看，未来一段时间算力租赁市场仍有望持续增长。

rss · IT HOME · May 9, 00:38

**背景**: Token（词元）是 AI 语言模型处理文本的最小单位，大约相当于 1-2 个汉字或 4 个英文字母，是 AI 所有理解、生成、记忆和计费的基础。AI 智能体（Agent）是基于大语言模型构建的自主系统，能够通过接入外部知识库和工具来完成客服、金融交易、医疗诊断等特定任务。算力租赁市场允许企业按需租用 GPU 算力而无需自购硬件，随着 AI 工作负载的大幅增长，这一市场变得日益重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.acabridge.cn/pinglun/202603/t20260316_2722532.shtml">人工智能（AI）里的“元词”：什么是“Token”</a></li>
<li><a href="https://www.cnblogs.com/halfcode/p/19955613">4. Token(词元)，5分钟彻底搞懂 - 老陈说编程 - 博客园</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#token usage`, `#compute demand`, `#AI adoption`, `#China AI`

---

<a id="item-8"></a>
## [日月光与楠梓电投资 352 亿新台币建设高雄先进封装厂](https://www.ithome.com/0/948/016.htm) ⭐️ 8.0/10

日月光半导体与楠梓电子联合宣布，将在高雄楠梓科技产业园区投资 352.35 亿新台币建设先进封装设施，预计 2029 年 9 月正式启用。该厂房为地上 8 层、地下 2 层的现代化建筑，总建筑面积约 113402.42 平方米，将导入 FOCoS 与 FC-BGA 封装技术。 这项投资直接针对 AI 芯片生产中的关键瓶颈——台积电 CoWoS 先进封装产能严重不足，无法满足 AI 加速器激增的需求。通过提供无需硅中介层、成本更低的 FOCoS 替代方案，日月光有望显著扩大 XPU 与 HBM 集成的供应基础，并降低整个行业的 AI 硬件成本。 FOCoS（扇出型基板上芯片封装）的变体如 FOCoS-CL 和 FOCoS-Bridge 可以在不需要硅中介层的情况下实现 XPU 与 HBM 的集成，而硅中介层正是台积电 CoWoS 工艺的主要成本来源。日月光 FOCoS 技术支持多达五层 RDL 重布线互连，RDL 线宽/间距可达 1.5/1.5µm，扇出模块尺寸最大可达 34×50mm²。

rss · IT HOME · May 9, 00:30

**背景**: CoWoS（Chip-on-Wafer-on-Substrate）是台积电独有的 2.5D/3D 先进封装技术，先将芯片绑定到硅中介层晶圆上，再将整体安装在基板上——它是 AI GPU 与 HBM 内存集成的关键工艺，但产能一直是重大瓶颈。FOCoS 是一种替代性的扇出型封装方案，使用 RDL（重布线层）互连而非硅中介层来连接多个小芯片，成本更低但在性能密度上有所取舍。FC-BGA（倒装芯片球栅阵列）是一种成熟的高性能封装技术，通过焊料凸点将硅芯片直接连接到封装基板上，广泛应用于 CPU 和高性能计算领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ase.aseglobal.com/focos/">FOCoS | ASE</a></li>
<li><a href="https://www.eetasia.com/ase-unveils-focos-advancements/">ASE Unveils FOCoS Advancements - EE Times Asia</a></li>
<li><a href="https://anysilicon.com/cowos-package/">Understanding CoWoS Packaging Technology - AnySilicon</a></li>

</ul>
</details>

**标签**: `#advanced packaging`, `#semiconductors`, `#AI hardware`, `#CoWoS`, `#ASE`

---

<a id="item-9"></a>
## [OpenAI 推出 Codex Chrome 扩展，实现浏览器自动化操作](https://developers.openai.com/codex/changelog) ⭐️ 8.0/10

OpenAI 为其 Codex agent 发布了 Chrome 扩展，使其能够自主导航网站、录入数据并在浏览器中直接执行任务。该扩展在独立的后台标签组中运行，支持跨标签页多任务并行执行，不会干扰用户当前的浏览会话。 这标志着自主 AI agent 能力的重大飞跃，使 Codex 从纯粹的代码生成扩展到真实的网页交互和浏览器操作。它将 Codex 定位为一个更广泛的企业级 agent 平台，能够处理重复性的基于网页的工作流程，这可能从根本上改变开发者和知识工作者与 Web 应用的交互方式。 用户需要先从 Codex app 安装 Chrome 插件，再从 Chrome Web Store 安装扩展才能开始使用。Codex app 的内置浏览器功能也得到增强，可以与本地开发服务器和文件页面交互，支持点击 UI 元素、复现视觉 bug 和验证本地修复等用例。该扩展目前除欧盟和英国外全地区可用，这两个地区的支持将在后续推出。

telegram · @zaihuapd · May 8, 04:17

**背景**: OpenAI Codex 是一个 AI 编程 agent，最初于 2025 年 4 月以 Codex CLI 的形式发布，专为编写代码和修复 bug 等软件工程任务而设计。到 2026 年 3 月，Codex 的周活跃用户已超过 200 万，并发展成为一个更广泛的企业级 agent 平台。用户可以通过 ChatGPT 网页应用、Codex CLI、Windows 和 macOS 桌面应用以及多种 IDE 集成来使用它。浏览器操作型 AI agent 已成为 AI 行业的一大重要趋势，多家公司正在竞相构建能够自主与网页界面交互的 agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent)</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#OpenAI`, `#Codex`, `#Browser Automation`, `#Web Interaction`

---

<a id="item-10"></a>
## [Anthropic 拟筹集数百亿新资金，估值逼近万亿美元](https://www.ft.com/content/a40cafcc-0fa4-4e70-9e24-90d826aea56d) ⭐️ 8.0/10

Anthropic 正考虑在今年夏天筹集数百亿美元的巨额资金，有望将其估值推高至近 1 万亿美元，从而超越 OpenAI 约 8800 亿美元的估值。在 Forge Global 等私募股权二级市场平台上，Anthropic 目前的隐含估值已飙升至 1 万亿至 1.2 万亿美元区间，较其 2 月完成 300 亿美元融资时 3800 亿美元的投后估值翻了逾两倍。 这笔潜在的融资标志着 AI 军备竞赛的急剧升级，表明资本市场将 Anthropic 视为 OpenAI 在前沿 AI 开发领域主导地位的有力挑战者。巨额资金的注入将用于支撑训练下一代前沿模型所需的大规模算力基础设施扩容，直接影响 AI 行业的竞争格局。 Anthropic 估值飙升的主要驱动力是企业端客户的爆发式增长，其二级市场隐含估值在短短数月内实现了对 OpenAI 的实质性反超。该公司今年 2 月刚完成 300 亿美元融资时投后估值为 3800 亿美元，这意味着其市场认知价值在不到半年的时间里翻了近三倍。

telegram · @zaihuapd · May 8, 11:15

**背景**: Anthropic 是领先的前沿 AI 实验室之一，以开发与 OpenAI 的 GPT 系列直接竞争的 Claude 大语言模型家族而闻名。前沿 AI 模型的训练需要庞大且不断增长的算力基础设施——主要由数据中心中的 Nvidia GPU 和 Google TPU 驱动——这使得数十亿美元级别的融资成为保持竞争力的必要条件。随着各公司竞相构建更强大的模型，AI 行业出现了一波前所未有的巨额融资浪潮，在企业对 AI 解决方案需求激增的背景下，估值也在快速攀升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackernoon.com/how-big-tech-is-locking-in-the-frontier-ai-supply-chain">How Big Tech Is Locking In the Frontier AI Supply Chain | HackerNoon</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI funding`, `#frontier AI`, `#compute infrastructure`, `#AI industry`

---

<a id="item-11"></a>
## [OpenAI Codex 框架在自主编码与人工审查之间取得平衡](https://twitter.com/sama/status/tweet-2052866501611540812) ⭐️ 8.0/10

Sam Altman 转发了 OpenAI 工程师 @ithilgore 的更新，透露团队在 Codex 底层框架上投入了大量精力，使其能够在常规编码任务上快速推进，同时在需要时暂停等待人工审查。这凸显了 Codex 智能体架构背后的一个关键设计理念——在速度和自主性与适当的安全检查点之间取得平衡。 这种设计方法对于 AI 编码智能体的企业级采用至关重要，因为它解决了自动化带来的生产力提升与软件开发中人工监督需求之间的根本矛盾。自主处理常规工作并在需要时暂停审查的能力，可能为 AI 智能体在编码之外众多领域的运作方式树立标准。 OpenAI 的 Codex 既作为 ChatGPT 内的云端智能体提供，也作为 Codex CLI 提供——后者是一个用 Rust 构建的开源本地编码智能体，可在终端中运行。该框架的"暂停审查"机制反映了从 o3 模型延续下来的安全考量，确保高风险决策能够接受人工审查。

twitter · Sam Altman · May 8, 21:41

**背景**: OpenAI 于 2025 年 5 月推出了 Codex，这是一款 AI 编码智能体，标志着从基于聊天的 AI 助手向能够接受目标、使用工具、编写代码和调试的自主执行引擎的转变。Codex CLI 是开源的本地运行版本，可以在用户机器上读取、修改和执行代码，而云端版 Codex 则在 ChatGPT 内使用沙盒环境运行。其底层模型 codex-1 即使在没有自定义脚手架的情况下也在编码评估中表现出色，并面向 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划的用户开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>
<li><a href="https://techcrunch.com/2025/05/16/openai-launches-codex-an-ai-coding-agent-in-chatgpt/">OpenAI launches Codex , an AI coding agent , in... | TechCrunch</a></li>
<li><a href="https://developers.openai.com/codex/cli">CLI – Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI Agents`, `#Software Engineering`, `#Autonomous Coding`

---

<a id="item-12"></a>
## [OpenAI 倡导通过思维链监控防范 AI 不对齐](https://twitter.com/sama/status/tweet-2052853008674017288) ⭐️ 8.0/10

OpenAI 在 CEO Sam Altman 的转发助推下，公开强调思维链（CoT）监控器是防范 AI 智能体不对齐的关键防御层，并表示他们刻意避免对模型的推理过程施加惩罚，以保持这种可监控性。 随着 AI 智能体变得越来越自主并能够执行现实世界的操作，确保它们与人类意图保持一致是一项关键的安全挑战。保持可读的思维链推理为窥探模型决策过程提供了一个罕见但脆弱的窗口，它有可能成为未来前沿 AI 系统的核心控制机制。 OpenAI 特别指出，对模型内部推理过程施加惩罚会降低可监控性，这意味着注重安全的训练必须避免压制模型自然的思维表达。研究人员将 CoT 可监控性描述为“脆弱的”，需要全行业共同努力在机会丧失之前对其进行测量和保存。

twitter · Sam Altman · May 8, 20:47

**背景**: 思维链（CoT）监控是一种 AI 安全技术，通过自动化系统读取模型在得出答案之前产生的逐步推理过程，从而标记可疑或潜在有害的推理路径。智能体不对齐指的是自主 AI 智能体（能够独立使用编码环境和电子邮件等工具的系统）追求偏离操作者意图的目标的风险。随着 AI 系统从简单的聊天机器人过渡到自主智能体，OpenAI 和 Anthropic 的近期研究都强调这是一个日益受到关注的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/evaluating-chain-of-thought-monitorability/">Evaluating chain - of - thought monitorability | OpenAI</a></li>
<li><a href="https://arxiv.org/html/2507.11473v1">Chain of Thought Monitorability : A New and Fragile Opportunity for...</a></li>
<li><a href="https://www.anthropic.com/research/agentic-misalignment">Agentic Misalignment : How LLMs could be insider threats \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Alignment`, `#Chain of Thought`, `#OpenAI`, `#AI Agents`

---