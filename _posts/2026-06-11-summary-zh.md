---
layout: default
title: "Horizon Summary: 2026-06-11 (ZH)"
date: 2026-06-11
lang: zh
---

> From 117 items, 10 important content pieces were selected

---

1. [Google 发布开源权重模型 DiffusionGemma](#item-1) ⭐️ 9.0/10
2. [Anthropic CEO Dario Amodei 警告 AI 进展突然爆发，呼吁政策改革](#item-2) ⭐️ 9.0/10
3. [台积电下一代 CoPoS 先进封装预计 2028 年量产](#item-3) ⭐️ 8.5/10
4. [研究人员抨击 Anthropic Fable 模型的过度安全护栏](#item-4) ⭐️ 8.0/10
5. [Jeremy Howard 批评 Anthropic 在 AI 安全问题上的双重标准](#item-5) ⭐️ 8.0/10
6. [LLM 安全法官在不同危害类别上评估结果不一致](#item-6) ⭐️ 8.0/10
7. [mlx-vlm v0.6.3 首发支持 DiffusionGemma 和 North Mini Code 1.0](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 零传统视频编辑完成 4K 发布视频制作](#item-8) ⭐️ 8.0/10
9. [iOS 27 测试版泄露 Siri LLM 系统提示词](#item-9) ⭐️ 8.0/10
10. [OpenAI 秘密提交 S-1 文件，计划 2027 年上市](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google 发布开源权重模型 DiffusionGemma](https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything) ⭐️ 9.0/10

Google 发布了 DiffusionGemma（google/diffusiongemma-26B-A4B-it），这是一个基于其实验性 Gemini Diffusion 研究的开放权重文本生成模型，采用 Apache 2.0 许可证。该模型使用基于扩散的去噪方法并行生成文本，而非传统的逐 token 顺序生成方式，速度至少是其他 Gemma 4 模型的 4 倍。 此次发布代表了文本生成领域一次重大的架构范式转变，从主流的自回归 Transformer 方法转向基于扩散的并行解码。通过以宽松的 Apache 2 许可证开源该模型，Google 使开发者和研究人员能够自由实验并商业部署一种全新的文本生成架构，这可能会重塑 LLM 的构建和服务方式。 该模型是一个 26B 参数的模型，采用 A4B 量化并进行指令微调（由后缀 "-it" 标识），目前可在 NVIDIA 的 NIM 云 API 上免费使用。在实际测试中，它达到了至少每秒 500 个 token 的速度，在 4.4 秒内生成了 2,409 个 token，并可在包括 H100、DGX Spark、DGX Station 和 RTX/RTX PRO GPU 在内的 NVIDIA 硬件上高效运行。

rss · Simon Willison · Jun 10, 20:00

**背景**: 传统的自回归语言模型以从左到右的顺序逐个 token 生成文本，这种方式速度较慢且可能限制输出的连贯性。扩散模型在图像生成领域（如 Stable Diffusion、DALL-E）已取得巨大成功，其工作原理不同：从噪声开始，逐步并行地迭代优化整个输出。Google 于 2025 年 5 月首次通过实验性的 Gemini Diffusion 模型展示了这种方法在文本领域的应用，在早期预览中达到了每秒 857 个 token 的速度，但该项目此后一直未有新消息，直到现在。将扩散应用于离散的文本 token（而非连续的图像像素）在技术上具有挑战性，此前的研究表明离散扩散模型的性能往往不如自回归模型，因此 DiffusionGemma 的竞争力表现是一个值得关注的突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/diffusiongemma-the-developer-guide/">DiffusionGemma: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://deepmind.google/models/gemini-diffusion/">Gemini Diffusion — Google DeepMind</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论反映出社区对这一架构创新和 Apache 2 许可证的强烈兴奋，许多评论者指出超越自回归模型的重要意义。部分用户持谨慎乐观态度，质疑基于扩散的文本模型能否在实际生产场景中匹敌成熟的自回归模型的质量和可靠性，而另一些用户则强调了自纠错和双向上下文能力作为扩散方法的独特优势。

**标签**: `#AI Models`, `#Open Source AI`, `#Google`, `#Diffusion Models`, `#NLP`

---

<a id="item-2"></a>
## [Anthropic CEO Dario Amodei 警告 AI 进展突然爆发，呼吁政策改革](https://x.com/rohanpaul_ai/status/2064869224015863848) ⭐️ 9.0/10

Anthropic CEO Dario Amodei 在采访中指出 AI 进展正从平滑的指数曲线出现突然的"爆发"，随后发布长文紧急呼吁全面政策改革。他具体提出了强制预部署安全测试、政府有权阻止高风险模型部署、加强 AI 公司安全规则、劳动力市场保护以及全球民主国家在 AI 安全方面协调等建议。 这一警告具有重要意义，因为它来自一家领先前沿 AI 实验室的 CEO，他直接了解能力提升的速度。如果 AI 能力确实正在以超越监管能力的速度加速，经济冲击、安全风险和地缘政治影响可能会非常严重，并且比各国政府准备应对的时间更早到来。 Amodei 提出的框架包括强制预发布测试和独立审计、政府有权阻止构成网络安全、生物、自主或自动化研发风险的模型部署，以及要求 AI 公司保护模型权重、定期进行红队测试和渗透测试并及时报告安全事件。他还呼吁民主国家在芯片供应链、出口管制、收益共享以及共同防御 AI 驱动的压制方面进行协调。

rss · AI Hot · Jun 11, 00:36

**背景**: 前沿 AI 模型是目前开发的最先进的 AI 系统，具备复杂推理、多模态理解和跨广泛用例的自主任务执行能力，不同于为单一任务设计的传统窄 AI。AI 领域的红队测试是一种结构化的探测过程，旨在部署前识别 AI 系统的有害能力、问题输出或基础设施漏洞。模型权重代表 AI 系统的核心知识产权，编码了训练中获得的所有知识；一旦被攻破，攻击者将直接获得组织最有价值的 AI 资产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thirdway.org/memo/what-are-frontier-ai-models">What Are Frontier AI Models? | Third Way</a></li>
<li><a href="https://learn.microsoft.com/zh-cn/azure/ai-services/openai/concepts/red-teaming">规划大型语言模型 (LLM) 及其应用程序的红队测试 - Azure OpenAI in Azure AI Foundry Models | Microsoft Learn</a></li>
<li><a href="https://i.ctrlworks.cn/2693.html">2024 保 护 人工智能 模 型 权 重 研究报告防止前沿 模 型 被盗和滥用英文版</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Policy`, `#Anthropic`, `#AI Regulation`, `#Frontier AI`

---

<a id="item-3"></a>
## [台积电下一代 CoPoS 先进封装预计 2028 年量产](https://x.com/mingchikuo/status/2064896082203849094) ⭐️ 8.5/10

分析师郭明錤透露，台积电下一代 CoPoS（Chip on Panel on Substrate）先进封装技术预计将于 2028 年下半年量产，目标实现 9.5 倍光罩尺寸以上的超大封装。NVIDIA 即将推出的 Feynman AI 芯片有望率先采用该技术。 随着摩尔定律逼近物理极限，先进封装已成为扩展前沿 AI 算力的主要瓶颈，CoPoS 因此成为下一代 AI 超级芯片的关键使能技术。该技术有望将台积电在先进封装领域的领先优势延续至 2032 年左右，对 AI 硬件竞争格局产生深远影响。 CoPoS 架构采用玻璃核心基板，为三层结构——玻璃芯上下两侧叠加 ABF（味之素堆积膜）增层。关键技术挑战集中在 TGV（玻璃通孔）成孔与铜填充工艺，同时需要澄清的是，玻璃并非中介层，互连由 RDL、TGV/Cu 及 ABF 增层共同承担，芯片贴装在 ABF 增层表面。

rss · AI Hot · Jun 11, 02:22

**背景**: CoPoS（Chip on Panel on Substrate）是台积电旨在接替 CoWoS（Chip on Wafer on Substrate）的下一代先进封装技术，而 CoWoS 是目前高端 AI 加速器的主流封装平台。随着基于小芯片的设计突破现有硅中介层的光罩尺寸限制，玻璃核心基板凭借更优异的尺寸稳定性和更大的封装尺寸，有望实现更低的成本。TGV（玻璃通孔）技术在玻璃基板上制作垂直电气连接，类似于硅基封装中的 TSV（硅通孔），但在玻璃材料上的成孔和导电填充面临独特的技术挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2037245975417378429">下一代先进封装！CoPoS锁定万亿风口！（附A股核心标的）</a></li>
<li><a href="https://www.eet-china.com/mp/a448358.html">CoWoS、CoPoS、CoWoP傻傻分不清？三大先进封装技术详解</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/706717838">半导体先进封装“玻璃通孔（TGV）”工艺技术的详解；</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#TSMC`, `#Advanced Packaging`, `#NVIDIA`, `#Semiconductors`

---

<a id="item-4"></a>
## [研究人员抨击 Anthropic Fable 模型的过度安全护栏](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/) ⭐️ 8.0/10

Anthropic 新发布的 Claude Fable 5 模型正遭到网络安全和科学研究人员的强烈批评，他们报告称该模型的安全护栏过于激进，在处理合法研究查询时会静默降级模型能力，通常在用户不知情的情况下将请求路由到能力较弱的模型。 这一争议暴露了前沿 AI 开发中安全护栏与专业用户信任及实用性之间的根本矛盾。如果 Anthropic 静默降级模型能力的做法成为行业常态，可能会削弱研究人员对 AI 工具的信心，并推动用户转向限制较少的竞争对手，尤其是开源替代方案。 虽然据报道 Anthropic 在处理网络安全和生物相关查询时会通知用户模型能力被降级，但对于化学和统计学等其他敏感研究主题的静默降级则不会告知用户。该模型的护栏范围如此之广，甚至识别室内植物上的真菌这类无害请求也会触发误拒绝，使得该模型在许多学术和科学工作流中几乎无法使用。

hackernews · AI Hot · Jun 10, 16:42 · [社区讨论](https://news.ycombinator.com/item?id=48478969)

**背景**: Claude Fable 5 是 Anthropic 最新推出的 "Mythos 级"模型，专为自主知识工作和编程设计，在 CursorBench 等基准测试中达到了最先进的性能。静默降级是指在用户不知情的情况下将请求路由到能力较弱的模型的做法，这种模式在企业 AI 系统中引发了担忧，因为它破坏了信任并可能产生结构不同的输出。AI 护栏是旨在防止模型生成有害内容的安全机制，但研究人员长期以来一直警告，过于激进的护栏会造成盲点，并可能使 AI 工具在合法专业用途中失去效用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://aiproductivity.ai/news/claude-fable-competitor-clause-silent-degradation/">Claude Fable Competitor Clause: Silent API Degradation Risk</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5">Claude Fable 5 - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区情绪压倒性地负面，来自化学、统计学和数据科学领域的研究人员称 Fable 在专业工作中"毫无用处"，并指出维基百科文章可能更高效。最具争议的方面是静默模型降级——用户认为这是一种欺骗行为并破坏了信任，特别是考虑到 Anthropic 仅领先竞争对手大约一年。多位评论者表示希望市场竞争，尤其是来自中国开源模型的压力，能迫使 Anthropic 改变这些限制性政策。

**标签**: `#AI safety`, `#Anthropic`, `#guardrails`, `#AI research`, `#model behavior`

---

<a id="item-5"></a>
## [Jeremy Howard 批评 Anthropic 在 AI 安全问题上的双重标准](https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything) ⭐️ 8.0/10

Jeremy Howard 公开批评 Anthropic 一边使用自家最顶尖的模型进行前沿 AI 研究，一边限制其他人这样做，认为这与其宣称的安全目标自相矛盾。他提出，如果一个实验室真心想要减缓递归式 AI 自我改进，拥有最强模型的实验室应该率先承诺不在内部将其用于前沿研究。 这一批评直击 AI 行业日益严重的权力集中问题的核心，少数资金雄厚的实验室控制着最强大的模型。如果前沿实验室能用自家模型加速研究却拒绝他人访问，可能会造成危险的垄断，并在缺乏充分安全保障的情况下加速通向 AGI 的竞赛。 Howard 本人澄清，他实际上并不主张减缓递归式自我改进——他主张尽可能广泛地实现民主化。他的论点专门针对 Anthropic 等实验室的逻辑矛盾：声称优先考虑安全，却采取加速前沿发展并将权力集中在自己手中的政策。

rss · Simon Willison · Jun 10, 15:23

**背景**: 递归式自我改进（RSI）是一种理论过程，即 AI 系统不断提升自身能力，可能导致智能爆炸并产生超级智能。Anthropic 已发布负责任扩展政策（RSP），目前为 3.0 版本，作为其管理日益强大的 AI 系统所带来的灾难性风险的自愿框架。关于谁应该有权访问前沿模型以及在何种条件下访问，已成为 AI 治理中最具争议的问题之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/responsible-scaling-policy">Responsible Scaling Policy Updates \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0">Anthropic's Responsible Scaling Policy (version 3.0)</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Governance`, `#Recursive Self-Improvement`, `#Anthropic`, `#AGI`

---

<a id="item-6"></a>
## [LLM 安全法官在不同危害类别上评估结果不一致](https://x.com/rohanpaul_ai/status/2064894134733693039) ⭐️ 8.0/10

这一发现至关重要，因为 AI 行业越来越依赖 LLM-as-a-judge 框架大规模自动化安全评估，以替代成本高昂的人工标注。如果这些法官不可靠，不安全的内容可能被放行，或者安全的内容被错误标记，这将直接削弱 AI 治理、对齐工作以及用户对部署系统的信任。 一个特别值得关注的发现是，不同 LLM 法官之间的高原始一致性可能会掩盖低真实可靠性，因为许多法官会默认选择相同的标签，而不考虑实际内容。这种表面一致性与真正评分者间可靠性之间的差异意味着，标准评估指标可能会对自动化安全评估产生虚假的信心。

rss · AI Hot · Jun 11, 02:15

**背景**: "LLM-as-a-Judge"（LLM 作为法官）是自然语言处理中广泛采用的评估框架，通过提示一个能力较强的语言模型对其他模型的输出进行评分和推理。它已成为替代人工标注以实现安全评估规模化的一种流行方案，因为人工审查既昂贵又耗时。然而，研究表明这些法官容易受到偏见、提示词措辞敏感性及其他局限性的影响，从而损害其准确性。依赖上下文的危害——例如金融建议的安全性取决于用户的具体人口统计和财务状况——构成了特殊的挑战，因为"最安全"的答案在不同用户情境下会有显著差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM-as-a-Judge">LLM-as-a-Judge - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2512.10687">Challenges of Evaluating LLM Safety for User Welfare</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#LLM Evaluation`, `#AI Alignment`, `#Research`

---

<a id="item-7"></a>
## [mlx-vlm v0.6.3 首发支持 DiffusionGemma 和 North Mini Code 1.0](https://x.com/berryxia/status/2064875107278098769) ⭐️ 8.0/10

mlx-vlm v0.6.3 正式发布，在发布当天即支持 Google DeepMind 的 DiffusionGemma（26B MoE 模型）和 Cohere 的 North Mini Code 1.0（30B MoE 模型），两款模型均可通过 MLX 框架在 Apple Silicon 上本地运行。用户可通过 `uv pip install -U mlx-vlm` 安装或升级体验。 此次发布大幅降低了在 Mac 硬件上本地运行前沿 MoE 视觉语言模型的门槛，使开发者和研究人员无需等待下游框架适配即可立即使用两款高效模型。DiffusionGemma 独创的块并行生成架构与迭代自纠错机制，标志着对传统自回归文本生成方式的重大突破。 DiffusionGemma 采用以 256 token 块为单位的并行生成方式，结合双向注意力和迭代自纠错机制；其 26B MoE 架构推理时仅激活 3.8B 参数，量化后仅需约 18GB 显存即可运行。North Mini Code 1.0 为 30B MoE 模型，仅激活 3B 参数，BF16 精度下可达约 66 tok/s 的推理速度。

rss · AI Hot · Jun 11, 00:59

**背景**: mlx-vlm 是一个基于 Apple MLX 框架的开源软件包，支持在 Apple Silicon 硬件上进行视觉语言模型（VLM）的推理和服务部署。混合专家模型（MoE）是一种机器学习技术，每次输入仅激活部分专家网络，使模型在拥有大量总参数的同时保持较低的推理计算开销。DiffusionGemma 基于 Gemma 4 骨干网络构建，用基于扩散的方法取代了传统的逐 token 顺序生成，从随机占位 token 开始，通过多次去噪过程并行迭代优化，生成速度最高可提升 4 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Blaizzy/mlx-vlm">GitHub - Blaizzy/ mlx - vlm : MLX - VLM is a package for inference and...</a></li>
<li><a href="https://developers.googleblog.com/diffusiongemma-the-developer-guide/">DiffusionGemma: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/">Google AI Releases DiffusionGemma, a 26B MoE Open Model Using Text Diffusion for Up to 4x Faster Generation - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#MLX`, `#Vision-Language Models`, `#Apple Silicon`, `#DiffusionGemma`, `#Local AI`

---

<a id="item-8"></a>
## [Claude Fable 5 零传统视频编辑完成 4K 发布视频制作](https://x.com/shao__meng/status/2064870367190270441) ⭐️ 8.0/10

一项技术实践演示了 Claude（Fable 5）能够完全通过提示词驱动的代码自主编排端到端 4K 视频生产流程，将 17 个 Sony S-Log3 4K 素材（约 25GB）处理为最终的 3840×2160@24fps、653MB 的发布视频，全程未打开任何传统视频编辑器。工作流整合了 Whisper 转录、Claude 子 agent 选片、FFmpeg 拼接、自定义 .cube LUT 调色，以及通过 Remotion 配合 Figma MCP 完成动态图形制作。 这是一项有力的概念验证，表明 AI agent 可以用纯提示词驱动的自动化流程替代传统上需要 Premiere 或 DaVinci Resolve 等专业编辑软件才能完成的复杂多工具创意工作流。它标志着向代码原生媒体制作的转变，开发者和 AI 协作即可产出广播级质量的内容，无需依赖基于时间线的编辑界面。 该流程使用 Whisper 进行逐词转录，Claude 作为子 agent 输出 JSON 编辑决策列表（EDL）进行选片，FFmpeg 进行粗剪拼接，手写 7 个自定义 .cube LUT 文件完成 S-Log3 调色，并通过 Remotion 结合 Figma MCP 将 11 张设计 PNG 转为 React 组件，实现代码与 Figma 之间的双向迭代。最终渲染输出 4334 帧、3840×2160@24fps、总计 653MB 的成品。

rss · AI Hot · Jun 11, 00:40

**背景**: Sony S-Log3 是索尼电影摄影机上的对数伽马曲线配置文件，能够捕捉更宽广的动态范围和色调范围，保留更多高光和阴影细节，但需要在后期进行调色处理。Remotion 是一个基于 React 的框架，允许开发者使用 JSX、CSS 和 Web 技术以编程方式创建真正的 MP4 视频，无需使用传统的时间线编辑软件。MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，为 AI 应用连接外部工具和数据源提供标准化接口，目前已被 OpenAI 和 Google DeepMind 等主要厂商采纳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Log_profile">Log profile - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.remotion.dev/">Remotion | Make videos programmatically</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Claude`, `#Video Production`, `#MCP`, `#Workflow Automation`

---

<a id="item-9"></a>
## [iOS 27 测试版泄露 Siri LLM 系统提示词](https://www.reddit.com/r/iOSBeta/comments/1u0kn3h/ios_27_db_1_siris_feedback_error_reporting_gives/) ⭐️ 8.0/10

有用户在 iOS 27 开发者预览版的诊断文件中发现了 Siri 的完整 LLM 系统指令，提示词超过 1300 行，约 22000 个 Token。随后相关内容被整理并发布到 GitHub Gist 上供公众分析。 这次泄露罕见地揭示了全球最大科技公司之一如何为面向消费者的 LLM 助手编写生产级系统提示词。它为 AI 社区提供了关于 Apple 在工具调用编排、推理护栏和大规模安全设计方面方法的宝贵洞察。 这些提示词将 Siri 定义为苹果设计的智能助手，要求它在调用工具之前先进行思考，并优先使用设备数据和搜索返回的结构化信息。指令明确要求 Siri 在遇到信息缺失、歧义或无法完成的任务时，必须向用户询问或说明限制，而不能自行编造答案。

telegram · @zaihuapd · Jun 10, 06:30

**背景**: 系统提示词是 LLM 接收到的最高权限指令，在任何用户交互开始之前就定义了模型的身份、行为边界、语气和不可违反的规则。在生产级 AI 助手中，这些提示词对于编排工具调用至关重要——指导模型何时以及如何调用外部 API、搜索功能或设备能力。嵌入在系统提示词中的护栏有助于防止幻觉、确保安全性，并在数百万次用户交互中保持一致的行为。分析主要科技公司的系统提示词已成为 AI 工程师了解前沿提示词工程技术的重要实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@himanshubhoir/how-llms-treat-system-and-user-prompts-34bb93796802">How LLMs Treat System and User Prompts | by Himanshu... | Medium</a></li>
<li><a href="https://www.nebuly.com/blog/llm-system-prompt-vs-user-prompt">LLM System Prompt vs. User Prompt</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri`, `#System Prompts`, `#LLM`, `#iOS 27`

---

<a id="item-10"></a>
## [OpenAI 秘密提交 S-1 文件，计划 2027 年上市](https://www.reuters.com/business/openai-expects-go-public-within-next-year-information-reports-2026-06-10/?utm_source=chatgpt.com) ⭐️ 8.0/10

OpenAI 已向美国证券交易委员会（SEC）秘密提交了 S-1 注册声明草案，CEO 萨姆·奥尔特曼向员工表示公司最早可能在 2027 年上市。此次提交旨在保留更早上市的选择权，同时让公司在私有阶段继续推进关键事务，潜在估值最高可达 1 万亿美元。 作为全球领先的前沿 AI 实验室，OpenAI 潜在的 1 万亿美元 IPO 将成为历史上最大规模的公开募股之一，将深刻重塑 AI 行业的融资格局和算力基础设施。奥尔特曼提到'递归自我改进'可能改变上市时间表，也表明公司的财务战略与 AGI 级别的重大突破密切相关。 OpenAI 还计划以每股 687.69 美元进行要约收购，为现有股东提供流动性。公司此前曾考虑最早在 2026 年 9 月上市，而秘密提交 S-1 文件通常比实际公开上市提前约六到九个月，不过具体时间表可能会有较大变化。

telegram · @zaihuapd · Jun 11, 02:19

**背景**: S-1 文件是公司在美国进行首次公开募股（IPO）前必须向 SEC 提交的注册声明。秘密提交允许公司在 SEC 审核期间保持财务细节的非公开状态，这一规定源于 2012 年的 JOBS 法案。递归自我改进（RSI）是指 AI 系统能够重写和改进自身代码的理论过程，可能导致智能的快速指数级增长，这一概念与 AGI 的发展密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-submits-confidential-s-1/">Confidential submission of draft S-1 to the SEC - OpenAI</a></li>
<li><a href="https://www.businessinsider.com/anthropic-submits-s-1-joins-ipo-race-with-openai-2026-6">Anthropic Submits S-1, Joins IPO Race With OpenAI - Business Insider</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#IPO`, `#S-1 Filing`, `#AI Industry`, `#Sam Altman`

---