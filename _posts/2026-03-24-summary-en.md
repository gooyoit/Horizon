---
layout: default
title: "Horizon Summary: 2026-03-24 (EN)"
date: 2026-03-24
lang: en
---

> From 86 items, 12 important content pieces were selected

---

1. [iPhone 17 Pro Runs 400B-Parameter LLM On-Device](#item-1) ⭐️ 9.0/10
2. [Westlake Team Unveils Titan o1 with Real-Time Human Motion Cloning](#item-2) ⭐️ 9.0/10
3. [Claude Gains Direct Control Over Macs via 'Computer Use'](#item-3) ⭐️ 9.0/10
4. [Tech Firms Tie Employee Performance to LLM Token Usage](#item-4) ⭐️ 8.0/10
5. [OpenAI Urges UK to Include AI Chatbots in Google Search Choice Screen](#item-5) ⭐️ 8.0/10
6. [Apple WWDC 2026 Set for June 8 with AI Focus](#item-6) ⭐️ 8.0/10
7. [LLM Agents Attempt Autonomous ML Research](#item-7) ⭐️ 7.0/10
8. [Critique of 'AI Slop' as Disrespectful Workplace Practice](#item-8) ⭐️ 7.0/10
9. [Polle Interactive Raises Angel Round for AI+IP Content Ecosystem](#item-9) ⭐️ 7.0/10
10. [Cursor Users Cut Credit Usage by 10x with Custom API Endpoints](#item-10) ⭐️ 7.0/10
11. [New Tool for Multi-Agent Task Collaboration Released](#item-11) ⭐️ 7.0/10
12. [Tencent Tests AI-Powered Stock Inquiry Mini-Program](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [iPhone 17 Pro Runs 400B-Parameter LLM On-Device](https://twitter.com/anemll/status/2035901335984611412) ⭐️ 9.0/10

A demonstration claims an iPhone 17 Pro successfully ran a 400-billion-parameter large language model (LLM) using on-device inference with weight streaming from SSD. The model leverages Mixture of Experts (MoE) architecture and aggressive quantization to operate within mobile hardware constraints. If verified, this represents a major leap in on-device AI, enabling powerful, private, and offline-capable language models without relying on cloud infrastructure. It signals Apple’s potential integration of frontier AI directly into consumer devices, reshaping expectations for mobile intelligence. The model reportedly uses Apple’s 'LLM in a Flash' technique to stream weights from SSD, requiring only ~5.5GB RAM and achieving ~0.6 tokens/second. Despite the 400B parameter count, it is a Mixture of Experts model where only a subset (e.g., 17B) are active per token, and heavy quantization further reduces computational load.

hackernews · anemll · Mar 23, 14:30

**Background**: Mixture of Experts (MoE) is an LLM architecture that increases model capacity by splitting computation across multiple 'expert' subnetworks, activating only a few per input token via a routing mechanism. This allows models to scale parameters without proportional increases in compute. Quantization reduces numerical precision (e.g., from 16-bit floats to 4-bit integers) to shrink model size and speed up inference on resource-constrained devices. Apple’s 2023 'LLM in a Flash' paper proposed using fast flash storage as an extension of RAM to run massive models without loading all weights into memory at once.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>
<li><a href="https://glenrhodes.com/running-a-400b-parameter-model-locally-on-a-macbook-using-flash-based-inference-streaming/">Running a 400B parameter model locally on a MacBook using flash-based inference streaming - Glen Rhodes</a></li>

</ul>
</details>

**Discussion**: Community comments question whether the headline misleads by citing total parameters instead of active ones, noting that MoE models like Qwen3.5-397B-A17B behave more like 17B models during inference. Others highlight thermal throttling issues on current Apple silicon and reference Apple’s 'LLM in a Flash' paper as the likely technical basis for the demo.

**Tags**: `#LLM`, `#On-Device AI`, `#Mixture of Experts`, `#Apple`, `#AI Hardware`

---

<a id="item-2"></a>
## [Westlake Team Unveils Titan o1 with Real-Time Human Motion Cloning](https://www.ithome.com/0/931/964.htm) ⭐️ 9.0/10

Westlake University’s spin-off, Westlake Robotics, has launched Titan o1, a humanoid robot powered by the GAE (General Action Expert) 'universal cerebellum' model that enables real-time, remote imitation of human movements without pre-training or programming. The system allows one human operator to control multiple robots simultaneously across distances using motion capture gear or simple computer input. This breakthrough bridges embodied AI and practical robotics by enabling intuitive, real-time teleoperation—potentially transforming high-risk industries like firefighting, mining, and emergency response. It also advances the frontier of large action models as a new paradigm for robot control, moving beyond scripted behaviors toward adaptive, human-like motor intelligence. The GAE model functions as a 'universal cerebellum,' coordinating full-body motion in real time and supporting cross-embodiment deployment—meaning it can run on robots of different sizes and structures. The system requires no prior task-specific training and claims a six-month lead over global competitors in this capability.

rss · IT HOME · Mar 24, 01:34

**Background**: Embodied AI focuses on agents that interact with the physical world through sensors and actuators, requiring tight integration between perception, decision-making, and motor control. Large Action Models (LAMs) are an emerging class of AI systems trained to generate complex, coordinated physical behaviors—akin to how large language models generate text. The 'brain-cerebellum' architecture separates high-level reasoning ('brain') from low-level motor coordination ('cerebellum'), mimicking biological neural organization to improve agility and responsiveness in robots.

<details><summary>References</summary>
<ul>
<li><a href="https://robohorizon.cn/zh/videos/robot-shixian-moni-renti/">机器人影子人类：AI实时模仿人体动作 | RoboHorizon Robot Magazine -...</a></li>
<li><a href="https://www.linkedin.com/posts/grishinrobotics_real-time-shadowing-can-turn-a-robot-demo-activity-7378491418933301248-_OZi">Westlake Robotics unveils GAE, a real-time shadow function ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1982101283356841191">Human Data EP06—Mocap+Video：GAE - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI Robotics`, `#Embodied AI`, `#Humanoid Robots`, `#Large Action Models`, `#Research`

---

<a id="item-3"></a>
## [Claude Gains Direct Control Over Macs via 'Computer Use'](https://www.ithome.com/0/931/960.htm) ⭐️ 9.0/10

Anthropic has launched a research preview of its 'Computer Use' feature, allowing Claude 3.5 Sonnet to autonomously control macOS by moving the cursor, clicking buttons, and typing text. This capability is accessible through new desktop apps—Claude Cowork for general tasks and Claude Code for programming—and includes Dispatch, a mobile feature enabling remote task initiation from smartphones. This marks a major step toward truly autonomous AI agents that can operate within real-world desktop environments, transforming AI from a conversational tool into an active digital coworker. It signals a shift in human-computer interaction, where AI handles multi-step, cross-application workflows without constant human oversight. The feature is currently limited to macOS, available only to Claude Pro and Max subscribers, and operates in a sandboxed environment for security. Dispatch enables cross-device control but requires the desktop app to be running, and Cowork can only work within a single folder at a time.

rss · IT HOME · Mar 24, 01:30

**Background**: Large language models (LLMs) like Claude traditionally process text and images but cannot interact directly with operating systems. 'Computer Use' extends LLM capabilities by integrating computer vision and action execution, allowing the AI to perceive screen content and perform UI interactions similar to a human user. Anthropic’s Claude 3.5 Sonnet is the first frontier model to offer this publicly in beta.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use, a new Claude 3.5 Sonnet, and ...</a></li>
<li><a href="https://claude.com/product/cowork">Cowork : Claude Code power for knowledge work | Claude by Anthropic</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/03/20/claude-dispatch-lets-you-control-claude-cowork-with-your-phone/">Anthropic Update Lets You Control Claude Cowork With Your Phone</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#Human-Computer Interaction`, `#Claude`, `#Autonomous Systems`, `#Frontier AI`

---

<a id="item-4"></a>
## [Tech Firms Tie Employee Performance to LLM Token Usage](https://gizmodo.com/tech-employees-are-reportedly-being-evaluated-by-how-fast-they-burn-through-llm-tokens-2000736627) ⭐️ 8.0/10

Meta, OpenAI, and Shopify are reportedly evaluating employee productivity based on how many LLM tokens they consume, with internal leaderboards tracking usage and top users receiving rewards. This practice signals a shift in how AI-native companies quantify productivity, directly linking performance metrics to generative AI consumption—a move that could influence cost management, innovation incentives, and workplace culture across the tech industry. An OpenAI engineer reportedly used 210 billion tokens, while GPT-5.4 reportedly processes 5 trillion tokens per day; token counts include both input (prompt) and output (completion), reflecting total model workload and cost.

telegram · zaihuapd · Mar 23, 08:42

**Background**: In large language models (LLMs), a 'token' is a unit of text—such as a word, punctuation mark, or subword—that the model processes. Token usage directly correlates with computational cost and latency, making it a key metric for operational efficiency. Companies increasingly monitor token consumption to optimize AI spending and system performance.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/state-of-ai">State of AI 2025: 100T Token LLM Usage Study | OpenRouter</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-02-06-track-token-usage-prompt-costs-model-latency-opentelemetry/view">How to Track Token Usage, Prompt Costs, and Model Latency with OpenTelemetry</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/introducing-gpt-5-4/">Introducing GPT - 5 . 4 | OpenAI</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI Industry`, `#Performance Metrics`, `#Generative AI`, `#Token Usage`

---

<a id="item-5"></a>
## [OpenAI Urges UK to Include AI Chatbots in Google Search Choice Screen](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 8.0/10

OpenAI submitted a policy proposal to the UK’s Competition and Markets Authority (CMA) on March 6, urging regulators to explicitly include AI chatbots like ChatGPT in Google’s search choice screen for Android and Chrome. It argues these services now functionally compete with traditional and AI-enhanced search engines. This move signals OpenAI’s strategic effort to secure equal footing with established search engines as AI reshapes how users discover information. It also challenges regulators to redefine ‘search’ in the era of large language models, potentially influencing global digital competition policy. OpenAI proposes using transparent, dynamic popularity metrics to determine eligibility and expanding the choice screen beyond text-based search to include voice, visual, and AI-assisted interfaces. It specifically cites functional parity between ChatGPT and Google’s AI Overviews and AI Mode.

telegram · zaihuapd · Mar 23, 14:50

**Background**: Google’s search choice screen is a regulatory remedy stemming from EU antitrust rulings, requiring Google to let users choose a default search engine on Android devices. AI Overviews is Google’s feature that uses generative AI to summarize search results, launched as part of its broader integration of LLMs into Search. Large language models like ChatGPT now enable conversational, multi-turn information retrieval that competes with traditional keyword-based search.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://search.google/ways-to-search/ai-overviews/">Google AI Overviews - Search anything, effortlessly</a></li>
<li><a href="https://support.google.com/websearch/answer/14901683?hl=en">Find information in faster & easier ways with AI Overviews in Google Search - Computer - Google Search Help</a></li>

</ul>
</details>

**Tags**: `#AI Policy`, `#LLM`, `#Search Engines`, `#Regulation`, `#OpenAI`

---

<a id="item-6"></a>
## [Apple WWDC 2026 Set for June 8 with AI Focus](https://www.apple.com/newsroom/2026/03/apples-worldwide-developers-conference-returns-the-week-of-june-8/) ⭐️ 8.0/10

Apple has announced that its Worldwide Developers Conference (WWDC) 2026 will take place online from June 8 to 12, featuring major updates on AI integration across its platforms, new software releases, and developer tools. A limited in-person event will also be held at Apple Park on June 8. As Apple increasingly emphasizes AI, WWDC 2026 could mark a pivotal moment in how the company embeds generative and on-device intelligence into iOS, macOS, and developer workflows—potentially reshaping user experiences and app development across its ecosystem. The conference kicks off with a keynote and Platform State of the Union on June 8, followed by over 100 technical video sessions and interactive labs with Apple engineers. Fifty top Swift Student Challenge winners will be invited to Cupertino for a three-day immersive experience.

telegram · zaihuapd · Mar 23, 17:37

**Background**: WWDC is Apple’s annual event where it unveils new software, developer tools, and platform strategies. In recent years, Apple has shifted focus toward privacy-centric, on-device AI processing, contrasting with cloud-heavy approaches from competitors. The 2024 and 2025 events introduced foundational AI features like enhanced Siri and predictive text; WWDC 2026 is expected to expand these capabilities significantly.

**Tags**: `#AI`, `#Apple`, `#WWDC`, `#Software Update`, `#Developer Tools`

---

<a id="item-7"></a>
## [LLM Agents Attempt Autonomous ML Research](https://ykumar.me/blog/eclip-autoresearch/) ⭐️ 7.0/10

A blog post details an experiment using LLM agents to autonomously iterate on a machine learning project (eCLIP), modifying code, training models, and evaluating results in a loop. The agent primarily performed hyperparameter tuning rather than introducing novel architectural changes. This exploration highlights the current practical limits of LLM-based research automation—useful for incremental improvements but not yet capable of high-level scientific reasoning or cost-effective innovation. It informs how AI agents might augment, rather than replace, human researchers in the near term. The core of the system is a single prompt file (program.md) instructing the agent to iteratively improve train.py, run training, evaluate, and log results while favoring simplicity. Community analysis of the GitHub commit history shows most changes were minor hyperparameter adjustments, raising questions about token cost efficiency.

hackernews · ykumards · Mar 23, 18:40

**Background**: LLM-powered autonomous agents use large language models as a 'brain' to plan, reason, and execute tasks by interacting with tools like code interpreters, documentation, and APIs. In AutoML, LLMs can assist in data generation, model selection, and pipeline optimization, though full autonomy remains experimental. Recent frameworks like AutoM3L orchestrate multiple specialized LLM modules for language-driven machine learning automation.

<details><summary>References</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2023-06-23-agent/">LLM Powered Autonomous Agents | Lil'Log</a></li>
<li><a href="https://arxiv.org/pdf/2306.08107">AutoML in the Age of Large Language Models:</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1590105/full">Frontiers | Evaluation of large language model-driven AutoML in data and model management from human-centered perspective</a></li>

</ul>
</details>

**Discussion**: Commenters noted that while LLMs occasionally provide useful insights, most suggestions are impractical or based on poorly maintained libraries. Several observed that the agent’s actions resembled basic hyperparameter optimization, questioning whether the computational cost justified the marginal gains.

**Tags**: `#LLM`, `#AI Agents`, `#AutoML`, `#Research Automation`, `#Prompt Engineering`

---

<a id="item-8"></a>
## [Critique of 'AI Slop' as Disrespectful Workplace Practice](https://simonwillison.net/2026/Mar/23/neurotica/#atom-everything) ⭐️ 7.0/10

A social media post by Neurotica coined the term 'slop' to describe raw, unedited AI output that takes more human effort to consume than it took to produce, calling its uncritical sharing in professional settings a sign of disrespect. This critique highlights a growing ethical and practical issue in human-AI collaboration: the normalization of low-effort AI content degrades communication quality and wastes collective time, especially in professional environments where trust and clarity matter. The term 'slop' specifically refers to fluent but vacuous AI-generated text that appears useful but lacks substance; sharing it without human review shifts cognitive labor onto recipients, violating norms of collaborative respect.

rss · Simon Willison · Mar 23, 23:31

**Background**: Generative AI models like Gemini or GPT can produce fluent text quickly, but they often lack true understanding, nuance, or factual grounding. Raw outputs may contain errors, generic phrasing, or irrelevant information. In workplace contexts, such outputs are increasingly used without editing, raising concerns about accountability, quality, and efficiency. The term 'AI slop' has gained traction to describe this low-value, high-volume content flooding digital spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://slopdetector.org/slop/what-is-ai-slop">What Is AI Slop? Definition, Examples & Why It Matters (2026)</a></li>
<li><a href="https://www.linkedin.com/posts/stephen-collins-2b8207aa_youd-never-trust-raw-user-input-in-production-activity-7345454102904041472-vyw7">You’d never trust raw user input in production. So why are you piping...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#generative AI`, `#LLMs`, `#slop`, `#human-AI collaboration`

---

<a id="item-9"></a>
## [Polle Interactive Raises Angel Round for AI+IP Content Ecosystem](https://36kr.com/p/3735324365094918?f=rss) ⭐️ 7.0/10

Polle Interactive, an AI-driven digital content startup founded in 2025, has secured tens of millions of RMB in angel funding led by Xinglian Capital and followed by Chunhua Venture. The company is advancing its 'AI+IP' strategy through proprietary multimodal tools like 'Juling AI' and 'Polle Vision', partnerships with major model providers such as Zhipu AI, and commercial projects including the AI-animated short 'Tomorrow Monday'. This development signals a growing convergence of generative AI and intellectual property (IP) management in entertainment, where startups are not just building tools but redefining how digital content is created, owned, and monetized. Polle’s focus on copyright-compliant, tokenized IP assets could influence standards for ethical and scalable AIGC in media. Polle Interactive integrates large models from Zhipu AI and Shengshu into its tech stack, operates a data flywheel using artist-original + AI-enhanced content, and has already served over 10,000 creators via API integrations. Its upcoming 'full-modal interactive storytelling platform' aims to tokenize IP assets and enable global distribution.

rss · 36kr · Mar 24, 02:00

**Background**: The term 'AI+IP' refers to the integration of artificial intelligence—particularly large language and multimodal models—into the creation, adaptation, and commercialization of intellectual properties such as films, games, and literary works. AIGC (AI-Generated Content) platforms are increasingly used to accelerate production while raising concerns about copyright and data provenance. Multimodal AI systems can process and generate combinations of text, image, audio, and video, enabling richer interactive experiences in entertainment.

<details><summary>References</summary>
<ul>
<li><a href="https://cn.chinadaily.com.cn/a/202503/28/WS67e667bea31008317a2af380.html">AI+IP 深度融合：百度智能云赋能千亿级IP衍生市场创新发展</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202401291619258531_1.pdf">中航证券-人工智能行业大 模 型专题报告百 模 渐欲迷人眼AI...</a></li>

</ul>
</details>

**Tags**: `#AI+Entertainment`, `#AIGC`, `#LLM`, `#Digital Content`, `#Startup Funding`

---

<a id="item-10"></a>
## [Cursor Users Cut Credit Usage by 10x with Custom API Endpoints](https://www.v2ex.com/t/1200621#reply1) ⭐️ 7.0/10

A developer empirically analyzed Cursor's credit consumption patterns and demonstrated how configuring custom OpenAI-compatible API endpoints—using tools like OpenRelay—can bypass official usage quotas, especially for high-consumption Agent mode tasks. This workaround enables developers to use powerful AI coding assistants like Cursor more sustainably and cost-effectively, avoiding service degradation from quota exhaustion while gaining flexibility to use alternative or newer LLMs. It also highlights a growing trend of community-driven optimization in AI tooling ecosystems. The user found that Agent mode consumes 15–30 rapid requests per complex task, quickly exhausting Cursor Pro’s 500 monthly quota. By routing Chat and Agent requests through a local OpenRelay proxy that aggregates free tiers from 33 providers, they reduced official credit usage by ~70% and avoided slow-mode fallbacks.

rss · V2EX · Mar 24, 02:00

**Background**: Cursor is an AI-powered code editor that offers features like inline code completion (Tab), chat-based assistance, and Agent mode—an autonomous assistant that plans, edits files, runs commands, and iterates on tasks. Its 'rapid requests' quota governs high-priority inference; once exhausted, responses fall back to slower processing. Many AI platforms provide OpenAI-compatible API endpoints, allowing third-party tools to integrate diverse LLMs using the same interface as OpenAI’s /v1/chat/completions.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/cn/docs/agent/overview">概述 | Cursor Docs</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/13553491637">Cursor效率之道：Agent模式＋7大高级技巧详解 - 知乎</a></li>
<li><a href="https://loudu.cn/reference/openai.html">OpenAI 兼 容 性 | Ollama学习指南</a></li>

</ul>
</details>

**Tags**: `#AI Coding Assistant`, `#LLM`, `#Developer Tools`, `#API Integration`, `#Cost Optimization`

---

<a id="item-11"></a>
## [New Tool for Multi-Agent Task Collaboration Released](https://www.v2ex.com/t/1200619#reply0) ⭐️ 7.0/10

A developer has released a new web-based tool called Agenet that enables task-based collaboration among multiple AI agents, each with isolated contexts. The tool supports integration with Claude, Codex, and OpenClaw AI agents. This addresses a key usability limitation in current AI agent interfaces by moving beyond single-chat paradigms to structured, task-isolated workflows. It represents practical progress toward scalable and organized multi-agent systems, which are critical for complex real-world LLM applications. Each task maintains its own context and invokes a dedicated agent; the system currently supports Claude, Codex, and OpenClaw. A live demo is available at https://agenet.elsetech.app, though technical architecture or API details are not disclosed.

rss · V2EX · Mar 24, 01:48

**Background**: Multi-agent collaboration involves coordinating multiple autonomous AI agents, each with specialized roles and local decision-making capabilities, to solve complex tasks more effectively than a single agent could. Tools like this aim to manage context isolation and workflow orchestration—key challenges in agentic AI systems. OpenClaw is an open-source personal AI agent that can perform tasks via messaging platforms while keeping user data under local control.

<details><summary>References</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html">Multi-agent collaboration - AWS Prescriptive Guidance</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is multi-agent collaboration? - IBM</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#LLM`, `#Tooling`, `#Multi-Agent Systems`, `#Developer Tools`

---

<a id="item-12"></a>
## [Tencent Tests AI-Powered Stock Inquiry Mini-Program](https://mp.weixin.qq.com/s/JdwMZQiiY2_lRGZxux_Fkw) ⭐️ 7.0/10

Tencent is internally testing a WeChat mini-program called 'AI Wen Gu' that uses large language models to answer securities-related questions, currently available only to invited users who apply as beta testers. This move signals Tencent’s strategic push into AI-driven wealth management within its dominant WeChat ecosystem, potentially reshaping competition in China’s fintech sector against rivals like East Money and Tonghuashun. The mini-program builds on Tencent’s existing financial offerings like Tencent Self-Selected Stocks and Licaitong, aiming to enhance smart advisory capabilities; access is restricted during the internal testing phase.

telegram · zaihuapd · Mar 23, 04:47

**Background**: Large language models (LLMs) are increasingly applied in finance to interpret complex data, generate insights, and assist with investment decisions. In China, WeChat mini-programs serve as lightweight, integrated applications within the super-app ecosystem, enabling rapid deployment of services like AI-powered financial tools without requiring separate app downloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pm-research.com/content/iijpormgmt/51/2/162">Large Language Models for Financial and Investment Management ...</a></li>
<li><a href="https://digitalcreative.cn/blog/china-mini-programs-ecosystems-wechat-alipay-douyin">The Mini Program Multiverse: Explore China's Super App Ecosystems</a></li>

</ul>
</details>

**Tags**: `#AI Finance`, `#Large Language Models`, `#Wealth Tech`, `#Tencent`, `#Product Launch`

---