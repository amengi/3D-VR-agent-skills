# 三方向交叉机会

本文件只在三个独立方向分析完成后做交叉。交叉不自动意味着更好：只有当共享变量、数据或评价闭环清晰时，组合才有研究价值。

## 两两交叉矩阵

| 交叉 | 共享对象 | 最强证据桥 | 主要缺口 | 优先级 |
|---|---|---|---|---|
| 三维重建 × 仿真 | 场景几何、相机/光照、合成真值、real-to-sim 资产 | StereoLunar、G3R、Physics-Based Lunar Sensor Simulation | photorealism 与几何/任务有效性脱节；模拟参数难从真实数据反演 | 高 |
| 三维重建 × 机器人 | metric map、不确定性、主动视点、算力预算 | MASt3R-SLAM、PINGS、GauSS-MI、Certifiably-Correct Mapping | 地图指标与安全/任务指标脱节；尾部错误未校准 | 很高 |
| 仿真 × 机器人 | 动力学、策略训练、失败数据、虚实更新 | ManiSkill3、Verti-Bench、CASHER、ASAP、Online Dynamics Adaptation | simulator bias；高保真模型太慢；安全长尾难覆盖 | 很高 |
| 三维重建 × 仿真 × 机器人 | 可更新世界状态、物理参数、任务效用 | Yutu-2 twin、CraterGrader、PINGS、Chrono sensor simulation | 缺少同时评价感知—物理—决策的 benchmark 和不确定性传播 | 高风险/高收益 |

## A. 三维重建 × 仿真

### A1. Physics-conditioned reconstruction benchmark

把太阳角、Hapke 参数、曝光、尘埃、相机内参和几何一起作为可控变量，系统测试重建模型，而不是只用固定 synthetic dataset。

- 支撑论文：StereoLunar、Physics-Based Lunar Sensor Simulation、VGGT/OmniVGGT。
- 最小实验：固定地形，逐一/联合扫描物理参数，测深度、位姿、完整度与置信校准。
- 贡献边界：建立“哪种物理变化导致哪类几何失败”的因果/敏感度图。
- 风险：`low-to-medium-risk`。

### A2. Reconstruction-driven simulator asset creation

从 analogue site 或真实任务图像快速构建可编辑几何/辐射资产，再用稀疏物理测量初始化接触层。

- 支撑论文：G3R、PINGS、CASHER。
- 关键难点：重建网格可渲染不等于可碰撞；需要 watertight、尺度、材质和物理分区修复。
- 风险：`medium-risk`。

### A3. Inverse rendering + inverse physics joint calibration

同时反演光度与地形参数，并报告参数相关性和不可辨识性。

- 关键问题：相似图像是否对应完全不同的土壤参数；必须引入本体感受或主动动作打破歧义。
- 风险：`high-risk/high-upside`。

## B. 三维重建 × 机器人

### B1. Task-aware / risk-aware mapping

地图根据规划敏感度分配分辨率、token、位宽和观测，而不是均匀追求视觉质量。

- 支撑论文：Lite/Q/FlashVGGT、GauSS-MI、Certifiably-Correct Mapping。
- 最小切口：在固定算力下保护小障碍、坑缘和高曲率区域，评价导航成功率而非只看平均深度。
- 风险：`low-to-medium-risk`，优先推荐。

### B2. Active reconstruction for navigation/science utility

将 GauSS-MI 的视觉互信息扩展为几何、地形参数、安全和科学目标的联合信息增益。

- 最小切口：固定能量预算，比较 frontier、几何 NBV、视觉 MI 和任务 MI。
- 风险：`medium-risk`。

### B3. Foundation-map uncertainty to formal safety

把 VGGT/MASt3R-SLAM 的深度和位姿置信度校准为集合，再接入可证明安全的局部 SDF。

- 关键难点：处理分布外场景的高置信错误。
- 风险：`medium-risk`。

## C. 仿真 × 机器人

### C1. Multi-fidelity sim-to-real policy training

高保真 DEM/SPH/CRM 只生成局部教师数据，降阶/残差模型用于大规模训练，真实数据做最终对齐。

- 支撑论文：CLVSim、elastic-wheel simulation、ManiSkill3、ASAP。
- 指标：策略表现、物理预测误差、每百万步成本、现实微调样本数。
- 风险：`medium-risk`。

### C2. Rare-failure curriculum and recovery policy

在仿真中系统生成陷车、打滑、传感器遮挡、轮故障和通信受限，使用 RLDG/CASHER 式数据生成与蒸馏。

- 风险：模拟长尾与真实长尾不一致；需要不确定性检测和安全回退。
- 风险等级：`medium-to-high-risk`。

### C3. Online digital-twin adaptation for MPC

将 Online Dynamics Adaptation 或 ASAP residual 持续写回数字孪生，用更新模型做短时域预测控制。

- 关键区别：不仅适配 policy，还维护显式模型版本、可信域和回滚机制。
- 风险：`medium-risk`。

## D. 三方向闭环

### D1. Geometry–Radiance–Terramechanics map

统一地图包含：SDF/mesh、3DGS/reflectance、地形参数后验、位姿和跨场协方差。观测来自视觉/LiDAR，本体感受更新地形层，规划反过来选择最有信息且安全的动作。

- 支撑链：PINGS → Chrono/CLVSim → Online Dynamics Adaptation → GauSS-MI/安全映射。
- 主要失败模式：不可辨识、算力过高、错误物理更新污染地图。
- 风险：`high-risk/high-upside`。

### D2. Landing-to-rover continuously updated twin

轨道/下降期重建初始化地形，rover 局部地图和接触观测持续修正；任务规划只使用带版本与置信域的地图。

- 支撑链：planetary descent neural height field → landmark-aware NeRF → MASt3R-SLAM/PINGS → digital twin。
- 风险：跨尺度配准与光照差异可能使先验产生负迁移。
- 风险：`medium-to-high-risk`。

## 推荐项目组合

### 可快速启动

**风险保持的三维重建压缩用于安全导航**：Lite/Q/FlashVGGT + 小障碍/坑缘 benchmark + certifiable local map。

### 中期系统论文

**物理条件化月面重建与主动感知**：StereoLunar/Chrono + OmniVGGT + task-aware NBV。

### 长期主线

**可在线校准的 perception–physics–decision 数字孪生**：PINGS-style map + 多保真轮壤 + 在线适配 + MPC/任务规划。

## 应避免的伪交叉

- 仅把月球纹理贴到通用机器人 simulator，不验证光度或接触物理；
- 仅把 3DGS 可视化接到机器人界面，却不参与定位、规划或控制；
- 只在 synthetic 数据上提升重建指标，就宣称 sim-to-real 有效；
- 用世界模型生成视觉上合理的未来，却不验证 metric geometry、碰撞和动力学；
- 同时堆叠三类方法但没有共同 benchmark、共享变量和消融设计。
