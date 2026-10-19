# 方向三：面向机器人任务的机器视觉、计算机视觉与具身视觉

本方向以视觉算法为核心，机器人只作为任务载体与闭环验证平台；没有视觉机制的纯控制、纯动力学、机械/执行器论文不纳入。

## 本轮新增代表论文

| 论文 | WHY | HOW | WHAT | 经典脉络中的位置与证据边界 |
|---|---|---|---|---|
| [End-to-End VLA for Autonomous Lunar Rover Docking](https://arxiv.org/abs/2610.19224) | 月面极端明暗与部署期感知扰动会在模块化导航链中逐级传播 | 在高保真月球仿真中生成 safety-aware expert demonstrations，训练端到端 VLA；按安全余量自适应 open-loop 执行 horizon | 作者称闭环表现可与模块化基线竞争，未见感知扰动下 adaptive horizon 降低 hazard-contact | 从模块化月球导航走向视觉语言预训练驱动的闭环策略；预印本，只有模拟证据，真实月面泛化和安全保证未成立 |
| [HyperLoop](https://arxiv.org/abs/2610.19742) | 行星地形重复、少纹理，RGB 回环易感知混淆 | 在 3DGS-SLAM 回环模块融合 BoSW/PCAK-VLAD 光谱描述子与 RGB 描述子，在 DLR MMOTS 的同步 RGB-D/HSI 序列测试 | 最佳 HSI 融合 ATE 5.04 cm，不优于 SIFT-VLAD 4.95 cm；收益来自 SIFT，不来自 600–860 nm HSI | 重要负结果：证明“多模态”不等于有增益，并把下一步指向 SWIR；IAC 2026 接收仅有作者声明，数据仅 65.5 m |
| [LidarVerse](https://arxiv.org/abs/2610.19201) | 重建式 LiDAR 仿真长时一致但慢，生成式方法快却易长期漂移、跨传感器不统一 | 通用 tokenizer + 双向 teacher，将 prefix、HD map、持久空间 cache、文本映射到共享 latent，再蒸馏四步 causal student | 同一模型做生成、预测和重模拟；作者称 H100 上 11 FPS，并支持 32/64/128 线及未见扫描模式 | 从单任务 sensor model 走向统一 LiDAR world model；预印本，硬件重、闭环安全与行星域未证 |
| [BridgeAfford](https://arxiv.org/abs/2610.21918) | 语言交互意图与未见物体目标区域特征存在 query–target gap | IRA 对齐跨物体相似交互区域，VEA 用 2D affordance 证据修正 3D 注意力 | 作者称在 LASO/PIAD 尤其未见物体上超过已有方法 | 从 seen-object affordance segmentation 走向 2D–3D 证据桥接；预印本，尚未证明真实机器人接触成功 |
| [P³-WAM](https://arxiv.org/abs/2610.22363) | 感知、动作条件预测与规划常由不同模型完成，表示不一致 | 在视频 diffusion transformer 中加入紧凑 3D action 表示与 mixture-of-transformers，以可见性随机化统一 Perceive/Predict/Plan | 作者称统一训练在手部 3D 重建、动作视频预测和目标导向计划上优于专用基线 | 从 video world model 走向 world-action model；预印本，VLM judge 与视频质量不等于真实闭环操作成功 |
| [All-St3R SLAM](https://arxiv.org/abs/2610.16143) | 动态 SLAM 的对象级遮罩会过删静止部分，且语义分割依赖标签 | 比较 DUSt3R ego-motion 预测与 All-Tracker 点运动差异，仅移除实际运动像素 | 作者称 RGB-only 约 10 FPS，较 0.5–3 FPS dense dynamic SLAM 更实用 | 从类别/对象遮罩走向 pixel-wise geometry-motion consistency；预印本，IROS 2026 接收仅为作者声明，30 FPS 是隔 3 帧处理 |

## 1. 月球车自主对接 VLA（本轮首读）

- **WHY**：极端光照与感知扰动让模块化管线的误差累积成为月面近距离对接的关键问题；端到端 VLA 是否真能借助大规模视觉语言先验仍需任务化验证。
- **HOW**：在高保真月球模拟器生成安全专家示范，端到端映射视觉/语言到动作；adaptive horizon 让策略按当前安全余量决定多长时间开环执行，以交换算力与风险。
- **WHAT**：证据支持模拟闭环中对未见感知扰动的竞争力，不能证明真实月壤、传感器辐射效应、时延或极端 OOD 下的安全。
- **经典位置**：承接视觉导航、VLA 与 planetary rover autonomy，把通用 VLA 拉进强约束近距离 docking；下一步应加入定位/几何可信度和可证伪的故障注入。

## 2. HyperLoop：值得保留的负结果

- **WHY/HOW**：用材料光谱缓解行星重复地形的 RGB 感知混淆；在 MMOTS 比较两类 HSI 描述子、两类 RGB 描述子和两种融合。
- **WHAT**：Red–NIR HSI 未带来可归因增益，最佳结果反而略逊 SIFT-VLAD；这是指导传感器波段选择的有效负证据。
- **边界**：不能从 65.5 m、600–860 nm 推断“高光谱对行星 SLAM 无用”；正确结论是当前波段/描述子/场景没有显示增益，应预注册 SWIR 实验并控制 RGB backbone。

## 3. LidarVerse、BridgeAfford、P³-WAM 与 All-St3R

- LidarVerse 把 sensor simulation、forecasting 与 resimulation 合为一体，持久空间 cache 是长时闭环价值所在，但当前计算平台不适合直接宣称板端部署。
- BridgeAfford 把 2D affordance 证据用于 3D query 对齐，适合检验“区域定位提升是否真的转化为接触成功”。
- P³-WAM 以共享模型连接重建、预测和规划；评价必须从 VLM judge 扩展到动作误差、接触、失败恢复和真实机器人闭环。
- All-St3R 的差异式运动掩码不依赖语义类别，适合未知动态对象；需报告被过删的可用静态像素与动态残留的任务代价。

## 独立研究点 A：带几何可信度与故障拒绝的月球 docking VLA

- **假设**：把 metric pose/depth、动态掩码与感知故障置信度输入 horizon selector，比仅从图像预测开环长度更能降低未见光照、遮挡和 frozen-frame 下的碰撞。
- **相对已有工作的变化**：VLA 仍产动作，但独立视觉 assurance head 决定执行、缩短 horizon、补看或停止；拒绝理由对应可观测几何/时间一致性。
- **最小验证**：复现月球 docking 模拟，加入 6 档太阳高度、曝光饱和、尘埃/遮挡、帧冻结、外参漂移和移动障碍；至少一个类比场相机回放。
- **指标**：对接成功、hazard contact、最小间距、ATE/depth error、故障 AUROC、risk–coverage、推理频率、P95 时延。
- **关键基线**：原 VLA fixed/adaptive horizon、模块化管线、All-St3R mask、MIRAGE 式 metric estimate、blackout/freeze mitigation、oracle fault label。
- **消融**：无 geometry、无 temporal check、无 dynamic mask、无拒绝、只缩 horizon、不同故障训练覆盖。
- **证伪条件**：等成功率下事故不降，或安全收益完全来自更频繁推理/更高停止率，而非可信度判断。
- **失败模式与风险**：assurance 与 VLA 共享同一视觉盲点；拒绝过多阻塞任务；模拟故障不代表现场。风险高。

## 独立研究点 B：可迁移 LiDAR 世界模型的跨传感器闭环校准

- **假设**：把 LidarVerse 的共享 latent 与真实传感器噪声 posterior、长期地图一致性和任务失败联合校准，可在未见扫描模式上预测“何时 world rollout 不可信”。
- **相对已有工作的变化**：不只报告 Chamfer/生成质量；为每个 beam pattern、天气/尘埃与时域长度输出风险覆盖曲线，并允许 cache reset 或请求真实帧。
- **最小验证**：nuScenes/Waymo 类数据加一个 rover/类比场 LiDAR；32/64/128 线互留一类，100/500/1000 帧 rollout，导航/检测闭环回放。
- **指标**：range/occupancy error、long-horizon drift、检测/定位性能、ECE/AUSE、failure recall、cache reset 次数、FPS/显存/能耗。
- **关键基线**：LidarVerse、reconstruction-based simulator、generative baseline、无空间 cache、传统 ray tracing、oracle sensor model。
- **消融**：无 sensor token、无 posterior、无持久 cache、teacher/student、无真实帧刷新、不同 rollout 长度。
- **证伪条件**：校准分数不能预测下游失败，或跨传感器收益在未见场景/长 rollout 消失。
- **失败模式与风险**：tokenizer 隐藏 beam-specific 偏差；cache 错误自增强；H100 性能不可迁移板端。风险高。

## 独立研究点 C：从 3D affordance grounding 到可验证接触行动

- **假设**：把 BridgeAfford 的目标区域、P³-WAM 的 3D action trajectory 与接触前后的视觉一致性联合训练，能让未见物体上的 grounding 改进转化为真实操作成功。
- **相对已有工作的变化**：区域分割不再是终点；显式预测接触点、进入方向、动作后视觉后果与失败恢复，并以闭环结果反训 query–target bridge。
- **最小验证**：LASO/PIAD 上离线 grounding，加 10 类未见对象、5 类交互的模拟与小规模真实操作；按对象类别严格留出。
- **指标**：mIoU/AUC、6D 接触误差、轨迹误差、操作成功、非预期接触、恢复率、预测—观察一致性。
- **关键基线**：BridgeAfford、P³-WAM、2D affordance-only、3D affordance baseline、VLA policy、oracle region/trajectory。
- **消融**：无 IRA、无 VEA、无 3D action token、无 future prediction、无闭环反馈、无失败恢复。
- **证伪条件**：grounding 指标提高却不改善未见对象的接触/任务成功，或收益完全由更强视频预训练解释。
- **失败模式与风险**：数据接触标签噪声；视觉可供性与动力学可执行性不一致；VLM 评价偏置。风险中高。
