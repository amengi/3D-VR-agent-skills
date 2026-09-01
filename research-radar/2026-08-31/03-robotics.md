# 方向三：面向机器人任务的机器视觉与具身视觉

> 更新日：2026-09-01；近两年窗口：2024-09-01—2026-08-31。

本章采用计算机学院/计算机视觉视角：研究对象是**如何让机器从视觉观测中形成可用于定位、导航、搜索、抓取、操作和交互的表示与预测**。机器人主要是视觉算法的任务载体和闭环验证平台，而不是研究机械本体、执行器设计、纯动力学或底层控制。

## 1. 研究边界与主线

### 纳入

- 视觉定位、视觉里程计、SLAM、语义/开放词汇地图；
- RGB/RGB-D/点云/多视图的任务导向三维感知；
- 目标、部件、姿态、可供性（affordance）与接触区域理解；
- 视觉导航、视觉语言导航（VLN）、主动视觉与 next-best-view；
- 视觉操作、视觉模仿、VLA 中的视觉/空间表示；
- 视觉世界模型、4D 场景预测和用视觉后果支持规划。

### 不作为本章核心

- 纯机械机构、材料、驱动器和机器人本体设计；
- 不依赖视觉贡献的纯控制、轨迹优化、动力学辨识或一般强化学习；
- 只提高语言推理或模型规模、却没有视觉空间机制和机器人任务验证的工作。

```text
图像/视频/深度/点云
        ↓
视觉表征与几何—语义理解
        ↓
可定位、可查询、可更新的场景表示
        ↓
导航 / 搜索 / 抓取 / 操作 / 交互
        ↑
主动观测与任务反馈
```

## 2. 代表性经典论文与发展脉络

