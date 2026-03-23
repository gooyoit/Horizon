---
layout: default
title: "Horizon Summary: 2026-03-23 (ZH)"
date: 2026-03-23
lang: zh
---

> From 86 items, 12 important content pieces were selected

---

1. [MiniMax 升级全模态支持，计划两周内开源 MiniMax 2.7 权重](#item-1) ⭐️ 9.0/10
2. [AI 编程工具无法取代人类创新](#item-2) ⭐️ 8.0/10
3. [Flash-MoE 在笔记本电脑上运行 3970 亿参数 MoE 模型](#item-3) ⭐️ 8.0/10
4. [韩国 3 月前 20 天芯片出口同比飙升 163.9%](#item-4) ⭐️ 8.0/10
5. [Mistral AI 首席执行官提议欧盟对 AI 使用公开内容征税](#item-5) ⭐️ 8.0/10
6. [宇树科技进军家用机器人市场，2026 年人形机器人目标出货 2 万台](#item-6) ⭐️ 8.0/10
7. [Claude Code 测试交互式 /init 命令以自定义生成初始化文件](#item-7) ⭐️ 8.0/10
8. [Simon Willison 将 Starlette 1.0 与 Claude AI 技能集成](#item-8) ⭐️ 7.0/10
9. [基于 Claude 和 Pyodide 构建的 CRDT 合并状态可视化工具](#item-9) ⭐️ 7.0/10
10. [竹马创新获种子轮融资，推 3DGS 空间相机](#item-10) ⭐️ 7.0/10
11. [瑞莎推出 25 TOPS 边缘 AI 模组 AICore DX-M1M](#item-11) ⭐️ 7.0/10
12. [阿里千问上线自然语言打车功能](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MiniMax 升级全模态支持，计划两周内开源 MiniMax 2.7 权重](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 9.0/10

MiniMax 将其 Coding Plan 升级为 Token Plan，Plus 及以上套餐用户可调用视频、语音、音乐和图像等全模态模型，并宣布将在约两周内开源 MiniMax 2.7 的模型权重。新模型在 OpenClaw 基准测试中表现显著提升。 此举大幅扩展了开发者和研究人员对多模态 AI 能力的访问权限，而 MiniMax 2.7 开源权重的发布有望推动开源社区创新并加剧大模型领域的竞争。OpenClaw 基准得分的提升表明其在真实 AI Agent 场景中的性能更强。 工作日下午高峰时段（15:00–17:30），平台将实施动态限流，单周多模态调用量上限为原编程模型 5 小时用量的 10 倍。MiniMax 2.7 模型仍在积极迭代中，最新版本已在 OpenClaw 基准上取得明显进步。

telegram · zaihuapd · Mar 23, 02:09

**背景**: 全模态模型指能在单一架构中处理和生成文本、图像、音频、视频等多种数据类型的 AI 模型，支持更广泛的应用场景。OpenClaw 是一个新兴基准测试，专注于评估 AI Agent 在真实软件工程和推理任务中的完成能力。开源权重允许研究社区自由检查、微调和部署模型，不受厂商限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.openclaw.ai/zh-CN/help/testing">测试 - OpenClaw</a></li>
<li><a href="https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude">We Tested MiniMax M 2 . 7 Against Claude Opus 4.6 - by Darko</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2016823158380995920">我用两周时间踩完openclaw所有坑，总结出这份完整调教指南</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Multimodal AI`, `#Open Source`, `#Model Release`, `#AI Infrastructure`

---

<a id="item-2"></a>
## [AI 编程工具无法取代人类创新](https://stevekrouse.com/precision) ⭐️ 8.0/10

开发者报告称，Claude 等 AI 编程助手难以生成真正新颖的解决方案，即使被明确指示，也常常默认采用传统模式。例子包括设计无墓碑（tombstone-free）CRDT 和缺乏创新的编译器时的失败尝试。 这揭示了当前大语言模型的一个根本局限：由于受限于训练数据，它们无法独立推动软件工程领域的前沿发展。人类的批判性思维对于编程范式和系统设计的突破仍然至关重要。 在一个案例中，尽管开发者的目标是消除墓碑机制，AI 仍坚持在 CRDT 实现中使用墓碑——这是传统方法中的已知约束。另一个案例中，Chris Lattner 审查了一个由 AI 编写的编译器，发现其中毫无创新，只是复制了现有模式。

hackernews · stevekrouse · Mar 22, 11:09

**背景**: CRDT（无冲突复制数据类型）是在分布式系统中用于无需协调即可解决冲突的数据结构。墓碑（tombstones）是用来表示已删除元素的标记，可能积累并导致效率低下。编译器设计涉及创建将高级代码转换为机器指令的程序，需要深层次的概念创新。像 Claude 这样的大语言模型（LLM）虽然在海量代码库上训练，但缺乏真正的推理或创造力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/top-content/artificial-intelligence/ai-limitations-overview/limitations-of-ai-coding-tools/">Limitations of AI Coding Tools - LinkedIn</a></li>
<li><a href="https://allthingsopen.org/articles/ai-code-assistants-limitations">6 limitations of AI code assistants and why developers should ...</a></li>
<li><a href="https://arxiv.org/abs/2308.10620">[2308.10620] Large Language Models for Software Engineering: A Systematic Literature Review</a></li>

</ul>
</details>

**社区讨论**: 开发者担心 AI 编程工具会强化传统观念，阻碍新想法（如无墓碑 CRDT 或新编程语言）的发展。一些人担忧，如果没有人类先驱者产生原创工作，未来的 AI 模型将缺乏创新所需的训练数据。

**标签**: `#AI`, `#Programming`, `#LLM`, `#Software Engineering`, `#Research`

---

<a id="item-3"></a>
## [Flash-MoE 在笔记本电脑上运行 3970 亿参数 MoE 模型](https://github.com/danveloper/flash-moe) ⭐️ 8.0/10

Flash-MoE 通过结合 2 比特量化并将每个 token 激活的专家数量从 10 个减少到 4 个，在消费级笔记本电脑上运行 Qwen3.5-397B 混合专家（MoE）模型，实现了约每秒 5 个 token 的推理速度。 这一突破挑战了人们对超大规模 AI 模型硬件需求的固有认知，有望推动前沿级推理能力的普及化，但其采用的激进压缩手段可能显著影响模型输出质量。 该实现采用激进的 2 比特量化，并将每个 token 激活的专家数从标准的 10 个降至仅 4 个；它利用 Metal 在 Apple Silicon 上运行，据称在高端 MacBook 上可达到每秒 5 个 token。另有用户指出，在 128GB 内存设备上使用约 2.5 比特每权重（BPW）的量化方案可获得更优的质量和速度。

hackernews · mft_ · Mar 22, 11:30

**背景**: 混合专家（MoE）架构在每个输入 token 上仅激活部分“专家”子网络，使模型能在不显著增加计算成本的前提下扩展参数量。量化通过降低权重数值精度（如从 16 比特降至 2 比特）来减小内存占用并加速推理，但通常会牺牲一定准确性。运行数百亿乃至数千亿参数的模型通常需要多 GPU 服务器，因此在笔记本电脑上部署此类模型实属罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://skills.sh/aradotso/trending-skills/flash-moe-inference">flash - moe -inference by aradotso/trending-skills</a></li>
<li><a href="https://arxiv.org/html/2412.14219v2">A Survey on Inference Optimization Techniques for Mixture of ...</a></li>
<li><a href="https://apxml.com/courses/mixture-of-experts-advanced-implementation/chapter-4-efficient-moe-inference/moe-quantization-techniques">Quantization for MoE Layers</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：有人赞赏其工程创新和分层存储策略，也有人批评 2 比特量化和减少专家数量导致严重质量下降，认为标题具有误导性。另有用户指出，现有其他量化方法已能在高内存消费设备上以更优性能运行 397B MoE 模型，并提供了具体基准数据。

**标签**: `#LLM`, `#MoE`, `#Quantization`, `#Inference Optimization`, `#AI Hardware`

---

<a id="item-4"></a>
## [韩国 3 月前 20 天芯片出口同比飙升 163.9%](https://36kr.com/newsflashes/3734870653944070?f=rss) ⭐️ 8.0/10

受全球对 AI 服务器的强劲需求推动，韩国 3 月前 20 天半导体出口额同比激增 163.9%，达 187 亿美元，创历史新高。同期整体出口额同比增长 50.4%，达 533 亿美元，亦为历年同期最高。 这一激增凸显了 AI 基础设施扩张正直接拉动硬件需求，尤其是 AI 服务器所用的 HBM 等存储芯片。作为 DRAM 和 NAND 的主要生产国，韩国出口表现反映了 AI 热潮在全球科技供应链中引发的广泛经济连锁效应。 此次出口激增主要由存储芯片带动，海关数据显示仅半导体一项出口额就达 187 亿美元。同期进口额同比增长 19.7%至 412 亿美元，贸易顺差达 121 亿美元。

rss · 36kr · Mar 23, 01:46

**背景**: AI 服务器需要专用的高带宽内存（HBM），这是一种针对并行处理任务中海量数据流优化的 DRAM。与传统服务器不同，AI 服务器通常将高性能 GPU 与 HBM 结合，以加速大语言模型的训练和推理。主要云服务商已大幅增加此类系统的采购，促使半导体制造商将产能从消费级存储芯片转向 HBM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20260112/herald/cf62ca8440b204fad9c1b1ecaeffb4d8.html">存 储 芯 片 持续“高烧”，手机行业迎“大浪淘沙” - 21经济网</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD000020240718976215.html">芯 片 供应瓶颈缓解， AI 服 务 器 将迎出货爆发期</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Semiconductors`, `#Export Data`, `#Memory Chips`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [Mistral AI 首席执行官提议欧盟对 AI 使用公开内容征税](https://www.ithome.com/0/931/586.htm) ⭐️ 8.0/10

Mistral AI 首席执行官 Arthur Mensch 提议对在欧洲运营的 AI 公司征收基于收入的“在线公开内容使用税”，税率建议为 1.0%至 1.5%，以支持内容创作者并确保公平竞争。 该提议旨在解决欧盟严格版权法规与全球 AI 企业规避行为之间的失衡，可能重塑 AI 训练数据的合法获取方式，并在 AI 快速发展背景下支持欧洲文化产业。 拟议中的税收将适用于所有在欧洲提供服务的 AI 公司，并与现有的深度合作授权模式并行；所获资金将用于资助新内容创作并向权利人提供补偿。

rss · IT HOME · Mar 23, 01:21

**背景**: 大语言模型（LLM）的训练需要大量文本数据，通常来自公开网络内容。欧洲的版权法比其他地区更严格，尤其在文本与数据挖掘（TDM）方面。欧盟《版权指令》虽包含 TDM 例外条款，但允许权利人选择退出，导致 AI 开发者面临法律不确定性。与此同时，非欧洲 AI 公司可能在更宽松的监管环境下运营，甚至忽略“退出”声明，从而获得竞争优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iosconews.com/news/nation/article_71f533a6-9578-54fb-8233-5ad5e50f6f7d.html">Mistral chief calls for European AI levy to pay creatives | Nation | iosconews.com</a></li>
<li><a href="https://kdhnews.com/news/nation/mistral-chief-calls-for-european-ai-levy-to-pay-creatives/article_7117dd20-4b39-54fd-9516-4f58f94d74b1.html">Mistral chief calls for European AI levy to pay creatives | News | kdhnews.com</a></li>
<li><a href="https://www.caict.ac.cn/kxyj/qwfb/bps/202412/P020241227660032159191.pdf">caict.ac.cn/kxyj/qwfb/bps/202412/P020241227660032159191.pdf</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Copyright`, `#LLM`, `#Regulation`, `#European AI`

---

<a id="item-6"></a>
## [宇树科技进军家用机器人市场，2026 年人形机器人目标出货 2 万台](https://www.eweek.com/news/unitree-20000-humanoid-robots-2026-china/) ⭐️ 8.0/10

中国机器人公司宇树科技计划将人形机器人年产量从 2025 年的约 5500 台提升至 2026 年的 2 万台，并在三年内推出家用机器人。公司正筹备在上海证券交易所 IPO，拟募资 42 亿元人民币用于人形机器人平台研发。 此举使宇树科技成为特斯拉 Optimus 在消费级人形机器人市场的重要竞争者，并彰显中国在 AI 驱动机器人领域的快速崛起。大规模量产有望加速 AI 实体化落地，并推动家用机器人成本下降。 宇树的人形机器人（如 H1 和 Go2）配备 4D 超广角激光雷达，并宣称通过大模型 GPT 实现具身智能。该公司最初专注于四足机器人，2024 年才进入人形机器人领域，当前产品售价约 1.6 万美元。

telegram · zaihuapd · Mar 22, 04:15

**背景**: 特斯拉 Optimus 和宇树 H1 等人形机器人旨在人类环境中执行通用任务，需融合高级 AI、灵巧操作与双足行走能力。具身智能（embodied AI）——即通过物理交互产生智能——被视为超越纯软件 AI 的关键前沿。宇树科技成立于 2016 年，早期以高性价比四足机器人闻名，后拓展至人形机器人领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>
<li><a href="https://www.unitree.com/h1/">Universal humanoid robot H1_Bipedal Robot_Humanoid Intelligent Robot Company | Unitree Robotics</a></li>
<li><a href="https://shop.unitree.com/collections/humanoid-robot">Humanoid Robot - Unitree</a></li>

</ul>
</details>

**标签**: `#Humanoid Robots`, `#AI Hardware`, `#Robotics`, `#Tesla Optimus`, `#China Tech`

---

<a id="item-7"></a>
## [Claude Code 测试交互式 /init 命令以自定义生成初始化文件](https://x.com/trq212/status/2035799806640115806) ⭐️ 8.0/10

Claude Code 正在测试一个新的交互式 /init 命令，会在进入代码库探索或编写前先询问用户要生成哪些初始化文件（如 CLAUDE.md、skills 和 hooks）。该功能目前通过环境变量 CLAUDE_CODE_NEW_INIT 启用。 此更新增强了开发者对 AI 辅助初始化过程的控制，支持根据实际工作流需求定制项目配置。这表明 Claude Code 正朝着更响应用户反馈、以开发者为中心的工具方向演进，在竞争激烈的 AI 编程助手生态中具有重要意义。 启用新 /init 模式后，用户可交互式选择要创建的文件；否则默认仅生成 CLAUDE.md。该功能目前为实验性，需通过设置环境变量激活。

telegram · zaihuapd · Mar 23, 01:51

**背景**: Claude Code 是一款 AI 驱动的编程助手，通过名为 CLAUDE.md 的特殊 Markdown 文件为特定代码库定制其行为。该文件提供项目结构、编码规范和目标等上下文信息，使 AI 能提供更准确、相关的协助。/init 命令用于自动初始化此类配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/using-claude-md-files">Using CLAUDE . MD files : Customizing Claude Code for your codebase</a></li>
<li><a href="https://code.claude.com/docs/en/cli-reference">Complete reference for Claude Code command -line interface...</a></li>

</ul>
</details>

**标签**: `#AI Coding`, `#Claude`, `#Developer Tools`, `#LLM`, `#Software Engineering`

---

<a id="item-8"></a>
## [Simon Willison 将 Starlette 1.0 与 Claude AI 技能集成](https://simonwillison.net/2026/Mar/23/starlette-1-skill/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一项实验，展示如何使用 Anthropic 的 Claude AI “技能”与基于 Starlette 1.0（一个 Python ASGI Web 框架）构建的应用进行交互并增强其功能。该实验包括创建一个可理解并协助处理 Starlette 特定开发任务的自定义 AI 技能。 这项工作展示了大语言模型驱动的开发者工具在现代 Web 框架中的实际应用，有望加速原型开发并减少 Python 异步服务的样板代码。它还展示了 AI 技能如何针对特定技术领域进行定制，而不仅限于通用编程辅助。 该实验利用 Claude 的自定义技能功能（可通过 claude.ai 或 API 使用），将 Starlette 1.0 的文档和使用模式嵌入 AI 的上下文中。该技能旨在通过结构化的领域知识，帮助生成、解释或调试基于 Starlette 的代码。

rss · Simon Willison · Mar 23, 00:05

**背景**: Starlette 是一个轻量级、可用于生产的 ASGI（异步服务器网关接口）框架，用于构建高性能的 Python 异步 Web 服务。它提供 WebSocket 支持、后台任务和中间件等核心功能，常被用作 FastAPI 等其他框架的基础。Claude AI 技能是可重用的领域专业知识包，使 AI 能在对话中一致地执行特定任务，例如在特定上下文中生成代码或分析数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview">Agent Skills - Claude API Docs</a></li>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://claude.com/skills">Skills | Claude</a></li>

</ul>
</details>

**标签**: `#AI Skills`, `#LLM`, `#Starlette`, `#Web Framework`, `#Developer Tools`

---

<a id="item-9"></a>
## [基于 Claude 和 Pyodide 构建的 CRDT 合并状态可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 利用 Anthropic 的 Claude 分析了 Bram Cohen 仅 470 行代码的 CRDT 版本控制原型，并使用 Pyodide 在浏览器中构建了一个交互式的合并状态可视化工具。 这展示了大语言模型（LLM）如何加速开发者对 CRDT 等复杂分布式系统的理解与原型开发，通过交互式教育工具让前沿技术更易于掌握。 该工具使用 Pyodide 在浏览器中直接运行 Python 代码，无需服务器依赖即可实时可视化 CRDT 合并操作；原始算法由 Bram Cohen 用极简的 Python 脚本实现。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（无冲突复制数据类型）是一种专为分布式系统设计的数据结构，允许多个副本并发更新而无需协调，最终保证一致性。它正被用于新一代版本控制系统以消除合并冲突。Pyodide 是基于 WebAssembly 的 CPython 移植版，可在浏览器中运行 Python，支持客户端交互式应用开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>
<li><a href="https://pyodide.com/what-is-pyodide/">What is Pyodide? - pyodide</a></li>
<li><a href="https://github.com/ljwagerfield/crdt">GitHub - ljwagerfield/crdt: CRDT Tutorial for Beginners (a digestible explanation with less math!) · GitHub</a></li>

</ul>
</details>

**标签**: `#CRDT`, `#Version Control`, `#LLM`, `#Developer Tools`, `#Pyodide`

---

<a id="item-10"></a>
## [竹马创新获种子轮融资，推 3DGS 空间相机](https://36kr.com/p/3734855815184390?f=rss) ⭐️ 7.0/10

杭州初创公司竹马创新完成数千万天使轮融资，将基于 3D 高斯泼溅（3DGS）技术开发消费级三维空间重建硬件。其首款产品“Pebble”面向室内设计师、独立游戏开发者等专业创作者。 此举有望将工业级三维重建能力以消费级价格普及，推动高质量 3D 内容创作的大众化。它连接了生成式 AI、空间智能与具身智能，是迈向世界模型和物理 AI 的关键一步。 竹马硬件采用 3DGS 技术，支持实时高保真渲染、轻量化存储和云端计算，无需高性能电脑。初代产品“Pebble”专注室内场景，小巧便携、操作简单，价格远低于均价 5 万元以上的工业设备。

rss · 36kr · Mar 23, 01:32

**背景**: 3D 高斯泼溅（3DGS）是计算机图形学的一项突破，通过数百万个可学习的三维高斯函数表示场景，实现照片级实时渲染。与 NeRF 不同，3DGS 在渲染时不依赖神经网络，速度更快，更适合消费设备。空间智能指 AI 理解并与三维环境交互的能力，被视为通向通用人工智能（AGI）、机器人和沉浸式计算的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://www.ifanr.com/1629695">李飞飞万字访谈：空间智能是 AI 的下一个前沿领域 | 爱范儿</a></li>
<li><a href="https://www.linktimecloud.com/posts/8278">李飞飞首个“空间智能”模型发布：一张图，生成一个3D世界 - BDOS 大数据操作系统</a></li>

</ul>
</details>

**标签**: `#3D Reconstruction`, `#Generative AI`, `#Spatial Intelligence`, `#3DGS`, `#AI Hardware`

---

<a id="item-11"></a>
## [瑞莎推出 25 TOPS 边缘 AI 模组 AICore DX-M1M](https://www.ithome.com/0/931/594.htm) ⭐️ 7.0/10

瑞莎推出了基于 DEEPX DX-M1M 芯片的 AICore DX-M1M 紧凑型 M.2 边缘 AI 加速模组，在仅 3W 功耗下提供 25 TOPS 的 INT8 算力。 该模组可在 x86 和 Arm 平台上高效部署 AI 推理任务（如视觉和传感器分析），适用于功耗受限的嵌入式与工业系统，并通过 DX-COM 编译器支持 TensorFlow、PyTorch 等主流框架。 AICore DX-M1M 采用 M.2 2242 B+M Key 外形规格，配备 PCIe Gen3 ×2 接口，板载 1GB LPDDR4X-4266 内存和 1Gbit QSPI 闪存，支持 Windows、Linux Ubuntu 及 Docker 环境。

rss · IT HOME · Mar 23, 01:49

**背景**: 边缘 AI 指在本地设备而非云端运行人工智能算法，可降低延迟和带宽消耗。NPU（神经网络处理单元）是专为高效执行神经网络计算而设计的硬件加速器。M.2 是一种紧凑型标准化接口，常用于 SSD 和嵌入式系统中的扩展卡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepx.ai/products/dx-m1m/">DX-M1M - DEEPX: Pioneering Innovation in Edge AI Semiconductors</a></li>
<li><a href="https://www.ithome.com/0/931/594.htm">Radxa 瑞莎推出 AICore DX-M1M 紧凑型边缘 AI 加速模组，25 TOPS 算力...</a></li>
<li><a href="https://linuxgizmos.com/aicore-dx-m1m-module-provides-25-tops-edge-ai-acceleration-in-m-2-form-factor/">AICore DX-M1M Module Provides 25 TOPS Edge AI Acceleration in ...</a></li>

</ul>
</details>

**标签**: `#Edge AI`, `#AI Hardware`, `#Inference Acceleration`, `#Embedded Systems`, `#LLM Deployment`

---

<a id="item-12"></a>
## [阿里千问上线自然语言打车功能](https://www.ithome.com/0/931/591.htm) ⭐️ 7.0/10

阿里千问 AI 现已支持用户通过自然语言一句话完成打车，可处理车型选择、多途经点、司机偏好和价格限制等复杂需求。系统还支持行程中修改路线、记忆常用地址，并通过“支付宝 AI 付”完成支付。 这一功能展示了大语言模型如何从聊天场景迈向现实任务自动化，在出行等日常服务中实现更自然的人机交互。它体现了 AI 正向具备上下文理解、多步骤任务规划和外部服务（如打车平台与支付系统）调用能力的智能体（Agent）演进。 千问能理解“空气清新、价格不超 30 元”或“车上病人需平稳驾驶的老司机”等细致需求，自动匹配车辆，并支持向司机传递个性化备注。系统还能记忆用户设定的家庭和公司地址，并通过自然语言实现定时预约打车。

rss · IT HOME · Mar 23, 01:32

**背景**: Qwen（通义千问）是阿里云推出的大语言模型系列，涵盖 Qwen-1 至 Qwen3.5 等多个版本，以及 Qwen-Max、Qwen-Agent 等专用模型。这些模型不仅支持通用对话，还具备工具调用、规划和记忆等智能体（Agent）能力，构成阿里 AI 生态的核心。此次打车功能正是基于 Qwen 的 Agent 架构，通过自然语言驱动真实世界的任务执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/658247906">[LLM]Qwen 技术报告 | Qwen 7B| Qwen 14B - 知乎</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.5">GitHub - QwenLM/Qwen3.5: Qwen3.5 is the large language model ...</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen) - Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI Application`, `#Natural Language Understanding`, `#Smart Mobility`, `#Alibaba`

---