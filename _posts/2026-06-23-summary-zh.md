---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> From 103 items, 13 important content pieces were selected

---

1. [研究表明 LLM 将文本风格与结构角色标签混淆，导致越狱漏洞](#item-1) ⭐️ 9.0/10
2. [OpenAI Daybreak、美团海报生成、PP-OCRv6、GLM 5.2 等 AI 进展](#item-2) ⭐️ 9.0/10
3. [字节跳动发布豆包 Seed 2.1 Pro 和 Turbo 模型](#item-3) ⭐️ 9.0/10
4. [NVIDIA Vera Rubin NVL4 平台 2026Q4 上市：科学计算模拟性能是 Grace Hopper 四倍](#item-4) ⭐️ 9.0/10
5. [Moebius：具备百亿参数级性能的 2 亿参数图像修复模型](#item-5) ⭐️ 8.0/10
6. [通过 WebGPU 将 Moebius 0.2B 图像修复模型移植到浏览器](#item-6) ⭐️ 8.0/10
7. [字节跳动在火山引擎大会发布 Seedance 2.5、豆包 Seed 2.1 及 Seeddream 5.0](#item-7) ⭐️ 8.0/10
8. [Cline 团队实测 GLM-5.2 vs Claude Opus 4.8：修 bug 后构建稳定性差异](#item-8) ⭐️ 8.0/10
9. [百度开源 Unlimited OCR：3B 参数 500M 激活性能惊艳](#item-9) ⭐️ 8.0/10
10. [Groq 完成 6.5 亿美元融资，转型 AI 推理云服务商](#item-10) ⭐️ 8.0/10
11. [三星电子业界率先突破 HBM4 内存 10 亿美元销售额](#item-11) ⭐️ 8.0/10
12. [消息称高通正洽谈收购 AI 芯片企业 Modular，估值约 40 亿美元](#item-12) ⭐️ 8.0/10
13. [OpenAI 扩展 Daybreak 计划，推出 Patch the Planet 与 GPT-5.5-Cyber](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [研究表明 LLM 将文本风格与结构角色标签混淆，导致越狱漏洞](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 9.0/10

Charles Ye、Jasmine Cui 和 Dylan Hadfield-Menell 撰写的新论文《Prompt Injection as Role Confusion》证明，LLM 在识别指令时，会将文本的写作风格置于结构角色标签（如 <system> 或 <think>）之上。研究人员发现，只需将不受信任的用户输入格式化为模型内部思考的风格，攻击成功率就高达 61%；而如果稍微改写文本以消除这种风格模仿（即“去风格化”），攻击成功率则骤降至 10%。 这一发现揭示了当前 AI 模型处理指令方式上的根本架构缺陷，证明如果不实现真正的角色感知，就无法在模型层面可靠地解决提示词注入问题。这对自主 AI 代理的安全性具有严重的影响，因为恶意攻击者可以大规模地利用看似无害的文本，巧妙地操纵模型状态并绕过安全防护。 研究人员通过在提示词中附加模仿模型内部策略检查独白的文本，成功诱骗 gpt-oss-20b 等模型覆盖了其安全训练，从而证实了该漏洞的存在。研究得出结论，由于角色边界是连续的而非离散的，因此在 LLM 架构中防御注入将一直是一场无休止的“打地鼠”游戏。

rss · Simon Willison · Jun 22, 23:59

**背景**: 提示词注入是一种网络安全漏洞，不受信任的用户输入会以非预期的方式改变大型语言模型（LLM）的行为，这类似于数据库中的 SQL 注入。AI 开发人员试图通过使用角色标签（例如 <system>、<user>、<assistant>）来缓解这一问题，从而在结构上将受信任的开发者指令与不受信任的外部数据分离开来。AI 对齐研究则致力于确保这些模型能够可靠地遵循人类意图和安全准则，而不被恶意操纵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM 01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调，依赖基于文本的标签来保障安全在根本上是存在缺陷的，有评论者认为必须改变 LLM 的架构，或者必须在受约束的受信环境中运行推理。一位开发者提出了一种技术修复方案，即将角色身份直接嵌入到 token 中以创建无法伪造的标签；而其他人则指出，静态的安全基准测试几乎毫无用处，因为人类红队成员可以通过不断调整攻击方式来实现接近 100% 的成功率。

**标签**: `#AI Safety`, `#Prompt Injection`, `#LLM Vulnerabilities`, `#AI Alignment`, `#Cybersecurity`

---

<a id="item-2"></a>
## [OpenAI Daybreak、美团海报生成、PP-OCRv6、GLM 5.2 等 AI 进展](https://aihot.virxact.com/items/cmqpw5z9e04dislp55q0qnlvh) ⭐️ 9.0/10

A comprehensive update on recent AI advancements including OpenAI's Daybreak cybersecurity program, Meituan's poster generation models, PP-OCRv6, and the GLM 5.2 multimodal agent.

rss · AI Hot · Jun 23, 00:00

**标签**: `#Frontier AI`, `#AI Agents`, `#Cybersecurity AI`, `#Multimodal Models`, `#OCR`

---

<a id="item-3"></a>
## [字节跳动发布豆包 Seed 2.1 Pro 和 Turbo 模型](https://www.ithome.com/0/967/314.htm) ⭐️ 9.0/10

字节跳动在火山引擎平台悄然上线了豆包 Seed 2.1 系列模型，推出 Pro 和 Turbo 两个深度思考模型版本，在编程工程交付、Agent 长链路任务执行和多模态理解三大方向实现全面升级。官方宣称其三大能力比肩 GPT-5.5，其中 Turbo 版本为规模化生产场景提供了更低成本、更低时延的选择。 此次发布标志着字节跳动在全球 AI 模型竞赛前沿的强势发力，尤其在自主编程 Agent 和复杂多步骤任务执行等关键领域。在宣称比肩 GPT-5.5 能力的同时配合极具竞争力的定价（Turbo 版输入仅 3 元/百万 tokens），有望大幅改变企业级 AI 部署的经济学格局，并加速 Agent AI 工作流在生产环境中的落地应用。 Pro 模型（doubao-seed-2-1-pro-260628）定价为输入 6 元/百万 tokens、输出 30 元/百万 tokens，Turbo 版本价格减半，分别为 3 元和 15 元/百万 tokens，两者均支持缓存命中八折优惠。Seed-Evolving 模型采用动态迭代机制，每周至少更新一次并通过统一 Model ID 调用，同时还发布了新增 Human-like 自然聊天能力的角色模型（doubao-seed-character-260628）。

rss · IT HOME · Jun 23, 01:57

**背景**: 字节跳动的豆包模型系列经历了从 1.x 到 2.0 再到 2.1 的持续迭代，每一代都在编程、Agent 能力和多模态理解方面进行重点提升。火山引擎是字节跳动旗下的云与 AI 服务平台，负责托管这些模型并向企业提供 API 接入服务。Agent AI 指的是能够自主规划、执行多步骤工作流、调用工具并根据中间结果进行动态调整的智能系统，这一能力在真实软件开发和复杂业务自动化场景中日益关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://evolink.ai/blog/doubao-seed-2-0-review-benchmarks-pricing">Doubao Seed 2.0 Review</a></li>
<li><a href="https://www.volcengine.com/product/doubao">volcengine.com/product/doubao</a></li>
<li><a href="https://lekha-bhan88.medium.com/introduction-to-agentic-ai-and-its-design-patterns-af8b7b3ef738">Introduction to Agentic AI and Its Design Patterns | by Lekha... | Medium</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#ByteDance`, `#AI Agents`, `#Coding`, `#Multimodal AI`

---

<a id="item-4"></a>
## [NVIDIA Vera Rubin NVL4 平台 2026Q4 上市：科学计算模拟性能是 Grace Hopper 四倍](https://www.ithome.com/0/967/303.htm) ⭐️ 9.0/10

NVIDIA has announced that its Vera Rubin NVL4 platform, offering up to 8x the scientific AI inference performance of the Grace Hopper architecture, will launch in Q4 2026.

rss · IT HOME · Jun 23, 01:44

**标签**: `#NVIDIA`, `#AI Infrastructure`, `#Vera Rubin`, `#AI Hardware`, `#Supercomputing`

---

<a id="item-5"></a>
## [Moebius：具备百亿参数级性能的 2 亿参数图像修复模型](https://hustvl.github.io/Moebius/) ⭐️ 8.0/10

研究人员推出了开源图像修复模型 Moebius，该模型仅有 2 亿参数，却声称能提供与比它大 50 倍的百亿参数级模型相媲美的性能。该模型已被转换为 ONNX 格式并可在浏览器中完全运行，交互式演示大约需要下载 1.3GB。 Moebius 直接挑战了人工智能领域的一个普遍假设，即高质量图像处理需要庞大的模型，证明了在不牺牲输出质量的情况下可以实现极高的效率。这一突破可能使专业级图像编辑工具能够在浏览器或消费级硬件上本地运行，从而让更多用户受益。 社区测试表明，尽管该模型在自然图像上表现相当不错，但修复区域在视觉上可能比周围环境更平滑，并且在处理新颖物体时存在明显困难。此外，当前版本仅限于 512x512 分辨率的输出，这限制了其在更高保真度应用中的实用性。

hackernews · DSemba · Jun 22, 13:53 · [社区讨论](https://news.ycombinator.com/item?id=48630171)

**背景**: 图像修复是一种人工智能驱动的技术，用于填充、恢复或替换数字图像中缺失或不需要的部分，其应用范围从物体移除到创意照片编辑。在机器学习中，模型参数是神经网络在训练过程中学习的内部变量（如权重和偏置），用于将输入数据转换为输出预测。通常，较高的参数数量使模型能够捕获更复杂的模式，但最近的研究越来越关注以更小、更高效的架构实现相当的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Image_inpainting">Image inpainting</a></li>
<li><a href="https://www.ibm.com/think/topics/model-parameters">What are Model Parameters? - Machine learning</a></li>

</ul>
</details>

**社区讨论**: 社区的反应褒贬不一：一位开发者使用 ONNX 成功构建了基于浏览器的演示，而其他人则指出该模型在某些测试图像上会失败，且并未真正达到百亿参数级的质量。一些用户分享了使用修复工具的实际经验，至少有一位评论者询问了该术语的基本定义，这表明这项技术尚未被广泛理解。

**标签**: `#AI`, `#Image Inpainting`, `#Computer Vision`, `#Model Efficiency`, `#Open Source`

---

<a id="item-6"></a>
## [通过 WebGPU 将 Moebius 0.2B 图像修复模型移植到浏览器](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

Simon Willison 在 Anthropic 的 Claude Code 代理的辅助下，成功将轻量级图像修复模型 Moebius 0.2B 移植到浏览器中，完全通过 WebGPU 运行。该模型原本需要依赖 PyTorch 和 NVIDIA CUDA，现在已被转换为通过 ONNX Runtime Web 运行，允许用户在没有后端基础设施的情况下进行客户端图像处理。 该项目展示了边缘 AI 日益成熟的可行性，证明了有能力的机器学习模型可以绕过繁重的云基础设施，在本地运行并获得可接受的性能。它同时也有力地验证了 LLM 辅助编程的潜力，展示了像 Claude Code 这样的 AI 编程代理如何能够自主处理复杂的多步骤软件移植项目。 移植过程利用了基于 WebGPU 后端的 ONNX Runtime Web，而不是 Transformers.js，这一策略是在初步研究期间由 Claude 建议的。Willison 通过提示 Claude“思考移植的可行性”来启动该项目，并将 AI 的技术评估保存为上下文，随后部署 Claude Code 执行实际的转换工作。

rss · Simon Willison · Jun 22, 23:43

**背景**: Moebius 是一个新发布的、专用于图像修复的高效深度学习框架，其参数量仅为 2 亿（0.2B），却能达到与庞大的 100 亿（10B+）级工业基础模型相媲美的性能。图像修复技术允许用户遮罩或高亮图像的特定区域，然后由 AI 通过想象该空间逻辑上应该存在的内容来进行填充。WebGPU 是一项现代 Web 标准，能够将 GPU 硬件加速直接暴露给网络浏览器，使复杂的机器学习任务能够在客户端执行，从而打破传统的性能瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.19195">Paper page - Moebius : 0 . 2 B Lightweight Image Inpainting Framework...</a></li>
<li><a href="https://www.mlhive.com/2026/06/why-moebius-0-2b-disrupts-generative-image-inpainting">Why Moebius 0 . 2 B is Disrupting Generative Image Inpainting</a></li>
<li><a href="https://opensource.microsoft.com/blog/2024/02/29/onnx-runtime-web-unleashes-generative-ai-in-the-browser-using-webgpu/">ONNX Runtime Web unleashes generative AI in the browser using...</a></li>

</ul>
</details>

**标签**: `#WebGPU`, `#Image Inpainting`, `#Edge AI`, `#Claude Code`, `#Browser AI`

---

<a id="item-7"></a>
## [字节跳动在火山引擎大会发布 Seedance 2.5、豆包 Seed 2.1 及 Seeddream 5.0](https://aihot.virxact.com/items/cmqpzf6br057mslp5kdw7vman) ⭐️ 8.0/10

字节跳动在 2026 年火山引擎大会上发布了多款全新 AI 模型，包括视频生成模型 Seedance 2.5、语言模型豆包 Seed 2.1 以及图像模型 Seeddream 5.0。字节跳动声称豆包 Seed 2.1 的能力已达到 Anthropic Claude Opus 4.6 的水平。 这些发布标志着字节跳动正积极进军全球 AI 前沿竞争行列，以声称达到 Opus 4.6 水平的性能直接挑战西方顶尖实验室。全新的模型矩阵也进一步强化了火山引擎云平台，为企业提供涵盖文本、图像和视频生成的全方位国产化替代方案。 尽管字节跳动做出了强有力的性能声明，但新模型的具体技术参数、基准测试分数及定价信息目前尚未公开。字节跳动声称对标的 Claude Opus 4.6 模型，以其出色的长上下文连贯性、智能体任务中的周密规划以及高级编程能力而闻名。

rss · AI Hot · Jun 23, 01:35

**背景**: 火山引擎是字节跳动旗下的云与 AI 服务平台，依托支撑抖音、TikTok 等海量应用所积累的技术能力而建立。"Seed"（豆包/种子）系列是字节跳动基础大模型的总品牌，涵盖用于文本生成的豆包系列和用于视频生成的 Seedance 等。Claude Opus 4.6 是由 Anthropic 开发的前沿大语言模型，被业界广泛视为在写作质量、复杂推理和编程任务上的顶级基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.volcengine.com/">火山引擎-你的ai云</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-6">Claude Opus 4.6 \ Anthropic</a></li>
<li><a href="https://seed.bytedance.com/en/seedance">Seedance</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#Foundation Models`, `#Generative AI`, `#Volcano Engine`, `#AI Releases`

---

<a id="item-8"></a>
## [Cline 团队实测 GLM-5.2 vs Claude Opus 4.8：修 bug 后构建稳定性差异](https://aihot.virxact.com/items/cmqpy5jtq04u2slp5kst6ijww) ⭐️ 8.0/10

A real-world test by the Cline team reveals that the open-source GLM model outperforms Claude Opus in production stability by using more tool calls to ensure clean builds, highlighting a key differentiation in agentic coding workflows.

rss · AI Hot · Jun 23, 01:08

**标签**: `#AI Coding Agents`, `#LLM Evaluation`, `#Open Source AI`, `#Software Engineering`, `#Autonomous Agents`

---

<a id="item-9"></a>
## [百度开源 Unlimited OCR：3B 参数 500M 激活性能惊艳](https://aihot.virxact.com/items/cmqpwt80k04gkslp5tzpa9zcz) ⭐️ 8.0/10

Baidu has open-sourced 'Unlimited OCR,' a highly efficient 3B parameter model with 500M active parameters that achieves impressive optical character recognition performance.

rss · AI Hot · Jun 23, 00:10

**标签**: `#Open Source AI`, `#OCR`, `#Baidu`, `#Computer Vision`, `#Efficient AI`

---

<a id="item-10"></a>
## [Groq 完成 6.5 亿美元融资，转型 AI 推理云服务商](https://www.ithome.com/0/967/312.htm) ⭐️ 8.0/10

AI 芯片初创企业 Groq 于 2026 年 6 月 22 日宣布完成新一轮 6.5 亿美元融资，并将业务模式转型为 AI 推理云服务供应商（CSP）。该公司计划大规模扩展其 AI 推理基础设施并部署 NVIDIA LPX 系统，目标到 2027 年底拥有 200MW 的算力资源。 这一战略转型将 Groq 从纯粹的硬件芯片设计者转变为直接参与云基础设施竞争的玩家，旨在抓住业界对高速 AI 推理激增的需求。通过利用其在 LPU 技术上的独特经验并与 NVIDIA 合作，Groq 旨在赢得数百万开发者和数千家 AI 原生企业所需的 AI 算力市场的巨大份额。 Groq 目前在北美、欧洲、中东和亚太地区运营着 13 座数据中心，为超过 500 万开发者提供服务，每周处理的词元（Token）消耗量以万亿计。在达成此前价值 200 亿美元的技术授权协议后，Groq 的工程团队将部署其最新的推理技术以及全新的 NVIDIA LPX 系统，该系统将 LPU 与 NVIDIA Vera Rubin GPU 相结合，以应对超低延迟的工作负载。

rss · IT HOME · Jun 23, 01:57

**背景**: Groq 以其设计的语言处理单元（LPU）而闻名，这是一种专门为加速 AI 推理任务而打造的专用芯片架构。与通用 GPU 不同，LPU 集成了数百兆字节的 SRAM 作为主要权重存储，并采用静态调度来降低延迟，使其在处理大型语言模型时极为高效。2025 年底，NVIDIA 以 200 亿美元收购了 Groq LPU 技术的非独家授权，并将其整合到全新的 NVIDIA Groq 3 LPX 推理加速器中，作为 Vera Rubin 平台的一部分，以解决智能体 AI 系统中吞吐量与延迟之间的权衡问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2021531244194738454">深度拆解Groq LPU架构：这颗让英伟达花200亿买下的芯片，凭什么</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/lpx/">AI Inference Accelerator | NVIDIA Groq 3 LPX</a></li>
<li><a href="https://groq.com/lpu-architecture">LPU | Groq is fast, low cost inference.</a></li>

</ul>
</details>

**标签**: `#Groq`, `#AI Infrastructure`, `#AI Inference`, `#Cloud Computing`, `#LPU`

---

<a id="item-11"></a>
## [三星电子业界率先突破 HBM4 内存 10 亿美元销售额](https://www.ithome.com/0/967/278.htm) ⭐️ 8.0/10

据报道，三星电子已成为业界首家 HBM4 内存销售额突破 10 亿美元的公司，该产品于 2026 年 2 月 12 日正式量产，用时不到五个月即达成这一里程碑。此外，三星上月还率先出样了下一代 HBM4E 内存，容量为 48GB（12Hi 堆叠），引脚速率最高可达 16Gbps。 这一里程碑标志着 HBM4 内存正快速从研发阶段进入大规模商用部署，直接为训练和推理前沿 AI 模型所需的下一代 AI 加速器提供支持。三星在 HBM4 营收和 HBM4E 出样方面的领先优势，巩固了其在关键 AI 硬件供应链中对 SK 海力士和美光等竞争对手的竞争地位。 三星的 HBM4 内存基于 1cnm DRAM Die 和 4nm 逻辑 Base Die 制造，采用 12Hi 堆叠实现单堆栈 36GB 容量，引脚速率为 13Gbps，总带宽达 3.3TB/s。HBM4E 样品将性能进一步提升至 14~16Gbps 引脚速率和 3.6TB/s 堆栈带宽，容量增至 48GB。

rss · IT HOME · Jun 23, 01:20

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，旨在为 AI 训练和高性能计算等高负载场景提供超高带宽和能效。每个 HBM 堆栈通过硅通孔（TSV）将多个 DRAM Die 与逻辑 Base Die 垂直连接，相比传统内存可实现大幅提升的数据吞吐量。受 NVIDIA GPU 等 AI 加速器需求激增的推动，HBM 市场预计在 2025 年达到 467 亿美元。HBM4 是 JEDEC 标准化的最新一代，HBM4E 则是其增强后续版本，提供更高的速度和容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.edn.com/advancing-ai-performance-with-hbm4-sphbm4-dram-solutions/">Advancing AI performance with HBM 4 , SPHBM4 DRAM solutions - EDN</a></li>
<li><a href="https://nerds.xyz/2026/06/samsung-hbm4e-memory/">Samsung ships industry-first HBM 4 E memory as AI infrastructure race...</a></li>
<li><a href="https://uomolab.com/en/hbm-memory-technology-deep-dive-the-memory-revolution-in-the-ai-era/">HBM Memory Technology Deep Dive: The Memory ... - UomoLab</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#AI Infrastructure`, `#HBM4`, `#Samsung`, `#Semiconductors`

---

<a id="item-12"></a>
## [消息称高通正洽谈收购 AI 芯片企业 Modular，估值约 40 亿美元](https://www.ithome.com/0/967/274.htm) ⭐️ 8.0/10

彭博社报道称，高通正就收购 AI 基础设施初创公司 Modular Inc. 进行深度洽谈，估值约 40 亿美元，远高于该公司仅 9 个月前 16 亿美元的估值。此外，高通据称还在洽谈以最高 100 亿美元的价格收购另一家 AI 芯片初创公司 Tenstorrent。 这些潜在的收购标志着高通正积极进行战略转型，试图降低对波动剧烈的智能手机芯片市场的依赖，切入数据中心处理器和自动驾驶芯片等高增长赛道。若交易成功，这也将是对 NVIDIA 在 AI 计算生态中主导地位的重大挑战，因为 Modular 的 Mojo 编程语言和编译器基础设施正是针对 NVIDIA 的 CUDA 软件护城河而设计的。 Modular 成立于 2022 年，由前苹果和谷歌工程师联合创立，迄今累计融资 3.8 亿美元，其中去年 9 月由美国创新技术基金领投的一轮融资募得 2.5 亿美元。该交易可能在未来数周内正式宣布，但彭博社提醒称谈判仍存在破裂或条款变更的可能性。

rss · IT HOME · Jun 23, 01:08

**背景**: Modular 最知名的产品是 Mojo 编程语言和 MAX（Modular Acceleration X）平台，旨在统一不同硬件后端的 AI 软件开发，解决 AI 部署中的碎片化问题。该初创公司的核心价值主张是挑战 NVIDIA 的 CUDA 软件生态系统——后者已成为 AI 计算的事实标准，但会导致供应商锁定。高通据称同时在洽谈收购的 Tenstorrent 由传奇芯片架构师 Jim Keller 领导，致力于开发基于 RISC-V 架构的 AI 加速器，在最近一轮融资中的投前估值为 20 亿美元。高通的收购策略反映了芯片行业的一个更广泛趋势：传统芯片制造商正通过收购 AI 软件和硬件初创公司来构建端到端的 AI 能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aol.com/articles/ai-startup-modular-raises-250-160943691.html">AI startup Modular raises $250 million, seeks to challenge Nvidia...</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#M&A`, `#Qualcomm`, `#Modular`, `#AI Chips`

---

<a id="item-13"></a>
## [OpenAI 扩展 Daybreak 计划，推出 Patch the Planet 与 GPT-5.5-Cyber](https://openai.com/index/patch-the-planet/) ⭐️ 8.0/10

OpenAI 扩展了其 Daybreak 网络安全计划，推出了 Patch the Planet 项目，利用 AI 模型配合人工审核，在 cURL、Go、Python 等 30 多个关键开源项目中查找并修复漏洞。公司还正式发布了 GPT-5.5-Cyber 模型（在 CyberGym 基准测试中得分 85.6%），并推出了 Daybreak Cyber 合作伙伴计划和更新的 Codex Security 工具。 这一计划展示了 AI 在防御性网络安全领域的一项重大实际应用，将重点从攻击转向为广泛使用的开源基础设施提供可扩展的漏洞修复。通过与 Trail of Bits 等机构以及多国政府机构合作，OpenAI 正将其模型定位为企业级安全工具，帮助组织在攻击发生前主动保护系统。 该计划已在覆盖的项目中发现了数百个安全问题并合并了数十个补丁，在 Linux、OpenBSD、Chrome、Safari 和 Firefox 等系统中确认了多个漏洞。OpenAI 还建立了 Trusted Access for Cyber 机制，与澳大利亚、加拿大、日本及欧盟 ENISA 等政府机构开展合作，同时确保所有 AI 生成的修复方案在部署前都经过人类安全工程师的审核。

telegram · @zaihuapd · Jun 23, 01:01

**背景**: Daybreak 是 OpenAI 的综合性网络安全计划，汇集了专门的 AI 模型、Codex 编码工具和安全合作伙伴，旨在加速网络防御。CyberGym 是一个标准化评估框架，用于衡量 AI 模型的防御性网络安全能力。开源软件支撑着全球大量数字基础设施，但这些项目通常缺乏进行全面安全审计的资源，这使得 AI 辅助漏洞检测成为一种具有变革性潜力的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/patch-the-planet/">Patch the Planet : a Daybreak initiative to support open... | OpenAI</a></li>
<li><a href="https://siliconangle.com/2026/06/22/openai-expands-daybreak-patch-planet-full-gpt-5-5-cyber-release/">OpenAI expands Daybreak with Patch the Planet and... - SiliconANGLE</a></li>
<li><a href="https://decrypt.co/367506/openai-launches-daybreak-ai-cybersecurity">OpenAI Launches Daybreak as AI Firms Expand Into Cybersecurity</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cybersecurity`, `#AI Safety`, `#GPT-5.5-Cyber`, `#Applied AI`

---