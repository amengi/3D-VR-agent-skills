# 方向三：机器人——从经典范式到具身基础模型

> 更新日：2026-09-01；近两年窗口：2024-09-01—2026-08-31。

本章只讨论机器人学本身，不要求论文涉及三维重建、仿真或行星任务。筛选首先看它是否改变了机器人学中的问题定义、方法范式或实验标准；与另外两个方向的连接统一留在 `04-cross-track-opportunities.md`。

## 1. 如何理解机器人学的主干

```text
感知与状态估计 → 建模与预测 → 规划与决策 → 控制与接触 → 真实系统反馈
          ↑                                                ↓
          └──────────── 学习、辨识、安全与系统设计 ────────────┘
```

机器人学不是单一的“机器人 AI”。本章同时保留模型驱动与数据驱动路线，并覆盖移动、操作、腿足、触觉和通用策略。单看 VLA（vision-language-action）会漏掉控制、安全和接触；单看经典规划控制又解释不了近年的跨任务泛化。

## 2. 代表性经典论文与发展脉络

经典并不等于“今天应原样复现”，而是它建立了后来研究仍在回答的问题。

| 阶段 | 代表工作 | 建立的范式 | 留给今天的问题 |
|---|---|---|---|
| 图搜索与任务规划（1968） | [A Formal Basis for the Heuristic Determination of Minimum Cost Paths](https://doi.org/10.1109/TSSC.1968.300136)（A*） | 把目标、代价与启发式搜索统一起来 | 学习启发式如何保留完备性、最优性或可解释的次优界？ |
| 力与接触控制（1985–1987） | [Impedance Control](https://doi.org/10.1115/1.3140702)；[Operational Space Formulation](https://doi.org/10.1109/JRA.1987.1087068) | 不只跟踪位置，还规定机器人与环境交互的动力学关系 | 学习策略如何继承稳定性、被动性与接触约束？ |
| 反应式机器人（1986） | [A Robust Layered Control System for a Mobile Robot](https://doi.org/10.1109/JRA.1986.1087032) | 以分层行为代替完整世界模型，强调实时闭环 | 世界模型应建到多复杂，何时反而拖慢或误导控制？ |
| 采样式运动规划（1998） | [Rapidly-Exploring Random Trees](https://msl.cs.illinois.edu/~lavalle/papers/Lav98c.pdf) | 在高维连续空间中快速探索可行轨迹 | 如何把学习先验与严格碰撞/动力学约束组合？ |
| 概率机器人（1999–2006） | [Monte Carlo Localization](https://robots.stanford.edu/papers/fox.aaai99.pdf)；[FastSLAM](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/montemerlo_fastslam.pdf)；[GraphSLAM](https://robots.stanford.edu/papers/thrun.graphslam.pdf) | 用概率分布和图优化处理感知噪声、数据关联与漂移 | 神经感知置信度怎样变成可校准、可传播的后验或集合？ |
| 大规模机器人学习（2016–2018） | [End-to-End Training of Deep Visuomotor Policies](https://www.jmlr.org/papers/v17/15-522.html)；[Domain Randomization](https://doi.org/10.1109/IROS.2017.8202133)；[QT-Opt](https://arxiv.org/abs/1806.10293) | 从手工模块转向数据驱动闭环，并用仿真或大规模试验扩展数据 | 数据覆盖、离线评价、长尾失败与 sim-to-real 成为核心瓶颈 |
| 序列策略与生成式动作（2022–2023） | [RT-1](https://arxiv.org/abs/2212.06817)；[Diffusion Policy](https://www.roboticsproceedings.org/rss19/p026.html)；[RT-2](https://arxiv.org/abs/2307.15818) | Transformer/VLM 提供语义迁移，扩散模型表达多峰连续动作 | 语言理解是否真正转化成可执行、精确和鲁棒的物理技能？ |
| 跨具身数据与开放模型（2024，窗口前锚点） | [Open X-Embodiment / RT-X](https://doi.org/10.1109/ICRA57147.2024.10611477)；[Octo](https://www.roboticsproceedings.org/rss20/p127.html)；[OpenVLA](https://www.roboticsproceedings.org/rss20/p133.html) | 多机器人数据、统一动作接口和开放通用策略成为可复现实验对象 | 具身差异、动作标定、数据质量和后训练方式仍未解决 |

### 脉络判断

机器人学没有从“模型”单向进化到“端到端学习”。更准确的历史是：搜索、优化、反馈控制和概率估计提供约束与结构；深度学习扩大感知与策略的覆盖；当前前沿正在寻找两者的系统级接口。

## 3. 近两年顶会顶刊代表作

以下不是按与本仓库其他方向的交叉程度选择，而是按机器人学独立代表性选择。`顶会/奖项` 只按会议官方页面确认；预印本不伪装成顶会论文。

| 主线 | 代表论文 | Venue / 年份 | 为什么值得读 | 主要边界 |
|---|---|---|---|---|
| 通用机器人策略 | [π₀: A Vision-Language-Action Flow Model for General Robot Control](https://www.roboticsproceedings.org/rss21/p010.html) | RSS 2025 | 将预训练 VLM 与 flow-matching action expert 组合，并在多种单臂、双臂和移动操作任务上研究通用策略及后训练 | 仍高度依赖大规模私有数据与高质量后训练；开放复现成本高 |
| 空间表征 | [SpatialVLA](https://www.roboticsproceedings.org/rss21/p011.html) | RSS 2025 | 以 Ego3D position encoding 和 adaptive action grids 显式处理三维空间与跨机器人动作迁移 | 结果不能说明一种动作离散化可无条件覆盖新机构和精细接触 |
| 数据引擎 | [RLDG](https://www.roboticsproceedings.org/rss21/p028.html) | RSS 2025 | 用任务专用 RL 生成更优状态—动作覆盖，再蒸馏回 generalist policy；论文报告部分任务最高约 40% 成功率提升 | RL 数据生成成本高，且可能继承 simulator/reward artifact |
| 语义与物理规划 | [Prompting with the Future](https://www.roboticsproceedings.org/rss21/p145.html) | RSS 2025 | 用交互式数字孪生模拟候选动作，再让 VLM 做任务相关排序，展示“语义模型 + 显式物理 + MPC”的组合 | 依赖快速场景建模和可用物理模型；长时程误差会累积 |
| 安全在线辨识 | [Provably-Safe, Online System Identification](https://www.roboticsproceedings.org/rss21/p121.html) | RSS 2025 | 在避障和输入/状态约束下生成激励轨迹，并给未知载荷惯量参数计算严格包络 | 保证依赖有界噪声和模型集合；复杂接触与柔性物体仍困难 |
| 非结构地形适配 | [Adaptive Locomotion on Mud](https://www.roboticsproceedings.org/rss21/p126.html) | RSS 2025 | 用电机电流和位置等本体感受在线估计基底性质，并据此改变运动策略 | 平台和材料范围有限，跨机器人、跨土壤泛化尚未建立 |
| 高维强化学习 | [FlashSAC](https://roboticsconference.org/program/awards/) | RSS 2026 Outstanding Paper | 官方奖项表明高维机器人控制中“更快且更稳定的 off-policy RL”仍是主问题，不只有基础模型扩展 | 需结合正文进一步核对跨任务、算力与真实机器人边界 |
| 动力学与系统建模 | [NeuralActuator](https://roboticsconference.org/program/awards/) | RSS 2026 Outstanding Systems Paper | 把执行器神经建模同时用于机器人动力学与外力感知，体现模型误差对控制系统的基础影响 | 神经执行器模型的分布外稳定性与跨硬件迁移仍需单独验证 |
| 快速生成式规划 | [Muninn](https://roboticsconference.org/program/awards/) | RSS 2026 Outstanding Student Paper | 针对 trajectory diffusion 的推理速度瓶颈，说明生成式规划开始进入实时性竞争 | “更快”不等于闭环更安全，需报告失效尾部和实时控制预算 |
| 三维操作策略 | [FP3: A 3D Foundation Policy for Robotic Manipulation](https://2026.ieee-icra.org/awards/) | ICRA 2026 Robot Learning Award Finalist | 官方奖项候选，代表从 2D VLA 向三维几何条件策略推进 | 奖项页只能支持代表性，方法与实验结论需以正式论文全文为准 |
| 触觉仿真与操作 | [ETac](https://2026.ieee-icra.org/awards/) | ICRA 2026 Automation Award Finalist | 代表轻量触觉仿真开始成为灵巧操作的数据与评价基础设施 | 触觉模拟的传感器依赖性、接触材料覆盖与 sim-to-real 是关键边界 |

### 近两年真正发生的变化

1. **通用策略从“预训练一次”转向“预训练 + 高质量后训练 + 在线/离线改进”**：π₀、RLDG 等路线都说明，后训练数据比继续堆通用示范更值得研究。
2. **空间与接触重新成为核心变量**：SpatialVLA、FP3 和触觉工作都在修补纯 2D 语义模型对几何、力和动作机构理解不足的问题。
3. **世界模型开始承担候选预测，不再被默认当作完整控制器**：Prompting with the Future 是一个清晰例子；硬约束、反馈控制和安全后端仍不可省略。
4. **学习系统重新重视辨识、稳定和实时性**：Provably-Safe SysID、NeuralActuator、FlashSAC、Muninn 说明“能跑、可控、可验证”正在成为第二轮竞争。

## 4. 重点论文简要 Reading

### 4.1 π₀：通用策略的关键不只是 VLM

- **WHY**：单任务策略缺少泛化，而把 VLM 直接离散成 action token 又不擅长精细、连续、灵巧动作。
- **HOW**：保留 VLM 的视觉—语言语义能力，增加独立 action expert，以 flow matching 生成连续动作，并用跨具身数据预训练、用高质量任务数据后训练。
- **WHAT**：论文展示了直接提示、任务专门化和新技能微调三种使用方式，覆盖洗衣、清理和装配等多阶段任务。
- **读后判断**：真正可迁移的研究问题是“通用先验和任务专长怎样分工”，而不是简单复制模型规模。
- **应补实验**：固定模型与总数据量，只改变数据质量、任务覆盖和后训练机制；同时报告平均成功率、最差任务、干预次数与恢复率。

### 4.2 RLDG：数据质量可以由交互优化产生

- **WHY**：人类示范往往集中在成功轨迹附近，缺少精密任务所需的纠错状态和更优动作分布。
- **HOW**：为专门任务训练 RL policy，用其生成数据，再蒸馏/微调 generalist policy。
- **WHAT**：官方摘要报告在连接器插入、装配等真实任务上持续优于人类示范数据训练，并把收益归因于动作分布和状态覆盖。
- **读后判断**：这是一种“专家数据工厂”，但是否优于主动采样、自动课程或失败回放仍需预算公平比较。
- **应补实验**：固定真实机器人小时数与仿真步数，比较 human demo、RL rollout、uncertainty sampling、failure replay 及其混合。

### 4.3 Prompting with the Future：让 VLM 看模拟后果

- **WHY**：VLM 能理解任务语义，但不应被假定为精确的接触动力学预测器。
- **HOW**：从短视频建立交互式数字孪生，模拟多条候选动作，把未来结果渲染成视觉提示，再由 VLM 排序并由采样式 MPC 执行。
- **WHAT**：论文在八类真实接触操作任务上验证，并通过消融支持显式物理建模的作用。
- **读后判断**：世界模型最稳健的近期角色可能是“候选生成与反事实比较器”，而不是完全替代控制器。
- **应补实验**：系统扫描物理模型误差、视觉重建误差、VLM 排序误差，确定三者各自在何处成为瓶颈。

### 4.4 Provably-Safe Online SysID：学习未知参数时也要安全

- **WHY**：系统辨识需要激励，激励动作却可能碰撞或违反输入约束。
- **HOW**：安全轨迹规划器产生可跟踪且有信息量的动作，鲁棒辨识器在有界噪声下更新未知惯量参数集合。
- **WHAT**：机械臂未知载荷实验显示可以边执行边缩小参数界，同时维持论文设定下的安全保证。
- **读后判断**：未来机器人适配不应只问“学得快不快”，还应问“辨识期间能否证明不会越界”。
- **应补实验**：将刚性未知载荷扩展到摩擦、柔性和间歇接触，并检查模型集合失配时保证如何退化。

## 5. 未来值得研究的独立方向

### R1. 可校准、可拒绝、可恢复的通用策略

**假设**：若策略显式预测任务条件下的失败概率，并配套拒绝/求助/恢复策略，则在相同平均成功率下可显著降低灾难性长尾失败。

- 变化：从单一 action policy 改为 `action + calibrated risk + recovery option`。
- 最小实验：在标准操作任务中注入遮挡、物体替换、指令歧义、夹持滑移和执行器降级。
- 指标：risk-coverage、ECE、最差任务成功率、无人干预完成率、恢复成本。
- 证伪：风险头无法比简单 ensemble/阈值更好预测失败，或拒绝造成任务完成率不可接受。

### R2. 预算公平的机器人数据引擎

**假设**：在固定真实机器人时间与计算预算下，主动采样 + 失败回放 + 少量 RL rollout 比单纯扩大人类示范集更有效。

- 对照：human demo、teleoperation correction、RL-generated data、synthetic video/action、mixed curriculum。
- 必须统一：机器人小时数、人工标注时间、GPU 小时数和安全中断次数。
- 价值：建立“每 100 小时新增数据带来多少可靠能力”的可比较数据效率标准。

### R3. 语义世界模型与可验证控制的分层接口

**假设**：让生成式/VLM 世界模型只提出子目标和候选未来，由 model-based planner、CBF/MPC 或 reachability 后端执行硬约束，会比纯生成控制获得更好的分布外安全—任务 Pareto。

- 关键接口：状态抽象、约束语言、置信集合、候选多样性和回退条件。
- 评价：不只看成功率，还看约束违反、错误自信、重规划频率和最坏执行时间。

### R4. 视觉—触觉—本体感受的接触基础策略

**假设**：以接触事件和力闭环为中心的预训练，比仅在视觉动作序列上扩模更能改善插接、布料、工具和滑移恢复。

- 数据单元：接触前状态—接触瞬态—稳定交互—失败/恢复，而非均匀视频帧。
- 最小 benchmark：跨三种传感器、两种机械手和未知材料测试；分别遮蔽视觉、触觉和力矩输入做消融。

### R5. 持续适配但不灾难遗忘的机器人

**假设**：结构化 fast parameters（载荷、摩擦、执行器、地形）与慢速语义/技能参数分离，可在在线适配时减少旧技能退化。

- 比较：full fine-tuning、LoRA、latent context、Bayesian parameter filter、neural residual。
- 指标：适配样本数、旧任务保持率、错误适配恢复时间、分布切换后的 regret。

### R6. 具身设计—控制—学习联合优化

**假设**：若把可制造性、能耗、感知可观性和策略可学习性共同放入设计环，得到的机器人会比“先定硬件、后学策略”更具任务效率。

- 最小范围：只优化一个末端执行器或腿足机构，避免一开始做全机器人搜索。
- 风险：仿真偏差可能让设计利用不可实现的物理漏洞；必须有原型或 hardware-in-the-loop 闭环。

## 6. 推荐阅读顺序

1. A*、Impedance Control、RRT、Monte Carlo Localization：建立搜索—控制—不确定性的基础语言。
2. Deep Visuomotor Policy、Domain Randomization、QT-Opt：理解大规模机器人学习的起点和代价。
3. RT-1、Diffusion Policy、RT-2、Open X-Embodiment：理解现代通用策略为何出现。
4. π₀、SpatialVLA、RLDG：比较模型、表征和数据三条扩展路径。
5. Prompting with the Future、Provably-Safe SysID、NeuralActuator：补上物理、辨识与保证。
6. FlashSAC、Muninn、FP3、ETac：追踪 2026 年实时学习、三维策略与触觉基础设施。

## 7. 选择课题时的三个警示

- 不要把“换一个更大的 VLM/VLA”本身当研究问题；必须指出动作、数据、反馈或评价发生了什么机制变化。
- 不要只报告平均成功率；机器人系统最重要的信息常在最差任务、失败后果和恢复过程。
- 不要让仿真任务定义替代真实问题定义；至少要证明策略没有依赖不可观测状态、精确重置或 simulator artifact。

## 参考来源说明

经典工作优先链接 DOI、作者主页或正式论文；近两年工作优先 RSS/ICRA 官方页面。RSS 2026 和 ICRA 2026 的奖项页面可证明论文的会议与奖项/候选身份，但不能替代全文证据，因此对仅由奖项页支持的论文没有写入未经全文核对的数值结论。
