---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> From 118 items, 11 important content pieces were selected

---

1. [Thinking Machines Lab 发布 975B 参数多模态开源权重模型 Inkling](#item-1) ⭐️ 10.0/10
2. [Kimi 发布 K3：2.8 万亿参数的全球最强开源模型](#item-2) ⭐️ 10.0/10
3. [Bun 用 AI 将 Zig 重写为 Rust、腾讯 Hook 拦截 Agent 越权、NVIDIA Nemotron 登顶检索榜](#item-3) ⭐️ 9.0/10
4. [日本购 2.75 万块英伟达 Rubin 芯片打造机器人主权 AI](#item-4) ⭐️ 9.0/10
5. [LM Studio 推出 Bionic：面向开源模型的 AI 智能体](#item-5) ⭐️ 8.0/10
6. [消息称谷歌旗舰 AI 模型 Gemini 3.5 Pro 因编程能力不足延期数月](#item-6) ⭐️ 8.0/10
7. [Firefox 被编译为 WebAssembly，可在浏览器中运行完整浏览器](#item-7) ⭐️ 8.0/10
8. [新 ChatGPT 应用展示电脑操控与内置浏览器功能](#item-8) ⭐️ 8.0/10
9. [智谱 AI 的 ARR 达到 10 亿美元，半年内增长 15 倍](#item-9) ⭐️ 8.0/10
10. [台积电再投千亿美元赴美建厂，Q2 利润飙升 77%创历史新高](#item-10) ⭐️ 8.0/10
11. [月之暗面 Kimi K3 模型或即将发布，搜索引擎缓存提前泄露](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Thinking Machines Lab 发布 975B 参数多模态开源权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 10.0/10

由前 OpenAI 首席技术官 Mira Murati 创立的 Thinking Machines Lab 发布了其首个开源权重模型 Inkling。这是一个庞大的混合专家多模态模型，总参数量达 9750 亿（激活参数 410 亿），在覆盖文本、图像、音频和视频的 45 万亿 token 上完成训练，并以宽松的 Apache-2.0 许可证发布。 此次发布为美国开源权重生态系统引入了一个强大的新竞争者，为补充现有的 NVIDIA Nemotron、Gemma 4 以及来自中国的竞争模型提供了可行选择。它还确立了 Thinking Machines Lab 在 AI 领域的重要地位，并提供了一个针对其 Tinker 平台进行微调而优化的强大基础模型。 该实验室坦言，Inkling 并非前沿模型，也不是目前可用的最强模型；相反，它被设计为用于定制的强大基础模型。值得注意的是，与行业预期相比，其模型卡和训练数据文档异常简略，除了声明包含公开可用的互联网内容外，几乎没有透露所使用数据集的具体信息。

rss · Simon Willison · Jul 16, 15:35

**背景**: 混合专家架构通过在处理任何给定输入时仅激活模型参数的一个子集来提高效率，从而允许实现庞大的总参数量，同时将计算成本保持在可控范围内。“开源权重”一词是指公开发布已训练参数权重的 AI 模型，但通常不提供底层的训练代码、方法和全面的数据细节，这与完全的“开源”AI 有所区别。模型卡是一种结构化文档，旨在提供有关 AI 模型架构、训练数据、性能和局限性的透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://www.adaline.ai/blog/what-is-the-difference-between-open-source-and-open-weight-models">What is the difference between open-source and open-weight ...</a></li>
<li><a href="https://aisecurityandsafety.org/it/guides/model-cards-documentation/">Model Cards & AI Documentation: Best Practices Guide (2026)</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Open-Weights`, `#Thinking Machines Lab`, `#Multimodal AI`, `#Mixture-of-Experts`

---

<a id="item-2"></a>
## [Kimi 发布 K3：2.8 万亿参数的全球最强开源模型](https://aihot.virxact.com/items/cmro7equy004rbitothere2b4) ⭐️ 10.0/10

Kimi 发布了 K3，这是一个拥有 2.8 万亿参数、100 万 token 上下文窗口的原生多模态开源模型。该模型在全球开源模型中排名第一，综合表现仅弱于 Claude Fable 5 和 GPT 5.6 Sol 等顶级闭源模型，并在 Frontend Code Arena 中以 1679 分位居榜首。 此次发布为开源 AI 社区树立了新的标杆，证明了开源权重模型已经能够紧逼顶级闭源系统的性能。这也表明中国 AI 实验室正在大力推进前沿智能的商品化，进一步加剧了全球大语言模型领域的竞争。 K3 基于 Kimi Delta Attention 与 Attention Residuals 架构，采用稀疏混合专家设计，在 896 个专家中仅激活 16 个，相比 K2 的扩展效率提升了约 2.5 倍。该模型目前已上线 Kimi 官网及 API，输入和输出 token 的定价分别为每百万 3 美元和 15 美元，完整权重预计将于 2026 年 7 月 27 日前开放。

rss · AI Hot · Jul 17, 00:22

**背景**: Kimi Delta Attention (KDA) 是一种混合线性注意力机制，旨在高效管理循环记忆，使模型能够处理超长上下文，同时避免传统注意力机制的巨大计算开销。Attention Residuals 是一种架构升级，它用注意力机制取代了网络层间固定的信息累积，从而缓解了信息稀释问题并有效提升了计算效率。Frontend Code Arena 是一个基准测试平台，通过基于真实编程任务的 Elo 风格人类投票，根据开发者的实际偏好对 AI 模型进行排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention-kda">Kimi Delta Attention : Efficient Long-Context Models</a></li>
<li><a href="https://medium.com/@himanshusamariya777/attention-residuals-the-most-elegant-idea-in-deep-learning-right-now-44c395c23a66">Attention Residuals : The Most Elegant Idea in Deep... | Medium</a></li>
<li><a href="https://cryptobriefing.com/kimi-k3-moonshot-ai-frontend-code-arena/">Kimi K3 by Moonshot AI ranks No. 1 in Frontend Code Arena ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出，尽管 K3 每百万 token 3/15 美元的定价对于中国的开源权重模型来说极高，但如果它确实能提供与 Anthropic Sonnet 系列相媲美的前沿性能，这一定价是合理的。一些开发者观察到，中国实验室正在积极推动 AI 智能的商品化，这可能是为了将核心价值驱动转向硬件和基础设施。早期的技术测试（例如通过 API 渲染复杂的 SVG）展示了其强大的能力，但也凸显了其高昂的推理 token 消耗，使其成为运行成本相对较高的模型。

**标签**: `#Kimi K3`, `#Open Source AI`, `#Large Language Models`, `#Multimodal AI`, `#Frontier AI`

---

<a id="item-3"></a>
## [Bun 用 AI 将 Zig 重写为 Rust、腾讯 Hook 拦截 Agent 越权、NVIDIA Nemotron 登顶检索榜](https://aihot.virxact.com/items/cmro7zjg500e5bito3o52qbg1) ⭐️ 9.0/10

Bun 的作者使用 Anthropic 的 Fable 模型，在 11 天内花费 16.5 万美元将 53.5 万行 Zig 代码重写为 Rust，动机是解决内存安全问题。此外，腾讯 DECO 平台推出了基于 Hook 切面的 Agent 框架，可在代码级拦截 LLM 处理长脚本时的偷懒与越权行为；NVIDIA 则开源了 Nemotron 3 Embed 嵌入模型族，8B 版本以 78.5% 的成绩在 RTEB 多语言检索榜排名第一。 这三项进展分别代表了 AI 辅助软件工程、Agent 安全和信息检索领域的重大突破。Bun 的重写证明 AI 已能大规模处理真实代码库的迁移，腾讯的框架应对了 LLM Agent 越权滥用这一新兴安全威胁，而 NVIDIA 的开源嵌入模型则为多语言搜索应用提供了新的最优选择。 NVIDIA 还推出了针对 Blackwell 架构优化的 NVFP4 版本 Nemotron 3 Embed，吞吐量翻倍且精度保留 99% 以上，该版本利用了专为 Blackwell GPU 架构设计的 4 位浮点格式。Bun 的重写专门出于 Rust 相比 Zig 在内存安全方面的优势，整个 53.5 万行代码的迁移成本低于许多传统咨询项目的费用。

rss · AI Hot · Jul 17, 00:01

**背景**: 嵌入模型将文本转换为数值向量，使语义搜索和检索增强生成（RAG）系统能够找到相关信息。NVFP4 是 NVIDIA Blackwell GPU 架构引入的 4 位浮点格式，张量被编码为 16 个 4 位值组成的块并附带 FP8 缩放因子，使大模型能在有限的显存中高效运行。Zig 和 Rust 都是系统编程语言，但 Rust 的借用检查器在编译时提供更强的内存安全保证，能消除整类内存错误。LLM Agent 安全是一个新兴领域，旨在应对 AI Agent 在处理复杂任务时可能超出预期权限或采取危险捷径的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision ...</a></li>
<li><a href="https://0xsero.github.io/blackwell-gpu-wiki/blackwell/nvfp4-deep-dive/">NVFP4 deep dive - Blackwell GPU Wiki - 0xsero.github.io</a></li>
<li><a href="https://www.tencentcloud.com/product/adp?lang=en">Tencent Cloud Agent Development Platform</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#LLM Coding`, `#NVIDIA Nemotron`, `#AI Security`, `#Code Translation`

---

<a id="item-4"></a>
## [日本购 2.75 万块英伟达 Rubin 芯片打造机器人主权 AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 9.0/10

Japan is investing $2.4 billion to purchase 27,500 next-generation Nvidia Rubin chips to build a sovereign AI infrastructure and develop foundation models specifically for robotics.

telegram · @zaihuapd · Jul 16, 10:59

**标签**: `#Nvidia Rubin`, `#Sovereign AI`, `#Robotics`, `#AI Infrastructure`, `#Embodied AI`

---

<a id="item-5"></a>
## [LM Studio 推出 Bionic：面向开源模型的 AI 智能体](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio 发布了全新的 AI 智能体应用 Bionic，旨在利用开源模型直接执行编程、研究和复杂文档处理等实际任务。用户可以在本地运行模型以保护隐私，也可以无缝切换到 LM Studio 的安全云服务，调用 Kimi Coder K2.7 和 GLM 5.2 等大型前沿开源模型来处理更繁重的工作。 此次发布标志着 LM Studio 从广受欢迎的本地聊天界面正式转型为成熟的智能体工作流平台，将直接与企业级 AI 编程和生产力工具展开竞争。通过将本地执行的隐私优势与云端托管开源模型的强大算力相结合，Bionic 为 OpenAI 的 ChatGPT 或 Anthropic 的 Claude 等封闭生态系统提供了一种灵活且高性价比的替代方案。 Bionic 将工作划分为特定的项目类型，例如用于编程的 "Code" 项目和用于文档创建的 "Work" 项目，后者在智能体每次更改时都会进行自动存档。尽管 LM Studio 承诺在其安全云服务中不保留或利用用户数据进行训练，但用户需注意，连接到第三方前沿云端模型时，数据隐私政策可能会有所不同。

hackernews · minimaxir · Jul 16, 20:18 · [社区讨论](https://news.ycombinator.com/item?id=48939662)

**背景**: 传统的 LLM 界面主要充当对话式聊天机器人，通过预测下一个词来回答问题。相比之下，AI 智能体能够自主规划、使用工具并执行多步骤工作流以实现复杂目标，这代表了软件运行方式的变革性转变。在用户自己的硬件上本地运行这些模型可以最大程度地保护隐私并支持离线使用，而借助云端托管的模型则能让用户突破硬件限制，访问更强大、更前沿的大型模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models | LM Studio Blog | LM Studio</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for open models - 9to5Mac</a></li>
<li><a href="https://medium.com/@speaktoharisudhan/llms-vs-ai-agents-what-is-the-actual-difference-cebd4cb789cd">LLMs vs AI Agents : What Is The Actual Difference | by Harisudhan.S | Medium</a></li>

</ul>
</details>

**社区讨论**: 创始人 Yagil 正积极提供免费云额度，邀请用户使用 GLM 5.2 和 Kimi Coder K2.7 等前沿模型测试 Bionic，并重点展示了其编程和文档处理能力。社区正在讨论该平台的竞争优势，一些人认为它是企业控制 LLM 使用成本的理想打包方案，而另一些人则对向云端商业模式的转变表示担忧，并质疑连接到外部云端模型时的实际数据隐私安全性。

**标签**: `#AI Agents`, `#Open Source Models`, `#Developer Tools`, `#Local LLMs`, `#LM Studio`

---

<a id="item-6"></a>
## [消息称谷歌旗舰 AI 模型 Gemini 3.5 Pro 因编程能力不足延期数月](https://aihot.virxact.com/items/cmro7ta9y00arbitodlaockok) ⭐️ 8.0/10

谷歌即将推出的旗舰 AI 模型 Gemini 3.5 Pro 据报道已延期数月，原因是其编程表现未达到内部预期。公司已尝试通过更换部分训练数据来改善该模型的编程能力，但测试结果仍未达到预期目标。 此次延期凸显了 AI 实验室在突破模型能力边界（尤其是在复杂推理和编程任务方面）时所面临的巨大技术挑战。这也表明谷歌在竞争激烈的前沿 AI 竞赛中可能面临被动，因为 Anthropic 和 OpenAI 等竞争对手正在快速推出更强大的新模型。 性能不足的问题具体集中在模型的编程能力上，这是用于软件开发领域的现代 AI 助手的关键指标。据报道，持续的延期和未达预期的测试结果已在谷歌内部引发了不满情绪，员工担忧公司会丧失竞争优势。

rss · AI Hot · Jul 16, 23:57

**背景**: 谷歌的 Gemini 是一系列多模态大语言模型，旨在处理和生成文本、代码、图像和音频。其中 "Pro" 级别代表了专为复杂推理任务设计的高算力模型，直接与 OpenAI 的 GPT 系列和 Anthropic 的 Claude 模型竞争。编程能力已成为 AI 实验室的关键竞争领域，因为在该领域的强劲表现不仅展示了先进的逻辑推理能力，还能吸引利润丰厚的企业开发者用户群体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_3_Pro">Gemini 3 Pro</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#AI Models`, `#AI Competition`, `#Frontier AI`

---

<a id="item-7"></a>
## [Firefox 被编译为 WebAssembly，可在浏览器中运行完整浏览器](https://aihot.virxact.com/items/cmro5qjt300y7bikncwml93rm) ⭐️ 8.0/10

Puter 使用 emscripten 成功将 Firefox/Gecko 浏览器引擎编译为 WebAssembly，使完整的 Firefox 浏览器能在任何标准浏览器标签页中运行。该项目大量借助 Claude Opus AI，消耗了价值约 25,000 美元的 Claude Max 订阅 token 来完成这一复杂的工程壮举。 该项目展示了使用 WebAssembly 实现完整浏览器嵌套虚拟化的可行性，同时展示了现代 AI 编程助手在软件工程方面的高级能力。它推动了浏览器虚拟化技术和 AI 辅助开发的边界，证明像 Claude Opus 这样的 AI 模型能够应对极其复杂的编译和移植挑战。 所有网络流量通过 Wisp 协议的 WebSocket 连接经 Puter 服务器代理，并支持端到端加密。Wisp 协议是一种低开销机制，旨在通过单个 WebSocket 连接代理多个 TCP 和 UDP 套接字，非常适合这种浏览器嵌套网络架构。

rss · AI Hot · Jul 16, 23:34

**背景**: WebAssembly（Wasm）是一种二进制指令格式，能使高性能应用在浏览器中以接近原生的速度运行。Gecko 是 Mozilla 开发的浏览器引擎，为 Firefox 提供动力，负责网页渲染和 Web 内容执行。Emscripten 是一个将 C 和 C++ 代码编译为 WebAssembly 的工具链，此处用于将 Gecko 引擎的原生代码库移植到浏览器环境中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HeyPuter/firefox-wasm">HeyPuter/firefox-wasm: Firefox in WebAssembly - GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gecko_(software)">Gecko (software) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#AI-Assisted Coding`, `#Browser Virtualization`, `#Claude`, `#Frontier Tech`

---

<a id="item-8"></a>
## [新 ChatGPT 应用展示电脑操控与内置浏览器功能](https://aihot.virxact.com/items/cmro58tvv00nnbiknv4gfck1v) ⭐️ 8.0/10

@dkundel 的一项新演示展示了 ChatGPT 桌面应用自主控制电脑应用程序的能力，该应用利用内置浏览器进行研究、网页导航以及与用户协作完成任务。这紧随 ChatGPT 电脑操控模式的最新推出，该模式允许 AI 直接控制鼠标并与桌面软件进行交互。 这代表了前沿 AI 代理能力的一次重大飞跃，从对话式助手转变为能够直接在用户桌面上执行复杂工作流程的自主操作者。通过将感知、决策和对标准软件界面的控制结合起来，这项技术有望从根本上改变我们处理日常数字任务和网络自动化的方式。 内置浏览器允许 AI 自主浏览网站并收集信息，而无需用户切换上下文。电脑操控功能依赖于 AI 执行鼠标点击、按键输入和其他系统事件等低级操作，从而操纵图形用户界面。

rss · AI Hot · Jul 16, 23:29

**背景**: 电脑操控代理（ACUs）是一类新兴的 AI 系统，能够根据自然语言指令在数字设备上执行复杂任务。OpenAI 一直在开发其电脑操控代理（CUA）技术，作为 AI 与数字世界交互的通用接口，为 Operator 等应用提供支持。这些代理结合了感知、决策和控制能力，可以自动化完成传统上需要人类通过鼠标和键盘干预的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent - OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2501.16150">A Comprehensive Survey of Agents for Computer Use ...</a></li>
<li><a href="https://www.pcworld.com/article/3190769/chatgpt-can-now-control-your-whole-desktop-i-tested-it-with-chess.html">ChatGPT can now control your whole desktop. I tested it with ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#ChatGPT`, `#Computer Use`, `#Web Automation`, `#Frontier AI`

---

<a id="item-9"></a>
## [智谱 AI 的 ARR 达到 10 亿美元，半年内增长 15 倍](https://36kr.com/newsflashes/3899038887643012?f=rss) ⭐️ 8.0/10

这一里程碑表明，中国 AI 公司能够实现与西方顶级实验室相媲美的商业化速度——智谱从 1 亿美元增长到 10 亿美元 ARR 仅用了 5 个月，而 Anthropic 用了 15 个月。这证明了即使在企业订阅市场不够成熟的环境下，强大的产品市场契合度和前沿模型竞争力依然能够推动大规模的收入增长。 智谱的成功很大程度上得益于其早期对代码能力的押注，每两个月发布一次旗舰模型，其中开源的 GLM-5.2 在多项基准测试中追平甚至超过了 Claude Opus 4.8 和 GPT-5.5。2026 年 6 月，该公司市值突破 1 万亿港元，年内股价涨幅超过 2000%，反映出投资者极大的信心。

rss · 36kr · Jul 17, 01:07

**背景**: 年度经常性收入（ARR）是基于订阅的 SaaS 公司使用的一项关键指标，用于衡量在 12 个月内标准化的可预测经常性收入总额。智谱 AI 是中国领先的 AI 实验室，以其通用语言模型（GLM）系列而闻名，该系列已从开源架构发展为具备高级推理和智能体代码能力的前沿模型。该公司的战略与更广泛的行业趋势相一致，即像 Anthropic 的 Claude Code 这样的 AI 编程工具，通过直接提升开发者生产力，已成为创收能力最强的 AI 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.paddle.com/resources/annual-recurring-revenue">What is annual recurring revenue (ARR) and how to calculate it</a></li>
<li><a href="https://glm5.ai/">GLM-5 - Zhipu AI's Flagship Foundation Model</a></li>
<li><a href="https://www.anthropic.com/features/making-of-claude-code">The Making of Claude Code \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Zhipu AI`, `#AI Industry`, `#ARR`, `#GLM`, `#AI Monetization`

---

<a id="item-10"></a>
## [台积电再投千亿美元赴美建厂，Q2 利润飙升 77%创历史新高](https://www.reuters.com/world/asia-pacific/tsmcs-second-quarter-profit-seen-hitting-record-ai-boom-2026-07-15/) ⭐️ 8.0/10

台积电宣布向美国亚利桑那州追加投资 1000 亿美元建厂，加上此前已宣布的 1650 亿美元，在美投资规模进一步扩大。同时公布的二季度财报显示，净利润同比飙升 77%至 7066 亿新台币（约 220 亿美元），远超市场预期的 6326 亿新台币。 这项大规模扩张凸显了 AI 算力热潮正在重塑全球半导体供应链，台积电进一步巩固了其作为 AI 芯片关键制造核心的地位。创纪录的利润和上调的资本支出指引表明，公司对 AI 驱动的多年需求增长充满信心。 台积电将 2026 年资本支出预测上调至 600 亿至 640 亿美元，预计全年美元营收将增长略超 40%。亚利桑那州目前已有 8 座工厂在建或规划中，未来可能再增加 4 座。

telegram · @zaihuapd · Jul 16, 12:29

**背景**: 台积电是全球最大的晶圆代工企业，为苹果、NVIDIA、AMD 等公司生产先进半导体芯片。受地缘政治压力和美国《芯片法案》等政府激励措施的影响，台积电一直在将制造能力扩展到台湾以外地区。AI 加速器和数据中心芯片的需求激增推动了半导体行业前所未有的增长，台积电作为先进制程节点的主导生产商，成为这一趋势的最大受益者。

**标签**: `#TSMC`, `#AI Infrastructure`, `#Semiconductors`, `#Chips`, `#Data Centers`

---

<a id="item-11"></a>
## [月之暗面 Kimi K3 模型或即将发布，搜索引擎缓存提前泄露](https://t.me/zaihuapd/42616) ⭐️ 8.0/10

搜索引擎缓存曝光了月之暗面 Kimi 开放平台上的促销活动页面，暗示全新的 Kimi K3 模型可能即将发布。泄露的页面提到了与 K3 发布相关的限时充值活动，表明发布时间已近在咫尺。 据报道，Kimi K3 拥有 2.8 万亿参数，将成为中国最大的开源权重 AI 模型，并有望与美国顶尖前沿模型展开有力竞争。该模型的发布标志着全球大语言模型军备竞赛的进一步升级，月之暗面旨在缩小与 Anthropic、OpenAI 等西方领先 AI 实验室之间的差距。 根据此前报道，Kimi K3 的参数量在 2 万亿至 3 万亿之间，并支持 100 万 token 的上下文窗口。该模型预计将以开源权重的形式发布，延续了中国 AI 实验室通过开源策略构建全球开发者生态系统的趋势。

telegram · @zaihuapd · Jul 16, 13:47

**背景**: 月之暗面是一家总部位于北京的 AI 创业公司，由具有清华大学背景的杨植麟于 2023 年创立。该公司获得了阿里巴巴等主要投资者的支持，并因其 Kimi 智能助手在处理超长文本方面的卓越能力而声名鹊起。'Moonshot' 这个名字的灵感来源于平克·弗洛伊德的音乐专辑《月之暗面》，公司的既定使命是构建通向通用人工智能（AGI）的基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/">Moonshot's upcoming Kimi 3 is expected to close the gap with Anthropic's Opus 4.8 | TechCrunch</a></li>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K3? Moonshot's 2.8T, 1M-Context Flagship</a></li>
<li><a href="https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems">China’s Moonshot AI releases Kimi K3, the largest open-source model ever, rivaling top U.S. systems | VentureBeat</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Moonshot AI`, `#Kimi K3`, `#LLM`, `#AI Industry News`

---