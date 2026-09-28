# 2026-09-28 周度研究雷达

本轮严格使用仓库内 `planetary-3d-robotics-radar` 与 `nature-academic-search` 的检索、来源分级、去重和核验规则。主窗口为 **2024-09-28—2026-09-28**；本周差量为 **2026-09-21—2026-09-28**，arXiv 实际可见最近发布日为 2026-09-25。经典里程碑仍见 [2026-08-31 基线](../2026-08-31/README.md)，不与新增论文混排。

## 本周结论

| 独立方向 | 新增 | 最值得读 | 独立判断 |
|---|---:|---|---|
| 三维重建 | 4 | [TrackEverything](01-3d-reconstruction.md#1-trackeverything本周首读) | 表示设计正在同时面对长时去重、跨平台可解码、超大场景分块和连续尺度查询四种部署约束 |
| 仿真与数字孪生 | 2（含 1 条跨周补检） | [X2Real](02-simulation-digital-twins.md#1-x2real本周首读) | 数字孪生可信度开始从“看起来相似”转向真实相关性、训练测试隔离与交互辨识的可审计证据 |
| 机器人视觉与具身视觉 | 6 | [Learning to Drive on Mars](03-robot-vision.md#1-learning-to-drive-on-mars本周首读) | 真实任务视觉数据、选择性风险、语义运动先验、空间语言定位、点级预测和主动可供性验证正在汇合 |

新增 12 篇均为 `emerging/preprint`；OceanXL 的 SIGGRAPH Asia 2026 只按作者在 arXiv 的声明处理，不冒充正式 proceedings 记录。本轮没有用引用数排序。

## 文件导航

- [方向一：三维重建](01-3d-reconstruction.md)
- [方向二：仿真与数字孪生](02-simulation-digital-twins.md)
- [方向三：机器人视觉与具身视觉](03-robot-vision.md)
- [两两交叉与三方向闭环](04-cross-track-opportunities.md)
- [可复现检索日志](query-log.md)
- [机器可读目录](../../planetary-3d-robotics-radar/references/paper-catalog.json)

## 证据边界

- 预印本中的指标均为作者报告，未替代独立复现；“将公开”的代码/数据不按已验证 artifact 计分。
- ForceTwin 首版为 2026-09-18，未在上一轮目录出现，本轮作为跨周补检而非伪装成本周首发。
- 仿真方向本轮未检出新的月球/火星、低重力、轮壤或行星传感器物理论文达到纳入门槛；纳入的两项是可迁移到行星场景的通用仿真/数字孪生方法信号。这不表示行星仿真本周不存在其他工作。
