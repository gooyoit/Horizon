---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> From 113 items, 13 important content pieces were selected

---

1. [OpenAI 将全双工语音模型 GPT-Live-1 引入 API](#item-1) ⭐️ 9.0/10
2. [DeepSeek 发布 MIT 协议开源 Harness 智能体应用并开放 DeepSeek-V4-Pro-0813 权重](#item-2) ⭐️ 9.0/10
3. [研究人员质疑 OpenAI 是否从聊天中的未发表数学成果中学习](#item-3) ⭐️ 8.0/10
4. [Cognition 发布 SWE-2 编程模型，宣称达到前沿水平](#item-4) ⭐️ 8.0/10
5. [OpenAI 发布 Agents API，托管运行 Codex harness 智能体会话](#item-5) ⭐️ 8.0/10
6. [IFM 发布 K2 Horizon：6 个开源模型覆盖 0.9B 到 375B](#item-6) ⭐️ 8.0/10
7. [消息称微软计划到 2032 年将数据中心容量提升至 38GW](#item-7) ⭐️ 8.0/10
8. [DeepSeek 发布 V4.1 Flash：更强、更快、更普惠](#item-8) ⭐️ 8.0/10
9. [中国 AI 芯片厂商涨价 20%-50%，HBM 短缺成为新瓶颈](#item-9) ⭐️ 8.0/10
10. [月之暗面（Kimi）秘密递交港股 IPO 申请，投前估值 500 亿美元](#item-10) ⭐️ 8.0/10
11. [腾讯混元开源音频编辑模型 AuK](#item-11) ⭐️ 8.0/10
12. [Anthropic 发布 2026 年 9 月威胁情报报告，披露被阻断的 Claude 滥用行动](#item-12) ⭐️ 8.0/10
13. [Suno 发布 v6：首个与音乐行业合作打造的模型](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 将全双工语音模型 GPT-Live-1 引入 API](https://aihot.news/items/cmtw91ijp080qrolklz56zi52) ⭐️ 9.0/10

OpenAI 宣布 GPT-Live-1 正式上线 API，该模型原生支持全双工对话（边听边说）、自然打断处理和抗背景噪声能力，并新增原生工具调用、自定义语音、更强的指令遵循以及电话（telephony）支持，可用于构建电话语音智能体。 这一发布使开发者可以摆脱传统“语音识别+大模型+语音合成”的高延迟拼接方案，用单一原生语音模型大幅降低延迟，让 AI 对话更接近真人体验。这对客服、呼叫中心等电话语音智能体场景是重大能力升级，也将加剧与 Retell、Telnyx 等语音 AI 平台的竞争。 GPT-Live-1 将语音理解与生成整合在同一模型中，据称采用“前端极速语音层＋后端思考委派”的解耦架构来处理工具调用，API 定价约为每分钟 0.05 美元。该模型能够优雅地处理用户打断，并在嘈杂环境中保持稳定表现。

rss · AI Hot · Sep 11, 00:28

**背景**: 传统语音智能体需要串联语音识别、大语言模型和语音合成三个独立组件，这不仅带来较高延迟（智能体通常要 600 毫秒以上才开始回应），也难以实现自然的轮流发言和打断。全双工意味着模型可以像人类一样同时听和说，从而支持“抢话”式打断和更流畅的对话。OpenAI 此前曾基于 GPT-4o 推出支持双向音频流的 Realtime API，GPT-Live-1 是这一原生语音路线的新一代演进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live-1-in-the-api/">Build more natural voice experiences with GPT‑Live‑1 in the ...</a></li>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>
<li><a href="https://www.aiposthub.com/openai-gpt-live-1-api-voice-agent/">OpenAI 推出 GPT-Live-1 API！每分鐘 0.05 美元全雙工語音與任務委派架構深度解析</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-Live-1`, `#speech AI`, `#real-time voice`, `#API`

---

<a id="item-2"></a>
## [DeepSeek 发布 MIT 协议开源 Harness 智能体应用并开放 DeepSeek-V4-Pro-0813 权重](https://t.me/zaihuapd/43738) ⭐️ 9.0/10

DeepSeek 以 MIT 协议开源发布了全新的 Harness 智能体应用，采用“一切皆插件”架构，模型、工具、技能、会话、沙箱、存储、调度和 UI 均为可替换插件。同时，DeepSeek 在 Hugging Face 上开放了 DeepSeek-V4-Pro-0813 的模型权重。 这 combining 了头部开源 AI 实验室的两大重要发布：采用宽松许可协议的智能体基础设施框架和前沿级模型权重，均可免费获取。这降低了全球开发者构建、定制和自托管有竞争力的编程智能体的门槛，也对闭源智能体平台形成了更大压力。 Harness 提供标准、PTC、极简和创造四种运行模式，底层由 Cordis 驱动，其设计在一篇关于时空可组合性的论文中有描述。据称 DeepSeek-V4-Pro-0813 在基准测试中超越了 DeepSeek-V4-Pro（Preview），支持 100 万 token 上下文窗口，与最强闭源模型基本持平；仓库已在 GitHub 和 npm 上发布。

telegram · @zaihuapd · Sep 10, 07:28

**背景**: “智能体 Harness（框架）”是包裹原始大模型、将其变成可靠智能体的工程层，负责管理工具调用、会话、沙箱和上下文，即“模型 + Harness = 智能体”的理念。多数现有框架将这些能力紧耦合，难以定制，而 DeepSeek Harness 将每种能力都实现为可替换、可重组的插件，通过 GitHub 和 npm 分发。DeepSeek 一直有高调开源模型的历史，此次发布将这一战略延伸到了智能体工具领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://huggingface.co/multimodalart/DeepSeek-V4-Pro-0813">multimodalart/ DeepSeek - V 4 - Pro - 0813 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#open-source AI`, `#AI agents`, `#model weights release`, `#frontier AI`

---

<a id="item-3"></a>
## [研究人员质疑 OpenAI 是否从聊天中的未发表数学成果中学习](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

由数学家 Andreas Thom 和 Valerio Capraro 在 mathstodon 上的帖子引发的一场 Hacker News 讨论，争论在与 OpenAI 模型协作后，OpenAI 发布了与研究人员协作成果相似的结果，OpenAI 是否值得被托付未发表的数学成果。Thom 指称这一事件类似于剽窃聊天中分享的想法。 这一事件触及研究诚信与数据使用规范的核心：如果前沿模型能记住或受私有聊天数据影响，那么与 AI 工具分享未发表成果的研究人员就面临想法被无署名吸收的风险。这影响到越来越多在开放问题上使用 ChatGPT、Codex 等工具的学者，并迫使 AI 实验室在训练数据透明度上承受压力。 OpenAI 的政策允许将用户聊天用于训练（包括人工审阅），但付费 API 和企业用户的保留条款与退出选项不同。有评论者指出，OpenAI 在得知某个重要数学证明可能已在其训练数据中后不久，就从一个仍在训练中的模型生成了约 3000 亿个输出 token，一些人认为这疑似“平行构建”。

hackernews · pred_ · Sep 10, 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: 像 Epoch AI 的 FrontierMath 这样的前沿数学基准专门使用全新的、未发表的问题，正是为了避免训练数据污染，这凸显了对未见问题的记忆会如何破坏评估的有效性。OpenAI 向大量研究人员免费开放其模型，这意味着研究开放问题的学者可能在无意中为这些允许从聊天中学习的系统提供新鲜训练素材。与人类合作者的类比是核心：如果一位人类合作者发表了源自合作却未署名的成果，将被视为极不道德。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.05382">User Privacy and Large Language Models : An Analysis of Frontier...</a></li>
<li><a href="https://epoch.ai/frontiermath">FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI</a></li>
<li><a href="https://factually.co/fact-checks/technology/openai-data-retention-deletion-policies-user-chats-92b93f">How do OpenAI 's data retention and deletion policies w...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为这种担忧是可信的：有人认为这种情况就像不道德的人类合作者未经署名就发表协作想法，另有人认为两者可能同时成立——聊天可能改善模型的潜在直觉，而基于可验证数学的强化学习也可能独立产生超人结果。还有人对 3000 亿 token 生成的时机表示怀疑，并担心 OpenAI 在开放问题上的快速进展可能部分得益于研究人员自己的新鲜聊天数据。

**标签**: `#OpenAI`, `#AI research`, `#data privacy`, `#AI math reasoning`, `#research ethics`

---

<a id="item-4"></a>
## [Cognition 发布 SWE-2 编程模型，宣称达到前沿水平](https://cognition.com/blog/swe-2) ⭐️ 8.0/10

Cognition 发布了 SWE-2，这是一款基于 Moonshot AI 的 Kimi K3（2.8 万亿参数）进行后训练的软件工程模型，宣称其得分与 Fable 5.1、GPT-5.6 Sol 等顶尖竞品相差不到一分，而成本低 64%。关键技术贡献是一种强化学习算法，可在单次训练中覆盖所有推理力度等级，并首次在数万亿参数规模上扩展了 RL。 如果宣称属实，SWE-2 将推动智能编程代理的成本-性能帕累托前沿，加剧编程模型提供商之间的价格竞争。它还证明了在现有的开放基座模型（Kimi K3）上进行强力后训练可以逼近前沿能力，这对没有巨额预训练预算的实验室意义重大。 在 FrontierCode 1.1 Main 上 SWE-2 得分 50.0%，并支持在一次 RL 训练中完成所有可配置推理力度等级。值得注意的是，Hacker News 评论者指出了明显的泛化差距：它在 Terminal Bench 2.1 上得 92.8%，但在更新的 Terminal Bench 4 上仅得 27.3%，引发了对“刷榜”的质疑；该模型也未开放权重。

hackernews · seelos · Sep 10, 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49645443)

**背景**: 后训练指在预训练基座模型上（通过微调或强化学习）进行优化，使其专精于智能软件工程等任务，而非从零训练。Kimi K3 是 Moonshot AI 的 2.8 万亿参数开放模型，具备原生视觉能力和 100 万上下文窗口。Cognition 是 Devin AI 软件工程师背后的公司，其 SWE 系列专注编程代理；Terminal Bench 等基准测试得分是比较此类模型的标准方式，但在更新的、未见过的基准版本上的表现才是检验真实泛化能力的常用方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE-2: Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://alphasignal.ai/news/cognition-s-swe-2-beats-gpt-5-6-sol-at-64-lower-cost">Cognition's SWE-2 Beats GPT-5.6 Sol at 64% Lower Cost | AlphaSignal</a></li>
<li><a href="https://ai-tldr.dev/releases/cognition-swe-2/">SWE-2 — Cognition's coding model lands within a… | AI/TLDR</a></li>
<li><a href="https://www.kimi.ai/ai-models/kimi-k3">Kimi K3: 2.8T Open Model for Coding & Knowledge Work</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者明显持怀疑态度：有人指出 Terminal Bench 2.1（92.8%）与 Terminal Bench 4（27.3%）之间的巨大差距，认为该模型可能过度拟合基准。还有人质疑缺少开放权重和模型参数信息，认为闭源权重提供商在面对 DeepSeek 等开放选项时市场正在萎缩，并回顾了 Cognition 早前 Devin 演示被夸大的历史，甚至有人直言 Devin 是一款一直很差的产品。

**标签**: `#AI models`, `#coding agents`, `#benchmark evaluation`, `#Cognition`, `#software engineering AI`

---

<a id="item-5"></a>
## [OpenAI 发布 Agents API，托管运行 Codex harness 智能体会话](https://aihot.news/items/cmtw8zcvc07s2rolkhc9wv005) ⭐️ 8.0/10

OpenAI 推出了 Agents API，让应用通过其完全托管的服务运行由 Codex harness 驱动的智能体会话。OpenAI 负责管理会话、编排、上下文压缩和恢复，而应用只需提供自己的工具并选择执行环境。 这降低了开发者构建长时间运行、可靠 AI 智能体的门槛，因为状态持久化、上下文管理和故障恢复这些最难的基础设施问题现在都由 OpenAI 处理。这也将 Codex harness 定位为一个开放平台，加剧了与其他智能体框架和编排服务提供商的竞争。 该 API 基于 Codex app-server，一个双向 JSON-RPC 接口，支持流式进度、工具调用、审批和 diff 输出。harness 负责跨轮次管理会话状态，并强制执行可配置的沙箱和审批策略；上下文压缩则减少长会话中的 token 消耗，使智能体在不丢失关键信息的情况下持续工作。

rss · AI Hot · Sep 11, 00:37

**背景**: Codex harness 是 OpenAI 为其编程智能体 Codex 构建的智能体运行时，负责管理会话状态、流式执行、调用工具以及跨轮次延续工作。OpenAI 近期将这些能力以文档化平台的形式开放（"Codex as a platform"），允许第三方开发者嵌入该 harness。上下文压缩是长时运行智能体的常见技术，因为有研究表明，多步骤任务中大量智能体失败源于上下文漂移，而非 token 上限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/blog/codex-as-a-platform">Codex as a platform: build on the open agent harness | OpenAI Developers</a></li>
<li><a href="https://openai.com/index/unlocking-the-codex-harness/">Unlocking the Codex harness: how we built the App Server | OpenAI</a></li>
<li><a href="https://usewire.io/blog/why-ai-agents-forget-mid-task/">Why AI agents forget mid-task (and how to fix it) | Wire Blog</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI agents`, `#Agents API`, `#Codex`, `#AI infrastructure`

---

<a id="item-6"></a>
## [IFM 发布 K2 Horizon：6 个开源模型覆盖 0.9B 到 375B](https://aihot.news/items/cmtw8caao07cnrolksf2a0q7r) ⭐️ 8.0/10

Institute of Foundation Models（IFM）发布了 K2 Horizon，包含 6 个开源模型，参数规模从 0.9B 到 375B，覆盖端侧小模型到面向推理、编码和 Agent 的大模型。据报道，此次发布不仅开放了模型权重，还开源了完整的训练流水线，并采用 Apache 2.0 许可证，获得 vLLM、SGLang 和 Ollama 的首日支持。 以宽松许可证发布最高达 375B 参数的完整模型家族，为开源社区提供了真正前沿规模的可自托管选择，降低了对闭源 API 的依赖。这增强了面向推理、编码和 Agent 应用的开放权重生态，也巩固了 MBZUAI/IFM 在主权 AI 领域的地位。 该系列包括 Hugging Face 上的 IFM/K2-Horizon-MoVA-36B-A4B 等模型，暗示家族内部采用了混合变体/架构设计；所有模型均采用 Apache 2.0 许可证，并在 vLLM、SGLang 和 Ollama 推理框架上提供首日支持。

rss · AI Hot · Sep 11, 00:31

**背景**: Institute of Foundation Models（IFM）隶属于阿布扎比的 MBZUAI，其模型组合包括主权级 Agent 开放大语言模型家族 K2、面向阿拉伯语的 Jais 以及世界模型 PAN。开放权重模型发布已成为重要趋势，让组织可以自托管强大模型而无需依赖闭源服务；而同时开源训练流水线（而非仅权重）则更为罕见，对可复现性价值更高。K2 系列此前一直瞄准科学、数学和 Agent 类工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kryptonforge.in/blog/2026-09-08-k2-horizon-open-weight-model-fleet-self-hosting">K 2 Horizon Open -Sourced the Training Pipeline, Not Just the Weights.</a></li>
<li><a href="https://mbzuai.ac.ae/research/our-institutes-centers/institute-foundation-models">Institute of Foundation Models (IFM)</a></li>
<li><a href="https://huggingface.co/models">Models – Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区论坛（类似 LocalLLaMA）的讨论集中在探索新模型家族、基准测试表现和自托管能力上；有观点指出，开源训练流水线而非仅权重，使这次发布区别于众多常规的开放权重发布。

**标签**: `#open-source AI`, `#foundation models`, `#LLM release`, `#AI agents`, `#frontier AI`

---

<a id="item-7"></a>
## [消息称微软计划到 2032 年将数据中心容量提升至 38GW](https://www.ithome.com/1/001/109.htm) ⭐️ 8.0/10

彭博社报道称，微软计划到 2032 年将数据中心容量从当前的 12GW 提升至 38GW，达到现在的三倍以上，其中 12~13GW 将专用于 AI 芯片。该统计口径包括微软自有容量及从 Neocloud（新云）之外的合作伙伴处租用的容量。 算力短缺是微软当前面临的最大障碍，导致 Azure 无法承接客户需求，甚至被迫将部分订单转给竞争对手。这一计划表明微软押注 AI 工作负载将主导未来基础设施需求，直接影响超大规模云厂商之间的前沿 AI 算力竞赛。 微软当前 12GW 算力中仅 2GW 用于 AI 专用芯片，其余侧重通用计算，意味着未来将大幅向 AI 倾斜调整算力结构。38GW 将超过纽约州当前高峰时段用电量，且由于服务器集群建设需数年，客户偏好变化和新技术出现可能使该计划有所变动。

rss · IT HOME · Sep 11, 01:13

**背景**: 数据中心容量通常以吉瓦（GW）级别的功耗衡量，这是衡量一个设施能容纳多少服务器和 AI 加速器的代理指标。Neocloud（新云）指专注于 GPU 即服务的新兴云服务商，为 AI 训练和推理提供算力，与微软 Azure、AWS、谷歌云等传统超大规模厂商竞争。微软通过 Azure 支持 OpenAI 的算力需求，此前报道称即使 1900 亿美元的年度资本支出预算仍不足以缓解整体算力紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smartcity.qianjia.com/html/2025-07/10_418095.html">什么是Neocloud？ - 智慧城市- 千家网</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Microsoft`, `#datacenters`, `#compute capacity`, `#Azure`

---

<a id="item-8"></a>
## [DeepSeek 发布 V4.1 Flash：更强、更快、更普惠](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是其全新模型结构系列中最小尺寸的模型，采用 552B 参数的 Causal-Encoder-Decoder 架构，输入和输出激活参数分别为 8B 和 16B，并原生支持多模态视觉理解。该模型已以 deepseek-flash 之名上线 DeepSeek API，新价格于 2026 年 9 月 10 日 12:00 生效；9 月 14 日 12:00 后，deepseek-v4-pro 请求将路由至 V4.1 Flash 并按其价格计费。 DeepSeek 一直以前沿能力加上开放、低价的策略著称，这款稀疏激活、原生支持视觉的 552B 模型可能大幅降低开发者的多模态推理成本。deepseek-v4-pro 流量迁移至 Flash 也意味着现有 API 用户将经历一次重要的架构切换。 该模型采用 Causal-Encoder-Decoder 结构和稀疏激活（输入激活 8B、输出激活 16B），即每个 token 只使用 552B 总参数中的一小部分，从而降低推理成本。需要注意的是，这是新系列中最小的版本，而非旗舰模型。

telegram · @zaihuapd · Sep 10, 05:54

**背景**: DeepSeek 是一家以极具竞争力的价格发布高性能开源模型而闻名的中国 AI 实验室，其策略对全球大模型市场形成了压力。稀疏激活（类似混合专家 MoE）让大模型在每次推理时只激活一小部分参数，在保持能力的同时降低延迟和成本。原生多模态视觉理解意味着模型可以直接处理图像，无需额外的视觉模块。Causal-Encoder-Decoder 结构表明这是一种将编码器与因果（自回归）解码器相结合的混合设计，有别于多数大模型采用的纯解码器 Transformer 架构。

**标签**: `#DeepSeek`, `#AI models`, `#multimodal`, `#LLM release`, `#API`

---

<a id="item-9"></a>
## [中国 AI 芯片厂商涨价 20%-50%，HBM 短缺成为新瓶颈](https://www.reuters.com/world/asia-pacific/chinas-ai-chipmakers-raise-prices-high-bandwidth-memory-shortage-bites-2026-09-10/) ⭐️ 8.0/10

华为与寒武纪因全球高带宽存储器（HBM）供应紧张而涨价：华为昇腾 950DT 芯片报价较两个月前上涨约 20%-50%，部分老款芯片涨价约 30%，寒武纪新一代思元 690 预计上涨约 20%-30%。 HBM 供应由 SK 海力士、三星和美光主导，美国出口限制进一步收紧对中国市场的供应，使其成为制约国产 AI 算力扩张的关键瓶颈。芯片涨价可能拖慢中国 AI 基础设施建设，并推高国内云与 AI 企业的成本。 昇腾 950DT 于 2026 年 8 月问世，搭载华为自研 HiZQ 2.0 HBM，容量 144GB、带宽 4TB/s；寒武纪思元 690 于 2026 年初量产，采用中芯国际 N+2 制程，FP16 算力超过 700 TFLOPS。尽管国产 HBM 替代方案有所进展，但供应仍远跟不上激增的需求。

telegram · @zaihuapd · Sep 10, 09:29

**背景**: HBM（高带宽存储器）是一种基于 3D 堆叠技术的 DRAM，可为 AI 训练和推理提供关键的高访存带宽，尤其在大模型场景下，算力与内存之间的数据搬运往往是主要瓶颈。全球 HBM 市场几乎被 SK 海力士、三星和美光三家垄断，其产能大部分被英伟达等西方 AI 芯片厂商预订。美国出口限制限制先进 HBM 对华销售，迫使华为等国产厂商自研 HBM（如 HiZQ 2.0），而国产 AI 芯片需求却在激增。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.cn/tech/2026-06-08/detail-iniaqtnn6288947.d.html?fromtech=1&vt=4">让DeepSeek V4更强大 华 为 昇 腾 950 DT 芯 片 8月问世：自研HBM...</a></li>
<li><a href="https://mirrorfrog.com/docs/cards/cambricon/mlu-690/">寒武纪 思元690（国产 AI 训练/推理芯片） | AI 算力卡百科 | 222 款 ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2064582808346030775">寒武纪思元690深度拆解：国产AI芯片离H200还有多远？</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#HBM`, `#Huawei`, `#Cambricon`, `#export controls`

---

<a id="item-10"></a>
## [月之暗面（Kimi）秘密递交港股 IPO 申请，投前估值 500 亿美元](https://t.me/zaihuapd/43743) ⭐️ 8.0/10

月之暗面（Kimi 聊天机器人开发商）已以保密形式向港交所递交 A1 申请文件，正式启动 IPO 进程，据报道拟募资约 30 亿美元。同时公司正以 500 亿美元投前估值推进新一轮融资，这可能是上市前最后一轮。 月之暗面的估值在半年内从 2025 年底的约 43 亿美元飙升至 7 月投后 350 亿美元，涨幅约 8 倍，显示出资本市场对中国前沿 AI 公司的强烈信心。其上市将成为中国大模型行业的标志性事件，另有消息称 DeepSeek 可能于明年上半年上市。 今年 1 至 7 月，Kimi 以约三个月一次的节奏先后发布 K2.5、K2.6 和 K3；旗舰模型 Kimi K3 拥有 2.8 万亿参数，原生多模态，支持 100 万 token 上下文，采用 Kimi Delta Attention（KDA）和 Attention Residuals 架构。公司回应称暂无信息可披露，这符合保密 A1 递交的惯例。

telegram · @zaihuapd · Sep 10, 10:58

**背景**: 保密 A1 递交是向港交所正式提交的首份上市申请文件，公司可在财务细节公开披露前先行启动上市审核流程。"投前估值"指公司在获得新一轮投资前的评估价值，决定了新投资人能获得的股权比例。月之暗面是中国头部大模型创业公司之一，以 Kimi 聊天机器人和开源前沿模型著称，与 DeepSeek、智谱、MiniMax 等同场竞技。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/09/03/moonshot-ai-reportedly-submits-confidential-hong-kong-ipo-filing/?trk=article-ssr-frontend-pulse_little-text-block">Moonshot AI reportedly submits confidential Hong Kong IPO filing ...</a></li>
<li><a href="https://qz.com/moonshot-ai-hong-kong-ipo-filing-3-billion-090326">Moonshot AI confidentially files Hong Kong IPO targeting $3 billion</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI lab`, `#Moonshot AI`, `#Kimi`, `#IPO`, `#LLM`

---

<a id="item-11"></a>
## [腾讯混元开源音频编辑模型 AuK](https://x.com/TencentHunyuan/status/2097996926876795197) ⭐️ 8.0/10

腾讯混元与上海交通大学合作发布了开源基础模型 AuK，它通过自然语言指令和参考音频统一完成语音生成与编辑，支持零样本 TTS、音色/风格/情绪编辑、去口音以及多人语音分离。同时推出的蒸馏版本 AuK-Flash 仅需 4 步推理，在匹配条件下速度提升约 4.5 倍。 AuK 将多种语音任务整合到一个指令驱动的模型中，让开发者无需训练定制模型即可构建语音克隆、配音和音频后期制作工具。代码和权重的开源丰富了开源语音 AI 生态，为闭源商业系统提供了一个易用的替代方案。 AuK-Flash 通过少步蒸馏技术实现加速，即让一个学生模型通过模仿多步教师模型的流轨迹，仅需少量步骤即可合成音频。模型权重已通过 ModelScope 和 GitHub 开放，并提供可直接运行的推理命令，支持指定指令、目标时长和音频预处理输入。

telegram · @zaihuapd · Sep 10, 11:56

**背景**: 零样本 TTS 只需一段未见说话人的短音频提示即可合成自然语音，依靠说话人嵌入和文本编码，而无需数小时的训练数据。AuK 这类音频编辑模型进一步扩展了这一思路，允许用户通过自然语言指令修改现有录音的音色、风格、情绪或口音等属性。少步推理技术在基于扩散的音频生成领域（如 AudioLCM）已被广泛采用，通过将多步教师模型蒸馏为快速学生生成器来大幅降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/AuK">Tencent - Hunyuan / AuK : AuK : An Open-Source Foundational Model ...</a></li>
<li><a href="https://auk-project.github.io/">AuK — An Open-Source Foundational Model for Speech Generation...</a></li>
<li><a href="https://www.emergentmind.com/topics/zero-shot-tts">Zero - shot TTS : Methods and Evaluation</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#speech-synthesis`, `#Tencent-Hunyuan`, `#audio-model`

---

<a id="item-12"></a>
## [Anthropic 发布 2026 年 9 月威胁情报报告，披露被阻断的 Claude 滥用行动](https://www.anthropic.com/threat-intelligence-report-september-2026) ⭐️ 8.0/10

Anthropic 发布 2026 年 9 月威胁情报报告，披露了 2025 年 12 月至 2026 年 8 月间在七个危害类别（网络攻击、生物滥用、监控、舆论操纵和模型窃取等）中阻断的滥用行动。报告特别描述了一起针对约 50 个组织、使用 13 个常驻 AI 代理的中文网络间谍行动，并指多家中国 AI 实验室涉嫌通过代理、虚假账号和会话转发窃取模型能力或用户数据。 这是迄今为止关于国家级行为者武器化前沿 AI 模型的最详细公开报告之一，表明 AI 滥用已从理论风险变为被常态化检测和阻断的实际行动。对中国实验室进行模型蒸馏的指控也加剧了围绕前沿模型能力作为战略资产加以保护的地缘政治和商业争论。 除间谍活动外，报告还涵盖维稳监控、跨境招募、宗教情报收集、武器研发软件尝试（中国三起、俄罗斯两起、也门一起），以及五起可能支持生物武器开发的案例。Anthropic 表示已阻断相关行动并加强了防护，但其归因结论依赖于其内部调查。

telegram · @zaihuapd · Sep 11, 01:17

**背景**: 模型蒸馏攻击是指反复查询更强模型的 API，并利用其输出训练竞争模型——Anthropic 此前曾披露某些实验室生成了超过 1600 万条此类输出。本报告延续其 2025 年 11 月披露的 AI 编排间谍行动：攻击者不仅把 AI 当作顾问，而是直接让其执行网络攻击。随着常驻自主代理在网络空间激增，这一趋势日益明显。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/threat-intelligence-report-september-2026">Countering misuse of AI: September 2026 / Anthropic \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/disrupting-AI-espionage">Disrupting an AI-orchestrated cyber espionage campaign</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Anthropic`, `#threat intelligence`, `#AI misuse`, `#AI security`

---

<a id="item-13"></a>
## [Suno 发布 v6：首个与音乐行业合作打造的模型](https://www.producthunt.com/products/suno) ⭐️ 8.0/10

Suno 发布了 v6，这是其首个与音乐行业合作打造的音乐生成模型，此前 Suno 已与华纳音乐集团（WMG）和 BMG 等主要版权方签署了授权协议。此次 Product Hunt 上线标志着该模型开始基于获得授权的作品进行训练，而不再仅仅依赖存在争议的数据。 这标志着生成式 AI 音乐创业公司与唱片公司之间法律和商业冲突的一个转折点，可能使大规模的 AI 音乐生成走向合法化。如果成功，v6 可能重塑艺术家、词曲作者和唱片公司参与并从 AI 生成音乐中获利的方式。 根据与华纳音乐的和解协议，WMG 的艺人和词曲作者可以选择加入，允许其姓名、肖像、声音和作品被用于 Suno 上的 AI 生成音乐。不过该 Product Hunt 页面本身信息量很少，几乎没有提供关于模型架构或能力的技术细节。

producthunt · Zac Zuo · Sep 10, 05:13

**背景**: Suno 是一家位于马萨诸塞州剑桥市的生成式 AI 平台，可根据文本提示生成包含人声和配乐的完整歌曲，此前曾因训练数据问题被多家大型唱片公司起诉侵犯版权。2025 年 11 月，Suno 与华纳音乐集团达成和解并签署授权协议，随后又与 BMG 签约，为推出唱片公司支持的模型铺平了道路。其订阅计划提供商用授权、分轨分离和歌曲编辑器等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Suno_(platform)">Suno (platform) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suno">Suno - Wikipedia</a></li>
<li><a href="https://variety.com/2026/music/news/suno-ai-licensing-deal-bmg-1236832703/">AI Music Generator Suno Strikes Licensing Deal With BMG as It Preps New Label-Backed Models</a></li>

</ul>
</details>

**标签**: `#AI music generation`, `#generative AI`, `#Suno`, `#model release`, `#frontier AI`

---