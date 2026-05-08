---
layout: default
title: "Horizon Summary: 2026-05-08 (ZH)"
date: 2026-05-08
lang: zh
---

> From 103 items, 15 important content pieces were selected

---

1. [Natural Language Autoencoders: Turning Claude's Thoughts into Text](#item-1) ⭐️ 9.0/10
2. [Google DeepMind 的 AlphaEvolve 将 AI 驱动的发现扩展至多个领域](#item-2) ⭐️ 9.0/10
3. [Mozilla 借助 Claude Mythos 修复 423 个 Firefox 安全漏洞](#item-3) ⭐️ 9.0/10
4. [Anthropic 租用 xAI 的 Colossus 1 数据中心，达成标志性交易](#item-4) ⭐️ 9.0/10
5. [Anthropic 与 SpaceX 达成算力合作，Claude 使用限额翻倍](#item-5) ⭐️ 9.0/10
6. [OpenAI 发布 GPT-Realtime-2 API，带来高级语音推理能力](#item-6) ⭐️ 9.0/10
7. [小米开源 OmniVoice：支持 646 语种的零样本语音克隆 TTS 模型](#item-7) ⭐️ 8.5/10
8. [Triton v3.7.0 新增缩放批量矩阵乘法、FP8 常量及 Gluon 布局改进](#item-8) ⭐️ 8.0/10
9. [Antirez 发布 ds4：专为 Apple Metal 打造的 DeepSeek 推理引擎](#item-9) ⭐️ 8.0/10
10. [英伟达 CEO：下一代 AI 基础设施将用光学连接取代铜线](#item-10) ⭐️ 8.0/10
11. [清华系 AI Infra 厂商容芯致远完成数亿元融资，推出 GPU 核心架构](#item-11) ⭐️ 8.0/10
12. [Anthropic 成立 AI 研究院，聚焦 AI 社会影响研究](#item-12) ⭐️ 8.0/10
13. [腾讯混元 Hy3 Preview 登顶 OpenRouter 周榜](#item-13) ⭐️ 8.0/10
14. [OpenAI 发布新一代语音转录与语音合成模型](#item-14) ⭐️ 8.0/10
15. [OpenAI Codex 现已直接集成 Chrome 浏览器](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Natural Language Autoencoders: Turning Claude's Thoughts into Text](https://www.anthropic.com/research/natural-language-autoencoders) ⭐️ 9.0/10

Anthropic has released a new interpretability technique and corresponding open-weight models capable of translating the internal activations of major AI models into readable natural language text and back again.

hackernews · instagraham · May 7, 17:54 · [社区讨论](https://news.ycombinator.com/item?id=48052537)

**标签**: `#AI Interpretability`, `#Mechanistic Interpretability`, `#Anthropic`, `#AI Safety`, `#Open Source AI`

---

<a id="item-2"></a>
## [Google DeepMind 的 AlphaEvolve 将 AI 驱动的发现扩展至多个领域](https://deepmind.google/blog/alphaevolve-impact/) ⭐️ 9.0/10

Google DeepMind 扩展了 AlphaEvolve 的影响力，这是一款基于 Gemini 的进化式编程智能体，展示了其自主发现新算法和推进复杂数学与科学问题解决方案的能力。在最新进展中，AlphaEvolve 被用于改进 DeepConsensus——一个由 Google Research 开发的用于纠正 DNA 测序错误的模型——以及其他真实基础设施优化工作。 AlphaEvolve 代表了将 AI 作为自主智能体用于科学发现和算法优化的重大飞跃，其实际部署已在提升 Google 的数据中心、芯片设计和 AI 训练流程方面发挥作用。这表明大语言模型可以超越文本生成，在数学、基因组学和基础计算机科学领域推动切实的突破。 AlphaEvolve 采用由 Gemini 模型驱动的进化方法，迭代地提出、评估和改进基于代码的解决方案，以解决明确定义的问题。它已被应用于数学领域的开放性问题（包括 Erdős 问题）、矩阵乘法优化，以及如今的基因组学，优化后的算法已部署在 Google 基础设施的关键部分。

hackernews · berlianta · May 7, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48050278)

**背景**: AlphaEvolve 最初由 Google DeepMind 推出，是一种利用 Gemini 等大语言模型来设计高级算法的进化式编程智能体。与传统的编程助手不同，它通过生成候选程序、根据自动化指标进行评估，并在连续迭代中进化出更优解决方案来自主运行。该系统建立在 DeepMind 此前的工作（如 AlphaTensor 和 FunSearch）之上，将 AI 驱动的数学发现理念扩展到更广泛的科学和工程领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphaevolve-impact/">AlphaEvolve: Gemini-powered coding agent scaling impact ...</a></li>
<li><a href="https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/">AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms</a></li>
<li><a href="https://en.wikipedia.org/wiki/AlphaEvolve">AlphaEvolve - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，AlphaEvolve 在矩阵乘法和 Redis 优化等高度结构化、定义明确的问题空间中表现出色，反应不一，有人惊叹于其速度，也有人对其更广泛的适用性持怀疑态度。一些人提出了关于 Google API 可靠性的实际担忧（Vertex 上频繁出现 429 错误），并质疑 Google 内部员工是否更倾向于使用 Gemini 编程智能体而非 Claude Code 等替代方案。还有人反思了 AI 改进自身架构的深层含义，将其与技术奇点的概念联系起来。

**标签**: `#Google DeepMind`, `#AI Agents`, `#AI for Science`, `#Code Generation`, `#Frontier AI`

---

<a id="item-3"></a>
## [Mozilla 借助 Claude Mythos 修复 423 个 Firefox 安全漏洞](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla 工程师利用 Anthropic 的 Claude Mythos Preview 模型，结合自定义的模型驾驭技术，仅在 2026 年 4 月就识别并修复了 423 个 Firefox 安全漏洞——相比 2025 年每月约 20–30 个的基线水平出现了急剧飙升。发现的漏洞包括隐藏极深的问题，例如一个存在 20 年的 XSLT 漏和一个存在 15 年的 <legend> HTML 元素漏洞。 这代表了 AI 辅助安全研究的质的飞跃：直到最近，AI 生成的安全漏洞报告还被广泛视为低质量的'垃圾信息'，给开源维护者带来了不对称的成本负担。Mozilla 的成功表明，前沿 AI 模型在被正确驾驭的情况下，可以从制造噪音转变为大规模产出真正有价值的漏洞发现，有望改变主流软件项目进行安全加固的方式。 Mozilla 将这一突破归因于两个因素：模型能力的显著提升，以及在驾驭模型方面的技术大幅改进——包括引导、扩展和堆叠模型以生成有效信号并过滤噪音。许多 AI 生成的漏洞利用尝试已被 Firefox 现有的纵深防御措施所阻止，团队认为这验证了其当前安全架构的可靠性。

rss · Simon Willison · May 7, 17:56

**背景**: Claude Mythos Preview 是 Anthropic 迄今最先进的前沿大语言模型，于 2026 年 4 月作为 Project Glasswing 的一部分发布，仅向少数公司提供，未向公众开放。该模型在计算机安全任务方面表现尤为突出。在此之前，开源社区一直在应对大量低质量 AI 生成的漏洞报告——有时被称为'AI 垃圾信息'——像 cURL 的 Daniel Stenberg 等项目维护者将其描述为实质上是在用看似合理但实际错误的漏洞报告对开源项目发起 DDoS 攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/">cURL's Daniel Stenberg: AI slop is DDoSing open source - The New Stack</a></li>

</ul>
</details>

**社区讨论**: 该文章在 Lobste.rs 上被分享和讨论，社区注意到 AI 生成的漏洞报告从被视为垃圾信息转变为真正有用的工具，这一转变意义重大。许多 AI 发现的漏洞利用已被 Firefox 的纵深防御架构所缓解，这一发现被特别强调为令人安心，表明 AI 工具正在揭示那些负责任的工程实践已经部分覆盖的攻击面。

**标签**: `#AI Coding`, `#Cybersecurity`, `#Claude`, `#Mozilla Firefox`, `#Frontier AI`

---

<a id="item-4"></a>
## [Anthropic 租用 xAI 的 Colossus 1 数据中心，达成标志性交易](https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything) ⭐️ 9.0/10

在 2026 年 5 月 7 日 Anthropic 的 Code w/ Claude 活动上，该公司宣布与 SpaceX/xAI 达成协议，将使用位于孟菲斯的 Colossus 1 数据中心的全部容量。xAI 保留其更大的 Colossus 2 设施用于自身训练工作，而 Anthropic 则获得 Colossus 1 的独家使用权。 这笔交易标志着前沿 AI 算力格局的重大转变，两家此前互为竞争对手的领先 AI 实验室如今在基础设施层面展开合作，Elon Musk 本人也公开表示认可 Anthropic 的安全使命。在 Anthropic 被描述为严重受限于算力的当下，此举大幅扩展了其计算资源，可能重塑前沿 AI 模型开发的竞争格局。 Colossus 1 设施存在争议性的环境记录：EPA 裁定 xAI 非法运营了 35 台天然气涡轮机，而合法获批的仅有 15 台，其利用将设备归类为"临时"的漏洞规避了《清洁空气法》的要求。此外，在公告发布的前一晚，xAI 发布了仅提前两周通知的弃用公告，将关闭包括 Grok 4.1 Fast 在内的多款 Grok 模型，引发了开发者的强烈批评。

rss · Simon Willison · May 7, 17:09

**背景**: Colossus 是 xAI 位于孟菲斯南部前伊莱克斯厂址的超级计算机集群，于 2024 年 9 月启用，用于训练 Grok AI 模型。该设施的建设速度惊人——据报道从项目构想到准备开工仅用了 19 天，而行业平均水平为四年。此后 xAI 开始建设 Colossus 2，该设施被描述为全球首个吉瓦级数据中心，xAI 于 2025 年 3 月在孟菲斯收购了一处 100 万平方英尺的仓库及相邻地块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://winbuzzer.com/2026/01/20/epa-rules-xai-illegally-operated-gas-turbines-at-memphis-data-centers-closing-loophole-that-allowed-year-long-pollution-without-permits-xcxwbn/">EPA Rules xAI Illegally Operated Gas Turbines at Memphis Data ...</a></li>
<li><a href="https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter">xAI's Colossus 2 - First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise</a></li>

</ul>
</details>

**社区讨论**: 以反驳夸大的反数据中心言论而闻名的评论者 Andy Masley 明确表示不会选择在 Colossus 设施中运行计算任务。Simon Willison 指出，鉴于 AI 数据中心在政治上的敏感性，Anthropic 与这个特定数据中心合作是"非常糟糕的形象"，而最初的讨论错误地认为 xAI 将放弃自家的 Grok 模型——实际上 xAI 只是将训练转移到了更大的 Colossus 2。受到 xAI 突然关闭模型影响的开发者表达了强烈不满，有人表示"再也不会依赖你们的产品了"。

**标签**: `#AI Infrastructure`, `#Anthropic`, `#xAI`, `#Data Centers`, `#Frontier AI`

---

<a id="item-5"></a>
## [Anthropic 与 SpaceX 达成算力合作，Claude 使用限额翻倍](https://t.me/zaihuapd/41259) ⭐️ 9.0/10

Anthropic 已与 SpaceX 签署协议，将使用其位于田纳西州孟菲斯的 Colossus 1 AI 数据中心的全部算力，获得超过 22 万块 NVIDIA GPU 和超过 300 兆瓦的容量。作为直接成果，Anthropic 即日起将 Claude Code 所有付费方案的 5 小时速率限制翻倍，并大幅提高了 Claude Opus 的 API 速率限制。 这项合作标志着 Anthropic 算力基础设施的大规模扩张，直接改善了开发者和用户对 Claude 最先进模型的访问体验。该合作尤其引人注目，因为 SpaceX 的 Colossus 1 数据中心与竞争对手 xAI 相关联，这在竞争激烈的 AI 领域中是一次出人意料的跨公司协作。 Colossus 1 数据中心在一个月内可提供超过 300 兆瓦的新增容量，包含逾 22 万块 NVIDIA GPU。Claude Code 面向 Pro、Max、Team 和 Enterprise 用户的 5 小时速率限制已翻倍，Pro 和 Max 用户的高峰期限制也被完全取消。

telegram · @zaihuapd · May 7, 08:19

**背景**: Colossus 1 是位于田纳西州孟菲斯的大型 AI 数据中心，最初由 xAI（Elon Musk 的 AI 公司）建造，现归 SpaceX 所有。它是全球最大的 AI 训练和推理设施之一，旨在支持前沿 AI 模型的开发。AI API 和 Claude Code 等编码工具通常会设置速率限制以管理有限的算力资源，扩展基础设施使提供商能够提高这些限制。Claude Code 是 Anthropic 的终端智能编程工具，Claude Opus 则是其用于复杂任务的最强模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html">Anthropic, SpaceX announce compute deal, includes space ...</a></li>
<li><a href="https://www.engadget.com/2166315/anthropic-is-doubling-claude-code-rate-limits-after-deal-with-spacex/">Anthropic is doubling Claude Code rate limits after deal with SpaceX - Engadget</a></li>
<li><a href="https://www.msn.com/en-us/news/other/anthropic-secures-full-use-of-spacexs-colossus-1-data-center/gm-GML9F02A91">Anthropic secures full use of SpaceX's Colossus 1 data center</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI Infrastructure`, `#SpaceX`, `#Claude`, `#Compute`

---

<a id="item-6"></a>
## [OpenAI 发布 GPT-Realtime-2 API，带来高级语音推理能力](https://twitter.com/sama/status/tweet-2052462271667028211) ⭐️ 9.0/10

Sam Altman 宣布 GPT-Realtime-2 现已在 OpenAI API 中上线，被称为语音 AI 交互领域的一次重大飞跃。该模型是 OpenAI 首个被描述为具备"GPT-5 级别推理能力"的语音模型，使实时语音代理能够在对话过程中倾听、推理并解决复杂问题。 此次发布标志着多模态 AI 的重大进步，首次将复杂的推理能力引入实时语音交互。它预示着用户与 AI 交互方式的转变——从基于文本的提示转向自然的语音对话，尤其是在需要大量上下文的复杂任务场景中。 GPT-Realtime-2 支持可配置的推理力度，但更高的推理力度可能会增加延迟和输出 token 的使用量。与此同时，OpenAI 还发布了 GPT-Realtime-Translate 和 GPT-Realtime-Whisper，作为 API 中全新音频能力组合的一部分。

twitter · Sam Altman · May 7, 18:55

**背景**: OpenAI 的 Realtime API 专为需要低延迟的实时音频交互而设计，能够直接处理音频流并在对话轮次之间保持会话状态，响应时间约为 200-300 毫秒。此前的实时语音模型缺乏 OpenAI 最新文本模型的深度推理能力，导致用户通过文本和语音能够完成的任务之间存在差距。GPT-Realtime-2 通过将高级推理能力引入语音代理来弥合这一差距，使其成为真正的实时协作者，而不仅仅是简单的语音应答器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/gpt-realtime-2">GPT-Realtime-2: A Voice Model with GPT-5-Class Reasoning</a></li>
<li><a href="https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/">Advancing voice intelligence with new models in the API | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-2">gpt-realtime-2 Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Voice AI`, `#GPT-Realtime`, `#Multimodal AI`, `#API Release`

---

<a id="item-7"></a>
## [小米开源 OmniVoice：支持 646 语种的零样本语音克隆 TTS 模型](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 8.5/10

小米 AI Lab 旗下的 k2-fsa 团队正式开源了 OmniVoice，这是一个大规模多语言零样本文本转语音模型，采用极简双向 Transformer 架构，支持 646 种语言的语音克隆。该模型基于 50 个开源数据集构建的 58 万小时训练集进行训练，训练代码、推理代码及模型权重均已公开。 OmniVoice 代表了前沿语音 AI 领域的一项重大开源进展，在 24 种测试语言中超越了商用系统，在 102 种语言中接近真人语音水平。其完全开源的特性使高质量多语言语音克隆技术得以普及，全球的研究人员和开发者都可以使用，包括用于低资源和濒危语言。 OmniVoice 的性能得益于两项关键技术创新：全码本随机掩蔽策略，相比传统的逐层掩蔽方法提高了训练效率和模型收敛速度；以及利用大型预训练 LLM 权重进行初始化，注入强大的语言先验知识以提升可懂度。该模型实现了每天 10 万小时的训练速度和 40 倍实时的 PyTorch 推理速度，词错率（WER）仅为 0.84%。

telegram · @zaihuapd · May 7, 10:06

**背景**: 零样本文本转语音（TTS）是一种技术，模型只需几秒钟的参考音频就能克隆并合成某个人的声音，无需针对该特定声音进行微调。传统 TTS 系统通常依赖复杂的多阶段流水线，先生成中间声学特征再转换为波形，这会引入瓶颈。OmniVoice 通过单阶段架构简化了这一过程，使用双向 Transformer 将文本直接映射到多码本声学 token，类似于 BERT 双向处理语言的方式。全码本随机掩蔽方法受掩码语言建模启发，允许模型同时而非顺序地预测所有声学 token 层，从而大幅提升效率和合成质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2604.00688">OmniVoice: Omnilingual Zero-Shot TTS</a></li>
<li><a href="https://www.aibase.com/news/26962">Xiaomi Open Sources Major Project! OmniVoice Covers 600+ Languages for Zero-Shot Speech Cloning TTS: WER Only 0.84%, 40 Times Faster, Small Languages Can Also Be Resurrected Easily</a></li>
<li><a href="https://www.communeify.com/en/blog/omnivoice-tts-600-languages-zero-shot-voice-cloning-guide/">OmniVoice: The Leading Zero-Shot TTS Model Supporting 600+ Languages | Communeify</a></li>

</ul>
</details>

**标签**: `#Text-to-Speech`, `#Voice Cloning`, `#Open Source AI`, `#Multilingual AI`, `#Xiaomi AI`

---

<a id="item-8"></a>
## [Triton v3.7.0 新增缩放批量矩阵乘法、FP8 常量及 Gluon 布局改进](https://github.com/triton-lang/triton/releases/tag/v3.7.0) ⭐️ 8.0/10

Triton 语言和编译器发布了 v3.7.0 版本，引入了缩放批量矩阵乘法（BMM）、直接创建 FP8 常量以及 tl.squeeze 和 tl.unsqueeze 等新前端特性。该版本还带来了重要的后端改进，包括 LLVM 更新、增强的 2CTA/多播/TMA 支持、AMD/HIP 后端的显著进展，以及用于更好 GPU 内核优化的 Gluon 布局改进。 Triton 是 PyTorch 为 AI 工作负载生成高度优化 GPU 内核的主要后端，是 AI 基础设施的关键组成部分。该版本通过支持更低精度的 FP8 运算、更快的批量矩阵乘法以及通过 AMD/HIP 增强实现的多厂商 GPU 支持，直接影响前沿 AI 模型训练和运行的效率与能力。 值得注意的技术新增包括用于树外 TTIR/TTGIR pass 的插件钩子和 Triton 方言插件、带有跨目标防护的可选设备预加载参数，以及支持广播的 tl.cat 非重排变体。该版本还包含多次 LLVM 升级及稳定性修复、通过预计算 inspect.signature 和惰性元组类型计算减少前端 JIT 开销，以及对旧版 make_block_ptr API 的弃用警告。

github · triton-lang/triton · May 7, 22:19

**背景**: Triton 是一个开源的 GPU 编程语言和编译器，提供基于 Python 的环境来编写能够在现代 GPU 硬件上以接近最大吞吐量运行的自定义深度学习计算内核。它旨在提供比编写原始 CUDA 代码更高的生产力，同时保持比其他领域特定语言更大的灵活性，是 AI 编译栈中的关键层。FP8（8 位浮点）是一种新兴的低精度格式，可显著减少大语言模型训练和推理的内存消耗和计算需求。Triton 中的 Gluon 布局系统赋予开发者对数据布局决策的显式控制权，防止编译器执行可能干扰手工调优性能优化的自动布局传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/triton-lang/triton">GitHub - triton-lang/triton: Development repository for the ...</a></li>
<li><a href="https://triton-lang.org/main/index.html">Welcome to Triton’s documentation! — Triton documentation</a></li>
<li><a href="https://www.lei.chat/posts/gluon-explicit-performance/">Gluon : Explicit Performance | Lei.Chat()</a></li>

</ul>
</details>

**标签**: `#Triton`, `#AI Infrastructure`, `#GPU Programming`, `#Compilers`, `#Open Source`

---

<a id="item-9"></a>
## [Antirez 发布 ds4：专为 Apple Metal 打造的 DeepSeek 推理引擎](https://github.com/antirez/ds4) ⭐️ 8.0/10

Redis 的创造者 Antirez 发布了 'ds4'，这是一个高度优化的本地推理引擎，专门设计用于通过 Apple 的 Metal GPU API 在 Apple Silicon 上运行 DeepSeek 模型。该项目是开源的，专注于在基于 Metal 的硬件上最大化 DeepSeek 的推理性能。 该项目凸显了一个日益增长的趋势：开发者利用最先进的 AI 编程助手来编写高度优化的、特定硬件的推理内核，从而突破消费级硬件上本地 AI 性能的极限。它证明了与 llama.cpp 等通用框架相比，针对单一模型的专注优化可以带来显著的性能提升。 在全速 token 生成期间，该引擎在 MacBook M3 Max 上的功耗峰值仅为 50W，展现了出色的能效表现。然而，在没有缓存的情况下，处理大型输入（约 25k tokens）的初始提示可能需要大约 4 分钟，这对于交互式使用场景来说是一个值得注意的限制。

hackernews · tamnd · May 7, 15:40 · [社区讨论](https://news.ycombinator.com/item?id=48050751)

**背景**: Metal 是 Apple 的底层低开销硬件加速图形和计算 API，旨在为 Apple 平台上的图形和计算任务提供紧密集成。DeepSeek 是一系列强大的开源语言模型，其中 DeepSeek-V3 是一个拥有 671B 参数的混合专家（MoE）模型，每个 token 激活 37B 参数，采用了多头潜在注意力（MLA）等创新架构。本地推理引擎允许用户直接在自己的硬件上运行 AI 模型，无需依赖云服务即可实现更快速、私密且经济的模型执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/metal/">Metal Overview - Apple Developer</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek-ai/DeepSeek-V3 · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metal_(API)">Metal (API) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该项目表示了热情，多位开发者分享了使用 Claude 等 AI 助手优化专用推理引擎的类似经验。一位评论者指出了数月内专注于单一模型优化的潜力，而另一位则指出大型输入的预填充时间过长是一个实际问题，不过缓存机制可以在常规使用模式下缓解这一问题。

**标签**: `#DeepSeek`, `#Local Inference`, `#Apple Silicon`, `#Metal`, `#Open Source AI`

---

<a id="item-10"></a>
## [英伟达 CEO：下一代 AI 基础设施将用光学连接取代铜线](https://36kr.com/newsflashes/3799989766429697?f=rss) ⭐️ 8.0/10

英伟达 CEO 黄仁勋表示，下一代人工智能基础设施将需要大规模扩展光学连接，因为传统铜线已无法满足快速增长的计算需求。他重点强调了英伟达与康宁公司达成的多年合作项目，旨在大幅扩展美国本土先进光学连接解决方案的制造能力。 从铜线向光学互连的转变代表了 AI 数据中心根本性的架构变革，将决定前沿 AI 模型能够扩展到何种程度。英伟达与康宁的合作可能达到 32 亿美元的股权敞口，标志着一项大规模的产业投资，将重塑 AI 基础设施供应链，并在建筑、制造和技术工种等领域创造广泛的经济需求。 康宁正在美国开设三家全新的先进制造工厂，专门为英伟达生产光学技术产品，分别位于北卡罗来纳州和德克萨斯州。该合作针对 AI 集群互连的无源光纤层，以支持 AI 工厂内部 GPU 网络的纵向和横向扩展，业界预测所有高带宽 AI 数据中心互连可能在五年内全部转为光学连接。

rss · 36kr · May 8, 01:49

**背景**: 在当前的 AI 数据中心中，铜缆由于成本较低且生态系统成熟，一直是机架内 GPU 与交换机之间短距离连接的主要互连介质。然而，随着 AI 集群扩展到数万个 GPU 的规模，铜线在带宽、传输距离和功耗方面面临根本性的物理限制——光纤成为 3 米以上连接的首选方案，可提供显著更高的带宽和更低的延迟。共封装光学（CPO）和有源光缆（AOC）等技术正在推动这一转型，将光学引擎与 GPU 和交换机直接耦合，从根本上改变数据中心和芯片架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2026/05/nvidia-and-corning-announce-long-term-partnership-to-strengthen-us-manufacturing-for-ai-infrastructure.html">NVIDIA and Corning Announce Long-Term Partnership To ...</a></li>
<li><a href="https://hightoweradvisors.com/blogs/well-th-blog/copper-vs-optical-in-the-ai-infrastructure-buildout">Copper vs Optical in the AI Infrastructure Buildout</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#NVIDIA`, `#Optical Interconnects`, `#Data Centers`, `#Hardware`

---

<a id="item-11"></a>
## [清华系 AI Infra 厂商容芯致远完成数亿元融资，推出 GPU 核心架构](https://36kr.com/p/3799984046333186?f=rss) ⭐️ 8.0/10

清华系 AI 基础设施初创企业容芯致远近日完成天使轮数亿元融资，由北京绿色能源和低碳产业基金与赛富投资基金领投，旨在推进其以 GPU 为核心的 AGC 计算体系架构，将 GPU 与 CPU 比例从传统的约 2:1 提升至 20:1 甚至 32:1。 该架构通过大幅提升 GPU 利用率、实现多达 64 个 GPU 的统一内存地址空间共享，并兼容国产 CPU 和 GPU，直接解决大模型训练与推理中的关键瓶颈，是一项重要的全栈系统级创新，有望重塑 AI 数据中心的成本结构并加速国产算力生态发展。 核心技术亮点包括：自研 AI BMC 系统将传统 3–5 秒级轮询提升至微秒级响应；GPU RAID 机制实现故障热插拔，将维护时间从约 2 小时压缩至约 1 分钟；Blue Link 光互连方案采用 Mini LED/MICRO LED 替代传统激光光模块；以及约 10TB 混合存储空间用于 KV Cache 冗余缓存。

rss · 36kr · May 8, 01:45

**背景**: 传统数据中心服务器架构以 CPU 为中心，CPU 负责数据调度和 GPU 间通信，在 AI 工作负载需要大规模 GPU 集群时成为瓶颈。传统配置中 GPU 与 CPU 比例约为 2:1，意味着 GPU 扩展时 CPU 数量也需同步增加，导致系统复杂度和成本显著上升。GPU 间通信瓶颈以及无法在多个 GPU 间共享统一内存地址空间进一步限制了整体算力利用率，因此系统级架构重构成为 AI 时代的关键需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.09874">[2409.09874] The Landscape of GPU - Centric Communication</a></li>
<li><a href="https://www.techpowerup.com/348800/amd-says-agentic-ai-could-put-more-cpus-than-gpus-in-compute-nodes">AMD Says Agentic AI Could Put More CPUs Than GPUs in Compute...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#GPU Architecture`, `#Hardware`, `#Datacenter`, `#Tsinghua`

---

<a id="item-12"></a>
## [Anthropic 成立 AI 研究院，聚焦 AI 社会影响研究](https://www.ithome.com/0/947/500.htm) ⭐️ 8.0/10

Anthropic 于 2026 年 5 月 7 日宣布成立 AI 研究院（The Anthropic Institute，TAI），主要研究 AI 对社会的影响，聚焦经济扩散、威胁与心理弹性、现实环境 AI 系统和 AI 驱动研发四大方向。该研究院还将邀请外部学者成为 TAI 研究员，参与为期四个月的指导研究项目。 这一举措表明，作为领先的前沿 AI 实验室，Anthropic 正在将其对 AI 社会影响的理解和缓解工作制度化，这可能影响行业实践和政府政策制定。通过可能公开原本内部的诸如经济指标等数据，TAI 能够为外部组织、政府和公众提供有价值的实证依据，帮助他们在 AI 开发方面做出更明智的决策。 TAI 的研究将直接影响 Anthropic 的内部决策，可能改变公司发布技术的方式以及对外分享的数据内容。其研究员项目为合格参与者提供为期四个月的指导，有机会在 Anthropic 团队成员的指导下研究多个课题。

rss · IT HOME · May 8, 01:24

**背景**: Anthropic 是全球领先的前沿 AI 公司之一，以开发 Claude 系列 AI 模型和对 AI 安全研究的重视而闻名。随着 AI 系统能力不断增强并被广泛部署，关于其经济替代效应、安全威胁、对人类心理的影响以及对科学研发的加速作用等担忧在学术界、产业界和政府中日益增长。成立专门研究院反映了主要 AI 实验室主动研究和应对其技术社会影响的更广泛趋势。

**标签**: `#Anthropic`, `#AI Safety`, `#AI Governance`, `#Societal Impact`, `#AI Research`

---

<a id="item-13"></a>
## [腾讯混元 Hy3 Preview 登顶 OpenRouter 周榜](https://finance.sina.com.cn/tech/shenji/2026-05-07/doc-inhwzrtp8521239.shtml) ⭐️ 8.0/10

腾讯混元 Hy3 preview 模型于 2026 年 4 月 23 日上线，仅两周内 Token 调用总量就超过了上一代模型 Hy2 的十倍以上。该模型在 OpenRouter 平台周榜的总榜和市场占有率均排名第一，编程与工具调用场景同样位列榜首。 爆发式的采用量表明 Hy3 preview 正成为极具竞争力的前沿模型，尤其在编程和智能体等对企业 AI 应用日益关键的场景中表现突出。它在拥有数百万开发者的第三方模型路由平台 OpenRouter 上迅速获得关注，证明了其在腾讯自身生态系统之外的强大市场认可度。 Hy3 preview 是一个 295B 参数的混合专家（MoE）模型，仅有 21B 活跃参数和 3.8B MTP 层参数，具有出色的成本效率。在腾讯 WorkBuddy、Codebuddy 及 QClaw 等应用中的调用量增幅超过 16.5 倍，团队在上线初期于 OpenRouter 开启限免以收集真实场景反馈，为后续迭代提供方向。

telegram · @zaihuapd · May 7, 05:34

**背景**: 混元是腾讯 AI 研究部门开发的旗舰大语言模型系列。Hy3 preview 融合了快思考和慢思考能力，旨在增强推理和智能体工作流。OpenRouter 是一个统一的 API 平台，通过单一标准化接口为开发者提供来自不同提供商的 300 多个 AI 模型访问，全球用户超过 420 万。WorkBuddy、Codebuddy 和 QClaw 是腾讯的桌面及办公 AI 助手，利用混元模型完成代码处理、数据分析和文档整理等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">GitHub - Tencent-Hunyuan/Hy3-preview: Hy3 preview (295B A21B), a leading reasoning and agent model in its size, with great cost efficiency</a></li>
<li><a href="https://www.tencent.com/en-us/articles/2202320.html">Tencent Unveils Hy3 preview; Model Enhances Agent Capabilities and Real-World Usability</a></li>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#Hunyuan`, `#LLM`, `#OpenRouter`, `#AI Agents`

---

<a id="item-14"></a>
## [OpenAI 发布新一代语音转录与语音合成模型](https://t.me/zaihuapd/41269) ⭐️ 8.0/10

OpenAI 发布了三款全新音频模型：用于语音转文本的 gpt-4o-transcribe 和 gpt-4o-mini-transcribe，以及用于文本转语音的 gpt-4o-mini-tts。这些模型支持通过自然语言指令控制语音合成效果，并在口音处理、嘈杂环境鲁棒性和减少幻觉方面相比此前的 Whisper 模型有显著提升。 这些升级标志着语音 AI 领域的重要进步，使开发者能够构建更自然、更可控且转录准确率更高的语音应用。在口音和噪声处理方面的改进，使这些模型在客服、媒体和无障碍工具等行业中更具实际多语言部署价值。 gpt-4o-mini-tts 模型的输入上限为 2,000 个 token，定价为每百万输入 token 0.60 美元、每百万输出 token 10.00 美元。虽然新的转录模型显著减少了幻觉并改善了词错误率，但某些语言的错误率仍然较高，且由于模型规模较大，OpenAI 此次未将其开源。

telegram · @zaihuapd · May 7, 17:19

**背景**: OpenAI 此前的语音识别工作基于 Whisper 模型系列，该系列虽被广泛采用，但在处理带口音的语音、嘈杂环境以及转录幻觉（即模型生成看似合理但实际不正确的文本）方面存在不足。新的 gpt-4o-transcribe 模型基于 GPT-4o 架构构建，利用其多模态能力实现了更好的语言识别和准确率。文本转语音（TTS）技术将书面文本转换为语音音频，而新的 gpt-4o-mini-tts 允许开发者使用自然语言提示词来指定说话风格，超越了传统的参数化语音控制方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-4o-mini-tts">GPT-4o mini TTS Model | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-4o-transcribe">GPT - 4 o Transcribe Model | OpenAI API</a></li>
<li><a href="https://cloudprice.net/models/openai-gpt-4o-mini-tts">GPT-4o mini TTS pricing & specs — OpenAI | CloudPrice</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#speech-recognition`, `#text-to-speech`, `#gpt-4o`, `#voice-AI`

---

<a id="item-15"></a>
## [OpenAI Codex 现已直接集成 Chrome 浏览器](https://twitter.com/sama/status/tweet-2052482715010949288) ⭐️ 8.0/10

OpenAI 宣布其 Codex AI 编程助手现可在 macOS 和 Windows 上的 Chrome 浏览器中直接运行，使其能够更高效地与网页应用和网站进行交互。这标志着 Codex 的计算机使用能力从最初仅支持 macOS 桌面端扩展到了跨平台的浏览器集成。 此次集成标志着 Codex 从纯粹的代码生成工具向能够操作真实软件界面的全能 AI 代理迈出了重要一步。通过直接在 Chrome 中工作，Codex 现在可以自动化复杂的基于网页的工作流程，极大地扩展了其对依赖浏览器工具的开发者和知识工作者的实用价值。 计算机使用功能最初于 2026 年 4 月 16 日发布，仅支持 macOS，用户需要安装计算机使用插件并授予屏幕录制和辅助功能权限。此次 Chrome 集成将该功能扩展到了 Windows 平台，但欧洲经济区、英国和瑞士等部分地区在发布时可能仍有限制。

twitter · Sam Altman · May 7, 20:16

**背景**: OpenAI Codex 是一套 AI 驱动的编程代理工具，旨在自动化软件工程任务，如构建功能、复杂重构和迁移。Codex 最初以 CLI 工具和 IDE 插件的形式提供，支持 VS Code 等编辑器，后来发展为基于云的应用，作为代理式编程的指挥中心。2026 年 4 月推出的计算机使用功能是一个里程碑式的升级，将 Codex 从能够编写代码提升到能够操作计算机，使其与 Anthropic 和 GitHub Copilot 的类似产品形成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/codex/app/computer-use">Computer Use – Codex app | OpenAI Developers</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/openai-codex-for-almost-everything-2026">OpenAI Codex 2026: Computer Use , Memory & Full Review</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI Agents`, `#Browser Integration`, `#Web Automation`

---