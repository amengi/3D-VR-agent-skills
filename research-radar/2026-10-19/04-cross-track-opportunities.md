# 两两交叉与三方向闭环

以下交叉分析在三个方向独立选文后进行，不反向决定纳入集。

## 两两交叉矩阵

| 组合 | 独立信号 | 可检验交叉问题 |
|---|---|---|
| 三维重建 × 仿真 | 重力/metric/reliability 前馈重建与材质物理 latent；主动生成、概率 twin、可微接触 | 重建残差能否区分几何/材质/物性不确定度，并决定下一批场景与 fidelity，而非把全部差异交给域随机化？ |
| 三维重建 × 机器人视觉 | SceneAE/MicroSDF/MIRAGE 提供 queryable metric scene；BridgeAfford/P³-WAM/All-St3R 需要任务几何与动态过滤 | 可查询 3D latent 能否直接服务 affordance、动作后果与 SLAM，同时给每次查询一个可靠度证书？ |
| 仿真 × 机器人视觉 | MetaGenSim/概率 twin/DiffGIPC 可主动产生风险场景；月球 VLA/HyperLoop/LidarVerse 给出闭环视觉目标 | 能否用真实失败与负证据反向优化“模拟什么、什么波段、什么故障”，而不是只生成更多好看的数据？ |

## 交叉 idea 1：重力—材质分解驱动的传感器 fidelity 调度

- **假设**：把重建误差分解为重力/运动、metric scale、几何、反射材质和传感器噪声后，按下游风险选择模拟模块，比统一提高渲染 fidelity 更省算力且更能保持真实算法排序。
- **相对已有工作的变化**：用 Motion/Gravity LUPI、MIRAGE 与 MicroSDF 给出可解释残差；MetaGenSim 的 action 从“场景参数”扩展为“场景 × 传感器/材质 fidelity”。
- **最小验证**：火星/月球类比场的 RGB-D/LiDAR 小规模 paired twin；4 类光照/材质、3 档 sensor fidelity、3 个定位/重建算法。
- **指标**：几何/位姿误差、材质参数误差、真实方法排序 Spearman、hazard miss、failure recall、GPU 小时和 fidelity 调用率。
- **关键基线**：uniform randomization、MetaGenSim、固定 fidelity、全高保真、像素域差调度、oracle error source。
- **消融**：无重力项、无 metric anchor、无材质分解、无风险目标、只优化图像相似度。
- **证伪条件**：误差源不可辨识，或调度不优于固定中 fidelity/简单域随机化。
- **失败模式与风险**：真实配准不准；材质与几何强耦合；调度器利用模拟伪影。风险高。

## 交叉 idea 2：查询式 3D latent 到 affordance/action 的闭环

- **假设**：SceneAE 式持久 3D latent 若同时保存动态 mask、材质和可靠度，可比逐帧 RGB token 更稳定地回答“哪里可操作、会发生什么、是否需要再看”。
- **相对已有工作的变化**：BridgeAfford query 与 P³-WAM action token 直接读写同一 spatial latent；动作后视觉证据回写并更新 affordance posterior。
- **最小验证**：20 个场景、10 类未见对象、5 类操作；固定 3 个视角预算，比较静态/动态干扰和高光表面。
- **指标**：3D grounding、pose/contact error、任务成功、重看次数、预测一致性、ECE、内存增长与 P95 时延。
- **关键基线**：SceneAE、BridgeAfford、P³-WAM、frame-token VLA、静态 3D map、oracle geometry/affordance。
- **消融**：无 persistent latent、无 reliability、无材质、无动态 mask、只读不回写、无 active view。
- **证伪条件**：共享 latent 不优于晚期融合，或长期回写导致误差累积并损害未见对象表现。
- **失败模式与风险**：错误 affordance 污染记忆；遮挡下身份错配；计算/显存超过逐帧方案。风险高。

## 三方向闭环 idea：风险触发的行星 docking 数字孪生

- **假设**：以可靠 metric 3D 状态为中心，让概率 twin 在真实风险上更新物性/传感器 posterior，让主动模拟器生成最有价值的照明、尘埃、地形与故障，再由 assurance-gated VLA 执行，可改善安全—任务—算力 Pareto。
- **相对已有工作的变化**：Motion/Gravity/MIRAGE 负责几何与尺度，MicroSDF/HyperLoop 管理材质/波段证据，MetaGenSim/概率 twin/DiffGIPC 决定场景与 fidelity，月球 VLA/LidarVerse/P³-WAM 做闭环预测；HyperLoop 的负结果作为 SWIR 选择先验而非被忽略。
- **最小验证**：一个月面 docking paired twin + 类比场回放，30 条路线；预注册强阴影、曝光、尘埃、freeze、外参漂移、低附着与动态遮挡，完全留出一个地点。
- **指标**：对接成功、碰撞/最小间距、ATE/几何误差、failure recall、posterior coverage、sim–real 排名、停止/补看/高保真次数、P95 时延/能耗。
- **关键基线**：原月球 VLA、模块化导航、固定高/中 fidelity、uniform simulation、无 twin 更新、无 assurance、oracle scenario/fidelity。
- **消融**：逐一去掉重力/metric、材质/波段、概率 posterior、主动模拟、接触反演、world rollout 与风险门控；严格等预算。
- **证伪条件**：联合系统不能改善 Pareto，或收益完全来自更多停止、更多真实数据/算力；模拟排序与类比场真实排序无相关。
- **失败模式与风险**：模块共享同一模拟偏差；错误 posterior 自强化；通信/时间同步失配；SWIR 成本与功耗超预算；过度保守导致任务不可完成。风险高。
