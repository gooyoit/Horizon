---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 93 items, 4 important content pieces were selected

---

1. [OpenAI 状态页面显示 Codex 5.5 和 GPT-5.5 出现高错误率](#item-1) ⭐️ 9.0/10
2. [小米开源 OneVL：自动驾驶一步式潜空间推理框架](#item-2) ⭐️ 9.0/10
3. [Anthropic 与 SpaceX 达成 Colossus 1 算力合作，Claude 限额翻倍](#item-3) ⭐️ 9.0/10
4. [OpenAI 提供两个月免费 Codex 以吸引企业用户](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 状态页面显示 Codex 5.5 和 GPT-5.5 出现高错误率](http://status.openai.com/) ⭐️ 9.0/10

OpenAI 官方状态页面当前报告称，Codex 5.5 引擎正经历高错误率，且 GPT-5.5 模型的错误率正在持续升高。这标志着 OpenAI 最新发布的两个前沿 AI 系统出现了显著的服务中断。 此次故障直接影响依赖 OpenAI 最新前沿模型进行生产工作的开发者和企业，尤其是使用 Codex 驱动的智能编程任务。这一事件凸显了即使在最先进的 AI 平台上，快速部署和扩展下一代模型时仍面临持续的可靠性挑战。 GPT-5.5 的内部代号被称为 'Spud'，由 OpenAI 于 2026 年 4 月 23 日发布，而 Codex 平台截至 2026 年 3 月已拥有超过 200 万周活跃用户。错误率被描述为持续升高，表明该问题可能尚未得到完全控制。

telegram · @zaihuapd · May 13, 08:56

**背景**: GPT-5.5 是 OpenAI 于 2026 年 4 月 23 日发布的大语言模型，其前代产品 GPT-5 于 2025 年 8 月 7 日发布。OpenAI 的 Codex 是一个 AI 驱动的编程智能体平台，能够处理从常规拉取请求到复杂重构和迁移等各类任务，并已被定位为更广泛的企业级智能体平台。在发布 GPT-5.5 之前，OpenAI 对该模型进行了全面的安全性和准备性框架评估，与内外部红队测试人员合作，并收集了近 200 个可信早期访问合作伙伴的反馈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5`, `#Codex`, `#AI Outage`, `#Frontier Models`

---

<a id="item-2"></a>
## [小米开源 OneVL：自动驾驶一步式潜空间推理框架](https://mp.weixin.qq.com/s/7po3r6YtmuXm8Xny1bw61Q) ⭐️ 9.0/10

小米发布并全面开源了 OneVL 一步式潜空间语言视觉推理框架，首次在自动驾驶领域将 VLA 与世界模型统一到同一框架内。该框架在 ROADWork、Impromptu 和 Alpamayo-R1 三项基准上达到 SOTA，NAVSIM PDM-score 达 88.84，首次在潜空间推理中超越显式 CoT（88.29）。 这一突破表明潜空间推理能够在大幅降低推理延迟的同时，达到甚至超越显式思维链方法的性能，这对实时自动驾驶系统至关重要。模型权重和代码的全面开源使更广泛的研究社区能够在此基础上继续探索统一的 VLA-世界模型架构。 OneVL 用视觉 latent token 编码物理因果结构、语言 latent token 编码驾驶意图，训练时通过双辅助解码器预测未来画面与可读思维链，推理时全部移除以实现一步并行生成。挂载 MLP 回归头变体后延迟可压至 0.24 秒，仅为 VLA 自回归推理的 5.4%。

telegram · @zaihuapd · May 13, 10:33

**背景**: 视觉-语言-动作（VLA）模型将视觉感知、语言理解和动作规划整合到统一框架中，是端到端自动驾驶的新兴范式。世界模型学习在给定当前观测的情况下预测环境的未来状态，使智能体能够进行仿真和前瞻规划。思维链（CoT）推理传统上依赖显式的文字化中间步骤，但最近的潜空间 CoT 研究将推理过程嵌入连续潜空间中，使模型无需生成可见 token 即可进行推理。NAVSIM 是广泛使用的自动驾驶评测基准，其 PDM-score 综合衡量驾驶安全性和运动质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.16782">[2505.16782] Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning</a></li>
<li><a href="https://github.com/autonomousvision/navsim">GitHub - autonomousvision/navsim: [CoRL '25] Pseudo-Simulation for Autonomous Driving; [NeurIPS '24] NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking · GitHub</a></li>
<li><a href="https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development">NVIDIA Announces Alpamayo Family of Open-Source AI Models and ...</a></li>

</ul>
</details>

**标签**: `#Autonomous Driving`, `#Vision-Language Models`, `#World Models`, `#Chain-of-Thought`, `#AI Research`

---

<a id="item-3"></a>
## [Anthropic 与 SpaceX 达成 Colossus 1 算力合作，Claude 限额翻倍](https://t.me/zaihuapd/41371) ⭐️ 9.0/10

Anthropic 已与 SpaceX 签署协议，将使用 Colossus 1 数据中心的全部算力，该数据中心包含超过 22 万块 NVIDIA GPU 和超过 300 兆瓦的电力容量。即日起，Claude Code 所有付费方案的 5 小时速率限制翻倍，Pro 和 Max 用户的高峰期限制被取消，Claude Opus 的 API 速率限制也大幅提升。 此次合作使 Anthropic 获得了全球最大 AI 超级计算集群之一的使用权，能够大规模扩展前沿模型训练和推理能力。限额的即时放宽表明新增算力已投入使用，直接惠及依赖 Claude API 和编程工具的开发者与企业。 Colossus 1 数据中心最初由 xAI 建造，位于田纳西州孟菲斯（并扩展至密西西比州 Southaven），现由 SpaceX 拥有，同时支持 X 平台及 Elon Musk 的其他项目。Claude Code 的速率限制基于滚动 5 小时窗口，按套餐等级（Pro、Max 5x、Max 20x）限制 token 用量，达到上限后 Claude Code 将停止响应，直到窗口重置。

telegram · @zaihuapd · May 14, 00:57

**背景**: Colossus 是一台大型 AI 超级计算机，最初由 xAI 在田纳西州孟菲斯建造，此后跨越州界扩展至密西西比州。它为 X（原 Twitter）及 Elon Musk 的其他项目提供计算支持，目前归属于 SpaceX 旗下。Anthropic 是 Claude 系列大语言模型背后的公司，其中包括 Claude Opus，定位为其处理复杂任务（如智能体编程）的最强模型。速率限制是 AI API 服务中管理计算需求的常见做法，通常通过滚动时间窗口来限制用户可消耗的 token 数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/anthropic-to-use-all-of-spacex-xais-colossus-1-data-center-compute/">Anthropic to use all of SpaceX-xAI's Colossus 1 data center compute - DCD</a></li>
<li><a href="https://www.servethehome.com/anthropic-signs-spacex-colossus-1-data-center-to-boost-capacity/">Anthropic Signs SpaceX Colossus 1 Data Center to Boost Capacity - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SpaceX`, `#AI Infrastructure`, `#Compute Scaling`, `#Claude`

---

<a id="item-4"></a>
## [OpenAI 提供两个月免费 Codex 以吸引企业用户](https://twitter.com/sama/status/tweet-2054626219858293128) ⭐️ 8.0/10

Sam Altman 宣布，在未来 30 天内，OpenAI 将为希望尝试切换的公司提供两个月的免费 Codex 使用权限，他称 Codex 是市场上最好的 AI 编程产品。这项促销是限时获客活动，旨在吸引企业从竞争对手的 AI 编程工具转向 Codex。 此举表明 AI 编程代理市场竞争日趋激烈，OpenAI 正在积极争夺企业用户，以对抗 GitHub Copilot、Cursor 等竞争对手。截至 2026 年 3 月，Codex 的周活跃用户已超过 200 万，OpenAI 正将其定位为超越编程工具的更广泛的企业代理平台。 该优惠从公告之日起持续 30 天，为愿意切换的公司提供两个月的免费 Codex 使用权限。Codex 是基于 codex-1 模型构建的云端自主编程代理，具有内置工作树和云端沙箱功能，允许代理跨项目并行工作。

twitter · Sam Altman · May 13, 18:13

**背景**: OpenAI Codex 不应与 2021 年推出的原始 Codex 语言模型混淆，后者是 GPT-3 的衍生版本，曾为 GitHub Copilot 提供支持。当前的 Codex 于 2025 年推出，是一个完全自主的 AI 编程代理，能够在云端沙箱中编写、测试和提交代码，并与 ChatGPT、CLI 工具和 IDE 扩展集成。它旨在处理功能开发、错误修复、拉取请求和代码库查询，通过并行代理执行将数周的工作压缩到数天内完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI</a></li>
<li><a href="https://www.quantumrun.com/consulting/openai-codex/">OpenAI Codex Explained - quantumrun.com</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI Coding Agents`, `#Enterprise AI`, `#Sam Altman`

---