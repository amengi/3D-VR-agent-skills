# 2026-10-19 周度研究雷达

本轮严格使用仓库内 `planetary-3d-robotics-radar` 与 `nature-academic-search` 的多源检索、来源分级、去重和核验规则。主窗口为 **2024-10-19—2026-10-19**；相对上一版的差量为 **2026-10-12—2026-10-19**，官方 arXiv 最近发布日为 2026-10-16。经典里程碑继续见 [2026-08-31 基线](../2026-08-31/README.md)，不与本轮新增混排。

## 本轮结论

| 独立方向 | 新增/补录 | 最值得读 | 独立判断 |
|---|---:|---|---|
| 三维重建 | 4（3 新增 + 1 补录） | [Motion- and Gravity-Aware Feedforward 3D Reconstruction](01-3d-reconstruction.md#1-motion--and-gravity-aware-feedforward-3d-reconstruction本轮首读) | 前馈几何开始显式吸收运动/重力先验、metric 传感锚点、可查询 3D latent 与材质物理 |
| 仿真与数字孪生 | 3 | [Active Generative Simulation](02-simulation-digital-twins.md#1-active-generative-simulation本轮首读) | 模拟器从固定数据源转向主动选择数据分布，并以概率物性和可微接触支持风险与参数反演 |
| 机器人视觉与具身视觉 | 6 | [End-to-End VLA for Lunar Rover Docking](03-robot-vision.md#1-月球车自主对接-vla本轮首读) | 行星视觉闭环、光谱回环、跨 LiDAR 传感器世界模型、3D affordance 与 world-action model 同周出现 |

目录新增 13 条：12 条 `preprint/emerging`，1 条（MicroSDF）由 IEEE TIP DOI 核验为 `peer_reviewed`。MIRAGE 是对 2026-10-08 首版的透明补录，其 v2 于 10 月 14 日更新；IROS/IAC/CoRL 等仅有作者声明时仍按预印本记录。本轮不使用引用数排序。

## 文件导航

- [方向一：三维重建](01-3d-reconstruction.md)
- [方向二：仿真与数字孪生](02-simulation-digital-twins.md)
- [方向三：机器人视觉与具身视觉](03-robot-vision.md)
- [两两交叉与三方向闭环](04-cross-track-opportunities.md)
- [可复现检索日志](query-log.md)
- [机器可读目录](../../planetary-3d-robotics-radar/references/paper-catalog.json)

## 证据边界

- 摘要中的指标与结论均是作者报告，不能替代独立复现；arXiv comments 中的会议接收声明不等于已核验 proceedings。
- 月球/火星低重力、轮壤与传感器物理、持续在线同步数字孪生的高相关差量为 **本轮未检出**；这不表示这些子领域没有新工作。
- HyperLoop 是重要的负结果：600–860 nm HSI 没有带来可归因增益，作者反而据此提出应试验 SWIR；本雷达保留负证据，不只收“刷新指标”的论文。
- LidarVerse 的 11 FPS 来自单张 H100；不能外推为 rover 板端实时。月球对接 VLA 只在作者构建的高保真模拟闭环中验证，尚非真实月面证据。
