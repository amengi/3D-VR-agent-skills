# 2026-09-07 可复现检索日志

## 范围与协议

- 检索日：2026-09-07
- 主窗口：2024-09-07—2026-09-07
- 本周差量：2026-09-01—2026-09-07；arXiv 本周最近发布日为 2026-09-04
- 语言：英语为主；中文扩展词已记录，计划在后续中文数据库可用时补检
- 出版类型：正式会议/期刊优先；高价值预印本标记为 `preprint/emerging`
- 去重：规范化 DOI 优先；无 DOI 时按规范化标题 + 第一作者；本轮 6 篇均未与既有 47 条重复
- 排序：不使用引用数；按仓库六维 rubric，预印本来源质量不超过 9/15

## 查询族

```text
(3D reconstruction OR Gaussian splatting OR visual geometry transformer)
AND (online OR streaming OR long sequence OR scalable OR reliable)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR regolith)
AND (simulation OR digital twin OR terramechanics OR wheel soil
OR low gravity OR sensor simulation OR multi-fidelity)
```

```text
(visual SLAM OR RGB-D OR point cloud OR multi-view OR open-vocabulary map
OR affordance OR active vision OR VLN OR visual manipulation OR VLA
OR visual world model OR 4D world model) AND robot
```

定向页面：arXiv `cs.CV/recent` 与 `cs.RO/recent`；官方 CVF 2026；Elsevier、Wiley、DOI、NASA/JPL/ESA 发现查询。检索工具还对 arXiv 2609 前缀及 ECCV/IROS 2026 状态做了补充查询。

## 来源路由与故障记录

1. 严格按 `nature-academic-search` 先尝试 OpenAlex 多源脚本；沙箱内 DNS 失败。
2. 获得联网权限后重试三条独立查询，均因本机 CA 证书校验失败而停止；未绕过 TLS 验证。
3. 后备路径使用 arXiv 官方分类列表和论文页完成日期、作者、题名、摘要与状态核验；出版社/会议官网用于正式状态核验。
4. Scal3R 的 “ECCV 2026” 当前只出现在作者 arXiv comments；目录因此保留 `preprint`，不升级为同行评议。

## 纳入结果

### 三维重建

- Scal3R — arXiv:2609.04201，2026-09-03
- On-the-Fly3R — arXiv:2609.00923，2026-09-01
- VI3 — arXiv:2609.03824，2026-09-03

### 仿真与数字孪生

- **本轮未检出**。发现结果要么已在基线目录，要么偏向纯轮结构/机构设计、无持续同步含义的静态模型，或缺乏可核验来源。

### 机器人视觉与具身视觉

- VOIM — arXiv:2609.00775，2026-09-01
- GIFT — arXiv:2609.04193，2026-09-03
- WISE — arXiv:2609.03681，2026-09-03

## 重点排除/观察

- DualDiff3D：与可靠 3DGS 高相关，但本周优先保留可诊断长序列/大尺度机制；列为候选观察，不进入代表目录。
- Puffin-World：原生 3D 世界状态很有启发，但当前摘要未给出明确机器人任务闭环验证，不纳入方向三；可作为交叉启发观察。
- 纯抓取力闭合、全身补偿、运动控制、轮结构设计：若视觉并非核心机制，按方向边界排除。
- 仅声明投稿、无正式接收记录：不视为同行评议。

## 下一轮状态核验

- ECCV 2026 官方 proceedings：Scal3R 及相关 accepted-paper 身份；
- IROS 2026 官方 proceedings：视觉 SLAM、开放词汇地图、地形/传感仿真；
- 新增代码仓库是否提供可运行权重、许可证与复现实验；
- NASA NTRS、JPL、ESA 与中文任务线的月/火星仿真记录。
