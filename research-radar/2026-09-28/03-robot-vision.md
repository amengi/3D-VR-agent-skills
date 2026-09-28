# 方向三：机器人视觉与具身视觉

仅收视觉表示、感知、建图、理解或视觉预测为核心贡献、机器人承担任务验证的工作；纯机构、本体、材料、执行器、纯控制/动力学辨识和无视觉机制的一般强化学习不纳入。

## 本周新增代表论文

| 论文 | WHY | HOW | WHAT | 脉络位置与证据边界 |
|---|---|---|---|---|
| [Learning to Drive on Mars](https://arxiv.org/abs/2609.24952) | 火星学习导航缺大规模真实任务数据，地形又包含沙丘、岩石和基岩等视觉/动力差异 | 汇集 Perseverance 500 sols、45 km 的双目灰度、位姿、加速度、摇臂转角、倾斜和滑移估计，学习带不确定度的多模态 traversability | 作者报告 AUROC 0.874、F1 0.758，分别较最强基线高 0.058/0.156，并接入 ENav 和物理 rover test bed | 从地球类比/合成转向真实火星经验学习；预印本，数据和代码仍写“将公开”，标签/选择偏差待审计 |
| [SplatLabel](https://arxiv.org/abs/2609.29836) | 2D 基础模型向动态 3D 场景迁移常依赖复杂启发式，伪标签还缺风险—覆盖评价 | 4D Gaussian 显式建模 primitive 轨迹/寿命，融合 360° LiDAR 虚拟深度与 2D soft probabilities，输出 LiDAR 分割置信度和任意尺度 occupancy | 作者报告 SemanticKITTI 多个 recall 水平优于所比基线 | 把 4D 表示变成选择性 3D 标注器；预印本，单数据集与 360° LiDAR 假设限制泛化 |
| [Retrieve-to-Localize](https://arxiv.org/abs/2609.29835) | 仅识别物体不足以回答多步空间关系并输出精确目标坐标 | SpatialLiDAR-LM 对齐点特征与 LLM，以语言条件、位置感知 proposal retrieval 加局部点 refinement 直接回归坐标 | 作者报告在 SpatialLiDAR-QA 上优于代表性 LiDAR-language 和多相机 VLM | 从语言回答推进到点云中的可执行空间 grounding；预印本，数据/代码尚未验证公开，坐标精度未等同闭环成功 |
| [KYS-SLAM](https://arxiv.org/abs/2609.27509) | 语义歧义、实例混淆和动态物体会破坏匹配，但二值删点又损失 bundle adjustment 支撑 | 在 ORB-SLAM3 匹配代价中连续融合 semantic、panoptic 与 depth-aware zero-shot motion compatibility，不改几何后端 | 作者报告一个固定配置在 KITTI/EuRoC/动态与合成数据上 ATE 均改善 | 从“拒绝动态特征”转向“软调制上下文证据”；预印本，依赖上游 panoptic/flow 且未测行星低纹理 |
| [PointCast](https://arxiv.org/abs/2609.28393) | 机器人需要在动作前预测刚体、关节体和柔性体的 3D 状态变化 | 以带身份的对象/末端 3D 点集为状态，用 diffusion transformer 预测未来点窗口，局部/全局 attention 与末端 cross-attention 耦合 | 作者报告四类 regime 中三类第一、一类第二，并在真实 teleoperation 数据和 MPC 中验证 | 从像素/隐变量 world model 走向可检查点级动力学；预印本，各 regime 仍用独立 checkpoint |
| [Imagine then Verify / ATAP](https://arxiv.org/abs/2609.23504) | 功能抓取部位常被遮挡，完整扫描浪费视角预算 | 生成形状先验提出遮挡可供性假设，NBV 联合最大化多假设熵下降与真实观测验证收益 | 作者报告仿真/真实杂乱场景功能抓取改善，较 reconstruction-based active perception 少 57% 以上 NBV | 从物体完整重建转向任务部件验证；2026-09-20 首版、预印本，生成先验错时可能主动确认错误假设 |

## 1. Learning to Drive on Mars（本周首读）

- **核心价值**：不是又一个地球越野数据集，而是把真实火星双目、车体状态和滑移代理沿 45 km 任务轨迹对齐，为“视觉何时可信”提供罕见证据。
- **方法机制**：由视觉与多模态驾驶经验学习 traversability，并显式输出不确定度，最后接到已有 ENav 规划器而不是只报离线分类。
- **首要复现**：按 sol、地点、太阳高度、人工驾驶/ENav、地形类别和滑移强度做时间/地理严格拆分；检查模型是否记忆路线或运营选择。
- **不能据此断言**：作者报告的离线 AUROC/F1 与 test-bed 集成不能证明在未见火星区域的安全闭环，也不能替代 mission-grade hazard certification。

## 2. SplatLabel、Retrieve-to-Localize、KYS-SLAM、PointCast 与 ATAP

- SplatLabel 把“语义地图要不要回答”建模为 risk–recall，而不是强制每个 voxel 给出标签。
- Retrieve-to-Localize 将 LLM 限制为解释关系，再由局部 LiDAR 几何给坐标，减少纯文本空间输出的幻觉入口。
- KYS-SLAM 证明视觉语义/运动线索可以作为连续匹配代价，而不必粗暴删掉潜在有用特征。
- PointCast 的点身份使预测误差更可定位，但跨材料/物体共用一个模型仍未实现。
- ATAP 把主动视觉目标从“完整看清物体”改为“验证当前任务所需部位”，是节约观测预算的重要转向。

## 独立研究点 A：可拒绝、可定位的动态开放词汇 4D 地图

- **假设**：将 SplatLabel 的 risk–recall 选择性预测与 Retrieve-to-Localize 的局部几何 refinement 联合，可在动态场景中减少语言查询坐标的高置信错误，同时维持可用覆盖率。
- **相对已有工作的变化**：每个对象/primitive 同时维护语义 soft posterior、寿命、运动、坐标协方差和拒绝理由；LLM 只生成关系约束，不直接生成坐标。
- **最小验证**：SemanticKITTI、nuScenes 或同类多传感序列，加一组移动机器人长序列；构造单步/多步空间查询和未见类别。
- **指标**：3D mIoU/AP、grounding distance、risk–coverage AUC、ECE、ID switch、语义错误寿命、查询成功率和时延。
- **关键基线**：SplatLabel、SpatialLiDAR-LM、静态 open-vocabulary map、直接 LLM 坐标解码、无拒绝模型。
- **消融**：无 temporal manifold、无 soft probability、无局部点 refinement、无坐标协方差、无拒绝。
- **证伪条件**：选择性机制只通过大量拒绝改善风险，或局部 refinement 在未见类别/动态对象上不优于 proposal 中心。
- **失败模式与风险**：错误 track 长期传播；360° LiDAR 不可用；LLM 关系解析和几何候选共同失败。风险高。

## 独立研究点 B：面向任务收益的主动视觉—定位联合系统

- **假设**：以“降低任务部位/可通行区域决策风险”而非完整场景熵作为 NBV 目标，可在相同观测预算下提高功能抓取或火星通行决策的闭环成功率。
- **相对已有工作的变化**：把 ATAP 的 affordance hypothesis verification 推广到 Mars traversability；再用 KYS-SLAM 的软语义—运动匹配评估候选视角是否也会破坏定位。
- **最小验证**：一套杂乱抓取和一套月/火星类比导航；每任务最多 1、3、5 次主动观测，加入强阴影、遮挡与动态干扰。
- **指标**：任务成功、hazard miss、功能抓取成功、ATE、NBV 次数、累计路程/能耗、风险校准与恢复率。
- **关键基线**：固定视角、完整重建 NBV、最大几何熵、ATAP、无语义 ORB-SLAM3、KYS-SLAM、oracle task region。
- **消融**：无任务部位、无定位风险、无多假设、无不确定度、只看几何/只看语义。
- **证伪条件**：任务定向 NBV 不优于通用最大信息增益，或定位退化抵消任务感知收益。
- **失败模式与风险**：生成先验遗漏真实部位；主动移动成本被低估；火星数据缺少可重拍真值。风险高。

## 独立研究点 C：带接触可见性的统一点级世界模型

- **假设**：在 PointCast 的点轨迹预测中显式加入可见性、接触状态和材料不确定度，可使一个共享 backbone 跨刚体、关节体和柔性体工作，而不是每类独立 checkpoint。
- **相对已有工作的变化**：点身份之外维护 observation/contact masks 与材料 latent，并用选择性 rollout 在高不确定区域请求新视角或短探测。
- **最小验证**：复用四类 PointCast regime，加未见材质、遮挡和不同相机视角；统一模型与四个专用模型等参数/等数据比较。
- **指标**：点轨迹误差、Chamfer、接触时刻误差、long-rollout drift、ECE、MPC 成功率、参数量和推理时延。
- **关键基线**：PointCast 专用 checkpoints、共享无材料 latent 模型、图网络动力学、像素 world model、oracle contact/material。
- **消融**：无可见性、无 contact、无材料 latent、无选择性 rollout、局部/全局 attention。
- **证伪条件**：统一模型在所有 regime 均不及专用模型，或不确定度不能预测 MPC 失败。
- **失败模式与风险**：点身份在拓扑变化时失效；接触标签昂贵；材料 latent 学成对象 ID。风险高。
