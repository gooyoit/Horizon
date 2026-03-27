---
layout: default
title: "Horizon Summary: 2026-03-27 (EN)"
date: 2026-03-27
lang: en
---

> From 86 items, 13 important content pieces were selected

---

1. [LiteLLM PyPI Package Compromised in Supply Chain Attack](#item-1) ⭐️ 9.0/10
2. [Xiaomi's MiMo-V2-Pro Tops OpenRouter with 3T Weekly Tokens](#item-2) ⭐️ 9.0/10
3. [Anthropic Wins Preliminary Injunction Against U.S. Ban on Claude](#item-3) ⭐️ 9.0/10
4. [Google Launches Real-Time Multimodal AI Model Gemini 3.1 Flash Live](#item-4) ⭐️ 9.0/10
5. [Apple to Open Siri to Third-Party AI Assistants in iOS 27](#item-5) ⭐️ 9.0/10
6. [Interactive Tutorial Demystifies LLM Quantization and Floating-Point Basics](#item-6) ⭐️ 8.0/10
7. [ByteDance Launches Dreamina Seedance 2.0 Globally via CapCut](#item-7) ⭐️ 8.0/10
8. [ChatGPT Ad Pilot Hits $100M Annualized Revenue](#item-8) ⭐️ 8.0/10
9. [Anvil Enables Parallel Execution of Claude Instances](#item-9) ⭐️ 8.0/10
10. [AI Rewrites JSONata in Go in One Day](#item-10) ⭐️ 7.0/10
11. [Zhixing Robotics Raises Nearly ¥100M for Dexterous Hands](#item-11) ⭐️ 7.0/10
12. [Google Adds Post-Quantum Cryptography to Android 17](#item-12) ⭐️ 7.0/10
13. [CAS Launches Open-Source Xiangshan RISC-V CPU and Ruyi OS](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM PyPI Package Compromised in Supply Chain Attack](https://simonwillison.net/2026/Mar/26/response-to-the-litellm-malware-attack/#atom-everything) ⭐️ 9.0/10

On March 24–26, 2026, versions 1.82.7 and 1.82.8 of the widely used LiteLLM Python package were found to contain a malicious litellm_init.pth file that executes credential-stealing code automatically upon Python startup. The discovery was made by ML engineer Callum McMahon, who used Anthropic’s Claude to analyze the malware in real time and coordinate disclosure with PyPI security. This incident exposes critical vulnerabilities in the AI/ML software supply chain, as LiteLLM is a foundational tool for routing LLM API calls across providers. The attack affected potentially hundreds of thousands of developers and systems, highlighting how compromised open-source packages can become vectors for large-scale data theft. The malware resides in a 34,628-byte litellm_init.pth file inside the PyPI wheel, which leverages Python’s .pth execution mechanism to run base64-encoded malicious code on every interpreter launch—without requiring an import of litellm. The payload exfiltrates environment variables and credentials, and evidence suggests the attacker compromised a maintainer’s PyPI account.

rss · Simon Willison · Mar 26, 23:58

**Background**: LiteLLM is a popular open-source library that simplifies calling APIs from various large language models (like OpenAI, Anthropic, and open-source models) through a unified interface. PyPI (Python Package Index) is the default repository for distributing Python packages, and .pth files are configuration files that Python automatically executes during startup if placed in site-packages. This makes them a stealthy vector for persistent malware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/popular-litellm-pypi-package-compromised-in-teampcp-supply-chain-attack/">Popular LiteLLM PyPI package backdoored to steal credentials ...</a></li>
<li><a href="https://docs.litellm.ai/blog/security-update-march-2026">Security Update: Suspected Supply Chain Incident - liteLLM</a></li>
<li><a href="https://www.truesec.com/hub/blog/malicious-pypi-package-litellm-supply-chain-compromise">Malicious PyPI Package - LiteLLM Supply Chain Compromise - Truesec</a></li>

</ul>
</details>

**Discussion**: Community members praised the real-time use of Claude to safely analyze the threat and emphasized the need for better monitoring of package registries. Some warned about the risks of LLM agents executing commands without safety guardrails, while others called for PyPI to provide real-time update feeds to enable faster community-driven detection.

**Tags**: `#AI Security`, `#LLM`, `#Supply Chain Attack`, `#Malware`, `#DevSecOps`

---

<a id="item-2"></a>
## [Xiaomi's MiMo-V2-Pro Tops OpenRouter with 3T Weekly Tokens](https://36kr.com/newsflashes/3740507252670720?f=rss) ⭐️ 9.0/10

Xiaomi's MiMo-V2-Pro, a 1-trillion-parameter Mixture-of-Experts (MoE) model, became the first model on OpenRouter to exceed 3 trillion weekly tokens and captured over 30% of the programming market share. This milestone signals strong real-world adoption of a Chinese-developed large language model in agentic and coding tasks, challenging dominant Western models with high performance at lower cost. It reflects a shift toward efficient, scalable MoE architectures in the competitive LLM landscape. MiMo-V2-Pro has 1 trillion total parameters with 42 billion active parameters per token, supports a 1-million-token context window, and is optimized for agentic workflows and coding—reportedly rivaling Claude Sonnet 4.6 in performance at a fraction of the cost.

rss · 36kr · Mar 27, 01:35

**Background**: Mixture of Experts (MoE) is an architecture where a model routes inputs to specialized sub-networks ('experts'), activating only a subset per request to balance capacity and efficiency. This approach enables trillion-parameter models like MiMo-V2-Pro to maintain high performance without proportional compute costs. MoE has been used in models from Google, Mistral, and now Xiaomi to scale intelligently while controlling inference expenses.

<details><summary>References</summary>
<ul>
<li><a href="https://awesomeagents.ai/models/mimo-v2-pro/">Xiaomi MiMo - V 2 - Pro - Agentic 1T MoE Model | Awesome Agents</a></li>
<li><a href="https://nowletus.com/news/xiaomi-stuns-with-new-mimo-v2-pro-llm-nearing-gpt-5-2-opus-4-6-performance-at-a-fraction-of-the-cost-now870.html">Xiaomi stuns with new MiMo - V 2 - Pro LLM nearing... | NOW LET US</a></li>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts (MoE)? How It Works, Use Cases & More | DataCamp</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#AI Infrastructure`, `#Model Adoption`, `#Agent AI`

---

<a id="item-3"></a>
## [Anthropic Wins Preliminary Injunction Against U.S. Ban on Claude](https://www.ithome.com/0/933/160.htm) ⭐️ 9.0/10

A U.S. federal judge granted Anthropic a preliminary injunction blocking the Trump administration’s ban on its Claude AI model, ruling that the government likely violated the First Amendment and lacked legal justification for national security claims. This ruling challenges the U.S. government’s authority to restrict domestic AI companies under national security pretexts without due process, setting a potential precedent for how AI regulation intersects with free speech and corporate rights. Judge Rita Lin criticized the government’s actions as retaliatory for Anthropic’s public stance on AI safety, noting the company is the first U.S. firm labeled a 'supply chain risk'—a designation previously reserved for foreign adversaries. The injunction halts enforcement while the case proceeds, which may take months.

rss · IT HOME · Mar 27, 02:11

**Background**: The U.S. government has historically used 'supply chain risk' designations to restrict foreign technology deemed threatening to national security, such as with Huawei or TikTok. Anthropic, co-founded by former OpenAI researchers, develops the Claude series of large language models and emphasizes AI safety and constitutional AI principles. The Trump administration’s executive actions against AI tools raised concerns about overreach in emerging tech governance.

**Tags**: `#AI Policy`, `#LLM`, `#Anthropic`, `#Legal`, `#National Security`

---

<a id="item-4"></a>
## [Google Launches Real-Time Multimodal AI Model Gemini 3.1 Flash Live](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/) ⭐️ 9.0/10

Google has launched Gemini 3.1 Flash Live, a real-time multimodal AI model supporting over 90 languages, now integrated into Gemini Live, Search Live, enterprise APIs, and Google AI Studio. It enables faster responses, extended context retention (2x longer), and improved audio processing in noisy environments. This release significantly advances real-time conversational AI by enabling seamless, voice-first interactions across consumer and enterprise applications at global scale. It positions Google to compete more effectively in the growing market for live, multimodal AI assistants that understand and respond to complex, contextual user inputs. Gemini 3.1 Flash Live is based on Gemini 3 Pro, supports multimodal inputs (text, images, audio, video) with a 128K-token context window, and generates both audio and text outputs. It excels in prosody understanding—such as pitch and speech rate—and robust tool use for executing complex tasks during live conversations.

telegram · zaihuapd · Mar 26, 17:01

**Background**: Multimodal AI models process and generate information across multiple data types—such as text, speech, images, and video—enabling more natural human-computer interaction. Real-time audio AI, like Gemini Live, aims to support continuous, low-latency voice conversations with memory of prior exchanges, moving beyond turn-based chat interfaces. Google’s Gemini series represents its flagship large language models, with variants optimized for speed (Flash), quality (Pro), or real-time interaction (Flash Live).

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-1-flash-live/">Gemini 3.1 Flash Live - Model Card — Google DeepMind</a></li>
<li><a href="https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Flash-Live-Model-Card.pdf">Gemini 3.1 Flash with Native Audio Capabilities (Flash Live)</a></li>
<li><a href="https://wallstreetcn.com/articles/3768515">谷歌发布最高质量音频模型Gemini 3.1 Flash Live，低延迟、高精度响应...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Multimodal AI`, `#Real-time AI`, `#Gemini`, `#AI Deployment`

---

<a id="item-5"></a>
## [Apple to Open Siri to Third-Party AI Assistants in iOS 27](https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27?srnd=phx-technology) ⭐️ 9.0/10

Apple plans to allow third-party AI assistants like Gemini and Claude to integrate directly with Siri in iOS 27, enabling users to route queries through these services just as they currently can with ChatGPT. This marks an expansion beyond ChatGPT’s current exclusive integration within Apple Intelligence. This move signals a strategic shift toward an open AI ecosystem on iPhone, fostering competition among large language models and giving users more choice while positioning Apple as a platform orchestrator rather than a sole AI provider. It could accelerate adoption of on-device and cloud-based LLMs across the mobile landscape. Integration will be managed through the App Store, with user-controlled toggles in Apple Intelligence and Siri settings; however, the feature remains subject to change or delay before its official WWDC unveiling on June 8, 2026.

telegram · zaihuapd · Mar 27, 01:40

**Background**: Apple Intelligence is Apple's generative AI system, introduced in June 2024 for iOS 18, iPadOS 18, and macOS Sequoia, combining on-device and cloud processing. It initially integrated only ChatGPT as an external LLM option. Supported devices include iPhone 15 Pro/Pro Max and iPhone 16 series, along with M1-or-later Macs and iPads. Notably, Apple Intelligence remains unavailable in mainland China due to regulatory constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence - Apple</a></li>

</ul>
</details>

**Tags**: `#AI Assistants`, `#Siri`, `#iOS 27`, `#LLM Integration`, `#Apple Intelligence`

---

<a id="item-6"></a>
## [Interactive Tutorial Demystifies LLM Quantization and Floating-Point Basics](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose published an interactive, in-depth tutorial titled 'Quantization from the ground up,' which explains LLM quantization techniques and includes a visual tool for understanding binary floating-point representation. The piece also introduces the concept of 'outlier values'—rare but critical weights that significantly impact model performance if removed. This tutorial makes a complex but essential AI engineering technique—quantization—accessible to practitioners, enabling more efficient model deployment on resource-constrained hardware. Understanding outlier handling and precision trade-offs helps developers optimize models without catastrophic quality loss. The tutorial demonstrates that reducing precision from 16-bit to 8-bit incurs almost no quality penalty, while 4-bit quantization retains about 90% of original performance depending on the metric. It uses llama.cpp’s perplexity tool and GPQA benchmark on Qwen 3.5 9B to evaluate accuracy impact, and explains how some quantization schemes preserve outliers via separate storage.

rss · Simon Willison · Mar 26, 16:21

**Background**: LLM quantization is a model compression technique that converts high-precision weights (e.g., 16-bit floats) into lower-precision formats (e.g., 8-bit or 4-bit integers) to reduce memory usage and accelerate inference. Binary floating-point representation, standardized by IEEE 754, encodes real numbers using sign, exponent, and significand fields—critical for understanding numerical precision limits in AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single-precision_floating-point_format">Single-precision floating-point format - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#AI Engineering`, `#Model Optimization`, `#Technical Tutorial`

---

<a id="item-7"></a>
## [ByteDance Launches Dreamina Seedance 2.0 Globally via CapCut](https://www.ithome.com/0/933/197.htm) ⭐️ 8.0/10

ByteDance has officially launched CapCut Video Studio powered by its new multimodal AI model, Dreamina Seedance 2.0, enabling end-to-end AI-assisted video creation without a traditional timeline. The tool is now available in Africa, South America, the Middle East, and Southeast Asia, with support for 15-second videos and six aspect ratios. This launch marks a significant step in democratizing professional-grade video creation through generative AI, integrating storyboarding, character design, and editing into one seamless workflow. Its strict copyright safeguards and content provenance features also set a precedent for responsible AI deployment in creative tools. Dreamina Seedance 2.0 supports video generation up to 15 seconds without reference images, includes visible AI watermarks and C2PA-compliant content credentials, and uses an 'invisible watermark' for off-platform identification. It also restricts generation from real human faces during initial rollout and blocks unauthorized IP use via active monitoring and creator collaboration.

rss · IT HOME · Mar 27, 02:33

**Background**: Dreamina Seedance 2.0 is a multimodal generative AI model developed by ByteDance for video synthesis, part of its broader Dreamina suite integrated into CapCut (known as Jianying in China). Multimodal AI models like this combine text, image, and audio understanding to generate coherent video content. CapCut, originally a mobile video editor, has evolved into an AI-powered creative platform competing with tools like Runway and Pika Labs.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/03/26/bytedances-new-ai-video-generation-model-dreamina-seedance-2-0-comes-to-capcut/">ByteDance's new AI video generation model , Dreamina Seedance ...</a></li>
<li><a href="https://www.capcut.com/ai-creator/start">CapCut video studio ｜The all-in-one canvas for video creation</a></li>
<li><a href="https://dreamina.capcut.com/tools/seedance-2-0">Free Seedance 2 . 0 — Multimodal AI Video Creator Online</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#Multimodal Models`, `#Video Generation`, `#AI Tools`, `#LLM`

---

<a id="item-8"></a>
## [ChatGPT Ad Pilot Hits $100M Annualized Revenue](https://www.ithome.com/0/933/157.htm) ⭐️ 8.0/10

OpenAI's ChatGPT ad pilot in the U.S. has generated over $100 million in annualized revenue within six weeks and attracted more than 600 advertisers, primarily targeting free and low-tier Go subscribers. This marks a pivotal shift in OpenAI’s monetization strategy, demonstrating that advertising can become a major revenue stream for AI platforms without compromising user trust—potentially reshaping how generative AI products are commercialized globally. Ads are shown only to about 20% of eligible users daily (85% of U.S. users qualify), remain separate from ChatGPT’s responses, and do not share user conversations with advertisers; relevance and low close rates indicate early success.

rss · IT HOME · Mar 27, 02:01

**Background**: ChatGPT, developed by OpenAI, is one of the world’s most widely used AI chatbots, offering both free and paid tiers. As AI development costs soar, companies like OpenAI are exploring sustainable revenue models beyond subscriptions. Advertising in AI interfaces presents unique challenges around user experience, data privacy, and content integrity.

**Tags**: `#AI Monetization`, `#ChatGPT`, `#Advertising`, `#OpenAI`, `#Business Strategy`

---

<a id="item-9"></a>
## [Anvil Enables Parallel Execution of Claude Instances](https://www.producthunt.com/products/anvil-5) ⭐️ 8.0/10

Anvil is a new developer tool that allows users to run multiple instances of Anthropic’s Claude AI model in parallel, significantly enhancing workflow scalability for coding and automation tasks. This capability addresses a key bottleneck in using large language models for complex, multi-step tasks by enabling concurrent execution—critical for developers and researchers building AI agent teams or automating large-scale workflows. Anvil appears to specialize in orchestrating 'a fleet' of Claude instances, likely through browser-based agents or API coordination, as suggested by community examples involving web automation and collaborative code generation.

producthunt · Zachary Denham · Mar 26, 06:59

**Background**: Claude, developed by Anthropic, is a leading large language model (LLM) known for strong reasoning and coding capabilities. Running multiple instances in parallel—often called 'agent teams'—allows decomposition of complex problems into subtasks handled simultaneously, improving efficiency and reducing latency. This approach is increasingly used in AI research and development for tasks like software compilation, data scraping, and automated testing.

<details><summary>References</summary>
<ul>
<li><a href="https://fazm.ai/blog/claude-code-parallel-instances-ctrl-c-muscle-memory">Running 5 Claude Code Instances in Parallel ... - Fazm Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/parallel-browser-agents-claude-code">Parallel Browser Agents: How to Run Multiple Claude Code Instances ...</a></li>
<li><a href="https://www.anthropic.com/engineering/building-c-compiler">Building a C compiler with a team of parallel Claudes \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Developers have shared experiences running multiple Claude Code instances for tasks like form filling and building compilers, noting both the power and operational challenges—such as managing processes and inconsistent UX feedback.

**Tags**: `#AI`, `#LLM`, `#Claude`, `#Developer Tools`, `#Parallel Computing`

---

<a id="item-10"></a>
## [AI Rewrites JSONata in Go in One Day](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

A team at Reco used large language models (LLMs) to rewrite the JSONata expression language from JavaScript to Go in under a day, achieving behaviorally identical results validated by the original test suite and a week-long shadow deployment. This demonstrates a high-impact, real-world application of 'vibe porting'—using AI to migrate critical software with minimal human effort—resulting in an estimated $500K annual cost saving and faster, more maintainable infrastructure. The project cost only $400 in LLM token usage and took 7 hours to produce a working version; correctness was ensured via JSONata’s comprehensive existing test suite and confirmed through parallel shadow deployment against the original implementation.

rss · Simon Willison · Mar 27, 00:35

**Background**: JSONata is a lightweight, open-source query and transformation language for JSON data, similar to jq but with richer expression capabilities. It is widely used in data integration tools like Node-RED. 'Vibe porting' refers to using AI to replicate software behavior in a new language or framework based on examples, tests, and conversational prompts rather than formal specifications.

<details><summary>References</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata</a></li>
<li><a href="https://devopstales.github.io/ai/ai-software-development-spec-vs-vibe/">AI Software Development: Spec-Driven vs. Vibe Coding</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Software Engineering`, `#Go`, `#JSONata`

---

<a id="item-11"></a>
## [Zhixing Robotics Raises Nearly ¥100M for Dexterous Hands](https://36kr.com/p/3740523277517063?f=rss) ⭐️ 7.0/10

Chinese robotics firm Zhixing Robotics has secured nearly RMB 100 million across two consecutive funding rounds (B+ and B++) to advance its full-stack dexterous hand technologies and embodied intelligence solutions. The company has launched two new products: the four-finger 'Lingsi Hand' for industrial logistics and the five-finger tendon-driven 'Shuqiao Hand' with adaptive left-right data collection capability. Advanced dexterous hands are critical hardware enablers for embodied AI, allowing robots to interact reliably with the physical world in industrial and high-end service settings. Zhixing’s progress in cost-effective, high-reliability designs and data-efficient training could accelerate real-world deployment of general-purpose manipulation capabilities in China’s rapidly growing robotics ecosystem. The 'Lingsi Hand' features 12 joints, 8 active DOFs, 5kg payload, and integrated servo control for easy integration with collaborative arms. The 'Shuqiao Hand' uses biomimetic tendon drive with 16 joints and 11 active DOFs, enabling one hand to collect both left- and right-handed operation data—halving data acquisition costs. Both hands leverage Zhixing’s proprietary underactuated, reconfigurable, and flexible adaptive mechanisms, and the company claims its data-collection hands endure over 5 million cycles—100x industry average.

rss · 36kr · Mar 27, 01:37

**Background**: Embodied intelligence (or embodied AI) refers to intelligent systems that learn through physical interaction with their environment, integrating perception, action, and cognition. Dexterous hands—robotic end-effectors mimicking human hand structure and function—are essential for complex manipulation tasks and represent one of the most challenging components in robotics due to constraints on size, weight, actuation, and sensing. Tendon-driven and underactuated designs are common approaches to balance dexterity, reliability, and cost, especially as the industry moves toward scalable deployment in logistics, manufacturing, and healthcare.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/具身智能/63286570">具身智能（智能体通过身体将感知、行动与认知深度融合的智能系统）_...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/678744015">机器人灵巧手行业深度：市场现状、未来发展方向、核心部位及相关企业... 灵巧手（人形机器人末端执行器）_百度百科 Images 灵巧手技术全景解析（一）：从三大核心到应用场景的完整指南 - 艾邦机... 百亿独角兽，为人形机器人放「手」一搏-36氪 Top Stories 机器人着力展示“打工”技能 灵巧手厂商关注度提升｜2026中关村论坛年会... 机器人灵巧手：技术演进、市场格局与未来前景 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位 机器人 灵巧手 行业深度：市场现状、未来发展方向、核心部位</a></li>
<li><a href="https://baike.baidu.com/item/灵巧手/67387238">灵巧手（人形机器人末端执行器）_百度百科</a></li>

</ul>
</details>

**Tags**: `#Embodied AI`, `#Robotics`, `#Hardware`, `#Dexterous Manipulation`, `#AI Infrastructure`

---

<a id="item-12"></a>
## [Google Adds Post-Quantum Cryptography to Android 17](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) ⭐️ 7.0/10

Google has integrated post-quantum cryptography (PQC) into Android 17, adding quantum-resistant digital signatures to the bootloader and upgrading the Keystore system to PQC-compliant standards. This move future-proofs Android security against emerging quantum computing threats that could break current public-key cryptography, ensuring long-term integrity of device boot chains and secure communications—critical for mobile AI and sensitive applications. The implementation covers the Verified Boot chain and Keystore, using NIST-standardized or candidate PQC algorithms ahead of the 2030 mandate; it aims to protect both device integrity during startup and cryptographic operations during runtime.

telegram · zaihuapd · Mar 26, 07:09

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to be secure against attacks by quantum computers. Current public-key systems like RSA and ECC could be broken by Shor’s algorithm on a sufficiently powerful quantum computer. NIST has been standardizing PQC algorithms since 2016, with final standards expected this decade. Google and other tech leaders are proactively integrating PQC to mitigate 'harvest now, decrypt later' risks.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/security/resources/post-quantum-cryptography?hl=zh-CN">后量子加密 (PQC) | Google Cloud</a></li>
<li><a href="https://winbuzzer.com/2026/03/26/google-android-17-quantum-resistant-encryption-pqc-xcxwbn/">Android 17 Gets Quantum-Safe Encryption Across Full Security ...</a></li>
<li><a href="https://www.secrss.com/articles/79273">MITRE后量子密码学 (PQC) 迁移路线图深度解读 - 安全内参 | 决策者的...</a></li>

</ul>
</details>

**Tags**: `#Post-Quantum Cryptography`, `#Android`, `#Security`, `#Quantum Computing`, `#Mobile OS`

---

<a id="item-13"></a>
## [CAS Launches Open-Source Xiangshan RISC-V CPU and Ruyi OS](https://h.xinhuaxmt.com/vh512/share/13024070?docid=13024070) ⭐️ 7.0/10

The Chinese Academy of Sciences (CAS) unveiled the open-source 'Xiangshan' high-performance RISC-V processor and the 'Ruyi' native operating system, and announced a joint initiative to co-develop next-generation chip-OS systems with major Chinese tech firms including Alibaba, Tencent, and ByteDance. This effort strengthens China’s domestic computing infrastructure by creating an open, customizable hardware-software stack based on RISC-V, which can support AI workloads and reduce reliance on foreign architectures like x86 and ARM. The collaboration with leading tech companies signals strong industry alignment and potential for scalable AI-ready platforms. The 'Xiangshan' processor has achieved international performance levels and includes the world’s first open-source on-chip interconnect network IP; the 'Ruyi' OS fully supports international standards. Commercial chips based on Xiangshan are already in mass production by companies like Bluechip Computing and ESWIN.

telegram · zaihuapd · Mar 26, 10:08

**Background**: RISC-V is an open instruction set architecture (ISA) that allows anyone to design, manufacture, and sell RISC-V chips and software without licensing fees. Unlike proprietary ISAs such as x86 (Intel/AMD) or ARM, RISC-V promotes customization and innovation, making it attractive for AI accelerators, edge devices, and sovereign computing initiatives. The Xiangshan project, launched by CAS’s Institute of Computing Technology in 2020, aims to build a high-performance, open-source RISC-V CPU core competitive with commercial offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://github.com/OpenXiangShan/XiangShan">GitHub - OpenXiangShan/XiangShan: Open-source high-performance RISC-V processor · GitHub</a></li>
<li><a href="https://openxiangshan.github.io/">XiangShan: An Open Source High Performance RISC-V Processor and Infrastructure for Architecture Research</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#Open Source Hardware`, `#Operating Systems`, `#Semiconductors`, `#AI Infrastructure`

---