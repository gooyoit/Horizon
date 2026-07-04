---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> From 103 items, 8 important content pieces were selected

---

1. [华为发布 Atlas 350 加速卡：搭载昇腾 950PR，算力达 H20 的 2.87 倍](#item-1) ⭐️ 9.0/10
2. [腾讯玄武实验室阿图因 AI 在 CyberGym 基准测试中超越 Anthropic Mythos](#item-2) ⭐️ 9.0/10
3. [Andrej Karpathy 推出 nanochat：100 美元打造 ChatGPT 克隆](#item-3) ⭐️ 8.0/10
4. [Current AI 发布开源 AI 差距地图 v0.1](#item-4) ⭐️ 8.0/10
5. [Simon Willison 2026 年 6 月通讯：前沿 AI 模型发布与开源权重进展](#item-5) ⭐️ 8.0/10
6. [重新上架的 Claude Fable 5 被反馈性能下降并频繁强制降级](#item-6) ⭐️ 8.0/10
7. [Google Gemini Omni Flash 登顶 Video Arena 榜首](#item-7) ⭐️ 8.0/10
8. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [华为发布 Atlas 350 加速卡：搭载昇腾 950PR，算力达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 9.0/10

在华为中国合作伙伴大会 2026 上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 Atlas 350 AI 加速卡。该卡单卡算力达到英伟达 H20 的 2.87 倍，配备 112 GB 自研 HBM，并且是目前国内唯一支持 FP4 低精度推理的加速卡。 此次发布标志着中国国产 AI 算力的重大飞跃，为国内市场提供了替代英伟达受限硬件的强大方案。通过支持 FP4 推理并实现 70B 参数大模型单卡加载，该产品大幅降低了大规模 AI 部署的推理延迟与硬件投资成本。 与前代产品相比，Atlas 350 在向量算力、互联带宽及自研 HBM 容量等方面均实现了大幅提升。其 FP4 能力采用 4 位浮点数格式（E2M1）压缩模型参数，相比 FP32 可减少多达 8 倍的内存占用，从而加速万亿参数模型的计算。

telegram · @zaihuapd · Jul 3, 08:35

**背景**: 英伟达 H20 是为遵守美国出口限制而专为中国市场设计的 AI 加速器，其 FP16 算力为 148 TFLOPS，性能低于 H100。FP4 是一种超低精度数值格式，相比传统的 FP16 或 FP32 实现了重大转变，能够在保持浮点表示非线性特性的同时实现高效推理。华为昇腾 950PR 芯片于 2025 年 9 月首次公布，是推动国产 AI 芯片至 2028 年发展路线图的重要组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/昇腾950PR芯片/66772899">昇腾950pr芯片 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/H20/64934047">H20_百度百科</a></li>
<li><a href="https://blog.csdn.net/stephen147/article/details/141031860">大模型涉及到的精度是啥？FP32、TF32、FP16、BF16、FP8、FP4、NF4、INT8区别_fp4和fp8-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#AI Chips`, `#Huawei`, `#Ascend`, `#AI Infrastructure`

---

<a id="item-2"></a>
## [腾讯玄武实验室阿图因 AI 在 CyberGym 基准测试中超越 Anthropic Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 9.0/10

腾讯玄武实验室宣布，其研发的阿图因 AI 在加州大学伯克利分校主导的 CyberGym 网络安全基准测试中获得 84.0% 的得分，超过 Anthropic 的 Claude Mythos Preview，且消耗的预算不到 Mythos 的 0.1%。阿图因 AI 还在 curl、gnark、OpenSSL、Python cryptography、Java bc-java 等重要项目中发现了多个 Mythos 未检出的高危逻辑漏洞。 这一结果表明，基于开源模型构建的低成本、可本地部署的 AI 系统在复杂网络安全任务中能够超越昂贵的前沿模型方案。它标志着自主 AI 代理在进攻性安全和漏洞发现方面的重大能力飞跃，可能重塑行业在自动化代码审计和零日漏洞挖掘方面的方法。 阿图因 AI 是一个多智能体安全分析系统，能够对源代码、二进制文件和 JavaScript 包进行推理，生成具体的漏洞利用证据。在伯克利 BVI 真实世界漏洞榜单中，阿图因 AI 的漏洞严重程度排名第 1，总数排名第 5，最高漏洞严重程度评分达 9.3。

telegram · @zaihuapd · Jul 3, 16:12

**背景**: CyberGym 是由加州大学伯克利分校开发的大规模、拟真网络安全基准测试，用于评估 AI 代理发现和利用真实世界软件漏洞的能力。除了复现已知漏洞外，CyberGym 还测试代理能否发现不完整的补丁和此前未知的零日漏洞。该基准测试为比较不同 AI 系统的进攻性安全能力提供了标准化框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rdi.berkeley.edu/blog/cybergym/">Center for Responsible, Decentralized Intelligence at Berkeley</a></li>
<li><a href="https://xlab.tencent.com/en/2026/07/02/xuanwu-atuin-cybergym/">Tencent Xuanwu Atuin AI on CyberGym - Tencent Xuanwu Lab</a></li>
<li><a href="https://letsdatascience.com/news/tencent-xuanwu-atuin-ai-achieves-strong-cybergym-results-5701face">Tencent Xuanwu Atuin AI Achieves Strong CyberGym Results | Let's Data Science</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Cybersecurity`, `#Vulnerability Detection`, `#Tencent`, `#Benchmark`

---

<a id="item-3"></a>
## [Andrej Karpathy 推出 nanochat：100 美元打造 ChatGPT 克隆](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

2025 年 10 月 13 日，Andrej Karpathy 创建了一个名为 'nanochat' 的新开源代码库，目标是仅用 100 美元构建尽可能好的 ChatGPT 克隆。该项目使用大约 8000 行 PyTorch 代码编写，旨在以极简、高可及性的方式实现一个功能强大的大型语言模型。 该项目大幅降低了理解和构建对话式 AI 的门槛，使前沿大语言模型开发能够被更广泛的受众所接触。鉴于 Karpathy 在创建 'nanoGPT' 等高影响力教育资源方面的声誉，nanochat 既是一个实用工具，也是一份学习资源，可能会影响开发者对低成本模型训练的看法。 nanochat 的主要性能指标是 'time to GPT-2'，即在一个 8xH100 GPU 节点上超越 GPT-2（1.6B）CORE 指标所需的实际运行时间。该项目强调简洁性和可读性，整个实现包含在大约 8000 行 PyTorch 代码中。

github · karpathy/nanochat · Jul 3, 17:47

**背景**: Andrej Karpathy 是一位著名的 AI 研究员和教育家，曾是 OpenAI 的创始成员和特斯拉的 AI 总监，以其通俗易懂的深度学习和 LLM 教程而闻名。他有创建 'nano' 系列项目的传统——即对复杂 AI 系统进行极简主义的教育性重新实现，例如用于复现 GPT-2 规模模型的 nanoGPT。虽然大规模训练最先进的大语言模型可能需要数千万甚至上亿美元的成本，但 Karpathy 的项目专注于将核心概念提炼成个人可以运行和研究的、经济实惠且易于理解的代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy / nanochat : The best ChatGPT that $100 can buy.</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/10/andrej-karpathys-nanochat/">Build ChatGPT Clone with Andrej Karpathy 's nanochat</a></li>
<li><a href="https://aidive.org/en/ai/nanochat-karpathy-ai">NanoChat - minimalist AI web chat</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Open Source`, `#Andrej Karpathy`, `#LLM Training`

---

<a id="item-4"></a>
## [Current AI 发布开源 AI 差距地图 v0.1](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

已获 4 亿美元资金承诺的非营利组织 Current AI 发布了开源 AI 差距地图 v0.1，这是一个针对开源 AI 生态系统的综合索引。该地图深入分类了来自 228 个组织的 421 个关键产品，包括 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，涵盖 14 个类别。 这一举措为碎片化的开源 AI 领域提供了急需的结构化概览，帮助研究人员、开发者和政策制定者识别关键差距并追踪最新技术发展。此外，底层数据在 GitHub 上以 MIT 许可证发布，使其成为更广泛社区高度可及且可重复使用的公共资源。 这 421 个经过深入分析的产品仅是冰山一角，剩余的 24,400 个未分类产物构成了等待未来研究的生态系统长尾。该项目共追踪了 16,185 个 GitHub 仓库，底层数据包含 1,184 个 YAML 文件、架构和收集脚本，均可在 currentai-org/os-ai-map 仓库中获取。

rss · Simon Willison · Jul 3, 22:04

**背景**: Current AI 是一个旨在为 AI 构建公共选项的全球合作组织，于 2025 年 2 月在巴黎举行的 AI 行动峰会上作为非营利组织成立。该组织的差距地图试图系统地索引跨越技术栈三个层次的开源 AI 产物：模型组件、产品/用户体验（UX）和基础设施。通过绘制这些项目，该倡议旨在突出开源替代方案在哪些方面已经成熟，以及在哪些方面与专有解决方案相比仍存在关键差距。

**标签**: `#Open Source AI`, `#AI Ecosystem`, `#AI Models`, `#Datasets`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [Simon Willison 2026 年 6 月通讯：前沿 AI 模型发布与开源权重进展](https://simonwillison.net/2026/Jul/3/june-newsletter/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 2026 年 6 月的赞助者专属通讯，涵盖了主要前沿 AI 模型的发布，包括 Claude Fable 5、GPT-5.6 和 GLM-5.2，其中 GLM-5.2 被他认为是目前最好的开源权重模型。通讯还讨论了美国出口管制政策、'tokenmaxxing'趋势的终结，以及 Datasette、sqlite-utils 和 shot-scraper 等软件项目的更新。 Willison 被广泛认为是 AI 领域高信噪率的内容策展人和思想领袖，他对前沿模型的评价有助于塑造社区对当前技术水平的认知。该通讯揭示了关键的行业动态——包括开源权重竞赛、出口管制带来的监管压力，以及不断变化的优化策略——这些都直接影响着 AI 开发者和研究人员。 该通讯通过 GitHub Sponsors 以每月 10 美元的价格付费订阅，每期内容在一个月延迟后免费公开。值得注意的是，GLM-5.2 被强调在能力上超越了其他开源权重模型，通讯还涵盖了 WASM（WebAssembly）相关项目以及 AI 模型分析。

rss · Simon Willison · Jul 3, 14:50

**背景**: 开源权重 AI 模型是指其训练参数（权重）公开可供下载、使用和修改的模型，与封闭的专有 API 形成对比。Simon Willison 是一位知名的开发者和博客作者，以创建 Datasette（用于探索和发布数据的工具）、sqlite-utils（用于操作 SQLite 数据库的命令行工具）和 shot-scraper（基于 Playwright 构建的自动化网页截图工具）而闻名。'Tokenmaxxing' 是指激进地最大化大语言模型的上下文窗口或 token 使用量以获得更好性能的做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for ...</a></li>
<li><a href="https://shot-scraper.datasette.io/">shot-scraper</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Newsletter`, `#Frontier AI`, `#LLMs`, `#Simon Willison`

---

<a id="item-6"></a>
## [重新上架的 Claude Fable 5 被反馈性能下降并频繁强制降级](https://www.ithome.com/0/972/477.htm) ⭐️ 8.0/10

Anthropic 在 6 月 30 日解除出口管制后，于 7 月 1 日重新上线了其最强模型 Claude Fable 5，但大量用户反馈称该模型的实际表现明显弱于此前的版本。此外，过于严苛的安全护栏在日常任务中频繁触发，导致系统自动回退到较旧的 Opus 4.8 模型。 这一情况凸显了 AI 行业在最大化模型能力与实施严格安全机制之间持续存在的紧张关系，表明过于激进的安全护栏可能会在无意中削弱前沿模型的实用性。这直接影响了依赖 Fable 5 执行大规模、多日自主编程项目的开发者和企业，因为意外的模型降级会打断复杂的工作流程并降低用户体验。 根据当前重新上架的条款，Fable 5 的使用量被限制在用户每周总额度的 50%，并计划在 7 月 7 日之后完全转入按用量积分计费模式。来自 @arena 测试平台的独立测试结果在很大程度上印证了用户的抱怨，即恢复后的模型表现与其重新上线前的能力不一致。

rss · IT HOME · Jul 3, 23:57

**背景**: Claude Fable 5 是 Anthropic 迄今为止公开发布的最强模型，专为高要求的推理和长周期智能体任务（如大规模代码迁移和复杂实现）而构建。它属于“Mythos 级”模型，Anthropic 通过严格的安全训练和护栏设置使其能够安全地用于通用场景。AI 安全护栏是一种内置机制，旨在防止模型生成有害、带有偏见或未经授权的内容，但如果校准不当，可能会导致系统拒绝正常的请求，或触发向能力较弱的模型回退。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 和 X（前 Twitter）上，用户普遍表达了不满，指出 Fable 5 的安全护栏在大多数任务上都会生效，并强制降级到 Opus 4.8。评论者特别指出，这种体验下降并非因为使用了一个被禁用的模型版本，而是重新上架版本上新实施的限制措施存在问题。

**标签**: `#Anthropic`, `#Claude`, `#AI Safety`, `#Frontier Models`, `#LLM`

---

<a id="item-7"></a>
## [Google Gemini Omni Flash 登顶 Video Arena 榜首](https://x.com/Designarena/status/2072759122366509130) ⭐️ 8.0/10

Google DeepMind 新公开的视频生成模型 Gemini Omni Flash 以 1404 分登顶 Video Arena 盲测榜单。这标志着它以 101 分的显著优势击败了此前排名第一的字节跳动 Seedance 2.0 Mini。 这一成就标志着 Google 强势回归竞争激烈的 AI 视频生成赛道榜首，在能力上实现了对近期行业领导者的重大超越。其显著的领先优势展示了前沿多模态模型的重大进步，也加剧了 Google 与字节跳动在生成式 AI 领域的竞争。 Gemini Omni Flash 是一款高性能多模态模型，原生支持通过文本、图像和视频输入的组合进行高质量视频生成和对话式编辑。Video Arena 排行榜基于用户盲测投票生成，确保排名反映真实的人类偏好。

telegram · @zaihuapd · Jul 3, 05:51

**背景**: Video Arena 是一个评估平台，用户提交提示词后，观看顶级 AI 视频模型并排竞争，并为最佳结果投票以生成排行榜。字节跳动的 Seedance 系列一直是该领域的主导力量，其中 Seedance 2.0 采用了统一的多模态音视频联合生成架构。Google 此前的视频生成工作主要在 Veo 模型系列下进行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/">Start building with Nano Banana 2 Lite and Gemini Omni Flash</a></li>
<li><a href="https://arena.ai/video">Video Arena : Compare the Best AI Video Generators</a></li>
<li><a href="https://seed.bytedance.com/en/seedance2_0">Seedance 2.0</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#Google DeepMind`, `#Gemini`, `#Video Arena`, `#Generative AI`

---

<a id="item-8"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 已致信美国参议院银行委员会，指控阿里巴巴对 Claude AI 模型发动了迄今已知最大规模的蒸馏攻击。据指控，阿里巴巴在 2026 年 4 月 22 日至 6 月 5 日期间，利用约 2.5 万个欺诈账户与 Claude 进行了超过 2880 万次交互，以非法提取模型能力。 这一指控凸显了围绕 AI 知识产权保护的紧张局势不断升级，以及复制前沿 AI 能力的激烈地缘政治竞争。 alleged 攻击的规模引发了关于 API 安全性的严重关切，可能促使整个 AI 行业采取更强的监管和技术反制措施。 Anthropic 通过典型特征识别了此次攻击，包括集中在特定领域的大量查询、高度重复的结构，以及直接对应有价值的 AI 训练数据的内容。被指控方包括阿里巴巴及其 AI 研究实验室 Qwen，表明提取的数据可能用于加速其自身开源模型的开发。

telegram · @zaihuapd · Jul 3, 06:21

**背景**: 知识蒸馏是一种机器学习技术，通过让更小、更弱的模型（学生模型）学习更大、更强大模型（教师模型）的输出来复制其行为。虽然这是一种合法且广泛使用的模型压缩方法，但蒸馏攻击将这一概念武器化，通过利用目标模型的 API 大量收集输入输出对，成本仅为原始研发投入的一小部分。Anthropic、Google 和 OpenAI 都曾报告面临此类攻击，因为这种做法直接损害了构建最先进 AI 系统所需的大量资金和计算资源投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Anthropic`, `#Alibaba`, `#Model Distillation`, `#AI Industry`

---