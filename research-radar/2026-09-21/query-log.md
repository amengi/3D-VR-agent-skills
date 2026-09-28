# 2026-09-21 可复现检索日志

## 范围与协议

- 检索日：2026-09-21（Asia/Shanghai）
- 主窗口：2024-09-21—2026-09-21
- 本周差量：2026-09-14—2026-09-21；arXiv 实际可见最近发布日为 2026-09-18
- 出版类型：官方 proceedings/出版社/DOI 优先；预印本标为 `preprint/emerging`
- 去重：规范化 DOI；无 DOI 用规范化标题 + 第一作者；与原 63 条目录比较
- 排序：仓库六维 rubric，预印本 `source_quality ≤ 9`；不使用引用数

## 三个独立查询族

```text
(3D reconstruction OR SfM OR NeRF OR 3DGS OR visual geometry foundation model
 OR dynamic reconstruction OR 4D reconstruction)
AND (online OR streaming OR scalable OR bounded compute OR reliable OR HDR OR memory)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR regolith OR space robotics)
AND (simulation OR digital twin OR low gravity OR wheel soil OR slip
 OR sensor physics OR multi-fidelity OR synchronization OR transfer)
```

```text
(visual SLAM OR RGB-D OR point cloud OR open-vocabulary 3D
 OR semantic memory OR object part OR articulation OR affordance
 OR active vision OR VLN OR visual manipulation OR VLA OR visual world model)
AND (robot OR embodied OR UAV)
```

## 来源路由与故障记录

1. 按 `nature-academic-search` 运行 PubMed/Crossref/arXiv 预检：沙箱内 DNS 失败。
2. 联网权限下重试：三个 T1 端点均被本机 TLS CA 链阻断；未关闭证书验证。
3. 按二次失败规则切换至 arXiv 官方 `cs.CV/recent`、`cs.RO/recent` 和论文页；正式状态另用 ECCV/ECVA accepted-paper 页面核验。
4. ECCV 页面确认 Scal3R 与 view-graph SfM 已在官方接收列表，但页面注明 preliminary pending publisher checks；不猜测 DOI。

## 纳入结果

### 三维重建（5 + 2 状态更新）

- EliGSiR — arXiv:2609.20348，2026-09-17
- AMB3R-SLAM — arXiv:2609.19518，2026-09-17
- RawSLAM — arXiv:2609.20589，2026-09-17
- SplashSplat — arXiv:2609.20818，2026-09-17
- Can 4D Foundation Models Remember? / PersistBench — arXiv:2609.20819，2026-09-17
- Scal3R — 官方 ECCV 2026 接收状态更新
- Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion — 官方 ECCV 2026 接收状态更新

### 仿真与数字孪生（1）

- Fleet-To-Lab — arXiv:2609.17187，2026-09-15；i-SAIRAS/iSpaRo 2026 接收仅作者声明
- 其余高相关差量：**本轮未检出**。

### 机器人视觉与具身视觉（4）

- SenseFuse — arXiv:2609.20475，2026-09-17
- PerSeM — arXiv:2609.19542，2026-09-17
- AnyviewMeter — arXiv:2609.20106，2026-09-17
- FunArt — arXiv:2609.20673，2026-09-17

## 去重、排除与观察

- 10 个新增标题/第一作者/URL 与原 63 条目录无重复；2 条只更新正式状态，不新增记录。
- SCOUT-SLAM 提交时间为 2026-09-13，略早于差量起点，列入观察池；不以“本周 recent 列表出现”替代首版日期。
- FAMOS 与 FunArt 同属 articulation；本轮方向三保留后者，因为同时输出功能交互部件。FAMOS 进入观察池。
- VGGT-GS SLAM、PhGS、TRiGS 等与本周已选机制重叠；不以数量替代代表性。
- Pelican-Sim 首版为 2026-09-10，且偏通用具身世界模型模拟器，不作为本周行星仿真新增。
- Scene-Q 的首版日期为 2026-07-28，不属于本周差量。
- 纯机械、本体、执行器、纯控制、动力学辨识与无视觉机制的一般 RL 均排除。

## 下一轮核验

- ECCV 2026 Springer 论文页、DOI 和卷页；
- Fleet-To-Lab 的正式 symposium proceedings 与真实/类比场验证；
- EliGSiR、RawSLAM、SplashSplat、PersistBench 的代码/数据许可证和可执行状态；
- NASA NTRS、JPL、ESA 及月/火星传感器物理、多保真同步数字孪生新记录。
