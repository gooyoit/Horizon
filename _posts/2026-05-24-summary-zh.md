---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 101 items, 9 important content pieces were selected

---

1. [2026 年前沿 AI 大模型发布：谨慎推出与意外泄露交织](#item-1) ⭐️ 9.0/10
2. [Anthropic 准备发布 Claude Mythos 1 模型](#item-2) ⭐️ 9.0/10
3. [Anthropic 的 Project Glasswing 发现逾万个高危漏洞](#item-3) ⭐️ 9.0/10
4. [AI 发展的三大启示：安全、协作与结构化赋能](#item-4) ⭐️ 8.0/10
5. [GPT-5.5 Pro 事实核查能力出色但过于拘泥细节](#item-5) ⭐️ 8.0/10
6. [WWDC 2026 在即，苹果注册全新 genai.apple.com 子域名](#item-6) ⭐️ 8.0/10
7. [阶跃星辰发布 StepAudio 2.5 Realtime 实时语音模型](#item-7) ⭐️ 8.0/10
8. [苹果开源 corecrypto 密码库，附形式化验证的量子安全算法](#item-8) ⭐️ 8.0/10
9. [微软在核心团队内部大规模推广 Claude Code](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 年前沿 AI 大模型发布：谨慎推出与意外泄露交织](https://x.com/kimmonismus/status/2058327095839756299) ⭐️ 9.0/10

OpenAI 采取谨慎策略，通过"可信访问"机制仅向经过验证的网络安全专家限量发布 GPT-5.5-Cyber 模型；与此同时，Anthropic 此前宣称其 Claude Mythos 模型因过于强大而不适合公开发布，但该模型却意外短暂出现在用户界面中，并导致服务容量告罄。目前 Anthropic 正为 Claude Mythos（代号 claude-mythos-1-preview）在 Claude Code 和 Claude Security 等企业产品线上的集成发布做准备。 这一鲜明对比凸显了顶级 AI 实验室在 AI 能力提升与负责任部署之间日益加剧的张力，直接影响最强大的模型如何触达公众。OpenAI 和 Anthropic 截然不同的策略可能为整个行业在安全、访问控制和企业优先的模型分发方式上树立重要先例。 GPT-5.5-Cyber 是英国 AI 安全研究所（AISI）在网络任务上测试过的最强模型之一，也是第二个能端到端解决其多步骤网络攻击模拟的模型。Claude Mythos 的内部代号为"Capybara"，Anthropic 曾在四月初以"Mythos Preview"的名义公布该模型，随后意外泄露事件导致服务基础设施承压。

rss · AI Hot · May 23, 23:19

**背景**: OpenAI 的 GPT-5.5-Cyber 是其 GPT-5.5 模型的网络安全专用变体，专为防御性网络操作设计，并在严格的访问控制下发布以防止滥用。Anthropic 的 Claude 模型家族传统上分为 Haiku、Sonnet 和 Opus 三个层级发布，但 Claude Mythos 代表了显著的能力跃升，公司最初判断其公开访问风险过高。这两项进展都反映了一个更广泛的行业趋势：具有先进网络能力的前沿 AI 模型越来越多地被限制在企业或专家级访问之后，而非广泛开放给公众。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/">Scaling Trusted Access for Cyber with GPT‑5.5 and GPT‑5.5 ... - OpenAI</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities">Our evaluation of OpenAI's GPT-5.5 cyber capabilities</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://medium.com/codex/the-model-that-leaked-itself-anthropics-claude-mythos-and-the-cybersecurity-stocks-it-rattled-0aee52aa2dac">The Model That Leaked Itself: Anthropic ’s Claude Mythos ... | Medium</a></li>

</ul>
</details>

**标签**: `#Frontier AI`, `#Large Language Models`, `#OpenAI`, `#Anthropic`, `#AI Safety`

---

<a id="item-2"></a>
## [Anthropic 准备发布 Claude Mythos 1 模型](https://x.com/testingcatalog/status/2058322222297518498) ⭐️ 9.0/10

Anthropic is preparing to release a new AI model named 'Claude Mythos 1' (claude-mythos-1-preview), which has been spotted in strings for Claude Code and Claude Security, though public access remains unconfirmed.

rss · AI Hot · May 23, 23:00

**标签**: `#Anthropic`, `#Claude`, `#Frontier AI`, `#LLM Release`, `#AI Models`

---

<a id="item-3"></a>
## [Anthropic 的 Project Glasswing 发现逾万个高危漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 的 Project Glasswing 项目利用 Claude Mythos Preview 模型，在一个月内与约 50 个合作伙伴共同扫描了上千个开源项目，发现了逾万个高危或严重漏洞。在经过审查的 1752 个漏洞中，90.6% 被确认为真阳性，Cloudflare 等合作伙伴表示漏洞发现速率提高了十倍以上。 这标志着 AI 驱动的防御性网络安全能力的巨大飞跃，表明专业前沿模型在大规模漏洞发现方面可以大幅超越人力。然而，它同时也暴露了一个关键瓶颈：人工验证、披露和补丁基础设施已严重跟不上，部分开源维护者甚至请求放缓漏洞报告速度。 Claude Mythos Preview 是一个通用前沿模型，Anthropic 不会将其公开发布，而是通过系统卡来描述其能力，因为它具有强大的安全相关能力。Anthropic 已与开源安全基金会（OpenSSF）合作，并发布了 Claude Security 工具以帮助企业修复已发现的漏洞。

telegram · @zaihuapd · May 23, 03:16

**背景**: Project Glasswing 是 Anthropic 的研究计划，专注于研究和缓解大型语言模型在网络安全领域的攻防应用。开源软件构成了现代系统中绝大多数的代码，包括 AI 代理用于编写新软件的系统，因此这些代码库的安全性至关重要。开源安全基金会（OpenSSF）隶属于 Linux 基金会，是一个跨行业论坛，致力于通过协作的技术和教育举措来提升开源软件的安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/">Anthropic's new AI model finds and exploits... - Help Net Security</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades">Anthropic's latest AI model identifies 'thousands of... | Tom's H...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Cybersecurity`, `#AI Safety`, `#Vulnerability Research`, `#Frontier AI`

---

<a id="item-4"></a>
## [AI 发展的三大启示：安全、协作与结构化赋能](https://x.com/hongming731/status/2058340392001745160) ⭐️ 8.0/10

来自 Anthropic、OpenAI 和腾讯的最新进展共同表明：AI 发现漏洞的速度已超越人类修补能力，GPT-5.3-Codex-Spark 等超高速编码模型反而要求人类工程师进行更精细的实时监督，而结构化的外部工具赋能远胜于简单的技能包装。这三个案例共同指向一个新范式：高效的 AI 开发需要结构化约束和更深层次的人机协作，而非单纯的能力扩展。 这些发现的汇聚标志着 AI 发展的核心瓶颈发生了根本性转移——从模型能力转向安全治理和人机协作设计。随着 AI 系统变得更强大、更快速，真正的挑战在于如何构建人类监督、工具集成和安全工作流，以跟上 AI 生成输出的节奏。 Anthropic 的 Claude 在漏洞发现方面展现了超越几乎所有人类安全专家的网络攻防能力，甚至检测到了国家级网络攻击，但补丁修复流程仍受限于人力。GPT-5.3-Codex-Spark 基于 Cerebras 硬件实现超低延迟推理，在 SWE-Bench Pro 和 Terminal-Bench 2.0 上表现强劲，但社区反馈指出推理速度并非真正的瓶颈——上下文质量更为关键。腾讯的实验证实，为 AI 提供结构化约束和外部工具比简单地将技能包装进模型效果更好。

rss · AI Hot · May 24, 00:12

**背景**: Anthropic 一直在运行协调漏洞披露计划，AI 发现的漏洞会标注来源并为维护者提供候选补丁。OpenAI 的 GPT-5.3-Codex-Spark 代表了一类新型小型快速推理模型，专为实时交互式编码优化，标志着从传统 Nvidia GPU 基础设施向 Cerebras 硬件的转变。腾讯一直在微信核心平台之外的沙盒环境中测试 AI 产品策略，尝试结构化的 AI 工具集成方法而非直接的模型扩展，反映出业界对算力军备竞赛已进入收益递减阶段的共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/coordinated-vulnerability-disclosure">Coordinated vulnerability disclosure for Claude-discovered ...</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-3-codex-spark/">Introducing GPT-5.3-Codex-Spark | OpenAI</a></li>
<li><a href="https://www.infoq.com/news/2026/03/open-ai-codex-spark/">OpenAI Codex-Spark Achieves Ultra-Fast Coding Speeds on Cerebras Hardware - InfoQ</a></li>

</ul>
</details>

**社区讨论**: Reddit 上关于 Codex-Spark 的讨论显示，社区对单纯提升推理速度能否改善编码效果持怀疑态度，用户认为上下文质量才是真正的瓶颈——快速产出低质量代码的模型比慢速产出好代码的模型更糟糕。这与更广泛的主题一致：原始速度和能力的提升必须配合结构化的人类监督才能真正发挥效用。

**标签**: `#AI Safety`, `#Human-AI Collaboration`, `#AI Coding`, `#Anthropic`, `#AI Agents`

---

<a id="item-5"></a>
## [GPT-5.5 Pro 事实核查能力出色但过于拘泥细节](https://x.com/emollick/status/2058331615525232988) ⭐️ 8.0/10

沃顿商学院教授、知名 AI 研究者 Ethan Mollick 报告称，GPT-5.5 Pro 作为事实核查工具非常可靠，能够准确找出整章内容中的每一个关键参考文献。但他也指出了一个明显的缺点：该模型过于注重细微差别，经常对微小的细节问题进行纠正。 这一来自 AI 应用领域最具影响力人物之一的评测表明，GPT-5.5 Pro 等前沿模型正在真正适用于严肃的研究和学术事实核查工作。在详尽性与过度挑剔之间的权衡凸显了 AI 开发者面临的一个关键挑战：如何在专业场景中平衡精确性与实用性。 GPT-5.5 Pro 由 OpenAI 于 2026 年 4 月 23 日发布，在多项基准测试中表现出色，包括 Terminal-Bench 2.0 上的 82.7%和 FrontierMath Tier 1–3 上的 51.7%。该模型对微小细节过度纠正的倾向表明，尽管其理解和验证能力令人印象深刻，但用户在将其用于编辑审查时可能需要调整期望。

rss · AI Hot · May 23, 23:37

**背景**: GPT-5.5 Pro 是 OpenAI 最新的前沿大语言模型，旨在以更低的延迟和更高的质量处理复杂任务。Ethan Mollick 是沃顿商学院副教授、沃顿生成式 AI 实验室联合主任，也是畅销书《共智》的作者，曾被《时代》杂志评为 2024 年 AI 领域最具影响力人物之一。他对 AI 模型的实用性评测受到研究人员、教育工作者和专业人士的广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5_Pro">GPT-5.5 Pro</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT - 5 . 5 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ethan_Mollick">Ethan Mollick</a></li>

</ul>
</details>

**标签**: `#GPT-5.5`, `#Fact-Checking`, `#LLM Evaluation`, `#AI Capabilities`

---

<a id="item-6"></a>
## [WWDC 2026 在即，苹果注册全新 genai.apple.com 子域名](https://www.ithome.com/0/954/457.htm) ⭐️ 8.0/10

苹果在 WWDC 2026（北京时间 6 月 9 日凌晨 1 点开幕）之前悄悄注册了全新子域名 genai.apple.com。该子域名目前尚未指向任何活跃网页，但其注册表明苹果正在筹备一个专门的生成式 AI 门户或发布平台。 这一举动表明苹果正准备将生成式 AI 作为 WWDC 2026 的核心主题，可能标志着其 Apple Intelligence 战略的重大飞跃。在谷歌和 OpenAI 等竞争对手大力推进 AI 生态系统的背景下，苹果注册专门的生成式 AI 子域名暗示该公司已准备好在 iOS、macOS 等平台上大幅扩展其端侧 AI 能力。 iOS 27 等即将推出的系统预计将包含大量新功能，包括支持连续多轮对话的 Siri 独立应用、视频实时字幕生成、自然语言语音控制以及智能扫描和信息提取工具。genai.apple.com 子域名由 MacRumors 贡献者 Aaron Perris 发现，但目前仍指向未激活的页面。

rss · AI Hot · May 23, 22:40

**背景**: Apple Intelligence 是苹果于 2024 年推出的集成 AI 框架，旨在为其生态系统带来端侧生成式 AI 能力，同时强调隐私保护。它为增强照片搜索、照片应用中的自定义回忆影片创建、写作工具以及更强大的 Siri 等功能提供支持。开发者可以利用免费且支持离线运行的端侧模型将 Apple Intelligence 集成到自己的应用中，这使得苹果的 AI 方案与依赖云端的竞争对手形成了明显差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/05/23/apple-new-gen-ai-subdomain-ahead-of-wwdc/">Apple registers new 'gen AI' subdomain ahead of next... - 9to5Mac</a></li>
<li><a href="https://machash.com/macrumors/410479/apple-preparing-new-gen-ai-website-ahead-wwdc/">Apple Preparing New 'Gen AI' Website Ahead of WWDC</a></li>
<li><a href="https://developer.apple.com/apple-intelligence/">Apple Intelligence - Apple Developer</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Generative AI`, `#WWDC 2026`, `#Apple Intelligence`, `#Siri`

---

<a id="item-7"></a>
## [阶跃星辰发布 StepAudio 2.5 Realtime 实时语音模型](https://x.com/StepFun_ai/status/2058316152351424590) ⭐️ 8.0/10

阶跃星辰发布了 StepAudio 2.5 Realtime，这是一款实时语音交互模型，能够感知语气、节奏、停顿甚至轻叹等副语言特征，从而理解用户话语背后的真实意图。该模型支持中英文双语交互，并提供超过 10,000 种可组合的预置角色人格以及 5 种开箱即用的预设角色。 此次发布标志着实时多模态人机交互的重大突破，因为理解副语言特征一直是语音 AI 实现自然对话的长期瓶颈。基于 RLHF 调优的高度可定制角色人格系统，能够在客服、游戏和虚拟陪伴等场景中实现更具沉浸感和情感智能的应用。 该模型经过 RLHF（基于人类反馈的强化学习）优化，即使在复杂的角色扮演压力测试中也能稳定保持角色一致性。用户可通过 API 自定义人格，设定个性、背景故事和语言风格，上万种原生人格选项可组合出数百万种角色变体。

rss · AI Hot · May 23, 22:36

**背景**: 副语言特征是指语音中除字面内容之外的非语言元素，如语气、音调、节奏、停顿和音量等，它们传达了超越字面意义的丰富信息。在人类交流中，这些线索承载着关键的情感和语境信息——例如轻叹可能表示沮丧，而停顿可能暗示犹豫或强调。传统语音识别系统主要关注将语音转换为文字，很大程度上忽略了这些丰富的副语言信号。RLHF（基于人类反馈的强化学习）是一种训练技术，由人类评估者对模型输出进行评分，模型利用这些反馈来改进其响应，被广泛用于使 AI 行为与人类偏好保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/rlhf">What Is Reinforcement Learning From Human Feedback ( RLHF )?</a></li>
<li><a href="https://scispace.com/pdf/the-boundaries-of-language-dealing-with-paralinguistic-16id4qo0xm.pdf">The Boundaries of Language: Dealing with Paralinguistic Features</a></li>

</ul>
</details>

**标签**: `#Real-time Voice AI`, `#StepFun`, `#Multimodal`, `#Human-Computer Interaction`, `#RLHF`

---

<a id="item-8"></a>
## [苹果开源 corecrypto 密码库，附形式化验证的量子安全算法](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 8.0/10

苹果于 5 月 22 日开源了其 corecrypto 密码库，发布了经过形式化验证的 NIST 标准后量子算法 ML-KEM 和 ML-DSA 的实现，并提供了端到端的数学证明。这些证明使用 Isabelle 定理证明器开发，确保 C 代码和手工优化的 ARM64 汇编代码严格符合 NIST 标准。 此举显著推进了后量子密码学的采用进程，因为 corecrypto 为超过 25 亿台活跃苹果设备提供基础加密运算，已部署于 iMessage 和 VPN 等场景。通过开源经过形式化验证的实现，苹果使独立安全专家能够审计代码，并推动整个行业向更高保障的关键密码软件迈进。 苹果还公开了定制的验证工具和 Isabelle 理论库，供独立专家评估。形式化验证覆盖了从数学规范到底层汇编代码的完整流程，这一点尤为值得关注，因为手写汇编通常是密码学实现中最容易出错的部分。

telegram · @zaihuapd · May 23, 04:49

**背景**: 后量子密码学（PQC）是指旨在抵御未来量子计算机攻击的密码算法，因为量子计算机可能破解当前广泛使用的 RSA 和 ECC 等经典算法。2024 年 8 月，NIST 完成了其首批后量子密码标准的制定，包括 ML-KEM（用于密钥封装）和 ML-DSA（用于数字签名）。形式化验证是一种将代码行为转化为数学公式并证明其是否成立的技术，相比传统测试或代码审查能提供更强的正确性保证。Isabelle 定理证明器是一种高阶逻辑证明辅助工具，用于以高度可信的方式构建和检查此类数学证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.signisys.com/blog/post-quantum-isnt-a-future-problem-harvest-now-decrypt-later-attacks-are-already-happening/">Post - Quantum Cryptography Guide - Signisys</a></li>
<li><a href="https://www.quantamagazine.org/how-the-evercrypt-library-creates-hacker-proof-cryptography-20190402/">Cryptography That Is Provably Secure | Quanta Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_theorem_prover">Isabelle theorem prover</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#formal verification`, `#cybersecurity`, `#quantum computing`, `#open-source`

---

<a id="item-9"></a>
## [微软在核心团队内部大规模推广 Claude Code](https://t.me/zaihuapd/41535) ⭐️ 8.0/10

微软正在其最重要的工程团队中广泛部署 Anthropic 的 Claude Code，包括 CoreAI 团队以及负责 Windows、Microsoft 365 和 Outlook 等产品的体验与设备部门。公司甚至鼓励没有编程经验的非技术员工使用 Claude Code 进行原型设计，同时要求工程师同时使用 Claude Code 和 GitHub Copilot 并提供对比反馈。 这是一个引人注目的进展，因为拥有 GitHub Copilot 且是 OpenAI 最大投资者的微软，正在自己的核心工程团队中积极推广竞争对手的编程工具。这表明 AI 编程助手市场竞争异常激烈，微软正优先考虑使用最优秀的工具——即使来自竞争对手——以保持领先地位。 Claude Code 是 Anthropic 的智能编程工具，可直接在终端中运行，能够理解开发者的代码库、编辑文件并运行命令，帮助更快地交付代码。微软的 CoreAI 团队是由前 Meta 高管 Jay Parikh 领导的新成立的工程团队，专注于 AI 工具和平台，因此该团队采用 Claude Code 尤其值得关注。

telegram · @zaihuapd · May 23, 06:05

**背景**: Claude Code 是 Anthropic 推出的一款智能编程工具，运行在开发者的终端中，能够自主处理大量工程任务。微软的 CoreAI 团队是近期成立的内部工程团队，整合了公司的平台与工具部门和开发部门，由从 Meta 加入的 Jay Parikh 领导。GitHub Copilot 是微软自有的 AI 编程助手，由 OpenAI 模型驱动，一直是公司的旗舰开发者工具，因此内部大力推广竞争对手的产品显得极不寻常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet and Claude Code \ Anthropic</a></li>
<li><a href="https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition">GitHub just got less independent at Microsoft after CEO... | The Verge</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Anthropic`, `#Claude Code`, `#AI Coding Assistants`, `#Enterprise AI`

---