# 方向三：机器人视觉与具身视觉

仅收视觉表示、感知、建图、理解或视觉预测为核心贡献、机器人承担任务验证的工作；纯机构、本体、材料、执行器、纯控制/动力学辨识和无视觉机制的一般强化学习不纳入。

## 本周新增代表论文

| 论文 | WHY | HOW | WHAT | 脉络位置与证据边界 |
|---|---|---|---|---|
| [SenseFuse](https://arxiv.org/abs/2609.20475) | 开放词汇 3D 实例标签常偏依赖 2D 图像特征，忽略 shape encoder 的互补错误模式 | 不加标签，在单场景 proposal 上估计敏感度，快速选择 2D image 与 3D shape encoder 的融合权重 | 作者报告三数据集所有设置标签准确率改善、22 项中 21 项 AP 提升 | 从 2D 蒸馏走向图像—形状异质证据；预印本，scene-level 权重可能掩盖对象级差异 |
| [PerSeM](https://arxiv.org/abs/2609.19542) | 帧级开放词汇分割跨视角和重复观测不稳定 | 世界 voxel 多数语义记忆 + 保历史空间细化 + trust-aware replay + context verification | 作者报告 Forest/UAVScenes 上语义正确性和时序稳定性改善 | 从即时预测走向长航程可修正语义记忆；预印本，仍受 pose/voxel 误差和多数偏见影响 |
| [AnyviewMeter](https://arxiv.org/abs/2609.20106) | 同一任务状态会因相机视角/遮挡导致视觉 reward 改变 | LoRA + Plücker rays + 同步多视图 block attention，适配预训练 Robometer | 作者报告仿真和真实任务中较 RGB 微调/单视图平均降低进度误差 | 将相机几何显式注入视觉任务评估；预印本，基于 reward 相关性不等于因果任务理解 |
| [FunArt](https://arxiv.org/abs/2609.20673) | 静态扫描难同时恢复可动物体、交互部件与关节运动 | RGB-D 重建实例转为 TRELLIS.2 O-Voxel，冻结生成式 3D VAE 作先验，轻量 decoder 预测部件/功能/关节 | 作者报告 Articulate3D 多项 SOTA，端到端功能部件 AP 有提升 | 从几何/语义图走向动作前的功能—运动图；预印本，仅单静态配置与一个基准 |

## 1. SenseFuse（本周首读）

- **核心 insight**：两个强 2D encoder 容易重复相同语义错误，而 2D 与 3D encoder 的失败更互补；“异质错误”比“多一个模型”更有价值。
- **方法机制**：只改 mask-labeling 阶段，通过无标签敏感度选择 scene-level 融合权重，几乎不增加训练成本。
- **首要复现**：按对象大小、遮挡、材质、形状相似类和 domain shift 分层，验证互补性是否在行星/室外点云仍成立。
- **不能据此断言**：ScanNet/Replica 的 label-free 最优权重不能直接推广到稀疏 LiDAR、极端光照或开放世界新增类别。

## 2. PerSeM、AnyviewMeter 与 FunArt

- PerSeM 表明长期视觉地图的关键是保留历史、只在不确定区域重放与验证，而不是重复跑更大的网络。
- AnyviewMeter 表明相机几何应进入任务进度表征；简单平均多视图可能破坏同步关系。
- FunArt 表明生成式 3D latent 可承载动作相关结构，但仍需闭环交互验证，不能只凭分割/关节 AP 宣称可操作。

## 独立研究点 A：分歧驱动、可撤销的开放词汇长期地图

- **假设**：把 2D–3D encoder 分歧作为 voxel 记忆的写入、重放和撤销信号，比固定融合权重或多数投票更能抵抗跨视角长期错误。
- **相对已有工作的变化**：将 SenseFuse 的 scene-level 无标签互补估计推进到 PerSeM 的对象/voxel 时序后验，并显式维护错误信念寿命。
- **最小验证**：ScanNet++、UAVScenes 与一组稀疏 LiDAR/RGB 序列；注入 pose drift、遮挡、类别别名和新类别。
- **指标**：3D mIoU/AP、temporal stability、ID switch、错误信念存活时间、撤销 precision/recall、内存与延迟。
- **关键基线**：单 2D、单 3D、SenseFuse、PerSeM、固定/学习权重、VOIM 式软证据。
- **消融**：无分歧门控；无 replay；无撤销；scene/object/voxel 三种粒度；无 pose 不确定度。
- **证伪条件**：等算力下不优于多数记忆，或撤销机制显著破坏稳定类别。
- **失败模式与风险**：两个 encoder 在新域共同错误；pose drift 伪造分歧；长尾类别被保守门控遗忘。风险中等。

## 独立研究点 B：相机几何与功能部件联合的视角不变任务进度

- **假设**：将 FunArt 的功能/关节状态作为 AnyviewMeter 多视图 reward 的结构瓶颈，可比纯视觉 scalar reward 更稳定地区分“视角变化”与“真实任务进度”。
- **相对已有工作的变化**：不直接从多视图图像回归 reward，而是先恢复对象功能部件、关节和可观测性，再预测进度及不确定度。
- **最小验证**：门/抽屉/柜体等 6 类 articulated 操作，固定、腕部和移动相机；同时覆盖遮挡与未见视角。
- **指标**：progress MAE、temporal ordering、跨视角方差、功能部件 AP、关节误差、ECE、任务成功预测。
- **关键基线**：RGB fine-tuning、AnyviewMeter、FunArt + 线性 reward、无几何多视图模型、oracle part state。
- **消融**：去掉 Plücker rays、功能部件、关节、同步 attention 或不确定度；单视图/多视图。
- **证伪条件**：结构瓶颈不降低跨视角误差，或 oracle 部件状态仍不能预测任务进度。
- **失败模式与风险**：静态扫描先验无法跟踪接触后状态；关节估计误差级联；reward 与真实安全性不一致。风险中高。
