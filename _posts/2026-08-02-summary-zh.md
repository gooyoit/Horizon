---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> From 113 items, 11 important content pieces were selected

---

1. [OpenAI Astra 模型解决十个长期未解数学难题](#item-1) ⭐️ 10.0/10
2. [DeepSeek-V4-Flash 公测版 API 上线，单任务成本比 GPT-5.6 Luna 低约 60%](#item-2) ⭐️ 10.0/10
3. [Seedance 2.5 发布：单次生成 30 秒视频，支持多模态参考与精准编辑](#item-3) ⭐️ 9.0/10
4. [MiniMax H3 与 OpenAI Astra 引领重大 AI 突破](#item-4) ⭐️ 9.0/10
5. [MiniMax H3 统一全模态生成，OpenAI Astra 解决 10 大数学难题](#item-5) ⭐️ 9.0/10
6. [高通完成收购 Modular，加速 AI 计算布局](#item-6) ⭐️ 8.5/10
7. [美国国会调查 DoorDash 使用中国 AI 模型 Kimi K2.6](#item-7) ⭐️ 8.0/10
8. [Lean 内核正确性漏洞 #14576 复盘：AI 辅助 Collatz 尝试暴露双重实现缺陷](#item-8) ⭐️ 8.0/10
9. [部分美国大型企业转向使用中国开源大模型以降低成本](#item-9) ⭐️ 8.0/10
10. [微软确认今年推出 Copilot「超级应用」](#item-10) ⭐️ 8.0/10
11. [AI 芯片每 9 个月翻番，2028 年底全球将达 2 亿颗](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Astra 模型解决十个长期未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 10.0/10

OpenAI 展示了其下一代模型 Astra 的内部版本，成功在数学和理论计算机科学领域取得了十项开放问题的新成果，这些问题至少在十年内没有任何进展。该公司在一个公开的 GitHub 仓库中发布了形式化验证的证明，并附带了详细的论文，指出每个解决方案的生成成本不到 2000 美元的 GPT-5.6 Sol token 费用。 这一成就代表了 AI 推理和科学发现能力的巨大飞跃，使前沿模型成为真正的研究协作者，能够解决以前被认为需要深刻人类数学直觉的问题。它标志着向数学家陶哲轩所说的“大数学”时代的范式转变，即 AI 在大规模人机协作中承担繁重的技术工作。 解决的问题涵盖多个领域，包括高维球体堆积、非索菲克群存在性、Connes 嵌入猜想和多色 Ramsey 数等。OpenAI 透明地承认数学论证由 AI 生成，而人类研究人员负责整理和 Lean 4 形式化验证，但该公司没有透露有多少问题被尝试过但未能得出解决方案。

rss · Simon Willison · Aug 1, 20:34

**背景**: Lean 是一种函数式编程语言和证明助手，允许数学家正式验证证明的逻辑严密性，确保绝对正确。Astra 模型系列是 OpenAI 即将推出的新一代 AI，旨在通过编排多个可以连续工作数小时甚至数天的智能体来处理长期、复杂的任务。这一消息紧随 Anthropic 的类似演示之后，后者使用名为 Mythos Preview 的专用内部模型发现了密码学漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten previously unsolved math solutions</a></li>
<li><a href="https://thenextweb.com/news/openai-astra-model-ten-math-proofs-non-sofic-groups">OpenAI says its next model, Astra, has solved ten open problems in mathematics</a></li>
<li><a href="https://www.theinformation.com/briefings/exclusive-openai-previews-astra-ai-model-dc">Exclusive: OpenAI Previews ‘Astra’ AI Model in DC</a></li>

</ul>
</details>

**社区讨论**: 这一消息在数学界引发了一场集体的存在主义反思，一些人描述了一种类似于国际象棋界“深蓝”时刻的“深刻精神危机”。评论者指出，虽然 AI 在理论探索方面的进展速度令人震惊，但人们也苦涩地意识到，越接近理论性质的工作量越容易被自动化取代。

**标签**: `#Frontier AI`, `#OpenAI`, `#Mathematical Reasoning`, `#Scientific Discovery`, `#AGI`

---

<a id="item-2"></a>
## [DeepSeek-V4-Flash 公测版 API 上线，单任务成本比 GPT-5.6 Luna 低约 60%](https://aihot.virxact.com/items/cmsb1ih6l01t5rohvzcdmlnuj) ⭐️ 10.0/10

DeepSeek 于 7 月 31 日正式上线了 DeepSeek-V4-Flash 公测版 API，@ArtificialAnlys、@arena 等基准测试平台于 8 月 1 日同步更新了评测结果。据显示，该模型的单任务 AI 成本比 OpenAI 的 GPT-5.6 Luna 低约 60%。 此次发布加剧了前沿 AI 模型市场的价格战，为开发者提供了一种比当前最先进模型成本大幅降低的替代方案。这表明 DeepSeek 正在价格与性能的前沿领域持续发起有力竞争，有望推动 AI 在对成本敏感的企业应用中加速普及。 DeepSeek-V4-Flash 是一款混合专家（MoE）模型，总参数量为 284B，激活参数量为 13B，支持一百万 token 的上下文窗口。在 OpenRouter 上，该 API 的定价为每百万输入 token 0.0896 美元，每百万输出 token 0.1792 美元，并同时兼容 OpenAI ChatCompletions 和 Anthropic API 格式。

rss · AI Hot · Aug 1, 23:22

**背景**: DeepSeek-V4 是 DeepSeek 推出的最新一代语言模型，采用混合专家（MoE）架构，在推理过程中仅激活一小部分总参数以优化效率。GPT-5.6 Luna 是 OpenAI 的高速、高吞吐量模型，旨在以远低于以往前沿模型的成本提供强大的性能。当前 AI 行业正处于激烈的竞争之中，各厂商都在努力突破价格与性能的边界，这使得推理成本成为 API 提供商之间的关键竞争因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/">Advancing the price-performance frontier with GPT - 5 . 6 | OpenAI</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Large Language Models`, `#AI API`, `#Frontier AI`, `#Cost Efficiency`

---

<a id="item-3"></a>
## [Seedance 2.5 发布：单次生成 30 秒视频，支持多模态参考与精准编辑](https://aihot.virxact.com/items/cmsb2e07t02gjrohvmoswiuvf) ⭐️ 9.0/10

ByteDance has released Seedance 2.5, an advanced AI video generation model capable of creating 30-second high-quality videos with robust multimodal referencing and precise timestamp-level editing controls.

rss · AI Hot · Aug 2, 00:09

**标签**: `#AI Video Generation`, `#Multimodal AI`, `#Generative AI`, `#ByteDance`, `#DeepTech`

---

<a id="item-4"></a>
## [MiniMax H3 与 OpenAI Astra 引领重大 AI 突破](https://aihot.virxact.com/items/cmsb17t7o01lwrohvy4qtbjn5) ⭐️ 9.0/10

MiniMax 发布了 H3 模型，这是一个统一的多模态系统，能够处理文本、图像、视频和音频，并可输出原生双声道 15 秒 2K 视频。此外，OpenAI Astra 的内部版本在数学和理论计算机科学的 10 个问题上取得新突破，成本约为 2000 美元。 这些进展代表了多模态生成和高级推理能力的重大飞跃，推动了前沿 AI 模型的能力边界。这些进步还伴随着优化 GPU 效率、解决长时程智能体训练瓶颈以及大幅降低 API 成本等更广泛的行业趋势，共同加速了 AI 的普及。 MiniMax H3 的突出之处在于能够原生生成带有同步双声道音频的高分辨率视频，这是多模态架构中一个值得注意的技术挑战。OpenAI Astra 的数学突破虽然每次运行成本约为 2000 美元，但凸显了解决复杂理论问题所需的巨大计算资源。

rss · AI Hot · Aug 1, 23:44

**背景**: 多模态模型是旨在同时处理、理解和生成多种类型数据（例如结合文本、视觉和音频输入）的人工智能系统。理论计算机科学和高等数学已成为评估新 AI 模型深度逻辑推理极限的关键基准。随着模型规模的扩大，AI 行业越来越关注克服硬件限制，例如 GPU 短缺和训练长时程任务智能体的困难。

**标签**: `#Frontier AI`, `#Multimodal Models`, `#OpenAI`, `#MiniMax`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [MiniMax H3 统一全模态生成，OpenAI Astra 解决 10 大数学难题](https://aihot.virxact.com/items/cmsb17t7o01lxrohv3i9u6t4w) ⭐️ 9.0/10

MiniMax 发布了通用多模态生成模型 H3，将文本、图像、视频和音频统一在同一上下文中，能够以不到主流模型三分之一的价格生成 15 秒 2K 分辨率且带有原生双声道的音视频，并计划开放权重。此外，OpenAI 宣布其下一代主要模型 Astra 的内部版本在数学和理论计算机科学的 10 个未解问题上取得了新成果，并附带了可验证的证明，总成本约为 2000 美元。 这些进展标志着 AI 正在迅速向真正统一且开放权重的多模态模型收敛，大幅降低了高质量媒体生成的成本门槛。与此同时，Astra 可供同行评审的数学突破表明，前沿 AI 正在从单纯模仿人类知识转向自主拓展基础科学研究的边界。 MiniMax H3 支持端到端的创作流程，用户可以利用多模态输入迭代优化视频输出。OpenAI 的 Astra 解决了数学家们至少十年未取得进展的开放性问题，其 AI 生成的论证随后由人类研究人员整理成正式的学术手稿；与此同时，KellyBench 等新基准测试表明，当前的前沿模型在长时程顺序决策方面仍然举步维艰，在模拟商业环境中处于亏损状态。

rss · AI Hot · Aug 1, 23:44

**背景**: 统一的多模态模型代表了一种转变，即摆脱分离的专用流程（例如用一个模型做文本转视频，另一个做文本转语音），转向一种能够原生理解和生成跨数据类型内容的单一架构。在 AI 推理领域，提供正式且可验证的证明是数学家使用的一种严格标准，旨在确保 AI 的结论在逻辑上是严密的，且不存在幻觉。此外，长时程 AI 智能体是负责在较长时间内执行复杂、多步骤目标的自主系统，这要求其在自我纠错、记忆管理和自适应规划方面具备复杂的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten previously unsolved math solutions</a></li>
<li><a href="https://www.gr.inc/releases/introducing-kellybench">Introducing KellyBench | General Reasoning</a></li>

</ul>
</details>

**标签**: `#Multimodal AI`, `#Frontier Models`, `#OpenAI`, `#MiniMax`, `#AI Reasoning`

---

<a id="item-6"></a>
## [高通完成收购 Modular，加速 AI 计算布局](https://aihot.virxact.com/items/cmsb3nnny03r9rohvgy8ry84o) ⭐️ 8.5/10

7 月 29 日，高通宣布完成以约 39.2 亿美元收购 AI 基础设施初创企业 Modular Inc.，将该公司的完整软件栈纳入高通版图。Modular 旗下的 Mojo 编程语言、MAX 推理引擎和 Modular Cloud 将继续作为独立品牌运营，联合创始人兼 CEO Chris Lattner 将出任高通 AI 软件与平台执行副总裁。 这笔收购标志着高通试图掌控完整的 AI 软硬件栈，借助 Modular 的硬件无关编译器技术直接挑战 Nvidia 的 CUDA 生态。如果 Modular 的软件层真正实现了跨 CPU、GPU 和 NPU 的可移植 AI 计算，它将从根本上改变 AI 推理的经济学——打破当前定义行业的硬件锁定效应。 Mojo 是一种基于 MLIR 编译器框架（而非直接基于 LLVM）构建的系统编程语言，旨在将类似 Python 的语法与媲美 C 语言的性能相结合，专门针对异构 AI 硬件进行优化。Modular 承诺维持其开放的异构生态系统，并计划于 2026 年秋季开源 Mojo，首个 Mojo 1.0 测试版已于 2026 年 5 月发布。

rss · AI Hot · Aug 2, 00:41

**背景**: Modular Inc. 由 Chris Lattner 联合创立，Lattner 是著名的编译器工程师，曾创建 LLVM 和 Apple 的 Swift 编程语言。该公司的旗舰产品 MAX（Modular Acceleration X）是新一代推理引擎和服务框架，能够自动优化 AI 模型在各类硬件加速器上的执行。高通一直在大力投资面向边缘设备和数据中心的 AI 芯片，但一直缺乏能与 Nvidia CUDA 相媲美的软件生态系统——而 Modular 的技术正是为了填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zoho.social/qualcomm-modular-acquisition-ai-portability/">Qualcomm's $3.92B Modular Deal: A Bet on AI Software</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://www.modular.com/">Modular: Inference from Kernel to Cloud</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Qualcomm`, `#Modular`, `#Mergers & Acquisitions`, `#Mojo`

---

<a id="item-7"></a>
## [美国国会调查 DoorDash 使用中国 AI 模型 Kimi K2.6](https://aihot.virxact.com/items/cmsb1ih6l01t3rohvlduqg5hl) ⭐️ 8.0/10

美国众议院两个委员会主席对 DoorDash 发起联合调查，此前该公司创始人 Andy Fang 公开表示，公司已通过模型路由服务将底层编码任务委托给中国月之暗面开发的开源模型 Kimi K2.6。Fang 称，Kimi K2.6 与 Anthropic Fable 5 的组合在性能上超越了 Sonnet 4.6 + Opus 4.8 的组合，且成本更低。 此次调查标志着美国政界对美国企业采用中国开源 AI 模型的政治审查正在升级，即便这些模型具有更高的成本效益和有竞争力的性能。此案可能开创先例，限制美国企业利用中国 AI 技术，从而从根本上重塑全球 AI 市场的竞争格局。 DoorDash 利用了模型路由服务，自动将较简单的底层编码任务委托给成本更低的 Kimi K2.6，同时将更昂贵的 Anthropic 模型保留用于处理更复杂的问题。国会调查信件明确承认中国模型具有竞争力的定价和定制化特性，但认为这些现实因素并不能消除国家安全方面的担忧。

rss · AI Hot · Aug 1, 23:33

**背景**: Kimi K2.6 是由月之暗面开发的开源模型，具备最先进的编码能力和高级智能体功能。模型路由是一种新兴技术，AI 系统会自动将每个查询定向到能够处理该任务且最具成本效益的模型，从而帮助企业优化支出。Anthropic 的 Claude Fable 5 是一款前沿模型，专为自主知识工作和复杂编码而设计，具备自适应推理能力和超长上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/ai-models/kimi-k2-6">Kimi K2.6 | Leading Open-Source Model in Coding & Agent</a></li>
<li><a href="https://openrouter.ai/docs/guides/routing/routers/auto-router">Auto Router - Intelligent Model Selection</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Geopolitics`, `#Moonshot AI`, `#Large Language Models`, `#AI Industry`

---

<a id="item-8"></a>
## [Lean 内核正确性漏洞 #14576 复盘：AI 辅助 Collatz 尝试暴露双重实现缺陷](https://aihot.virxact.com/items/cmsb08tc000o5rohvdh5el44e) ⭐️ 8.0/10

Lean 定理证明器内核中发现了一个正确性漏洞（#14576），起因是一次 AI 辅助证明 Collatz 猜想的尝试利用了嵌套归纳类型处理中缺失的类型检查，从而构造出了 False 的证明。该漏洞仅能通过元编程触发，且官方 Lean 内核与基于 Rust 的独立检查器 nanoda 各有一个互不相关的缺陷，需要同时修复才能确保安全。 这一事件凸显了形式化证明系统中多层独立验证的关键重要性，因为单个正确性漏洞就可能破坏整个系统所验证的全部证明的可信度。它同时也展示了一个引人注目的 AI 安全应用场景：AI 系统能够协助发现用于验证 AI 生成证明和数学定理的工具本身所存在的深层、隐蔽缺陷。 该漏洞源于嵌套归纳类型编译过程中缺失的类型检查——嵌套归纳类型是指被定义的类型作为参数出现在其他归纳类型构造器中的递归类型。Lean FRO 已修复该漏洞并新增了回归测试，OpenAI 的 AI 安全团队在调查过程中还协助发现了其他内核编程错误。

rss · AI Hot · Aug 1, 23:21

**背景**: Lean 是一种基于依值类型论的函数式编程语言和交互式定理证明器，被广泛用于形式化验证数学定理和软件正确性。在这类系统中，正确性漏洞意味着逻辑不一致——可以证明 False，进而导致任何命题都能被证明，彻底破坏系统的可靠性。嵌套归纳类型是一种定义复杂递归数据结构的方式，其正确编译需要严格的类型检查以维持逻辑一致性。像 nanoda 这样用 Rust 编写的独立检查器，通过在 Lean 生态系统之外重新检查证明，构成了第二道防线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lawrencecpaulson.github.io/2026/07/30/Collatz.html">Why is it all in the kernel ?</a></li>
<li><a href="https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/">4.4. Inductive Types</a></li>
<li><a href="https://lean-lang.org/faq/">Frequently Asked Questions — Lean Lang</a></li>

</ul>
</details>

**社区讨论**: Lawrence Paulson 在其博客中指出，该漏洞利用了 Lean 内核中的缺陷，而 nanoda 同样未能检测到该错误，并将其与 Rocq 中由递归函数模式匹配引发的类似正确性漏洞进行了类比。Manifold 预测市场社区此前曾争论此类实现层面的漏洞是否应算作正确性漏洞，有人认为这些是可以修复的疏忽，而非根本性的理论问题。

**标签**: `#Formal Verification`, `#AI Safety`, `#Lean Theorem Prover`, `#Automated Theorem Proving`, `#Software Correctness`

---

<a id="item-9"></a>
## [部分美国大型企业转向使用中国开源大模型以降低成本](https://36kr.com/newsflashes/3920583026929281?f=rss) ⭐️ 8.0/10

包括 Coinbase 和 Airbnb 在内的大型美国企业正越来越多地采用中国开源 AI 模型（如 Kimi K3 和阿里巴巴的 Qwen），以大幅降低运营成本。这一转变发生在中国 AI 模型以远低于西方替代方案的成本展现出有竞争力的性能之际。 这一趋势标志着全球 AI 格局可能发生范式转变，挑战了美国企业在前沿 AI 模型领域保持不可逾越领先优势的长期假设。中国开源模型的成本效益可能使先进的 AI 能力更加普及，并迫使西方 AI 供应商重新思考其定价策略。 由月之暗面开发的 Kimi K3 总参数达到 2.8 万亿，单次激活 1040 亿参数，支持约 100 万 Token 上下文，并且原生支持文本、图像和视频理解。爱彼迎称赞阿里巴巴的 Qwen 模型"快速且便宜"，而 Kimi K3 的发布引发了美股半导体板块的大幅下跌，市场开始质疑"强模型必然需要更多 GPU"的投资逻辑。

rss · 36kr · Aug 1, 07:30

**背景**: 从 AlphaGo 称霸围棋界到 ChatGPT 面世，美国在算法大模型领域积累了显著的先发优势。然而，中国 AI 企业通过开源策略正在迅速缩小差距，DeepSeek 于 2025 年 1 月发布的 R1 模型曾引发类似的市场震动。开源方式使企业能够获取和部署强大的模型，而无需向专有提供商支付高额 API 费用，这对于注重成本的企业来说是一个有吸引力的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hao.cnyes.com/post/261010">Kimi ...</a></li>
<li><a href="https://www.knews.com.tw/news/CC3E7668CD874E36905E339E78C40510">「DeepSeek時刻」重演？ 一文搞懂 月 之 暗 面 Kimi ... | 知新聞</a></li>
<li><a href="https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1">Top-performance foundation models from Alibaba Cloud</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Open Source`, `#Industry Trends`, `#Global AI Race`, `#Cost Optimization`

---

<a id="item-10"></a>
## [微软确认今年推出 Copilot「超级应用」](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 纳德拉在财报电话会议上确认，公司将于今年推出一款 AI「超级应用」，将 Copilot 的聊天、编程和智能体能力整合到一个统一体验中，同时覆盖消费者和商用场景。该应用将融合 Copilot 聊天机器人、GitHub Copilot、Copilot Cowork 和 Autopilot 系统的功能。 这一整合标志着行业向统一智能体 AI 架构的重大转变，单一应用即可处理多步骤任务执行、编程和对话辅助，同时覆盖企业和消费者市场。此举使微软能够直接与 OpenAI 近期推出的 ChatGPT Work 应用竞争，并进一步巩固了公司将 AI 深度嵌入日常生产力工作流的战略。 Copilot Cowork 于 2026 年中全面发布，是内置于 Microsoft 365 的 AI 自动化层，由 Anthropic 的 Claude 模型驱动，可在 Outlook、Teams、Excel 和 PowerPoint 中委派、规划和执行多步骤任务。超级应用还将整合 Copilot Tasks，这是一项能够规划和执行用自然语言描述的多步骤工作的智能体功能。

telegram · @zaihuapd · Aug 1, 13:18

**背景**: 「超级应用」是指将众多功能和服务整合到一个统一平台中的单一应用程序，这一概念由微信等应用普及。微软的 Copilot 经历了多个演进阶段：从基于聊天的 AI 助手起步，发展到用于后台多步骤任务执行的 Copilot Cowork，再进一步向具备更强自主能力的 Autopilot 系统迈进。Copilot Cowork 由微软与 Anthropic 合作开发，在预览期结束后已向所有 Microsoft 365 Copilot 客户全面开放。微软最近一个季度的营收达到 900 亿美元，主要由 AI 和云业务推动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/microsoft-launches-copilot-cowork-built-anthropic-cross-m365-bora-g2xzc">Microsoft launches Copilot Cowork , built with Anthropic...</a></li>
<li><a href="https://peafowlit.com/blog/microsoft-copilot-cowork-ga-governance-guide/">Microsoft Copilot Cowork GA Guide for IT Governance and Security</a></li>
<li><a href="https://windowsforum.com/threads/copilot-tasks-microsofts-agentic-ai-for-multi-step-automation.403400/">Copilot Tasks: Microsoft’s Agentic AI for Multi-Step Automation | Windows Forum</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI Agents`, `#Super App`, `#Enterprise AI`

---

<a id="item-11"></a>
## [AI 芯片每 9 个月翻番，2028 年底全球将达 2 亿颗](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html) ⭐️ 8.0/10

据《纽约时报》引用的 Epoch AI 估算数据，全球 AI 芯片将从目前的约 2000 万颗增长至 2028 年底的约 2 亿颗，大约每 9 个月翻一番，增幅达十倍。IDC 预测，2029 年全球 AI 基础设施投资将突破 1 万亿美元，而去年仅为 3180 亿美元。 AI 算力的爆发式增长直接反映了规模定律的推进轨迹，而规模定律是 AI 能力提升的主要驱动力，决定了哪些机构和国家能够构建前沿模型。巨额投资和高度集中的算力分布——美国控制了全球约 80% 的 AI 算力——将深刻影响全球 AI 研究、地缘政治竞争和经济结构的未来走向。 据信仅 Google 一家的 AI 芯片数量就是中国所有公司总和的四倍，凸显了美国在算力领域的压倒性优势。然而，大规模数据中心建设正在推高电价并引发环境争议，经济学家同时警告当前支出可能超过盈利，与历史上的基建泡沫有相似之处。

telegram · @zaihuapd · Aug 2, 01:01

**背景**: AI 规模定律描述了一个经验性观察：随着训练数据规模、模型参数量和计算资源的增加，模型性能会以可预测的方式提升。这一原理已在视觉、语言、音频和多模态学习等大规模任务中得到验证，成为科技巨头以前所未有的规模投资 AI 基础设施的根本依据。Epoch AI 是一家多学科研究机构，专注于研究影响 AI 发展轨迹的关键趋势，提供关于算力、投资和能力进展的数据驱动预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-scaling-laws/">How Scaling Laws Drive Smarter, More Powerful AI | NVIDIA Blog</a></li>
<li><a href="https://epoch.ai/about">About Us | Epoch AI</a></li>
<li><a href="https://www.aisafetybook.com/textbook/scaling-laws">2.4: Scaling Laws | AI Safety, Ethics, and Society Textbook</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#AI Chips`, `#Scaling Laws`, `#Data Centers`, `#Epoch AI`

---