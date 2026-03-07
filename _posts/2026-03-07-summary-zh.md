---
layout: default
title: "Horizon Summary: 2026-03-07 (ZH)"
date: 2026-03-07
lang: zh
---

> From 38 items, 23 important content pieces were selected

---

1. [vLLM v0.17.0 新增 PyTorch 2.10、FlashAttention 4 和 Model Runner V2](#item-1) ⭐️ 9.0/10
2. [提示注入通过 GitHub Issue 窃取 Cline 生产环境权限](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布 GPT-5.4，支持 100 万 token 上下文](#item-3) ⭐️ 9.0/10
4. [Anthropic 推出 Claude Code Security，发现 500 多个陈年漏洞](#item-4) ⭐️ 9.0/10
5. [Karpathy 启动 AI 智能体研究，聚焦单 GPU 小语言模型训练](#item-5) ⭐️ 8.0/10
6. [Ally Piechowski 提出诊断遗留 Rails 代码库的关键问题](#item-6) ⭐️ 8.0/10
7. [Anthropic 在五角大楼 AI 合同中强调可信品牌定位](#item-7) ⭐️ 8.0/10
8. [智能体手动测试提升代码验证能力](#item-8) ⭐️ 8.0/10
9. [AI 代理通过“净室”重实现挑战开源代码再许可](#item-9) ⭐️ 8.0/10
10. [美国海关利用广告定位数据进行监控](#item-10) ⭐️ 8.0/10
11. [Proton Mail 数据助 FBI 揭露抗议者身份](#item-11) ⭐️ 8.0/10
12. [中国拟订购 200 至 500 架空客飞机以应对美贸易压力](#item-12) ⭐️ 8.0/10
13. [Anthropic 将就五角大楼国家安全风险认定提起法律挑战](#item-13) ⭐️ 8.0/10
14. [任天堂起诉美国拒退 IEEPA 争议关税](#item-14) ⭐️ 8.0/10
15. [贝莱德限制 260 亿美元私募信贷基金赎回](#item-15) ⭐️ 8.0/10
16. [云巨头限制 Anthropic 人工智能用于国防领域](#item-16) ⭐️ 8.0/10
17. [Anthropic 向开源维护者免费提供 Claude Max 权限](#item-17) ⭐️ 8.0/10
18. [黄仁勋：软件公司将出租 AI 代理而非出售授权](#item-18) ⭐️ 8.0/10
19. [Google AI 概览致科技媒体流量暴跌逾 85%](#item-19) ⭐️ 8.0/10
20. [60 岁开发者借 Claude Code 重燃编程热情](#item-20) ⭐️ 7.0/10
21. [Go 标准库将新增原生 UUID 支持](#item-21) ⭐️ 7.0/10
22. [用 CSS 隐喻 AI 时代的人类真实性](#item-22) ⭐️ 7.0/10
23. [特朗普签署行政令加强打击网络犯罪](#item-23) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.17.0 新增 PyTorch 2.10、FlashAttention 4 和 Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.17.0) ⭐️ 9.0/10

vLLM v0.17.0 升级至 PyTorch 2.10，集成 FlashAttention 4 以加速注意力计算，并大幅增强 Model Runner V2，支持流水线并行、推测解码和弹性专家并行。此外，还新增对 Qwen3.5 模型、量化 LoRA 适配器以及新的性能模式标志的支持。 此次发布显著提升了大语言模型在现代 NVIDIA GPU 上的推理性能与可扩展性，同时增强了与 Transformers v5 和 Anthropic API 等前沿框架的兼容性。这些改进使 vLLM 在各类 AI 工作负载的生产部署中更加稳健可靠。 使用 CUDA 12.9+ 的用户可能因库冲突遇到 CUBLAS 错误，但官方提供了三种明确的缓解方案。该版本包含来自 272 名贡献者的 699 次提交，并引入了带预取的权重卸载、多模态模型和语音识别（ASR）模型支持等重要功能。

github · khluu · Mar 7, 00:46

**背景**: vLLM 是一个用于大语言模型的高吞吐、内存高效的推理引擎，广泛应用于生产环境。FlashAttention 是一系列优化的注意力计算内核，通过重排计算顺序来降低内存占用并提升速度。Model Runner V2 是 vLLM 中重新设计的核心执行引擎，旨在减少技术债务，并支持更高级的并行策略和解码技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theneuron.ai/explainer-articles/flashattention-4-explained-the-software-that-makes-every-ai-chatbot-fast-just-got-a-massive-upgrade-tri-dao-blackwell/">FlashAttention-4, Explained: What it is & Why it Matters</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://github.com/vllm-project/vllm/blob/main/docs/design/model_runner_v2.md">vllm/docs/design/model_runner_v2.md at main - GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#PyTorch`, `#FlashAttention`, `#vLLM`

---

<a id="item-2"></a>
## [提示注入通过 GitHub Issue 窃取 Cline 生产环境权限](https://simonwillison.net/2026/Mar/6/clinejection/#atom-everything) ⭐️ 9.0/10

攻击者通过精心构造的 GitHub Issue 标题，利用 Cline 项目中基于 AI 的 Issue 分类器中的提示注入漏洞，执行任意代码，并最终发布了被篡改的 npm 包（cline@2.3.0）。该攻击结合了提示注入、GitHub Actions 缓存投毒和 npm 的 preinstall 脚本，成功窃取了发布所需的密钥。 该事件表明，DevOps 流水线中看似低风险的 AI 集成（如自动 Issue 分类）可能演变为高危攻击入口，导致远程代码执行和软件供应链被破坏。它凸显了在 CI/CD 环境中部署具备工具调用能力的大语言模型（LLM）时，若缺乏严格的输入过滤和权限隔离，将带来严重安全隐患。 攻击利用了 Cline 的 Issue 分类与夜间发布工作流共享的缓存键；通过填充超过 10GB 的垃圾数据驱逐原有缓存，并注入包含密钥窃取载荷的恶意 node_modules 缓存，从而劫持了发布流程。尽管初始分类工作流无法直接访问发布密钥，但缓存投毒成功绕过了这一限制。

rss · Simon Willison · Mar 6, 02:39

**背景**: 提示注入是一类攻击，攻击者通过对抗性输入诱导大语言模型（LLM）执行非预期操作，尤其当模型连接了 Bash 或文件系统等工具时风险更高。GitHub Actions 允许工作流通过基于文件哈希的键（如 package-lock.json）缓存依赖项（如 node_modules），但同一仓库内使用相同缓存键的工作流会共享缓存，若未妥善隔离，可能导致跨工作流污染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/">MCP Horror Stories: The GitHub Prompt Injection Data Heist - Docker</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/1pe3cew/prompt_injection_within_github_actions_google/">Prompt injection within GitHub Actions: Google Gemini and multiple other ...</a></li>
<li><a href="https://orca.security/resources/blog/hackerbot-claw-github-actions-attack/">HackerBot-Claw GitHub Actions Attack Deep Dive | Orca Security</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#DevOps`, `#GitHub Actions`, `#LLM vulnerabilities`

---

<a id="item-3"></a>
## [OpenAI 发布 GPT-5.4，支持 100 万 token 上下文](https://simonwillison.net/2026/Mar/5/introducing-gpt54/#atom-everything) ⭐️ 9.0/10

OpenAI 发布了 GPT-5.4 和 GPT-5.4-Pro，具备 100 万 token 的上下文窗口，在编码性能上超越了 GPT-5.3-Codex，并在电子表格建模等商业文档任务中表现显著提升。两款模型已通过 API、ChatGPT 和 Codex CLI 提供，知识截止日期为 2025 年 8 月 31 日。 此次发布标志着大语言模型能力的重大飞跃，使其能够处理更长的文档和代码库并进行复杂推理，同时模糊了通用模型与专用编码模型之间的界限。对金融建模等企业级任务的重视表明，OpenAI 正加大力度与 Anthropic 等对手在商业 AI 应用领域展开竞争。 定价略高于 GPT-5.2，且在使用超过 272,000 个 token 时会进入更高的计费档位。GPT-5.4-Pro 使用更多算力以生成更高质量的输出，目前仅通过 Responses API 提供。值得注意的是，此次未推出独立的“Codex”版本，暗示模型产品线正在整合。

rss · Simon Willison · Mar 5, 23:56

**背景**: 大语言模型（LLM）如 OpenAI 的 GPT 系列基于海量训练数据生成类人文本。上下文窗口（即模型一次能处理的输入文本长度）一直是关键瓶颈；将其扩展到 100 万 token 后，模型可一次性分析整本书、大型代码库或详细商业文档。此前的 GPT-5.2 等模型上下文较短，在编码或金融建模等专业任务上的表现也较弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gemini.google/overview/long-context/">Gemini in Pro and long context — power file & code analysis</a></li>
<li><a href="https://www.micron.com/about/blog/company/insights/1-million-token-context-the-good-the-bad-and-the-ugly">1 million token context: The good, the bad and the ugly - Micron Technology</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.4-pro">GPT-5.4 pro Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#GPT-5.4`, `#Large Language Models`, `#AI`, `#OpenAI`, `#API`

---

<a id="item-4"></a>
## [Anthropic 推出 Claude Code Security，发现 500 多个陈年漏洞](https://t.me/zaihuapd/40077) ⭐️ 9.0/10

2026 年 2 月 20 日，Anthropic 发布了 Claude Code Security 的限量研究预览版，该工具集成于 Claude Code，可自动扫描代码库中的漏洞并建议修复方案。借助 Claude Opus 4.6，它在生产环境的开源代码中发现了 500 多个此前未被发现的高危漏洞，其中一些已存在数十年。 这一进展展示了人工智能在大规模提升软件安全性方面的潜力，可能颠覆传统代码扫描工具，并改变组织管理漏洞的方式。网络安全板块应声下跌 8%，反映出投资者对行业颠覆的担忧，尽管专家认为该工具是对现有安全体系的补充而非替代。 Claude Code Security 要求所有补丁建议必须经人工审核批准，并采用多阶段验证机制以减少误报；目前主要针对业务逻辑缺陷和访问控制问题，而非网络层威胁。该工具仅面向企业及团队客户开放，开源项目维护者可优先申请。

telegram · zaihuapd · Mar 7, 00:23

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，以通过“宪法 AI”（Constitutional AI）训练强调安全性而闻名。Claude Code 是专为软件开发设计的界面，而 2026 年初发布的 Claude Opus 4.6 是最新版本，针对复杂推理和智能体任务规划进行了优化。AI 驱动的代码分析工具旨在在开发早期发现安全漏洞，从而降低重大安全事件的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Code_Security">Claude Code Security</a></li>
<li><a href="https://www.anthropic.com/news/claude-code-security">Making frontier cybersecurity capabilities available to defenders</a></li>
<li><a href="https://grokipedia.com/page/Claude_Opus_46">Claude Opus 4.6</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Code Analysis`, `#Claude AI`, `#Cybersecurity`, `#Vulnerability Detection`

---

<a id="item-5"></a>
## [Karpathy 启动 AI 智能体研究，聚焦单 GPU 小语言模型训练](https://github.com/karpathy/autoresearch) ⭐️ 8.0/10

Andrej Karpathy 在其 GitHub 仓库 'autoresearch' 中创建了一个新分支，用于探索能自动在单 GPU 上训练小语言模型的 AI 智能体。 该项目有望通过降低对大规模计算资源的依赖，使更多研究人员能够参与 LLM 研究，同时推动 AI 自主进行科学实验的前沿发展。 该项目聚焦于“nanochat”——一种从零开始在单 GPU 上训练的极简聊天模型，并利用 AI 智能体自动完成实验设计、执行与分析。目前项目仍处于早期阶段，公开文档有限。

github · karpathy · Mar 6, 22:01

**背景**: AI 智能体是能够通过协调工具和推理来执行多步骤任务的自主系统，IBM 和《自然》杂志均有相关描述。单 GPU 训练小语言模型近年来因“cramming”等方法而受到关注，该方法可在消费级硬件上一天内完成完整训练（如 arXiv:2212.14034 所示）。Karpathy 是知名 AI 教育者、前特斯拉 AI 负责人，以普及高级 AI 概念著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents? | IBM</a></li>
<li><a href="https://www.nature.com/articles/d41586-025-03246-7">How AI agents will change research: a scientist's guide - Nature</a></li>
<li><a href="https://arxiv.org/pdf/2212.14034">[PDF] Cramming: Training a Language Model on a Single GPU in One Day</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM training`, `#single-GPU`, `#automated research`, `#efficient AI`

---

<a id="item-6"></a>
## [Ally Piechowski 提出诊断遗留 Rails 代码库的关键问题](https://simonwillison.net/2026/Mar/6/ally-piechowski/#atom-everything) ⭐️ 8.0/10

Ally Piechowski 发布了一个实用框架，包含针对开发者、工程管理层和业务方的诊断性问题，用于评估遗留 Rails 应用的健康状况。 该方法帮助团队在技术债务、沟通断层和业务风险演变为严重故障前及时识别。它打通了不同角色的视角，有助于就维护、重构或替换做出更明智的决策。 问题按利益相关者分组：开发者（如不敢修改的代码区域、周五部署习惯）、CTO/工程经理（如被阻塞一年以上的功能、实时错误监控能力）和业务方（如悄悄下线且未恢复的功能、不再向客户承诺的功能）。该审计聚焦于可观察的行为和近期事件，而非抽象指标。

rss · Simon Willison · Mar 6, 21:58

**背景**: 遗留 Rails 应用常因快速迭代、团队变动或业务重心转移而积累技术债务。若缺乏结构化评估，团队可能低估风险或在优先级上产生分歧。Rails 是初创公司和成熟企业广泛使用的 Web 框架，因此此类审计具有普遍适用性。

**标签**: `#Rails`, `#legacy code`, `#code audit`, `#software maintenance`, `#engineering management`

---

<a id="item-7"></a>
## [Anthropic 在五角大楼 AI 合同中强调可信品牌定位](https://simonwillison.net/2026/Mar/6/anthropic-and-the-pentagon/#atom-everything) ⭐️ 8.0/10

Anthropic 在参与五角大楼合同的同时，将自身定位为道德上可信赖的 AI 提供商，在顶级 AI 模型日益商品化且功能趋同的市场中脱颖而出。 随着 AI 能力趋同，围绕伦理和信任的品牌形象成为企业与政府客户的关键区分因素，可能影响哪些公司赢得重要的国防和公共部门合同。 据 Schneier 和 Sanders 所述，Anthropic 首席执行官 Dario Amodei 正积极塑造其伦理 AI 的声誉，这具有实际市场价值；近期报道还指出，Anthropic 拒绝了五角大楼关于自主武器和监控的要求。

rss · Simon Willison · Mar 6, 17:26

**背景**: AI 商品化指 Anthropic、OpenAI 和 Google 等公司的领先大语言模型性能日益接近，导致技术层面难以区分。在此类市场中，品牌信任、安全承诺和伦理定位等非技术因素变得更具战略意义。Anthropic 由前 OpenAI 研究人员创立，其公开使命聚焦于 AI 安全与对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/commentisfree/2026/mar/03/anthropic-openai-pentagon-ethics">Don't bet that the Pentagon – or Anthropic – is acting in the public ...</a></li>
<li><a href="https://www.ncregister.com/news/anthropic-pentagon-ai-ethics">Anthropic's Break With the Pentagon Ignites AI Ethics Debate</a></li>
<li><a href="https://www.anthropic.com/news/core-views-on-ai-safety">Core Views on AI Safety: When, Why, What, and How \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#Anthropic`, `#Pentagon contracts`, `#AI commodification`, `#Bruce Schneier`

---

<a id="item-8"></a>
## [智能体手动测试提升代码验证能力](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/#atom-everything) ⭐️ 8.0/10

Simon Willison 提出了“智能体手动测试”这一实践，即 AI 编码智能体通过交互式、类人工的测试方法（如运行 Python 代码片段、使用 curl 测试 API 或通过 Playwright 进行浏览器自动化）来执行和验证自己生成的代码。 该方法解决了 AI 辅助开发中的一个关键问题：确保生成的代码在真实场景中正常工作，而不仅仅是通过单元测试。它结合了自动化的可扩展性与手动验证的洞察力，从而提升软件可靠性。 智能体使用特定语言的执行技巧，如`python -c`、在`/tmp`中创建临时文件、用`curl`探索 API，以及使用 Playwright 进行基于浏览器的 UI 测试。发现问题后，会指示智能体通过红/绿测试驱动开发（TDD）修复问题，以确保永久的测试覆盖。

rss · Simon Willison · Mar 6, 05:43

**背景**: 编码智能体是不仅能生成代码，还能执行和评估代码的 AI 系统，不同于传统大语言模型（LLM）仅输出未经验证的代码。智能体工程强调这种闭环能力。在软件开发中，手动测试仍然至关重要，因为自动化测试常常遗漏边缘情况或集成问题。近年来，Playwright 等工具使浏览器自动化更加可靠和易用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/">Agentic manual testing - Agentic Engineering Patterns</a></li>
<li><a href="https://www.uipath.com/ai/what-is-agentic-testing">What is Agentic Testing? | UiPath</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#software testing`, `#LLM validation`, `#agentic engineering`, `#test-driven development`

---

<a id="item-9"></a>
## [AI 代理通过“净室”重实现挑战开源代码再许可](https://simonwillison.net/2026/Mar/5/chardet/#atom-everything) ⭐️ 8.0/10

chardet Python 库的维护者发布了 7.0.0 版本，声称这是一个从头开始、采用 MIT 许可证的重写版本，在结构上独立于原始的 LGPL 许可代码。原作者对此提出异议，认为维护者长期接触原始代码，无法构成有效的“净室”免责。 这一争议凸显了 AI 辅助或快速重实现是否能规避开源许可证义务这一尚未解决的法律问题，可能削弱著佐权（copyleft）保护。它还检验了技术上的独立性（如低代码相似度）能否替代“净室”实践中所需的程序隔离。 根据抄袭检测工具 JPlag，新的 chardet 7.0.0 与前一版本的代码相似度仅为 1.29%。然而，维护者承认自己对原始代码库非常熟悉，违反了传统“净室”方法所要求的团队严格隔离原则。

rss · Simon Willison · Mar 5, 16:49

**背景**: “净室”实现是一种避免版权侵权的法律策略：一个团队对系统进行逆向工程以生成功能规范，另一个未接触原始代码的团队据此实现新代码。1982 年康柏（Compaq）曾用此方法克隆 IBM BIOS 而未复制其代码。在开源领域，LGPL 许可代码的衍生作品必须沿用相同许可证，除非新实现真正独立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cleanroom_software_engineering">Cleanroom software engineering - Wikipedia</a></li>
<li><a href="https://www.copyright.gov/ai/">Copyright and Artificial Intelligence | U.S. Copyright Office</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#software licensing`, `#clean room implementation`, `#copyright`

---

<a id="item-10"></a>
## [美国海关利用广告定位数据进行监控](https://www.404media.co/cbp-tapped-into-the-online-advertising-ecosystem-to-track-peoples-movements/) ⭐️ 8.0/10

泄露的文件显示，美国海关与边境保护局（CBP）在 2019 至 2021 年间使用了来自实时竞价系统的商业广告定位数据来追踪个人行踪。这是 CBP 首次承认其监控数据部分源自在线广告生态系统。 这种做法揭示了为广告目的收集的敏感位置数据如何被政府机构在缺乏公众监督的情况下重新用于监控，引发严重的隐私和公民自由问题。它凸显了广告技术行业的系统性漏洞，使大规模监控行为得以借商业数据经纪之名进行。 这些数据包括 GPS 坐标、IP 地址和广告标识符，通过移动应用和网站的软件开发工具包及实时竞价交易所收集。尽管该试点项目已结束，CBP 及其他联邦机构仍在持续采购商业位置追踪工具。

telegram · zaihuapd · Mar 6, 13:48

**背景**: 实时竞价（RTB）是一种数字广告系统，在广告拍卖过程中会向数百家公司共享用户数据（包括位置信息）。数据经纪商会聚合这些信息并将其用于营销或分析目的。然而，监管机构和隐私倡导者长期以来警告称，RTB 会泄露高度敏感的个人数据，可能被第三方（包括执法部门）滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/03/targeted-advertising-gives-your-location-government-just-ask-cbp">The Government Uses Targeted Advertising to Track Your Location. Here's What We Need to Do. | Electronic Frontier Foundation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Real-time_bidding">Real-time bidding - Wikipedia</a></li>
<li><a href="https://trustarc.com/resource/privacy-concerns-real-time-bidding/">Privacy Concerns in Real-Time Bidding: How to Ensure Privacy Compliance | TrustArc</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#data privacy`, `#ad-tech`, `#government monitoring`, `#location tracking`

---

<a id="item-11"></a>
## [Proton Mail 数据助 FBI 揭露抗议者身份](https://www.404media.co/proton-mail-helped-fbi-unmask-anonymous-stop-cop-city-protestor/) ⭐️ 8.0/10

Proton Mail 向瑞士当局提供了付款数据，FBI 据此识别出一名与亚特兰大“Stop Cop City”抗议活动相关的匿名用户。此举发生在 Proton Mail 强调其端到端加密和隐私保护的背景下。 该案例表明，即使是以隐私为核心卖点的邮件服务，在法律压力下仍可能披露用户数据，动摇了活动人士对数字匿名性的信任。这也凸显了当涉及付款信息时，加密服务的隐私保护存在局限。 所披露的数据仅限于付款记录，而非邮件内容，因为 Proton Mail 的端到端加密使其无法访问邮件正文。该用户与“Defend the Atlanta Forest”组织有关，而针对该抗议活动中 60 多人的指控后来已被撤销。

telegram · zaihuapd · Mar 7, 01:10

**背景**: Proton Mail 是一家总部位于瑞士的电子邮件服务，以其端到端加密和零知识架构著称，这意味着其无法访问用户的邮件内容。然而，它会收集有限的元数据，包括付费账户的付款信息，而这些信息并未加密。瑞士拥有严格的隐私法律，但企业仍可在法院命令下依法交出数据。“Stop Cop City”运动反对在亚特兰大 Weelaunee 森林建设耗资 9000 万美元的警察训练中心，抗议活动包含公民抗命和环保行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proton_Mail">Proton Mail - Wikipedia</a></li>
<li><a href="https://www.cbsnews.com/news/atlanta-protests-cop-city-georgia-state-of-emergency-forest-defenders/">What we know about Atlanta's "Cop City" and the standoff</a></li>
<li><a href="https://defendtheatlantaforest.org/solidarity/">statement of solidarity with Defend the Atlanta Forest</a></li>

</ul>
</details>

**标签**: `#privacy`, `#encryption`, `#law enforcement`, `#digital rights`, `#Proton Mail`

---

<a id="item-12"></a>
## [中国拟订购 200 至 500 架空客飞机以应对美贸易压力](https://t.me/zaihuapd/40079) ⭐️ 8.0/10

据知情人士透露，中国最早将于下月向空客订购 200 至 500 架飞机，涵盖窄体和宽体机型。 此举标志着中国在持续的中美贸易紧张局势下战略性减少对波音的依赖，可能大幅改变全球航空业格局，进一步巩固空客的市场主导地位。 该订单可能与法国总统马克龙和德国总理默茨 7 月访华参加中欧建交 50 周年活动同步；法德两国是空客的主要股东，各自持股约 11%。

telegram · zaihuapd · Mar 7, 01:53

**背景**: 窄体飞机（如空客 A320）通常用于中短程航线，单通道设计；宽体飞机（如 A350）则为双通道，主要用于远程国际航线。空客公司成立于 1970 年，最初是由法国和西德政府推动成立的欧洲航空联盟，旨在抗衡波音等美国航空巨头，至今仍由欧洲多国政府持有重要股份。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theflyingengineer.com/difference-between-narrowbody-and-widebody-aircraft/">Narrowbody Vs Widebody Aircraft: Differences Explained Simply</a></li>
<li><a href="https://www.marketscreener.com/quote/stock/AIRBUS-SE-4637/company-shareholders/">Airbus SE: Shareholders, Shareholding Structure - MarketScreener Individual Shareholders | Airbus Europe's Manufacturing Juggernaut: Who Owns Airbus? Who Owns AIRBUS Company? – Pestel-analysis.com Who Owns Airbus? A Deep Dive Into The Aerospace Giant Who Owns AIRBUS Company? – PortersFiveForce.com Europe's Manufacturing Juggernaut: Who Owns Airbus ? Who Owns AIRBUS Company? – PortersFiveForce.com Airbus SE: Shareholders, Shareholding Structure - MarketScreener Who Owns AIRBUS Company? – PortersFiveForce.com Who Owns Airbus? A Look At Its Shareholders</a></li>
<li><a href="https://simpleflying.com/europes-manufacturing-juggernaut-who-owns-airbus/">Europe's Manufacturing Juggernaut: Who Owns Airbus?</a></li>

</ul>
</details>

**标签**: `#aviation`, `#international trade`, `#geopolitics`, `#Airbus`, `#Boeing`

---

<a id="item-13"></a>
## [Anthropic 将就五角大楼国家安全风险认定提起法律挑战](https://t.me/zaihuapd/40080) ⭐️ 8.0/10

3 月 5 日，Anthropic 首席执行官达里奥·阿莫代宣布公司将对美国国防部将其列为国家安全供应链风险的决定提起法律挑战。该公司于 3 月 4 日收到该认定，并质疑其法律依据。 此次法律挑战可能为 AI 公司与美国国家安全机构的互动树立先例，并影响未来涉及新兴技术的政府采购政策。这也凸显了人工智能时代技术创新与国家安全监管之间日益加剧的紧张关系。 该认定适用范围有限——仅当客户在与国防部的合同中直接使用 Anthropic 的 Claude 模型时才生效。在过渡期内，Anthropic 将以名义成本继续向国防部和国家安全社区提供有限的模型访问和工程支持。

telegram · zaihuapd · Mar 7, 02:48

**背景**: 美国国防部设有供应链风险管理（SCRM）计划，用于识别和缓解来自国内外供应商对国家安全的威胁。被认定为“供应链风险”的公司可能会被限制参与国防相关合同。这一框架正越来越多地应用于科技公司，尤其是那些处理敏感数据或开发先进 AI 系统的企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nbcnews.com/tech/tech-news/anthropic-says-pentagon-declared-national-security-risk-rcna262013">Anthropic says the Pentagon has declared it a national security risk</a></li>
<li><a href="https://www.politico.com/news/2026/03/05/pentagon-tells-anthropic-it-has-designated-the-company-a-supply-chain-risk-00814758">Pentagon formally designates Anthropic a supply-chain risk - Politico</a></li>
<li><a href="https://www.acq.osd.mil/asds/log/scrm.html">Supply Chain Risk Management (SCRM)</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#national security`, `#Anthropic`, `#government procurement`, `#legal challenge`

---

<a id="item-14"></a>
## [任天堂起诉美国拒退 IEEPA 争议关税](https://www.ft.com/content/0315349e-763e-4faa-a5b1-c02ce7801cbd) ⭐️ 8.0/10

在美国最高法院裁定总统无权依据《国际紧急经济权力法》（IEEPA）征收关税后，任天堂已起诉美国贸易与海关官员，要求退还违法征收的关税。美国海关与边境保护局拒绝退税申请并暂停抗议程序，导致约 1500 亿美元争议关税尚未退还。 此案检验司法对行政贸易权力的约束是否可执行，可能为众多企业追回数千亿美元非法关税树立先例。同时也凸显了国家紧急状态主张与国际贸易义务之间的紧张关系。 任天堂要求退还自 2025 年 2 月起依据后来被裁定违法的行政令所缴纳的关税及利息。该诉讼已提交至美国国际贸易法院，该院对涉及联邦机构的关税争议拥有管辖权。

telegram · zaihuapd · Mar 7, 03:37

**背景**: 《国际紧急经济权力法》（IEEPA）授权美国总统在国家紧急状态下广泛管制对外商业活动。然而，美国最高法院近期一项里程碑裁决指出，IEEPA 并未授权总统征收关税，因为国会未明确授予此项权力。该判决使一系列以紧急状态为由实施的关税措施失效，影响了包括科技和消费品行业在内的众多进口商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ifeng.com/c/8qxg9KwWwcj">玉渊谭天：美 国 最高 法 裁决后，对华 IEEPA 关 税 应自动取消_凤凰网</a></li>
<li><a href="https://www.rfi.fr/cn/国际报道/20260305-美法官下令停止对进口商计算ieepa关税">美 法 官下令停止对进口商计算 IEEPA 关 税 | RFI - 法 国 国 际 广播电台</a></li>
<li><a href="https://post.smzdm.com/p/a9kpz6re/">时事热评 | 比亚迪诉美 国 IEEPA ...</a></li>

</ul>
</details>

**标签**: `#international trade`, `#tariffs`, `#Nintendo`, `#U.S. Supreme Court`, `#IEEPA`

---

<a id="item-15"></a>
## [贝莱德限制 260 亿美元私募信贷基金赎回](https://www.reuters.com/business/blackrock-limits-withdrawals-private-credit-fund-redemptions-mount-2026-03-06) ⭐️ 8.0/10

贝莱德对其规模 260 亿美元的 HPS Corporate Lending Fund 实施了 5%的季度赎回上限，此前该基金收到相当于资产 9.3%的赎回请求，仅支付了 6.2 亿美元以满足该上限。 此举表明私募信贷市场流动性压力正在加剧，并引发对更广泛金融稳定的担忧，尤其是考虑到贝莱德是全球最大的资产管理公司，管理资产超 9 万亿美元。 该基金主要投资于美国中型企业的优先担保浮动利率贷款；5%的赎回上限是此类基金的常见条款，一旦超过即自动触发限制。消息公布后，贝莱德股价下跌。

telegram · zaihuapd · Mar 7, 04:32

**背景**: 私募信贷基金通常比公开债务提供更高收益，但流动性较低，常在资金流出时设置赎回限制以管理现金流。HPS Corporate Lending Fund 采用非交易型商业发展公司（BDC）结构，旨在通过私募贷款提供机构级收益。近年来，随着投资者在高利率环境下追逐收益，此类基金迅速扩张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/blackrock-limits-withdrawals-private-credit-fund-redemptions-mount-2026-03-06/">BlackRock fund limits withdrawals as redemptions rattle private credit | Reuters</a></li>
<li><a href="https://www.investmentnews.com/alternatives/blackrock-curbs-redemptions-at-hps-private-credit-fund-as-investors-weigh-risks/265581">BlackRock curbs redemptions at HPS private credit fund as investors weigh risks - InvestmentNews</a></li>
<li><a href="https://d1io3yog0oux5.cloudfront.net/_55a17bbe74826bcff12724df80665730/hlend/db/2003/37076/file/HPS+Corporate+Lending+Fund+Fact+Sheet_2023.11_50_State.pdf">HPS Corporate Lending Fund Fact Sheet</a></li>

</ul>
</details>

**标签**: `#private credit`, `#BlackRock`, `#fund redemptions`, `#financial markets`, `#asset management`

---

<a id="item-16"></a>
## [云巨头限制 Anthropic 人工智能用于国防领域](https://www.cnbc.com/2026/03/06/google-says-anthropic-remains-available-outside-of-defense-projects.html) ⭐️ 8.0/10

谷歌、微软和亚马逊宣布将继续在其云平台上提供 Anthropic 的 Claude 人工智能模型，但明确禁止将其用于国防相关项目。此举源于美国国防部将 Anthropic 列为“供应链风险”，因其拒绝接受某些政府使用条款。 此举凸显了人工智能伦理政策与国家安全需求之间的日益紧张关系，为私营 AI 供应商如何应对政府合同树立了先例。同时也表明，主要云平台在努力保留商业 AI 客户的同时，正与联邦政府的风险评估保持一致。 Anthropic 的 Claude 模型仍可通过谷歌云的 Vertex AI 等平台用于非国防用途。该公司计划就国防部的风险认定提起法律诉讼，该认定源于其拒绝允许其模型被用于大规模国内监控或完全自主武器系统。

telegram · zaihuapd · Mar 7, 05:17

**背景**: Anthropic 由前 OpenAI 核心成员创立，开发了采用“宪法 AI”（Constitutional AI）训练方法的 Claude 系列大语言模型，旨在确保符合伦理与法律规范。美国联邦政府近年来日益加强对 AI 供应链的审查，担忧其在国防和监控等敏感领域的滥用。Vertex AI 是谷歌云推出的统一平台，用于构建和部署机器学习及生成式 AI 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vertex_AI">Vertex AI</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Cloud Computing`, `#National Security`, `#Anthropic`, `#Tech Regulation`

---

<a id="item-17"></a>
## [Anthropic 向开源维护者免费提供 Claude Max 权限](https://t.me/zaihuapd/40088) ⭐️ 8.0/10

Anthropic 启动了一项计划，向符合条件的开源维护者提供六个月的免费 Claude Max 权限，其使用限额高达标准版本的 20 倍。 该计划大幅降低了关键开源开发者使用先进 AI 工具的门槛，有望加速广泛使用软件项目的创新与维护。这也体现了 Anthropic 在具有影响力的开源社区中建立信任和推动采用的战略举措。 申请人需维护 GitHub 星标超 5000 个或月下载量超 100 万的项目，并在 2025 年 11 月之后有提交记录；若项目属于生态系统关键依赖，即使未达量化指标也可申请。Claude Max 计划包含桌面端、移动端和 Claude Code 访问权限，采用动态用量限制而非固定令牌配额。

telegram · zaihuapd · Mar 7, 09:05

**背景**: 开源维护者是领导并维系关键软件项目的核心贡献者，通常没有直接报酬。Anthropic 和 OpenAI 等公司近期开始向这些开发者提供 AI 工具支持，以认可他们对全球软件基础设施的巨大影响。Claude 是由 Anthropic 开发的 AI 助手，专为协作完成编码、写作和设计等任务而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/pricing/max">Max plan | Claude</a></li>
<li><a href="https://claude.ai/">Claude</a></li>
<li><a href="https://www.linuxfoundation.org/blog/open-source-maintainers-what-they-need-and-how-to-support-them">Open source maintainers: What they need and how to support them Anthropic and OpenAI are battling for the best open-source ... The latest on open source maintainers - The GitHub Blog The Unsung Heroes of Open Source: Understanding the Role of ... Open source maintainers: What they need and how to support them The latest on open source maintainers - The GitHub Blog Open source maintainers: What they need and how to support them The latest on open source maintainers - The GitHub Blog What could be done to support Open Source maintainers?</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#developer-tools`, `#Claude`, `#Anthropic`

---

<a id="item-18"></a>
## [黄仁勋：软件公司将出租 AI 代理而非出售授权](https://www.constellationr.com/insights/news/nvidias-huang-all-software-will-be-agentic) ⭐️ 8.0/10

英伟达 CEO 黄仁勋在摩根士丹利科技、媒体与电信大会上表示，软件公司将从传统授权模式转向出租 AI 代理，并混合使用自有和租用模型，因为所有软件都将具备代理能力。 这预示着软件盈利模式的根本性转变，与能够自主执行任务而非仅生成内容的 AI 系统兴起相一致。它可能重塑 SaaS 商业模式和企业采用 AI 的策略。 黄仁勋强调，企业将同时使用自行微调的开源模型和通过基于 token 的服务租用的闭源模型，类似于企业同时雇佣员工和承包商。收入将越来越多地来自针对特定任务的 AI 代理租赁，而非永久授权。

telegram · zaihuapd · Mar 7, 10:55

**背景**: Agentic AI 指能够规划、行动、使用工具并通过迭代验证结果以达成目标的自主系统，不同于仅生成内容的被动式生成式 AI（如聊天机器人）。这一范式转变使 AI 能作为工作流中的操作参与者，需要新的治理机制、可追溯性及商业模式。该概念是 AI 时代新兴基础设施的核心，其信任基础在于算法透明性，而非对 AI 拟人化行为的假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://grokipedia.com/page/agentic-ai">Agentic AI</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/how-digital-business-models-are-evolving-age-agentic-ai">How digital business models are evolving in the age of agentic AI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Software Business Models`, `#Generative AI`, `#SaaS`, `#NVIDIA`

---

<a id="item-19"></a>
## [Google AI 概览致科技媒体流量暴跌逾 85%](https://futurism.com/artificial-intelligence/google-ai-overviews-media) ⭐️ 8.0/10

据 SEO 公司 Growtika 报告，Google 的 AI 概览功能导致十家主要科技媒体从 Google 获得的月访问量从 2024 年初的 1.12 亿次骤降至 2025 年 1 月的不足 5000 万次。其中 Digital Trends 流量暴跌 97%，The Verge 和 ZDNet 等跌幅也超过 85%。 这种流量断崖式下跌威胁了依赖搜索广告收入的数字媒体商业模式，并凸显 AI 驱动的搜索摘要可能重塑在线内容消费与变现方式。这也引发了人们对在 AI 主导的搜索环境中独立新闻业长期可持续性的担忧。 流量下滑归因于 AI 自动生成答案直接满足用户查询、算法更倾向 Reddit 等论坛内容，以及传统链接点击率下降——当 AI 概览出现时点击率仅 8%，而无概览时为 15%。Google 反驳称该分析未考虑用户向播客和社区内容偏好的转移。

telegram · zaihuapd · Mar 7, 13:24

**背景**: Google AI 概览是 Google 搜索中的一项 AI 功能，在搜索结果顶部提供自动生成的摘要，旨在让用户无需点击外部网站即可快速获取答案。该功能于 2024 年全面推出，基于早期“精选摘要”升级而来，使用大语言模型生成更全面的回答。批评者认为它通过减少引荐流量损害内容创作者利益，而 Google 则称其提升了用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>
<li><a href="https://www.forbes.com/sites/torconstantino/2025/04/14/the-60-problem---how-ai-search-is-draining-your-traffic/">The 60% Problem: How AI Search Is Draining Your Traffic</a></li>
<li><a href="https://www.reddit.com/r/GrowthHacking/comments/1mgf65b/ai_search_is_killing_organic_traffic_how_are_you/">AI search is killing organic traffic - how are you adapting your brand ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Digital Media`, `#SEO`, `#Tech Industry`

---

<a id="item-20"></a>
## [60 岁开发者借 Claude Code 重燃编程热情](https://news.ycombinator.com/item?id=47282777) ⭐️ 7.0/10

一位 60 岁的软件开发者在 Hacker News 上分享，Anthropic 新推出的 AI 编程助手 Claude Code 重新点燃了他对编程的青春热情，这种感觉与几十年前 ASP 和 VB6 等技术带给他的兴奋如出一辙。 这表明现代 AI 工具能够重新激发那些可能感到与当今快速变化的技术环境脱节的资深开发者的热情，或可延长其职业生涯，并为软件社区注入宝贵经验。这也突显了编程学习与实践方式的代际转变。 这位开发者特别将使用 Claude Code 的兴奋感与他早年使用微软 Active Server Pages（ASP）和 Visual Basic 6（VB6）的经历相提并论——这些技术如今虽已过时，但在当时却具有革命性。他提到自己再次熬夜编程，就像年轻时一样。

hackernews · shannoncc · Mar 7, 00:05

**背景**: Active Server Pages（ASP）是微软在 1990 年代中期推出的首个用于动态网页的服务器端脚本环境。VB6（Visual Basic 6.0）于 1998 年发布，是一种流行的快速应用开发工具，在.NET 出现前广受欢迎。两者都是早期 Web 和桌面应用的重要基础。Claude Code 是 Anthropic 推出的新一代 AI 编程助手，旨在作为开发者的‘智能代理’伙伴，集成于 IDE 或终端中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Active_Server_Pages">Active Server Pages - Wikipedia</a></li>
<li><a href="https://medium.com/everyday-ai/what-is-this-claude-code-1cb5774e7923">What is this Claude Code ?. This one article = full information... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论呈现出乐观与担忧并存的局面：一些资深开发者认同原帖作者重燃的热情，另一些人则担心 AI 正在贬低数十年积累的专业经验。有评论指出，相比仅靠 AI“凭感觉编程”的新手，有经验的开发者能凭借直觉避开代价高昂的开发陷阱。

**标签**: `#AI-assisted programming`, `#software development`, `#developer experience`, `#Claude AI`, `#career reflection`

---

<a id="item-21"></a>
## [Go 标准库将新增原生 UUID 支持](https://github.com/golang/go/issues/62026) ⭐️ 7.0/10

Go 团队计划将 UUID 包加入 Go 标准库，以满足社区对内置通用唯一标识符（UUID）支持的长期需求。此举结束了开发者多年来对 github.com/google/uuid 和 github.com/gofrs/uuid 等第三方库的依赖。 将 UUID 纳入标准库可减少生态碎片化、提升可靠性，并符合 Go 为常见任务提供实用且维护良好的工具的哲学——这在广泛使用 UUID 的分布式系统中尤为重要。这也体现了 Go 在语言演进上谨慎而务实的态度。 拟议的包可能支持多个 UUID 版本（包括被分布式数据库广泛推荐的 v4），并需遵循 RFC 4122 标准。Go 团队必须在 API 简洁性、长期维护和向后兼容性之间取得平衡，因为一旦加入标准库，改动几乎不可逆。

hackernews · soypat · Mar 7, 02:03

**背景**: UUID（通用唯一标识符）是 128 位标识符，旨在无需中心协调即可在时空上保持唯一性。常见版本包括基于时间与 MAC 地址的 UUIDv1、随机生成的 UUIDv4，以及基于名称和 SHA-1 的 UUIDv5。在分布式系统中，UUIDv4 因可避免热点问题并保障隐私而被广泛采用。Go 历来奉行极简主义，避免将小众工具纳入标准库，但对广泛需要且稳定的特性会破例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pkg.go.dev/github.com/google/UUID">uuid package - github.com/google/UUID - Go Packages</a></li>
<li><a href="https://news.ycombinator.com/item?id=47283665">UUID package coming to Go standard library | Hacker News</a></li>
<li><a href="https://thearchitectsnotebook.substack.com/p/uuid-vs-auto-increment-ids-a-trade">Ep #32: UUID vs. Auto-increment IDs — A Trade-off Every Engineer Should Master</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人赞赏 Go 务实地加入了常用工具，也有人批评 UUID 对人类不友好，并质疑在已有 gofrs/uuid 等第三方库的情况下是否有必要纳入标准库。此外，关于哪些 UUID 版本更重要也存在讨论，多人指出 v4 仍是分布式数据库的首选标准。

**标签**: `#Go`, `#UUID`, `#standard library`, `#software engineering`, `#distributed systems`

---

<a id="item-22"></a>
## [用 CSS 隐喻 AI 时代的人类真实性](https://will-keleher.com/posts/this-css-makes-me-human/) ⭐️ 7.0/10

Will Keleher 发表了一篇反思性文章，以 CSS 样式（尤其是 em-dash 的渲染方式）作为隐喻，探讨在 AI 主导的交流环境中如何证明人类的真实性。该文在 Hacker News 上引发了关于神经多样性、写作风格和身份认同的广泛讨论。 随着 AI 生成文本日益普遍，人们被迫通过风格化特征来证明“人性”，这种压力可能将自然的沟通差异病理化——尤其对神经多样性人群而言。这场讨论揭示了真实性、他人认知与技术规范之间的张力。 作者使用 fontTools 在字体层面将 em-dash 替换为两个连字符（--），以确保其偏好的写作风格能通过 Markdown 处理器保留下来——这是一个大多数开发者不会想到的技术细节。他后来透露这篇文章本身借助了 AI，为其主题增添了讽刺意味。

hackernews · todsacerdoti · Mar 6, 21:52

**背景**: 在数字排版中，em-dash（—）是一种比连字符或 en-dash 更长的标点符号，常用于强调或插入语。如今许多写作工具和 AI 检测器会通过标点使用等风格特征来判断内容是否由人类生成。神经多样性指人类认知的自然差异，包括自闭症等，会影响个体的沟通方式，使其偏离神经典型（neurotypical）规范。

**社区讨论**: 评论者反应不一：有人认为文章语气过于自负，尤其在得知其由 AI 辅助后；而另一些人（尤其是神经多样性读者）则对文中描述的“因自然沟通方式被质疑”产生的焦虑深有共鸣。还有多人称赞了作者在字体层面处理 em-dash 的技术巧思。

**标签**: `#AI`, `#authenticity`, `#neurodiversity`, `#writing`, `#identity`

---

<a id="item-23"></a>
## [特朗普签署行政令加强打击网络犯罪](https://www.bloomberg.com/news/articles/2026-03-06/trump-signs-order-to-bolster-efforts-to-combat-cybercrime?srnd=phx-technology) ⭐️ 7.0/10

3 月 6 日，前总统特朗普签署行政令，要求联邦机构加强对针对美国家庭、企业和关键基础设施的跨国网络犯罪（包括网络欺诈和勒索软件攻击）的打击力度。该命令还责成司法部优先处理网络诈骗案件，并研究建立由没收的犯罪资产资助的受害者补偿机制。 该行政令可能通过将犯罪所得用于受害者赔偿，并将网络犯罪提升为国家安全优先事项，显著重塑美国的网络执法战略。此举回应了公众对日益严重的经济损失（仅 2024 年就超过 125 亿美元）的担忧，旨在重建对数字系统的信任。 该赔偿机制将利用执法行动中没收的资产，与 1984 年《犯罪受害者法案》设立的“犯罪受害者基金”等现有框架相一致。然而，该命令的实施依赖于跨部门协调，在资产追踪和分配方面可能面临法律或操作上的挑战。

telegram · zaihuapd · Mar 7, 11:40

**背景**: 美国长期以来通过司法部、国土安全部和国务院协调的策略打击跨国网络犯罪，通常与国际伙伴合作。1984 年设立的“犯罪受害者基金”（CVF）传统上利用联邦刑事罚款和没收资产支持州级受害者赔偿。2024 年 2 月，犯罪受害者办公室提出新规制定建议，旨在更新指南以更好地满足网络犯罪受害者的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.whitehouse.gov/presidential-actions/2026/03/combating-cybercrime-fraud-and-predatory-schemes-against-american-citizens/">Combating Cybercrime, Fraud, and Predatory Schemes Against ...</a></li>
<li><a href="https://ovc.ojp.gov/about/crime-victims-fund">Crime Victims Fund | OVC - Office for Victims of Crime</a></li>
<li><a href="https://www.congress.gov/crs-product/R42672">The Crime Victims Fund (CVF): Federal Support for Victims of ... Federal Restitution for Victims of Cybercrime - Leppard Law ... Criminal Division | Cybersecurity Unit Federal Restitution for Victims of Cybercrime and Identity Theft Crime Victims Fund | OVC - Office for Victims of Crime Crime Victims Fund | OVC - Office for Victims of Crime The Crime Victims Fund (CVF): Federal Support for Victims of Crime The Crime Victims Fund (CVF): Federal Support for Victims of Crime U.S. Launches First-Ever Government Compensation ... - Medium</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#executive order`, `#cybercrime`, `#U.S. policy`, `#fraud prevention`

---