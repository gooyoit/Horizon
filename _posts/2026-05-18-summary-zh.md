---
layout: default
title: "Horizon Summary: 2026-05-18 (ZH)"
date: 2026-05-18
lang: zh
---

> From 80 items, 2 important content pieces were selected

---

1. [OpenClaw 开发者单月消耗 130 万美元 OpenAI API Token](#item-1) ⭐️ 9.0/10
2. [Semble：面向 AI 智能体的高效代码搜索工具](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenClaw 开发者单月消耗 130 万美元 OpenAI API Token](https://www.tomshardware.com/tech-industry/artificial-intelligence/openclaw-creator-burns-through-1-3-million-in-openai-api-tokens-in-a-single-month) ⭐️ 9.0/10

An OpenAI employee spent $1.3 million in a single month on 100 autonomous Codex agents to stress-test AI-driven development, generating 603 billion tokens and revealing the use of a future 'GPT-5.5' model.

telegram · @zaihuapd · May 17, 13:38

**标签**: `#OpenAI`, `#AI Agents`, `#Codex`, `#GPT-5.5`, `#AI Infrastructure`

---

<a id="item-2"></a>
## [Semble：面向 AI 智能体的高效代码搜索工具](https://github.com/MinishLab/semble) ⭐️ 8.0/10

MinishLab 开源了 Semble，这是一款面向 AI 智能体的代码搜索工具，结合了静态 Model2Vec 嵌入（potion-code-16M）与 BM25 关键词搜索，通过 Reciprocal Rank Fusion（RRF）进行融合，并使用代码感知信号进行重排序。在涵盖 63 个代码仓库和 19 种语言的约 1250 个查询/文档对基准测试中，它达到了 0.854 的 NDCG@10，相比 grep+read 减少了 98% 的 token 用量，同时达到了 1.37 亿参数 transformer 99% 的检索质量。 在大型代码库中，AI 编程智能体（如 Claude Code、Cursor 和 Codex）在进行代码搜索时消耗大量 token 是一个关键瓶颈，智能体往往会回退到 grep 并读取整个文件。Semble 通过提供一个即插即用的 MCP 服务器直接解决了这一问题，大幅减少了 token 浪费，降低了智能体驱动开发流程的成本和延迟。 Semble 完全在 CPU 上运行，无需 GPU、API 密钥或外部服务，索引一个典型代码仓库约需 250 毫秒，查询响应约 1.5 毫秒。其核心创新在于使用 Model2Vec 的静态嵌入——从句子 transformer 蒸馏得到的模型，速度提升高达 500 倍、体积缩小 50 倍——并通过 RRF 与 BM25 词法搜索相结合，避免了查询时 transformer 推理的开销。

hackernews · Bibabomas · May 17, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48169874)

**背景**: Model2Vec 是一种将任意句子 transformer 蒸馏为小型快速静态嵌入模型的技术，可将模型大小缩小最多 50 倍，速度提升最多 500 倍，性能损失很小。BM25（Best Matching 25）是一种经典的信息检索排序算法，基于词频和逆文档频率对文档相关性进行评分，广泛应用于搜索引擎中。Reciprocal Rank Fusion（RRF）是一种将多个排序结果集合并为单一排序的方法，通过对所有检索器的倒数排名求和来实现，能够有效地融合语义和词法信号进行混合搜索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MinishLab/model2vec">GitHub - MinishLab/model2vec: Fast State-of-the-Art Static Embeddings · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Okapi_BM25">Okapi BM 25 - Wikipedia</a></li>
<li><a href="https://medium.com/@devalshah1619/mathematical-intuition-behind-reciprocal-rank-fusion-rrf-explained-in-2-mins-002df0cc5e2a">Reciprocal Rank Fusion (RRF) explained in 4 mins — How to score results form multiple retrieval methods in RAG | by Deval Shah | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极，但提出了实际使用中的顾虑：有用户指出在小型代码库上，启动时直接将整个代码库加载到上下文中比任何搜索工具都更高效。一个关键担忧是，经过大量 grep 相关强化学习训练的模型可能不信任其他工具返回的结果，会反复重试或重新读取，可能抵消 token 节省的效果——用户希望看到实际的端到端智能体基准测试来验证真实场景下的 token 减少量。还有用户询问与现有 LSP 方案及 colgrep 等工具的对比情况。

**标签**: `#code-search`, `#AI-agents`, `#embeddings`, `#developer-tools`, `#token-optimization`

---