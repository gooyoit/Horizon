---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> From 99 items, 7 important content pieces were selected

---

1. [腾讯开源 Hy4 预览版模型，实现递归自我改进循环](#item-1) ⭐️ 9.0/10
2. [腾讯发布 Hy4 Preview：770B 参数开源权重大模型，支持 100 万 token 上下文](#item-2) ⭐️ 9.0/10
3. [腾讯发布 Hy4 Preview：770B 参数开源权重文本模型，上下文窗口达 1M token](#item-3) ⭐️ 9.0/10
4. [MirroS 发布 Code-as-World：将真实视频重写为可执行的 MuJoCo 物理程序](#item-4) ⭐️ 8.0/10
5. [腾讯开源 Hy4 preview：770B 参数 MoE 模型，上下文超百万](#item-5) ⭐️ 8.0/10
6. [腾讯开源 Hy4 预览版：770B 参数 MoE 大模型，上下文超 100 万 token](#item-6) ⭐️ 8.0/10
7. [OpenAI 将于 2026 年 11 月 12 日终止向 Cursor 提供模型](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [腾讯开源 Hy4 预览版模型，实现递归自我改进循环](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 9.0/10

腾讯发布并开源了 Hy4 预览版，这是一个总参数量 770B、激活参数 49B 的下一代混合专家（MoE）大语言模型，上下文窗口超过 100 万 token。值得注意的是，该模型参与了自身开发过程，首次用于自动化优化训练方法、数据策略、评估框架和底层算子，形成了早期阶段的递归自我改进循环。 这是首批前沿模型发布中模型自身实质性地参与自身训练流程的案例之一，是迈向长期被假设的递归自我改进范式的具体一步。结合开放权重和激进定价，它加剧了开源前沿模型领域的竞争，也让研究者能够直接研究自我改进技术。 Hy4 预览版已在多家服务商上线，输入约每百万 token 0.83 美元、输出约 2.50 美元，缓存成本仅为 5%，远低于业界常见的 10-20%。它支持最多 64,000 个输出 token，上线数天内在 OpenRouter 上已处理数万亿 token，超过 GLM 5.3 一周的用量。

hackernews · shenli3514 · Aug 29, 19:33 · [社区讨论](https://news.ycombinator.com/item?id=49492632)

**背景**: 递归自我改进（RSI）是一种假设的过程，即 AI 系统改进自身的代码或训练，理论上可能引发智能爆炸，但此前的尝试均未显示出这种爆炸。Hy4 的循环是一个早期的、有边界的版本：模型提出方案、运行实验并根据结果迭代，产生的代码、日志和反馈被用于后续探索轮次。混合专家（MoE）架构每个 token 只激活总参数的一小部分，从而以更低的推理成本获得更大的模型容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open-Sources Tencent Hy 4 preview - Tencent</a></li>
<li><a href="https://models.dev/models/tencent/hy4-preview/">Hy 4 preview pricing, providers, and specs | Models .dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了 Hy4 在 OpenRouter 上的巨大流量，部分归因于异常便宜的 5%缓存定价，并讨论了递归自我改进声明的意义。还有人担忧 token 密度优化类似'新话'（Newspeak），并批评模型厂商发布误导性的基准测试图表。

**标签**: `#AI`, `#frontier-models`, `#open-source`, `#recursive-self-improvement`, `#Tencent`

---

<a id="item-2"></a>
## [腾讯发布 Hy4 Preview：770B 参数开源权重大模型，支持 100 万 token 上下文](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 9.0/10

腾讯发布了 Hy4 Preview，这是一个开源权重的纯文本大模型，总参数量 770B（MoE 架构下激活参数 49B），上下文窗口达 100 万 token，在 Hugging Face 上的文件大小为 1.56TB。相比 7 月份的 Hy3（总参数 295B、激活 21B、上下文 25.6 万）是一次大幅升级。 这是一次重要的开源权重前沿模型发布，缩小了可自由下载模型与闭源前沿系统之间的差距，让研究者和开发者能用上超长上下文的超大模型。这也表明腾讯等中国实验室在开源 AI 领域依然是最激进的参与者之一，加剧了全球竞争。 该模型仅支持文本输入（无视觉能力），其聊天模板显示只有两档推理强度设置：默认的 'high' 和关闭推理的 'no_think'。Simon Willison 的测试显示其推理过程使用略为简略的英语以节省 token，并且该模型在他的 SVG 生成测试中表现良好，已可通过 OpenRouter 使用。

rss · Simon Willison · Aug 29, 23:53

**背景**: 混合专家（MoE）模型拥有很大的总参数量，但每个 token 只激活其中一部分“专家”，因此 770B 总参数、49B 激活的模型能以远低于同规模稠密模型的推理成本获得广泛的知识。“开源权重”意味着模型文件可以下载并在本地运行，但 1.56TB 的大小意味着运行它需要相当可观的硬件资源。聊天模板（在 Hugging Face 上以 chat_template.jinja 形式存储）定义了提示词的格式，并且可以在官方文档发布之前揭示诸如推理强度控制之类的功能特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between... | Medium</a></li>
<li><a href="https://huggingface.co/docs/transformers/chat_templating_writing">Writing a chat template · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-weights`, `#Tencent`, `#MoE`, `#model-release`

---

<a id="item-3"></a>
## [腾讯发布 Hy4 Preview：770B 参数开源权重文本模型，上下文窗口达 1M token](https://aihot.virxact.com/items/cmtf2n1vh01i0ron8nxicpb3h) ⭐️ 9.0/10

腾讯发布了 Hy4 Preview，这是一款开源权重、纯文本输入的大语言模型，总参数 770B（每 token 激活 49B），上下文窗口达 1M token，在 Hugging Face 上的体积为 1.56TB。相比 7 月发布的 Hy3（总参数 295B、激活 21B、上下文 256k、体积 598GB），规模大幅提升。 这是一次前沿规模的开源权重发布，参数量和上下文长度都远超前代，让开源社区获得了通常只有闭源模型才具备的能力。1M token 的上下文窗口可以在单次处理中应对超长文档、代码库或对话。 Hy4 仅支持纯文本输入，不具备视觉能力，推理配置只支持两档："high"（默认）和 "no_think"。1.56TB 的下载体积意味着本地部署需要大量硬件资源，实际使用可能仅限于资源充足的组织。

rss · AI Hot · Aug 29, 23:53

**背景**: Hy4 采用混合专家（MoE）架构，每个 token 只激活模型参数的一部分（770B 中的 49B），以更大的总参数量换取可控的推理成本。"开源权重"模型是指公开发布训练参数的模型，任何人都可以下载、运行和修改，但与同时公开训练数据和代码的完全开源模型有所区别。"no_think" 模式会跳过显式的思维链推理，在简单任务上给出更快、更简洁的回答，与近期其他推理模型的类似模式相似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.emergentmind.com/topics/thinking-based-non-thinking-tnt">TNT: Non-Thinking Reasoning in LLMs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#Tencent`, `#long-context`, `#model-release`

---

<a id="item-4"></a>
## [MirroS 发布 Code-as-World：将真实视频重写为可执行的 MuJoCo 物理程序](https://aihot.virxact.com/items/cmtf5v6ig0294ro07i4r7racq) ⭐️ 8.0/10

MirroS 提出了 Code-as-World 范式，将物理场景表示为可在 MuJoCo 物理仿真器中运行的可执行 scene.json 文件。这些场景描述通过最多五轮迭代的智能体循环从真实视频中恢复得到。 这项工作将被动观看的视频转化为可执行、可编辑的世界模型，连接了视频理解与物理仿真，对具身智能、机器人和世界模型研究都高度相关。它有望让研究者更便捷地从真实数据生成仿真环境，用于智能体的训练与评估。 该系统采用最多五轮的智能体循环，智能体基于仿真输出与源视频之间的差异来编写、运行并迭代优化 scene.json。其输出基于 MuJoCo——一个由 Google DeepMind 维护的开源、擅长接触动力学的物理仿真器。

rss · AI Hot · Aug 30, 01:35

**背景**: MuJoCo（Multi-Joint dynamics with Contact）是一个广泛使用的物理仿真器，2021 年被 Google DeepMind 收购并于 2022 年开源，在机器人和强化学习研究中非常流行。世界模型旨在让 AI 系统拥有对环境的内部预测性表征，而具身智能研究智能体如何通过与仿真器或真实机器人的交互来学习。智能体 AI（Agentic AI）指能够自主规划步骤、调用工具、观察结果并循环迭代直到完成任务的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MuJoCo">MuJoCo - Wikipedia</a></li>
<li><a href="https://github.com/google-deepmind/mujoco">GitHub - google-deepmind/mujoco: Multi-Joint dynamics with Contact. A general purpose physics simulator. · GitHub</a></li>
<li><a href="https://agentic.ai/what-is-agentic-ai">What Is Agentic AI? Definition, 6 Levels & Examples (2026)</a></li>

</ul>
</details>

**标签**: `#world models`, `#embodied AI`, `#video understanding`, `#physics simulation`, `#AI research`

---

<a id="item-5"></a>
## [腾讯开源 Hy4 preview：770B 参数 MoE 模型，上下文超百万](https://aihot.virxact.com/items/cmtf5cfy501rcro07i1lflqmc) ⭐️ 8.0/10

腾讯 Hy 团队开源了 Hy4 preview，这是一款混合专家（MoE）旗舰模型，总参数 770B、每 token 激活 49B，支持超过 100 万 token 的上下文，端到端吞吐较基线提升 31.8%。同期，Anthropic 分享了员工内部使用 Claude 的一线实践，携程机票团队推出了「代码即文档」工程工具 Lumos，已接入 74 个业务仓库。 770B 参数、百万级上下文的开源权重 MoE 模型使腾讯直接参与前沿开源模型的竞争，为研究者和企业提供了可自部署的强大替代方案。另外两条新闻则反映了行业趋势：AI 厂商分享真实的内部使用实践，以及企业构建让代码库对 AI 更友好的工程基础设施。 根据 vLLM recipes，Hy4 preview 共有 78 层，可在 16 张 B200 或 8 张 B300 GPU 上部署，并支持 MTP（多 token 预测）。这是预览版本，正式版发布前能力和稳定性可能仍有变化。

rss · AI Hot · Aug 30, 01:19

**背景**: 混合专家（MoE）是一种模型架构，每个 token 只激活一部分参数（即「专家」），从而在总参数量非常大的同时保持较低的推理计算成本——本模型 770B 参数中每个 token 仅激活 49B。超长上下文（100 万 token 以上）支持一次性处理整个代码库或长文档。「代码即文档」工具（如 Lumos）的目标是让源代码本身充当文档，提升大型代码仓库的可维护性和 AI 理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview · Hugging Face</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview · GitHub</a></li>
<li><a href="https://recipes.vllm.ai/tencent/Hy4-preview">tencent/Hy4-preview — 770B / 49B active · MOE · 1024K ctx</a></li>

</ul>
</details>

**标签**: `#open-source-model`, `#MoE`, `#Tencent`, `#LLM`, `#Anthropic`

---

<a id="item-6"></a>
## [腾讯开源 Hy4 预览版：770B 参数 MoE 大模型，上下文超 100 万 token](https://aihot.virxact.com/items/cmtf5cfy501rdro073jceu89n) ⭐️ 8.0/10

腾讯发布并开源了下一代大语言模型 Hy4 预览版，采用混合专家（MoE）架构，总参数量 770B、激活参数 49B，上下文窗口超过 100 万 token。该模型已接入腾讯 WorkBuddy 和 CodeBuddy 产品，官方称端到端吞吐较内部基线提升 31.8%。 这是一次前沿规模的开源权重发布，让全球开源社区能够获得在规模和上下文长度上可与顶级闭源系统竞争的模型。同时它也强化了腾讯内部 AI 生态——WorkBuddy 已是中国日活用户最多的生产力智能体工具之一。 Hy4 预览版是早期版本，据报道腾讯计划在 2026 年发布规模更大、聚焦智能体（agentic）能力的完整版 Hy4。MoE 设计意味着每个 token 仅激活 770B 参数中的 49B，推理效率远高于同等总参数量的稠密模型。

rss · AI Hot · Aug 30, 01:19

**背景**: 混合专家（MoE）是一种架构，由路由器为每个 token 选择一小部分"专家"网络，因此模型可以拥有极大的总参数量，同时保持较低的每 token 计算成本。100 万 token 级别的长上下文窗口可以在一次处理中读入整个代码库或长文档，对腾讯 CodeBuddy 这类编程智能体尤其有价值。Hy4 是腾讯 Hy3 的继任者，延续了 DeepSeek、Qwen 等竞争对手也在采用的开源权重策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open-Sources Tencent Hy4 preview - Tencent</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1w0igxk/tencenthy4preview_770ba49b_weight_dropped/">r/LocalLLaMA on Reddit: Tencent/Hy4-preview 770B-A49B weight dropped</a></li>
<li><a href="https://www.tencent.com/en-us/articles/2202350.html">Tencent Cloud Debuts Productivity Agent Suite... - Tencent 腾讯</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 的 r/LocalLLaMA 社区，用户讨论了 Tencent/Hy4-preview（770B-A49B）权重的发布，并指出这是该模型的早期版本。

**标签**: `#LLM`, `#open-source`, `#Tencent`, `#MoE`, `#model-release`

---

<a id="item-7"></a>
## [OpenAI 将于 2026 年 11 月 12 日终止向 Cursor 提供模型](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI 宣布，在 SpaceX 收购 Cursor 之后，将终止向 Cursor 提供 OpenAI 模型的合同，建议停服日期为 2026 年 11 月 12 日。OpenAI 理由是马斯克旗下公司有违约记录，包括 Twitter 被收购后违反合同，以及 xAI 今年在宣誓下承认违反 OpenAI 服务条款。 这将使最流行的 AI 编程工具之一失去头部模型供应商，迫使 Cursor 的数百万开发者用户转向其他模型。这也标志着 Sam Altman 与 Elon Musk 之间长期争斗的重大升级，显示商业整合与个人恩怨正在重塑 AI 生态格局。 OpenAI 与 Cursor 之间合作近四年的定制协议包含控制权变更条款，允许在收购后的限定时间内终止合作。OpenAI 表示无法确信 SpaceX 会遵守服务条款，并指出 xAI 曾在宣誓下承认利用 OpenAI 的输出训练 Grok，而这正是服务条款所禁止的。

telegram · @zaihuapd · Aug 29, 02:24

**背景**: Cursor 由 Anysphere 公司开发，是基于 Visual Studio Code 分叉的 AI 辅助编程编辑器，到 2026 年初估值达 293 亿美元，年度经常性收入超过 30 亿美元。2026 年 6 月起 Cursor 被收购并整合进 SpaceX 的 AI 业务（SpaceXAI），8 月成为其全资子公司。马斯克与 OpenAI 有长期恩怨——他曾联合创立 OpenAI 后离开，其旗下的 xAI 与 OpenAI 的模型直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/openai-ends-cursor-contract-elon-musk-spacex-sam-altman-feud-2026-8">OpenAI Ending Deal With Cursor Because XAI Violated Terms of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://cybersecuritynews.com/openai-models-ends-with-cursor/">OpenAI Is Pulling Its AI Models From Cursor Following SpaceX...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI industry`, `#Elon Musk`

---