# 2026-10-19 可复现检索日志

## 范围与协议

- 检索日：2026-10-19（Asia/Shanghai）
- 主窗口：2024-10-19—2026-10-19
- 相对上一版差量：2026-10-12—2026-10-19；官方 arXiv 最近发布日为 2026-10-16
- 出版类型：官方 proceedings、出版社和 DOI 优先；没有正式记录的预印本标为 `preprint/emerging`
- 去重：规范化 DOI；无 DOI 时用规范化标题 + 第一作者；与原 100 条已发布目录比较
- 排序：仓库六维 rubric，预印本 `source_quality ≤ 9`；不使用引用数
- 三个查询族先独立筛选；交叉价值只在确定纳入集后分析

## 查询族

```text
(3D reconstruction OR multi-view geometry OR neural field OR NeRF OR 3DGS
 OR visual geometry foundation model OR dynamic OR 4D OR streaming)
AND (motion OR gravity OR reliability OR metric OR queryable latent
 OR reflectance OR material OR uncertainty)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR regolith OR low gravity
 OR simulation OR digital twin OR sensor physics OR multi-fidelity)
AND (active generative simulation OR probabilistic physics OR differentiable contact
 OR wheel soil OR continuous synchronization OR real2sim2real)
```

```text
(visual SLAM OR hyperspectral OR RGB-D OR LiDAR OR point cloud OR multi-view
 OR affordance OR active vision OR navigation OR VLN OR visual manipulation
 OR VLA OR visual world model OR world action model)
AND (robot OR embodied OR rover OR lunar OR manipulation)
```

## `nature-academic-search` 路由与故障记录

1. 按 `multi-source-search` 工作流运行 PubMed/Crossref/arXiv 多源预检；沙箱内三个 T1 端点均发生 DNS 解析失败。
2. 在授权联网环境重试后没有得到可用元数据响应；没有关闭 TLS/SSL 验证，也没有修改安全配置。
3. 按技能 fallback 规则检索 arXiv 官方 `cs.CV/recent`、`cs.RO/recent`、`cs.GR/recent` 最近发布列表，并逐篇核验官方摘要、提交日期、DOI/期刊信息、作者项目页。
4. 只有 MicroSDF 通过 arXiv journal reference 与 IEEE DOI 交叉核验为正式发表；其余没有独立 publisher/proceedings 记录时维持 `preprint`。

## 纳入结果（13）

### 三维重建（4）

- Motion- and Gravity-Aware Feedforward 3D Reconstruction — arXiv:2610.22177，2026-10-15
- SceneAE — arXiv:2610.19708，2026-10-14
- MicroSDF — arXiv:2610.19681，2026-10-14；IEEE TIP 2026，DOI: 10.1109/TIP.2026.3678096
- MIRAGE — arXiv:2610.12568，v1 2026-10-08、v2 2026-10-14；作为上一轮发布边界后的透明补录

### 仿真与数字孪生（3）

- Active Generative Simulation / MetaGenSim — arXiv:2610.19479，2026-10-14；CoRL 2026 为作者声明
- Probabilistic Physics Digital Twin — arXiv:2610.19336，2026-10-14
- DiffGIPC — arXiv:2610.19091，2026-10-13
- 月球/火星低重力、轮壤、传感器物理和持续同步数字孪生高相关差量：**本轮未检出**。

### 机器人视觉与具身视觉（6）

- End-to-End VLA Policies for Autonomous Lunar Rover Docking — arXiv:2610.19224，2026-10-13
- HyperLoop — arXiv:2610.19742，2026-10-14；IAC 2026 接收为作者声明
- LidarVerse — arXiv:2610.19201，2026-10-13
- BridgeAfford — arXiv:2610.21918，2026-10-15
- P³-WAM — arXiv:2610.22363，2026-10-15
- All-St3R SLAM — arXiv:2610.16143，2026-10-12；IROS 2026 接收为作者声明

## 去重、排除与观察池

- 13 条按 DOI、arXiv ID、规范化标题 + 第一作者与原 100 条目录去重；未发现目录重复。
- Motion/Gravity、SceneAE、MicroSDF、MIRAGE 先按三维重建独立价值筛入；不是因为其对机器人或仿真的交叉价值。
- Active Generative Simulation、概率 twin、DiffGIPC 先按模拟数据分布、物性不确定度、可微接触价值筛入；三者都不是行星专用论文，文档中未作此声称。
- Lunar docking VLA、HyperLoop、LidarVerse、BridgeAfford、P³-WAM、All-St3R 均有明确视觉机制与任务闭环；纯机械机构、执行器、材料、纯控制、纯动力学辨识和非视觉 RL 按边界排除。
- Safe and Fuel-Efficient Motion Planning for Lunar Propulsive Drones（arXiv:2610.22225）以规划/控制为主，排除。
- Learning Safety-Constrained Whole-Body Loco-Manipulation for Lunar Surface Operations（arXiv:2610.15486）以 whole-body control 为主，排除。
- Toward Lunar Legged Robots（arXiv:2610.12276）首版早于差量且更偏平台部署经验，不跨周回填。
- Graph3R、Anchor3DGS、CompactSplat、PUGS、LIN-SLAM 等进入观察池：主题相关，但本轮代表集已覆盖初始化/压缩/水下 UQ/轻量定位的主要相邻问题。
- MIRAGE 的 v1 早于差量起点；因 v2 在本周更新且上一目录漏记，明确标为“补录”，不伪装为本周首发。

## 下一轮核验

- Motion/Gravity 的逐数据集量化结果、错误 gravity/flow 和真实 IMU 消融；SceneAE 的 metric/online update；MIRAGE 的跨模态时间同步。
- MetaGenSim 的正式 CoRL 记录、代码与参数空间外泛化；概率 twin 的 calibration 数值；DiffGIPC 的公开实现和颗粒/地形适用边界。
- 月球 docking VLA 的模拟器配置/代码、真实类比场证据；HyperLoop 数据/代码与 SWIR 预注册；All-St3R 的正式 IROS proceedings。
- LidarVerse/P³-WAM/BridgeAfford 的公开 checkpoint、严格跨场景拆分和真实闭环任务指标。
