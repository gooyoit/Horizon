---
layout: default
title: "Horizon Summary: 2026-03-25 (EN)"
date: 2026-03-25
lang: en
---

> From 93 items, 19 important content pieces were selected

---

1. [Claude Code Introduces Auto Mode with AI-Powered Permissions](#item-1) ⭐️ 9.0/10
2. [Streaming Experts Enables Trillion-Parameter MoE Models on Consumer Devices](#item-2) ⭐️ 9.0/10
3. [China's Daily AI Token Usage Surges Over 1000x in Two Years](#item-3) ⭐️ 9.0/10
4. [Google Launches Gemini-Powered Dark Web Threat Intelligence Agent](#item-4) ⭐️ 9.0/10
5. [OpenAI to Discontinue Sora, Shift Focus to AI Agents and Spud Model](#item-5) ⭐️ 9.0/10
6. [Claude Code Launches Auto Mode with Built-in Safety Reviews](#item-6) ⭐️ 9.0/10
7. [OpenAI Shuts Down Sora Video Generation App](#item-7) ⭐️ 8.0/10
8. [LiteLLM Versions 1.82.7–1.82.8 Compromised in Supply Chain Attack](#item-8) ⭐️ 8.0/10
9. [Malicious LiteLLM Package Steals Credentials via .pth File](#item-9) ⭐️ 8.0/10
10. [Guangxiang Tech Raises Over ¥100M for Embodied AI Robotics](#item-10) ⭐️ 8.0/10
11. [NVIDIA Uses Financial Power to Lock in AI Startups](#item-11) ⭐️ 8.0/10
12. [Alibaba Unveils Xuantie C950 RISC-V CPU with AI Accelerator](#item-12) ⭐️ 8.0/10
13. [Package Managers Adopt Dependency Cooldowns for Security](#item-13) ⭐️ 7.0/10
14. [Open-Source Software Factory Uses Claude Agent SDK and GitHub](#item-14) ⭐️ 7.0/10
15. [Chaterm Offers Free 3-Month Pro Membership for Its First Anniversary](#item-15) ⭐️ 7.0/10
16. [AMD RDNA 4m iGPUs GFX1171/GFX1172 Spotted with AI Compute Upgrades](#item-16) ⭐️ 7.0/10
17. [Tianba Previews MACO470 Mini PC with Ryzen AI 9 HX 470](#item-17) ⭐️ 7.0/10
18. [Amazon Acquires Humanoid Robot Startup Fauna Robotics](#item-18) ⭐️ 7.0/10
19. [China Sets New 2.5 Pb/s Optical Fiber Record](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude Code Introduces Auto Mode with AI-Powered Permissions](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 9.0/10

Claude Code has launched 'auto mode,' a new permissions system where a dedicated classifier model (Claude Sonnet 4.6) autonomously approves or blocks code actions based on user intent and safety rules, replacing manual approvals or unsafe skip flags. This advancement significantly improves the usability and safety of autonomous AI coding agents by enabling trusted automation without sacrificing security, setting a new standard for secure AI-assisted development workflows. The classifier runs on Claude Sonnet 4.6 regardless of the main model in use, enforces default allow/deny rules (e.g., permitting local file ops within project scope but blocking external code execution), and supports custom rule extensions; it also preempts actions that appear to scout for later malicious use.

rss · Simon Willison · Mar 24, 23:57

**Background**: AI coding assistants like Claude Code can perform powerful actions such as editing files, running commands, or making network requests, which pose security risks if executed without oversight. Traditional approaches require manual approval for each action, hindering automation. Permission systems—similar to mobile app permissions—use allowlists and denylists to control what an AI agent can do, balancing autonomy and safety.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6">What's new in Claude 4.6 - Claude API Docs</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-4-6.html">Claude Sonnet 4.6 - Amazon Bedrock</a></li>
<li><a href="https://www.briangershon.com/blog/securing-ai-coding-tools/">Securing AI Coding Tools: Permission Controls and Credential Protection for Engineering Teams | Brian Gershon</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#Code LLM`, `#Safety`, `#Claude`, `#Autonomous Coding`

---

<a id="item-2"></a>
## [Streaming Experts Enables Trillion-Parameter MoE Models on Consumer Devices](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 9.0/10

Researchers have successfully run trillion-parameter Mixture-of-Experts (MoE) models like Kimi K2.5 and Qwen3.5 on consumer hardware—including MacBooks and iPhones—using a technique called 'streaming experts' that loads only the active expert weights from SSD during inference. Recent demonstrations achieved inference on an M2 Max MacBook Pro with 96GB RAM and even on an iPhone at 0.6 tokens/second. This breakthrough dramatically lowers the hardware barrier for running state-of-the-art large language models, enabling on-device AI with massive model capacity without requiring expensive GPUs or cloud infrastructure. It accelerates the trend toward private, offline, and personalized AI applications on everyday devices. The technique leverages the sparsity of MoE models—only ~17B to 32B parameters are active per token in trillion-parameter models—and streams required expert weights from SSD into RAM just-in-time. Performance remains limited (e.g., 0.6–1.7 tokens/second), but it proves feasibility on devices like iPhones and MacBooks with ≤128GB RAM.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) is a neural network architecture where a router dynamically selects a subset of specialized 'expert' subnetworks to process each input token, enabling models to scale to trillions of parameters while keeping computation per token manageable. Unlike dense models that use all parameters for every token, MoE models activate only a fraction, making them more efficient in theory—but still memory-intensive if all experts must reside in RAM. Streaming experts addresses this by loading experts on-demand from storage.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.co/posts/streaming-experts">Streaming experts</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Mixture-of-Experts`, `#Efficient Inference`, `#On-Device AI`, `#Research`

---

<a id="item-3"></a>
## [China's Daily AI Token Usage Surges Over 1000x in Two Years](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 9.0/10

China’s daily AI token (词元) usage reached over 140 trillion in March 2026, up from 100 billion in early 2024—a more than 1000-fold increase in just two years, according to the National Data Bureau. This explosive growth signals rapid scaling of large language model infrastructure and commercialization in China, reflecting deep integration of AI into the economy and progress in data要素 market reforms. It also establishes token as a foundational unit for pricing, trading, and measuring value in the emerging AI-driven data economy. Tokens are the smallest units of text processed by large language models, with Chinese text averaging about 1.5 characters per token. The metric tracks total daily model input and output volume across China’s AI ecosystem, serving as a proxy for real-world AI adoption and computational demand.

telegram · zaihuapd · Mar 24, 07:22

**Background**: In AI systems based on Transformer architectures, a token represents a basic unit of text—such as a word, subword, or punctuation mark—that the model processes during inference or training. Tokens are central to how LLMs manage context length, compute costs, and billing. In China’s policy framework, tokens are now being formalized as measurable, tradable data elements within the national data要素 market strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://tech.ifeng.com/c/8rkw9XWfkkx">词元（Token）是什么意思？官方首次定义：AI数据要素与投资价值全解析</a></li>
<li><a href="https://www.runoob.com/ai-agent/token-intro.html">Token (词元) - 菜鸟教程</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2633960">聊聊 AI 的 token 到底是啥？-腾讯云开发者社区-腾讯云</a></li>

</ul>
</details>

**Tags**: `#AI Adoption`, `#LLM`, `#Token Economy`, `#Data Infrastructure`, `#China AI`

---

<a id="item-4"></a>
## [Google Launches Gemini-Powered Dark Web Threat Intelligence Agent](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 9.0/10

Google has launched a public preview of a new AI agent within Google Threat Intelligence that uses the latest Gemini models to analyze 8–10 million dark web posts daily, identifying threats such as data leaks, insider risks, and initial access broker activity with reported 98% accuracy. This marks a significant advancement in applying large language models to real-world cybersecurity operations, automating labor-intensive threat intelligence tasks and enabling security teams to respond faster to emerging risks. It also demonstrates Google’s push to embed agentic AI deeply into enterprise security workflows. The system first builds an organizational profile for each customer, then continuously scans dark web forums to surface relevant threats. It leverages agentic capabilities—autonomous data synthesis and artifact triage—to reduce analyst cognitive load, as highlighted at RSAC 2026.

telegram · zaihuapd · Mar 24, 13:15

**Background**: Initial Access Brokers (IABs) are cybercriminals who infiltrate networks and sell access to other attackers, often enabling ransomware campaigns. The dark web hosts numerous forums where stolen data, credentials, and access are traded. Traditional threat intelligence requires manual monitoring of these sources, which is time-consuming and scales poorly. Agentic AI systems use LLMs to autonomously gather, analyze, and prioritize intelligence from unstructured data sources like dark web posts.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/rsac-26-supercharging-agentic-ai-defense-with-frontline-threat-intelligence">RSAC ’26: Supercharging agentic AI defense with frontline threat intelligence | Google Cloud Blog</a></li>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cybersecuritynews.com/google-gemini-ai-dark-web/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to Detect Threats</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cybersecurity`, `#Gemini`, `#LLM`, `#Threat Intelligence`

---

<a id="item-5"></a>
## [OpenAI to Discontinue Sora, Shift Focus to AI Agents and Spud Model](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 9.0/10

OpenAI plans to discontinue its AI video generation model Sora, shut down its developer API, and wind down its partnership with Disney. The company is reallocating resources toward developing AI agents and a new model codenamed 'Spud.' This marks a major strategic pivot for OpenAI, deprioritizing multimodal video generation just months after Sora’s high-profile launch. It signals a broader industry shift toward agentic AI systems and next-generation foundational models like Spud, potentially reshaping generative AI development priorities. Sora’s standalone app and API will be shut down, and the Disney collaboration is being phased out. OpenAI is also restructuring its safety teams to integrate them more closely into core development workflows alongside the push for AI agents and Spud.

telegram · zaihuapd · Mar 25, 00:30

**Background**: Sora, unveiled by OpenAI in early 2024, was a state-of-the-art text-to-video generative AI model capable of creating high-quality, minute-long videos from prompts. AI agents refer to autonomous systems that use large language models to plan, reason, and execute multi-step tasks using tools and external APIs. The newly mentioned 'Spud' model appears to be OpenAI’s next major foundational AI system, though technical details remain undisclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theinformation.com/articles/openai-ceo-shifts-responsibilities-preps-spud-ai-model">OpenAI CEO Shifts Responsibilities, Preps ‘Spud’ AI Model</a></li>
<li><a href="https://www.tomsguide.com/ai/openai-just-killed-sora-as-company-readies-ipo-and-new-spud-model">OpenAI just killed Sora as company readies IPO and new 'Spud' model | Tom's Guide</a></li>
<li><a href="https://getstream.io/blog/openai-agents-sdk/">OpenAI Agents SDK — Getting Started</a></li>

</ul>
</details>

**Tags**: `#AI Video Generation`, `#Sora`, `#OpenAI`, `#Generative AI`, `#AI Strategy`

---

<a id="item-6"></a>
## [Claude Code Launches Auto Mode with Built-in Safety Reviews](https://claude.com/blog/auto-mode) ⭐️ 9.0/10

Claude Code has launched 'Auto Mode,' which grants AI autonomous decision-making during task execution by using a classifier to review each tool call in real time, automatically approving safe actions and blocking high-risk ones like bulk file deletion or data exfiltration. This feature significantly advances the practical deployment of autonomous AI agents by balancing usability and safety—reducing manual interruptions while preventing dangerous actions, which is crucial for enterprise adoption of LLM-powered workflows. Auto Mode is currently available as a research preview for Team plan users and will roll out to Enterprise and API users soon; it supports Claude Sonnet 4.6 and Opus 4.6 models, may slightly increase token usage and latency, and should still be used in isolated environments despite being safer than the --dangerously-skip-permissions flag.

telegram · zaihuapd · Mar 25, 01:15

**Background**: Claude is a series of large language models developed by Anthropic, known for its use of Constitutional AI—a training approach designed to align models with ethical and legal principles. Claude Code is Anthropic’s developer-focused interface that enables AI-assisted coding and tool use. The newly referenced Sonnet 4.6 and Opus 4.6 models are optimized for complex, multi-step workflows and long-context reasoning, respectively.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Sonnet_46">Claude Sonnet 4.6</a></li>
<li><a href="https://grokipedia.com/page/Claude_Opus_46">Claude Opus 4.6</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-6">Introducing Claude Opus 4.6 - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Autonomous Agents`, `#LLM`, `#Claude`, `#Tool Use`

---

<a id="item-7"></a>
## [OpenAI Shuts Down Sora Video Generation App](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 8.0/10

OpenAI has announced the shutdown of its Sora AI video generation app, despite having recently published safety guidelines for the platform. The decision comes after a limited public release and growing internal and external scrutiny over its purpose and impact. Sora represented a major step in generative AI’s expansion into dynamic media, with implications for entertainment, misinformation, and creative expression. Its abrupt discontinuation raises questions about OpenAI’s product strategy and the societal readiness for AI-generated video at scale. Sora was both a text-to-video generative model and a standalone social media app that allowed users to create and share short AI-generated videos. Despite technical capabilities like extending existing clips and generating scenes from text or images, user engagement reportedly declined after an initial novelty phase.

hackernews · mikeocool · Mar 24, 20:01

**Background**: Sora is OpenAI’s text-to-video generative model, capable of producing realistic and imaginative video clips up to one minute long based on natural language prompts. Unlike image generators such as DALL·E, Sora handles temporal coherence across frames, making it significantly more complex. It was positioned as part of OpenAI’s broader push into multimodal AI systems that understand and generate diverse media types.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to-video model) - Wikipedia</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/video-generation">Video generation with Sora | OpenAI API</a></li>
<li><a href="https://openai.com/sora?via=1bestai.tools">Sora</a></li>

</ul>
</details>

**Discussion**: Community reactions were mixed: some praised the shutdown as a rejection of addictive, corporate-controlled content, while others lamented the loss of a tool that sparked genuine creativity and bonding. Critics also questioned the timing, noting the safety guidelines were published just before the shutdown announcement.

**Tags**: `#AI Video Generation`, `#Sora`, `#OpenAI`, `#Generative AI`, `#Ethics`

---

<a id="item-8"></a>
## [LiteLLM Versions 1.82.7–1.82.8 Compromised in Supply Chain Attack](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 8.0/10

Malicious code was injected into LiteLLM versions 1.82.7 and 1.82.8 on PyPI, including a base64-encoded payload in proxy_server.py and a litellm_init.pth file that triggers credential theft upon package installation. The packages have been quarantined on PyPI, and the incident is linked to the threat actor TeamPCP. This supply chain attack poses severe risks to AI developers who rely on LiteLLM for LLM routing and proxying, as it enables arbitrary code execution and credential theft without requiring explicit imports. It underscores systemic vulnerabilities in open-source dependency trust and CI/CD security practices across the AI ecosystem. The malicious payload activates during Python startup via a .pth file, meaning infection occurs simply by installing the package. Additionally, commented-out earlier versions of the payload were left in proxy_server.py, revealing the attacker’s development process—an operational security failure.

hackernews · dot_treo · Mar 24, 12:06

**Background**: LiteLLM is a popular open-source library that provides a unified API for routing requests to various large language models (LLMs) like OpenAI, Anthropic, and open-source alternatives. It is widely used in AI infrastructure for load balancing, fallbacks, and cost optimization. Supply chain attacks target software dependencies to inject malicious code upstream, compromising all downstream users. TeamPCP is a known threat actor that has previously compromised tools like Aqua Security's Trivy scanner and Checkmarx GitHub Actions.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.dreamfactory.com/the-litellm-supply-chain-attack-a-complete-technical-breakdown-of-what-happened-who-is-affected-and-what-comes-next">The LiteLLM Supply Chain Attack: A Complete Technical ...</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/malicious-litellm/">Malicious litellm_init.pth in litellm 1.82.8 — credential stealer</a></li>
<li><a href="https://www.endorlabs.com/learn/teampcp-isnt-done">TeamPCP Isn't Done: Threat Actor Behind Trivy and... | Endor Labs</a></li>

</ul>
</details>

**Discussion**: Maintainers confirmed the breach likely originated from a compromised CI/CD tool (Trivy), and clarified that Docker users were unaffected due to pinned dependencies. Community members called for stronger sandboxing, defense-in-depth, and better dependency hygiene, while others shared detection tools like canary honeypots. Some also noted spam flooding in the GitHub issue thread.

**Tags**: `#AI Security`, `#Supply Chain Attack`, `#LLM`, `#LiteLLM`, `#DevSecOps`

---

<a id="item-9"></a>
## [Malicious LiteLLM Package Steals Credentials via .pth File](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 8.0/10

Version 1.82.8 of the LiteLLM Python package on PyPI was compromised with a malicious litellm_init.pth file that automatically executes a credential-stealing payload upon installation, without requiring the package to be imported. Version 1.82.7 also contained similar malware hidden in proxy_server.py. This supply chain attack targets a widely used AI orchestration library, potentially compromising developer credentials, cloud secrets, and cryptocurrency wallets across thousands of AI projects. It highlights critical vulnerabilities in open-source dependency trust and CI/CD security practices. The .pth file exploits Python’s site-packages initialization mechanism to run code on every interpreter startup, exfiltrating files from ~/, including SSH keys, AWS/Azure configs, Docker credentials, and even cryptocurrency wallet directories. The attack is attributed to the TeamPCP group, likely using credentials stolen via a prior compromise of the Trivy security scanner used in LiteLLM’s CI pipeline.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is an open-source Python library that provides a unified interface to over 100 large language models (LLMs), allowing developers to switch between providers like OpenAI, Anthropic, and AWS Bedrock using the OpenAI API format. It is widely adopted in AI agent frameworks and production systems. In Python, .pth files placed in site-packages can execute arbitrary code during interpreter startup if they contain import statements, a feature sometimes abused in supply chain attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI ... Getting Started | liteLLM TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via ... Popular LiteLLM PyPI package compromised in TeamPCP supply ... LiteLLM on PyPI Was Compromised, What the Attack Changed and ... LiteLLM Supply Chain Attack: What Happened, Who’s Affected ...</a></li>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack : Malicious PyPI... | Wiz Blog</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Supply Chain Attack`, `#LLM`, `#LiteLLM`, `#Cybersecurity`

---

<a id="item-10"></a>
## [Guangxiang Tech Raises Over ¥100M for Embodied AI Robotics](https://36kr.com/newsflashes/3737738833232132?f=rss) ⭐️ 8.0/10

Industrial embodied AI startup Guangxiang Tech has secured over ¥100 million across seed, angel, and angel+ funding rounds. The investment was led by IDG Capital and Oriental Fortune Capital, with participation from robotics-focused firms like Efort and Lingyi Ventures. This significant funding signals strong investor confidence in embodied intelligence as a critical frontier for AI’s real-world application, particularly in industrial automation. It accelerates the development of physical AI agents capable of interacting intelligently with complex environments. The raised capital will be used for core R&D of embodied robotics, productization, and commercial delivery. Investors include both top-tier financial VCs and strategic players in the robotics industry, indicating dual validation of technical potential and market readiness.

rss · 36kr · Mar 25, 02:24

**Background**: Embodied AI refers to intelligent systems that interact with the physical world through sensors and actuators, learning from real or simulated environments. Unlike traditional 'disembodied' AI that processes text or images in isolation, embodied intelligence enables robots to perceive, reason, and act in dynamic settings—making it essential for industrial automation, logistics, and service robotics. Recent advances in large language models (LLMs) and simulation platforms like ManiSkill3 are accelerating progress in this field.

<details><summary>References</summary>
<ul>
<li><a href="http://scis.scichina.com/cn/2025/SSI-2025-0177.pdf">SCIENTIA SINICA</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202510031755113354_1.pdf">Survey on Embodied AI, Liu Yang, et.al》中国银河证券研究院</a></li>
<li><a href="https://36kr.com/p/2714495949771399">具 身 智 能 的月亮与六便士-36氪</a></li>

</ul>
</details>

**Tags**: `#Embodied AI`, `#Robotics`, `#AI Hardware`, `#Startup Funding`, `#Industrial AI`

---

<a id="item-11"></a>
## [NVIDIA Uses Financial Power to Lock in AI Startups](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

NVIDIA has invested billions since 2022 in AI startups like OpenAI, CoreWeave, and Reflection, acting simultaneously as a chip supplier, investor, and lender. It also signed a $20 billion licensing deal with Groq and hired its core team, prompting U.S. senators to question whether these moves circumvent antitrust scrutiny. This strategy strengthens NVIDIA’s dominance in AI infrastructure by locking customers into its ecosystem, raising concerns about reduced competition, higher barriers for rivals like AMD, and potential stifling of innovation in the AI hardware market. NVIDIA’s deals often include flexible structures that avoid triggering formal merger reviews, and its investments help startups afford expensive GPU-based infrastructure—making switching to alternatives like AMD or Groq’s LPU economically difficult. Groq’s architecture uses a Temporal Instruction Set Computer design with 220MB on-chip memory and no external HBM, offering a different approach to AI acceleration.

telegram · zaihuapd · Mar 24, 03:02

**Background**: NVIDIA dominates the AI chip market with its GPUs, which are essential for training large language models. Competitors like AMD offer alternative hardware, but face challenges due to NVIDIA’s mature software stack (CUDA) and ecosystem lock-in. Groq, a newer entrant, developed a Language Processing Unit (LPU) optimized for inference with deterministic latency, differing fundamentally from GPU architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://36kr.com/p/2660945964753667">AI芯片黑马Groq走红，英伟达又多了一个挑战者-36氪</a></li>
<li><a href="https://www.36kr.com/p/3205490522694146">AI圈的“资金循环”——英伟达和“亲儿子”CoreWeave的故事-36氪</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#NVIDIA`, `#Antitrust`, `#Startup Ecosystem`, `#Chip Industry`

---

<a id="item-12"></a>
## [Alibaba Unveils Xuantie C950 RISC-V CPU with AI Accelerator](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

Alibaba's DAMO Academy launched the Xuantie C950, a new high-performance RISC-V CPU that achieves over 70 points in SPECint2006 single-core benchmark and integrates a custom AI accelerator capable of natively running billion-parameter models like Qwen3 and DeepSeek V3. This marks the first time a RISC-V CPU natively supports large-scale generative AI models, bridging open-architecture hardware with frontier AI deployment and potentially reshaping edge and cloud inference infrastructure. The chip operates at up to 3.2 GHz, supports the RVA23 RISC-V standard, and uses a hybrid architecture combining general-purpose computing with dedicated AI acceleration for efficient large-model inference.

telegram · zaihuapd · Mar 24, 06:01

**Background**: RISC-V is an open-source instruction set architecture (ISA) gaining traction as an alternative to proprietary architectures like x86 and ARM, especially in AI and embedded systems due to its modularity and customization potential. Large language models (LLMs) such as Qwen3 and DeepSeek V3 typically require specialized hardware like GPUs or NPUs for efficient inference, making native support on a CPU a significant milestone.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/玄铁C950/67526091">玄铁C950 - 百度百科</a></li>
<li><a href="https://www.xinhuanet.com/tech/20260324/fdc7c3b201074147a46b5ce6ad51045f/c.html">阿里达摩院发布RISC-V CPU玄铁C950，首次原生支持千亿参数大模型</a></li>
<li><a href="https://www.ithome.com/0/931/986.htm">全球性能最高 RISC-V CPU：阿里达摩院新一代旗舰处理器玄铁 C950 正式...</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#AI Hardware`, `#LLM`, `#Chip Design`, `#Generative AI`

---

<a id="item-13"></a>
## [Package Managers Adopt Dependency Cooldowns for Security](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

Major package managers—including pnpm, Yarn, Bun, Deno, uv, pip, and npm—have recently added support for dependency cooldown features that delay installation of newly published packages. These mechanisms were accelerated by the recent malicious LiteLLM supply chain attack. Dependency cooldowns help mitigate supply chain attacks by giving the community time to detect malicious updates before they propagate widely—critical for AI/ML systems that depend heavily on open-source packages. This shift represents a proactive security measure embedded directly into development tooling. Features vary by tool: pnpm uses minimumReleaseAge with per-package exemptions, npm 11.10.0 introduced min-release-age, and pip 26.0 supports only absolute timestamps via --uploaded-prior-to (relative durations require workarounds). Most tools allow trusted packages to bypass the cooldown.

rss · Simon Willison · Mar 24, 21:11

**Background**: Supply chain attacks occur when attackers compromise legitimate software dependencies to inject malicious code. The LiteLLM incident in early 2026 involved a hijacked maintainer account publishing a backdoored version of the popular AI proxy library. Dependency cooldowns act as a time-based filter, reducing the risk of automatically pulling in freshly published—but potentially compromised—packages.

<details><summary>References</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://maier.tech/notes/pnpm-minimum-release-age">PNPM minimumReleaseAge</a></li>

</ul>
</details>

**Tags**: `#Supply Chain Security`, `#Package Managers`, `#AI Infrastructure`, `#Software Engineering`, `#LiteLLM`

---

<a id="item-14"></a>
## [Open-Source Software Factory Uses Claude Agent SDK and GitHub](https://www.v2ex.com/t/1200923#reply1) ⭐️ 7.0/10

A developer released an open-source 'software factory' that uses GitHub and Anthropic's Claude Agent SDK to automatically create pull requests from issues and refine code based on reviewer feedback. This project demonstrates a practical, real-world application of AI agents in software development workflows, potentially reducing manual coding tasks and accelerating iteration cycles for developers. The system uses git worktree to manage isolated branch environments for each task and integrates directly with a project’s GitHub issues and PRs. It leverages the Claude Agent SDK—originally powering Claude Code—for code generation and refinement.

rss · V2EX · Mar 25, 02:19

**Background**: The Claude Agent SDK is an official toolkit from Anthropic that enables developers to build custom AI agents using Claude models, particularly for coding tasks. Git worktree is a Git feature allowing multiple working directories tied to the same repository, useful for parallel development without context switching.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Claude_Agent_SDK_Python">Claude Agent SDK (Python)</a></li>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git-worktree Documentation</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#LLM`, `#Developer Tooling`, `#GitHub Automation`, `#Open Source`

---

<a id="item-15"></a>
## [Chaterm Offers Free 3-Month Pro Membership for Its First Anniversary](https://www.v2ex.com/t/1200919#reply0) ⭐️ 7.0/10

Chaterm, an AI-native terminal for infrastructure and cloud management, is celebrating its first anniversary by offering users a free 3-month Pro membership. The tool now includes features like SSH/JumpServer asset management, reusable AI Agent Skills, Kubernetes context switching, SFTP support, and natural language-driven command execution. Chaterm demonstrates practical integration of LLMs and AI agents into DevOps workflows, enabling engineers to manage complex cloud infrastructures more efficiently through natural language and automation. This reflects a growing trend of AI-native developer tools that aim to reduce cognitive load and operational friction. Chaterm supports cross-device cloud-synced asset management, auditable AI agent workflows, context-aware command suggestions, and a plugin system for public cloud and Kubernetes integration. Users can encapsulate运维 processes as shareable 'Agent Skills' for team-wide reuse.

rss · V2EX · Mar 25, 02:09

**Background**: An 'AI-native terminal' refers to a command-line interface enhanced with large language models (LLMs) that understand natural language, maintain contextual awareness, and can execute or suggest commands based on user intent and environment state. AI Agents in this context are autonomous or semi-autonomous modules that perform multi-step tasks by chaining actions, often using predefined 'skills'—reusable workflows that encapsulate domain-specific knowledge or procedures.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1939630380220145925">9 款终端 AI 编码工具横向对比：从 Claude Code 到 gROK CLI，谁能重...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1993287535472960620">Agent Skills 完全指南：让你的 AI Agent 拥有超能力</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2628286">AI Agent核心能力载体：Skills技能模块从基础到实战全指南</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#DevOps`, `#LLM`, `#Developer Tools`, `#Cloud Infrastructure`

---

<a id="item-16"></a>
## [AMD RDNA 4m iGPUs GFX1171/GFX1172 Spotted with AI Compute Upgrades](https://www.ithome.com/0/932/374.htm) ⭐️ 7.0/10

AMD has added two new integrated GPU targets, GFX1171 and GFX1172, to its open-source LLVM stack, both based on the RDNA 4m architecture and featuring native support for FP8/BF8 data formats and WMMA matrix instructions for AI acceleration. These enhancements signal AMD’s strategic push to enable efficient on-device AI workloads in future mobile and edge APUs, aligning with industry trends toward hardware-optimized low-precision computation for AI inference. Although GFX1171 and GFX1172 share identical instruction sets with GFX1170—including FP8/BF8 and WMMA—they likely differ in compute unit count or clock speeds; RDNA 4m is not a full RDNA 4 architecture but a derivative of RDNA 3, intended for Zen 6 'Medusa Point' APUs.

rss · IT HOME · Mar 25, 02:09

**Background**: FP8 and BF8 are 8-bit floating-point formats that reduce memory bandwidth and power consumption while maintaining acceptable accuracy for AI inference tasks. WMMA (Wave Matrix Multiply Accumulate) is a GPU instruction set that accelerates matrix operations—core to neural network computations—by leveraging dedicated hardware units similar to NVIDIA’s Tensor Cores. AMD first introduced WMMA support in RDNA 3 GPUs to boost AI performance on consumer hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://gpuopen.cn/learn/wmma_on_rdna3/">如何使用 WMMA 加速 RDNA 3 上的 AI 应用 - AMD GPUOpen - GPUOpen 文...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1912129762048074069">大模型精度：FP32、TF32、FP16、BF16、FP8、FP4、NF4、INT8</a></li>
<li><a href="https://blog.aiking.net:888/archives/shen-ru-jie-xi-xian-dai-ai-ji-suan-zhong-de-shu-ju-lei-xing-fp16bf16int8fp8">深入解析现代ai计算中的数据类型fp16bf16int8fp8 - 爱擎思考</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#RDNA 4m`, `#GPU`, `#On-Device AI`, `#AMD`

---

<a id="item-17"></a>
## [Tianba Previews MACO470 Mini PC with Ryzen AI 9 HX 470](https://www.ithome.com/0/932/371.htm) ⭐️ 7.0/10

Tianba (AOOSTAR) announced the MACO470 mini PC featuring AMD’s Ryzen AI 9 HX 470 processor, 32GB RAM, 1TB storage, and support for local OpenClaw execution, set to launch on April 1 at a price of 6XX9 yuan. This device highlights the growing trend of on-device AI inference by enabling local execution of autonomous AI agents like OpenClaw, reducing reliance on cloud infrastructure and improving latency—key for edge AI applications. Its compact form factor combined with high-end AI-capable hardware could influence mini PC design for AI workloads. The MACO470 is advertised with three PCIe Gen4 ×4 M.2 SSD slots and an external OCuLink port, despite the Ryzen AI 9 HX 470 having only 16 native PCIe lanes—a technical constraint that raises questions about how bandwidth is allocated among these interfaces.

rss · IT HOME · Mar 25, 02:01

**Background**: The AMD Ryzen AI 9 HX 470 is a 2026 mobile processor based on Zen 5/Zen 5c architectures, featuring 12 cores (24 threads) and integrated AI acceleration capabilities. OpenClaw is an open-source autonomous AI agent that uses large language models to perform tasks via messaging platforms. OCuLink is a PCIe-based external connectivity standard developed by PCI-SIG, enabling high-speed, low-latency connections for devices like eGPUs or NVMe storage using copper or optical cables.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/cpu-specs/ryzen-ai-9-hx-470.c4320">AMD Ryzen AI 9 HX 470 Specs | TechPowerUp CPU Database</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://www.howtogeek.com/what-is-oculink/">What is OCuLink? (And Why You Might Want It) - How-To Geek Oculink: The new interface for external graphics cards | PCWorld What Is OCuLink: A Beginner's Guide - optcore.net PCIe vs OCuLink : Choosing the Best Interface for Mini PCs ... OCuLink Interface - Delock What the heck is OcuLink and do I need to buy one? What Is OCuLink : A Beginner's Guide - optcore.net Which eGPU Interface Is Best? OCuLink , NVMe, or Thunderbolt? OCuLink Interface - Delock What Is OCuLink : A Beginner's Guide - optcore.net Which eGPU Interface Is Best? OCuLink, NVMe, or Thunderbolt?</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#Edge AI`, `#Mini PC`, `#AMD Ryzen AI`, `#On-Device Inference`

---

<a id="item-18"></a>
## [Amazon Acquires Humanoid Robot Startup Fauna Robotics](https://www.ithome.com/0/932/352.htm) ⭐️ 7.0/10

Amazon has acquired Fauna Robotics, a New York-based startup that recently launched Sprout, a $50,000 consumer-oriented humanoid robot designed for safe interaction in human environments. The deal includes Fauna’s ~50 employees joining Amazon’s personal robotics division, and Sprout will continue to be available to external researchers post-acquisition. This acquisition signals Amazon’s strategic push into embodied AI and consumer-facing physical agents, aligning with broader industry trends where tech giants invest in humanoid platforms as extensions of AI ecosystems. It also highlights growing commercial interest in socially interactive robots for homes, schools, and research. The Sprout robot is built on NVIDIA Jetson Orin hardware, stands 107 cm tall, supports natural voice interaction, performs gestures like waving and high-fives, and offers 3 hours of battery life. Despite the acquisition, Fauna will keep supplying Sprout to researchers as a development platform.

rss · IT HOME · Mar 25, 01:34

**Background**: Embodied AI refers to artificial intelligence systems that interact with the physical world through robotic bodies, requiring integration of perception, reasoning, and motor control. Humanoid robots like Sprout are designed not for industrial tasks but for social and domestic settings, emphasizing safety, intuitive interaction, and adaptability. Recent advances in AI hardware (e.g., NVIDIA Jetson) and large language models have accelerated development of such platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://faunarobotics.com/">Fauna Robotics | Capable, Safe, Fun Robots for Everyone</a></li>
<li><a href="https://apnews.com/article/amazon-humanoid-robot-fauna-sprout-f51ced4a097b1af56b0b2561cdca8fef">Amazon buys Fauna Robotics, maker of the Sprout humanoid robot</a></li>
<li><a href="https://www.cnbc.com/2026/03/24/amazon-humanoid-maker-fauna-robotics-sprout.html">Amazon acquires 'approachable' humanoid maker Fauna Robotics HUMANOID ROBOTICS | Amazon Acquires Fauna Robotics to Advance ... Amazon acquires humanoid developer Fauna Robotics - The Robot ... Amazon Acquires Fauna Robotics, Entering Consumer Humanoid ... Fauna Robotics Unveils Sprout, a Humanoid Platform Built for ...</a></li>

</ul>
</details>

**Tags**: `#Robotics`, `#AI Hardware`, `#Embodied AI`, `#Corporate Strategy`, `#Humanoid Robots`

---

<a id="item-19"></a>
## [China Sets New 2.5 Pb/s Optical Fiber Record](https://www.ithome.com/0/932/351.htm) ⭐️ 7.0/10

Researchers from China Information Technology Corporation (CICT), Peng Cheng Laboratory, and Furukawa Optical Fiber have achieved a world-record 2.5 petabits per second (Pb/s) real-time bidirectional transmission over a 24-core single-mode fiber using S+C+L band multiplexing. This breakthrough was recognized as a high-scoring paper at OFC 2026 and featured in an invited SCI journal article. This advancement directly addresses the exploding bandwidth demands of AI training, large-scale data centers, and next-generation networks by demonstrating a scalable, commercially viable path beyond traditional single-mode fiber limits. It validates space-division multiplexing and multi-band transmission as practical solutions for future AI infrastructure. The system uses 24-core fiber with S+C+L bands (19.65 THz total bandwidth), 262 WDM channels, and commercial 400G coherent modules based on 64GBaud PDM-16QAM, creating 6,288 parallel channels. Crucially, it achieves stable bidirectional transmission without complex MIMO processing by optimizing core allocation to suppress crosstalk.

rss · IT HOME · Mar 25, 01:32

**Background**: Traditional optical fibers use a single core and are approaching their theoretical capacity limit due to nonlinear effects and bandwidth constraints. Space-division multiplexing (SDM) increases capacity by using multiple spatial paths—either through multi-core fibers (multiple cores in one cladding) or few-mode fibers. Meanwhile, expanding transmission beyond the conventional C-band to include S and L bands significantly widens the usable optical spectrum, enabling higher aggregate data rates.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/空分复用技术/22291444">空分复用技术_百度百科</a></li>
<li><a href="https://www.cww.net.cn/article?id=608288">光全重实验室最新成果—《基于24芯单模光纤S+C+L波段实时双向2.5 Pb/s...</a></li>
<li><a href="https://baike.baidu.com/item/多芯光纤传输系统/67443166">多芯光纤传输系统_百度百科</a></li>

</ul>
</details>

**Tags**: `#Optical Communication`, `#AI Infrastructure`, `#Networking`, `#Research`, `#Data Transmission`

---