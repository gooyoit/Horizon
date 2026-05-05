---
layout: default
title: "Horizon Summary: 2026-05-05 (ZH)"
date: 2026-05-05
lang: zh
---

> From 91 items, 23 important content pieces were selected

---

1. [vLLM 发布 v0.20.1 版本，优化 DeepSeek V4 支持](#item-1) ⭐️ 8.5/10
2. [OpenAI 公布低延迟语音 AI 基础设施](#item-2) ⭐️ 8.0/10
3. [Redis 创始人用大语言模型耗时四个月开发复杂功能](#item-3) ⭐️ 8.0/10
4. [Y Combinator 持有 OpenAI 价值 50 亿美元的股份](#item-4) ⭐️ 8.0/10
5. [IBM 发布 Apache 2.0 许可的 Granite 4.1 大语言模型及量化 3B 版本](#item-5) ⭐️ 8.0/10
6. [安迪·马斯利称数据中心用地担忧被夸大](#item-6) ⭐️ 8.0/10
7. [2026 年 4 月 AI 通讯涵盖多个重要模型发布](#item-7) ⭐️ 8.0/10
8. [豆包新增付费订阅，聚焦高阶生产力功能](#item-8) ⭐️ 8.0/10
9. [马斯克诉讼中质疑 OpenAI 总裁 300 亿美元持股](#item-9) ⭐️ 8.0/10
10. [Anthropic 成立面向中型企业的 AI 服务公司](#item-10) ⭐️ 8.0/10
11. [宇树人形机器人乘民航客机，电池被没收](#item-11) ⭐️ 8.0/10
12. [英伟达因 LPDDR4 短缺提前终止部分 Jetson 产品供应](#item-12) ⭐️ 8.0/10
13. [Google 全面改版 Gemini 应用界面](#item-13) ⭐️ 8.0/10
14. [黄仁勋驳斥 Amodei 与马斯克的 AI 末日预言](#item-14) ⭐️ 8.0/10
15. [肯尼亚 AI 医疗系统对穷人多收费、富人少收费](#item-15) ⭐️ 8.0/10
16. [Grok 遭提示注入攻击致 17.5 万美元转账](#item-16) ⭐️ 8.0/10
17. [OpenClaw 登顶 GitHub 星标榜首，开通官方微博](#item-17) ⭐️ 8.0/10
18. [剂泰科技拟通过港交所 IPO 募资 21.1 亿港元](#item-18) ⭐️ 7.0/10
19. [开发者推出带预览功能的在线 AI 人声分离工具](#item-19) ⭐️ 7.0/10
20. [用户询问天翼云和 Ollama 上 GLM-5.1 的使用体验](#item-20) ⭐️ 7.0/10
21. [北大 128 周年校庆发布首部 AI 宣传片《举火》](#item-21) ⭐️ 7.0/10
22. [Telegram 群组通过 /q 命令共享 AI 助手](#item-22) ⭐️ 7.0/10
23. [预测市场利润高度集中于少数专业交易者](#item-23) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM 发布 v0.20.1 版本，优化 DeepSeek V4 支持](https://github.com/vllm-project/vllm/releases/tag/v0.20.1) ⭐️ 8.5/10

vLLM v0.20.1 是一个补丁版本，重点稳定并提升了 DeepSeek V4 大语言模型的性能，新增对 MXFP8 和 FlashInfer 单边通信的支持，并修复了多个关键错误。 该版本显著提升了在广泛使用的开源推理框架 vLLM 中运行前沿 MoE 架构大模型 DeepSeek V4 的推理效率与稳定性，有助于在生产环境中实现更快速、可靠的 AI 部署。 关键更新包括多流预注意力 GEMM 优化、通过 FlashInfer 实现的 BF16/MXFP8 全对全通信支持、基于 PTX 指令的 FP32→FP4 转换加速，以及对持久化 TopK 死锁的临时规避措施；同时还修复了多个 CUDA 图和内存管理相关的错误。

github · vllm-project/vllm · May 4, 10:36

**背景**: vLLM 是一个用于高效大语言模型推理与服务的开源库，以其 PagedAttention 技术著称。DeepSeek V4 是一种混合专家（MoE）模型，具备潜注意力和记忆痕迹（engram memory）等先进特性。FlashInfer 是一个高性能的 LLM 注意力算子内核库，而 MXFP8 是 NVIDIA Blackwell GPU 支持的一种微缩放浮点格式，可在低精度计算中保持动态范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macaron.im/blog/deepseek-v4-architecture">DeepSeek V 4 Architecture : MoE & Latent Attention... - Macaron</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer -ai/ flashinfer : FlashInfer : Kernel Library for LLM...</a></li>
<li><a href="https://pytorch.org/blog/faster-diffusion-on-blackwell-mxfp8-and-nvfp4-with-diffusers-and-torchao/">Faster Diffusion on Blackwell: MXFP8 and NVFP4 with Diffusers and TorchAO – PyTorch</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#vLLM`, `#DeepSeek`, `#inference-optimization`

---

<a id="item-2"></a>
## [OpenAI 公布低延迟语音 AI 基础设施](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/) ⭐️ 8.0/10

OpenAI 发布了一篇技术文章，深入介绍了其如何利用 WebRTC 和自定义基础设施实现大规模、亚秒级延迟的实时语音交互。 低延迟语音 AI 对于实现自然的人机对话至关重要，OpenAI 的方法为行业中的实时多模态系统树立了标杆。 OpenAI 使用 WebRTC 进行点对点媒体传输，并构建了定制组件以最小化处理延迟；其系统目标是端到端延迟低于 400 毫秒。该基础设施支持全球规模，但目前语音功能仍基于 GPT-4o 模型系列。

hackernews · Sean-Der · May 4, 19:42

**背景**: WebRTC（Web 实时通信）是一个开源框架，可在网页浏览器中直接实现音频、视频和数据的实时通信，无需插件。它广泛用于视频会议、直播，如今越来越多地应用于语音代理等实时 AI 应用。实现语音 AI 的低延迟需要语音识别、语言模型和语音合成流水线之间的紧密集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebRTC">WebRTC - Wikipedia</a></li>
<li><a href="https://webrtc.org/">WebRTC</a></li>
<li><a href="https://simplismart.ai/blog/real-time-voice-ai-sub-400ms-latency">Building Real-Time Voice AI : Inside the Infrastructure That Achieves...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 OpenAI 使用 Pion 等开源 WebRTC 库表示赞赏，但也有人指出其语音交互过于急切地打断用户说话，且当前语音模型的能力落后于前沿文本模型。还有人质疑文中提到的用户数量是否真实反映了语音功能的实际使用规模。

**标签**: `#AI`, `#Voice AI`, `#Real-time Systems`, `#WebRTC`, `#OpenAI`

---

<a id="item-3"></a>
## [Redis 创始人用大语言模型耗时四个月开发复杂功能](https://antirez.com/news/164) ⭐️ 8.0/10

Redis 创始人 Salvatore Sanfilippo（antirez）详细描述了他借助 Claude 等大语言模型耗时四个月开发 Redis array 功能的过程。他强调将 AI 作为协作伙伴，同时始终保持对开发过程的完全人工监督和控制。 这位备受尊敬的专家提供的真实案例展示了当前 AI 编程助手在复杂系统编程中的实际效用与局限性。它挑战了“氛围编程”（vibe coding）的炒作，并强调 AI 是增强而非取代熟练开发者。 Antirez 手动在终端和 LLM 界面之间传输代码，以确保深度参与每一步；他避免让 LLM 自主运行。最终实现的功能涉及重大架构决策，包含数千行代码，需要仔细审查。

hackernews · antirez · May 4, 14:23

**背景**: Redis 是一个开源的内存数据结构存储系统，可用作数据库、缓存和消息代理。它支持字符串、列表、集合等多种数据类型，近期还通过模块扩展了更多类型。“array”功能指的是一组相关键的命名空间隔离，由 A+E Networks 赞助开发。GitHub Copilot 或 Anthropic 的 Claude 等基于大语言模型的编程助手已逐渐普及，但它们在核心系统开发中的作用仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/phpredis/phpredis/blob/develop/arrays.md">phpredis/ arrays .md at develop · phpredis/phpredis · GitHub</a></li>
<li><a href="https://serenitiesai.com/articles/antirez-automatic-programming-vibe-coders-2026">Antirez on AI Coding: Redis Creator's Take on Vibe... | Serenities AI</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍认为大语言模型是有价值的协作者，但不能替代专家判断。一些人警告不要将 antirez 的成功误解为鼓励非专家完全依赖 AI，其他人则分享了使用对抗式提示来改进设计质量的方法。还有人担忧在开源项目中审查缺乏充分文档说明的大规模 AI 辅助代码提交会非常困难。

**标签**: `#AI coding assistants`, `#LLMs`, `#software engineering`, `#frontier AI applications`, `#developer tools`

---

<a id="item-4"></a>
## [Y Combinator 持有 OpenAI 价值 50 亿美元的股份](https://simonwillison.net/2026/May/5/john-gruber/#atom-everything) ⭐️ 8.0/10

John Gruber 报道称，Y Combinator 持有 OpenAI 约 0.6% 的股份，按 OpenAI 当前 8520 亿美元的估值计算，价值超过 50 亿美元。 这一披露揭示了 OpenAI 不透明的所有权结构，并凸显了 Y Combinator 等早期支持者在这家全球最有价值的人工智能公司中所持有的巨额财务权益。 按 OpenAI 公布的 8520 亿美元估值计算，0.6% 的股份价值超过 50 亿美元；该信息由 John Gruber 引述一位熟悉 OpenAI 投资者的匿名消息人士提供。

rss · Simon Willison · May 5, 00:46

**背景**: Y Combinator 是一家知名创业加速器，曾在 OpenAI 早期给予支持。OpenAI 最初于 2015 年作为非营利组织成立，2019 年转为“利润上限”（capped-profit）模式以吸引投资，同时保持其使命导向。由于 GPT-4 等模型的成功和广泛应用，其估值大幅飙升。

**标签**: `#openai`, `#y-combinator`, `#ai`, `#valuation`, `#frontier-tech`

---

<a id="item-5"></a>
## [IBM 发布 Apache 2.0 许可的 Granite 4.1 大语言模型及量化 3B 版本](https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything) ⭐️ 8.0/10

IBM 发布了采用 Apache 2.0 许可证的 Granite 4.1 开源大语言模型系列，包括 3B、8B 和 30B 参数版本。社区开发者 Unsloth 已将 3B 模型量化为 21 种 GGUF 格式，大小从 1.2GB 到 6.34GB 不等。 Apache 2.0 许可证允许商业使用和修改，极大提升了开发者和企业的可访问性。量化版本使这些模型能在消费级硬件上高效运行，从而扩大前沿 AI 在开源生态中的应用范围。 该 3B 模型在全部 21 种量化版本上均使用“生成一只骑自行车的鹈鹕 SVG”提示进行测试，但结果未显示模型大小与输出质量之间的明显关联——所有输出基本都是抽象且不准确的。全部量化文件总大小达 51.3GB。

rss · Simon Willison · May 4, 23:49

**背景**: Granite 4.1 是一系列密集型、仅解码器的大语言模型，训练数据约 15 万亿 token，支持最高 512K token 的上下文长度。GGUF（通用分组均匀量化框架）是一种量化格式，可在本地设备上实现 CPU/GPU 推理，同时减小模型体积和内存占用。IBM 的 Granite 模型专为工具调用和企业集成而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-granite/granite-4-1">Granite 4.1 LLMs: How They’re Built</a></li>
<li><a href="https://aman.ai/primers/ai/quantization/">Aman's AI Journal • Primers • Quantization</a></li>
<li><a href="https://www.ibm.com/granite">Granite | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#quantization`, `#Granite-4.1`

---

<a id="item-6"></a>
## [安迪·马斯利称数据中心用地担忧被夸大](https://simonwillison.net/2026/May/4/andy-masley/#atom-everything) ⭐️ 8.0/10

安迪·马斯利指出，人们对数据中心占用农田的担忧被夸大了：2000 年至 2024 年间，美国农民自愿出售了相当于科罗拉多州面积的农地，是 2028 年预计数据中心用地的 77 倍，但并未影响粮食供应。 这一观点挑战了 AI 伦理与可持续性讨论中的常见叙事，表明反对数据中心建设的声音可能方向错误——农地流失主要源于农业经济因素，而非科技基础设施。这有助于重新界定关于生成式 AI 物理足迹和土地政策优先级的讨论。 马斯利提到，弗吉尼亚州劳登县一块普通干草田以十倍于农业价值的价格卖给超大规模数据中心运营商，却引发了不成比例的恐慌，而全国数据显示，即便农地减少，粮食产量仍在增加。据行业估计，超大规模数据中心通常占地约 10 英亩。

rss · Simon Willison · May 4, 22:51

**背景**: 随着生成式 AI 模型规模扩大，其所需的计算资源必须部署在超大规模数据中心内，这些设施消耗大量土地、水和能源，引发了公众和政策层面对其环境与空间影响的担忧，尤其是在农村或农业地区。与此同时，数十年来，由于经济压力、城市化和农业实践变化，美国农业用地持续被转作他用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rpa.org/news/lab/the-rise-of-data-centers">RPA | The Rise of Data Centers in the Grid</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agriculture_in_the_United_States">Agriculture in the United States - Wikipedia</a></li>

</ul>
</details>

**标签**: `#ai`, `#generative-ai`, `#ai-ethics`, `#data-centers`, `#infrastructure`

---

<a id="item-7"></a>
## [2026 年 4 月 AI 通讯涵盖多个重要模型发布](https://simonwillison.net/2026/May/4/april-newsletter/#atom-everything) ⭐️ 8.0/10

2026 年 4 月的通讯重点介绍了 Opus 4.7、GPT-5.5 和 Claude Mythos 等先进 AI 模型的发布，以及大语言模型安全研究和 ChatGPT Images 2.0 的更新。其中多个模型能力增强，并伴随价格上涨。 这些进展体现了前沿 AI 的快速演进，对企业采用、AI 安全和多模态应用具有深远影响。Claude Mythos 等聚焦安全的模型表明，业界正日益重视高风险场景中的系统鲁棒性。 Opus 4.7 提供 3 倍更高分辨率视觉、更强的代码生成能力及新的成本控制功能；Claude Mythos 目前仅限私有预览，在网络安全任务上表现突出；ChatGPT Images 2.0 改进了文字渲染并支持多语言图像生成。

rss · Simon Willison · May 4, 22:38

**背景**: Anthropic 的 Claude 系列采用“宪法 AI”（Constitutional AI）技术，使模型输出符合伦理与法律准则。OpenAI 的 ChatGPT Images 基于 DALL·E 技术实现文生图功能。GPT-5.5 是 OpenAI GPT 系列的一次重要渐进式升级，可能是通往 GPT-6 的过渡版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-7">Introducing Claude Opus 4 . 7 \ Anthropic</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2 . 0 | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI models`, `#LLM research`, `#AI safety`, `#frontier AI`, `#newsletter`

---

<a id="item-8"></a>
## [豆包新增付费订阅，聚焦高阶生产力功能](https://36kr.com/p/3794799114476809?f=rss) ⭐️ 8.0/10

字节跳动旗下 AI 助手豆包将推出三档付费订阅：标准版（68 元/月）、加强版（200 元/月）和专业版（500 元/月），同时保留免费版本供日常使用。付费功能将聚焦 PPT 生成、数据分析和视频制作等高阶生产力场景。 此举表明豆包正转向对算力消耗大、价值高的 AI 服务进行商业化，呼应了行业趋势——随着模型能力提升，高级生成式 AI 功能因计算成本高昂而逐步采用付费模式。这也标志着豆包在专业 AI 生产力工具领域的竞争野心。 各档均提供年付选项，价格分别为 688 元、2048 元和 5088 元；但目前应用内尚未上线相关付费功能，官方称仍在测试阶段。字节跳动强调免费版本将永久保留，用于满足日常基础需求。

rss · 36kr · May 4, 09:49

**背景**: 豆包是字节跳动推出的大型 AI 助手，旨在与阿里通义千问、百度文心一言等模型竞争。随着生成式 AI 技术发展，企业正通过分层订阅模式平衡用户增长与运行大模型带来的高昂算力成本。

**标签**: `#AI assistant`, `#generative AI`, `#monetization`, `#ByteDance`, `#frontier AI`

---

<a id="item-9"></a>
## [马斯克诉讼中质疑 OpenAI 总裁 300 亿美元持股](https://www.ithome.com/0/946/346.htm) ⭐️ 8.0/10

在埃隆·马斯克对 OpenAI 提起的诉讼中，总裁格雷格·布罗克曼披露其持股价值约 300 亿美元，马斯克的律师据此质疑 OpenAI 管理层是否将个人财富置于非营利使命之上。 此次证词揭示了前沿人工智能发展中利润激励与非营利理想之间的关键矛盾，引发外界对全球最具影响力的 AI 实验室之一在治理、受托责任及决策动机方面的质疑。 布罗克曼提到 2017 年日记中曾思考如何积累 10 亿美元财富；马斯克律师以此指控其追求私利。布罗克曼辩称，该笔记反映的是公司在关键转折点上的战略权衡，而非贪婪。

rss · IT HOME · May 5, 01:48

**背景**: OpenAI 于 2015 年以非营利组织形式成立，旨在确保通用人工智能（AGI）造福全人类。2019 年，它设立了营利性子公司 OpenAI LP 以吸引投资，同时由原非营利董事会监督。埃隆·马斯克是早期联合创始人和捐助者，但于 2018 年退出董事会。他目前提起的诉讼指控 OpenAI 背离创始使命，过度与微软结盟，追求利润而非公共利益。

**标签**: `#OpenAI`, `#AI Governance`, `#Elon Musk`, `#Frontier AI`, `#AI Ethics`

---

<a id="item-10"></a>
## [Anthropic 成立面向中型企业的 AI 服务公司](https://www.ithome.com/0/946/337.htm) ⭐️ 8.0/10

Anthropic 与黑石、赫尔曼与弗里德曼、高盛及其他投资方合作成立了一家新的人工智能服务公司，专注于将 Claude 模型嵌入中型企业的核心业务。Anthropic 的应用 AI 工程师将与新公司团队紧密合作，开发定制化 Claude 解决方案并提供长期支持。 此举大幅降低了中型企业使用前沿 AI 能力的门槛，这类企业通常缺乏独立部署 Claude 等先进模型的资源。这也标志着 Anthropic 正在加速商业化和企业级落地，可能推动 AI 在多个行业的深度整合。 新公司面向各行业的中型企业，提供从需求评估、定制开发到长期维护的 Claude 全流程部署服务。除创始合作伙伴外，General Atlantic、Leonard Green、Apollo、GIC 和红杉资本（Sequoia Capital）等也参与了投资。

rss · IT HOME · May 5, 00:03

**背景**: Anthropic 是一家领先的人工智能实验室，以开发 Claude 系列大语言模型著称，包括 Claude Opus 4.7 和 Claude Sonnet 4.6 等高性能前沿模型。前沿 AI 模型通常指最先进的通用人工智能系统，具备复杂推理、多模态处理和智能体工作流能力，训练算力常超过 10^26 FLOPS。与面向消费者的产品不同，企业级 AI 部署需要定制化集成、安全保障和持续支持——这正是新公司旨在为中端市场解决的关键问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet 4.6 \ Anthropic</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#Enterprise AI`, `#Frontier Models`

---

<a id="item-11"></a>
## [宇树人形机器人乘民航客机，电池被没收](https://www.ithome.com/0/946/334.htm) ⭐️ 8.0/10

美国机器人租赁公司 Elite Event Robotics 为宇树 Bebop 人形机器人购买了座位，搭乘西南航空从奥克兰飞往圣地亚哥的航班，但因电池尺寸超标被航空公司没收，导致航班延误一小时。 该事件凸显了先进人形机器人在非受控环境中部署时面临的现实物流与监管障碍，表明随着具身 AI 系统进入公共基础设施，行业正经历成长阵痛。 Bebop 机器人重约 31.8 公斤（70 磅），其锂离子电池超出美国联邦航空管理局（FAA）对随身携带设备 100 瓦时的限制；尽管机器人已购买乘客座位，西南航空仍要求登机前移除电池。

rss · IT HOME · May 4, 23:30

**背景**: 宇树机器人（Unitree Robotics）总部位于中国杭州，开发了 G1 和 H1 系列等高灵活性人形机器人。Bebop 型号专为娱乐和活动场景设计。由于航空安全规定严格限制锂离子电池（因其火灾风险），大型机器人搭乘民航极为罕见。美国联邦航空管理局（FAA）通常只允许 100 瓦时以下的电池作为随身行李携带，超限需特别批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.faa.gov/hazmat/packsafe/lithium-batteries">PackSafe - Lithium Batteries | Federal Aviation Administration</a></li>
<li><a href="https://www.robotseuropa.com/Unitree-Humanoid-Robots.htm">Unitree Humanoid Robots : H1/H1-2 & G1 Specs | Robots Europa</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid robots`, `#frontier technology`, `#AI hardware`, `#logistics`

---

<a id="item-12"></a>
## [英伟达因 LPDDR4 短缺提前终止部分 Jetson 产品供应](https://www.tomshardware.com/maker-stem/nvidia-accelerates-end-of-life-for-some-jetson-ai-processors-due-to-memory-shortages-rampocalypse-sends-older-ddr4-based-modules-to-the-great-scrapheap-in-the-sky) ⭐️ 8.0/10

由于 LPDDR4 内存短缺，英伟达正加速终止多款 Jetson AI 边缘计算模块的供应，包括 TX2 NX、TX2i、AGX Xavier 32GB 工业版以及 Xavier NX 8GB 和 16GB 型号。这些产品现已标记为不可取消、不可退货（NCNR），客户须在 2026 年 7 月 1 日前下单，最后发货日期为 2027 年 7 月 15 日。 此举影响了依赖成熟 Jetson 平台的机器人和嵌入式 AI 开发者，迫使其重新设计或迁移到更新的 Orin 系列模块。同时也凸显了半导体供应链的脆弱性——尤其是老旧内存类型——可能严重阻碍边缘 AI 的大规模部署。 所有受影响的模块均采用 LPDDR4 内存，该内存目前供应紧张且价格高涨；英伟达合作伙伴 Connect Tech 已确认 NCNR 政策变更。尽管载板可能继续获得支持，但模块的长期可用性完全取决于英伟达剩余的 LPDDR4 库存。

telegram · @zaihuapd · May 4, 02:09

**背景**: 英伟达 Jetson 是一系列广泛应用于机器人、无人机和工业自动化的嵌入式 AI 计算模块。LPDDR4 是一种低功耗 DRAM 标准，常见于较旧的边缘设备，但随着厂商转向 LPDDR5，其生产正逐步减少。“RAMpocalypse”指近期全球 DRAM 短缺及价格飙升现象，尤其影响老旧内存类型。与此同时，美国出口管制已禁止英伟达向中国出售 A100/H100 等高端 AI 加速器，导致其在中国 AI 芯片市场的直接份额归零。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/maker-stem/nvidia-accelerates-end-of-life-for-some-jetson-ai-processors-due-to-memory-shortages-rampocalypse-sends-older-ddr4-based-modules-to-the-great-scrapheap-in-the-sky">Nvidia accelerates end-of-life for some Jetson AI processors due to memory shortages — RAMpocalypse sends older DDR4-based modules to the great scrapheap in the sky | Tom's Hardware</a></li>
<li><a href="https://www.cnx-software.com/2026/04/30/nvidia-phases-out-several-jetson-modules-due-to-high-lpddr4-ram-prices-and-tight-supplies/">NVIDIA phases out several Jetson modules due to high LPDDR4 RAM prices and tight supplies - CNX Software</a></li>
<li><a href="https://vava8.com/index.php?act=view&app=index&id=40989">美国禁令“生效”！黄仁勋：NVIDIA中国业务完全停滞 份额已降至0% - Vava8 发吧</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Edge AI`, `#NVIDIA Jetson`, `#Semiconductor Supply Chain`, `#AI Policy`

---

<a id="item-13"></a>
## [Google 全面改版 Gemini 应用界面](https://9to5google.com/2026/05/03/gemini-full-redesign/) ⭐️ 8.0/10

Google 推出了 Gemini AI 应用的全面视觉与功能改版，新增药丸形输入框、“+”按钮用于上传照片、文件和笔记本，并集成视频、Canvas 和深度研究等工具。模型切换器回归左上角，账号切换器则移至导航抽屉底部。 此次改版大幅优化了用户与高级 AI 功能的交互方式，使 Canvas 中的 Vibe Coding 和深度研究等强大功能更易使用。这表明 Google 正持续投入优化其前沿 AI 模型的用户体验，在易用性和功能整合方面与其他 AI 助手展开直接竞争。 iOS 版本采用了 Google 新的“Liquid Glass”视觉效果——一种能根据光线和内容动态调整的半透明材质，目前仅限部分用户使用。“查看思考步骤”功能现已移入溢出菜单，并在对话中以底部面板形式展示。

telegram · @zaihuapd · May 4, 04:03

**背景**: Gemini 是 Google 推出的一系列大型 AI 模型，其应用作为面向消费者的操作界面，支持从编程到深度研究等多种任务。Canvas 是 Gemini 内置的交互式工作区，支持“Vibe Coding”功能，用户可通过自然语言提示生成具备一定功能的代码。Liquid Glass 是一种现代 UI 设计语言，强调类似玻璃的流动半透明效果，能根据环境内容智能调整明暗，不同于传统的毛玻璃模糊效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bnext.com.tw/article/82670/gemini-canvas-2025">Gemini Canvas 功能教學｜ Canvas 是什麼？ Gemini Canvas ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Liquid_Glass">Liquid Glass - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1917975463755768346">Flutter 应该如何实现 iOS 26 的 Liquid Glass ，它为什么很难？ - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#User Interface`, `#Frontier Tech`, `#Google`

---

<a id="item-14"></a>
## [黄仁勋驳斥 Amodei 与马斯克的 AI 末日预言](https://www.businessinsider.com/jensen-huang-predictions-ai-dario-amodei-elon-musk-unemployment-humanity-2026-5) ⭐️ 8.0/10

英伟达 CEO 黄仁勋公开批评 Anthropic CEO 达里奥·阿莫迪关于 AI 将在五年内取代 50%初级白领岗位的预测，以及埃隆·马斯克声称 AI 有 20%概率毁灭人类的说法，称此类言论“荒谬”且无益。 作为全球最具影响力的 AI 硬件公司领导者，黄仁勋对 AI 末日论的否定挑战了当前主流的风险叙事，强调基于事实的讨论，可能影响公众认知、政策制定以及 AI 领域的投资方向。 黄仁勋指出一些科技 CEO 会产生“上帝情结”，夸大 AI 的短期风险，并以 Atlassian 和 Twilio 等 SaaS 公司强劲的财报表现作为反例，反驳 AI 将导致软件行业崩溃的说法。

telegram · @zaihuapd · May 4, 05:15

**背景**: 达里奥·阿莫迪是 Anthropic 的联合创始人兼 CEO，也是 AI 安全研究的重要人物，曾任职于 OpenAI。他近期预测 AI 可能在五年内使一半初级白领岗位过时。埃隆·马斯克是 xAI 创始人，也是 AI 发展的早期支持者，长期警告 AI 可能带来人类灭绝风险。黄仁勋领导的英伟达为大多数前沿 AI 模型提供 GPU 算力，在 AI 生态中扮演关键基础设施角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/roflaherty_dario-amodei-says-ai-could-displace-half-activity-7426307412900442112-XICJ">Dario Amodei Predicts AI Displaces Half of Entry-Level... | LinkedIn</a></li>
<li><a href="https://www.marketingaiinstitute.com/blog/anthropic-dario-amodei-essay">Anthropic CEO Makes Radical New AI Predictions</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI policy`, `#frontier AI`, `#AI ethics`, `#industry leadership`

---

<a id="item-15"></a>
## [肯尼亚 AI 医疗系统对穷人多收费、富人少收费](https://www.theguardian.com/global-development/2026/may/04/kenya-ai-healthcare-reforms-driving-up-costs-for-poor) ⭐️ 8.0/10

一项调查揭露，肯尼亚基于人工智能的社会健康管理局（SHA）系统在设定医保保费时，系统性高估穷人的收入、低估富人的收入，导致收费不公和医疗拒诊。尽管 IDinsight 此前已警告该方案存在缺陷，政府仍在全国推行。 该案例表明，公共服务中的偏见算法可能加剧不平等并剥夺基本医疗权利，凸显了政府政策中 AI 伦理、透明度和问责制的紧迫性。它为其他国家在社会福利系统中部署 AI 提供了警示。 该算法使用代理经济状况调查（如住房条件）来推断非正式工人的收入，这种方法被批评为不准确且不透明。超过 2000 万人注册，但仅有 500 万人缴费，部分医院出现赤字，许多患者因无力支付而被拒诊。

telegram · @zaihuapd · May 4, 10:30

**背景**: 肯尼亚于 2024 年推出社会健康管理局（SHA），旨在通过 AI 评估收入，为非正式部门工人提供分级或补贴医保，以实现全民医疗覆盖。非正式部门工人占肯尼亚劳动力的 80%以上，该系统用预测算法替代自我申报收入，以减少欺诈，但若未经严格验证，可能嵌入社会经济偏见。

**标签**: `#AI ethics`, `#algorithmic bias`, `#AI in healthcare`, `#public policy`, `#predictive algorithms`

---

<a id="item-16"></a>
## [Grok 遭提示注入攻击致 17.5 万美元转账](https://x.com/Xuegaogx/status/2051267266256551997) ⭐️ 8.0/10

2026 年 5 月 4 日，攻击者利用摩尔斯电码进行提示注入攻击，诱使 Grok 输出转账指令，导致 Bankrbot 转移了价值 17.5 万美元的 $DRB 代币。随后攻击者以 ETH 和 USDC 形式归还资金，未造成实际损失。 此次事件表明，当大语言模型被接入自动化金融系统时，提示注入这一已知但常被低估的漏洞可能引发真实财务风险。这凸显了在处理敏感操作的 AI 代理中建立严格输入验证和安全边界的重要性。 攻击利用了 Bankrbot 将不可信的大语言模型输出直接视为可执行财务指令的设计缺陷；事后 Grok 的交易权限已被撤销。此次转账涉及在 Base 链上转移 30 亿枚 $DRB 代币。

telegram · @zaihuapd · May 4, 15:26

**背景**: 提示注入是一种网络安全攻击，通过恶意输入覆盖 AI 模型的原始指令，从而操控其行为。像 Grok 这样的大语言模型在输出被直接用于触发外部系统（如交易机器人或 API）操作且未经适当过滤时尤其脆弱。Bankrbot 是一个与加密货币协议集成的 AI 交易代理，用于执行代币兑换和自动化交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://grokipedia.com/page/bankrbot">Bankrbot</a></li>
<li><a href="https://grokipedia.com/page/Prompt_injection_attacks_on_robots">Prompt injection attacks on robots</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Prompt Injection`, `#Grok`, `#LLM Risks`, `#DeFi`

---

<a id="item-17"></a>
## [OpenClaw 登顶 GitHub 星标榜首，开通官方微博](https://t.me/zaihuapd/41212) ⭐️ 8.0/10

AI 开源项目 OpenClaw 开通了官方微博，并宣布其 GitHub 星标数已达 25.2 万，超越 React，成为全球星标数最多的软件仓库。 这一里程碑表明社区对开放、普惠的 AI 工具的高度认可，凸显 OpenClaw 在推动前沿 AI 技术大众化方面的影响力。其崛起也反映了开源 AI 生态系统的整体发展势头。 OpenClaw 在发布 2026.3.1 版本后达到 25.2 万星标，明确表示其使命是“让人人都能解锁 AI 无穷能力”，并计划通过新微博账号同步技术进展。

telegram · @zaihuapd · May 4, 23:52

**背景**: GitHub 星标数是衡量开源项目受欢迎程度和社区关注度的常用指标。此前长期位居榜首的是用于构建用户界面的 JavaScript 库 React，星标数超过 20 万。OpenClaw 似乎是一个新兴的 AI 开源项目，正迅速获得广泛关注。

**标签**: `#AI`, `#open-source`, `#GitHub`, `#frontier tech`, `#developer tools`

---

<a id="item-18"></a>
## [剂泰科技拟通过港交所 IPO 募资 21.1 亿港元](https://36kr.com/newsflashes/3795702003981319?f=rss) ⭐️ 7.0/10

剂泰科技（北京）股份有限公司计划通过香港 IPO 发行 2.01 亿股，每股定价 10.50 港元，预计募资 21.1 亿港元（约合 2.69 亿美元），并于 5 月 13 日正式挂牌上市。 此次 IPO 是亚洲 AI 驱动药物研发领域的重要里程碑，剂泰科技有望成为首家上市的 AI 药物递送公司，反映出资本市场对 AI 与生物医药前沿交叉领域的信心日益增强。 本次发行由杰富瑞、德意志银行和中信证券联合保荐。根据其 PHIP 版招股书，剂泰科技 2025 年营收为 1.05 亿元人民币。

rss · 36kr · May 5, 01:48

**背景**: 剂泰科技将人工智能与药物研发相结合，专注于 AI 驱动的药物递送系统。该公司利用机器学习优化治疗分子在体内的配方与递送方式，旨在提高药效并减少副作用。近年来，AI 在生物医药领域的应用在全球范围内迅速发展，被视为加速药物发现、降低研发成本的关键技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KQTBVRNN0511A0EF.html">剂 泰 科 技 通过上市聆讯：将成AI药物递送第一股_手机网易网</a></li>
<li><a href="https://plitka-msk.com/tech/20260420/4670942.shtml">剂 泰 科 技 通过港交所聆讯：2025年营收1.05亿元 | 财经快讯网</a></li>

</ul>
</details>

**标签**: `#AI in biotech`, `#drug discovery`, `#IPO`, `#frontier technology`, `#artificial intelligence`

---

<a id="item-19"></a>
## [开发者推出带预览功能的在线 AI 人声分离工具](https://www.v2ex.com/t/1210266#reply0) ⭐️ 7.0/10

一位开发者发布了一款轻量级在线工具“AI Vocal Remover”，利用 AI 从上传的音频中分离人声和伴奏，并强调在浏览器中预览效果后再下载。该工作流优先让用户评估分离质量，而非直接输出文件。 该工具体现了以用户为中心的 AI 应用设计理念，满足了练歌或音频剪辑等场景中对结果质量的实际需求。同时，它通过明确说明 AI 的局限性，展现了负责任的产品设计。 该工具使用第三方 AI 人声分离模型处理音频，仅在用户预览人声和伴奏两个音轨后才允许下载。它明确说明输出质量受原始音频、混音方式和模型性能影响，并提醒用户仅上传有权处理的内容。

rss · V2EX · May 5, 01:29

**背景**: 得益于 Demucs 和 Spleeter 等模型的发展，AI 驱动的音频源分离（尤其是人声与伴奏分离）已变得越来越普及。这类工具被音乐人、内容创作者和教育者广泛用于混音、练习或分析。与专业数字音频工作站（DAW）不同，基于网页的音轨分离工具更注重易用性和无需安装的即时访问体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://voice.ai/tools/stem-splitter">Free Online AI Stem Splitter - Separate Instruments From... - Voice.ai</a></li>
<li><a href="https://stemsplitter.online/">Free AI Music Stem Splitter - Online Audio Track Separation</a></li>
<li><a href="https://audioenhancer.ai/stem-splitter/">AI Stem Splitter - Isolate Instruments from Song - 100% Free</a></li>

</ul>
</details>

**标签**: `#AI`, `#audio processing`, `#vocal separation`, `#web tool`, `#machine learning`

---

<a id="item-20"></a>
## [用户询问天翼云和 Ollama 上 GLM-5.1 的使用体验](https://www.v2ex.com/t/1210261#reply2) ⭐️ 7.0/10

一位开发者在社区中询问近期在天翼云或 Ollama Cloud 上使用 GLM-5.1 的实际体验，特别关注工作日高峰时段的可用性、速度和稳定性。 对于开发 AI 应用的开发者而言，能否稳定、快速地调用 GLM-5.1 等前沿大模型至关重要；云平台的推理性能直接影响开发效率和最终用户体验。 该问题特别聚焦于新发布的 GLM-5.1 大模型，并针对天翼云（中国电信）和 Ollama Cloud 这两个提供大模型托管服务的平台。

rss · V2EX · May 5, 00:53

**背景**: GLM-5.1 是由智谱 AI 开发的通用语言模型（GLM）系列的一个版本，以出色的中文能力著称，在开源和闭源大模型中均具竞争力。天翼云是中国电信旗下的主流云服务商，而 Ollama 是一个开源框架，也提供云端服务，支持本地或远程运行大语言模型。

**标签**: `#AI`, `#large language models`, `#cloud inference`, `#GLM`, `#Ollama`

---

<a id="item-21"></a>
## [北大 128 周年校庆发布首部 AI 宣传片《举火》](https://www.ithome.com/0/946/340.htm) ⭐️ 7.0/10

北京大学于 5 月 4 日建校 128 周年之际，发布了首部 AI 生成的宣传片《举火》，片中呈现了学校的重要历史事件、知名校友和重大科研成果。 此举标志着中国顶尖高校将前沿 AI 技术融入机构叙事的重要尝试，体现了学术界在媒体制作和文化表达中日益广泛地应用人工智能的趋势。 该视频完全由 AI 工具生成，但未披露所使用具体模型或技术流程；内容包含富有诗意的旁白，并以视觉形式展现了北大在国家发展和科技进步中的历史贡献。

rss · IT HOME · May 5, 00:50

**背景**: 北京大学创建于 1898 年，初名京师大学堂，是中国近代第一所国立综合性大学。辛亥革命后于 1912 年更名为北京大学。1952 年全国高校院系调整后，北大成为以文理基础教学与研究为主的顶尖综合性大学，在中国的思想、政治和科技发展中具有重要地位。

**标签**: `#AI`, `#frontier tech`, `#university`, `#AI video generation`, `#China`

---

<a id="item-22"></a>
## [Telegram 群组通过 /q 命令共享 AI 助手](https://t.me/zaihuapd/41197) ⭐️ 7.0/10

一个 Telegram 群组允许所有成员使用 /q 命令，让 AI 回复特定消息。每位用户每天可免费使用两次，超出次数需消耗通过签到或发言排行获得的积分。 这展示了在消息平台中由社区驱动的 AI 实际应用，使 AI 助手无需中心化控制即可被广泛使用。这反映了将轻量级 AI 工具直接嵌入社交沟通场景的日益增长趋势。 用户需回复某条具体消息并输入 /q 才能触发 AI 回复。每日两次的免费使用限制旨在防止滥用，同时满足大多数用户的日常需求。

telegram · @zaihuapd · May 4, 02:34

**背景**: Telegram 支持响应 /q 等斜杠命令的机器人，便于第三方集成。消息应用中的 AI 助手通常利用自然语言处理技术理解上下文并生成相关回复。ManyChat 和自定义 Python 机器人常被用于部署此类功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kmfinfotech.com/blogs/integrating-ai-in-messaging-apps-revolutionizing-user-interaction-and-support/">Integrating AI in Messaging Apps : Revolutionizing User Interaction...</a></li>
<li><a href="https://grokipedia.com/page/Python_Telegram_Bot_Commands">Python Telegram Bot Commands</a></li>
<li><a href="https://www.piax.org/en/gpts/app-integrator/E33vZlDd">App Integrator - Guide to ChatGPT and Messaging App Integration</a></li>

</ul>
</details>

**标签**: `#AI assistant`, `#Telegram bot`, `#applied AI`, `#user interface`, `#AI integration`

---

<a id="item-23"></a>
## [预测市场利润高度集中于少数专业交易者](https://www.wsj.com/finance/investing/polymarket-kalshi-betting-profits-prediction-markets-eb23ac11) ⭐️ 7.0/10

《华尔街日报》调查发现，在 Polymarket 和 Kalshi 等预测市场上，前 0.1%的账户攫取了 67%的总利润，而超过 70%的散户交易者亏损。专业交易者利用 AI 算法、专有数据流和高频交易策略主导市场。 这表明 AI 和算法优势正在重塑预测市场这类小众金融场所，加剧了机构与散户之间的不平等。同时也引发人们对市场公平性、透明度以及其作为集体预测工具有效性的质疑。 在 Polymarket 上，仅 0.1%的账户赚取了三分之二的利润；在 Kalshi 上，亏损者与盈利者比例接近 3:1。某些散户热衷的市场（如押注政治人物言论提及）回报率甚至低于拉斯维加斯老虎机。

telegram · @zaihuapd · May 4, 09:45

**背景**: 预测市场允许参与者对现实世界事件（如选举或经济指标）的结果下注，其价格反映隐含概率。Polymarket（基于加密货币）和 Kalshi（受美国商品期货交易委员会监管）等平台迅速发展，吸引了普通用户和专业量化交易者。这类市场常被宣传为聚合分散信息的工具，但其有效性依赖于参与者的多样性和激励机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket - Wikipedia</a></li>
<li><a href="https://polymarket.com/">Polymarket | The World's Largest Prediction Market</a></li>

</ul>
</details>

**标签**: `#AI in finance`, `#prediction markets`, `#algorithmic trading`, `#data-driven investing`, `#market inequality`

---