# 2026-09-14 可复现检索日志

## 范围与协议

- 检索日：2026-09-14（Asia/Shanghai）
- 主窗口：2024-09-14—2026-09-14
- 本周差量：2026-09-07—2026-09-14；arXiv 实际可见最近发布日为 2026-09-11
- 出版类型：正式会议/期刊和 DOI 优先；高价值预印本标为 `preprint/emerging`
- 去重：规范化 DOI；无 DOI 时用规范化标题 + 第一作者；与原 53 条目录交叉检查
- 排序：仓库六维 rubric；预印本来源质量不超过 9/15；不使用引用数

## 三个独立查询族

```text
(3D reconstruction OR structure from motion OR neural field OR NeRF
 OR 3D Gaussian splatting OR visual geometry foundation model)
AND (online OR streaming OR dynamic OR scalable OR reliable OR interactive)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR space robotics OR regolith)
AND (simulation OR digital twin OR low gravity OR wheel soil OR terramechanics
 OR sensor physics OR multi-fidelity OR synchronization)
```

```text
(visual SLAM OR RGB-D OR point cloud OR multi-view OR functional scene graph
 OR open-vocabulary map OR affordance OR active vision OR VLN
 OR visual manipulation OR visual imitation OR VLA OR visual world model)
AND (robot OR embodied)
```

定向检查 arXiv `cs.CV/recent`、`cs.RO/recent`、论文官方 arXiv 页面、出版社页面和 DOI。方向三先按“视觉机制是否是核心贡献”筛选，未按与重建/仿真的交叉价值倒推。

## 来源路由与故障记录

1. 按 `nature-academic-search` 先运行 PubMed/Crossref/arXiv 预检；沙箱内 DNS 失败。
2. 获得联网执行权限后再次运行，三个端点均因本机 TLS CA 校验失败而终止；未关闭证书验证。
3. OpenAlex 后备查询同样因 TLS CA 校验失败；按 skill 的二次失败规则切换到官方网页手工核验。
4. 正式状态只在出版社/DOI 页面可确认时升级；LightSplat、view-graph SfM、FocusPool、RoboReel 和 mjorbit 的会议身份均仅由作者在 arXiv comments 声明，因此保留 `preprint`。

## 纳入结果

### 三维重建（3）

- FIRE3D — arXiv:2609.08848，2026-09-08
- LightSplat — arXiv:2609.07274，2026-09-07
- Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion — arXiv:2609.09491，2026-09-08

### 仿真与数字孪生（2 + 1 修正）

- mjorbit — arXiv:2609.08010，2026-09-07
- Digital Twin Models for Space Robotics — *Array* 30 (2026) 100902，DOI: 10.1016/j.array.2026.100902；本轮新发现的目录缺口，不是本周新发表
- Data-Driven Terramechanics Approach Towards a Realistic Real-Time Simulator for Lunar Rovers — arXiv:2601.04547；从既有文字基线补入机器目录，不计新增

### 机器人视觉与具身视觉（4）

- Functional-SLAM — arXiv:2609.07497，2026-09-07
- FARM — arXiv:2609.11445，2026-09-10
- FocusPool — arXiv:2609.08408，2026-09-08
- RoboReel — arXiv:2609.08209，2026-09-08；2026-09-09 修订

## 去重、排除与观察

- 10 条写入均未与原目录的 DOI、规范化标题或 URL 重复；其中 1 条明确标为“文字已有、机器目录补齐”。
- RouteBridge、OmniPoint、SAMV-DUSt3R：与可靠路由、全相机模型和实例重建高度相关，但本周代表集已覆盖资产化、在线 3DGS 与全局 SfM；进入观察，不以数量替代代表性。
- Beyond Task Success：视觉/世界模型分阶段退化诊断很有启发，但与 FARM 的可靠性问题重合，本周放入观察池。
- DeCAL、TANGO：分别含视触觉操作与视觉导航价值，但前者混入接触控制、后者强调全身动作；本轮不作为机器视觉首选。
- 纯机械结构、本体设计、材料、执行器、纯控制、纯动力学辨识和无视觉机制的一般强化学习全部排除。

## 下一轮核验

- ECCV/IROS/CoRL/ISPARO 2026 官方 proceedings 出现后升级或纠正作者声明状态；
- FIRE3D/Functional-SLAM/mjorbit/RoboReel 代码的许可证、权重、数据与可执行性；
- 数字孪生综述 46 篇样本中的持续同步、UQ、HIL/SIL 编码是否可复核；
- NASA NTRS、JPL、ESA 以及月球/火星地表仿真与传感器物理的新记录。
