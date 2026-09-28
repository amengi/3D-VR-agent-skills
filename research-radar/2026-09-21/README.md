# 2026-09-21 周度研究雷达

本轮严格使用仓库内 `planetary-3d-robotics-radar` 与 `nature-academic-search` 的检索、来源分级、去重和核验规则。主窗口为 **2024-09-21—2026-09-21**；本周差量为 **2026-09-14—2026-09-21**，arXiv 实际可见最近发布日为 2026-09-18。经典里程碑仍见 [2026-08-31 基线](../2026-08-31/README.md)，不与新增论文混排。

## 本周结论

| 独立方向 | 新增/状态更新 | 最值得读 | 独立判断 |
|---|---:|---|---|
| 三维重建 | 5 + 2 条 ECCV 正式状态更新 | [EliGSiR](01-3d-reconstruction.md#1-eligsir本周首读) | 在线重建开始把长期一致性、有限算力、照明动态范围和离场对象记忆拆成独立可测问题 |
| 仿真与数字孪生 | 1 | [Fleet-To-Lab](02-simulation-digital-twins.md#1-fleet-to-lab本周首读) | 本周高相关证据聚焦“如何用异构历史模型和少量新数据跨越地球—月球域差” |
| 机器人视觉与具身视觉 | 4 | [SenseFuse](03-robot-vision.md#1-sensefuse本周首读) | 视觉系统正在从单帧单模态决定转向跨模态分歧、长期记忆、相机几何和功能部件联合建模 |

新增 10 篇均为 `emerging/preprint`；Fleet-To-Lab 的会议接收仅有作者在 arXiv 的声明。上周的 Scal3R 与 *Learning Global Camera Poses from Noisy View-Graphs* 已在 ECCV 2026 官方 accepted-paper 列表出现，机器目录本周升级为 `peer_reviewed`；该列表仍标注“preliminary pending publisher checks”，所以尚未补写 Springer DOI。

## 文件导航

- [方向一：三维重建](01-3d-reconstruction.md)
- [方向二：仿真与数字孪生](02-simulation-digital-twins.md)
- [方向三：机器人视觉与具身视觉](03-robot-vision.md)
- [两两交叉与三方向闭环](04-cross-track-opportunities.md)
- [可复现检索日志](query-log.md)
- [机器可读目录](../../planetary-3d-robotics-radar/references/paper-catalog.json)

## 证据边界

- 预印本数字均为作者报告，不能替代独立复现；代码/数据“将公开”不按已验证 artifact 计分。
- 仿真方向只有 1 篇达到本轮相关性门槛；这表示“本轮检出 1 篇”，不表示领域只有一项新工作。
- 不使用引用数排序；优先级来自六维 rubric 与可验证研究问题。
