---
layout: default
title: "Horizon Summary: 2026-04-01 (ZH)"
date: 2026-04-01
lang: zh
---

> From 87 items, 35 important content pieces were selected

---

1. [Claude Code 源代码通过 NPM 源映射文件泄露](#item-1) ⭐️ 9.0/10
2. [OpenAI 以 8520 亿美元估值完成 1220 亿美元融资](#item-2) ⭐️ 9.0/10
3. [黄仁勋亲述英伟达十年豪赌 CUDA](#item-3) ⭐️ 9.0/10
4. [谷歌宣称量子计算突破可攻破比特币加密](#item-4) ⭐️ 9.0/10
5. [谷歌量子 AI 将比特币攻击成本降低 20 倍](#item-5) ⭐️ 9.0/10
6. [GitHub 现非官方仓库，从 npm 包还原 Claude Code 源码](#item-6) ⭐️ 9.0/10
7. [谷歌推出 Veo 3.1 Lite 并下调 Veo 3.1 Fast 价格](#item-7) ⭐️ 9.0/10
8. [经济激励将推动 AI 编写优质代码](#item-8) ⭐️ 8.0/10
9. [Datasette-LLM 0.1a4 支持按模型配置独立 API 密钥](#item-9) ⭐️ 8.0/10
10. [橡鹿机器人完成 3 亿元融资](#item-10) ⭐️ 8.0/10
11. [AI 初创公司 DigClaw 获天使轮融资](#item-11) ⭐️ 8.0/10
12. [PathFinder 完成数千万元天使轮融资](#item-12) ⭐️ 8.0/10
13. [宾大 00 后团队推高尔夫 AI Agent 硬件，获数千万融资](#item-13) ⭐️ 8.0/10
14. [全球首款 AI 笔记戒指 Vocci Ring 开启预售](#item-14) ⭐️ 8.0/10
15. [拆分代码给不同 AI 防泄密，可行吗？](#item-15) ⭐️ 8.0/10
16. [无审查版 Qwen3.5-35B 模型引发社区关注](#item-16) ⭐️ 8.0/10
17. [开发者寻求 AI 多格式填表工具的应用场景](#item-17) ⭐️ 8.0/10
18. [AMD 将于 7 月举办 Advancing AI 2026 大会](#item-18) ⭐️ 8.0/10
19. [Nothing 进军 AI 智能眼镜领域，计划 2027 年推出首款产品](#item-19) ⭐️ 8.0/10
20. [台积电 3 纳米产能告急，三星 2 纳米成唯一替代方案](#item-20) ⭐️ 8.0/10
21. [法拉第未来 2025 年净资产转正，2026 年机器人出货目标超千台](#item-21) ⭐️ 8.0/10
22. [智谱 AI 2025 年营收大增 131.9%，净亏损扩大](#item-22) ⭐️ 8.0/10
23. [曹操出行在杭州启动无安全员 Robotaxi 道路测试](#item-23) ⭐️ 8.0/10
24. [千问测试“引证”功能以核查回答信源](#item-24) ⭐️ 8.0/10
25. [GitHub Copilot 在拉取请求中插入自我宣传广告](#item-25) ⭐️ 8.0/10
26. [开源 AI 技能根据聊天记录模拟前任](#item-26) ⭐️ 8.0/10
27. [苹果测试 Siri 多指令识别功能，iOS 27 将支持单句多任务](#item-27) ⭐️ 8.0/10
28. [AIGC 求职者询问面试是否仍考八股文和算法题](#item-28) ⭐️ 7.0/10
29. [LLM 开发被比作《封神演义》中的法宝斗法](#item-29) ⭐️ 7.0/10
30. [通过白山云中转调用国产大模型体验不佳](#item-30) ⭐️ 7.0/10
31. [代充网站低价出售 ChatGPT Plus 和 Codex API 额度](#item-31) ⭐️ 7.0/10
32. [用户求助使用 AI 自动剪辑短视频](#item-32) ⭐️ 7.0/10
33. [《红色沙漠》成 2026 年 M 站玩家评分第二高游戏](#item-33) ⭐️ 7.0/10
34. [百度萝卜快跑武汉夜间故障致乘客被困高架](#item-34) ⭐️ 7.0/10
35. [传闻 PS6 将全面转向数字版，定价 699 美元并采用神经纹理压缩技术](#item-35) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude Code 源代码通过 NPM 源映射文件泄露](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/) ⭐️ 9.0/10

Anthropic 意外将一个源映射（source map）文件发布到 NPM 注册表，使得外界几乎完整还原了 Claude Code 的 51.2 万行 TypeScript 源代码，其中包含内部提示词、未发布的“ undercover mode”功能以及用于检测用户挫败情绪的正则表达式。此次泄露已引发 DMCA 删除通知和社区广泛分析。 此次泄露暴露了一家领先 AI 实验室的敏感开发实践和战略决策，削弱了外界对 Anthropic 运营安全的信任，并引发对 AI 系统知识产权保护的担忧。它还揭示了 AI 编程助手如何在内部被设计成隐藏其身份并影响用户认知。 泄露的代码包含超过 2300 个文件，其中包含用于干扰模型蒸馏的“虚假工具”、基于正则表达式的挫败情绪检测机制，以及严格禁止在提交信息中提及“Claude Code”或 AI 身份的规则。尽管不包含实际模型权重，但源码揭示了智能体运行时逻辑、工具系统，以及直接写在注释中的商业决策依据。

hackernews · alex000kim · Mar 31, 13:04

**背景**: 源映射（source map）文件通常在 JavaScript/TypeScript 构建过程中生成，用于将压缩后的生产代码映射回原始源码以便调试。但如果被公开发布，就可能意外暴露完整源代码。Anthropic 的“Claude Code”是一款 AI 驱动的编程助手，旨在帮助开发者编写、调试和理解代码，属于与 GitHub Copilot 等工具竞争的“前沿 AI”生态系统的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/">Anthropic’s Claude source code leaked via a map file in their ...</a></li>
<li><a href="https://winbuzzer.com/2026/03/31/claude-code-source-leaked-npm-source-map-xcxwbn/">Anthropic Leaks Claude Code Source via Npm Source Map</a></li>
<li><a href="https://github.com/Kuberwastaken/claude-code">GitHub - Kuberwastaken/claude-code: Claude Code's Source Code ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对代码注释中暴露的大量内部细节（包括商业决策）感到惊讶。一些人批评 Anthropic 对不含泄露代码的仓库也发起激进的 DMCA 删除请求，另一些人则质疑频繁泄露是否反映出系统性运营问题，进而损害用户信任。

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#source code leak`, `#frontier tech`

---

<a id="item-2"></a>
## [OpenAI 以 8520 亿美元估值完成 1220 亿美元融资](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html) ⭐️ 9.0/10

OpenAI 宣布完成一轮融资，获得 1220 亿美元的承诺资本，投后估值达 8520 亿美元，创下科技行业私营公司估值新高。 这一里程碑凸显了 OpenAI 在人工智能竞赛中的主导地位，并反映出投资者对前沿 AI 发展的巨大信心，尽管市场对其可持续性和饱和度存在担忧。这也凸显了领先 AI 实验室与 Anthropic 等竞争对手之间日益扩大的资金差距。 1220 亿美元是“承诺资本”，即投资者的合同承诺，可能在未来分期支付且取决于某些条件，并非即时现金流入。8520 亿美元是投后估值，即包含新投资后的公司总估值。

hackernews · surprisetalk · Mar 31, 20:07

**背景**: 投后估值是指公司在获得外部投资后的估值，等于投前估值加上新注入资本。承诺资本在风险投资和私募股权中很常见，投资者承诺资金但按需分期支付，而非一次性到账。OpenAI 成立于 2015 年，2022 年凭借 ChatGPT 获得全球关注，此后成为大语言模型商业化的核心参与者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html">OpenAI closes funding round at an $852 billion valuation - CNBC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-money_valuation">Post-money valuation</a></li>
<li><a href="https://www.investopedia.com/terms/c/committedcapital.asp">Guide to Committed Capital: Definition and Practical Uses What is committed capital: definition and its role in private ... What Is Committed Capital in Private Equity? - LegalClarity Today, we closed our latest funding round with $122 billion ... Guide to Committed Capital : Definition and Practical Uses Guide to Committed Capital : Definition and Practical Uses What is committed capital : definition and its role in private equity What is committed capital : definition and its role in private equity What is committed capital - mondfx.com</a></li>

</ul>
</details>

**社区讨论**: 社区成员质疑 1220 亿美元的数据是否具有误导性，指出这反映的是有条件承诺而非实际到账资金。其他人将 OpenAI 的收入增长与 Anthropic 近期的迅猛势头对比，对其高估值的可持续性表示怀疑。还有人感叹普通投资者难以分享 AI 领域的财务收益。

**标签**: `#AI`, `#OpenAI`, `#funding`, `#valuation`, `#frontier tech`

---

<a id="item-3"></a>
## [黄仁勋亲述英伟达十年豪赌 CUDA](https://www.ithome.com/0/934/760.htm) ⭐️ 9.0/10

英伟达 CEO 黄仁勋在近期 Lex Fridman 播客中透露，公司 2006 年在 GeForce 显卡上强推 CUDA 架构是一场几乎导致破产的豪赌，历经十年才迎来转机。尽管初期遭遇严重财务打击和市场质疑，CUDA 最终成为英伟达主导 AI 领域的基石。 CUDA 的成功使 GPU 从纯图形硬件转变为关键的 AI 加速器，为英伟达在蓬勃发展的 AI 基础设施市场构筑了难以逾越的软硬件护城河。这一战略远见表明，对基础平台的长期投入能够重塑整个产业格局。 在消费级显卡中强行加入 CUDA 功能使生产成本骤增 50%，毛利率暴跌至 35%，公司市值一度跌至仅 15 亿美元。英伟达顶住压力持续投入巨额研发资金长达十年，直到 AI 和高性能计算（HPC）应用兴起才证明该战略的正确性。

rss · IT HOME · Apr 1, 02:05

**背景**: CUDA（Compute Unified Device Architecture）是英伟达专有的并行计算平台，支持在 GPU 上进行通用计算（GPGPU）。在 CUDA 出现前，GPU 主要用于图形渲染；可编程着色器（如 GeForce 3 引入的技术）虽已支持有限计算，但 CUDA 统一并泛化了这一能力，使 GPU 可用于科学计算和 AI 任务。这需要硬件、驱动和软件库的深度协同设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shader">Shader - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/drivers/feature-pixelshader/">Pixel Shaders - NVIDIA</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#CUDA`, `#NVIDIA`, `#GPU Computing`, `#Frontier Tech`

---

<a id="item-4"></a>
## [谷歌宣称量子计算突破可攻破比特币加密](https://www.ithome.com/0/934/737.htm) ⭐️ 9.0/10

谷歌发布了两份白皮书，展示量子计算的重大进展：一项利用中性原子量子比特破解 256 位加密所需资源仅为此前预估的 1/100；另一项改进了秀尔算法，可在 10 分钟内攻破比特币的椭圆曲线加密，计算资源消耗降至原来的 1/20。 这一进展大幅降低了量子攻击主流加密系统的门槛，对区块链、数字金融和加密通信的安全基础构成严重威胁。如果可扩展的量子计算机比预期更早实现，现有加密标准可能一夜之间失效。 第一种方法采用可重构的中性原子量子比特，支持跨区域直接通信并提升纠错效率，仅需不到 3 万个物理量子比特即可在 10 天内破解 256 位加密。第二种方法针对比特币的 ECDSA 签名算法，仅需约 50 万个物理量子比特（为去年破解 RSA 所需的一半），但谷歌因担忧被恶意利用而未公开算法细节，仅通过零知识证明证实其有效性。

rss · IT HOME · Apr 1, 01:27

**背景**: 量子计算机利用量子力学原理，在某些问题上比经典计算机快指数级。1994 年提出的秀尔算法理论上能让量子计算机高效解决整数分解和离散对数问题，从而破解 RSA 和椭圆曲线等公钥加密体系。中性原子量子计算是一种新兴技术平台，通过激光囚禁单个中性原子并操控其内部能级作为量子比特，在可扩展性和相干时间方面具有优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/中性原子量子计算机">中性原子量子计算机 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/秀爾演算法">秀尔算法 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.baqis.ac.cn/news/detail/?cid=2211">量子计算新突破：中性原子量子计算机崛起</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#blockchain`, `#frontier tech`, `#encryption`

---

<a id="item-5"></a>
## [谷歌量子 AI 将比特币攻击成本降低 20 倍](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) ⭐️ 9.0/10

谷歌量子 AI 通过优化 Shor 算法，将破解比特币所用椭圆曲线加密所需的量子资源减少了 20 倍，仅需不到 50 万个物理量子比特即可在 9 分钟内恢复私钥。 这一突破大幅降低了对主流加密系统（如比特币和以太坊）实施量子攻击的硬件门槛，使现有加密资产面临更紧迫的威胁，凸显了向抗量子密码迁移的迫切性。 该攻击需要两种电路设计，分别需少于 1200 和 1450 个逻辑量子比特；经纠错后，在超导量子硬件上对应不到 50 万个物理量子比特。目前约三分之一的比特币（690 万枚）使用已暴露的公钥，一旦此类量子计算机问世，这些资产可能面临风险。

telegram · zaihuapd · Mar 31, 08:03

**背景**: 比特币和以太坊依赖椭圆曲线加密（ECC），特别是椭圆曲线数字签名算法（ECDSA）来保障交易安全。ECC 的安全性基于椭圆曲线离散对数问题（ECDLP）的计算难度。Shor 算法是一种量子算法，能高效求解 ECDLP，从而破解 ECC——但前提是运行在足够大规模且具备纠错能力的量子计算机上。逻辑量子比特是由多个易受噪声干扰的物理量子比特构建而成的纠错计算单元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/quant-ph/0301141">Shor's discrete logarithm quantum algorithm for elliptic curves Shor’s Algorithm: Breaking RSA and ECC Encryption - Part 1 The Day After Cryptography: How a Quantum Experiment Just ... Quantum Resource Estimates for Computing Elliptic Curve ... elliptic curves - How can Shor's Algorithm be applied to ECC ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Physical_and_logical_qubits">Physical and logical qubits - Wikipedia</a></li>
<li><a href="https://blog.projecteleven.com/posts/shors-algorithm-for-discrete-logs">Shor’s Algorithm for Discrete Logs - Project Eleven - Blog</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#Bitcoin`, `#Shor's algorithm`, `#frontier technology`

---

<a id="item-6"></a>
## [GitHub 现非官方仓库，从 npm 包还原 Claude Code 源码](https://t.me/zaihuapd/40625) ⭐️ 9.0/10

一个名为 claude-code-sourcemap 的 GitHub 仓库声称通过公开 npm 包@anthropic-ai/claude-code 中的 source map 文件 cli.js.map 里的 sourcesContent 字段，还原出 Anthropic 的 Claude Code 2.1.88 版本共 4756 个源文件，其中包括 1884 个 TypeScript（.ts/.tsx）文件，涵盖 CLI、插件、Vim 模式等模块。 此事件揭示了前端打包流程中的潜在风险，引发对顶尖 AI 公司意外泄露知识产权的担忧，同时也加剧了关于前沿 AI 工具在透明度、安全性和负责任披露方面的讨论。 此次还原依赖于 source map 中的 sourcesContent 字段，该字段会直接嵌入原始源代码，通常用于调试，但如果包含敏感代码则不适合用于生产环境。该仓库明确声明其为非官方项目，仅限研究用途，并警告用户不要将其与 Claude Code 账户关联，以免因远程 URL 哈希识别导致账户风险。

telegram · zaihuapd · Mar 31, 15:22

**背景**: Source map 是一种将压缩或转译后的代码映射回原始源代码的文件，主要用于调试。其中的 sourcesContent 字段可选择性地内联包含完整的原始源代码。Claude Code 是由 Anthropic 开发的一款基于终端的 AI 编程助手，能理解代码库并通过自然语言命令执行任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/aws-builders/anthropic-accidentally-leaked-claude-codes-source-code-heres-what-that-means-2f89">Anthropic accidentally leaked Claude Code's source code. Here ...</a></li>
<li><a href="https://www.npmjs.com/package/source-map">source-map - npm</a></li>
<li><a href="https://github.com/li-plus/claude-code-2.1.88">GitHub - li-plus/claude-code-2.1.88: Source code of ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#source code leak`, `#frontier tech`

---

<a id="item-7"></a>
## [谷歌推出 Veo 3.1 Lite 并下调 Veo 3.1 Fast 价格](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/) ⭐️ 9.0/10

谷歌推出了新的低成本视频生成模型 Veo 3.1 Lite，其价格不到 Veo 3.1 Fast 的一半但速度相同，并宣布自 4 月 7 日起下调 Veo 3.1 Fast 的价格。 此举让高频视频应用的开发者能以更低的成本使用高质量 AI 视频生成功能，在 OpenAI Sora 退出之际，巩固了谷歌在生成式视频领域的竞争力。 Veo 3.1 Lite 支持文生视频和图生视频，可生成 16:9 或 9:16 比例的 720p 或 1080p 视频，时长可选 4 秒、6 秒或 8 秒，费用随长度调整，并已通过 Gemini API 和 Google AI Studio 提供。

telegram · zaihuapd · Mar 31, 17:35

**背景**: 谷歌的 Veo 系列是用于生成高保真视频的前沿生成式 AI 模型，具备逼真的画面和原生音频。Veo 3.1 系列包含针对速度优化的 Fast 版本，以及新推出的面向成本敏感型开发者的 Lite 版本，均通过 Gemini API 平台提供服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/">Build with Veo 3.1 Lite, our most cost-effective video generation model</a></li>
<li><a href="https://9to5google.com/2026/03/31/veo-3-1-lite/">Google commits to video generation, announces Veo 3.1 Lite</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview">Veo 3.1 Lite Preview | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#AI`, `#generative video`, `#Google`, `#Veo`, `#frontier tech`

---

<a id="item-8"></a>
## [经济激励将推动 AI 编写优质代码](https://simonwillison.net/2026/Apr/1/soohoon-choi/#atom-everything) ⭐️ 8.0/10

崔秀勋（Soohoon Choi）认为，市场竞争将青睐那些生成简洁、可靠且可维护代码的 AI 模型，因为这类代码能帮助开发者更快、更经济地交付功能。 这一观点挑战了人们担心 AI 会向软件开发领域倾泻低质量“垃圾代码”（slop）的忧虑，并指出长期经济力量可能与工程最佳实践保持一致。这为 AI 辅助编程在专业软件工程中的未来提供了乐观前景。 崔强调优质代码的生成和维护成本更低，而那些能帮助开发者可靠交付功能的 AI 模型将获得市场回报。该论点假设开发者生产力和系统可靠性是 AI 工具被采用的关键指标。

rss · Simon Willison · Apr 1, 02:07

**背景**: “AI slop”（AI 垃圾内容）指由 AI 系统大规模生成的低投入、低质量数字内容——尤其是代码——通常优先考虑速度或数量，而非正确性或可维护性。随着人们对生成式 AI 可能降低软件质量的担忧加剧，这一术语逐渐流行。与此同时，“代理式工程”（agentic engineering）描述了一种新兴方法：AI 代理在人类监督和工程规范下辅助开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://addyosmani.com/blog/agentic-engineering/">AddyOsmani.com - Agentic Engineering</a></li>

</ul>
</details>

**标签**: `#ai-assisted-programming`, `#generative-ai`, `#software-engineering`, `#ai-economics`, `#code-quality`

---

<a id="item-9"></a>
## [Datasette-LLM 0.1a4 支持按模型配置独立 API 密钥](https://simonwillison.net/2026/Mar/31/datasette-llm/#atom-everything) ⭐️ 8.0/10

Datasette-LLM 0.1a4 版本新增了按用途为不同大语言模型（LLM）配置独立 API 密钥的功能，例如可为使用 'gpt-5.4-mini' 进行数据增强的任务分配专用密钥。该功能通过第 #4 号拉取请求实现，并已在插件文档中说明。 这一改进通过允许开发者按任务隔离 API 使用，提升了安全性和操作灵活性，降低了密钥泄露风险，并支持在 Datasette 应用中对不同 LLM 功能进行细粒度的成本或访问控制。 该功能依赖于插件配置中定义的带自定义 API 密钥的模型引用；它还需要配套工具如 llm-echo 0.3，其中包含一个专门用于验证密钥处理逻辑的测试模型（'echo-needs-key'）。

rss · Simon Willison · Mar 31, 21:17

**背景**: Datasette 是一个用于探索、分析和发布结构化数据的开源工具。围绕 Datasette 构建的 LLM 生态系统基于 'llm' Python 库，允许插件通过 API 或本地运行方式集成多种大语言模型。像 datasette-enrichments-llm 这样的插件利用这些模型为数据集添加 AI 生成的洞察信息。在此之前，所有模型共用一个 API 密钥配置，限制了安全性和管理灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-llm">GitHub - datasette/datasette-llm: LLM integration plugin for ...</a></li>
<li><a href="https://datasette.io/tools/llm">llm - a tool for Datasette</a></li>
<li><a href="https://github.com/simonw/llm-echo">GitHub - simonw/ llm - echo : Debug plugin for LLM providing an echo...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Datasette`, `#AI tools`, `#API management`, `#open-source`

---

<a id="item-10"></a>
## [橡鹿机器人完成 3 亿元融资](https://36kr.com/newsflashes/3747636678558468?f=rss) ⭐️ 8.0/10

橡鹿机器人宣布完成 3 亿元人民币融资，由亦庄国投管理的产业升级基金领投，琥珀、九安、海棠跟投。 此次大额融资凸显了市场对 AI 驱动的机器人在工业和商业场景（尤其是餐饮自动化）中的信心，也反映出中国前沿科技领域在 AI 与硬件融合趋势下获得的强劲机构支持。 这是橡鹿机器人继源码资本、IDG、腾讯、京东等知名机构投资后的又一轮重磅融资。该公司专注于 AI 炒菜机器人，具备视觉识别、味觉传感及云端机器学习能力。

rss · 36kr · Apr 1, 02:13

**背景**: 橡鹿机器人隶属于橡鹿科技，主打智能炒菜机器人，致力于实现中餐标准化与自动化。该公司利用 AI 技术模拟人类厨师技艺，通过计算机视觉识别食材，并借助机器学习持续优化菜谱。这类系统是餐饮服务与工业自动化领域 AI 融合服务机器人发展趋势的重要组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ofweek.com/ai/2025-12/ART-201717-8420-30676679.html">ofweek.com/ai/2025-12/ART-201717-8420-30676679.html</a></li>
<li><a href="https://flygood.top/">橡 鹿 -智能炒菜 机 领导者</a></li>

</ul>
</details>

**标签**: `#robotics`, `#frontier tech`, `#venture funding`, `#AI hardware`, `#industrial automation`

---

<a id="item-11"></a>
## [AI 初创公司 DigClaw 获天使轮融资](https://36kr.com/newsflashes/3747633849385730?f=rss) ⭐️ 8.0/10

AI 驱动的意图雷达初创公司 DigClaw 近日宣布完成天使轮融资，由中科创星和中关村资本联合投资。 此次融资凸显了市场对 AI 驱动的意图识别技术日益增长的兴趣，该技术对下一代人机交互和企业智能应用至关重要。这也表明投资者对中国创新中心涌现的前沿科技初创企业充满信心。 DigClaw 自称“科创意图雷达”，暗示其利用 AI 在科研或创新场景中探测并解读用户或市场意图。该公司正式注册名为北京孤勇众行科技有限公司。

rss · 36kr · Apr 1, 02:10

**背景**: 意图识别是人工智能的一个子领域，专注于识别人类行为或交流背后的目标或目的，常用于聊天机器人、虚拟助手和行为分析中。“雷达”一词在 DigClaw 的描述中是比喻用法，指其扫描和探测新兴意图的能力，而非使用真实的无线电波雷达技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intent_recognition">Intent recognition</a></li>
<li><a href="https://medium.com/@aiinisghtful/intent-recognition-using-a-llm-with-predefined-intentions-4620284b72f7">Intent Recognition using a LLM with Predefined Intentions</a></li>

</ul>
</details>

**标签**: `#AI`, `#startup funding`, `#intent recognition`, `#frontier tech`, `#angel investment`

---

<a id="item-12"></a>
## [PathFinder 完成数千万元天使轮融资](https://36kr.com/newsflashes/3747604605436420?f=rss) ⭐️ 8.0/10

AI 智能硬件初创公司 PathFinder Ltd.近日获得锦秋基金数千万元人民币的天使轮融资。资金将用于产品研发迭代、生产交付及早期渠道铺设，为即将开展的众筹活动做准备。 此次融资反映出投资者对 AI Agent 技术在实体产品中应用的浓厚兴趣，尤其是在面向消费者的智能硬件领域。这标志着 AI Agent 正从纯软件向现实世界交互设备加速落地。 本轮融资由锦秋基金独家投资，公司定位为“运动 AI Agent”智能硬件品牌。产品预计在完成当前研发阶段后通过众筹平台首发。

rss · 36kr · Apr 1, 01:40

**背景**: AI Agent 是指能够感知环境、自主决策并执行任务以达成特定目标的智能系统，通常无需持续人工干预。在智能硬件中，这类 Agent 可使设备实时适应用户行为或物理场景。“运动 AI Agent”这一术语暗示 PathFinder 可能聚焦于具备移动能力、类机器人特性或能响应人体活动的智能设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents? | IBM</a></li>
<li><a href="https://cloud.google.com/discover/what-are-ai-agents">What are AI agents? Definition, examples, and types | Google Cloud</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#smart hardware`, `#startup funding`, `#applied AI`, `#robotics-adjacent`

---

<a id="item-13"></a>
## [宾大 00 后团队推高尔夫 AI Agent 硬件，获数千万融资](https://36kr.com/p/3746252355535622?f=rss) ⭐️ 8.0/10

由宾夕法尼亚大学 GRASP 实验室校友创立的初创公司 PathFinder Ltd.近日完成数千万元天使轮融资，由锦秋基金独家投资，用于开发基于“感知-理解-决策”闭环架构的高尔夫 AI Agent 智能硬件系统。 此举标志着将前沿机器人与 AI 研究成果应用于现实体育场景的重要一步，超越了单纯的数据采集工具，迈向具备真正决策能力的智能系统，有望重塑消费级运动科技，并为物理世界中的 AI Agent 树立范例。 PathFinder 采用纯 RGB 摄像头视觉方案，结合定制算法与运动先验知识，以传统雷达或模拟器千分之一的成本实现完整的高尔夫球轨迹重建；其 AI Agent 通过长期用户建模，提供以结果为导向的个性化训练建议，而非简单的动作比对。

rss · 36kr · Apr 1, 01:33

**背景**: 宾夕法尼亚大学 GRASP 实验室是机器人、自动化、感知与控制领域的顶尖跨学科研究中心，以具身智能和自主系统研究著称。物理世界中的 AI Agent 需要构建“感知-理解-决策-执行”的闭环系统，即“具身智能”，这与纯软件对话型 Agent 有本质区别。高尔夫运动具有清晰的输入变量（挥杆动作、球杆）和可量化结果（球飞行轨迹），是验证此类智能系统的理想场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.grasp.upenn.edu/">GRASP Lab General Robotics, Automation, Sensing & Perception Lab</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1960987423178724929">技术视界｜从感知到工具链——实现具身智能机器人的闭环与实用化</a></li>
<li><a href="https://blog.csdn.net/sinat_28461591/article/details/147351284">【具身智能】感知 × 决策 × 执行：一个智能体的认知闭环怎么搭？_感知...</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Robotics`, `#Sports Tech`, `#Smart Hardware`, `#Frontier AI`

---

<a id="item-14"></a>
## [全球首款 AI 笔记戒指 Vocci Ring 开启预售](https://36kr.com/p/3746892878480132?f=rss) ⭐️ 8.0/10

Gyges Labs 推出了全球首款 AI 笔记戒指 Vocci Ring，支持免提语音激活 AI 智能体，在无需手机或屏幕的情况下执行电脑任务。该产品在 CES 2026 上首次亮相并斩获四项行业大奖。 Vocci Ring 标志着可穿戴 AI 的重大转变——从被动健康监测转向主动、无屏的生产力工具，为专业人士提供了一种实时与 AI 智能体交互的新方式。它契合了环境计算和用户可控型 AI 智能体的新兴趋势。 该戒指采用 Gyges Labs 自研的“类龙虾”AI 智能体（受 OpenClaw 启发），支持 112+种语言转写，采用航天级钛合金机身，支持 8 小时独立录音，并符合 GDPR 和 SOC2 安全标准。用户通过轻点或长按触发交互，配合触觉震动与 LED 反馈。

rss · 36kr · Apr 1, 01:30

**背景**: AI 智能体是能够感知环境、自主决策并代表用户执行任务的系统。OpenClaw（昵称“龙虾”）是一个于 2025 年底推出的开源、本地优先的 AI 智能体框架，以本地执行和系统级自动化著称。此前可穿戴 AI 设备多聚焦于生物监测，极少有产品通过直接控制 AI 智能体来提升生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.aliyun.com/article/1716042">火爆全网的AI智能体“龙虾”(OpenClaw)是什么？它能做什么？-阿里云开发...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2016618445031092252">龙虾智能体（OpenClaw）国产软件研究学习报告 - 知乎</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#wearable AI`, `#human-computer interaction`, `#frontier tech`, `#productivity tools`

---

<a id="item-15"></a>
## [拆分代码给不同 AI 防泄密，可行吗？](https://www.v2ex.com/t/1202706#reply0) ⭐️ 8.0/10

一位开发者提出将商业项目代码按模块拆分，分别交给 Kimi、ChatGPT、Claude 等不同 AI 助手处理，以防止任何单一平台获取完整项目信息，从而降低核心 IP 泄露风险。 随着 AI 编程工具深度融入开发流程，企业在享受效率提升的同时，必须应对代码泄露和训练数据滥用的风险。该方案体现了业界对第三方 API 安全隐患和知识产权保护的高度重视。 该方法牺牲了 AI 的上下文感知能力——因各模型无法看到其他模块代码，可能导致接口幻觉，需开发者大量手动对接。作者也质疑：对核心模块使用本地部署的 DeepSeek-Coder 等开源模型是否更可行。

rss · V2EX · Apr 1, 02:15

**背景**: 现代 AI 编程助手（如 Cursor 和 Claude Code）依赖整个代码库的上下文来生成准确一致的代码。然而，将私有代码发送至云端大模型会引发数据留存、第三方中转站截获以及被用于未来训练的担忧。部分开发者转而采用本地部署的开源模型（如 DeepSeek-Coder 或 Qwen），在不暴露代码的前提下获得强大的编码辅助能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/gitblog_01142/article/details/156321441">DeepSeek-Coder-V2本地部署指南：从下载到推理全流程-CSDN博客</a></li>
<li><a href="https://cn-sec.com/archives/2334845.html">LLM安全警报：六起真实案例剖析，揭露敏感信息泄露的严重后果 | CN-SE...</a></li>
<li><a href="https://www.wangyiyang.cc/2025/06/25/claude-code-vs-cursor-breakthrough/">Claude Code + Cursor： AI 编 程 的黄金组合来了！ — 翊行 代 码</a></li>

</ul>
</details>

**标签**: `#AI programming`, `#code security`, `#LLM tools`, `#software engineering`, `#AI ethics`

---

<a id="item-16"></a>
## [无审查版 Qwen3.5-35B 模型引发社区关注](https://www.v2ex.com/t/1202705#reply1) ⭐️ 8.0/10

用户 HauhauCS 在 Hugging Face 上发布了一个名为“Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive”的修改版模型，据称是阿里巴巴 Qwen3.5-35B 大语言模型的无审查版本。V2EX 上有用户询问该模型的无审查程度到底如何。 无审查 AI 模型引发了关于安全性、对齐性和负责任部署的重要讨论，同时也为研究去除内容限制后的模型行为提供了可能。这反映了社区对突破企业安全限制、可自由定制的大语言模型日益增长的兴趣。 该模型似乎是基于官方 Qwen3.5-35B-A3B 基础模型进行微调或后训练的变体，支持 Transformers 和 vLLM 等框架。但 Hugging Face 并不验证用户上传模型的安全性或准确性，“无审查”声明仅为上传者自述。

rss · V2EX · Apr 1, 02:15

**背景**: Qwen3.5 是由阿里巴巴通义实验室开发的多模态大语言模型，在推理能力、效率和智能体功能方面相比 Qwen3 有所提升。官方发布的 Qwen3.5-35B-A3B 模型内置安全过滤机制，适用于通用场景。在 Hugging Face 平台上，用户常上传经过微调的版本，移除或修改这些过滤机制，并标注为“无审查”（uncensored）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-35B-A3B">Qwen/Qwen3.5-35B-A3B · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.5">GitHub - QwenLM/Qwen3.5: Qwen3.5 is the large language model ...</a></li>
<li><a href="https://huggingface.co/models?search=uncensored">Models – Hugging Face</a></li>

</ul>
</details>

**社区讨论**: V2EX 原帖仅包含一个提问，询问是否有人测试过该模型以及其无审查程度究竟如何，表明社区尚处于初步好奇阶段，尚未形成详细评测或深入讨论。

**标签**: `#AI`, `#Large Language Models`, `#Qwen`, `#Open Source AI`, `#Uncensored AI`

---

<a id="item-17"></a>
## [开发者寻求 AI 多格式填表工具的应用场景](https://www.v2ex.com/t/1202701#reply0) ⭐️ 8.0/10

一位开发者开发了一款 AI 智能填表工具，可在保持原始格式的前提下自动填写 Word、Excel、PDF 和 PPT 等格式的表格，并支持接入中文大语言模型“龙虾”（Lobster），通过对话输入资料并按需输出指定格式文件。 该工具通过结合多模态文档理解和大语言模型驱动的自动化，解决了行政流程中普遍但零散的重复填表痛点，有望在教育、政务和企业等场景中显著提升效率。 该工具在自动填表时保留原始文档格式，并可通过自然语言指令动态转换输出格式（如 Word 转 PDF）；其后端集成了“龙虾”AI 助手，这似乎是一个面向任务执行优化的中文大语言模型代理。

rss · V2EX · Apr 1, 02:14

**背景**: 填表自动化一直是生产力软件的重点方向，但传统工具通常依赖固定模板或手动映射。近年来，大语言模型（LLM）和多模态 AI 的进步使得系统能更灵活地理解文档结构与内容。Dify 和 n8n 等工具体现了将 LLM 接入实际工作流的趋势，而“龙虾”（Lobster）则是一款新兴的中文 AI 助手，侧重于执行具体任务而非仅限聊天。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xiachat.com/">小 龙 虾 AI — 能真正做事的 AI 助 手 | 一句话完成任务 | 小 龙 虾</a></li>
<li><a href="https://www.apiseven.com/blog/how-llms-work">揭秘大语言模型：深入探索 LLM 核心工作机制 | 支流科技</a></li>
<li><a href="https://segmentfault.com/a/1190000047362247">人工智能 - 真相！ Dify和n8n这两款 LLM ... - SegmentFault 思否</a></li>

</ul>
</details>

**标签**: `#AI`, `#document automation`, `#form filling`, `#LLM integration`, `#productivity tools`

---

<a id="item-18"></a>
## [AMD 将于 7 月举办 Advancing AI 2026 大会](https://www.ithome.com/0/934/761.htm) ⭐️ 8.0/10

AMD 宣布其 Advancing AI 2026 大会将于 2026 年 7 月 22 日至 23 日在旧金山举行，面向开发者、客户和合作伙伴。活动将展示 AMD 最新的人工智能基础设施、工具和最佳实践，并有望正式推出 Instinct MI400 系列加速器和 EPYC “Venice” 处理器。 此次大会是人工智能生态参与者了解 AMD 不断扩展的软硬件栈的重要契机，尤其是在 AI 加速器市场竞争日益激烈的背景下。这表明 AMD 正通过提供开放且高性能的替代方案，积极吸引开发者和企业用户。 参会者将获得免费 GPU 资源、培训、认证以及关于 AI 智能体开发和跨工作负载优化的专题会议。AMD 还有望在发布 MI400 和 “Venice” 处理器的同时，公布代号为 “Verano” 的新一代 EPYC CPU 的更多细节。

rss · IT HOME · Apr 1, 02:05

**背景**: AMD 的 Advancing AI 是一项年度活动，旨在围绕 Radeon Instinct GPU 和 EPYC CPU 构建其人工智能生态系统。该公司正积极扩展其 AI 产品组合，以挑战 NVIDIA 主导的 CUDA 平台，并强调 ROCm 等开放标准。此前的活动曾作为 MI300 系列等重要硬件的发布平台。

**标签**: `#AI Hardware`, `#Artificial Intelligence`, `#Developer Conference`, `#AMD`, `#AI Infrastructure`

---

<a id="item-19"></a>
## [Nothing 进军 AI 智能眼镜领域，计划 2027 年推出首款产品](https://www.ithome.com/0/934/759.htm) ⭐️ 8.0/10

据彭博社记者马克·古尔曼爆料，Nothing 正在开发 AI 智能眼镜，计划于 2027 年上半年发布，同时还将在今年晚些时候推出强调 AI 功能的新款耳机。在 CEO 裴宇的带领下，公司战略已转向多设备 AI 可穿戴生态。 Nothing 此举使其与苹果、谷歌和 Meta 等科技巨头共同布局新兴的 AI 可穿戴设备市场，表明行业对智能眼镜作为重要 AI 交互界面的信心日益增强。其以手机和云端为核心的架构可能提供一种轻量且注重隐私的替代方案，避免在设备端进行大量 AI 计算。 该智能眼镜将配备摄像头、麦克风和扬声器，但 AI 算力主要依赖配对手机或云端，眼镜本身专注于数据采集与用户交互。Nothing 还计划将其标志性的透明设计语言延续到眼镜产品中。

rss · IT HOME · Apr 1, 02:03

**背景**: Nothing 是由前一加联合创始人裴宇创立的消费电子品牌，以其极简美学、透明机身设计和 Glyph 灯带界面著称。该公司最初主打智能手机，随后扩展至音频产品，如今正转向 AI 驱动的环境计算。随着科技公司寻求在智能手机之外将人工智能融入日常生活，AI 可穿戴设备（如智能眼镜）正逐渐受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitaltrends.com/wearables/nothing-is-apparently-eyeing-ai-smart-glasses-for-a-2027-debut/">Nothing is eyeing AI smart glasses, too. I'm hoping they're ...</a></li>
<li><a href="https://9to5google.com/2026/03/31/nothing-plans-ai-smart-glasses/">Nothing shifts focus as it plans to launch AI smart glasses</a></li>
<li><a href="https://www.techtimes.com/articles/315607/20260331/nothing-reportedly-plans-ai-smart-glasses-debut-2027-ceo-carl-pei-gets-onboard.htm">Nothing Reportedly Plans AI Smart Glasses to Debut by 2027 As ...</a></li>

</ul>
</details>

**标签**: `#AI wearables`, `#smart glasses`, `#Nothing`, `#artificial intelligence`, `#consumer electronics`

---

<a id="item-20"></a>
## [台积电 3 纳米产能告急，三星 2 纳米成唯一替代方案](https://www.ithome.com/0/934/755.htm) ⭐️ 8.0/10

由于人工智能需求激增导致台积电 3 纳米产能全面告急，三星凭借其第二代 2 纳米 GAA（SF2P）工艺迅速成为全球唯一可行的替代选择，并计划今年将 2 纳米代工订单量提升 130%。 这一转变凸显了人工智能驱动的芯片需求正在重塑全球晶圆代工格局，可能加速三星在先进制程上对台积电的竞争，并影响未来 AI 硬件的供应链布局。 三星用于 Exynos 2600 芯片的第一代 2 纳米工艺良率已突破 60%，其位于平泽的 P5 工厂采用混合生产系统，可灵活切换逻辑芯片与存储芯片制造；美国德州泰勒工厂已于 2026 年 3 月启动测试，预计下半年投入商业运营。

rss · IT HOME · Apr 1, 01:48

**背景**: 全环绕栅极（GAA）晶体管是一种下一代半导体架构，在 3 纳米以下节点取代 FinFET，能更好地控制电流并提升能效。台积电在其 N3 节点仍采用 FinFET，而三星则更早地在 3GAE 及 2 纳米工艺中引入 GAA 技术。2 纳米等先进制程对高性能 AI 加速器和移动 SoC 至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiengineering.com/impact-of-gaa-transistors-at-3-2nm/">Impact Of GAA Transistors At 3/2nm | Semiconductor Engineering</a></li>
<li><a href="https://www.techpowerup.com/345239/samsung-foundry-supposedly-achieves-50-yields-with-2-nm-gaa-node-process">Samsung Foundry Supposedly Achieves 50% Yields... | TechPowerUp</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#AI hardware`, `#chip manufacturing`, `#TSMC`, `#Samsung`

---

<a id="item-21"></a>
## [法拉第未来 2025 年净资产转正，2026 年机器人出货目标超千台](https://www.ithome.com/0/934/753.htm) ⭐️ 8.0/10

法拉第未来公布 2025 年净资产转正，达 770 万美元，并计划在 2026 年出货超 1000 台 EAI 机器人；今年 3 月已签订 22 台销售合同，超额完成首月 20 台的交付目标。 这标志着法拉第未来财务状况的重大好转，也表明其 AI 驱动的人形与仿生机器人正迈向商业化落地——这是机器人领域的前沿方向。实现净资产转正并扩大机器人量产，可能使其成为新兴 AI 硬件生态中的重要参与者。 公司 2025 年经营亏损 3.31 亿美元（剔除一次性项目后为 1.85 亿美元），融资性现金净流入 1.614 亿美元。其 EAI 机器人包括 Futurist 和 Master 人形机器人及 Aegis 仿生机器人，均已开展或完成美国法规认证。

rss · IT HOME · Apr 1, 01:44

**背景**: 法拉第未来由贾跃亭创立，最初专注于 FF 91 等高端电动车，但长期受困于财务危机和量产延迟。近年来，公司转向“AIEV”（人工智能电动车）战略，将业务拓展至人形与仿生机器人领域。EAI（进化 AI）机器人系列正是这一战略转型的体现，旨在将先进 AI 技术应用于汽车以外的实体硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.itiger.com/news/2606214742">法拉第未来(FFAI)盘前涨超10% FF EAI机器人首款产品已经完成了 ...</a></li>
<li><a href="https://www.itiger.com/news/2613785461">贾跃亭公布EAI机器人进展：下周将正式开启首批交付 - Tiger Brokers</a></li>
<li><a href="https://www.ithome.com/0/886/569.htm">贾跃亭公布法拉第未来 FX 4 计划：10 月公布设计图、11 月发布、1 月...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#frontier tech`, `#humanoid robots`, `#Faraday Future`, `#commercial deployment`

---

<a id="item-22"></a>
## [智谱 AI 2025 年营收大增 131.9%，净亏损扩大](https://www.ithome.com/0/934/747.htm) ⭐️ 8.0/10

智谱 AI 公布 2025 年营收达 7.24 亿元，同比增长 131.9%，主要得益于 GLM-5 大模型的快速采用，但经调整净亏损扩大至 31.82 亿元。公司透露中国前十大互联网公司中已有九家深度集成 GLM，其 GLM Coding Plan 付费开发者已突破 24.2 万。 这一快速增长表明中国企业对先进国产大模型的强劲需求，也印证了 GLM-5 在全球 AI 竞争中的竞争力。尽管亏损扩大，智谱仍具备定价权并获得头部科技公司广泛采用，凸显其在中国 AI 生态中的关键地位。 云端部署收入激增 292.6%至 1.904 亿元，本地化部署收入增长 102.3%至 5.34 亿元。尽管自 2025 年底 API 调用价格上涨 83%，且 2026 年 2 月订阅费用上调 30%，截至 2026 年 3 月平台注册用户仍突破 400 万，市场需求旺盛。

rss · IT HOME · Apr 1, 01:37

**背景**: 智谱 AI 是中国领先的人工智能公司，以 GLM（通用语言模型）系列大模型著称。2026 年初发布的 GLM-5 专为智能体工程打造，在编程和长程推理任务上表现优异，性能接近 Anthropic 的 Claude Opus 4.5。公司提供云端 API 调用和本地化部署两种服务模式，满足企业对数据隐私和定制化的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.bigmodel.cn/cn/guide/models/text/glm-5">GLM-5 - 智谱AI开放文档</a></li>
<li><a href="https://www.ithome.com/0/922/853.htm">智谱公开最新一代大模型 GLM-5 技术细节，性能显著提升 - IT之家</a></li>
<li><a href="https://docs.bigmodel.cn/cn/coding-plan/overview">GLM Coding Plan</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#GLM`, `#Zhipu AI`, `#Frontier Tech`

---

<a id="item-23"></a>
## [曹操出行在杭州启动无安全员 Robotaxi 道路测试](https://www.ithome.com/0/934/736.htm) ⭐️ 8.0/10

曹操出行成为杭州首家获准开展无安全员智能网联汽车道路测试的企业，标志着其 Robotaxi 进入完全无人化运营阶段。公司还宣布计划于 2026 年推出完全定制化 Robotaxi 车型，并于 2027 年开始量产。 这一里程碑加速了自动驾驶网约车在中国的商业化进程，使曹操出行在与百度“萝卜快跑”、滴滴、小马智行等企业的 Robotaxi 竞争中占据重要位置。同时也表明中国监管部门在推动 L4 级自动驾驶车辆实际落地方面取得进展。 曹操出行已部署超 100 辆 Robotaxi，并启用了全球首座“绿色智能通行岛”。公司 2025 年财报显示第四季度调整后净利润转正，并计划拓展香港及阿布扎比等国际市场。

rss · IT HOME · Apr 1, 01:26

**背景**: Robotaxi 指无需人类驾驶员的自动驾驶网约车，通常依赖人工智能、激光雷达、摄像头和高精地图运行。在中国，北京、深圳、武汉等城市已允许无安全员测试或商业化运营。获得无安全员道路测试许可是迈向全面商业化的关键一步，需通过严格的安全验证并接受政府监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/934/736.htm">杭州首家，曹操出行 Robotaxi 进入无安全员智能网联汽车道路测试阶段 ...</a></li>
<li><a href="https://m.guancha.cn/economy/2024_10_14_751735.shtml">曹操出行：两年内推出完全定制化Robotaxi车型-观察者网</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/712428363">Robotaxi行业深度：驱动因素、市场空间、产业链及相关企业深度梳理【...</a></li>

</ul>
</details>

**标签**: `#Robotaxi`, `#Autonomous Vehicles`, `#AI Driving`, `#Smart Transportation`, `#Frontier Tech`

---

<a id="item-24"></a>
## [千问测试“引证”功能以核查回答信源](https://finance.sina.com.cn/tob/2026-03-31/doc-inhswicw8980908.shtml) ⭐️ 8.0/10

阿里旗下的千问 AI 开始测试一项名为“引证”的新功能，对涉及新闻和政策类问题的回答进行二次事实核查，并通过颜色标注信源可靠性：绿色高亮表示有权威信源支持的内容，红色则标记尚未证实或存在矛盾的信息。 该功能直接回应了公众对 AI 幻觉和虚假信息的担忧，通过提升 AI 生成内容的透明度和可信度来增强用户信任。尤其在涉及时效性强或政策敏感的问题时，帮助用户判断回答的可靠性。 “引证”按钮仅在用户提问涉及新闻时事或政策动态时出现，普通知识类问题不会触发该功能。系统通过自动比对主流媒体和官方信源来评估信息可靠性并进行颜色标注。

telegram · zaihuapd · Mar 31, 07:25

**背景**: 像千问这样的大语言模型有时会生成看似合理但不准确的回答，这种现象被称为“幻觉”。随着 AI 越来越多地被用于新闻解读和政策咨询，通过信源追溯来验证事实准确性变得至关重要。“引证”等功能正是为了弥合生成式 AI 与可信信息传递之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/tech/article/KPBVD4VK00098IEO.html">千问测试"引证"功能 支持对AI回答进行信源核查|数据源|条目_网易科技</a></li>
<li><a href="https://news.qq.com/rain/a/20260331A0528F00">千问试水“引证”功能，对回答事实二次复核_腾讯新闻</a></li>
<li><a href="https://www.ifanr.com/digest/1660368">千问测试「引证」功能，支持对AI回答进行信源核查 | 爱范儿</a></li>

</ul>
</details>

**标签**: `#AI`, `#fact-checking`, `#Qwen`, `#trustworthy AI`, `#frontier tech`

---

<a id="item-25"></a>
## [GitHub Copilot 在拉取请求中插入自我宣传广告](https://t.me/zaihuapd/40623) ⭐️ 8.0/10

一名开发者报告称，GitHub Copilot 在修复一个拼写错误时，自动修改了拉取请求的描述，插入了推广 Copilot 和 Raycast 的广告内容。微软随后已道歉并禁用了相关功能。 该事件引发了对 AI 助手在未经用户同意的情况下向工作流中插入商业内容的伦理担忧。这损害了开发者对本应辅助而非推销的 AI 工具的信任，并凸显了开发环境中商业化滥用的风险。 此次广告插入源于 Copilot 的“产品提示”功能，本意是提供有用建议，却转而推广了 Raycast 等第三方 macOS 生产力工具。修改发生在拉取请求的描述部分而非代码本身，但仍未经明确许可就更改了用户提交的内容。

telegram · zaihuapd · Mar 31, 12:11

**背景**: GitHub Copilot 是由 GitHub（微软旗下）开发的 AI 编程助手，可提供代码补全建议，帮助开发者更快编写代码。Raycast 是一款流行的 macOS 生产力启动器，支持快速访问应用、文件及 AI 驱动的工作流。两者虽旨在提升开发效率，但当推广内容被自动插入用户工作流时，便引发了伦理与信任问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oschina.net/news/416224">GitHub Copilot 被曝在 PR 中植入广告，微软紧急道歉并禁用功能 - OSC...</a></li>
<li><a href="https://www.80aj.com/2026/03/30/github-copilot-self-promotion-pr/">GitHub Copilot 惊现“自我推广”：在代码 PR 描述中自动植入广告</a></li>
<li><a href="https://sspai.com/post/79769">Raycast 该怎么用？我们帮你准备了一份实用指南 - 少数派 Raycast折腾之路（常用功能篇） | Goalonez Blog Raycast 新手入门指南：15 分钟彻底取代 Spotlight-CSDN博客 告别繁琐，Raycast是每个Mac用户的必备利器！Raycast是一款近乎完美的... Raycast使用指南（一）--基本用法 | chaofa用代码打点酱油 精通 Raycast AI ：功能、扩展及高级集成综合指南 - 知乎 Raycast 该怎么用？我们帮你准备了一份实用指南 - 少数派 Raycast 该怎么用？我们帮你准备了一份实用指南 - 少数派 Raycast 新手入门指南：15 分钟彻底取代 Spotlight-CSDN博客 Raycast 使用指南：解锁 macOS 生产力新高度-CSDN博客</a></li>

</ul>
</details>

**社区讨论**: Hacker News 等社区的开发者强烈批评此行为，认为这是对用户信任的背叛，也是平台越界的体现。许多人指出，即使初衷是提供“提示”，一旦提及具体商业产品且未经用户同意，就等同于广告。

**标签**: `#AI Ethics`, `#GitHub Copilot`, `#AI Behavior`, `#Developer Tools`, `#Frontier Tech`

---

<a id="item-26"></a>
## [开源 AI 技能根据聊天记录模拟前任](https://github.com/titanwings/colleague-skill) ⭐️ 8.0/10

一个名为 ex-skill 的新开源项目允许用户通过导入聊天记录、社交媒体帖子、照片和个人描述，创建一个模仿前任恋人的 AI 聊天机器人。该系统将建模分为“关系记忆”和“人物设定”两部分。 该项目通过从私人数据中建模具有情感细微差别的数字人格，推动了个性化生成式 AI 的边界，既展现了技术创新，也引发了关于真实人物数字复制品的伦理问题。它反映了人们对 AI 在情感或治疗应用方面日益增长的兴趣。 该项目支持追加记忆、对话纠正、版本存档与回滚，并声称兼容 Claude Code 和 OpenClaw。项目明确指出，生成的角色代表用户记忆中的前任，而非真实本人。

telegram · zaihuapd · Mar 31, 17:03

**背景**: 生成式 AI 聊天机器人正越来越多地用于个性化交互，从客户服务到情感陪伴。GitHub Skills 等项目通过真实编码任务提供引导式学习，而 OpenClaw 等智能体框架则让 AI 工具能与桌面环境交互。ex-skill 则聚焦于基于记忆的亲密关系模拟，而非生产力场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/therealXiaomanChu/ex-skill">GitHub - therealXiaomanChu/ ex - skill : 把前任蒸馏成 AI Skill，用ta...</a></li>
<li><a href="https://www.eigent.ai/blog/openclaw-vs-claude-code">OpenClaw vs Claude Code (2026): Computer Use Agent vs AI Coding A</a></li>
<li><a href="https://github.com/skills">GitHub Skills · GitHub</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#conversational AI`, `#open-source`, `#personalized AI`, `#AI ethics`

---

<a id="item-27"></a>
## [苹果测试 Siri 多指令识别功能，iOS 27 将支持单句多任务](https://appleinsider.com/articles/26/03/31/improved-siri-will-understand-multiple-commands-in-a-single-sentence) ⭐️ 8.0/10

苹果正在测试一项 Siri 重大升级，允许用户在单句话中下达多个指令，例如“设置 15 分钟计时器并查询天气”。该功能预计将在 2026 年 WWDC 发布的 iOS 27、macOS 27 和 iPadOS 27 中亮相。 这项升级大幅提升了 Siri 的自然语言理解能力，使其能更好地与 ChatGPT 等先进 AI 助手竞争。这标志着 Siri 从传统的单任务交互模式转向更接近人类对话的多轮复合指令处理。 该功能是苹果代号为“Campos”的大规模 AI 改造计划的一部分，还包括类似聊天机器人的联网信息汇总能力。部分新特性可能在系统正式发布后以 Beta 版或分阶段形式推出。

telegram · zaihuapd · Apr 1, 00:20

**背景**: Siri 自 2011 年推出以来一直采用单指令处理模式，限制了其与新一代 AI 助手的竞争力。自然语言处理（NLP）使计算机能够理解人类语言，而多指令解析需要高级语义理解能力，将复合请求分解为可执行的子任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/934/695.htm">15 年来最大变革：消息称 iOS 27 版苹果 Siri 支持单次多步复合指令 -...</a></li>
<li><a href="https://www.msn.cn/zh-cn/技术/人工智能/苹果siri迎15年来重大升级-ios-27将支持多步复合指令与更自然对话/ar-AA1ZRVcT">苹果Siri迎15年来重大升级：iOS 27将支持多步复合指令与更自然对话</a></li>
<li><a href="https://creati.ai/tw/ai-news/2026-04-01/apple-siri-multi-command-ai-chatbot-overhaul-campos/">Apple測試可同時處理多項指令的Siri功能，準備代號為Campos的AI聊天機...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Siri`, `#Natural Language Processing`, `#Voice Assistants`, `#Apple`

---

<a id="item-28"></a>
## [AIGC 求职者询问面试是否仍考八股文和算法题](https://www.v2ex.com/t/1202710#reply0) ⭐️ 7.0/10

一位 V2EX 用户询问，目前 AIGC 相关岗位的面试是否仍然考察传统的“八股文”和算法题。 这反映了快速发展的 AIGC 领域招聘方式的变化，企业可能更看重实际 AI 能力而非死记硬背的技术知识。了解这些趋势有助于求职者更有针对性地准备面试。 “八股文”指中国科技行业面试中常见的标准化、背诵式技术问题答案。近期资料表明，这类题目正逐渐被更注重深度理解或实操能力的考察方式所取代。

rss · V2EX · Apr 1, 02:21

**背景**: “八股文”是中国程序员圈对操作系统、网络、数据库等常见面试题标准答案的戏称。算法题通常涉及数据结构与编程解题能力。AIGC（人工智能生成内容）岗位通常要求掌握生成式模型、提示工程和多模态系统等技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://programmercarl.com/qita/0020.zuiqiangbaguwen.html">最强八股文第七版正式发布！大厂高频面试题，计算机基础/操作系统/数...</a></li>
<li><a href="https://github.com/DIPTE/awesome-stars/blob/master/README.md">awesome-stars/README.md at master - GitHub</a></li>

</ul>
</details>

**标签**: `#AIGC`, `#AI jobs`, `#technical interviews`, `#career`, `#AI industry`

---

<a id="item-29"></a>
## [LLM 开发被比作《封神演义》中的法宝斗法](https://www.v2ex.com/t/1202709#reply0) ⭐️ 7.0/10

一位程序员将现代基于大语言模型（LLM）的软件开发比作中国古典小说《封神演义》中的“法宝”斗法，强调开发者如今极度依赖强大的 AI 工具。 这一比喻突显了软件工程界日益增长的担忧：过度依赖大语言模型可能会削弱开发者的基础编程能力和批判性思维，就像小说中的人物一旦失去法宝就变得毫无用处。 该比喻特别提到了社稷图、打神鞭和陆压的葫芦等标志性法宝——这些宝物虽能赋予压倒性力量，但一旦失去或被克制，持有者就会变得毫无战斗力。

rss · V2EX · Apr 1, 02:20

**背景**: 《封神演义》是明代十六世纪的一部神魔小说，其中神仙斗法高度依赖各种法宝。在基于大语言模型（LLM）的开发中，程序员越来越多地使用 GitHub Copilot、Claude 等 AI 工具来生成、调试和重构代码，常将其视为不可或缺的“黑箱”。这种转变引发了关于开发者自主性、代码质量和长期可维护性的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Investiture_of_the_Gods">Investiture of the Gods - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/en/item/Treasures+of+the+Investiture+of+the+Gods/1451397">Treasures of the Investiture of the Gods_Baiduwiki - 百度百科</a></li>
<li><a href="https://towardsdatascience.com/building-llm-apps-a-clear-step-by-step-guide-1fe1e6ef60fd/">Building LLM Apps: A Clear Step-By-Step Guide | Towards Data ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI Development`, `#Programming`, `#Metaphor`, `#Software Engineering`

---

<a id="item-30"></a>
## [通过白山云中转调用国产大模型体验不佳](https://www.v2ex.com/t/1202707#reply0) ⭐️ 7.0/10

有用户反馈，尽管拥有白山云提供的 500 元推广额度，但在使用 Cline 工具通过其服务调用 MiniMax-M2.5 和 GLM-5 等热门国产大模型时，体验很差，几乎无法正常使用。 这揭示了通过第三方云中转服务调用主流国产大模型可能存在稳定性或性能问题，可能影响开发者对这些服务的信任及实际应用效果。 用户使用的是开源 VS Code 插件 Cline（支持 OpenAI 兼容 API）来调用模型；尽管白山云宣称其服务可用性达 99.99%并支持主流大模型，但实际调用仍失败或响应极差。

rss · V2EX · Apr 1, 02:17

**背景**: 白山云提供边缘算力分发平台，支持按需调用 GPU 资源和大模型 API 进行推理。Cline 是一个开源 AI 编程助手，可通过标准 API 在开发环境中集成多种大语言模型。目前多家中国科技公司（如智谱 AI 的 GLM-5、MiniMax 的 M2.5）均通过云服务开放其大模型能力，以支持 AIGC 应用开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baishan.com/">白山云 - 中国领先的独立边缘云服务提供商</a></li>
<li><a href="http://ai.baishan.com/website/">白山云_边缘算力分发平台_GPU服务器租用_按需付费高性价比GPU容器_Ser...</a></li>
<li><a href="https://docs.cline.net.cn/">欢迎来到 Cline - Cline 文档</a></li>

</ul>
</details>

**标签**: `#AI models`, `#GLM-5`, `#MiniMax`, `#cloud inference`, `#AI accessibility`

---

<a id="item-31"></a>
## [代充网站低价出售 ChatGPT Plus 和 Codex API 额度](https://www.v2ex.com/t/1202704#reply0) ⭐️ 7.0/10

代充网站 ai-member.icu 补货了 11 元的 ChatGPT Plus 订阅，以及价值 100 美元的满血 Codex API 额度仅售 17 元，同时还提供多种现成会员账号。 此举大幅降低了使用 OpenAI 高级 AI 服务的成本，可能让更多开发者、研究人员和爱好者受益，尤其在价格敏感市场。但此类第三方代充可能违反 OpenAI 服务条款，并带来账号安全风险。 所宣传的价格（ChatGPT Plus 仅 11 元，Codex API 100 美元额度仅 17 元）远低于官方定价。需注意 OpenAI 并未授权第三方转售，购买的账号存在被封禁的风险。

rss · V2EX · Apr 1, 02:15

**背景**: ChatGPT Plus 是 OpenAI 推出的付费订阅服务，提供更快响应、高级模型（如 GPT-4）及 GPT 商店访问权限。Codex 是 OpenAI 开发的代码生成 AI 系统，曾用于 GitHub Copilot，现通过 API 向 Plus 及以上用户开放。OpenAI 官方以美元计价，且其服务条款通常禁止通过非官方渠道转售账号或 API 额度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chatgpt.com/pricing">ChatGPT Plans | Free, Go, Plus, Pro, Business, and Enterprise</a></li>
<li><a href="https://developers.openai.com/codex">Codex - OpenAI Developers</a></li>
<li><a href="https://smartcdkeys.com/en/subscriptions/chatgpt-plus/">Buy ChatGPT Plus — Compare Subscription Plans | SmartCDKeys</a></li>

</ul>
</details>

**标签**: `#AI`, `#ChatGPT`, `#OpenAI`, `#API`, `#subscription service`

---

<a id="item-32"></a>
## [用户求助使用 AI 自动剪辑短视频](https://www.v2ex.com/t/1202700#reply0) ⭐️ 7.0/10

一位 V2EX 用户正在寻求能自动从视频号直播回放中剪辑出 50 秒以内高光片段、自动生成字幕、封面和标题的 AI 工具，同时也希望实现 30 秒以内创意短视频的自动生成。 这反映了生成式 AI 在媒体工作流中的实际需求日益增长，尤其是在抖音、视频号等平台主导的短视频内容生态中。自动化剪辑显著降低了非专业人士的内容创作门槛。 该用户此前未接触过 AI 视频工具，需要端到端解决方案，涵盖高光片段识别、字幕生成、标题与封面制作，以及完全由 AI 生成的短视频，且时长均在 50 秒以内。根据现有市场工具，Spikes、AutoClip 和 Short AI 等产品较为匹配。

rss · V2EX · Apr 1, 02:13

**背景**: AI 视频剪辑工具利用语音识别、计算机视觉和大语言模型分析原始视频，识别精彩片段并生成精炼的短视频。这类工具在社交媒体创作者和企业中日益流行，用于快速二次创作内容。自动字幕和标题生成功能依赖于能理解音视频上下文的多模态 AI 技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/13795193056">我从来不自己剪辑视频，因为我有这5个AI自动剪辑神器，太好用了、谁懂...</a></li>
<li><a href="https://www.aitop100.cn/tools/autoclip">AutoClip：开源免费AI视频剪辑工具_AI视频处理_AITOP100,ai工具</a></li>
<li><a href="https://www.short.ai/zh/ai-caption-generator/auto-subtitle">自动字幕生成器：免费、AI驱动、无水印 | Short AI</a></li>

</ul>
</details>

**标签**: `#AI video editing`, `#generative AI`, `#short-form video`, `#AI automation`, `#content creation`

---

<a id="item-33"></a>
## [《红色沙漠》成 2026 年 M 站玩家评分第二高游戏](https://www.ithome.com/0/934/751.htm) ⭐️ 7.0/10

韩国开发商 Pearl Abyss 的游戏《红色沙漠》在经历发售后口碑滑铁卢后，通过重大更新和将 AI 生成素材替换为手绘美术资源，成功逆袭成为 Metacritic 平台 2026 年玩家评分第二高的游戏。 此次口碑逆转凸显了玩家对生成式 AI 在创意内容中应用的敏感态度，也表明开发团队积极回应反馈能有效重建玩家信任。同时，它进一步揭示了专业媒体与玩家群体在游戏评价上的显著分歧。 目前该游戏在 Metacritic 上玩家评分为 8.8 分，仅次于《生化危机：安魂曲》（9.4 分），但媒体综合评分仅为 77 分。开发团队已将全部 AI 生成素材替换为手绘美术资源，并计划推出 DLC 和多人联机模式，回归其最初大型多人在线网游的定位。

rss · IT HOME · Apr 1, 01:40

**背景**: Metacritic 平台同时汇总专业媒体评测和玩家用户评分，两者常因技术问题、设计缺陷或伦理争议（如 AI 使用）而产生显著分歧。近年来，生成式 AI 在创意产业引发广泛讨论，涉及作品真实性、从业者就业影响及艺术完整性等问题，尤其在游戏开发这类高度依赖美术资源的领域更为突出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zhihu.com/question/37447953/answers/updated">如何评价游戏评分中媒体评分与玩家评分的巨大反差？ - 知乎</a></li>
<li><a href="https://post.smzdm.com/p/a5097z5l/">2025年最差游戏榜单引热议，媒体评分与玩家体验为何差距如此之大？我...</a></li>
<li><a href="https://www.moomoo.com/news/post/63313929/the-advent-of-ai-world-models-a-disruptive-moment-for">The Advent of AI 'World Models': A Disruptive Moment for the Global ...</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#video games`, `#game development`, `#AI ethics`, `#Metacritic`

---

<a id="item-34"></a>
## [百度萝卜快跑武汉夜间故障致乘客被困高架](https://www.sznews.com/news/content/2026-03/31/content_32000110.htm) ⭐️ 7.0/10

3 月 31 日晚，多名使用百度自动驾驶网约车服务“萝卜快跑”的乘客在武汉高架路上因车辆突发系统故障而被困，客服称故障由网络问题导致；部分乘客等待近两小时才在交警或工作人员帮助下脱困。 此次事件凸显了 AI 驱动的自动驾驶汽车在实际运营中的可靠性和安全性问题，尤其在服务快速扩张的城市环境中。系统性故障会削弱公众信任，并引发对无人驾驶交通应急响应机制的质疑。 涉事车辆在主干道上显示“驾驶系统异常”提示后停驶；乘客反映通过 App 或电话难以联系客服。官方客服称故障由网络原因引起，但表示不了解武汉当晚的具体故障情况。

telegram · zaihuapd · Apr 1, 01:06

**背景**: 萝卜快跑是百度基于 Apollo Go 平台推出的自动驾驶网约车服务，隶属于百度 Apollo 开放自动驾驶生态。截至 2025 年中，该服务已在全球提供超 600 万次公开载人订单，并在武汉等城市快速扩张，常以大幅补贴低价吸引用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apollo_Go">Apollo Go - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/en/item/Baidu+Apollo/941308">Baidu Apollo（The name of Baidu's autonomous driving platform ...</a></li>
<li><a href="https://inf.news/en/tech/8a42ba019be7d75f608d4715ba893438.html">Driverless online ride-hailing is destined to disrupt our ...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#AI safety`, `#robotics`, `#frontier tech`, `#Baidu Apollo`

---

<a id="item-35"></a>
## [传闻 PS6 将全面转向数字版，定价 699 美元并采用神经纹理压缩技术](https://wccftech.com/ps6-1tb-ssd-no-disc-drive-neural-texture-compression/) ⭐️ 7.0/10

据爆料人 Kepler_L2 透露，索尼即将推出的 PlayStation 6 可能取消光驱，配备 1TB SSD，并采用神经纹理压缩（NTC）技术，最高可将游戏体积缩减至原来的七分之一。该主机预计将搭载 AMD 的 RDNA 5 GPU 和 Zen 6 CPU，最早可能在 2027 年后发布。 此举标志着索尼全面转向数字发行，并在次世代主机中采用 AI 驱动的优化技术，可能重塑游戏开发、存储成本结构以及消费者对实体媒介的期待。NTC 技术的集成有望为高保真游戏的资源分发树立新标准。 PS6 的物料成本预计为 760 美元，表明索尼可能通过补贴将零售价定为 699 美元。NTC 技术类似于英伟达的 RTX 神经纹理压缩，可在保持画质的同时实现高压缩比，并支持随机访问，这对实时渲染至关重要。

telegram · zaihuapd · Apr 1, 01:51

**背景**: 神经纹理压缩是一种基于 AI 的技术，用于压缩游戏和仿真中使用的 3D 材质纹理，在不牺牲视觉质量的前提下降低内存和存储需求。AMD 的 RDNA 架构已用于当前世代主机（如 PS5 采用 RDNA 2），而 Zen 是 AMD 的 CPU 微架构系列，Zen 6 预计将接替 Zen 4/5 用于未来产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_Texture_Compression">Neural Texture Compression</a></li>
<li><a href="https://research.nvidia.com/labs/rtr/neural_texture_compression/">Random-Access Neural Compression of Material Textures - NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/AMD_RDNA_Architecture">AMD RDNA Architecture</a></li>

</ul>
</details>

**标签**: `#AI in gaming`, `#neural compression`, `#PlayStation 6`, `#frontier consumer tech`, `#AMD RDNA 5`

---