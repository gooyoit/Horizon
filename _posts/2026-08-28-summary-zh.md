---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> From 114 items, 20 important content pieces were selected

---

1. [腾讯混元发布 Hy4 预览版：770B 参数 MoE 模型开源，支持 1M 上下文](#item-1) ⭐️ 9.0/10
2. [腾讯混元发布 Hy4 preview：770B 参数、1M 上下文并开源](#item-2) ⭐️ 9.0/10
3. [Anthropic 发布模型硬件标准（MHS）研究预览，让 AI 操控实验设备](#item-3) ⭐️ 9.0/10
4. [Anthropic 开放模型硬件标准（MHS）研究预览，AI 智能体可安全操控物理设备](#item-4) ⭐️ 9.0/10
5. [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](#item-5) ⭐️ 9.0/10
6. [Google 发布语音转文本模型 Gemini-3.5-Transcribe](#item-6) ⭐️ 8.0/10
7. [谷歌发布 Gemini Omni 1.1 Flash，支持 40 秒场景扩展与 4K 视频输出](#item-7) ⭐️ 8.0/10
8. [研究者以 80%成功率攻破 Claude Code Opus 5 自动模式](#item-8) ⭐️ 8.0/10
9. [谷歌内部测试 Gemini 3.8 Flash 预览版，Pro 与 Flash 系列表现分化](#item-9) ⭐️ 8.0/10
10. [消息称 Anthropic 曾有意约 70 亿美元收购芯片初创公司 MatX，现转向合作谈判](#item-10) ⭐️ 8.0/10
11. [腾讯发布开源 MoE 旗舰模型 Hy4 Preview](#item-11) ⭐️ 8.0/10
12. [Qwen3.8-Flash 上线 OpenCode Go 编程工具](#item-12) ⭐️ 8.0/10
13. [Qwen3.8-Flash 上线 GMI Cloud，作为 Qwen4 架构早期预览](#item-13) ⭐️ 8.0/10
14. [腾讯开源混元 Hy4 preview：770B 参数 MoE 模型，支持 1M 上下文](#item-14) ⭐️ 8.0/10
15. [Google 发布 Gemini 3.5 Transcribe：85+ 语言平均 WER 2.6% 的语音转文本模型](#item-15) ⭐️ 8.0/10
16. [Anthropic 发布模型硬件标准（MHS），进军物理 AI 领域](#item-16) ⭐️ 8.0/10
17. [谷歌员工内部测试 Gemini 3.8 Flash 预览版](#item-17) ⭐️ 8.0/10
18. [消息称 Anthropic 曾考虑以约 70 亿美元收购 AI 芯片初创公司 MatX](#item-18) ⭐️ 8.0/10
19. [英伟达 Q4 营收 681 亿美元超预期，下季度指引上调至 780 亿美元](#item-19) ⭐️ 8.0/10
20. [OpenAI 被曝开发常驻 Codex 代理，持续工作直至休眠](#item-20) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [腾讯混元发布 Hy4 预览版：770B 参数 MoE 模型开源，支持 1M 上下文](https://aihot.virxact.com/items/cmtcklzws01lcrojzxuushys5) ⭐️ 9.0/10

腾讯混元发布了 Hy4 预览版，这是一个开源前沿模型，采用混合专家（MoE）架构，总参数量 770B，激活参数 49B，支持 100 万 token 的上下文窗口。模型权重已在 HuggingFace 和 GitHub 上开放，腾讯明确邀请用户使用并反馈问题。 这是目前规模最大的全开源前沿模型之一，让开发者和研究者可以免费使用接近闭源系统的能力。1M 上下文与 MoE 高效推理的结合，使其适合长文档处理、编程等生产力场景，也将加剧与 DeepSeek、MiniMax 等开源模型的竞争。 该模型每个 token 仅激活 770B 总参数中的 49B，大幅降低了相对于模型规模的推理成本。作为预览版，腾讯强调价格稳定实惠并邀请社区反馈问题，说明后续还会迭代；另外需注意，标称 1M 上下文并不总是意味着整个窗口都能被有效利用。

rss · AI Hot · Aug 28, 06:23

**背景**: 混合专家（MoE）是一种架构，由路由器为每个 token 只选择一小部分“专家”网络参与计算，因此模型总参数可以非常大，而推理时只激活其中一小部分——例如 DeepSeek 的模型同样是在更大的总参数中只激活 13B–49B。1M 级别的长上下文窗口可以在单次提示中处理整个代码库或书籍长度的文档，但实际效果可能受“lost in the middle”等问题影响。腾讯混元此前已有开源大型 MoE 模型的经验，如 Hunyuan-Large 曾在 MMLU、BBH 等基准上超过 Llama3.1 和 Mixtral。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xiaohu.ai/p/15254">腾 讯 发布目前最 大 开源MoE 模 型 ： 腾 讯 混 元 大 模 型 （ Hunyuan -Large...</a></li>
<li><a href="https://javabetter.cn/ai/video/what-is-moe.html">MoE 是 什 么 ？ DeepSeek 模 型 为 什 么 采用 混 合 专 家 架构？ | 二哥的Java...</a></li>
<li><a href="https://realtime-ai.chat/posts/long-context-reality/">百万级 上 下 文 真的能用吗 | Chico's Tech Blog</a></li>

</ul>
</details>

**标签**: `#open-source-models`, `#large-language-models`, `#Tencent-Hunyuan`, `#MoE`, `#long-context`

---

<a id="item-2"></a>
## [腾讯混元发布 Hy4 preview：770B 参数、1M 上下文并开源](https://aihot.virxact.com/items/cmtcjzlxy03f8rodbxqdotbhg) ⭐️ 9.0/10

腾讯混元发布了新一代旗舰模型 Hy4 preview，总参数 770B、激活参数 49B，支持 1M token 上下文长度。该模型现已开源，并上线腾讯云 TokenHub 和 OpenRouter。 这是一次重要的开源前沿级模型发布，规模远超前代 Hy3（295B 总参数、21B 激活），有助于腾讯冲击中国模型第一梯队。开源 770B 参数、1M 上下文的 MoE 模型，为开发者和企业提供了可替代闭源模型的强大长上下文选择。 该模型采用混合专家（MoE）架构，每次推理仅激活 770B 参数中的 49B，在保持大容量的同时控制了计算成本。作为 preview 版本，后续预计还会推出更大的多模态版本，与此前关于 Hy4 将支持多模态的报道一致。

rss · AI Hot · Aug 28, 06:03

**背景**: 混合专家（MoE）是一种稀疏激活架构，通过解耦参数规模与计算成本，让模型在推理时只激活一小部分“专家”参数，从而以较低成本实现超大容量，DeepSeek-V3 等模型均采用该架构。混元是腾讯的旗舰大模型系列，前代 Hy3 总参数为 295B、激活 21B。腾讯云 TokenHub 是一站式大模型服务平台，聚合混元及 DeepSeek、Kimi、智谱 GLM 等第三方模型；OpenRouter 则是流行的统一 API 网关，可通过一个接口调用多种模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.tencent.com/document/product/1823/130050">大模型服务平台 TokenHub 产品简介_腾讯云</a></li>
<li><a href="https://x.com/AiBattle_/status/2076706838821703925">AiBattle on X: "Tencent’s HY4 is currently in training and will be larger than HY3 (295B total parameters, 21B active) HY4 will also be multimodal. Hunyuan aims to enter the top tier of Chinese models by 2027 ByteDance’s Seed team is training an unprecedentedly large model Source: LatePost" / X</a></li>
<li><a href="https://juejin.cn/post/7629603625098674222">混合专家模型 MoE ...</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#open-source`, `#Tencent-Hunyuan`, `#MoE`, `#long-context`

---

<a id="item-3"></a>
## [Anthropic 发布模型硬件标准（MHS）研究预览，让 AI 操控实验设备](https://aihot.virxact.com/items/cmtcidc5d03olroucud51b3mj) ⭐️ 9.0/10

Anthropic 与 HHMI Janelia 研究园区合作，推出了模型硬件标准（MHS）的研究预览，这是一套标准化驱动规范，让 AI 智能体能够安全地发现并操作显微镜、液体处理器、机械臂等物理设备。首批科研实验室和先进制造商已可使用，集成时间从数周或数月缩短至数小时或数分钟。 MHS 是 AI 智能体进入物理世界的重要一步，解决了目前每台实验仪器和机器人都需要定制化、耗时集成的问题。如果被广泛采用，它将大幅加速自动化科研和先进制造，并把 Anthropic 制定标准的影响力从软件（MCP）扩展到硬件领域。 MHS 与模型无关，支持 MCP 等标准协议，任何兼容的智能体都可以通过标准化命令和接口操作设备。在开源之前，Anthropic 计划与合作伙伴共同制定安全评估和最佳实践。

rss · AI Hot · Aug 28, 05:10

**背景**: MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 AI 应用连接到外部数据源和工具，目前已在行业内广泛采用。MHS 将这种标准化思路从数字工具扩展到物理硬件，提供统一的驱动层，使智能体无需定制集成即可控制各类设备。HHMI Janelia 研究园区位于美国弗吉尼亚州，是知名的生物医学研究基地，以先进成像和仪器著称，因此成为试点 AI 驱动实验室自动化的天然合作伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/">Anthropic 's new hardware standard lets AI agents... - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI agents`, `#robotics`, `#MCP`, `#frontier AI`

---

<a id="item-4"></a>
## [Anthropic 开放模型硬件标准（MHS）研究预览，AI 智能体可安全操控物理设备](https://www.anthropic.com/news/model-hardware-standard-research-preview) ⭐️ 9.0/10

Anthropic 开放了模型硬件标准（MHS）研究预览的第一阶段，这是一套共享规范，让 AI 智能体能够安全操控显微镜、液体处理器、机械臂等物理设备，应用于科研和先进制造领域。设备集成时间从数周甚至数月缩短到几小时甚至几分钟，Anthropic 计划在完成安全评估后开源该标准。 这标志着前沿 AI 实验室向物理世界迈出的重要一步，提供统一接口后，AI 驱动的实验室和工厂自动化的部署成本和时间将大幅降低。首批合作方横跨生物技术、机器人和量子计算领域，包括基因泰克、卡内基梅隆大学和 QuEra，显示出业界对 AI 与硬件标准化控制的广泛需求。 QuEra 基于 MHS 构建的 AI 控制器可在 99.3% 的情况下无需人工干预自主恢复中性原子量子计算机的激光锁定，将原本需要工程师到场的修复工作缩短到几秒内完成。该预览目前仅面向首批科研实验室和先进制造商开放，开源需待安全评估完成。

telegram · @zaihuapd · Aug 28, 01:38

**背景**: 传统上，将 AI 智能体连接到实验室和工业设备需要为每台设备进行定制化集成，往往需要数周到数月的工程工作。像 QuEra 这样的中性原子量子计算机依赖精确锁定的激光来操控量子比特，而温度、振动和压力会不断使激光偏离目标，需要持续的人工调谐和维护。MHS 这样的共享标准旨在让 AI 智能体以统一、安全的方式发现、通信并操控各类物理硬件，类似于标准 API 统一软件集成的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/08/27/anthropic-pushes-into-physical-world-with-new-standard-to-help-ai-agents-operate-machines.html">Anthropic pushes into physical world with new standard to help AI agents operate machines</a></li>
<li><a href="https://quantumzeitgeist.substack.com/p/queras-ai-now-tunes-quantum-lasers">QuEra’s AI now tunes quantum lasers in seconds, not minutes</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI agents`, `#robotics`, `#quantum computing`, `#frontier AI`

---

<a id="item-5"></a>
## [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 9.0/10

2026 年 8 月 28 日，腾讯发布迄今最强开源模型 Hy4 preview，总参数量 770B、活跃参数 49B、上下文窗口 1M token。在 203 个工程任务的盲评中，Hy4 preview 以 2.99 分小胜 GLM-5.3（2.92）与 Kimi K3（2.94）。 此次发布使开源大模型第一梯队的竞争更加激烈，腾讯、智谱、月之暗面、DeepSeek 等中国厂商的得分已近乎持平。开发者针对长周期软件工程、文档办公与科研任务又多了一个强大的开源选择，可通过腾讯云、Hugging Face、ModelScope、GitHub、AtomGit 和 OpenRouter 等渠道获取。 Hy4 preview 采用混合专家（MoE）架构，每个 token 仅激活 770B 总参数中的 49B，推理成本相对较低。API 定价为每 1M tokens 输入 0.834 美元、输出 2.501 美元，腾讯称其稳居开源模型第一梯队。

telegram · @zaihuapd · Aug 28, 06:11

**背景**: 腾讯在 2026 年 8 月 12 日的第二季度业绩材料中已确认 Hy4 即将发布，参数规模超过 HY-3，并从纯文本扩展到多模态，同时继续推进强化学习方向。MoE（混合专家）架构将每个输入路由到少量专家网络，使大模型只需激活很少的参数即可运行，大幅降低计算成本。GLM-5.3（智谱）和 Kimi K3（月之暗面）是目前领先的开源模型，而在真实工程任务上做人工盲测已成为静态基准之外流行的对比方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L5E54N0H0511B8LM.html">稳居开源模型第一梯队，腾讯发布混元Hy4 preview模型|hy|知名企业|一代版本模型|tencent_网易订阅</a></li>
<li><a href="https://www.datalearner.com/ai-models/pretrained-models/tencent-hy4">Tencent Hy4（腾讯混元4）：研发状态、已确认信息与发布时间 | DataLearnerAI</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-K3">GitHub - MoonshotAI/ Kimi - K 3 : Open Frontier Intelligence · GitHub</a></li>

</ul>
</details>

**标签**: `#open-source-models`, `#LLM-release`, `#Tencent-Hunyuan`, `#MoE`, `#benchmark`

---

<a id="item-6"></a>
## [Google 发布语音转文本模型 Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

Google 发布了 Gemini 系列中的专用语音转文本模型 Gemini-3.5-Transcribe。Hacker News 上的早期用户已将其与 Mistral 的 Voxtral、ElevenLabs 和 Soniox 等替代方案进行基准测试，实际使用结果褒贬不一。 语音转文本是实时翻译、会议转录和语音助手的核心能力，Google 的加入加剧了这一竞争激烈领域的角逐。社区测试表明基准测试分数并不总能转化为实际优势，这对选择 STT 服务商的开发者很重要。 该模型支持函数调用，可将复杂任务（如图像生成和文件分析）委托给其他 Gemini 模型，目前可在 Gemini macOS 应用中使用——这一点让部分用户困惑 STT 模型本身是否会执行任意任务。用户报告其准确率领先，但延迟仍需改进，而且它可能会“简化”精确措辞，丢掉用户特意说出的内容。

hackernews · k9294 · Aug 27, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=49468818)

**背景**: 语音转文本（STT）模型将音频转换为文本，评估维度包括准确率、多语言支持、噪声鲁棒性和延迟。竞争对手包括 Mistral 的开源权重 Voxtral 系列（Voxtral Mini 3B 在本地部署中很受欢迎）、ElevenLabs 的付费 API 以及 Soniox 的低延迟 STT v5。实际应用中的挑战包括语言混用、行业专有词汇，以及保留精确措辞而非改写。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/voxtral/">Voxtral | Mistral AI</a></li>
<li><a href="https://elevenlabs.io/docs/api-reference/speech-to-text/convert">Create transcript | ElevenLabs Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区评价褒贬不一。一位用公司多语言会议测试了约 20 个 STT 模型的用户表示，本地部署中只有 Voxtral Mini 3b 令人满意，付费 API 中 ElevenLabs 略好。一位实时翻译开发者称赞 Gemini-3.5-Transcribe 的准确率，但认为 Soniox STT v5 在延迟上更胜一筹；还有 Pixel 11 Pro 用户抱怨该模型会“简化”精确表达，破坏原意。

**标签**: `#AI`, `#speech-to-text`, `#Gemini`, `#Google`, `#model-release`

---

<a id="item-7"></a>
## [谷歌发布 Gemini Omni 1.1 Flash，支持 40 秒场景扩展与 4K 视频输出](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) ⭐️ 8.0/10

谷歌发布了 Gemini Omni 1.1 Flash，为视频生成模型带来重大升级：场景扩展可参考此前 10 秒画面并按 10 秒递增延长至累计 40 秒，同时支持指定首尾关键帧、360p 草稿生成以及最高 1080p 或 4K 高清输出。开发者可通过 Gemini API 和 Google AI Studio 使用。 在 OpenAI 等竞争对手已放弃 Sora 视频产品之际，此次升级巩固了谷歌在前沿视频生成领域的地位，表明谷歌将视频生成视为构建世界模型的关键。更长的场景扩展和关键帧控制让 AI 视频在真实创作与制作流程中更加实用。 场景扩展通过参考此前 10 秒画面实现，并按 10 秒递增，最长可累计至 40 秒。首尾关键帧控制让开发者精确定义视频片段的起始与结束状态，模型还支持 360p 草稿模式，便于在输出 1080p 或 4K 成品前低成本迭代。

hackernews · @zaihuapd · Aug 27, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49467922)

**背景**: Gemini Omni Flash 是 Gemini API 中谷歌默认的视频生成模型，与面向不同工作流的 Veo 并列。首尾关键帧控制（指定起始帧和结束帧，由模型补全中间运动）已成为 MiniMax H3、Wan 等竞品的标配能力，可让创作者精确控制画面过渡。场景扩展则允许用户将较短的 AI 生成片段串联成可用的场景长度，弥补多数视频模型只能生成数秒短片的局限。这些能力之所以重要，是因为视频生成正日益被视为通向理解物理动态的世界模型的垫脚石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemini-api/docs/video">Video generation in the Gemini API | Google AI for Developers</a></li>
<li><a href="https://lovegen.ai/minimax-h3">MiniMax H3 (Hailuo 03) AI Video Generator : 2K Text, Image...</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到 OpenAI 已放弃 Sora 而谷歌持续重金投入的对比，simonw 猜测谷歌将视频生成视为构建世界模型的关键。一位用户抱怨该模型仍无法将生成的视频与已有音频同步，转而在本地 12GB 显存的 RTX 4070 上使用 MiniMax H3 完成对口型；还有人调侃谷歌页面对 Firefox 的兼容性，并吐槽谷歌迟迟不发布新版 Gemini Pro。

**标签**: `#AI`, `#video-generation`, `#Google`, `#Gemini`, `#generative-models`

---

<a id="item-8"></a>
## [研究者以 80%成功率攻破 Claude Code Opus 5 自动模式](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

提示注入研究者 Johann Rehberger 演示了一种攻击，能以约 80%的成功率绕过 Claude Code Opus 5 的自动模式。该攻击诱使代理下载并解压包含恶意 struct.py 的压缩包，当代码执行 import base64 时该文件会被悄悄导入并执行。 Anthropic 最近将自动模式设为 Claude Code 的默认设置，并宣称其高效性（独立测试中拦截了 89%的危险命令）。这项研究表明该安全层可被绕过，更糟的是，它有时还会在代理察觉入侵后阻止 Claude 自己的清理命令，安全机制本身成了故障的一部分。 该攻击利用了 Python 的导入解析机制：从恶意 zip 解压出的本地 struct.py 会遮蔽标准库，导入 base64（其内部会导入 struct）时就会执行攻击者代码。在某些运行中，自动模式的分类器允许了恶意进程的创建，却拒绝了用于终止它的命令。

rss · Simon Willison · Aug 27, 22:50

**背景**: 提示注入是指藏在 AI 代理读取的内容（文件、网页、工具输出）中的恶意指令覆盖其原始指令的攻击方式。Claude Code 的自动模式于 2026 年 8 月成为默认设置，它使用服务端提示注入探针扫描工具输出，并用命令分类器判断哪些操作可无需用户批准直接执行。Anthropic 曾报告自动模式在 Trajectory Labs 的独立评估中拦截了全部 72 个间接提示注入场景。Rehberger 的工作表明，结合社会工程与 Python 模块遮蔽的现实攻击链仍能绕过这些防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/claude-code-auto-mode">How we built Claude Code auto mode: a safer way to skip permissions \ Anthropic</a></li>
<li><a href="https://gbhackers.com/claude-code-auto-mode-blocks-attacks/">Claude Code Auto Mode Blocks 89% of Dangerous Commands and Prompt Injection Attacks</a></li>
<li><a href="https://code.claude.com/docs/en/security">Security - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 认同 Rehberger 的结论：面对对抗性风险时，沙箱是运行代理唯一安全的方式——在容器或虚拟机中运行、限制网络出口、监控代理，并且绝不向代理运行时暴露主目录、SSH 密钥或云凭证。

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#Anthropic`, `#agent safety`

---

<a id="item-9"></a>
## [谷歌内部测试 Gemini 3.8 Flash 预览版，Pro 与 Flash 系列表现分化](https://aihot.virxact.com/items/cmtcmo13p01nsro64dryxxdd8) ⭐️ 8.0/10

据 Business Insider 获取的泄露信息，谷歌员工已开始在内部编程平台 Jetski 上试用 "Gemini 3.8 Flash Preview" 模型。一名参与测试的员工称其体验明显好于 3.7 Flash，但目前下完整结论还为时过早。 这一泄露表明谷歌正以极快的节奏迭代其前沿模型，据报道 CEO 皮查伊希望将发布节奏提高到接近每月一次。这加剧了与 OpenAI 和 Anthropic 的前沿模型竞赛，也表明更便宜、更快速的 Flash 系列正成为面向开发者的 AI 编程工具的主要竞争焦点。 这是一份基于内部截图泄露的传闻级报道，并非官方发布，且未披露任何基准测试数据或上线时间。标题中的"冰火两重天"指 Flash 系列快速迭代而 Pro 系列更新较慢，3.7 Flash 等版本在速度和成本上已可与部分 Pro 模型竞争。

rss · AI Hot · Aug 28, 07:06

**背景**: 谷歌的 Gemini 模型家族分为多个层级：Pro 系列追求最强能力，而 Flash 系列以牺牲部分质量换取更快的响应速度和更低的成本，因此在高频编程和智能体工作负载中很受欢迎。Jetski 是谷歌内部的 AI 编程平台，员工会在模型公开发布前进行内部试用。数周内从 3.7 升级到 3.8 的快速小版本迭代，反映了行业从罕见大版本发布转向持续更新的新常态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8">Google Employees Are Already Testing the Next... - Business Insider</a></li>
<li><a href="https://emergent.sh/learn/gemini-3-7-flash-vs-gemini-3-1-pro">Gemini 3.7 Flash vs Gemini 3.1 Pro Preview: Full Comparison</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#LLM`, `#AI models`, `#frontier AI`

---

<a id="item-10"></a>
## [消息称 Anthropic 曾有意约 70 亿美元收购芯片初创公司 MatX，现转向合作谈判](https://aihot.virxact.com/items/cmtcmo13q01nvro64o874fih2) ⭐️ 8.0/10

据路透社报道，Anthropic 曾考虑以约 70 亿美元收购 AI 芯片初创公司 MatX，但谈判现已转向合作模式。与此同时，MatX 正以约 40 亿美元的估值筹集新资金，而 Anthropic 已招募前谷歌 TPU 负责人 Amir Salek，并与多家 AI 芯片初创公司进行了会谈。 这一动向表明，前沿 AI 实验室日益将定制芯片视为控制算力成本和供应的关键，效仿谷歌（TPU）和亚马逊（Trainium）的做法。合作或收购可以降低 Anthropic 对英伟达的依赖，并可能改变 AI 推理硬件的竞争格局。 MatX 由前谷歌 TPU 工程师创立，此前已融资 5 亿美元；其 MatX One 芯片基于可分割的脉动阵列架构，宣称在大模型推理的吞吐和延迟上表现优异，预计 2027 年出货。据报道，70 亿美元的收购报价远高于 MatX 当前约 40 亿美元的融资估值。

rss · AI Hot · Aug 28, 07:00

**背景**: MatX 是一家由前谷歌 TPU 工程师创立的低调 AI 芯片初创公司，目标是挑战英伟达在 AI 加速器领域的主导地位。TPU 是谷歌为机器学习中的大规模矩阵运算量身定制的专用芯片，谷歌之所以自研，是因为认为完全依赖英伟达 GPU 存在长期风险。MatX One 芯片瞄准大模型推理中“高吞吐”与“低延迟”难以兼得的难题，而这正是 GPU 并非最优的场景。与其他前沿 AI 实验室一样，Anthropic 在算力上投入数十亿美元，因此自研或合作开发芯片成为有吸引力的战略选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://matx.com/research/series_b">MatX One and our Series B | MatX</a></li>
<li><a href="https://www.techbuzz.ai/articles/matx-raises-500m-to-challenge-nvidia-s-ai-chip-dominance">Ex-Google TPU engineers land half-billion raise for AI chip startup MatX</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI芯片`, `#MatX`, `#AI基础设施`, `#收购谈判`

---

<a id="item-11"></a>
## [腾讯发布开源 MoE 旗舰模型 Hy4 Preview](https://aihot.virxact.com/items/cmtcme3kb017ero64b9lt7bla) ⭐️ 8.0/10

腾讯发布了 Hy4 Preview，一款采用 Apache 2.0 许可证的开源权重 MoE 旗舰模型。该模型拥有 770B 总参数、每 token 激活 49B 参数以及 1M token 上下文窗口，主打生产力场景并保持定价稳定。 一款 770B 参数、采用宽松 Apache 2.0 许可证的开源权重模型，让开发者和企业可以自由地自托管、微调并将前沿级模型商业化。这将加剧开源 MoE 领域与 DeepSeek、Qwen 等对手的竞争，推动开源生态向前沿能力迈进。 该模型为 Preview（预览）版本，尚未经基准测试验证是否达到 SOTA 水平，对其实际性能宣称应保持谨慎。稀疏 MoE 设计意味着 770B 参数中每个 token 仅激活 49B，相比同等规模的稠密模型大幅降低了推理计算量。

rss · AI Hot · Aug 28, 06:49

**背景**: MoE（混合专家）是一种架构，每个输入 token 仅由模型参数的一个子集（“专家”）处理，从而在不按比例增加计算成本的情况下获得更大的模型容量。采用 Apache 2.0 许可证的开源权重模型属于最宽松的许可之一，允许商业使用、修改和再分发，限制极少——到 2026 年它已成为 Hugging Face 上开源权重模型采用最多的许可证。1M token 上下文窗口意味着模型可以在单次请求中处理约一百万个 token（整个代码库或长文档集），这是目前领先前沿模型才具备的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://localaimaster.com/blog/mixture-of-experts-explained">Mixture of Experts Explained: How DeepSeek... | Local AI Master</a></li>
<li><a href="https://presenc.ai/research/open-weight-license-landscape-2026">Open - Weight License Landscape 2026 | Presenc AI</a></li>
<li><a href="https://www.morphllm.com/llm-context-window-comparison">LLM Context Window Comparison (2026): 20 Models From 200K to...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#MoE`, `#open-source`, `#Tencent`

---

<a id="item-12"></a>
## [Qwen3.8-Flash 上线 OpenCode Go 编程工具](https://aihot.virxact.com/items/cmtcm0cqr02p9rojzho2o4n50) ⭐️ 8.0/10

阿里巴巴 Qwen 团队宣布，Qwen3.8-Flash 现已上线 OpenCode Go 编程工具。该模型采用 125B 总参数 / 6B 激活参数的 MoE 架构，支持 100 万 token 上下文和多模态能力。 OpenCode Go 是每月约 10 美元的订阅服务，通过一个 API 密钥即可使用多种顶级模型，此次接入一个快速、长上下文的多模态模型，让开发者能以极低成本获得强大的编程能力。这也表明 Qwen 正持续通过平价的第三方编程平台分发其前沿模型。 该模型采用混合专家（MoE）设计：总参数约 125B（含 51B 嵌入表和多 token 预测模块后磁盘上约 180B），但每个 token 仅激活 6B 参数，推理成本接近小型稠密模型。其 100 万 token 上下文和多模态输入支持编程、智能体工作流、视觉理解、代码库分析和长视频分析。

rss · AI Hot · Aug 28, 06:41

**背景**: Qwen 是阿里巴巴的大语言模型系列，"Flash" 产品线主打快速、高效的推理。OpenCode Go 是订阅制 AI 编程服务，以固定月费将多种模型（GPT、Kimi、DeepSeek、GLM、Qwen 等）整合到一个 API 密钥下。MoE（混合专家）模型让每个 token 只经过一小部分参数，以小模型的计算成本获得大模型的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3.8-flash">Qwen 3 . 8 Flash - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.orcarouter.ai/blog/qwen-3-8-flash-release">Qwen3.8-Flash: open-weight 6 B -active MoE previews Qwen4</a></li>
<li><a href="https://www.bitdoze.com/opencode-go-plan/">OpenCode Go Review 2026: 18 AI Models for $10/Month...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#AI models`, `#coding`, `#multimodal`

---

<a id="item-13"></a>
## [Qwen3.8-Flash 上线 GMI Cloud，作为 Qwen4 架构早期预览](https://aihot.virxact.com/items/cmtclbinp029orojzeeu58bdm) ⭐️ 8.0/10

阿里云发布了 Qwen3.8-Flash，这是一款多模态 MoE（混合专家）模型，也是即将到来的 Qwen4 架构的早期预览。该模型现已通过 GMI Cloud、阿里云百炼（Model Studio）和 Qwen Cloud 等 API 渠道开放访问。 此次发布标志着阿里云在 Qwen3 系列之后的下一代架构方向，让开发者得以提前了解 Qwen4 的设计思路。通过多家推理服务商开放访问，降低了开发者构建编程助手、智能体工作流和多模态应用的门槛。 根据各服务商页面，Qwen3.8-Flash 拥有百万 token 的上下文窗口，适用于编程辅助、智能体工作流、视觉理解、文档与代码库分析以及长视频分析。但官方在发布时未公布参数量、专家配置等详细技术细节。

rss · AI Hot · Aug 28, 06:35

**背景**: MoE（混合专家）架构在处理每个输入时只激活一小部分专门的“专家”网络，从而在不按比例增加计算成本的情况下扩大模型容量，Mixtral、Grok-1 和 DeepSeek 等模型均采用该架构。GMI Cloud 是 NVIDIA 参考云平台合作伙伴，提供 GPU 优化的训练与推理服务。Qwen 是阿里的旗舰大模型系列，其中“Flash”版本定位为面向高吞吐场景的高速、高性价比模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qwencloud.com/models/qwen3.8-flash">Qwen 3 . 8 - Flash - QwenCloud</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-flash">Qwen 3 . 8 Flash - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://nano-gpt.com/models/text/alibaba/qwen3.8-flash">Qwen 3 . 8 Flash model | NanoGPT</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#multimodal`, `#MoE`, `#model-release`

---

<a id="item-14"></a>
## [腾讯开源混元 Hy4 preview：770B 参数 MoE 模型，支持 1M 上下文](https://aihot.virxact.com/items/cmtckiu8a01imrojzjag515ji) ⭐️ 8.0/10

腾讯发布了新一代开源混合专家（MoE）语言模型混元 Hy4 preview，总参数 770B，每个 token 激活 49B 参数（共 78 层），上下文长度达 1M。该模型已上线腾讯云 TokenHub 和 OpenRouter。 这使腾讯的开源模型跻身开源模型第一梯队，加剧了与其他前沿开源模型的竞争。1M 上下文和高效的 MoE 设计对需要处理长文档和构建智能体应用的开发者极具吸引力，减少了对闭源 API 的依赖。 作为 preview 版本，它是腾讯已确认仍在训练中的更大规模多模态 Hy4 模型的前身。MoE 架构意味着每个 token 仅激活 770B 参数中的 49B，推理成本远低于同等规模的稠密模型。

rss · AI Hot · Aug 28, 06:15

**背景**: 混合专家（MoE）是一种将模型拆分为多个专家子网络、每次输入只激活相关部分的架构，从而将模型容量与计算成本解耦。混元是腾讯的旗舰 AI 模型系列，腾讯在 2026 年第二季度财报电话会议上曾提及。OpenRouter 是流行的模型聚合平台，通过统一 API 提供对 OpenAI、Google、Anthropic 等数百家模型的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/tencent/Hy4-preview">tencent / Hy 4 -preview | vLLM Recipes</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/12095/tencent-hunyuan-hy4-in-training">Tencent Confirms Hy 4 , a Bigger Multimodal Model , Is in Training</a></li>
<li><a href="https://weventure.de/en/blog/mixture-of-experts">The magic of Mixture of Experts : More performance, lower costs</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#model-release`

---

<a id="item-15"></a>
## [Google 发布 Gemini 3.5 Transcribe：85+ 语言平均 WER 2.6% 的语音转文本模型](https://aihot.virxact.com/items/cmtcidfr503q8roucvz17doy5) ⭐️ 8.0/10

Google 发布了 Gemini 3.5 Transcribe 语音转文本模型，在超过 85 种语言上报告了平均 2.6% 的词错误率（WER）。该模型通过 Interactions API 处理预录音频文件，并通过 Live API 支持双向流式音频。 在 85+ 种语言上实现 2.6% 的平均 WER 将为语音识别设立新的基准，在许多语言上接近甚至超越人类级别的转录准确率。这将增强 Google 在竞争激烈的 ASR 市场中相对于 OpenAI Whisper 等产品的地位，并惠及构建语音助手、字幕和转录产品的开发者。 该模型通过两个 API 提供：Interactions API 用于预录文件的批量转录，Live API 用于实时双向流式处理。WER 数据为厂商自行报告的基准结果，独立评测可能因领域、口音和音频质量不同而有所差异。

rss · AI Hot · Aug 28, 05:00

**背景**: 语音转文本（也称 ASR，自动语音识别）将语音音频转换为文本，词错误率（WER）——即被错误转录的词的比例——是标准的准确率指标。更低的 WER 非常重要，因为转录错误会在语音助手、字幕和会议记录等下游应用中被放大。Google 长期以来凭借其语音 API 在该领域竞争，而 OpenAI 的 Whisper 等端到端神经模型近年来也推动了多语言准确率的提升。

**标签**: `#Google`, `#Gemini`, `#speech-to-text`, `#ASR`, `#AI models`

---

<a id="item-16"></a>
## [Anthropic 发布模型硬件标准（MHS），进军物理 AI 领域](https://aihot.virxact.com/items/cmtcidn1i03sjrouca5fgb7sv) ⭐️ 8.0/10

Anthropic 以研究预览形式发布了模型硬件标准（MHS），这是一套让 AI 智能体安全发现并操控可编程物理设备（如显微镜、机械臂和量子计算设备）的共享规范。基因泰克（Genentech）报告称，通过 MHS 让 AI 直接控制多台异构实验设备，其全自动剂量反应实验的整体开发与运行时间缩短至原来的三分之一。 这标志着 Anthropic 首次公开进军具身智能与物理 AI 领域，将其以协议为先的策略（如 MCP）从数字世界延伸到物理硬件。统一的设备控制标准有望大幅降低 AI 驱动的实验室自动化与先进制造门槛，将影响机器人、制药和工业自动化等生态。 MHS 被描述为类似 MCP 的统一接口与驱动规范，通过标准化命令让 AI 智能体与任意设备交互，目前研究预览仅向首批科研实验室和先进制造商开放。它只是研究预览而非成品或模型突破，其安全性与设备覆盖范围仍有待实际验证。

rss · AI Hot · Aug 28, 04:46

**背景**: Anthropic 此前推出了模型上下文协议（MCP），这是一个将 AI 应用连接到数据源、工具和工作流的开放标准，常被比作 AI 的 USB-C 接口。MHS 将同样的理念应用于硬件：通过单一协议取代碎片化的定制集成，让 AI 智能体控制物理设备。物理 AI 或具身智能指通过机器人、传感器和机器在现实世界中感知、思考并行动的 AI 系统，而不仅仅是回答文本问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/">Anthropic 's new hardware standard lets AI agents... - Ars Technica</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#embodied AI`, `#MHS`, `#AI agents`, `#robotics`

---

<a id="item-17"></a>
## [谷歌员工内部测试 Gemini 3.8 Flash 预览版](https://www.ithome.com/0/995/594.htm) ⭐️ 8.0/10

据《商业内幕》报道，谷歌内部名称为“Gemini 3.8 Flash Preview”的模型已上线内部编程平台 Jetski，供员工测试。一名参与测试的员工表示其体验已明显好于 3.7 Flash，但目前尚难下定论。 此次泄露表明谷歌正以接近每月一次的节奏快速迭代 Flash 模型，以追赶 OpenAI 和 Anthropic，但至今仍缺乏能正面对标竞争对手的前沿 Pro 模型。在企业日益关注 AI 成本的背景下，速度快、价格低的 Flash 模型正成为谷歌的主要竞争筹码，尤其适用于编程和消耗 Token 较快的智能体任务。 Flash 系列更新极快：Gemini 3.6 Flash 于 7 月发布，仅三周后 3.7 Flash 便接续推出，CEO 皮查伊也提出希望将发布节奏提高到接近每月一次。需要注意的是，这只是内部预览版的泄露而非正式发布，公开上线时间尚无法确定。

rss · IT HOME · Aug 28, 07:06

**背景**: 谷歌 Gemini 产品线涵盖高端 Pro 模型和更便宜、更快的 Flash 模型；Flash 被定位为编程和运行智能体的“主力模型”，因为智能体执行任务时消耗 Token 远快于普通聊天机器人。由于 Gemini 3.5 Pro 迟迟未亮相，而 Anthropic 和 OpenAI 持续推进前沿模型，谷歌受到不少质疑。智能体助手正成为新战场：谷歌今年早些时候推出了 Gemini Spark 个人智能体，Meta 也在内部测试名为“Hatch”的智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8">Google Employees Are Already Testing the Next... - Business Insider</a></li>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/">The Gemini app becomes more agentic, delivering proactive, 24/7 help</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#AI models`, `#AI competition`, `#LLM`

---

<a id="item-18"></a>
## [消息称 Anthropic 曾考虑以约 70 亿美元收购 AI 芯片初创公司 MatX](https://www.ithome.com/0/995/591.htm) ⭐️ 8.0/10

路透社 8 月 27 日报道称，Anthropic 曾有意以约 70 亿美元收购 AI 芯片初创公司 MatX，但双方谈判现已转向合作模式。MatX 同时正寻求以约 40 亿美元的估值筹集新资金。 这一消息表明，头部 AI 实验室 Anthropic 正在推进自研训练和推理芯片的战略，呼应了整个行业降低对英伟达 GPU 依赖的趋势。成功的造芯战略有望大幅降低其长期算力成本，并增强其相对于谷歌、OpenAI 等竞争对手的竞争力。 MatX 宣称其 MatX One 芯片的吞吐超过所有已公布竞品，在训练和推理预填充上算力表现出色，在推理解码与强化学习负载上则在延迟、算力和长上下文支持方面均有优势。Anthropic 最近招募了前谷歌 TPU 负责人 Amir Salek，并已与多家 AI 芯片初创公司会谈，但尚未确定是做训练芯片还是推理芯片。

rss · IT HOME · Aug 28, 07:00

**背景**: MatX 是一家由前谷歌员工创立的美国半导体初创公司，专注于为大语言模型设计 AI 芯片；其最近完成了 5 亿美元的 B 轮融资，由前 OpenAI 研究员 Leopold Aschenbrenner 创立的 Situational Awareness 领投，Jane Street 联合领投。大模型推理分为两个阶段：预填充（prefill）可并行处理输入上下文，而解码（decode）需逐个生成输出 token、难以并行，因此针对不同阶段优化的芯片非常重要。谷歌的 TPU 是定制 AI 加速芯片最著名的例子，Anthropic 招募其前负责人显示出其在算力垂直整合上的决心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://matx.com/">MatX : High-throughput chips for LLMs</a></li>
<li><a href="https://completeaitraining.com/news/ex-googlers-matx-lands-500m-to-ship-high-throughput-low/">Ex-Googlers' MatX Lands $500M to Ship High-Throughput...</a></li>
<li><a href="https://www.parasail.io/blog/prefill-vs-decode-llm-inference">Prefill vs . decode in LLM inference</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI chips`, `#MatX`, `#compute infrastructure`, `#AI industry`

---

<a id="item-19"></a>
## [英伟达 Q4 营收 681 亿美元超预期，下季度指引上调至 780 亿美元](https://t.me/zaihuapd/43450) ⭐️ 8.0/10

英伟达第四财季营收达 681 亿美元，其中数据中心业务贡献 623 亿美元，每股利润 1.62 美元，均高于市场预期。公司预计 2027 财年第一季度销售额将达 780 亿美元，显著超过华尔街预测的 726 亿美元，盘后股价上涨超过 3%。 英伟达的业绩是前沿 AI 算力需求持续增长最直接的财务信号，其数据中心业务收入占比已超过九成，直接反映各大 AI 实验室和云厂商的资本开支。强劲的指引向投资者表明，尽管存在竞争和客户融资能力的担忧，AI 基础设施建设仍在持续推进。 首席执行官黄仁勋表示计算需求呈指数级增长，公司已通过战略手段锁定库存以应对供应链压力，其中存储已成为明显瓶颈。游戏与汽车业务营收未达预期，部分投资者仍担忧 OpenAI 的融资能力及行业竞争加剧。

telegram · @zaihuapd · Aug 27, 08:51

**背景**: 英伟达主导 AI 训练和推理 GPU 市场，其数据中心业务（计算加网络）已成为超大规模云厂商和 AI 实验室巨额 AI 基础设施支出的最大受益者。公司目前处于 Blackwell 产品周期，主力产品为 B300/GB300 系统。由于英伟达处于 AI 供应链的核心位置，其季度财报被广泛视为 AI 行业整体景气度的风向标，而 OpenAI 等客户持续融资的能力则直接影响市场对其需求的预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ofweek.com/ai/2026-05/ART-201713-8420-30688258.html">英 伟 达 : 群雄逼宫、AI... - OFweek 人工智能网</a></li>
<li><a href="https://www.okx.com/zh-hans-ar/orbit/insight/85764046715296">今天这个走势我觉得更有意思了。 英 伟 达 财报落地以后，市场给... | 欧易</a></li>
<li><a href="https://news.pedaily.cn/202605/564202.shtml">英 伟 达 ：群雄逼宫、AI「堵点」生变，宇宙股也会「小失意」？_ 投资界</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI infrastructure`, `#data center`, `#earnings`, `#AI compute`

---

<a id="item-20"></a>
## [OpenAI 被曝开发常驻 Codex 代理，持续工作直至休眠](https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/) ⭐️ 8.0/10

据 WIRED 审查的代码，OpenAI 正在为命令行版 Codex 添加「常驻模式」：代理将持续工作直到被「休眠」，不同于现有模式几分钟或几小时后即停止的做法。该模式内置「主动性」设定，代理可在答完请求后自行创建后续任务、跨会话执行，并依据对用户的了解决定工作内容。 这是迈向真正自主、常驻运行的 AI 代理的重要一步——代理将主动行动而非仅响应指令。Codex 已拥有超过 200 万周活跃用户，并被定位为企业级代理平台，常驻自主能力可能重塑开发者和企业向 AI 委托持续性工作的方式。 安全护栏仍然保留：改动用户系统之外的任何东西仍需事先批准。OpenAI 确认该功能正在测试中，但表示暂无近期上线计划。

telegram · @zaihuapd · Aug 28, 02:47

**背景**: Codex 是 OpenAI 的 AI 编程代理，于 2025 年 4 月以 Codex CLI 形式发布，现可通过 ChatGPT 网页应用、命令行工具、桌面应用和 IDE 集成使用。到 2026 年 3 月，其周活跃用户已超过 200 万，OpenAI 正将其定位为可承担软件开发之外任务的企业级代理平台。现有 AI 代理通常以离散会话方式运行，会话之间会丢失上下文，因此能够独立循环、具备持久记忆的常驻代理已成为行业重要趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent)</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI agents`, `#Codex`, `#autonomous agents`, `#frontier AI`

---