---
layout: default
title: "Horizon Summary: 2026-04-04 (ZH)"
date: 2026-04-04
lang: zh
---

> From 90 items, 33 important content pieces were selected

---

1. [vLLM v0.19.0 新增 Gemma 4 和零气泡推测解码支持](#item-1) ⭐️ 9.0/10
2. [前沿 AI 模型彻底改变漏洞研究](#item-2) ⭐️ 9.0/10
3. [基于 Wan2.7 的 AI 视频生成在线平台上线](#item-3) ⭐️ 9.0/10
4. [OpenAI 上市前夕突发高层人事变动](#item-4) ⭐️ 9.0/10
5. [Meta 低调组建硬件团队，打造多形态 AI 智能体](#item-5) ⭐️ 9.0/10
6. [Arm 计划向中国市场销售 AGI 服务器 CPU](#item-6) ⭐️ 9.0/10
7. [Google Vids 接入 Veo 3.1，免费提供 AI 视频生成](#item-7) ⭐️ 9.0/10
8. [Anthropic 限制 Claude Code 订阅用户使用 OpenClaw 等第三方工具](#item-8) ⭐️ 8.0/10
9. [西蒙·威利森谈 AI 编程代理的认知影响](#item-9) ⭐️ 8.0/10
10. [AI 工具导致 Linux 内核安全漏洞报告激增](#item-10) ⭐️ 8.0/10
11. [AI 从“垃圾报告”转向高质量开源安全报告](#item-11) ⭐️ 8.0/10
12. [智己汽车官宣刘翔代言，LS8 智能 SUV 即将上市](#item-12) ⭐️ 8.0/10
13. [强一股份一季度净利预增 655%-762%](#item-13) ⭐️ 8.0/10
14. [OpenClaw 现可通过 Ollama 使用本地 Gemma4 模型](#item-14) ⭐️ 8.0/10
15. [AI 平台提供 MiniMax-2.5 模型接入并寻求微信支付方案](#item-15) ⭐️ 8.0/10
16. [日本研发抗辐射能力超航天设备千倍的 Wi-Fi 芯片](#item-16) ⭐️ 8.0/10
17. [上汽 2025 年将推出半固态电池量产车型](#item-17) ⭐️ 8.0/10
18. [奥尔特曼希望幼儿玩泥巴而非过早接触 AI](#item-18) ⭐️ 8.0/10
19. [苹果 2026 款 AirPods Pro 将搭载红外摄像头与 H3 芯片](#item-19) ⭐️ 8.0/10
20. [Cursor 发布 Cursor 3，打造面向 AI 代理的统一开发工作区](#item-20) ⭐️ 8.0/10
21. [OpenAI 推出团队版按量计费 Codex，降低 ChatGPT Business 年费](#item-21) ⭐️ 8.0/10
22. [美国人形机器人依赖中国核心零部件](#item-22) ⭐️ 8.0/10
23. [中国拟禁止向未成年人提供虚拟伴侣服务](#item-23) ⭐️ 8.0/10
24. [研究人员逆向 Claude Code 请求签名以解锁功能](#item-24) ⭐️ 8.0/10
25. [马斯克据称将 SpaceX 上市资格与 Grok 订阅挂钩](#item-25) ⭐️ 8.0/10
26. [Anthropic 将第三方工具费用从 Claude 订阅中剥离](#item-26) ⭐️ 8.0/10
27. [激光无线通信达 360 Gbps，能耗仅为 Wi-Fi 一半](#item-27) ⭐️ 8.0/10
28. [iNaturalist 及 AI 驱动的生物多样性应用引发关注](#item-28) ⭐️ 7.0/10
29. [千里科技发布 2025 年财报：营收 99.99 亿元，同比增长 42.13%](#item-29) ⭐️ 7.0/10
30. [ChatGPT.com 出现连接失败问题](#item-30) ⭐️ 7.0/10
31. [Synstax：基于 AI 的 iOS 补剂冲突检测与排程应用](#item-31) ⭐️ 7.0/10
32. [Win11 Canary 预览版支持触控笔一键唤起 Copilot](#item-32) ⭐️ 7.0/10
33. [Meta 首席技术官鼓励学生持续动手实践以进入科技行业](#item-33) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.19.0 新增 Gemma 4 和零气泡推测解码支持](https://github.com/vllm-project/vllm/releases/tag/v0.19.0) ⭐️ 9.0/10

vLLM v0.19.0 新增对 Google Gemma 4 架构的支持（包括混合专家、多模态和推理能力），引入零气泡推测解码与异步调度，完善了 Model Runner V2 功能，为视觉 Transformer（ViT）提供完整的 CUDA 图支持，并实现了通用的 CPU KV 缓存卸载机制。 此次发布大幅提升了前沿大语言模型的推理效率和模型通用性，使 Gemma 4 等先进模型能更快部署，并通过零气泡推测解码提高吞吐量，这对大规模实时 AI 应用至关重要。 Gemma 4 支持需要 HuggingFace Transformers ≥5.5.0；零气泡推测解码在生成过程中消除了流水线气泡；ViT 的 CUDA 图可降低 GPU 内核启动开销；CPU KV 缓存卸载机制可插拔，并支持块级抢占。

github · khluu · Apr 3, 02:19

**背景**: vLLM 是一个用于大语言模型推理和服务的高吞吐、内存高效开源库，广泛应用于生产级 AI 系统。推测解码通过使用小型“草稿”模型预测 token，再由大型“目标”模型验证，从而加速生成过程。CUDA 图通过将一系列 GPU 操作捕获为单个可执行图，减少 CPU 开销。Gemma 4 是 Google 最新推出的开源大语言模型系列，具备混合专家（MoE）、多模态输入和增强推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/docs/app/advanced/speculative-decoding">Speculative Decoding | LM Studio Docs</a></li>
<li><a href="https://developer.nvidia.com/blog/cuda-graphs/">Getting Started with CUDA Graphs | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/collections/matlok/papers-training-pipeline-zero-bubble-rate-1f1b">Papers - Training - Pipeline - Zero Bubble Rate - 1F1B - a matlok...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#vLLM`, `#inference optimization`, `#Gemma 4`

---

<a id="item-2"></a>
## [前沿 AI 模型彻底改变漏洞研究](https://simonwillison.net/2026/Apr/3/vulnerability-research-is-cooked/#atom-everything) ⭐️ 9.0/10

据 Thomas Ptacek 称，前沿 AI 模型和自主编码智能体将很快通过分析源代码实现零日漏洞的快速、自动化发现。这标志着漏洞利用开发能力的一次跃进式突破，而非渐进式改进。 这一转变可能使攻击性网络安全研究大众化并加速发展，大幅降低发现高影响力漏洞的技术门槛。同时，它也可能破坏当前的安全经济格局，使零日漏洞更容易被发现和武器化。 前沿大语言模型在此任务中表现出色，因其预训练中已包含海量代码库知识、对已知漏洞类别（如类型混淆、整数溢出）的内置理解，以及对可利用性进行隐式约束求解的能力。自主智能体可不知疲倦地持续测试假设，使漏洞利用开发变成一个可扩展的自动化流程。

rss · Simon Willison · Apr 3, 23:59

**背景**: 漏洞研究旨在发现软件中可能被攻击者利用的安全缺陷。“零日”漏洞利用针对的是厂商尚不知晓的漏洞，因此尤其危险。前沿 AI 模型指具备最先进推理与编码能力的大语言模型。自主编码智能体是能够独立规划、编写、测试和调试代码的 AI 系统，几乎无需人工干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Frontier_AI_models">Frontier AI models</a></li>
<li><a href="https://www.emergentmind.com/topics/autonomous-coding-agents">Autonomous Coding Agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_day_exploits">Zero day exploits</a></li>

</ul>
</details>

**标签**: `#AI`, `#frontier models`, `#vulnerability research`, `#coding agents`, `#cybersecurity`

---

<a id="item-3"></a>
## [基于 Wan2.7 的 AI 视频生成在线平台上线](https://www.v2ex.com/t/1203470#reply0) ⭐️ 9.0/10

一个基于 Wan2.7 AI 模型的在线平台已上线，用户可通过文本生成高质量视频，并精细控制风格、镜头语言和局部编辑。该平台支持迭代生成，专为短视频、广告、分镜草稿和创意验证优化。 该平台大幅降低了专业级 AI 视频创作的门槛，将原本局限于研究实验室的多模态生成能力交到创作者和营销人员手中。这标志着利用前沿 AI 技术实现影视内容创作民主化的重要一步。 该平台可生成最长 15 秒的 1080P 视频，支持首尾帧控制、九宫格图生视频以及角色与语音克隆。局部编辑（如调整节奏或镜头构图）和风格一致性仍在持续优化中。

rss · V2EX · Apr 4, 00:57

**背景**: Wan2.7 是阿里巴巴最新推出的开源多模态 AI 视频生成模型，被称作“多模态导演”，不再依赖简单的文本猜测，而是通过精准指令驱动视频合成。与早期模型不同，它能理解推拉摇移等镜头语言，并支持复杂的编辑流程。文本生成视频 AI（如 OpenAI 的 Sora）旨在将自然语言提示转化为连贯且视觉一致的视频片段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wan2-7ai.com/blog/what-is-wan-2-7-ai-video-generator">What is Wan 2.7? The Ultimate Multi-modal AI Video Generator | Blog</a></li>
<li><a href="https://www.dzine.ai/tools/wan-2-7/">Wan 2.7 - AI Video Generator with First & Last Frame Control | Dzine</a></li>
<li><a href="https://openai.com/index/sora/">Sora: Creating video from text | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#generative AI`, `#multimodal models`, `#text-to-video`, `#frontier tech`

---

<a id="item-4"></a>
## [OpenAI 上市前夕突发高层人事变动](https://www.ithome.com/0/935/929.htm) ⭐️ 9.0/10

OpenAI 将首席运营官布拉德·莱特卡普调任至特别项目，并宣布首席营销官凯特·罗奇和 AGI 负责人菲吉·西莫因健康原因暂时离岗。此次高管调整正值公司筹备潜在 IPO 并调整产品战略的关键时期。 此次人事变动发生在 OpenAI 商业化和 AGI 研发的关键阶段，可能影响其 IPO 进程、产品路线图（包括暂停 Sora 等决策）以及在与 Anthropic 和谷歌等对手竞争中的战略定位。 首席运营官莱特卡普现专注于通过私募股权合作推进企业软件销售，直接向 CEO 奥尔特曼汇报；首席营销官罗奇正在接受癌症治疗，未来可能以有限职责回归；AGI 及产品负责人西莫因神经免疫疾病休假数周，她近期主导了整合“超级应用”并叫停了 Sora 视频生成工具的开发。

rss · IT HOME · Apr 4, 00:07

**背景**: AGI（通用人工智能）指能在大多数经济活动中超越人类表现的高度自主系统。OpenAI 成立于 2015 年，是 GPT 系列模型和 ChatGPT 的开发者，处于全球 AI 前沿。Sora 是 OpenAI 开发的文本生成视频模型，旨在模拟现实世界的物理动态，目前尚未公开发布。该公司此前曾经历管理层动荡，尤其是 2023 年底 CEO 奥尔特曼曾被短暂罢免。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-bot.cn/sites/8613.html">Sora - OpenAI推出的AI文本到视频生成模型 | AI工具集</a></li>
<li><a href="https://ai-bot.cn/sora-com/">Sora官网 - OpenAI推出的AI视频生成工具：Sora.com | AI工具集</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AGI`, `#AI Leadership`, `#AI Industry News`, `#Generative AI`

---

<a id="item-5"></a>
## [Meta 低调组建硬件团队，打造多形态 AI 智能体](https://www.ithome.com/0/935/924.htm) ⭐️ 9.0/10

Meta 正在其超级智能实验室内部组建一个独立的硬件团队，开发承载持久性、多模态个人 AI 智能体的 AI 原生设备。该团队由前 AI 初创公司 Dreamer 高管 Rui Xu 领导，并已从 Reality Labs 调入部分工程师。 此举表明 Meta 正从智能手机转向构建 AI 原生硬件生态，让个性化智能体始终在线并感知用户环境。这使 Meta 与 OpenAI 等公司共同竞逐以具身化、主动式 AI 为核心的下一代计算范式。 目前硬件项目仍处于原型阶段，依托现有 Reality Labs 设备进行开发，两个团队高度协同。Meta 计划让智能体运行于多种设备形态中，能够持续“看见”和“听见”用户并与之互动。

rss · IT HOME · Apr 3, 23:25

**背景**: AI 原生设备旨在本地或与云端紧密协同运行 AI 模型，实现无需显式指令的情境感知和主动交互。持久性多模态 AI 智能体能跨语音、视觉和文本输入自主运行，并具备记忆与行为连续性。Meta 超级智能实验室成立于 2025 年 6 月，专注于开发“个人超级智能”——即在辅助个体方面超越人类能力的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@pcpatil410/how-ai-native-devices-are-redefining-human-computer-interaction-and-ushering-in-a-new-era-of-ea1a1000f623">How AI - Native Devices Are Redefining Human-Computer... | Medium</a></li>
<li><a href="https://www.akira.ai/blog/ai-agents-with-multimodal-models">Multimodal AI Agents: Reimaging Human-Computer Interaction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs">Meta Superintelligence Labs - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#AI Hardware`, `#Meta`, `#Superintelligence`, `#Frontier Tech`

---

<a id="item-6"></a>
## [Arm 计划向中国市场销售 AGI 服务器 CPU](https://www.tomshardware.com/pc-components/cpus/arm-to-sell-its-new-agi-cpu-in-china-we-would-expect-the-demand-for-this-product-to-be-just-as-strong-in-china-as-it-is-in-the-rest-of-the-world) ⭐️ 9.0/10

Arm 宣布将向中国客户直接销售基于 Neoverse V3 架构的新型 AGI 优化服务器 CPU。尽管美国出口管制限制向中国公司授权 Neoverse V3 的 IP，但 Arm 认为销售成品芯片符合现行法规。 此举可能在中国面临地缘政治限制的情况下，显著增强其获取前沿 AI 基础设施的能力，或加速当地 AGI 发展。同时也凸显了半导体公司如何通过从 IP 授权转向直接销售芯片来应对复杂的出口管制制度。 该 AGI CPU 每颗芯片集成 136 个 Neoverse V3 核心，专为数据中心高密度、低功耗部署而设计；Arm 参考设计在 1OU 双节点刀片中容纳 272 个核心。其出口合规性取决于 IP 授权与成品芯片销售之间的区别，后者受基于性能阈值（如绝对算力、互连带宽等）的不同规则约束。

telegram · zaihuapd · Apr 3, 02:30

**背景**: Arm 的 Neoverse 平台面向数据中心、高性能计算（HPC）和 AI 工作负载，V3 代相比 V2 在云和机器学习任务上提供两位数的性能提升。美国已逐步加强对先进 AI 芯片和半导体 IP 的出口管制，以限制中国获取前沿算力，尤其是与 AGI 相关的技术。然而，若不涉及技术转让，成品芯片可能适用限制较少的出口类别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/arm-to-sell-its-new-agi-cpu-in-china-we-would-expect-the-demand-for-this-product-to-be-just-as-strong-in-china-as-it-is-in-the-rest-of-the-world">Arm to sell its new AGI CPU in China — 'we would expect the demand for this product to be just as strong in China as it is in the rest of the world' | Tom's Hardware</a></li>
<li><a href="https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v3">Neoverse V3 | Enhanced Cloud & ML with Confidential ... - Arm</a></li>
<li><a href="https://newsroom.arm.com/blog/introducing-arm-agi-cpu">Announcing Arm AGI CPU: The silicon foundation for the agentic AI cloud era - Arm Newsroom</a></li>

</ul>
</details>

**标签**: `#AGI`, `#AI Hardware`, `#Semiconductors`, `#Export Controls`, `#Neoverse`

---

<a id="item-7"></a>
## [Google Vids 接入 Veo 3.1，免费提供 AI 视频生成](https://www.techradar.com/ai-platforms-assistants/google-is-pushing-ai-video-into-ordinary-life-just-as-openai-pulls-sora-back) ⭐️ 9.0/10

Google 更新了其基于浏览器的视频创作工具 Google Vids，集成 Veo 3.1 AI 视频生成模型和 Lyria 音乐模型。所有拥有 Google 账号的用户每月可免费生成 10 次视频，而订阅用户则获得更高的生成配额和高级音频功能。 此举大幅降低了普通用户使用高质量 AI 视频创作的门槛，在 OpenAI 对 Sora 采取更保守策略的背景下，凸显了 Google 在面向消费者的生成式 AI 领域的领先地位。这也体现了 Google 将多模态 AI 深度融入生产力工具的战略。 Veo 3.1 支持文本生成视频、图像生成视频以及同步音视频生成，最高可达 4K 分辨率，并支持横屏（16:9）和竖屏（9:16）比例。Lyria 3 和 Lyria 3 Pro 音乐生成功能仅限 Google AI Pro 和 Ultra 订阅用户使用，而可自定义外观、语音和道具的数字人功能现已向所有用户开放。

telegram · zaihuapd · Apr 3, 05:23

**背景**: Google Vids 是 Google 于 2024 年 4 月推出的 AI 视频编辑应用，作为 Google Workspace 的一部分，主要用于制作培训材料、项目更新等工作场景视频。Veo 是 Google DeepMind 开发的先进文本生成视频模型，于 2024 年 5 月首次发布，3.1 版本新增了高保真音频合成功能。Lyria 是 Google 的 AI 音乐生成模型系列，可根据文本提示生成专业级音乐片段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/veo/">Veo — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/lyria/">Lyria 3 — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Vids">Google Vids</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#Google Veo`, `#generative AI`, `#multimodal AI`, `#consumer AI tools`

---

<a id="item-8"></a>
## [Anthropic 限制 Claude Code 订阅用户使用 OpenClaw 等第三方工具](https://news.ycombinator.com/item?id=47633396) ⭐️ 8.0/10

从 4 月 4 日起，Anthropic 将不再允许 Claude Code 订阅用户通过 OpenClaw 等第三方工具使用其订阅额度；此类使用现在需要单独启用按量计费。用户若在 4 月 17 日前启用额外用量，将获得一笔等于其月订阅费用的一次性信用额度。 这一政策转变反映了 Anthropic 管理系统容量并针对高强度使用模式进行变现的努力，可能重塑开发者通过第三方工具集成和依赖前沿 AI 模型的方式。这也表明在竞争激烈的 AI 领域，公司正加强对 API 访问和使用经济的控制。 该限制最初针对 OpenClaw，但适用于所有第三方工具；Anthropic 为预购用量包提供最高 30%的折扣，并允许受影响用户申请退款。公司称这些工具对系统造成了“不成比例的负担”，因此做出调整。

hackernews · firloop · Apr 3, 22:55

**背景**: Claude Code 是 Anthropic 推出的专为编程任务优化的 Claude AI 模型版本。OpenClaw 等第三方工具作为“harness”（接口层），可自动化或扩展 Claude 的功能，超出官方网页或 API 的使用范围。Anthropic 提供分级订阅（如 Pro、Code），包含使用额度，但高度自动化的工具消耗的资源远超普通交互式使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aitoolly.com/ai-news/article/2026-04-04-anthropic-restricts-claude-subscription-limits-for-third-party-harnesses-starting-with-openclaw-inte">Anthropic Limits Claude Subscriptions for Third-Party Tools</a></li>
<li><a href="https://creati.ai/ai-news/2026-04-04/anthropic-bans-openclaw-from-claude-subscriptions/">Anthropic Bans Third-Party Harness OpenClaw from Claude ...</a></li>
<li><a href="https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access/">Anthropic clarifies ban on third-party tool access to Claude</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍理解 Anthropic 的立场，指出 OpenClaw 这类重度用户破坏了统一订阅制的补贴模式。一些用户因 Claude 频繁出错而计划转向其他模型，另有用户澄清 OpenClaw 与此前被禁工具的技术差异。甚至有贡献者已提交代码优化 OpenClaw 以减少对 Anthropic 系统的负载。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#API Policy`, `#Frontier Tech`

---

<a id="item-9"></a>
## [西蒙·威利森谈 AI 编程代理的认知影响](https://simonwillison.net/2026/Apr/3/cognitive-cost/#atom-everything) ⭐️ 8.0/10

西蒙·威利森分享了一段他与莱尼·拉奇茨基播客中关于依赖 AI 编程代理所带来认知成本的 48 秒短视频，在社交媒体上获得了超过 110 万次观看。 随着 AI 编程代理日益成为软件开发的核心工具，理解其对人类认知的影响对于保持开发者技能、自主性和长期解决问题的能力至关重要。这一讨论突显了人类认知与生成式 AI 交汇处的伦理和实践关切。 该片段摘自一场长达 1 小时 40 分钟的播客，主题涉及“代理工程”和“认知债务”；视频特别警示，将过多推理任务外包给 AI 可能会削弱开发者对代码的深层理解。

rss · Simon Willison · Apr 3, 23:57

**背景**: AI 编程代理（如 GitHub Copilot、Cursor 和 Devin）是在集成开发环境（IDE）中协助甚至自主执行编程任务的人工智能系统。“认知债务”指过度依赖自动化所带来的长期心智代价，类似于软件中的技术债务。包括麻省理工学院在内的一些近期研究表明，过度依赖 AI 进行写作和编程可能会改变与学习和问题解决相关的神经通路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/agents/coding">Coding Agents Comparison: Cursor, Claude Code, GitHub Copilot ...</a></li>
<li><a href="https://app.daily.dev/posts/the-cognitive-impact-of-relying-on-ai-for-writing-and-programming-zgu5qyx8g">The Cognitive Impact of Relying on AI for Writing and Programming</a></li>
<li><a href="https://codegen.com/blog/best-ai-coding-agents/">Best AI Coding Agents in 2026: Ranked and Compared</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#coding-agents`, `#AI`, `#software-development`, `#human-AI-collaboration`

---

<a id="item-10"></a>
## [AI 工具导致 Linux 内核安全漏洞报告激增](https://simonwillison.net/2026/Apr/3/willy-tarreau/#atom-everything) ⭐️ 8.0/10

Willy Tarreau 指出，Linux 内核安全漏洞报告数量急剧上升——从两年前每周 2 到 3 份增至如今每天 5 到 10 份——这完全归因于 AI 生成的代码分析。现在不同 AI 工具频繁提交重复报告，迫使内核团队招募更多维护者。 这一激增表明 AI 对关键开源基础设施产生了切实影响，既展现了其提升安全性的潜力，也暴露了意外后果，如维护者负担过重和重复报告造成的干扰。这标志着 AI 正深刻改变基础软件开发的工作流程。 大多数由 AI 报告的漏洞都是有效的，但报告数量庞大且频繁重复（有时同一漏洞被不同工具发现），给人工审核带来压力。周五和周二的报告量最高，可能反映出批量处理或工具调度的规律。

rss · Simon Willison · Apr 3, 21:48

**背景**: Linux 内核是大多数 Linux 操作系统的核心，由全球开发者社区共同维护。内核中的安全漏洞可能导致整个系统被攻破，因此及时发现和修复至关重要。近期，AI 驱动的静态分析和代码审查工具变得更易用、更强大，使得对 Linux 内核这类复杂代码库的自动化审查大幅增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linux.slashdot.org/story/26/03/28/0717258/linux-maintainer-greg-kroah-hartman-says-ai-tools-now-useful-finding-real-bugs">Linux Maintainer Greg Kroah-Hartman Says AI Tools Now... - Slashdot</a></li>
<li><a href="https://overcentral.com/en/linux-kernel-maintainer-confirms-ais-sudden-practical-value-for-developers/">Linux Kernel Maintainer Confirms AI 's Sudden Practical... - Overcentral</a></li>
<li><a href="https://simonwillison.net/tags/ai-security-research/">Simon Willison on ai - security -research</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Linux`, `#software engineering`, `#frontier tech`

---

<a id="item-11"></a>
## [AI 从“垃圾报告”转向高质量开源安全报告](https://simonwillison.net/2026/Apr/3/daniel-stenberg/#atom-everything) ⭐️ 8.0/10

cURL 项目负责人 Daniel Stenberg 表示，AI 生成的开源安全报告已从低质量的“垃圾信息”转变为大量准确且可操作的发现，如今每天耗费他数小时时间。Linux 内核维护者 Greg Kroah-Hartman 也提到，大约一个月前，AI 报告突然变得真正有用。 这标志着 AI 在网络安全领域的一个关键转折点：生成式 AI 和大语言模型（LLMs）现已足够成熟，能够大规模生成可靠的安全部署建议，直接影响 cURL 和 Linux 内核等关键基础设施维护者的时间与资源分配。这对开源生态既是机遇也是负担。 这一转变发生在最近一个月内，影响全球主要开源项目。早期的 AI 报告容易被当作噪音忽略，而当前的报告需要认真分类处理，表明大语言模型在代码分析中的准确性和上下文理解能力显著提升。

rss · Simon Willison · Apr 3, 21:46

**背景**: 大语言模型（LLMs）正越来越多地用于软件漏洞检测，利用其理解和推理代码的能力。传统安全工具常因高误报率和可扩展性问题受限，而 LLMs 通过更接近人类审阅者的方式解读代码语义，提供了新范式。cURL 和 Linux 内核等项目构成了互联网基础设施的骨干，其安全性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/10.1145/3769082">LLMs in Software Security: A Survey of Vulnerability ...</a></li>
<li><a href="https://arxiv.org/abs/2502.07049">LLMs in Software Security: A Survey of Vulnerability ... Vulnerability Detection in Large Language Models: Addressing ... Large language models for software vulnerability detection: a ... GRACE: Empowering LLM-based software vulnerability detection ... huhusmang/Awesome-LLMs-for-Vulnerability-Detection - GitHub LLM-based Vulnerability Detection - IEEE Xplore</a></li>
<li><a href="https://www.mdpi.com/2624-800X/5/3/71">Vulnerability Detection in Large Language Models: Addressing ...</a></li>

</ul>
</details>

**标签**: `#ai`, `#security`, `#generative-ai`, `#llms`, `#ai-security-research`

---

<a id="item-12"></a>
## [智己汽车官宣刘翔代言，LS8 智能 SUV 即将上市](https://36kr.com/newsflashes/3751088175907585?f=rss) ⭐️ 8.0/10

4 月 3 日，智己汽车宣布奥运冠军刘翔成为品牌代言人。同时，其搭载 AI 技术的 LS8 SUV 自 3 月 26 日开启预售以来，45 分钟内小订突破 10000 台，并将于 4 月 16 日正式上市。 此举表明智己汽车正通过顶级体育明星代言与前沿 AI 汽车技术相结合，提升高端智能电动车的大众吸引力。LS8 所搭载的先进硬件组合有望树立下一代高阶智能驾驶的新标杆。 LS8 搭载英伟达 Thor 芯片、速腾聚创 520 线超视域激光雷达（最远探测距离达 300 米）、全线控四轮转向、百万级底盘，以及基于通义千问大模型的 AI 超级智能体 IM Ultra Agent 1.0，提供“专属司机助理”功能。

rss · 36kr · Apr 3, 12:44

**背景**: 英伟达 Thor 是面向自动驾驶和机器人领域的下一代系统级芯片（SoC），性能远超前代 Orin 平台。520 线高分辨率激光雷达可实现精准的三维环境感知，为 L3 及以上高阶智驾提供关键支持。车载 AI 智能体旨在超越传统语音助手，具备主动执行复杂任务的“全域代劳”能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ee.ofweek.com/2025-01/ART-11000-2800-30654929.html">技术分析｜ 英 伟 达 的 Thor 芯 片 有多先进？ - OFweek电子工程网</a></li>
<li><a href="https://chejiahao.autohome.com.cn/info/25105045">智己LS8 25.98万，520线激光雷达智驾更安心_车家号_发现车生活_汽车之...</a></li>
<li><a href="https://www.ithome.com/0/930/392.htm">首搭“专属司机助理”IM ULTRA AGENT 1.0，智己 LS8 预售定档 3 月 26 ...</a></li>

</ul>
</details>

**标签**: `#AI智能体`, `#智能汽车`, `#英伟达Thor芯片`, `#激光雷达`, `#新能源汽车`

---

<a id="item-13"></a>
## [强一股份一季度净利预增 655%-762%](https://36kr.com/newsflashes/3751084860949252?f=rss) ⭐️ 8.0/10

强一股份预计 2026 年第一季度净利润为 1.06 亿至 1.21 亿元，同比增长 654.79%至 761.60%。这一显著增长主要得益于 AI 算力需求爆发、成熟产品订单放量、前期已发货未确认收入的订单在本期确认，以及客户结构优化和规模效应显现。 此次利润激增反映了 AI 基础设施投资的加速势头，凸显了半导体和硬件企业正直接受益于 AI 热潮。这表明处于 AI 算力供应链中的企业已获得强劲的市场验证。 公司特别指出，除新增 AI 驱动的需求外，前期发货订单的收入确认及运营规模效应也是关键因素。该预测区间表明公司正从此前较低的盈利水平跃升至显著盈利，暗示其增长具有结构性而非一次性特征。

rss · 36kr · Apr 3, 12:40

**背景**: AI 算力指训练和运行人工智能模型（尤其是大模型）所需的计算资源。随着生成式 AI 和基础模型的快速普及，对这类算力的需求激增，推动了半导体和数据中心硬件生态系统的增长。提供芯片、服务器、互连和散热解决方案的企业正迎来订单和定价能力的提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1004926375_120109837">AI算力需求提前引爆，科创板半导体企业迎业绩拐点</a></li>
<li><a href="https://news.qq.com/rain/a/20250331A079YP00">AI 算力革命为半导体产业带来的新机遇_腾讯新闻</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2574352">AI浪潮下的“芯”思考：半导体产业的变革、挑战与未来机遇</a></li>

</ul>
</details>

**标签**: `#AI算力`, `#semiconductors`, `#AI infrastructure`, `#financial performance`, `#tech hardware`

---

<a id="item-14"></a>
## [OpenClaw 现可通过 Ollama 使用本地 Gemma4 模型](https://www.v2ex.com/t/1203472#reply5) ⭐️ 8.0/10

用户现在可以通过 Ollama 配置 OpenClaw 使用本地托管的 Gemma4 模型，只需指定一个兼容 OpenAI 的 API 端点。该设置通过命令行参数指定本地服务器地址、模型 ID 和认证信息。 这使开发者能够在完全离线环境下运行前沿 AI 应用，确保数据隐私和控制权，并利用 Google 新近开源的 Gemma4 模型。它展示了前沿开源大语言模型在实际工具中的集成应用。 配置使用 Ollama 在 http://127.0.0.1:11434/v1 提供的 OpenAI 兼容 API，模型 ID 为 'gemma4:31b-it-q4_K_M'，API 密钥设为占位符 'ollama'。'--accept-risk' 参数表明运行此类模型可能存在计算或安全方面的考量。

rss · V2EX · Apr 4, 01:05

**背景**: Gemma4 是 Google 最新推出的开源大语言模型，采用 Apache 2.0 许可证，支持多模态输入、140 多种语言以及最高达 256K 的上下文窗口。Ollama 是一个流行的本地大模型运行工具，提供兼容 OpenAI 的 API，便于集成到现有应用中。OpenClaw 似乎是一个用于与大模型 API 对接以执行自动化或智能体任务的应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zdnet.com/article/google-gemma-4-fully-open-source-powerful-local-ai/">Google's Gemma 4 model goes fully open-source and ... - ZDNET</a></li>
<li><a href="https://ai.google.dev/gemma/docs">Gemma models overview - Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemma4`, `#Ollama`, `#Local LLM`, `#OpenClaw`

---

<a id="item-15"></a>
## [AI 平台提供 MiniMax-2.5 模型接入并寻求微信支付方案](https://www.v2ex.com/t/1203471#reply1) ⭐️ 8.0/10

一家 AI 服务平台正在推广 MiniMax-2.5（2300 亿参数）模型的接入，定价为 1 元人民币兑换 50 万 token，并寻求通过第三方支付平台集成微信支付的建议。 这反映了中国大模型商业化趋势的加速，也凸显了独立 AI 创业公司在基础设施（如支付集成）方面面临的挑战。以实惠价格提供 MiniMax-2.5 等前沿模型，有助于开发者和中小企业更广泛地使用先进 AI 能力。 该服务声称提供完整的 2300 亿参数 MiniMax-2.5 模型推理（非蒸馏或量化版本），并强调其自建算力基础设施。其定价相比主流云服务商具有显著的成本优势。

rss · V2EX · Apr 4, 01:03

**背景**: MiniMax-2.5 是由中国 AI 公司 MiniMax 开发的 2300 亿参数稀疏专家混合（MoE）大语言模型，在代码生成、智能体任务和办公场景中表现优异。该模型于 2026 年初发布，在 SWE-Bench Verified（80.2%）和 BrowseComp（76.3%）等基准测试中成绩领先。在中国，个人开发者常通过“易支付”类第三方平台接入微信支付，无需营业执照，但此类服务通常处于监管灰色地带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/news/minimax-m25">MiniMax M2.5: Built for Real-World Productivity.</a></li>
<li><a href="https://build.nvidia.com/minimaxai/minimax-m2.5/modelcard">minimax-m2.5 Model by Minimaxai | NVIDIA NIM</a></li>
<li><a href="https://e-pay.com.cn/">易支付 - 易支付通道-易支付接口-个人网站支付申请-个人微信支付宝易...</a></li>

</ul>
</details>

**标签**: `#AI models`, `#LLM`, `#AI infrastructure`, `#minimax`, `#token pricing`

---

<a id="item-16"></a>
## [日本研发抗辐射能力超航天设备千倍的 Wi-Fi 芯片](https://www.ithome.com/0/935/940.htm) ⭐️ 8.0/10

东京科学研究所的研究人员展示了一款可承受 50 万戈瑞（500 kGy）电离辐射的抗辐射 Wi-Fi 接收器，其耐辐射能力是航天级电子设备的 1000 倍。该芯片可为在核反应堆内作业的机器人（如福岛核电站清理任务）提供无线通信支持。 这项突破消除了高辐射环境中机器人对物理线缆的依赖，大幅提升了核事故响应和反应堆退役作业中机器人的机动性、安全性和操作效率。它为在极端危险区域部署真正自主的机器人系统铺平了道路。 该芯片采用抗辐射加固设计：增大 MOSFET 晶体管栅极尺寸、减少使用对辐射敏感的 PMOS 晶体管，并用无氧化层电感器替代部分元件，以减轻伽马射线在氧化层中引起的电荷俘获问题。经 500 kGy 辐射后，其信号增益仅下降约 1.5 分贝。目前团队正开发耐辐射发射器，早期版本在 300 kGy 下损坏，正在探索使用金刚石等半导体材料提升性能。

rss · IT HOME · Apr 4, 01:46

**背景**: 抗辐射电子器件专为在强电离辐射环境（如太空、核反应堆和粒子加速器）中工作而设计。普通硅基半导体在伽马射线照射下，绝缘层中会积累电荷，导致性能下降甚至失效。传统屏蔽方法（如铅）虽能阻挡辐射，但也会阻断无线信号，因此必须通过芯片级加固来实现此类环境中的无线通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techxplore.com/news/2026-03-radiationhardened-wifi-chip-survives-kgy.html">Radiation‑hardened Wi‑Fi chip survives 500 kGy for nuclear ...</a></li>
<li><a href="https://www.tomshardware.com/networking/routers/researchers-build-wi-fi-chip-that-can-operate-inside-a-nuclear-reactor-receiver-uses-special-materials-and-design-to-withstand-high-doses-of-radiation-for-at-least-six-months">Researchers build Wi-Fi chip that can operate inside a ...</a></li>
<li><a href="https://www.eurekalert.org/news-releases/1120923">Radiation-resistant Wi-Fi chip could enable wireless robots ...</a></li>

</ul>
</details>

**标签**: `#radiation-hardened electronics`, `#nuclear robotics`, `#frontier tech`, `#wireless communication`, `#disaster response technology`

---

<a id="item-17"></a>
## [上汽 2025 年将推出半固态电池量产车型](https://www.ithome.com/0/935/932.htm) ⭐️ 8.0/10

上汽集团宣布将从 2025 年起在旗下各品牌逐步推出搭载半固态电池的量产车型，其中名爵全新 MG4 半固态安芯版已交付，MG 4X 也已完成申报。公司还确认将于 2027 年实现全固态电池“光启电池”的量产交付。 此举加速了下一代电池技术的商业化进程，提供更高的能量密度和更强的安全性，对推动电动汽车普及和在全球市场保持竞争力至关重要。这也使上汽在中国固态电池产业化竞赛中处于领先地位。 即将推出的全固态“光启电池”目标能量密度超过 400Wh/kg，体积能量密度超 820Wh/L，容量超 75Ah。该电池在针刺和 200℃热箱测试中不起火不爆炸，低温容量保持率超 90%。

rss · IT HOME · Apr 4, 00:39

**背景**: 半固态电池采用固液混合电解质（通常含 5%–10%液体），相比传统锂离子电池可燃性更低，是迈向全固态电池的过渡技术。全固态电池则完全使用固态电解质，理论上具备更高安全性和能量密度，但面临制造工艺和成本挑战。这两类技术被视为下一代电动汽车和储能系统的关键发展方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/半固態電池">半固态电池 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/半固态电池/12578834">半固态电池_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/697439174">半固态电池全固态电池傻傻分不清？6个拷问讲透，彻底告别焦虑？</a></li>

</ul>
</details>

**标签**: `#solid-state battery`, `#electric vehicles`, `#frontier tech`, `#energy storage`, `#automotive innovation`

---

<a id="item-18"></a>
## [奥尔特曼希望幼儿玩泥巴而非过早接触 AI](https://www.ithome.com/0/935/927.htm) ⭐️ 8.0/10

OpenAI 首席执行官萨姆·奥尔特曼在播客中透露，尽管自己依赖 ChatGPT 获取育儿建议，但他推迟让孩子接触 AI 和屏幕设备，更希望孩子进行玩泥巴等现实世界的游戏。他还描绘了由 AI 驱动的个性化教育愿景，包括一对一辅导和项目式学习。 作为 AI 领域的关键人物，奥尔特曼的谨慎态度凸显了人们对屏幕成瘾、算法对儿童发展的影响以及面向青少年的 AI 伦理设计日益增长的担忧。他的观点反映了在塑造儿童未来时，技术乐观主义与负责任治理之间的深层张力。 奥尔特曼表示会“在合理范围内尽可能晚”让孩子接触 AI，并对幼儿无法放下 iPad 的现象感到忧虑。他本人曾用 ChatGPT 判断婴儿发育是否正常，同时设想未来学校采用 AI 进行高强度个性化辅导，但也承认这类系统可能出问题。

rss · IT HOME · Apr 3, 23:49

**背景**: “无限滚动”和算法推荐是社交媒体和应用程序中常见的设计模式，容易导致强迫性使用，尤其对发育中的大脑影响显著。研究表明（如 Meta 内部研究），长期接触此类内容会对青少年心理健康产生负面影响。与此同时，AI 驱动的个性化辅导利用自适应学习算法，根据学生个体需求定制教学内容，这一模式在教育科技领域正日益普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ukiyo-journal.com/cn/article/impact-of-endless-scroll-on-youth">年轻人被无限滚动的黑暗侵蚀：为什么无法停止使用TikTok？“被动滚动”...</a></li>
<li><a href="https://www.news.cn/world/20260331/34a0ee5acf864f809f66ca4f8dc8993d/c.html">让青少年社交媒体成瘾的硅谷“大厂”，该付出代价了-新华网</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#AI in education`, `#Sam Altman`, `#responsible AI`, `#frontier tech`

---

<a id="item-19"></a>
## [苹果 2026 款 AirPods Pro 将搭载红外摄像头与 H3 芯片](https://www.ithome.com/0/935/925.htm) ⭐️ 8.0/10

苹果正在开发 2026 款 AirPods Pro（可能命名为 AirPods Pro 3+），将配备用于环境感知的红外摄像头、取代压感柄的手势控制功能，以及全新的 H3 音频芯片。这些功能旨在与 Apple Intelligence 和 iOS 27 增强版 Siri 深度集成。 此举将 AirPods Pro 定位为 Apple Intelligence 生态的关键可穿戴入口，使 AI 能力从屏幕延伸至现实环境感知。这标志着苹果正战略性地转向日常设备中的无感、免手持 AI 交互模式。 红外摄像头不用于拍摄照片或视频，而是为 Siri 提供视觉智能；手势控制可能需要用户重新适应此前由压感柄完成的操作；H3 芯片旨在降低延迟、提升音质，并为端侧 AI 处理提供算力支持。

rss · IT HOME · Apr 3, 23:38

**背景**: Apple Intelligence 是苹果于 2024 年 6 月发布的生成式人工智能系统，已集成至 iOS 18、iPadOS 18 和 macOS Sequoia，结合端侧与云端处理，提供注重隐私的情境感知 AI 功能。苹果长期推行自研芯片垂直整合战略，从 A 系列、M 系列到 H 系列芯片，均旨在为 AI 负载优化软硬件协同。目前 AirPods Pro（第二代）采用 H2 芯片，而即将推出的 H3 芯片将是其在可穿戴设备上的下一代演进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2025/10/12/next-generation-airpods-5-and-h3-chip-in-the-pipeline-report/">Apple has already begun work on an H3 chip and next ... - 9to5Mac</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence - Wikipedia</a></li>
<li><a href="https://www.apfelpatient.de/en/generally/new-airpods-pro-with-camera-and-h3-chip-coming-this-fall">New AirPods Pro with camera and H3 chip from Fall Apfelpatient</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Apple Intelligence`, `#wearable AI`, `#gesture control`, `#Siri`

---

<a id="item-20"></a>
## [Cursor 发布 Cursor 3，打造面向 AI 代理的统一开发工作区](https://cursor.com/blog/cursor-3) ⭐️ 8.0/10

Cursor 发布了 Cursor 3，这是一个专为 AI 代理设计的统一开发工作区重大更新。新版本采用围绕代理工作流重构的界面，支持多仓库，并可通过移动端、网页、桌面端以及 Slack、GitHub 和 Linear 等入口访问。 此次发布体现了软件开发正加速向 AI 代理驱动模式转变，使开发者能更无缝地与自主或半自主编码助手协作。通过在多个平台和仓库间统一上下文，Cursor 3 显著降低了基于 AI 代理的工作流摩擦。 Cursor 3 支持在本地与云端之间切换代理会话：本地用于实时编辑和测试，云端可在后台或离线时继续运行。新版本还引入了 diff 视图以加速代码变更审查，并集成暂存、提交和 PR 管理功能。

telegram · zaihuapd · Apr 3, 02:00

**背景**: Cursor 是一款基于 VS Code 构建的 AI 编码编辑器，旨在将大语言模型深度集成到开发流程中。此处的“AI 代理”指能根据高层指令自主或半自主执行编写、调试、重构等编码任务的系统。“统一工作区”概念旨在将文件、对话和工具等所有开发上下文整合到一个连贯环境中，供开发者与 AI 代理共同使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zed.dev/languages/diff">Diff Editor — Zed</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#AI agents`, `#developer tools`, `#software engineering`, `#AI IDE`

---

<a id="item-21"></a>
## [OpenAI 推出团队版按量计费 Codex，降低 ChatGPT Business 年费](https://openai.com/index/codex-flexible-pricing-for-teams/) ⭐️ 8.0/10

OpenAI 现在为 ChatGPT Business 和 Enterprise 工作区提供仅含 Codex 的席位，采用按量计费模式，无固定席位费，仅按 token 消耗收费。同时将 ChatGPT Business 的年费从每席位 25 美元降至 20 美元。 此举降低了企业和开发团队试用及采用 AI 编程工具的门槛，可能加速企业对 AI 的整合。价格调整表明 OpenAI 正聚焦于推动更广泛的开发者参与和商业化扩展。 Codex-only 席位无速率限制，仅按 token 使用量计费；符合条件的团队每新增一名 Codex 用户可获 100 美元额度（每团队最高 500 美元）。OpenAI 表示已有超 900 万付费企业用户和超 200 万每周使用 Codex 的开发者，Business 和 Enterprise 中的 Codex 用户数自 1 月以来增长了 6 倍。

telegram · zaihuapd · Apr 3, 03:06

**背景**: Codex 是 OpenAI 开发的专注于根据自然语言提示生成代码的 AI 模型，也是 GitHub Copilot 的核心技术。ChatGPT Business（前身为 Team）和 Enterprise 是面向组织的付费版本，提供增强的协作功能、管理控制和数据隐私保护。Enterprise 版本还额外支持单点登录（SSO）、数据驻留和 SOC 2 合规等 Business 不具备的功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2014744418435998214">ChatGPT 订阅怎么选：Free、Go、Plus、Pro、Business、Enterprise 的...</a></li>
<li><a href="https://www.hungyichen.com/en/insights/chatgpt-enterprise-guide">ChatGPT Enterprise vs Business 2026: Features, Pricing & Plan ...</a></li>
<li><a href="https://chatgpt.com/zh-Hant/pricing">ChatGPT 方案 | 免費版、Plus、Pro、Business 和 Enterprise</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#ChatGPT Business`, `#AI Pricing`, `#Enterprise AI`

---

<a id="item-22"></a>
## [美国人形机器人依赖中国核心零部件](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf) ⭐️ 8.0/10

《华尔街日报》报道指出，美国人形机器人（包括特斯拉 Optimus 和迪士尼奥拉夫）日益依赖中国制造的电机、关节、磁体和传感器。中国计划在 2025 年推出 28 款人形机器人，数量接近美国企业的三倍，其供应链最多可将制造成本降低三分之二。 这种依赖引发了美国对其在关键前沿技术领域技术主权和供应链安全的战略担忧。随着人形机器人成为未来自动化和人工智能部署的核心，对中国零部件的依赖可能影响美国的国家竞争力和产业政策。 特斯拉正与中国供应商合作推进 Optimus 量产，目标在 2026 年中实现月产 1 万台。中国公司宇树科技已向客户供应用于机器人关节的自润滑轴承等关键部件，并计划 2025 年全球出货超 5500 台。

telegram · zaihuapd · Apr 3, 08:55

**背景**: 人形机器人需要先进的执行器、传感器和精密机械部件来模拟人类动作，其中电机、谐波减速器和力矩传感器等子系统技术门槛高、成本昂贵。中国已快速构建起机器人供应链，宇树科技等企业实现了较高的零部件集成度和成本优势。与此同时，特斯拉等美国公司将人形机器人视为其人工智能与自动化战略的重要延伸。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/Robot251/article/details/146038160">「宇树科技」13家核心零部件供应商梳理！_金力永磁 宇树科技-CSDN博客</a></li>
<li><a href="https://jishuzhan.net/article/1904078367320780801">「宇树科技」13家核心零部件供应商梳理！ - 技术栈</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1989474341176497767">特斯拉Optimus量产倒计时：A股核心供应商全梳理</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid robots`, `#supply chain`, `#Tesla Optimus`, `#frontier tech`

---

<a id="item-23"></a>
## [中国拟禁止向未成年人提供虚拟伴侣服务](https://mp.weixin.qq.com/s/EHpjg2sfth0W7OE-v6hq9g) ⭐️ 8.0/10

国家网信办于 2026 年 4 月 3 日发布《数字虚拟人信息服务管理办法（征求意见稿）》，拟禁止向未成年人提供虚拟伴侣、虚拟亲属等服务，并要求服务界面全程显著标注“数字人”字样。 此举标志着中国正将 AI 治理延伸至生成式人工智能驱动的虚拟人领域，重点防范针对未成年人的沉迷诱导、过度消费及隐私泄露风险，强化对前沿交互技术的伦理监管。 征求意见稿要求使用自然人敏感个人信息建模须获单独同意，处理未成年人信息需监护人同意，具有舆论属性或社会动员能力的服务提供者须履行算法备案和安全评估义务，违规最高可处 20 万元罚款。

telegram · zaihuapd · Apr 3, 09:39

**背景**: 数字虚拟人是由大语言模型和生成式 AI 驱动的虚拟化身，能模拟人类对话与行为。在中国，此类服务被纳入深度合成与算法推荐技术的监管范畴。自 2022 年《互联网信息服务深度合成管理规定》实施以来，相关服务需遵守标识、用户同意及算法备案等合规要求方可上线运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.tencent.com/developer/article/2648154">AI产品办理算法备案全流程实操指南（2026最新版）</a></li>
<li><a href="https://beian.cac.gov.cn/">互联网信息服务算法备案系统</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2019433727579702384">2026算法备案避坑指南 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#digital virtual humans`, `#generative AI`, `#AI ethics`, `#minor protection`

---

<a id="item-24"></a>
## [研究人员逆向 Claude Code 请求签名以解锁功能](https://a10k.co/b/reverse-engineering-claude-code-cch.html) ⭐️ 8.0/10

研究人员逆向分析了 Anthropic 的 Claude Code 所使用的专有请求签名机制，特别是 `cch` 头部和 `cc_version` 后缀，成功开发出一个不依赖官方 Bun 运行时的 Python 概念验证工具，并解锁了快速模式等功能。 此举揭示了主流 AI 系统如何通过客户端签名实现功能门控和使用归因，为 API 安全设计及潜在绕过方式提供了重要洞见。它还使开发者能更灵活地与 Claude 后端交互，引发对商业 AI 产品访问控制机制可靠性的讨论。 `cch` 签名由私有 Bun 运行时（而非标准 JavaScript）使用 xxHash64 对包含 `cch=00000` 占位符的完整 JSON 请求体计算得出；`cc_version` 后缀则通过用户首条消息中的特定字符、内置盐值和版本号经 SHA-256 计算生成。该机制似乎用于计费归因和功能开关，而非强加密安全控制。

telegram · zaihuapd · Apr 3, 15:00

**背景**: Claude Code 是 Anthropic 开发的 AI 编程助手，通过带签名的请求与 Anthropic API 通信。Bun 是一个注重性能的现代 JavaScript 运行时，常作为 Node.js 的替代方案。xxHash64 是一种非加密哈希算法，以极高速度和良好的分布特性著称，通常用于校验和与数据完整性检查，而非安全用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bun.com/docs/runtime/networking/fetch">Fetch - Bun</a></li>
<li><a href="https://github.com/Cyan4973/xxHash">xxHash - Extremely fast hash algorithm - GitHub xxHash - Extremely fast non-cryptographic hash algorithm XXHash Algorithm Implementation | ceph/xxHash | DeepWiki xxHash - Extremely fast hash algorithm - Google Open Source xxHash in C# | SSOJet XXHash - Richard Startin’s Blog XxHash64 Class (System.IO.Hashing) | Microsoft Learn XXHash Algorithm Implementation | ceph/xxHash | DeepWiki XXHash - Richard Startin’s Blog XXHash - Richard Startin’s Blog</a></li>
<li><a href="https://xxhash.com/?source=post_page---------------------------">xxHash - Extremely fast non-cryptographic hash algorithm</a></li>

</ul>
</details>

**标签**: `#AI`, `#reverse-engineering`, `#Anthropic`, `#Claude`, `#API-security`

---

<a id="item-25"></a>
## [马斯克据称将 SpaceX 上市资格与 Grok 订阅挂钩](https://arstechnica.com/tech-policy/2026/04/elon-musk-insists-banks-working-on-spacex-ipo-must-buy-grok-subscriptions/) ⭐️ 8.0/10

据称，埃隆·马斯克要求参与 SpaceX 首次公开募股（IPO）的银行和顾问公司必须购买 xAI 开发的 Grok 人工智能服务订阅，部分机构已承诺投入数千万美元。SpaceX 本周提交了 IPO 文件，距离其收购 xAI 仅过去两个月。 此举表明马斯克试图通过 SpaceX 备受瞩目的 IPO 来推动 Grok 的商业化，可能加速企业对 xAI 技术的采用。同时也引发外界对其多项商业利益交织以及在金融交易中捆绑服务是否合乎伦理的质疑。 一些银行已开始将 Grok 集成到其 IT 系统中；尽管马斯克还要求它们在 X 平台投放广告，但这一要求的执行力度明显弱于 Grok 订阅要求。

telegram · zaihuapd · Apr 4, 00:07

**背景**: Grok 是由埃隆·马斯克于 2023 年创立的人工智能公司 xAI 开发的生成式 AI 聊天机器人。xAI 已于 2026 年初成为 SpaceX 的全资子公司。Grok 具备实时网络搜索、图像与视频生成、语音聊天和高级推理能力，被视为 OpenAI 的 ChatGPT 等模型的竞争对手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/04/elon-musk-insists-banks-working-on-spacex-ipo-must-buy-grok-subscriptions/">Elon Musk insists banks working on SpaceX IPO must buy Grok ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">xAI (company) - Wikipedia</a></li>
<li><a href="https://x.ai/grok/business">Grok for Business - xAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Grok`, `#xAI`, `#SpaceX`, `#Enterprise AI`

---

<a id="item-26"></a>
## [Anthropic 将第三方工具费用从 Claude 订阅中剥离](https://x.com/bcherny/status/2040206440556826908) ⭐️ 8.0/10

自 4 月 4 日太平洋时间中午 12 点起，Anthropic 将不再把 OpenClaw 等第三方工具包含在 Claude 订阅计划中。用户现在必须通过额外用量包或使用 Claude API 密钥按量付费才能继续使用这些工具。 这一变化影响了依赖基于 Claude 构建的自主代理（如 OpenClaw）的开发者和高级用户，可能增加其运营成本，并表明 Anthropic 正将战略重心转向核心 API 和官方产品使用，而非第三方集成。 Anthropic 高管 Boris Cherny 表示，当前订阅模式不适合第三方工具的使用模式，公司将优先保障直接使用 Claude 官方产品或 API 的用户。通过 API 使用仍然可行，但需明确管理 API 密钥并跟踪成本。

telegram · zaihuapd · Apr 4, 01:05

**背景**: OpenClaw 是一个开源的自主 AI 代理，利用 Claude 等大语言模型在 WhatsApp、Telegram 等消息平台上执行现实任务。Claude API 允许开发者将 Anthropic 的模型集成到自定义应用中，按令牌消耗计费。Anthropic 既提供直接 API 访问，也通过面向消费者的 Claude.ai 平台提供订阅服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://platform.claude.com/docs/en/api/overview">API Overview - Claude API Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#API`, `#AI Pricing`

---

<a id="item-27"></a>
## [激光无线通信达 360 Gbps，能耗仅为 Wi-Fi 一半](https://www.sciencedaily.com/releases/2026/04/260402042734.htm) ⭐️ 8.0/10

研究人员展示了一种芯片级光无线通信系统，在两米距离内实现了 362.7 Gbps 的传输速率，每比特能耗约为 1.4 皮焦耳，约为当前领先 Wi-Fi 技术的一半。 这一突破为未来人工智能计算、数据中心和高密度计算环境提供了超高速且节能的无线连接方案，而传统射频系统在这些场景中正面临带宽和功耗瓶颈。 该系统采用 5×5 VCSEL（垂直腔面发射激光器）阵列，测试中启用了 21 个激光器，每个激光器速率达 13 至 19 Gbps；相关成果已发表于《Advanced Photonics Nexus》。

telegram · zaihuapd · Apr 4, 01:47

**背景**: 光无线通信利用光（通常来自激光器或 LED）在自由空间中传输数据，而非使用无线电波。VCSEL 是一种半导体激光器，其发光方向垂直于芯片表面，适合紧凑型高密度集成。由于其高能效和高速调制能力，VCSEL 已广泛应用于面部识别、激光雷达（LiDAR）和短距离数据链路中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vertical-cavity_surface-emitting_laser">Vertical-cavity surface-emitting laser - Wikipedia</a></li>
<li><a href="https://optics.org/news/cambridge-develops-optical-method-for-faster-greener-indoor-wireless-comms">Cambridge develops optical method for faster, greener indoor ...</a></li>
<li><a href="https://www.sciencedaily.com/releases/2026/04/260402042734.htm">Laser-powered wireless hits 360 Gbps and uses half the energy ...</a></li>

</ul>
</details>

**标签**: `#optical wireless communication`, `#VCSEL`, `#frontier tech`, `#energy efficiency`, `#high-speed networking`

---

<a id="item-28"></a>
## [iNaturalist 及 AI 驱动的生物多样性应用引发关注](https://www.inaturalist.org/) ⭐️ 7.0/10

Hacker News 上的一场讨论聚焦于 iNaturalist、Merlin Bird ID 和 Flora Incognita 等利用 AI 进行物种识别的应用程序，既称赞其准确性和实用性，也提出用户隐私方面的担忧。据报道，Flora Incognita 的识别准确率高达 80% 至 98%，而 iNaturalist 最近获得了 Google.org 提供的 150 万美元资助，用于开发生成式 AI 物种识别工具。 这些应用程序展示了应用型 AI 和计算机视觉如何通过推动公众参与生物多样性监测，变革公民科学和生态研究。但它们也引发了关于数据隐私和无意中暴露个人位置信息的重要问题。 iNaturalist 的 API 允许无需身份验证的只读访问并支持 CORS，对开发者十分友好。Flora Incognita 虽然准确率高，但其 API 文档有限；而带地理标记的观测数据可能暴露用户家庭住址，带来隐私风险。

hackernews · bookofjoe · Apr 3, 17:22

**背景**: iNaturalist 是一个公民科学平台，用户上传动植物照片以帮助记录全球生物多样性。它利用计算机视觉模型提供物种识别建议，并由社区进行验证。类似的应用如康奈尔鸟类学实验室开发的 Merlin Bird ID 使用音频识别鸟鸣，而 Flora Incognita 则专注于欧洲植物，其深度学习模型基于数百万张图像训练而成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inaturalist.org/posts/113184-inaturalist-receives-grant-to-improve-species-suggestions">iNaturalist receives grant to improve species suggestions</a></li>
<li><a href="https://www.scientificamerican.com/article/google-ai-grant-to-inaturalist-prompts-community-outcry/">Google AI Grant to iNaturalist Prompts Community Outcry</a></li>
<li><a href="https://www.pathsoflearning.net/13598/7-best-nature-based-citizen-science-apps/">7 Best Nature-Based Citizen Science Apps That Spark Wonder ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞 iNaturalist 开放的 API 及其现实影响力，有人提到通过该平台发现了新物种。但也有人对隐私问题表示严重担忧，尤其是非技术用户在后院观察时可能无意中暴露家庭住址。尽管用户对 Merlin 和 Flora Incognita 等相关应用充满热情，但受限的 API 访问和技术小问题也带来一定困扰。

**标签**: `#AI`, `#computer vision`, `#biodiversity`, `#citizen science`, `#ecological tech`

---

<a id="item-29"></a>
## [千里科技发布 2025 年财报：营收 99.99 亿元，同比增长 42.13%](https://36kr.com/newsflashes/3751128551244552?f=rss) ⭐️ 7.0/10

千里科技发布 2025 年年度报告，全年实现营业收入 99.99 亿元，同比增长 42.13%，并强调“AI+车”商业化取得突破。其中汽车业务收入达 64.40 亿元，同比增长 52.71%；归母净利润约 0.84 亿元，同比增长 111%。 汽车业务的强劲增长，尤其是在“AI+车”领域的突破，表明千里科技在智能出行领域成功实现了 AI 技术的商业化落地，这在行业内具有示范意义。这也反映出市场对智能化车辆需求的上升，并验证了公司将 AI 深度融入汽车制造与销售的战略有效性。 整车销量同比增长 83.93%，成为主要增长动力；而科技业务板块收入仅为 3.50 亿元，表明当前 AI 能力主要通过硬件产品（如智能汽车）实现商业化，尚未形成独立的软件或服务收入模式。

rss · 36kr · Apr 3, 13:25

**背景**: “AI+车”指将人工智能技术融入汽车系统，包括高级驾驶辅助系统（ADAS）、自动驾驶、车载信息娱乐以及制造流程优化等。边缘 AI（即在车辆端本地处理数据）正变得至关重要，可在保障低延迟和隐私的前提下实现实时决策。全球车企正加速与 AI 企业合作，以应对激烈竞争并降低生产成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builtin.com/artificial-intelligence/artificial-intelligence-automotive-industry">AI in Cars: 25 Examples of Automotive AI - Built In</a></li>
<li><a href="https://www.mckinsey.com/industries/semiconductors/our-insights/the-rise-of-edge-ai-in-automotive">The rise of edge AI in automotive | McKinsey</a></li>
<li><a href="https://www.businessinsider.com/car-companies-ai-production-rising-costs-new-york-auto-show-2026-4">Automakers are teaming up, speeding up, and hoping AI can ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Automotive`, `#Financial Results`, `#Commercialization`, `#Smart Mobility`

---

<a id="item-30"></a>
## [ChatGPT.com 出现连接失败问题](https://www.v2ex.com/t/1203469#reply3) ⭐️ 7.0/10

有用户报告称 chatgpt.com 无法访问，显示“ERR_TUNNEL_CONNECTION_FAILED”错误，而其他聊天机器人服务仍可正常访问。 作为 OpenAI 的旗舰 AI 平台，ChatGPT 被数百万用户和开发者广泛使用；任何中断或访问问题都可能影响工作流程，并引发对服务可靠性的担忧。 “ERR_TUNNEL_CONNECTION_FAILED”错误通常表明本地网络问题，例如代理或 DNS 设置错误，而非服务器端宕机。但若大量用户同时报告，则可能暗示更广泛的问题。

rss · V2EX · Apr 4, 00:52

**背景**: 2024 年 5 月，OpenAI 将 ChatGPT 从 chat.openai.com 迁移至专用域名 chatgpt.com，标志着将 ChatGPT 打造为独立产品的战略转变。该新域名现已成为免费和付费用户的主要访问入口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aimode.co/news/chatgpt-moves-to-new-domain/">ChatGPT Moves to New Domain: ChatGPT.com - AI Mode</a></li>
<li><a href="https://kinsta.com/blog/err_tunnel_connection_failed/">How To Fix ERR_TUNNEL_CONNECTION_FAILED in Chrome - Kinsta</a></li>

</ul>
</details>

**标签**: `#AI`, `#ChatGPT`, `#OpenAI`, `#service outage`, `#frontier tech`

---

<a id="item-31"></a>
## [Synstax：基于 AI 的 iOS 补剂冲突检测与排程应用](https://www.v2ex.com/t/1203466#reply1) ⭐️ 7.0/10

一位独立开发者发布了名为 Synstax 的 iOS 应用，该应用利用 AI 检测补剂与食物之间的相互作用，依据 RDI/UL 标准验证剂量安全性，并基于超过 5000 条科学规则自动生成摄入时间表。该应用还支持通过 OCR 扫描补剂瓶身标签，所有核心功能均可离线使用且无需注册账号。 该应用解决了人们常忽视的健康风险——不安全或无效的补剂组合，通过自动化和 AI 将复杂的营养科学变得易于理解和使用。它让用户无需专业知识即可安全优化自己的补剂方案。 Synstax 内置 5142 条补剂交互规则、337 条饮食-补剂冲突提醒（如咖啡、葡萄柚等），并配备基于膳食参考摄入量（DRI）的剂量安全引擎，包含可耐受最高摄入量（UL）。所有数据均本地存储，支持 8 种语言，免费版提供全部核心功能，仅无限次 AI 分析需升级 Pro 版。

rss · V2EX · Apr 4, 00:32

**背景**: 膳食参考摄入量（DRI）是由美国国家医学院制定的一套营养指南，包括推荐膳食摄入量（RDA）、适宜摄入量（AI）、可耐受最高摄入量（UL）和平均需要量（EAR），用于指导健康人群的安全有效营养素摄入。补剂之间的相互作用（如钙会抑制铁的吸收）在科学文献中有明确记载，但很少被整合成面向普通消费者的应用工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.80aj.com/2026/04/04/smart-supplement-app-synstax/">独立开发者推出智能补剂管理App Synstax：AI分析冲突，数据仅存本地</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/参考膳食摄入量">参考膳食摄入量 - 维基百科，自由的百科全书</a></li>
<li><a href="https://health.baidu.com/m/detail/ar_6284086288960376445">营养素的每日推荐摄入量 (dri) | 百度健康·医学科普</a></li>

</ul>
</details>

**标签**: `#AI`, `#health tech`, `#mobile app`, `#supplement management`, `#independent development`

---

<a id="item-32"></a>
## [Win11 Canary 预览版支持触控笔一键唤起 Copilot](https://www.ithome.com/0/935/935.htm) ⭐️ 7.0/10

微软发布了 Windows 11 Canary 频道的 Build 29560.1000 和 Build 28020.1803 预览版，新增触控笔尾键可一键启动 Copilot 的功能。此次更新还修复了 USB 设备异常、屏保设置可靠性问题，并改进了语音听写和系统文件检查器。 此举标志着微软正将 Copilot 更深入地融入 Windows 系统，为使用触控笔的专业用户（如设计师、笔记用户）提供更流畅的 AI 辅助体验。通过硬件按钮直接调用 AI 助手，提升了人机交互的便捷性与效率。 触控笔尾键现可设置为与 Copilot 键（Win+C）功能一致，该功能目前仅限 Canary 频道预览版。此外，开发者模式对话框已采用 Windows 11 统一设计语言进行视觉更新，界面更协调。

rss · IT HOME · Apr 4, 00:53

**背景**: 微软于 2025 年底在 Copilot+ PC 上首次引入专用 Copilot 按键，用户可一键调用 AI 助手。Windows 预览体验计划的 Canary 频道用于测试尚不稳定的早期功能，未来可能面向大众推送。触控笔常用于运行 Windows 的二合一设备，广泛应用于绘图、记笔记和批注等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.windows.com/windows-insider/2026/04/03/announcing-windows-11-insider-preview-build-for-canary-channel-29560-1000/">Announcing Windows 11 Insider Preview Build for Canary ...</a></li>
<li><a href="https://www.ithome.com/0/922/409.htm">微软拆分 Win11 Canary 频道，推行功能版 / 平台重构版双轨制</a></li>
<li><a href="https://iknow.lenovo.com.cn/detail/419323">Copilot Key指导说明 - 联想知识库</a></li>

</ul>
</details>

**标签**: `#AI integration`, `#Windows 11`, `#Copilot`, `#Human-computer interaction`, `#Operating systems`

---

<a id="item-33"></a>
## [Meta 首席技术官鼓励学生持续动手实践以进入科技行业](https://www.ithome.com/0/935/931.htm) ⭐️ 7.0/10

Meta 首席技术官安德鲁·博斯沃思在 Instagram 问答中建议学生持续构建和实验，推荐软件方向使用 AI 辅助编程，硬件方向使用树莓派和 Arduino。此番言论正值硅谷企业激烈争夺 AI 人才之际。 随着 AI 重塑软件开发与硬件原型设计，博斯沃思的建议反映了行业重点，并为学生进入竞争激烈的就业市场提供了可行路径。Meta 对早期动手实践的重视，表明行业正从单纯依赖学历转向更注重实际技能。 博斯沃思特别提到“氛围编程”——通过自然语言利用 AI 生成和优化代码——并建议从树莓派和 Arduino 入手，再进阶到印刷电路板。他还透露 Meta 如今甚至直接招募优秀的高中毕业生。

rss · IT HOME · Apr 4, 00:23

**背景**: AI 辅助软件开发利用大语言模型来自动化编码、调试和文档编写等环节。树莓派和 Arduino 是广泛用于教育和原型开发的平台：树莓派是一种低成本的单板计算机，而 Arduino 是一个开源的微控制器平台，适合交互式电子项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/ai_assisted_software_development">AI-assisted software development</a></li>
<li><a href="https://en.wikipedia.org/wiki/Raspberry_Pi">Raspberry Pi</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arduino">Arduino</a></li>

</ul>
</details>

**标签**: `#AI in software development`, `#tech careers`, `#Meta`, `#AI tools`, `#hardware prototyping`

---