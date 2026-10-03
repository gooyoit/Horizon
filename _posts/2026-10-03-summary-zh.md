---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> From 107 items, 5 important content pieces were selected

---

1. [Google 发布前沿模型 Gemini 4 Argon](#item-1) ⭐️ 9.0/10
2. [Google Research 发布 Cogentic：用于自动证明发现的多智能体系统](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布 GPT-6.1 Sol，价格仅为 Astra 的五分之一](#item-3) ⭐️ 9.0/10
4. [新 AI 系统 Ataraxos 击败史上最优秀的 Stratego 玩家](#item-4) ⭐️ 8.0/10
5. [OpenAI 发布 GPT-6 选型指南：Astra、Sol、Luna 三档模型](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google 发布前沿模型 Gemini 4 Argon](https://t.me/zaihuapd/44165) ⭐️ 9.0/10

Google 于 2026 年 9 月 30 日发布前沿模型 Gemini 4 Argon，面向实际软件工程、企业知识工作和网络防御场景。该模型支持最多 100 万输出 token（上一代为 6.4 万），定价为每百万输入 token 2 美元、输出 token 10 美元。 Argon 是 Alphabet 迄今最先进的模型，标志着 Google 大力推进面向长周期软件工程和网络安全的智能体 AI，其自主发现和修复漏洞的能力可能重塑开发者工作流与网络防御格局。通过 Fairwind 计划分阶段开放，也凸显了业界对具备强大网络攻防能力的模型被滥用的日益担忧。 Google 称 Argon 可自主发现、验证并修复关键软件漏洞。访问权限初期仅限于 Fairwind 计划中受信任的网络防御者，待扩大测试并完善安全措施后，才会向付费 API 客户和 Google AI Ultra 订阅用户开放。

telegram · @zaihuapd · Oct 2, 04:59

**背景**: 前沿模型（frontier model）指某一时期能力最强的通用 AI 系统，通常是大实验室的最新旗舰模型。Google 于 2026 年 9 月初启动的 Fairwind 计划，向经过审批的政府机构、Google Cloud 客户和网络安全合作伙伴提前提供前沿 AI 与网络防御能力（如 Gemini 3.8 Flash Cyber 模型和漏洞修复智能体 CodeMender），优先面向关键基础设施运营方和开源维护者。Argon 的 100 万 token 输出上限大幅扩展了 AI 智能体单次运行可完成的任务规模，例如整个代码库的重写或长篇报告的生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-4-argon">Gemini 4 Argon: Benchmarks, Pricing, and Access | DataCamp</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/">Google’s Fairwind Program: Cyber defense tools for trusted ...</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#frontier-model`, `#AI-agents`, `#cybersecurity`

---

<a id="item-2"></a>
## [Google Research 发布 Cogentic：用于自动证明发现的多智能体系统](https://arxiv.org/abs/2609.40324v1) ⭐️ 9.0/10

Google Research 发表了 Cogentic，一个基于 Gemini 的多智能体系统，用于在开放研究问题上自动发现证明。该系统通过迭代的“证明—验证”循环，让多个独立证明器探索不同方向并进行对抗式验证，在在线学习、拍卖理论和机制设计领域的五个开放问题上产出了新结果，均由领域专家独立验证。 这表明由大模型协调的多智能体系统（而非单次生成）能够对开放的数学问题做出真正的研究级贡献，是 AI 辅助科学发现的重要里程碑。它标志着大模型从助手角色向自主研究型智能体系统的转变。 Cogentic 将已确认的结果存入可持续使用的验证账本，从而在长时间探索中保留并复用中间进展。其设计动机在于单次生成不足以解决需要探索多个竞争性猜想、克服微妙技术障碍的开放问题；新结果在配套论文中有详细展开。

telegram · @zaihuapd · Oct 2, 12:04

**背景**: 自动定理证明（ATP）传统上依赖 Lean 等形式化系统和形式化验证器逐步检查证明；近期研究将大模型与“验证器在环”反馈结合以提升性能。Cogentic 将这一思路扩展到猜想本身也可能需要修正的开放研究问题。机制设计与拍卖理论是经济学和算法博弈论的分支，研究如何设计规则（机制）使自利的参与者表现出期望的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.40324">[2609.40324] Cogentic: Multi-Agent Orchestration for ...</a></li>
<li><a href="https://agentic-design.ai/news-hub/cogentic-multi-agent-orchestration-automated-proof-discovery-b84add">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>

</ul>
</details>

**标签**: `#AI research`, `#multi-agent systems`, `#automated theorem proving`, `#Gemini`, `#Google Research`

---

<a id="item-3"></a>
## [OpenAI 发布 GPT-6.1 Sol，价格仅为 Astra 的五分之一](https://t.me/zaihuapd/44177) ⭐️ 9.0/10

OpenAI 推出了 GPT-6 Sol 的升级版 GPT-6.1 Sol，该模型在智能体编程、计算机操作和专业任务上的表现接近旗舰模型 GPT-6 Astra，而输入输出价格仅为 Astra 标准价的五分之一，缓存输入价格为每百万 token 0.10 美元。该模型已向 Plus、Pro、Business、Enterprise 和 Edu 用户在 ChatGPT Work 与 Codex 中开放（暂未进入 Chat），开发者也可通过 API 调用。 此举大幅降低了大规模运行 AI 智能体的成本，因为智能体工作流在多步骤工具调用和长上下文中会消耗大量 token。这也加剧了前沿模型厂商之间的价格竞争，可能促使高并发的编程和自动化工作负载从旗舰模型转向更便宜的准旗舰替代方案。 GPT-6.1 Sol 被定位为 GPT-6 Sol 系列中的高效推理模型，专为软件工程、知识工作、文档理解和智能体辅助工作流设计，具有高效的推理服务配置。该模型还通过 Amazon Bedrock 和 Microsoft Foundry 等第三方云平台提供。

telegram · @zaihuapd · Oct 2, 16:21

**背景**: OpenAI 的 GPT-6 Astra 是其旗舰模型，在计算机操作、编程和数学基准测试中名列前茅，但 API 定价高昂。"Sol" 系列是成本高效的推理模型家族，以少量能力损失换取大幅降低的成本，适合运行 token 消耗量大的智能体管线的开发者。提示缓存（prompt caching）可以让重复的提示部分以极低价格计费，这对在多步骤中反复发送长指令和代码库的智能体尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT-6.1 Sol | OpenAI</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html">GPT-6.1 Sol - Amazon Bedrock</a></li>
<li><a href="https://ai.azure.com/catalog/models/gpt-6.1-sol">gpt-6.1-sol | Model Catalog | Microsoft Foundry</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6.1`, `#frontier-models`, `#AI-agents`, `#API-pricing`

---

<a id="item-4"></a>
## [新 AI 系统 Ataraxos 击败史上最优秀的 Stratego 玩家](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

发表在《Nature》上的新 AI 系统 Ataraxos 击败了史上最优秀的 Stratego 玩家，攻克了长期困扰 AI 的不完全信息博弈难题。它比 DeepMind 在 2022 年推出的 DeepNash 训练效率高得多，训练对局数量约少 34 倍，棋力却强得多。 Stratego 同时具有隐藏信息、巨大的博弈树和长期虚张声势等特点，是 AI 领域的重大挑战，国际象棋和围棋式的搜索方法无法直接应对。这一以低成本实现的突破展示了在隐藏信息下进行自我博弈强化学习和测试时搜索的通用技术，其意义可能超出游戏领域。 Ataraxos 基于为不完全信息博弈下的自我博弈强化学习和测试时搜索而开发的通用技术，而非针对特定游戏的手工建模。在不完全信息博弈中，一步棋的好坏取决于未知的对手棋子，因此相比 DeepNash 减少 34 倍对局的样本效率提升被认为是该成果的关键。

hackernews · PaulHoule · Oct 2, 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: Stratego 是一款经典的双人棋盘游戏，双方各自以隐藏阵型布置 40 枚棋子，目标是夺取对方的军旗；由于棋子身份保密，它属于不完全信息博弈。与国际象棋或围棋不同，玩家无法直接向前搜索，因为不知道对手的布局，这使传统 AI 方法数十年来难以应付。DeepMind 于 2022 年推出的 DeepNash 结合了博弈论与无模型深度强化学习，达到了专家水平，但未能真正击败顶尖人类玩家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11036-y">Scalable decision-making for games of imperfect information</a></li>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego , the classic game of imperfect information</a></li>
<li><a href="https://arxiv.org/abs/2206.15378">[2206.15378] Mastering the Game of Stratego with Model-Free...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 Stratego 的怀旧之情，但惊讶于这个看似简单的游戏竟然对 AI 如此困难。有评论者强调 34 倍的样本效率提升是关键，因为隐藏信息使得直接的前瞻搜索无法进行。还有人指出，2022 年 DeepNash 所谓的“掌握”Stratego 如今看来名不副实，新系统才真正超越了人类水平。

**标签**: `#AI research`, `#game AI`, `#hidden information games`, `#reinforcement learning`, `#breakthrough`

---

<a id="item-5"></a>
## [OpenAI 发布 GPT-6 选型指南：Astra、Sol、Luna 三档模型](https://aihot.news/items/xm8y5t0llcnk9iv6b4gmk89x6) ⭐️ 8.0/10

OpenAI 发布了 GPT-6 系列选型指南，按任务将模型分为三档：Astra 面向最难的推理任务，Sol 面向复杂编码、研究与电脑操作，Luna 面向目标明确的重复执行任务。指南建议从成功率、延迟和每次成功任务成本三个维度综合评估，并指出提示词缓存的输入价格最高可比非缓存便宜 95%。 随着前沿模型分化为面向不同任务的专用版本，为每个任务选择合适的模型已成为工程团队控制成本和质量的关键手段。以“每次成功任务成本”为核心的选型建议，反映出行业重心正从基准测试分数转向生产环境中智能体的实际单位经济性。 缓存折扣只作用于输入侧计费，因此实际节省幅度很大程度上取决于任务的输入密集程度。“每次成功任务成本”这一指标很重要，因为失败或升级人工处理的运行同样消耗 token，单纯的每次运行成本会掩盖这一点。

rss · AI Hot · Oct 3, 01:02

**背景**: 现代大模型供应商越来越多地提供不同能力与价位的模型版本，应用可以将简单任务路由到便宜的模型、把困难任务交给昂贵模型。提示词缓存是一种定价机制：重复或共享的输入前缀可以大幅折扣计费（通常便宜 80%–90%），因为供应商可以复用已计算的结果。本条新闻来自 BestBlogs/AIHOT 的二次摘要而非 OpenAI 官方原始公告，具体细节建议以原文为准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thetokenmart.com/blog/llm-discount-stacking-cache-route-bulk">Discount Stacking on LLM APIs: Cache + Route + Bulk Math</a></li>
<li><a href="https://callsphere.ai/blog/how-to-measure-if-your-ai-agent-is-actually-working">How to Measure If Your AI Agent Is Actually Working | CallSphere Blog</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#model-selection`, `#prompt-caching`, `#AI-agents`

---