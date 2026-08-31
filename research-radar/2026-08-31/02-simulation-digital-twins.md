# 方向二：仿真与数字孪生

本文件把仿真作为独立研究方向。核心问题不是“场景看起来是否真实”，而是仿真对设计、感知、控制和任务风险是否具有可验证的预测能力。行星部分重点关注月球/火星地形、低重力、轮壤和传感器物理。

## 近两年技术主线

### 1. 行星任务级数字孪生

- [Yutu-2 lunar digital twin](https://www.nature.com/articles/s41467-024-46233-8) 将任务地形、车辆动力学、轮壤模型与任务数据更新组合为月背数字孪生锚点。
- [CLVSim](https://onlinelibrary.wiley.com/doi/10.1002/rob.22421) 分别建模并验证软土、悬架、电机、车轮、驾驶员等子系统，再集成 Apollo LRV 级系统。
- [DVS](https://www.roboticsproceedings.org/rss21/p129.html) 虽非行星平台，但其运动捕捉 + ROS + 虚实代理双向同步，是实时更新型数字孪生的软件架构参考。

**判断**：数字孪生正从离线 CAD/动画走向“可被现实数据更新、能反向影响任务决策”的运行时系统。

### 2. 视觉传感与交互物理的耦合

- [A Physics-Based Sensor Simulation Environment for Lunar Ground Operations](https://doi.org/10.1109/AERO63441.2025.11068496) 用 Chrono、可变形地形、尘埃、光线追踪和 Hapke 光度模拟 VIPER/RASSOR 作业观测。
- [StereoLunar](https://openaccess.thecvf.com/content/ICCV2025W/3D-VAST/html/Grethen_Adapting_Stereo_Vision_From_Objects_To_3D_Lunar_Surface_Reconstruction_ICCVW_2025_paper.html) 用高分辨率地形与反射模型生成月球南极立体视觉监督。

**判断**：仿真研究应联合报告“像不像”和“下游算法误差是否被正确排序”；否则 photorealism 可能与感知有效性脱节。

### 3. 轮壤多保真建模与低重力外推

- [Using Gravitational Offset…Is Misleading](https://onlinelibrary.wiley.com/doi/10.1002/rob.22597) 用 CRM/SPH 与实验对照说明简单重力补偿不能代表低重力整车轮壤动力学。
- [Granular Scaling Laws for low-gravity slopes](https://doi.org/10.1016/j.jterra.2025.101085) 研究如何从 DEM/地球试验外推到低重力坡面轮移动性。
- [Efficient elastic-wheel simulation](https://www.sciencedirect.com/science/article/pii/S088832702600590X) 用降阶弹性轮 + 扩展 terramechanics，在系统级效率和高保真接触之间取中间层。
- [Comparison of lunar rover wheel performance in cohesive soils](https://doi.org/10.1016/j.jterra.2024.101011) 提供不同黏聚性材料下的单轮牵引与沉陷实验锚点。

**判断**：值得投入的是多保真模型栈：DEM/SPH/CRM 作为局部高保真参考，降阶模型服务系统仿真，在线模型服务规划控制；不同层之间必须传递误差分布。

### 4. 面向学习与 benchmark 的高速仿真

- [ManiSkill3](https://www.roboticsproceedings.org/rss21/p021.html) 提供 GPU 并行物理、渲染、异构环境、点云/体素和多类数字孪生。
- [Verti-Bench](https://www.roboticsproceedings.org/rss21/p138.html) 把崎岖地形、刚性/可变形接触和交互任务变成可重复移动性 benchmark。
- [DVS](https://www.roboticsproceedings.org/rss21/p129.html) 关注动态场景和虚实同步，而不是只追求并行吞吐。

**判断**：高速、真实、可编辑、可校准、可复现五个目标无法由一个 simulator 同时最大化，应公开 fidelity–speed–coverage Pareto 曲线。

## 独立值得探索的研究点

### S1. Validity-aware multi-fidelity planetary simulator

构建 DEM/SPH/CRM → 降阶轮壤 → 实时控制模型三级栈，并学习每一层的适用域和误差上界，而非只校准一组最佳参数。

- 最小实验：同一轮、同一土壤在不同坡度、载荷、滑移率和速度下跨模型比较。
- 指标：力/沉陷/滑移误差、实时因子、适用域覆盖、置信区间覆盖率。
- 风险：`medium-risk`。

### S2. Differentiable inverse simulation for regolith identification

从轮速、电机电流、IMU、轮迹和图像反演土壤/接触参数；重点研究参数不可辨识性与多解，而非只输出点估计。

- 基线：贝叶斯优化、EnKF、粒子滤波、可微物理、neural residual。
- 关键产物：参数后验 + 哪种新动作最能缩小后验。
- 风险：`high-risk/high-upside`。

### S3. Sensor-physics co-simulation benchmark

同时随机化太阳角、Hapke 参数、曝光、尘埃、地形几何与轮壤参数，评价重建、定位、滑移估计和导航的联合 sim-to-real gap。

- 不只报告 RGB FID/LPIPS；必须报告下游实例性能差异与参数敏感度。
- 风险：`medium-risk`。

### S4. Continuously synchronized planetary digital twin

借鉴 DVS 的虚实同步，但把更新源换成 analogue rover 或任务遥测；每次更新不仅修改位姿和场景，还更新物理参数与模型可信域。

- 指标：同化后多步预测误差、更新时间、通信量、错误更新恢复能力。
- 风险：`medium-to-high-risk`。

### S5. Benchmark design for interactive terrain

借鉴 Verti-Bench，把行星 benchmark 从静态图像/DEM 扩展为交互任务：陷车、坡面、坑缘、越障、挖掘和地形整备。

- 必须锁定任务生成器、物理版本、随机种子、传感模型和评价协议。
- 风险：`low-to-medium-risk`，容易形成社区资产。

## 推荐精读顺序

1. Yutu-2 digital twin：任务数据驱动的数字孪生范式。
2. CLVSim：分系统建模和验证链。
3. Gravitational Offset Is Misleading：理解仿真有效性的反例。
4. Physics-Based Lunar Sensor Simulation：传感与交互物理耦合。
5. ManiSkill3、DVS、Verti-Bench：比较高速、同步和 benchmark 三种平台目标。
