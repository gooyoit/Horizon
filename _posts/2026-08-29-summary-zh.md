---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> From 108 items, 14 important content pieces were selected

---

1. [Z.ai 开源发布 GLM-5.3 模型权重](#item-1) ⭐️ 9.0/10
2. [智谱开源 GLM-5.3 模型权重，主打智能体编程与网络防御](#item-2) ⭐️ 9.0/10
3. [OpenAI 在 Cursor 被 SpaceX/xAI 收购后限制其 API 访问](#item-3) ⭐️ 8.0/10
4. [Google 新论文提出 SKILL.state，用显式执行状态替代智能体对话历史](#item-4) ⭐️ 8.0/10
5. [腾讯混元 Hy4 预览版登陆 Cline 编程智能体](#item-5) ⭐️ 8.0/10
6. [FastVideo 开源 FastH3，实现 14 倍视频生成加速](#item-6) ⭐️ 8.0/10
7. [腾讯混元 Hy4 预览版上线 OpenCode Go](#item-7) ⭐️ 8.0/10
8. [全球首例半侵入式视网膜脑机接口让失明患者重见光明](#item-8) ⭐️ 8.0/10
9. [OpenAI 在 Cursor 被 SpaceX 收购后终止双方合作](#item-9) ⭐️ 8.0/10
10. [世界人形机器人运动会：全自主机器人打破 5 项人类纪录](#item-10) ⭐️ 8.0/10
11. [OpenAI 因 SpaceX 收购 Cursor 将终止向其提供 AI 模型](#item-11) ⭐️ 8.0/10
12. [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](#item-12) ⭐️ 8.0/10
13. [谷歌员工内测 Gemini 3.8 Flash，测试者称明显优于 3.7 Flash](#item-13) ⭐️ 8.0/10
14. [Z.ai 发布 GLM-5.3-Flash：原生多模态 MoE 模型，价格仅为上代十分之一](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Z.ai 开源发布 GLM-5.3 模型权重](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 9.0/10

Z.ai 于 2026 年 8 月 14 日发布 GLM-5.3，并在两周后公开了模型权重，随后于 8 月 26 日推出了 GLM-5.3-Flash 变体。该模型与 GLM-5.2 使用相同的基座模型，所有提升均来自后训练，Z.ai 称其在内部代码基准上提升了 50%。 GLM-5.3 被定位为最强的开源权重编程模型，为开发者提供了一个可自托管的前沿级闭源模型替代方案。它加剧了 Z.ai、DeepSeek、月之暗面（Kimi）等中国开源实验室之间的竞争，并推动整个生态的推理成本下降。 GLM-5.3 与 GLM-5.2 共享基座模型，因此提升完全来自针对复杂编程、长程任务和智能体能力的后训练。社区测试者指出其原始能力略逊于 Kimi，但部署难度低得多，且相比 Qwen3.8 和 GLM-5.2 等过度思考的模型，其 token 消耗与准确率之比明显更优。

hackernews · jeudesprits · Aug 28, 15:20 · [社区讨论](https://news.ycombinator.com/item?id=49479878)

**背景**: 开源权重模型允许任何人下载模型参数并在自己的基础设施上运行，但这并不保证能获得训练数据或完全不受限制的许可。Z.ai 的 GLM 系列是中国开源权重模型浪潮（与 DeepSeek 和 Kimi 并列）的一部分，使前沿级能力得以广泛普及。GLM-5.3 专注于编程和智能体任务，反映了行业向能够自主完成多步骤软件工程工作的模型转变的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities - z.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM-5.3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极：用户称赞 GLM-5.3 是'最佳平衡点'的开源权重模型，有测试者称其'感觉像 Opus 4.8'，在难题上超越了 DeepSeek V4 Flash。讨论的要点包括其相比 Kimi 和 Qwen 更易部署、token 效率更高，不过也有人指出它尚未达到顶级闭源模型的水平。

**标签**: `#open-source-ai`, `#LLM`, `#GLM`, `#model-release`, `#frontier-AI`

---

<a id="item-2"></a>
## [智谱开源 GLM-5.3 模型权重，主打智能体编程与网络防御](https://www.ithome.com/0/995/896.htm) ⭐️ 9.0/10

智谱（Z.ai）已开放 GLM-5.3 模型权重下载，支持本地部署、微调和在 GLM-5.3 许可协议下的商业化使用。该模型擅长复杂编码、长程任务和防御性网络安全，在 Artificial Analysis 综合智能指数中取得 60 分，与 Kimi K3 并列开源模型第一。 这将此前主要通过闭源 API 提供的前沿级 AI 能力交到开发者手中，使其可以本地运行和定制。此举加剧了开源大模型领域的竞争，并降低了构建智能体编程与安全应用的门槛。 GLM-5.3 与 GLM-5.2 使用相同的基座模型，所有提升均来自后训练，并支持 100 万 token 的上下文窗口。商业化使用免费，但年营业额超过 100 亿美元且将 GLM-5.3 作为外部模型服务对外提供的机构需通过安全审查；鉴于模型的网络安全能力，智谱在发布前还额外进行了两周安全评估。

rss · IT HOME · Aug 29, 04:31

**背景**: 智能体编程（agentic coding）指利用 AI 智能体自主完成代码生成、调试、测试等多步骤软件开发任务。Artificial Analysis 综合智能指数是一个覆盖推理、编码、知识、指令遵循和多步骤任务的复合基准，用于衡量模型在真实复杂任务中的综合能力。开放权重发布允许用户下载并在本地运行模型，与只能通过 API 访问的闭源模型形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM-5.3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://unsloth.ai/docs/models/glm-5.3">GLM-5.3 - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.1.1 | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#GLM-5.3`, `#Zhipu AI`, `#LLM release`, `#agentic coding`

---

<a id="item-3"></a>
## [OpenAI 在 Cursor 被 SpaceX/xAI 收购后限制其 API 访问](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI 宣布限制 Cursor 对其模型的访问权限，此前 Cursor 的母公司 Anysphere 被 SpaceX 旗下的 SpaceXAI 以约 600 亿美元的全股票交易收购，交易于 2026 年 8 月 14 日完成。此举切断了这一主流 AI 编程工具与 OpenAI 前沿模型的连接，因为 Cursor 现在归直接竞争对手所有。 这表明前沿 AI 实验室越来越愿意将模型访问权限作为对抗竞争对手的武器，正在重塑开发者工具生态。依赖 GPT 模型的 Cursor 用户将被推向 Grok/Composer 或 Anthropic 的 Claude、Codex 等竞品，加速 AI 编程工具沿竞争阵营走向碎片化。 Anthropic 今年早些时候已因类似的条款违规封禁了 xAI，据报道是在 Musk 承认蒸馏其模型之后，因此 OpenAI 此举是沿袭先例。OpenAI 的服务条款也严格限制未经授权转售 API 访问，而转售多家供应商的模型正是 Cursor IDE 商业模式的基础。

hackernews · @zaihuapd · Aug 29, 01:47 · [社区讨论](https://news.ycombinator.com/item?id=49486172)

**背景**: Cursor 由 Anysphere 公司开发，是一款基于 Visual Studio Code 分支的 AI 辅助代码编辑器，允许开发者通过自然语言指令编写和修改代码；在被收购前估值达 293 亿美元，年度经常性收入超过 30 亿美元。SpaceX 旗下的 SpaceXAI 部门在 SpaceX 于纳斯达克上市后不久，以约 600 亿美元收购了 Anysphere，将 Cursor 整合为全资子公司。由于 Cursor 的 IDE 转售 OpenAI、Anthropic 等多家供应商的模型访问，被竞争模型提供商（xAI 的 Grok 生态）收购后，在 API 条款和竞争对手模型的使用上产生了直接冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company) - Wikipedia</a></li>
<li><a href="https://www.techzine.eu/news/devops/142197/spacex-acquires-cursor-for-60-billion/">SpaceX acquires Cursor for $60 billion - Techzine Global</a></li>
<li><a href="https://finance.yahoo.com/technology/article/how-spacex-benefits-from-its-cursor-acquisition-123000466.html">How SpaceX benefits from its Cursor acquisition</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为这一举动不可避免，指出 Cursor 转售 API 的商业模式一直存在风险，如今该工具主要只对使用 Grok/Composer 的用户有价值。有人指出 Anthropic 此前已因类似条款违规封禁 xAI，并猜测 Anthropic 是否会将封禁扩大到 Cursor。一些用户表示，这一限制只会让他们回归 Anthropic 生态，彻底放弃 OpenAI 的模型。

**标签**: `#OpenAI`, `#Cursor`, `#xAI`, `#AI industry`, `#developer tools`

---

<a id="item-4"></a>
## [Google 新论文提出 SKILL.state，用显式执行状态替代智能体对话历史](https://aihot.virxact.com/items/cmtdubvmq072ero2m9mgeh7xp) ⭐️ 8.0/10

Google 发表论文（arXiv 2608.26263）提出 SKILL.state，这是一种用显式、可变的执行状态替代只增不减的对话历史的智能体运行时架构。在 100 步仓库任务中，Gemini-3-Flash 配合 SKILL.state 仅用 65,408 tokens 取得 0.94 分，而 LangGraph 风格基线消耗 1,062,387 tokens 仅得 0.91 分，token 消耗差距达 16.2 倍。 当前的长程智能体被不断增长的对话历史拖累，成本和延迟上升，上下文膨胀还会降低准确率。SKILL.state 证明紧凑、结构化的状态表示能让智能体既更便宜又更准确，这一结果可能重塑智能体运行时和框架管理记忆的方式。 论文声称显式执行状态是一种与架构无关的抽象，意味着它不局限于 LangGraph 等单一框架。评估在 100 步仓库级任务上使用 Gemini-3-Flash，与基于对话历史的基线进行对比。

rss · AI Hot · Aug 29, 03:33

**背景**: 大多数 LLM 智能体（例如用 LangGraph 构建的）将所有消息、工具调用和观察结果作为工作记忆持续追加保存。当任务增长到几十甚至上百步时，这种只增不减的历史会占用巨大的上下文窗口，推高成本并使模型难以追踪关键信息。SKILL.state 则维护一个小型、可变的状态对象，只保留任务所需的信息，类似于传统程序使用程序状态而非重放执行日志。Gemini-3-Flash 是 Google 面向复杂智能体工作流设计的高效模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.26263">[2608.26263] SKILL.state: Scalable Long-Horizon Agent Skills</a></li>
<li><a href="https://arxiv.org/html/2608.26263">SKILL.state: Scalable Long-Horizon Agent Skills</a></li>
<li><a href="https://github.com/langchain-ai/langgraph">GitHub - langchain-ai/langgraph: Build resilient agents. · GitHub</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Google research`, `#token efficiency`, `#LLM architecture`, `#agentic workflows`

---

<a id="item-5"></a>
## [腾讯混元 Hy4 预览版登陆 Cline 编程智能体](https://aihot.virxact.com/items/cmtdsjspy05n9ro2mh4vphvye) ⭐️ 8.0/10

腾讯发布了混元 Hy4 预览版，这是一个总参数量 770B、激活参数 49B、上下文窗口达 100 万 token 的开放权重 MoE 模型，现已在 Cline 编程智能体中可直接选用。腾讯称该模型在 SWE-bench Pro 上领先，并实现了迄今最大的一次代际跃升。 又一个能与前沿闭源模型竞争的开放权重模型，为开发者提供了可自由下载的替代方案，尤其适用于编程智能体场景。该模型接入拥有超过 800 万开发者的开源智能体 Cline，使前沿级编程能力可以立即在实际工作流中使用。 Hy4 采用混合专家（MoE）架构，总参数 770B，但每次推理仅激活 49B，并支持 100 万 token 的上下文窗口。用户可在 Cline 中通过 'npm i -g cline' 安装后输入 '/model' 选择 Hy4 preview 试用；模型权重也已发布在 Hugging Face（tencent/Hy4-preview）。

rss · AI Hot · Aug 29, 02:34

**背景**: 混元（Hunyuan）是腾讯的大模型系列，Hy4 是其最新一代，腾讯在 2026 年第二季度财报电话会议上确认了该模型的训练进展。SWE-bench Pro 是 SWE-bench 基准的升级版，用于评估模型在真实软件工程任务（如修复代码仓库中的 bug）上的表现。Cline 是一款广受欢迎的开源 AI 编程智能体，支持 Plan/Act 模式、MCP 集成和终端优先的工作流，既可接云端 API 也可用本地模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent / Hy 4 -preview · Hugging Face</a></li>
<li><a href="https://www.kucoin.com/news/flash/tencent-s-hunyuan-hy4-open-sourced-with-770b-total-parameters-and-1m-context">Tencent 's HunYuan Hy 4 is open-sourced with 770 billion... | KuCoin</a></li>
<li><a href="https://cline.bot/">Cline - AI Coding , Open Source and Uncompromised</a></li>

</ul>
</details>

**社区讨论**: 发帖者对又一个开放权重模型能够与前沿闭源模型竞争表示兴奋，并分享了快速上手步骤，方便其他人在 Cline 中亲自试用 Hy4 预览版。

**标签**: `#AI models`, `#open weights`, `#SWE-bench`, `#Tencent Hunyuan`, `#coding agents`

---

<a id="item-6"></a>
## [FastVideo 开源 FastH3，实现 14 倍视频生成加速](https://aihot.virxact.com/items/cmtdrofau04woro2mr5vznkuf) ⭐️ 8.0/10

Sky Computing Lab（UCSD 的 Hao AI Lab）联合 Nuva Lab 和 NVIDIA FastGen 团队开源了 FastH3 预览版 v1，这是对 MiniMax H3 进行 4 步 DMD2 蒸馏后的模型，在 NVIDIA Blackwell GPU 上仅需 13 秒即可生成 15 秒的音视频同步内容，实现 14 倍加速。权重已发布于 HuggingFace。 这项工作让接近实时的开源文生视频（含音频）生成对更广泛的社区成为可能，大幅降低了视频生成应用的成本和延迟门槛。盲测中 45% 的用户更偏好 FastH3 或认为其与原版 MiniMax H3 持平，表明基于蒸馏的加速方法能够保持有竞争力的质量。 FastH3 预览版 v1 是一个 4 步 DMD2 蒸馏、采用稀疏注意力的模型，仅需四次 transformer 前向传播即可从文本生成音视频同步内容。该版本仅使用部分数据和算力训练，因此未来版本的质量还有提升空间。

rss · AI Hot · Aug 29, 02:32

**背景**: 以 MiniMax H3 为代表的视频扩散模型可以生成带原生音频的高质量视频（最高 15 秒、2K 分辨率），但通常需要几十个去噪步骤，推理既慢又昂贵。DMD2 等蒸馏技术可以训练学生模型用极少步数逼近教师模型的输出，而 FastVideo 是一个用于加速视频生成的统一后训练与实时推理框架。FastH3 在 MiniMax（MiniMax 公司发布的开源多模态生成模型）之上应用了这些技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://haoailab.com/blogs/fasth3-preview/">FastVideo FastH3 V1: Open-Weight 4-Step Sparse Distilled Minimax H3 for 14x Speedup on NVIDIA Blackwell GPU | Hao AI Lab @ UCSD</a></li>
<li><a href="https://github.com/hao-ai-lab/FastVideo">GitHub - hao-ai-lab/FastVideo: A unified inference and post-training framework for accelerated video generation. · GitHub</a></li>
<li><a href="https://huggingface.co/FastVideo/FastVideo-FastH3-4-step-Preview-v1-VSA-DataFree">FastVideo/FastVideo-FastH3-4-step-Preview-v1-VSA-DataFree · Hugging Face</a></li>

</ul>
</details>

**标签**: `#video generation`, `#open source AI`, `#FastH3`, `#inference acceleration`, `#generative models`

---

<a id="item-7"></a>
## [腾讯混元 Hy4 预览版上线 OpenCode Go](https://aihot.virxact.com/items/cmtdrh7uw04r1ro2m9mh03zq0) ⭐️ 8.0/10

腾讯混元 Hy4 预览版模型现已上线 OpenCode Go（基于 Go 的 AI 编程智能体）。该模型为 770B 参数的 MoE 架构，每个 token 激活 49B 参数，支持 100 万 token 上下文窗口，专为编程智能体场景优化。 这将一个前沿级的开源模型（Apache 2.0 许可）直接带入流行的终端编程智能体，为开发者提供了专有模型之外的免费选择。这也表明腾讯正与 DeepSeek、Qwen 等竞争，积极布局开源权重模型生态。 模型主干共 78 层，第一层使用标准稠密 FFN，其余 77 层采用 MoE 结构，每层包含 256 个路由专家和 1 个共享专家。部署需要 vLLM 0.29.0 及以上版本，且作为预览版，正式发布前可能仍有变动。

rss · AI Hot · Aug 29, 02:27

**背景**: 混合专家（MoE）模型每个 token 只激活部分参数，因此 Hy4 总参数 770B、每 token 仅激活 49B 的设计能以更低的推理成本提供前沿级能力。OpenCode 是一个开源的命令行/终端界面编程智能体，开发者可在终端中调用多种 AI 模型，OpenCode Go 是其配套的编程服务方案。混元是腾讯的旗舰大模型系列，更大规模的多模态 Hy4 版本已被确认正在训练中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview · Hugging Face</a></li>
<li><a href="https://recipes.vllm.ai/tencent/Hy4-preview">tencent/Hy4-preview | vLLM Recipes</a></li>
<li><a href="https://www.brocker.org/tencent-hy4-preview-open-source-770b-parameters-1m-context">Tencent open-sources Hy4 preview 770 B MoE model</a></li>

</ul>
</details>

**标签**: `#Tencent Hunyuan`, `#LLM release`, `#coding agents`, `#long context`, `#AI models`

---

<a id="item-8"></a>
## [全球首例半侵入式视网膜脑机接口让失明患者重见光明](https://aihot.virxact.com/items/cmtdree3104ooro2meha7emz3) ⭐️ 8.0/10

武汉大学人民医院肖璇教授团队完成了全球首例高分辨率半侵入式视网膜脑机接口的临床应用。一位失明四年的 60 岁患者在术后开机一周内即可辨认和书写汉字、英文字母，并实现独立行走。 这是神经假体和脑机接口领域的重大里程碑，证明通过更安全、可升级的手术方式即可为盲人恢复功能性人工视觉。该成果有望惠及数百万视网膜退行性疾病患者，并推动神经接口技术的前沿发展。 刺激芯片植入在巩膜上，不穿透眼球，并采用无线传输方式，规避了眼内手术的高危并发症。设备可完整取出并更换为迭代升级版本，便于后续持续改进。

rss · AI Hot · Aug 29, 02:09

**背景**: 视网膜脑机接口是一种神经假体装置，通过电刺激尚存的视网膜细胞来绕过受损的感光细胞，从而产生视觉感知。传统的视网膜内或视网膜下植入方案需要进入眼球内部手术，存在感染、出血等并发症风险。半侵入式设计将电极阵列置于眼球外部，大幅降低手术风险，同时仍能传递有效的视觉信息。

**标签**: `#brain-computer interface`, `#BCI`, `#neuroprosthetics`, `#biotech`, `#medical breakthrough`

---

<a id="item-9"></a>
## [OpenAI 在 Cursor 被 SpaceX 收购后终止双方合作](https://aihot.virxact.com/items/cmtdqgmht0400ro2msmpjo8vg) ⭐️ 8.0/10

OpenAI 宣布在 Cursor 被 SpaceX 收购后终止与 Cursor 的合作关系，Cursor 对 OpenAI 模型的直接访问权限将于 11 月 12 日结束。OpenAI 表示将为受影响的开发者提供过渡期支持。 这是 AI 开发者工具生态的一次重大变动：年经常性收入超过 30 亿美元、最受欢迎的 AI 编程 IDE 之一 Cursor 将失去对 OpenAI 模型的直接访问权限。依赖 Cursor 中 OpenAI 模型的开发者将需要迁移或更换工具，这一决定也表明企业收购正在重新划分 AI 实验室与工具厂商之间的阵营。 OpenAI 表示与 Cursor 已合作近四年，并对该团队表示尊重，将切断访问定位为 SpaceX 收购的结果而非对产品本身的不满。11 月 12 日的截止日期为受影响的开发者提供了一个明确的迁移窗口。

rss · AI Hot · Aug 29, 01:46

**背景**: Cursor 由 Anysphere 公司开发，是基于 Visual Studio Code 分叉的 AI 辅助代码编辑器，允许开发者通过自然语言指令编写代码。到 2026 年初其估值达 293 亿美元，年经常性收入超过 30 亿美元；被收购后，它于 2026 年 8 月成为 SpaceXAI 的全资子公司。由于 Cursor 的 AI 功能依赖 OpenAI 模型作为关键后端，此次收购使 OpenAI 处于向竞争对手子公司供应模型的境地，从而促成了合作的终止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#AI-industry`, `#developer-tools`, `#SpaceX`

---

<a id="item-10"></a>
## [世界人形机器人运动会：全自主机器人打破 5 项人类纪录](https://aihot.virxact.com/items/cmtdqg9r603zaro2mbwy6iewp) ⭐️ 8.0/10

在近日闭幕的世界人形机器人运动会上，全自主人形机器人在 51 个项目中打破了 5 项人类纪录。Agibot 轮式机器人 Genie G2（约 14 万美元）与 Agilink OmniHand Ultra（约 6.1 万美元）称霸任务类项目，X-Humanoid 天工 Ultra（约 4.1 万美元）领跑田径类项目。 这是具身智能快速进步的强烈信号，表明人形机器人已能以相对较低的硬件成本全自主完成复杂物理任务。它凸显了中国在机器人与 AI 融合前沿的加速领先地位，对制造、物流和服务行业都有深远影响。 破纪录的机器人价格跨度很大，从约 4.1 万美元的天工 Ultra 到 14 万美元的 Genie G2，说明能力提升不再依赖极其昂贵的硬件。天工 Ultra 此前在 2025 年 WHRG 百米项目中跑出 21.50 秒，并以 2 小时 40 分赢得机器人半程马拉松。

rss · AI Hot · Aug 29, 01:45

**背景**: 世界人形机器人运动会是中国的一个人形机器人赛事，机器人参加田径和任务类项目。Agibot（智元机器人）是一家由前华为工程师于 2023 年创立的上海机器人公司，其 Genie G2 是工业级轮式人形机器人。X-Humanoid 是政府支持的研究机构，天工平台是面向运动的人形机器人。Agilink 的 OmniHand 是专为复杂、非结构化操作任务设计的灵巧机械手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/agibot_g2_genie">AgiBot G 2 Genie | AI Wiki</a></li>
<li><a href="https://robot-fighting-championship.com/robots/tiangong-ultra">Tiangong Ultra robot , platform and competition record — Project H</a></li>
<li><a href="https://techcrunch.com/2025/04/19/robots-run-a-half-marathon-slowly/">Robots run a half-marathon, slowly | TechCrunch</a></li>

</ul>
</details>

**标签**: `#humanoid-robots`, `#embodied-AI`, `#robotics`, `#Agibot`, `#frontier-tech`

---

<a id="item-11"></a>
## [OpenAI 因 SpaceX 收购 Cursor 将终止向其提供 AI 模型](https://www.ithome.com/0/995/874.htm) ⭐️ 8.0/10

8 月 28 日，OpenAI 宣布已正式通知 SpaceX，将终止向 Cursor 提供 OpenAI 模型的合作合同，服务停止接入日期定为 2026 年 11 月 12 日。OpenAI 表示，鉴于马斯克旗下公司（包括推特和 xAI）屡次违约，无法确保 SpaceX 会在服务条款约束内合规使用其技术。 Cursor 是最受欢迎的 AI 编程工具之一，失去 OpenAI 模型可能显著重塑 AI 开发者工具市场，迫使用户转向其他模型提供商。此举也加剧了 OpenAI 与马斯克之间的长期争斗，表明控制权变更条款和商业纠纷正成为 AI 行业的博弈武器。 OpenAI 与 Cursor 签署的定制协议中包含控制权变更条款，赋予 OpenAI 在限定期限内终止协议的权利，该条款因 SpaceX 约 600 亿美元收购 Cursor 而被触发。OpenAI 称已将终止日顺延至合规允许的最晚时间，但 Cursor 将不再获得后续新模型，包括即将推出的 Astra。

rss · IT HOME · Aug 29, 02:21

**背景**: Cursor 由 Anysphere 开发，是基于 Visual Studio Code 分叉的 AI 辅助编程编辑器，在 2026 年中被 SpaceX 收购前估值达 293 亿美元，年度经常性收入超过 30 亿美元。马斯克于 2026 年 2 月将 xAI（此前已并入推特/X）合并入 SpaceX，整合了自己的 AI 帝国。OpenAI 即将推出的新模型 Astra 是尚未发布的下一代系统，据报道已解决十个长期悬而未决的数学难题。马斯克与 OpenAI 之间存在长期的法律和商业冲突，包括马斯克起诉这家他联合创立的公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://www.nytimes.com/2026/02/02/technology/spacex-xai-deal.html">Elon Musk Merges SpaceX With His A.I. Start-Up xAI - The New York...</a></li>
<li><a href="https://gipyeong-lee.github.io/2026/08/04/OpenAIs-Unreleased-Model-Astra-Solves-Ten-Major-Open-Mathematics-Problems.en/">AI ' Astra ' Solves 10 Decade-Old Mathematical Challenges in a Single...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI industry`, `#Elon Musk`

---

<a id="item-12"></a>
## [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

2026 年 8 月 28 日，腾讯混元发布迄今最强开源模型 Hy4 preview，总参数量 770B、活跃参数 49B，上下文窗口达 1M token。在 203 个工程任务的盲测中，Hy4 preview 以 2.99 分略胜 GLM-5.3（2.92）与 Kimi K3（2.94）。 这加剧了国产开源前沿模型之间的竞争，混元如今直接挑战 GLM 与 Kimi 的第一梯队地位。该模型主攻长周期软件工程、文档办公与科学研究，并在 Hugging Face、ModelScope 等平台开放权重，为开发者提供了强有力的新选择。 Hy4 preview 采用混合专家（MoE）架构，每次推理仅激活 770B 总参数中的 49B，从而控制计算成本。API 定价为每 1M tokens 输入 0.834 美元、输出 2.501 美元，模型已上线腾讯云、GitHub、HuggingFace、ModelScope、AtomGit、OpenRouter 等渠道。

telegram · @zaihuapd · Aug 28, 06:11

**背景**: 混合专家（MoE）模型拥有很大的总参数量，但每次输入只激活一部分“专家”子网络，因此 770B 的模型可以以约 49B 稠密模型的计算成本运行。盲测评估通常由不知道输出来自哪个模型的评审（人类或 LLM-as-a-judge）打分，被认为比传统静态基准测试更公平。智谱的 GLM 与月之暗面的 Kimi 是目前国产开源模型的领先阵营，自然成为混元新模型的对比对象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7669993495223205898">MoE（ Mixture of Experts ...</a></li>
<li><a href="https://developer.aliyun.com/article/1756327">把 GLM - 5 . 3 接入到 DeepSeek Harness，夯爆了！ -阿里云开发者社区</a></li>
<li><a href="https://arxiv.org/abs/2306.05685">Judging LLM -as-a-Judge with MT- Bench and Chatbot Arena</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Tencent Hunyuan`, `#open-source models`, `#benchmark`

---

<a id="item-13"></a>
## [谷歌员工内测 Gemini 3.8 Flash，测试者称明显优于 3.7 Flash](https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8) ⭐️ 8.0/10

谷歌员工已开始内测下一代 Gemini 3.8 Flash 预览版，一名测试者称其明显优于 3.7 Flash。该预览版通过谷歌内部编码平台 Jetski 向员工开放，谷歌拒绝就此置评。 在谷歌新一代旗舰大模型一再延期的情况下，公司转而加快推出更快、更便宜的 Flash 系列，此次泄露表明这一近乎每月一更的节奏仍在延续。Flash 系列的快速迭代将直接影响依赖 Gemini API 处理高并发、成本敏感型工作负载的开发者和企业。 发布节奏极快：3.6 Flash 于今年 7 月发布，3.7 Flash 仅三周后跟进，CEO 皮查伊曾表示计划近乎每月推新。需要注意的是，这只是内部预览版的非官方泄露而非正式发布，实际能力和上线时间可能有所变化。

telegram · @zaihuapd · Aug 28, 09:38

**背景**: Gemini 是谷歌 DeepMind 开发的多模态大语言模型家族，包括能力更强的 Pro 系列和更快、更便宜的 Flash 系列（以及 Flash Lite），于 2023 年 12 月首次发布。Flash 模型基于前代版本训练——例如 Gemini 3.7 Flash 即基于 3.6 Flash——并在推理、编码、智能体工具调用、多模态、多语言和长上下文等基准上评估。通过编码平台让员工内测通常是新模型公开发布前的后期步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model ) - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-7-flash/">Gemini 3.7 Flash - Model Card — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#LLM`, `#AI models`, `#frontier AI`

---

<a id="item-14"></a>
## [Z.ai 发布 GLM-5.3-Flash：原生多模态 MoE 模型，价格仅为上代十分之一](https://t.me/zaihuapd/43471) ⭐️ 8.0/10

Z.ai 发布了 GLM-5 系列首个原生多模态模型 GLM-5.3-Flash，总参数 320B、激活参数仅 18B。该模型在多项编程和智能体基准上超过 GLM-5.2，接近 Claude Opus 4.8，限时 API 输入价格低至每百万 Tokens 0.075 美元。 此次发布将接近前沿水平的编程和智能体能力带入极低价格区间，加剧了大模型 API 提供商之间的价格战，让更多开发者能够用上强大的多模态模型。这也表明 Z.ai 正以稀疏 MoE 架构带来的效率而非单纯堆参数量作为竞争策略。 限时优惠价格为输入每百万 Tokens 0.075 美元、缓存输入 0.015 美元、输出 0.25 美元，缓存存储暂时免费，整体约为上代价格的十分之一。该模型基于全新训练的基础模型，架构和训练方案均经过重新设计，可通过 Z.ai API 和 OpenRouter 使用。

telegram · @zaihuapd · Aug 28, 15:32

**背景**: GLM-5.3-Flash 采用混合专家（MoE）架构，每个 token 仅激活总参数（320B 中的 18B）的一部分，在保留模型能力的同时大幅降低推理成本。缓存输入 token 的价格远低于普通输入，因为提供商在之前的请求中已处理过这些内容，无需重新计算注意力。Z.ai（前身为智谱 AI）是一家中国 AI 实验室，其 GLM 系列与 OpenAI、Anthropic 和 DeepSeek 的模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.3-Flash">zai-org/ GLM - 5 . 3 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.3-flash">GLM 5 . 3 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM - 5 . 3 - Flash - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**标签**: `#AI model release`, `#GLM`, `#multimodal`, `#MoE`, `#API pricing`

---