| 阶段 | 代表工作 | 对“视觉 + 机器人任务”的贡献 | 当前仍未解决的问题 |
|---|---|---|---|
| 视觉反馈控制（1996） | [A Tutorial on Visual Servo Control](https://doi.org/10.1109/70.538972) | 建立 image-based / position-based visual servoing 的基本闭环：视觉误差直接驱动任务 | 感知延迟、遮挡、深度误差和 learned representation 下的稳定性 |
| 实时视觉 SLAM（2007） | [MonoSLAM](https://doi.org/10.1109/TPAMI.2007.1049)；[Parallel Tracking and Mapping](https://doi.org/10.1109/ISMAR.2007.4538852) | 证明单目相机可实时联合跟踪与建图，并形成前后端分工 | 尺度、动态、重定位、长期变化和弱纹理 |
| 特征式可复现 SLAM（2015） | [ORB-SLAM](https://doi.org/10.1109/TRO.2015.2463671) | 用统一 ORB 特征贯穿跟踪、建图、重定位和回环，成为视觉 SLAM 重要系统基线 | 手工特征在极端光照、重复纹理和域外场景仍会失效 |
| 点云深度表征（2017） | [PointNet](https://openaccess.thecvf.com/content_cvpr_2017/html/Qi_PointNet_Deep_Learning_CVPR_2017_paper.html) | 直接学习无序点集，为三维检测、分割和机器人点云理解建立通用算子 | 局部结构、尺度变化、稀疏观测与时序一致性 |
| 视觉六自由度姿态（2019） | [DenseFusion](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_DenseFusion_6D_Object_Pose_Estimation_by_Iterative_Dense_Fusion_CVPR_2019_paper.html) | 稠密融合 RGB 与深度特征估计物体 6D pose，把多模态视觉直接接入抓取/操作 | 遮挡、透明/反光物体、类别级泛化与姿态不确定性 |
| 具身视觉 benchmark（2019） | [Habitat](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) | 把视觉导航变成可复现的大规模 embodied AI 问题，推动 ObjectNav、VLN 和主动探索 | 仿真视觉偏差、任务定义简化和真实部署差距 |
| 任务空间视觉操作（2020） | [Transporter Networks](https://proceedings.mlr.press/v155/zeng21a.html) | 用视觉注意力和特征相关在像素空间表达 pick-and-place，展示强空间归纳偏置 | 更复杂 6-DoF、接触、长时程和多模态条件 |
| 机器人视觉预训练（2022–2023） | [R3M](https://proceedings.mlr.press/v205/nair23a.html)；[VC-1](https://proceedings.mlr.press/v229/majumdar23a.html) | 从大规模视频/图像获得可迁移视觉表示，开始系统比较通用视觉 encoder 对机器人任务的价值 | 预训练目标与动作、几何、接触需求仍错位 |
| 生成式视觉动作策略（2023） | [Diffusion Policy](https://www.roboticsproceedings.org/rss19/p026.html) | 将视觉观测映射为多峰动作序列，成为视觉操作强基线 | 视觉错误归因、长时程记忆、实时性和失败恢复 |
| 跨具身视觉—动作模型（2024，窗口前锚点） | [Open X-Embodiment / RT-X](https://doi.org/10.1109/ICRA57147.2024.10611477)；[OpenVLA](https://www.roboticsproceedings.org/rss20/p133.html) | 用多机器人视觉动作数据和 VLM backbone 建立通用 VLA 路线 | 三维空间、动作坐标系、数据质量和真实长尾仍是瓶颈 |

### 脉络判断

该方向的演进不是“视觉模块被端到端策略取代”，而是视觉输出从特征点和位姿，扩展为对象、部件、可供性、三维场景、动态未来与语言条件动作。真正值得研究的是：**哪一种视觉表示能以更少数据、更低延迟和更可控的失败方式改善真实任务**。

## 3. 近两年顶会代表作

以下按视觉贡献与任务闭环筛选。CVPR/ICCV 工作强调计算机视觉方法，RSS/CoRL/ICRA 工作用于验证这些视觉表示是否真正服务机器人任务。

| 主线 | 代表论文 | Venue / 年份 | 视觉贡献与任务意义 | 主要边界 |
|---|---|---|---|---|
| 三维视觉预训练 | [3D-MVP: 3D Multiview Pretraining for Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_3D-MVP_3D_Multiview_Pretraining_for_Manipulation_CVPR_2025_paper.html) | CVPR 2025 | 用 Objaverse 多视 RGB-D masked pretraining 学习三维视觉 encoder，并接入 RVT 操作策略 | 主要在虚拟操作任务评价；真实材质、遮挡和传感噪声需扩展 |
| 视觉导航世界模型 | [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) | CVPR 2025 | 以动作条件视频生成预测未来视觉观测，用于从头规划或候选轨迹排序 | 像素未来不保证 metric/碰撞正确；长时程生成误差会累积 |
| 4D 具身世界模型 | [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) | ICCV 2025 | 联合生成 RGB、depth、normal，形成随动作演化的 4D 场景并服务 inverse dynamics / policy learning | 深度和法线部分由现成模型扩充，伪标签误差可能进入世界模型 |
| 空间化 VLA | [SpatialVLA](https://www.roboticsproceedings.org/rss21/p011.html) | RSS 2025 | 以 Ego3D position encoding 和 adaptive action grids 将三维空间信息注入 VLA | 仍需区分视觉表征收益与大规模数据/后训练收益 |
| 统一视觉导航 | [Uni-NaVid](https://www.roboticsproceedings.org/rss21/p013.html) | RSS 2025 | 从 egocentric RGB video + language 统一多类导航任务，并以时空 token merge 支持在线推理 | 端到端动作难以诊断；benchmark 协同不等于真实开放世界泛化 |
| 分层视觉语言导航 | [NaVILA](https://www.roboticsproceedings.org/rss21/p018.html) | RSS 2025 | VLA 输出带空间含义的中层语言动作，再交给 locomotion policy，保留视觉语义与执行接口 | 中层语言动作的几何精度、歧义和闭环纠错仍需分析 |
| 交互式主动感知 | [Map Space Belief Prediction for Manipulation-Enhanced Mapping](https://www.roboticsproceedings.org/rss21/p039.html) | RSS 2025 | 联合推理对象几何、位置、类别、遮挡和操作后果，用移动物体减少语义地图不确定性 | 货架场景和动作模型较受限；复杂对象动力学会破坏 belief update |
| 可更新视觉世界模型 | [Physically Embodied Gaussian Splatting](https://2024.corl.org/program/papers-xx) | CoRL 2024 | 将 Gaussian Splatting 变成可由机器人交互实时修正的场景世界模型 | CoRL 总目录可确认收录；具体数值与模块需回到论文全文核验 |
| 操作用视觉重建 | [Robo3R](https://roboticsconference.org/program/papers/56/) | RSS 2026 | 从 RGB 和 robot state 实时预测 metric-scale、robot-frame 的精细点云，服务模仿、抓取、避碰和 sim-to-real | 对训练合成数据、相机/机器人状态标定和未知材质的依赖需验证 |
| 视觉想象自改进 | [Self-Improving Robot Policy with Compositional World Model](https://roboticsconference.org/program/papers/12/) | RSS 2026 | 多视未来预测与 progress value 分开建模，在想象 rollout 中改进视觉操作策略 | 想象偏差可能被 value model 放大；需真实失败分布校准 |
| 开放词汇地图 | [FindAnything](https://2026.ieee-icra.org/awards/) | ICRA 2026 Robot Perception Award Finalist | 代表 object-centric、open-vocabulary mapping 用于机器人探索 | 奖项页只支持论文身份和代表性，方法结论需以正式全文为准 |

### 近两年真正发生的变化

1. **视觉预训练从 2D 语义转向 3D/时空任务表征**：3D-MVP、SpatialVLA 与 4D world model 都在显式补空间和动态。
2. **地图从被动记录转向任务可查询、可交互更新**：Map Space Belief、Physically Embodied GS、FindAnything 关注对象、遮挡、行动和开放词汇查询。
3. **视觉世界模型从“生成视频”转向“比较行动后果”**：NWM 与 4D/组合式世界模型把预测接入规划或策略改进，但仍需几何与不确定性约束。
4. **导航与操作开始共享视频/VLM backbone，但任务接口仍关键**：Uni-NaVid 走统一端到端路线，NaVILA 走中层空间动作路线，两者构成值得比较的系统选择。

## 4. 重点论文简要 Reading

### 4.1 3D-MVP：视觉预训练目标要与机器人空间任务匹配

- **WHY**：通用 2D MAE 能提供语义，但操作需要从多视观测推断三维位置、遮挡与末端姿态。
- **HOW**：将 RVT 拆为视觉 encoder 和 action decoder，在 Objaverse 多视 RGB-D 上通过 masked reconstruction 预训练 encoder。
- **WHAT**：CVPR 论文报告其在一组虚拟机器人操作任务上优于 2D 视觉预训练基线。
- **读后判断**：核心不是“使用更多 3D 数据”，而是预训练中保留跨视图对应和可执行空间结构。
- **应补实验**：固定 backbone 与数据规模，比较 2D MAE、多视一致性、depth/normal、point correspondence 和 action-conditioned pretraining。

### 4.2 Navigation World Models：用视觉生成做反事实导航

- **WHY**：监督导航策略只能复现训练行为，遇到新约束时缺少“如果这样走会看到什么”的预测能力。
- **HOW**：Conditional Diffusion Transformer 根据历史观测和导航动作生成未来视觉观测，再评价是否到达目标或对外部策略候选排序。
- **WHAT**：论文展示熟悉环境中的视觉轨迹规划，以及从单幅输入图像对陌生环境进行未来想象。
- **读后判断**：它提供柔性的视觉预测先验，但像素合理性与可通行性、尺度和碰撞安全不是同一概念。
- **应补实验**：同时评估视频质量、深度/光流一致性、碰撞预测、候选排序校准和闭环任务成功率。

### 4.3 Learning 4D Embodied World Models：从 2D 视频未来走向空间—时间未来

- **WHY**：二维视频生成可能在单视角看似合理，却无法保持物体三维形状、遮挡关系和跨视角一致。
- **HOW**：用 RGB-DN 视频微调生成模型，联合预测 RGB、depth、normal，并转换成动作条件 4D 场景。
- **WHAT**：ICCV 论文报告更好的时空一致性，并展示对 inverse dynamics 和下游 embodied task 的帮助。
- **读后判断**：4D 表示是正确方向，但伪 depth/normal 的系统偏差可能被误认为物理规律。
- **应补实验**：将真实 RGB-D、小比例高质量标注、单目伪标签分开训练，测几何误差如何传导到策略收益。

### 4.4 Robo3R：重建指标必须对齐操作需求

- **WHY**：通用重建模型可能缺少 metric scale、robot-frame 对齐和接触区域精度，深度传感器又受噪声与材质影响。
- **HOW**：联合局部几何与相机姿态，用 learned similarity transform 对齐机器人坐标系，并以 masked point head 与 keypoint PnP 精化点云和外参。
- **WHAT**：RSS 官方摘要报告其在模仿学习、sim-to-real、抓取合成和无碰规划等下游任务上获得一致收益。
- **读后判断**：这类工作应成为“三维重建 × 机器人视觉”的核心范式：不是只提高 Chamfer，而是证明几何改善改变任务结果。
- **应补实验**：按透明/反光、遮挡、细小结构、标定偏差和动态物体分桶，比较重建误差与任务失败的因果关联。

## 5. 未来值得研究的方向

### V1. Task-aligned 3D perception：面向任务损失的三维视觉

**假设**：以抓取、避碰、可达性或导航风险作为辅助目标，比只优化深度/点云平均误差更能保留关键几何。

- 方法变化：共享 3D encoder，分别输出 metric geometry、task affordance 和 calibrated uncertainty。
- 最小实验：构造相同平均深度误差但薄结构/接触边界不同的样本。
- 指标：几何误差 + grasp success、collision recall、planning success、风险覆盖率。
- 证伪：任务收益完全可由更高分辨率或更多数据解释，任务辅助目标没有独立贡献。

### V2. 开放词汇、长期一致的语义地图

**假设**：对象级 persistent memory + 视觉语言检索 + 几何证据追踪，能比逐帧 open-vocabulary segmentation 更可靠地支持长期搜索与问答。

- 关键问题：同一对象跨视角/跨时间 identity、状态变化、错误标签回滚和遗忘。
- 指标：跨天 object retrieval、地图问答正确率、重复对象关联、变化检测和错误修复成本。

### V3. 面向任务信息增益的主动视觉

**假设**：直接选择最能降低任务失败不确定性的观测，比最大化覆盖率、熵或渲染质量更高效。

- 任务：遮挡货架目标搜索、抓取前视点选择、狭窄空间导航。
- 对照：coverage、geometric uncertainty、semantic uncertainty、task-value information gain。
- 指标：单位移动成本的任务成功增益、观测次数、碰撞/操作风险。

### V4. 几何一致且带不确定性的视觉世界模型

**假设**：在视频生成中联合约束相机、depth、normal、object motion 和 epistemic uncertainty，可提高候选行动排序而不必追求完全精确的长期像素生成。

- 评价分层：像素 → 几何/运动 → 候选排序 → 闭环成功。
- 证伪：更好的 4D 几何指标不改善行动排序，说明瓶颈在目标/value 或策略接口。

### V5. 人类视频—仿真—机器人视频的视觉对齐

**假设**：以对象状态变化、手—物交互和相机运动为中间视觉语言，比直接统一 action token 更能利用无机器人动作标注的人类视频。

- 关键变量：视角差异、手/夹爪形态、动作时标和不可观测力。
- 最小实验：固定机器人示范量，逐步增加人类视频和合成视频，测少样本任务迁移。

### V6. 可诊断的视觉—动作模型

**假设**：让模型同时给出可验证的中间视觉结论（目标、部件、姿态、可供性、预计接触点），能更早发现错误并改善回退，而不显著损害端到端性能。

- 对照：纯端到端 VLA、显式模块化 pipeline、共享 backbone 多头模型。
- 指标：错误定位准确率、干预收益、OOD failure AUROC、最终任务成功率和延迟。

### V7. 多模态极端视觉感知

**假设**：RGB 与 event、thermal、偏振或稀疏深度在光照突变、低纹理和尘埃遮挡下进行不确定性感知融合，可比固定早/晚融合更稳健。

- 方法重点：缺失模态、冲突模态和标定漂移下的动态可信度分配。
- 价值：作为独立机器视觉问题成立，也能自然迁移到夜间、工业和月/火星场景。

## 6. 推荐阅读顺序

1. Visual Servoing、MonoSLAM/PTAM、ORB-SLAM：理解视觉如何进入闭环任务与持久状态估计。
2. PointNet、DenseFusion、Transporter Networks：理解点云、RGB-D 姿态和任务空间视觉表示。
3. Habitat、R3M、VC-1、Diffusion Policy：理解 embodied benchmark、视觉预训练与视觉策略。
4. Open X-Embodiment/OpenVLA、3D-MVP、SpatialVLA：比较通用视觉、三维预训练和空间化 VLA。
5. Navigation World Models、4D Embodied World Models：理解动作条件视觉未来及其证据边界。
6. Map Space Belief、Robo3R、FindAnything：理解主动视觉、任务导向三维感知和开放世界地图。

## 7. 选题警示

- 不要把“在机器人数据上使用一个 CV backbone”当作充分贡献；应说明视觉表征为什么适合该任务，并做机制消融。
- 不要只报告重建/检测指标或只报告任务成功率；应建立视觉误差到任务失败的关联。
- 不要把仿真中可直接读取的 depth、pose、semantic label 偷渡到真实系统；必须列出测试时可观测输入。
- 不要默认 VLA 的收益来自视觉理解；语言模型、数据规模、动作 tokenizer 和后训练都可能是混杂因素。

## 参考来源说明

经典工作链接正式 DOI、CVF 或 PMLR；近两年条目优先 CVF、RSS、CoRL 和 ICRA 官方页面。ICRA 2026 的 FindAnything 当前仅以官方奖项页证明论文身份与代表性，因此不写入未经全文核对的数值结论。CoRL 2024 的 Physically Embodied Gaussian Splatting 由官方 program 确认收录，后续深读仍应补正式 OpenReview/PDF 证据。
