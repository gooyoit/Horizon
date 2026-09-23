---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> From 120 items, 16 important content pieces were selected

---

1. [OpenAI 发布 GPT-6 Sol 和 Luna，Luna 价格减半](#item-1) ⭐️ 10.0/10
2. [Anthropic 发布 Claude Opus 5.5：降价并提升能力](#item-2) ⭐️ 10.0/10
3. [Claude Opus 5.5 与 GPT-6 Sol/Luna 引发新一轮前沿模型价格战](#item-3) ⭐️ 10.0/10
4. [OpenAI 发布 GPT-6 Sol 与 Luna，API 价格降低 50%](#item-4) ⭐️ 10.0/10
5. [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](#item-5) ⭐️ 10.0/10
6. [Claude Opus 5.5（Max 推理模式）基准测试引发价格与价值争论](#item-6) ⭐️ 9.0/10
7. [Claude Opus 5.5 发布：成本降低 40%，速度提升 30%](#item-7) ⭐️ 9.0/10
8. [阿里平头哥发布真武 V900，号称最强国产 AI 芯片](#item-8) ⭐️ 9.0/10
9. [vLLM v0.30.0 发布：支持 DeepSeek-V4.1-Flash、GLM-5.3-Flash 及 Fast Start 权重缓存](#item-9) ⭐️ 8.0/10
10. [GPT-6 Astra 破解自 2005 年以来悬而未决的恩尼格玛密电](#item-10) ⭐️ 8.0/10
11. [KVMEM：通过分页旧 KV 状态实现实用的百万 token 级智能体记忆](#item-11) ⭐️ 8.0/10
12. [Qwen-Image-2.1 登顶 Arena 图像编辑与文生图开源榜第一](#item-12) ⭐️ 8.0/10
13. [Claude Opus 5.5 发布成本降 40%；小米开源 MiMo-V2.6 强化学习框架](#item-13) ⭐️ 8.0/10
14. [DeepSeek 与清华联合发布 DSec 沙箱平台技术报告](#item-14) ⭐️ 8.0/10
15. [中国监管机构调查 DeepSeek 与月之暗面涉嫌数据泄露](#item-15) ⭐️ 8.0/10
16. [DeepSeek 本周将向联合国安理会通报 AI 风险](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 和 Luna，Luna 价格减半](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 10.0/10

OpenAI 发布了最新的前沿模型 GPT-6 Sol 和 Luna，其中 GPT-6 Sol 定价为每百万 token 输入 2 美元/输出 10 美元，Luna 为输入 0.10 美元/输出 0.50 美元，仅为 GPT-5.6 Luna 价格的一半。此次发布紧随 GPT-6 Astra 之后，引发了社区对新旧模型的大量对比测试。 前沿模型价格减半将大幅降低生产级 AI 应用的成本，可能重塑智能体（agent）和高吞吐量应用的经济模型。这也加剧了与 Anthropic 的 Claude Code 等竞品的竞争，推动整个市场走向更便宜、更快的智能服务。 GPT-6 Sol 提供多个档位：GPT-6 Sol (max) 在 Artificial Analysis 智能评测中得分 48，Sol (low) 输出速度达 129 t/s，非推理版本首 token 延迟仅 0.93 秒。Luna 并非统一定价，而是随请求的上下文长度变化，宣传的 0.10/0.50 美元为标准区间价格。

hackernews · OfficialTurkey · Sep 22, 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 近期密集发布 GPT-6 系列模型：GPT-6 Astra 于 2026 年 9 月初发布，定位为对齐程度最高、面向企业的模型；而 GPT-5.6 Sol 在此次发布前一天刚刚预览，强项在于编程、科学和网络安全。命名体系中，Sol 面向复杂编程和智能体工作流，Luna 则是更便宜、更快的档位。API 的每百万 token 输入/输出定价是开发者构建 AI 应用的主要成本，因此价格减半直接影响成本底线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalapplied.com/blog/gpt-6-sol-luna-launch-pricing-benchmarks-2026">GPT - 6 Sol and Luna : API Prices , Benchmarks and Trade-offs</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6-sol">GPT-6 Sol Model | OpenAI API</a></li>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-sol">GPT-6 Sol Models - Intelligence, Performance & Price Comparison | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 讨论整体积极：Simon Willison 立即用他标志性的 SVG '鹈鹕'绘图测试对比了 GPT-6 Luna、Sol 和 Astra 的输出。用户在比较 Codex Pro 与 Claude Code 套餐的用量限制，jeffnash 认为 Codex 因 ChatGPT 用量几乎不计费而大幅胜出。m_fayer 表达了对 GPT-5.6 Sol 沟通风格的喜爱，担心技术上更强的新模型用起来反而不如它自然；leokennis 则表示自 5.6 以来 ChatGPT Plus 几乎没有限制且'开箱即用'。

**标签**: `#OpenAI`, `#GPT-6`, `#frontier-models`, `#LLM-release`, `#AI`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5：降价并提升能力](https://www.anthropic.com/claude-opus-5-5) ⭐️ 10.0/10

Anthropic 发布了前沿模型升级版 Claude Opus 5.5，其特点是价格下调、编码和 3D 生成能力提升，以及更自然的沟通风格。每百万 token 的输入价格从 5 美元降至 4 美元，输出从 25 美元降至 20 美元，缓存读取从 0.50 美元降至 0.20 美元。 这是 Anthropic CEO Dario Amodei 一周前呼吁“控制前沿节奏”后的首次重大发布，而发布本身就展示了显著的能力提升，引发了关于安全言论与竞争压力之间张力的讨论。降价也影响整个市场，因为据报道 Opus 5 在 OpenRouter 上的消费额最高，可能是全球消费额最高的模型。 早期测试者发现 Opus 5.5 的写作更清晰易懂，回应了对 Opus 5 的常见批评，并将重要信息前置——Anthropic 称这既有实用性，也便于核查模型输出，是一种安全收益。社区测试（例如将动画鹈鹕的 SIML 转换为 3D）显示其相比 Opus 5 有显著改进。

hackernews · @zaihuapd · Sep 22, 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: “前沿模型”指处于通用能力最前沿的 AI 模型，通常是主要实验室的最新旗舰产品。2026 年 9 月 12 日，Anthropic CEO Dario Amodei 发表《我们必须控制前沿节奏》，主张“我们必须放慢提升 AI 模型能力的速度”，该计划迅速获得 OpenAI、xAI 和微软的支持。Claude Opus 5.5 是该声明发布后的首个旗舰模型，因此成为检验行业能否真正放慢能力进步的试金石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/">Anthropic CEO outlines plan to slow AI development | TechCrunch</a></li>
<li><a href="https://www.marktechpost.com/2026/09/13/anthropics-3-step-pace-the-frontier-plan-wins-openai-xai-and-microsoft-support-is-it-too-late-to-slow-ai-down/">Anthropic's 3-Step 'Pace the Frontier' Plan Wins OpenAI, xAI and Microsoft Support: Is It Too Late to Slow AI Down? - MarkTechPost</a></li>
<li><a href="https://www.levellers.ai/what-is/frontier-model">What is a frontier model ? Clear business guide | Levellers. ai</a></li>

</ul>
</details>

**社区讨论**: 热门评论讽刺地指出，公告开头提醒读者“控制前沿节奏”的呼吁，随后却用具体数字表明他们完全没有放慢。用户对降价表示欢迎，并通过并排的 3D 生成对比测试证明了实际能力提升；也有用户表示更喜欢 DeepSeek v4.1 作为更便宜的选择。

**标签**: `#anthropic`, `#claude`, `#frontier-model`, `#llm-release`, `#ai`

---

<a id="item-3"></a>
## [Claude Opus 5.5 与 GPT-6 Sol/Luna 引发新一轮前沿模型价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 10.0/10

Anthropic 发布了 Claude Opus 5.5，OpenAI 在约一小时后发布了 GPT-6 Sol 和 GPT-6 Luna，而此前一天 xAI 发布了 Grok 4.7，小米发布了 MiMo v2.6。Simon Willison 指出，GPT-6 系列定价仅为 GPT-5.6 对应版本的一半，其中 GPT-6 Luna 输入价格仅每百万 token 0.10 美元，输出 0.50 美元。 在保持或提升性能的同时降价 50%，标志着前沿模型提供商之间的价格战正在加剧，这将大幅降低 AI 应用开发者的成本。Grok 4.7 激进的 $2/$6 定价如今在输入端已被 GPT-6 Sol 追平，竞争压力加剧，并加速了今年以来 API 价格持续走低的趋势。 Claude Opus 5.5 在高强度模式下匹配了 Opus 5 的表现，同时输出 token 减少约 20-25%，价格也降至输入每百万 4 美元、输出 20 美元。GPT-5.6 计划在 11 月涨价 25%，这意味着 GPT-6 实际上连 GPT-5.6 的促销价的一半都不到；由于 GPT-5.6 Terra 与 GPT-6 Sol 定价相同，Willison 认为 Terra 已没有存在的理由。

rss · Simon Willison · Sep 22, 23:46

**背景**: OpenAI、Anthropic、xAI 乃至小米等前沿模型提供商，不仅在基准性能上竞争，也在按每百万 token（分输入与输出计费）的 API 定价上竞争。整个 2026 年，前沿 API 价格持续下行，使 GPT-5.6 Luna 这类便宜又能干的模型成为应用开发者的最爱。Willison 常用“画鹈鹕”测试作为快速比较新模型输出质量的定性方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://www.beri.net/tools/xiaomi-mimo-v2-6">Xiaomi MiMo-V2.6 — Overview, Features & Use Cases | THE D*AI*LY BRIEF</a></li>
<li><a href="https://www.toolmintx.in/blog/ai-api-price-war-gpt-5-6-claude-deepseek-2026">The AI API Price War : GPT-5.6, Claude Opus 5 and... | ToolMintX</a></li>

</ul>
</details>

**社区讨论**: Grok 4.7 和 MiMo v2.6 在 Hacker News 上的讨论围绕 Willison 的“画鹈鹕”测试展开，该测试已成为流行的快速基准。评论者借助这些讨论分享对新模型编程和推理能力的早期上手体验。

**标签**: `#frontier-models`, `#claude-opus`, `#gpt-6`, `#llm-pricing`, `#model-releases`

---

<a id="item-4"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，API 价格降低 50%](https://aihot.news/items/cmudd3ig3068uroggif72kglr) ⭐️ 10.0/10

OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna 两款新模型，API 价格下调 50%，同时将 GPT-6 Astra 在编码、计算机使用、事实性和对齐方面的性能带入更快速、更经济的模型层级。这两款模型已在 GitHub Copilot 的 Pro、Pro+、Max、Business 和 Enterprise 套餐中上线。 在保持旗舰级性能的同时降价 50%，大幅降低了构建 AI 应用的成本，加剧了与 Anthropic 和 Google 等对手的价格竞争。这也表明推理效率的提升正在惠及客户，将加速智能体（agent）工作流的普及。 Luna 针对快速响应和高吞吐量场景优化，而 Sol 具备更强的推理能力；OpenAI 称 GPT-6 Sol 的错误数量约为 GPT-5.6 Sol 的一半。缓存和推理基础设施的改进是实现更低服务成本的关键。

rss · AI Hot · Sep 22, 23:53

**背景**: OpenAI 的 GPT-6 系列是其前沿模型产品线，Astra 为最高层级，而 Sol 和 Luna 将这种能力沿"成本—智能曲线"向下延伸。"计算机使用"指能够自主操作图形界面（按钮、菜单、文本框）来完成任务的智能体，OpenAI 于 2025 年初通过 Operator 背后的 Computer-Using Agent（CUA）率先推出该能力。当前 AI 行业同时在基准性能和每 token 价格上展开竞争，因为开发者正转向消耗大量推理资源的智能体应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT-6 Sol and Luna | OpenAI</a></li>
<li><a href="https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available/">OpenAI's GPT-6 Sol and GPT-6 Luna now available - GitHub Changelog</a></li>
<li><a href="https://www.macrumors.com/2026/09/22/openai-gpt-6-sol-luna/">OpenAI's New GPT-6 Sol and Luna Models Bring Astra Improvements to Cheaper Tiers - MacRumors</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#AI models`, `#API pricing`, `#frontier AI`

---

<a id="item-5"></a>
## [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](https://t.me/zaihuapd/43990) ⭐️ 10.0/10

OpenAI 开始对 GPT-5.6 模型系列进行有限预览，包括旗舰模型 Sol、均衡型 Terra 和低成本 Luna，首先通过 API 和 Codex 向少数可信伙伴开放。Sol 新增了 max 推理强度和利用子智能体的 ultra 模式，Terra 号称性能接近 GPT-5.5 且成本减半，Luna 则定位为最低成本选项。 这是 OpenAI 最新的前沿模型发布，按工作负载拆分为三档的策略表明其正从单一巨型模型转向面向编码、推理和低成本场景的组合式产品线。据报道本次分阶段发布是应美国政府要求进行的，这也凸显了前沿 AI 发布与政府监管之间日益紧密的交集。 据报道，Sol 的 ultra 模式超越了单智能体能力，通过生成子智能体来分解并加速复杂任务，max 推理强度则让模型有更多时间进行深度思考。目前仅限可信伙伴通过 API 和 Codex 使用，计划在未来几周内扩展到 ChatGPT 和更广泛的 Codex 用户。

telegram · @zaihuapd · Sep 22, 18:04

**背景**: GPT-5.6 延续了 OpenAI 的旗舰大模型产品线，但将家族拆分为针对不同工作负载优化的三个版本：追求最强能力的 Sol、平衡性能与成本的 Terra，以及主打速度与低价的 Luna。Codex 是 OpenAI 的 AI 编程智能体，可通过 ChatGPT 网页版、CLI、桌面应用和 IDE 插件使用，是面向编码场景模型的天然首发渠道。推理强度控制（如 low/medium/high 以及新的 max）允许开发者用延迟和成本换取更深的思维链推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://bota.chat/chat-gpt-5-6/openai-luna-model/">OpenAI Luna Model : $1/M, 84.7% Terminal-Bench & 1M+ Context</a></li>
<li><a href="https://blog.wentuo.ai/en/gpt-5-6-sol-ultra-mode-multi-agent-guide-en.html">Analysis of GPT-5.6 Sol Ultra Mode: The Multi-Agent Collaboration Technology Behind the 91.9% Benchmark Score – WentuoAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#frontier-models`, `#LLM-release`, `#AI-infrastructure`

---

<a id="item-6"></a>
## [Claude Opus 5.5（Max 推理模式）基准测试引发价格与价值争论](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，Hacker News 正在讨论其在 Artificial Analysis 上 'max' 推理档位的基准测试页面，该模型智能水平位居前列，拥有 100 万 token 上下文窗口。值得注意的是，在高档位对高档位的比较下，其每任务成本约为 Opus 5 的一半。 这次发布体现了前沿模型的竞争格局：智能提升有限，但每任务成本效率显著改善，直接影响开发者的 API 预算和模型选择。它还加剧了关于闭源前沿模型相对日益强大的开放权重模型是否物有所值的争论。 该模型提供多个推理档位（默认 medium，另有 xhigh 和 max），各有独立的基准测试页面，max 档位可能在给出答案前就耗尽 128,000 token 的输出预算。Artificial Analysis 强调'每任务成本'而非每百万 token 价格，因为 token 单价本身无法反映任务实际消耗的 token 数量。

hackernews · theanonymousone · Sep 22, 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: Artificial Analysis 是一家独立基准测试服务机构，从智能、速度、延迟和价格等维度为 AI 模型打分，并汇总为智能指数等指标。Claude Opus 5.5 采用自适应推理，可配置推理档位，用更多 token（和成本）换取复杂任务上更深入的思考。'每任务成本'已成为比按 token 计价更实用的定价指标，因为智能略高的模型完成同一任务所需的 token 数量可能相差悬殊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5.5 ( max with fallback) - Intelligence... | Artificial Analysis</a></li>
<li><a href="https://usagebox.com/articles/cost-per-intelligence-index-task-explained-2026">Cost Per Task , Explained: How the Metric Is Built and... | UsageBox</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区观点分歧：有人欢迎每任务成本较 Opus 5 减半，也有人认为前沿模型仅比开放权重模型略强却贵约 100 倍，预言'够用就好'的开放模型终将胜出。评论者还担心发布后性能回退（'撤回承诺'）问题，以及 max 档位在推理中途耗尽 128k token 预算等实际故障；一位用户甚至因指令遵循能力更强而更偏爱旧版 Opus 4.8。

**标签**: `#Claude`, `#Anthropic`, `#LLM benchmarks`, `#frontier models`, `#AI pricing`

---

<a id="item-7"></a>
## [Claude Opus 5.5 发布：成本降低 40%，速度提升 30%](https://aihot.news/items/cmuddlkm206pjroggtcf5sepp) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，典型任务运行成本较 Opus 5 低 40%，缓存读取价格下降 60%，输出速度提升超 30%。本期 BestBlogs 早报还涵盖了小米 MiMo-V2 扩展强化学习以及美团统一推荐基座大模型 MTFM 等内容。 一次在成本和速度上有显著改进的前沿模型发布，直接影响所有基于 Claude 构建智能体编程或知识工作应用的企业，降低了长时间运行智能体任务的门槛。同期关于强化学习扩展和工业推荐基座大模型的报道，表明前沿 AI 正在多条战线上同时推进。 Anthropic 将 Opus 5.5 定位为在智能体编程和知识工作方面领先的模型，40% 的成本降低是基于典型工作负载测量的。本期早报还重点介绍了美团在 MTGR 基础上提出的多场景统一推荐基座大模型 MTFM，以及小米 MiMo-V2 关于通过扩展强化学习算力实现自我改进的研究。

rss · AI Hot · Sep 23, 00:29

**背景**: Claude 是 Anthropic 的大语言模型系列，按 Haiku、Sonnet、Opus 三个规模发布，其中 Opus 能力最强。随着 AI 智能体需要运行大量长时间的模型调用，推理成本和输出延迟在实际部署中已与模型能力本身同等重要。强化学习已成为推动基础模型自我改进的核心训练范式，小米的 MiMo 系列即体现了这一方向。与此同时，美团等大型互联网公司正将基座大模型思路引入推荐系统，训练一个统一基座模型服务多个业务场景，而非维护各自独立的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>
<li><a href="https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html">MTFM...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2609.mimo-scaling-reinforcement-learning">MiMo - V 2 .6: Scaling Reinforcement Learning Towards... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#claude`, `#llm-release`, `#frontier-ai`, `#reinforcement-learning`

---

<a id="item-8"></a>
## [阿里平头哥发布真武 V900，号称最强国产 AI 芯片](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 9.0/10

9 月 22 日，在 2026 杭州云栖大会上，阿里平头哥发布新一代训推一体 AI 芯片真武 V900，算力达上一代真武 M890 的 3 倍，单一集群可扩展至 50 万卡规模。CEO 吴泳铭还透露，M890 超节点已具备支撑 2 万亿参数大模型推理的能力，本季度将在阿里云规模化上架。 在美国限制英伟达高端芯片出口的背景下，V900 使阿里成为国产 AI 算力芯片的头部竞争者，并直接支撑其训练 5 至 10 万亿参数 Qwen 新模型的计划。这表明中国正转向以自研芯片构建前沿级别的 AI 基础设施。 真武 V900 为训推一体芯片，号称目前算力性能最强的中国自研 AI 芯片，可满足万亿级参数大模型的训练和推理需求。阿里还提出到 2032 年全球数据中心规模超 20GW 的目标；据 IDC 数据，2025 年平头哥以 26.5 万片出货量位居国产 AI 加速芯片市场第二，仅次于华为昇腾。

telegram · @zaihuapd · Sep 22, 03:30

**背景**: 平头哥是阿里巴巴旗下的半导体公司，其真武系列 AI 加速芯片（PPU）为阿里云的 AI 训练和推理提供算力。"超节点"是一种将大量芯片高速互联、组成单一大型算力单元的架构，国内厂商普遍以此弥补单芯片算力与英伟达的差距。云栖大会是阿里云每年在杭州举办的旗舰大会，通常用于发布重要产品与战略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1079601164_121019331">平头哥半导体发布AI芯片真武V900，号称目前算力性能最强中国自研AI芯...</a></li>
<li><a href="https://www.aitop100.cn/infomation/details/34752.html">2026年云栖大会阿里平头哥发布AI芯片真武V900，算力达M890三倍-AITOP1...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2040455907130226258">性能翻 3 倍！平头哥最新一代PPU芯片真武 M890 重磅发布</a></li>

</ul>
</details>

**标签**: `#AI芯片`, `#阿里云`, `#Qwen`, `#AI基础设施`, `#平头哥`

---

<a id="item-9"></a>
## [vLLM v0.30.0 发布：支持 DeepSeek-V4.1-Flash、GLM-5.3-Flash 及 Fast Start 权重缓存](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM v0.30.0 包含来自 315 位贡献者（其中 104 位为新贡献者）的 762 个提交，新增了对 DeepSeek-V4.1-Flash（通过 SM100 上的 FlashMLA V4.1 实现全量 MXFP8 KV 缓存）、GLM-5.3-Flash（支持 EPLB）、K2-Horizon 以及 DeepSeek-V4 CPU 后端等前沿模型的支持。同时引入了 Fast Start 持久化 GPU 权重缓存守护进程，使引擎重启时可通过 `--load-format ipc_cache` 用 CUDA IPC 直接映射已量化和 TP 切分的权重，无需从磁盘重新加载，并已支持 FP4 检查点和多节点 TP。 vLLM 是使用最广泛的开源大模型推理引擎之一，对 DeepSeek-V4.1-Flash 等前沿模型的即时支持，直接决定了业界在生产环境中部署这些模型的速度。Fast Start IPC 缓存大幅缩短引擎重启时间，对推理集群的自动扩缩容和模型快速上线都具有重要意义。 值得注意的技术亮点包括：使用带密钥 PRF、支持按请求退出的 Gumbel-max 水印生成（通过双密钥方案与投机解码兼容）、面向稀疏 MLA 解码的 HiSparse 主机端 KV 溢出机制，以及 Elastic EP 复用 CUDA 图、DeepEP v2 异步 finalize 等大规模服务改进。性能方面，图捕获期间冻结 GC 将 H200 上的捕获时间从 12 秒降至 2 秒、引擎初始化从 28.9 秒降至 8.2 秒，Kimi K3 的多个内核提速 12-81%，Qwen3.8-Flash-Next 移除 torch.compile 后 FP8 可在单张 GB300 上运行。

github · vllm-project/vllm · Sep 22, 05:20

**背景**: vLLM 是一个开源的高吞吐大模型服务引擎，以 PagedAttention 技术和广泛的模型支持著称，与 TensorRT-LLM、SGLang 相互竞争。FlashMLA 是 DeepSeek 的优化注意力内核库，支撑其稀疏注意力模型；MXFP8/FP8 KV 缓存量化可降低长上下文推理的显存占用。EPLB（专家并行负载均衡器）用于解决混合专家（MoE）模型在专家并行部署中各 rank 负载不均的问题。从磁盘加载数百 GB 权重导致的冷启动时间一直是服务集群的主要运维瓶颈，持久化 GPU 权重缓存守护进程正是针对这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/">weight _ cache - vLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/">Expert Parallel Deployment - vLLM</a></li>

</ul>
</details>

**标签**: `#vllm`, `#AI inference`, `#DeepSeek`, `#LLM serving`, `#open-source`

---

<a id="item-10"></a>
## [GPT-6 Astra 破解自 2005 年以来悬而未决的恩尼格玛密电](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

据报道，OpenAI 的 GPT-6 Astra 破解了一条自 2005 年以来一直未被解开的二战恩尼格玛密电，并在过程中自行编写了 Python 和 C++ 恩尼格玛模拟器软件。一位评论者还证实，Gemini 3.8 Flash 在一次无人工干预的运行中约 45 分钟内独立完成了同样的解密。 这一结果是智能体推理能力的一次重要展示：前沿模型能够自主规划、编写代码并执行基于工具的密码分析，解决了一个困扰人类密码学家和分布式计算项目二十年的难题。这表明前沿大模型已能处理开放式的长期研究问题，而不仅是基准测试类任务，尽管其自主程度仍存争议。 这条密电之所以长期未被破解，是因为它使用了与当天其他通信完全不同的密钥，原始转录存在错误，且左侧转子在第 72 个字母处发生翻转——这种罕见情况会破坏标准的线索攻击法。据报道，解密来自一位研究者与 Astra 为期两天的协作，明文（含拼写错误）大意是从 Rosenow 请求告知行军路线，署名 Waschbusch。

hackernews · sohkamyung · Sep 22, 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: 恩尼格玛机是二战期间纳粹德国广泛用于加密军事通信的转子式密码设备；艾伦·图灵和盟军密码分析人员曾著名地破解了它，但许多被截获的密电至今仍未解密。诸如 Stefan Krah 的 M4 项目和 Enigma@Home 等分布式计算项目多年来一直利用爬山密码分析技术破解此前未解决的德国海军恩尼格玛密电。智能体推理指的是大语言模型作为自主智能体，通过规划、编写和执行代码、迭代使用工具来解决复杂问题，而非仅给出一次性的文本回答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enigma_machine">Enigma machine - Wikipedia</a></li>
<li><a href="https://enigma.hoerenberg.com/">ENIGMA M4 - Breaking German Navy Ciphers</a></li>
<li><a href="https://boincsynergy.ca/wiki/Enigma@Home">Enigma@Home - boincsynergy.ca</a></li>

</ul>
</details>

**社区讨论**: 评论者们对此印象深刻，但淡化了对自主性的说法：有人指出“完全靠自己完成”与模型把工作交给自行生成的软件这一事实相矛盾，并质疑这些代码有多少是原创的、有多少来自网络。另有人认为更准确的说法是“研究者在 Astra 的有力协助下破解了密电”，强调这是为期两天的人机协作，还有评论者确认了明文内容以及 Gemini 模型复现了这一解密。

**标签**: `#AI`, `#LLM`, `#Enigma`, `#cryptography`, `#agentic-reasoning`

---

<a id="item-11"></a>
## [KVMEM：通过分页旧 KV 状态实现实用的百万 token 级智能体记忆](https://aihot.news/items/cmudfro04092jrogg94xcq2u3) ⭐️ 8.0/10

KVMEM 提出将旧的键值（KV）缓存状态从显存中分页换出，使编码智能体无需重算或有损压缩即可维持百万 token 级的上下文历史。在 DeepSWE 基准上配合 Qwen3.8-27B，它将 Pass@1 从 43.8% 提升至 48.4%，且上下文恢复速度比 Compact+RAG 基线快 11.4-53.8 倍。 长时程智能体（如编码助手）的 KV 缓存随上下文长度线性增长，很快耗尽显存，只能依赖会丢失信息的压缩或 RAG 方案。KVMEM 表明将 KV 状态视为可分页内存，可以在有限显存内保留完整的注意力精度，从而直接提升智能体在真实软件工程任务上的表现。 关键的技术贡献是将 KV 页的物理放置与传输和重建的粒度解耦，并通过打包式重物化（packed rematerialization）将选中的块批量合并为连续传输。社区还有一个基于 llama.cpp 分支的可复现 16GB 显存本地智能体方案，展示在消费级硬件上将 KV 缓存放入系统内存运行 KVMem。

rss · AI Hot · Sep 23, 01:36

**背景**: KV 缓存保存自注意力中的键值张量，使新 token 无需对全部历史重算注意力，但其显存占用随上下文长度线性增长。vLLM 的 PagedAttention 让 KV 缓存分页（类似操作系统虚拟内存）广为人知，可减少碎片并提升吞吐，而 KV 缓存压缩方法则对缓存做有损压缩。KVMEM 进一步扩展了分页思路：将旧的 KV 状态换出到更廉价的内存中，需要时再重新载入，与“压缩+RAG”这类摘要并检索旧上下文的方案形成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.04852">KVMem : Virtualizing Million-Token Agent Workspaces on a Consumer...</a></li>
<li><a href="https://github.com/G0K0U/kvmem-agent-16gb">GitHub - G0K0U/ kvmem -agent-16gb: Reproducible 16GB-VRAM...</a></li>
<li><a href="https://tildalice.io/pagedattention-vllm-kv-cache-throughput/">PagedAttention in vLLM: KV Cache Paging for 24x Throughput</a></li>

</ul>
</details>

**标签**: `#AI research`, `#KV cache`, `#long-context memory`, `#agents`, `#LLM inference`

---

<a id="item-12"></a>
## [Qwen-Image-2.1 登顶 Arena 图像编辑与文生图开源榜第一](https://aihot.news/items/cmudfo3yi090orogg6bl51tiq) ⭐️ 8.0/10

阿里通义千问团队宣布 Qwen-Image-2.1 在 Arena 的 Image Edit Arena 和 Text-to-Image Arena 两个榜单上均位列开源模型第一。其在 Image Edit Arena 上得分 1367，总榜排名第 16，仅比第 15 名的 GPT-Image-1.5-high-fidelity 低 3 分。 这表明开源图像生成与编辑模型已经基本追平最先进的闭源前沿模型。这使开发者、创业公司和研究人员能够免费使用接近前沿的能力，将加剧图像生成领域的竞争。 尽管 Arena 总榜前列被闭源模型占据，Qwen-Image-2.1 的 Image Edit Arena 得分 1367 仅比 OpenAI 的闭源模型 GPT-Image-1.5-high-fidelity 低 3 分。该排名基于 LMArena 平台的用户偏好投票。

rss · AI Hot · Sep 23, 01:24

**背景**: LMArena（前身为 Chatbot Arena）通过用户盲测对比 AI 模型，并将胜率换算为类似 Elo 的评分。Image Edit Arena 评测基于指令的图像编辑能力，Text-to-Image Arena 评测文生图质量。Qwen-Image 是阿里巴巴的开源图像生成模型系列，GPT-Image-1.5 则是 OpenAI 的闭源图像生成模型。

**标签**: `#Qwen`, `#image-generation`, `#open-source-AI`, `#text-to-image`, `#leaderboard`

---

<a id="item-13"></a>
## [Claude Opus 5.5 发布成本降 40%；小米开源 MiMo-V2.6 强化学习框架](https://aihot.news/items/cmuddlkm206piroggzfferg09) ⭐️ 8.0/10

Anthropic 发布 Claude Opus 5.5，官方称典型任务成本较 Opus 5 降低 40%，并新增每次行动前的分类器、可审计沙箱与合并前代码审查等安全特性。小米发布并开源 MiMo-V2.6 系列，采用大规模强化学习训练，两个模型在 6 天 Live RL 中各完成 30 步、累计约 75 万条轨迹，同时公开了训练框架与轻量 Harness。 这两项发布体现了行业两大趋势的交汇：前沿实验室通过环境隔离而非模型自觉来强化 Agent 安全，以及小米等开源力量将传统上最不透明的强化学习训练阶段完全公开。更便宜的前沿模型加上公开的 RL 基础设施，可能同时加速企业落地与社区驱动的能力提升。 Anthropic 的方案明确承认 AI Agent 安全不能只靠模型自觉，需要沙箱隔离、权限收口与出口治理共同兜底。小米 MiMo-V2.6 包含原生全模态模型（Pro 为最强版本），发布内容不止权重，还包括技术报告、训练环境与 RL 代码，据报道单步训练消耗 20 亿 token、成本超 128 万美元。

rss · AI Hot · Sep 23, 00:29

**背景**: 在可验证任务上进行强化学习（RL）已成为突破监督预训练能力上限的关键方法，但 RL 阶段通常是前沿模型开发中最不透明的一环。小米的 RSI 路径探索在复杂可验证任务上扩展 RL 算力，让模型通过探索与反馈不断扩展能力边界。在安全方面，Anthropic 持续公开 Claude.ai、Claude Code 与 Cowork 的沙箱隔离设计，主张限制 Agent 行为的爆炸半径比单纯行为审核更重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://fluxbbs.com/mimo-v2-6-rl-training-public/">小米 MiMo-V2.6 RL 训练公开：单步 20 亿 Token，成本破 128 万美元 |...</a></li>
<li><a href="https://gyznsw.cn/2026/05/31/2026-05-31-Anthropic详解Claude产品沙箱技术-AI-Agent安全不能只靠模型自觉/">Anthropic详解Claude产品沙箱技术：AI Agent安全，不能只靠模型自觉 |...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#reinforcement learning`, `#AI models`, `#open source AI`

---

<a id="item-14"></a>
## [DeepSeek 与清华联合发布 DSec 沙箱平台技术报告](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI 与清华大学联合发布了 DSec（DeepSeek Elastic Compute）技术报告，公开了这一每日服务约 300 万个沙箱实例的弹性沙箱基础设施，用于支撑大规模智能体训练与基于强化学习的评测。平台通过统一 SDK 提供 FnCall、容器、Firecracker microVM 和完整 VM 四种后端，覆盖 OJ 判题、软件工程、安全渗透和电脑操作等负载。 大规模训练和评测智能体需要在隔离环境中执行不可信的、有状态的代码，而 DSec 展示了一套日服务数百万实例的生产级系统。该报告为 AI 基础设施社区提供了一份罕见且详细的蓝图，展示了如何将有状态的 rollout 执行与可抢占的 GPU 训练解耦，这正是智能体强化学习的关键瓶颈。 单个约 160 节点的生产单元每日服务约 300 万个沙箱，峰值并发超过 38 万，创建速度超过每秒 5000 个；单节点可承载 3200 个容器或 800 个 microVM。通过 3FS 分布式文件系统按需加载 EROFS 镜像而非 Docker 全量拉取，任务完成时间快 1.7 倍、磁盘写入减少 57%；内存共享与回收机制使峰值内存占用下降约 40%。

telegram · @zaihuapd · Sep 22, 04:45

**背景**: Firecracker 是 AWS 开源的虚拟化技术，基于 Linux KVM 创建轻量级 microVM，兼具硬件虚拟化的安全隔离、亚秒级启动和低内存开销，单机可运行数千个 microVM。EROFS 是最初由华为开发的轻量级只读 Linux 文件系统，支持压缩和高效的按需块加载。3FS（Fire-Flyer File System）是 DeepSeek 此前开源的高性能分布式文件系统，DSec 借助它在节点间共享不可变的沙箱镜像，避免数据重复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">[2609.22978] DeepSeek Elastic Compute (DSec): A Sandbox...</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast ... GitHub - firecracker-microvm/firecracker: Secure and fast ... firecracker-microvm/firecracker | DeepWiki I tried Firecracker microVMs for self-hosted services, and it ... Run Your First Firecracker microVM - labs.iximiuz.com What Is a Firecracker VM? · Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI-agents`, `#AI-infrastructure`, `#reinforcement-learning`, `#microVM`

---

<a id="item-15"></a>
## [中国监管机构调查 DeepSeek 与月之暗面涉嫌数据泄露](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

据知情人士透露，中国互联网监管机构正在调查 DeepSeek 和月之暗面，起因是 Anthropic 于 9 月 10 日发布的 154 页报告，该报告指控 7 家中国公司大规模违规使用 Claude API，并将敏感用户数据转发给 Claude。报告中举例称，DeepSeek 曾将一名警方监控系统开发工程师的请求转发给 Claude。 这是中国监管机构罕见地根据美国 AI 公司对中国本土头部 AI 企业的指控采取行动，对数据安全、AI 治理以及中美 AI 博弈都有重要影响。这也表明通过境外模型 API 进行的跨境数据流动正成为中国监管层的高度关注点。 调查的核心指控是，包括警方监控系统开发者发出的敏感请求在内的用户查询被转发至 Anthropic 的 Claude API，实质上使这些数据流出中国。Anthropic 的报告认定 7 家中国公司大规模违反其使用条款，而 DeepSeek 和月之暗面目前正面临监管审查。

telegram · @zaihuapd · Sep 22, 14:37

**背景**: DeepSeek 是总部位于杭州的 AI 公司，以开源权重大语言模型著称；月之暗面（Moonshot AI）是总部位于北京的初创公司，被誉为中国 'AI 六小虎' 之一，以 Kimi 聊天助手闻名。Anthropic 是美国 AI 公司，其 Claude 模型通过 RESTful API 提供访问，其使用条款对用途和地域有限制。将中国用户数据发送至美国托管的 API，既可能违反使用条款，也涉及中国的数据跨境传输合规问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://platform.claude.com/docs/en/api/overview">API overview - Claude Platform Docs - Anthropic</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Anthropic`, `#AI治理`, `#数据泄露`, `#中国AI监管`

---

<a id="item-16"></a>
## [DeepSeek 本周将向联合国安理会通报 AI 风险](https://t.me/zaihuapd/43989) ⭐️ 8.0/10

据路透社援引两名知情人士报道，中国 AI 初创公司 DeepSeek 将于本周三向由 15 个成员组成的联合国安理会通报人工智能带来的风险。OpenAI 首席执行官 Sam Altman 计划出席，Anthropic 高层代表预计参加，月之暗面（Moonshot）等中国 AI 公司也受邀发言。 这是中美前沿 AI 实验室罕见地共同面向联合国最高安全机构发言，表明 AI 风险已被视为国际和平与安全问题。此举可能影响全球 AI 治理框架的成形，以及中美在 AI 安全领域的合作走向。 据报道，DeepSeek 创始人梁文锋不打算出席，但相关安排仍可能临时变动。安理会会议定于周三举行，聚焦 AI 与国际安全议题。

telegram · @zaihuapd · Sep 22, 17:39

**背景**: DeepSeek 是一家总部位于杭州的中国 AI 公司，由对冲基金幻方量化（High-Flyer）出资，专注于开发开放权重的大语言模型，曾在登顶应用下载榜后引发美国科技股下跌而声名大噪。月之暗面（Moonshot AI）是另一家领先的中国大模型公司，以 Kimi 系列模型著称。联合国安理会近年在国际安全框架下日益讨论 AI 议题，此次通报是主要中国 AI 公司与美国 OpenAI、Anthropic 等实验室首次在此类场合同台的重要节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.bbc.com/news/articles/c5yv5976z9po">What is DeepSeek - and why is everyone talking about it?</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#AI治理`, `#DeepSeek`, `#联合国安理会`, `#国际政策`

---