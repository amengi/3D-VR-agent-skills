# 2026-10-12 周度研究雷达

本轮严格使用仓库内 `planetary-3d-robotics-radar` 与 `nature-academic-search` 的多源检索、来源分级、去重和核验规则。主窗口为 **2024-10-12—2026-10-12**；相对上一版的差量为 **2026-09-28—2026-10-12**，官方 arXiv 最近发布日为 2026-10-09。经典里程碑继续见 [2026-08-31 基线](../2026-08-31/README.md)，不与本轮新增混排。

## 本轮结论

| 独立方向 | 新增 | 最值得读 | 独立判断 |
|---|---:|---|---|
| 三维重建 | 5 | [Slot3R](01-3d-reconstruction.md#1-slot3r本轮首读) | 前馈重建开始把多状态空间记忆、gauge 对齐、不确定度、主动采集与稀疏注意力放进同一部署问题 |
| 仿真与数字孪生 | 4 | [MarsLab](02-simulation-digital-twins.md#1-marslab本轮首读) | 行星视觉仿真有了开源火星底座；局部接触神经仿真与成对可编辑 twin 把 fidelity 评价推向可归因证据 |
| 机器人视觉与具身视觉 | 6 | [DepthWorld](03-robot-vision.md#1-depthworld本轮首读) | metric 世界模型、视觉故障安全、可变相机集合、主动看视角与 SE(3) 运动表示正在汇合 |

新增 15 篇均按 `emerging/preprint` 记录；CoRL 2026、NeurIPS 2026/Spotlight、iSpaRo 2026 等仅有作者或项目页声明时，不冒充正式 proceedings 记录。本轮不使用引用数排序。

## 文件导航

- [方向一：三维重建](01-3d-reconstruction.md)
- [方向二：仿真与数字孪生](02-simulation-digital-twins.md)
- [方向三：机器人视觉与具身视觉](03-robot-vision.md)
- [两两交叉与三方向闭环](04-cross-track-opportunities.md)
- [可复现检索日志](query-log.md)
- [机器可读目录](../../planetary-3d-robotics-radar/references/paper-catalog.json)

## 证据边界

- 指标均来自作者摘要或项目页，未替代独立复现；已核验公开仓库不等于已核验全部实验可复现。
- 本轮仿真方向虽纳入 MarsLab，但低重力、轮壤接触物理与持续同步数字孪生子主题仍为 **本轮未检出**；这不表示这些子领域不存在新工作。
- `ReVar3R` 能去除坐标 gauge 造成的伪不确定度，但作者明确指出它不能发现跨扰动稳定存在的系统性偏差。
- `RenderBench` 只有 12 个真实场景、1,496 对帧；其验证设计有启发性，但尚不能代表开放世界数字孪生。
