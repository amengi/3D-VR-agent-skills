# 方向三：机器人

本文件把机器人作为独立方向，重点覆盖定位建图、安全导航、在线动力学适配、世界模型、通用策略与移动操作。并非每篇论文都依赖三维重建或行星仿真。

## 近两年技术主线

### 1. 从感知地图到安全可用地图

- [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](https://www.roboticsproceedings.org/rss21/p007.html) 把里程计误差传播到局部安全空间，对 SDF/安全走廊给出正确性保证。
- [MISO](https://www.roboticsproceedings.org/rss21/p004.html) 用多分辨率子图维持大尺度神经隐式重建的全局一致性。
- [PINGS](https://www.roboticsproceedings.org/rss21/p040.html) 让地图同时服务几何、视觉与里程计。

**判断**：机器人地图的评价正在从“重建误差”转向“是否能支撑安全、规划、回环和长期运行”。

### 2. 平台感知的导航与在线动力学适配

- [Learned Perceptive Forward Dynamics Model](https://www.roboticsproceedings.org/rss21/p001.html) 从周围几何和本体历史预测状态与失败概率，并接入 MPPI。
- [Meta-Learning Online Dynamics Model Adaptation](https://www.roboticsproceedings.org/rss21/p139.html) 让车辆在新地形上沿元学习子空间快速更新动力学。
- [Adaptive Locomotion on Mud](https://www.roboticsproceedings.org/rss21/p126.html) 用本体感受估计可变形基底性质并调整运动策略。

**判断**：仅做视觉地形分类正在让位于“动作条件下会发生什么”的动力学预测；视觉、接触和本体感受应当联合建模。

### 3. 世界模型与约束可插拔规划

- [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) 用动作条件视频生成模型想象并筛选导航轨迹。
- [Differentiable GPU-Parallelized Task and Motion Planning](https://www.roboticsproceedings.org/rss21/p050.html) 在 GPU 上并行探索大量连续解，并在双层 TAMP 中处理长时程约束。
- [GauSS-MI](https://www.roboticsproceedings.org/rss21/p030.html) 把地图不确定性转成主动视点规划目标。

**判断**：世界模型擅长提出和排序候选，解析/优化规划器擅长执行硬约束；两者结合比纯生成或纯搜索更值得研究。

### 4. 通用策略、数据生成与 sim-to-real

- [Robot Learning with Super-Linear Scaling / CASHER](https://www.roboticsproceedings.org/rss21/p025.html) 通过重建数字孪生和仿真数据摊薄人类示范成本。
- [RLDG](https://www.roboticsproceedings.org/rss21/p028.html) 用任务专用 RL 生成更优状态—动作覆盖，再蒸馏进通用策略。
- [ASAP](https://www.roboticsproceedings.org/rss21/p066.html) 从真实 rollout 学 residual action model，放回 simulator 对齐动力学。
- [SpatialVLA](https://www.roboticsproceedings.org/rss21/p011.html) 用 3D 位置编码和自适应 action grid 强化 VLA 的空间与跨机器人迁移能力。

**判断**：机器人 foundation policy 的瓶颈正在从模型规模转向数据覆盖、物理一致性、动作空间对齐和失败数据稀缺。

### 5. 行星移动操作与场地作业

- [CraterGrader](https://www.roboticsproceedings.org/rss20/p018.html) 将在线感知、无 GPS 定位、能量优化、地形整备和工具控制闭成月面作业系统（near-window）。
- [Passivity-Based Tracking Control of a Planetary Rover With Robotic Arm](https://elib.dlr.de/225596/) 研究 rover-arm 非完整约束下的被动性和全身跟踪控制。

**判断**：行星机器人研究不应只做“车能走”，还应把采样、部署、挖掘、整备等任务级目标纳入系统评价。

## 独立值得探索的研究点

### B1. Safety-guaranteed learned mapping

将深度/位姿的不确定性校准为可覆盖的集合，再由局部 SDF 或控制屏障函数保证规划安全。

- 指标：置信覆盖率、错误安全区面积、碰撞率、保守导致的任务失败率。
- 风险：`medium-risk`。

### B2. Vision–proprioception online terrain adaptation

通过视觉预测地形先验，通过轮速、电流、IMU 和沉陷在线修正，输出动作条件下的状态和失败分布。

- 核心问题：安全探索与参数辨识的冲突。
- 风险：`high-risk/high-upside`。

### B3. Geometry-grounded navigation world model

在 Navigation World Model 的视觉想象外增加 metric geometry、可通行性和能量状态；生成模型负责候选，安全后端负责硬约束。

- 指标：多步几何误差、约束违反率、候选排序质量、MPC 计算量。
- 风险：`medium-risk`。

### B4. Generalist policy for rare recovery behaviors

用 RL 在仿真中生成陷车恢复、轮故障、打滑和受限通信等少见数据，再蒸馏到通用策略；真实数据只用于残差对齐与安全验证。

- 主要风险：模拟失败模式不覆盖真实长尾，策略学会利用 simulator artifact。
- 风险：`medium-to-high-risk`。

### B5. Task-and-motion planning for mobile manipulation in unstructured terrain

把 rover 路径、底盘稳定性、机械臂可达性、工具接触和能量作为统一 TAMP 约束。

- 最小任务：移动到岩石—稳定停车—机械臂接触/采样—安全撤离。
- 风险：`medium-risk`。

## 推荐精读顺序

1. Certifiably-Correct Mapping：感知不确定性如何进入正式安全保证。
2. Perceptive FDM + Online Dynamics Adaptation：从几何地图走向平台条件动力学。
3. Navigation World Models：生成式预测如何进入规划。
4. CASHER + RLDG + ASAP：三种不同的数据/仿真/现实闭环。
5. CraterGrader：检验上述方法是否能组合成真实任务系统。
