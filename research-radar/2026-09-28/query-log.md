# 2026-09-28 可复现检索日志

## 范围与协议

- 检索日：2026-09-28（Asia/Shanghai）
- 主窗口：2024-09-28—2026-09-28
- 本周差量：2026-09-21—2026-09-28；arXiv 实际可见最近发布日为 2026-09-25
- 出版类型：官方 proceedings/出版社/DOI 优先；预印本标为 `preprint/emerging`
- 去重：规范化 DOI；无 DOI 用规范化标题 + 第一作者；与原 73 条目录比较
- 排序：仓库六维 rubric，预印本 `source_quality ≤ 9`；不使用引用数

## 三个独立查询族

```text
(3D reconstruction OR SfM OR neural field OR NeRF OR 3DGS
 OR visual geometry foundation model OR dynamic OR 4D OR streaming)
AND (compression OR long-horizon OR scalable OR reliable OR continuous OR uncertainty)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR regolith OR low gravity
 OR digital twin OR simulation OR sensor physics OR multi-fidelity)
AND (wheel soil OR slip OR synchronization OR calibration OR sim-to-real OR physics-informed)
```

```text
(visual SLAM OR RGB-D OR LiDAR OR point cloud OR open-vocabulary map
 OR spatial grounding OR affordance OR active vision OR navigation OR VLN
 OR visual manipulation OR VLA OR visual world model OR 4D world model)
AND (robot OR embodied OR rover OR UAV)
```

## 来源路由与故障记录

1. 按 `nature-academic-search` 先运行 PubMed/Crossref/arXiv 多源预检：沙箱内三个端点均 DNS 失败。
2. 依规则在联网权限下重试一次：三个端点均被本机 TLS CA 链阻断；未关闭证书验证、未绕过安全检查。
3. 二次失败后切换到 arXiv 官方 `cs.CV/recent?show=1000`、`cs.RO/recent?show=1000`、逐篇官方摘要页和定向 `arxiv.org` 检索。
4. 论文首版日期、作者、摘要、分类和作者声明均以官方 arXiv 页面核验；正式会议状态没有官方 proceedings/DOI 时不升级为 peer-reviewed。

## 纳入结果

### 三维重建（4）

- Towards Practical Compression of 3D Gaussian Splatting / COSA-GS — arXiv:2609.30245，2026-09-24
- TrackEverything — arXiv:2609.30222，2026-09-24
- OceanXL — arXiv:2609.29985，2026-09-24；SIGGRAPH Asia 2026 仅作者声明
- Efficient Continuous DEM Reconstruction / SCOPE — arXiv:2609.29864，2026-09-24

### 仿真与数字孪生（2）

- X2Real — arXiv:2609.27449，2026-09-23
- ForceTwin — arXiv:2609.21751，2026-09-18；跨周补检
- 月球/火星、低重力、轮壤和行星传感器物理高相关差量：**本轮未检出**。

### 机器人视觉与具身视觉（6）

- Learning to Drive on Mars — arXiv:2609.24952，2026-09-21
- SplatLabel — arXiv:2609.29836，2026-09-24
- Retrieve-to-Localize / SpatialLiDAR-LM — arXiv:2609.29835，2026-09-24
- KYS-SLAM — arXiv:2609.27509，2026-09-23
- PointCast — arXiv:2609.28393，2026-09-23
- Imagine then Verify / ATAP — arXiv:2609.23504，2026-09-20；在本轮官方 recent 列表首次核验

## 去重、排除与观察

- 12 个标题/第一作者/URL 与原 73 条目录无重复；无 publisher DOI 可用于二次去重。
- ADATEX4D 与本轮已选动态/大场景 3DGS 机制重叠，进入观察池；生成式 3D 论文若不从观测恢复场景，不按重建纳入。
- Representation World Model 主要在通用连续控制与隐表示规划验证，视觉机制证据不够明确；不纳入方向三。
- ReVNM 提供远端相机 exo-to-ego 深度导航，但仅作者声明投稿 ICRA 2027，且本轮已有更强的真实火星导航与主动视觉信号，进入观察池。
- Online Sim-to-Real Adaptation via Closed-Loop System Modeling 以动力学/控制适配为核心，无视觉机制；按边界排除。
- lunar excavator bucket、free-floating manipulator 等偏机构/纯动力学论文按方向三边界排除。
- Digital Twin-Driven VR Teleoperation 面向手术远程操作，虽含数字孪生与多视空间感知，但对本轮行星/通用仿真问题迁移较间接，进入观察池。

## 下一轮核验

- OceanXL 的 ACM/SIGGRAPH Asia 正式页面、DOI 与代码/数据许可证；
- COSA-GS 在 x86/ARM/GPU 的 bit-exact 与真实解码时延；
- Mars 2020 数据集、视频和代码是否按作者声明公开，以及 sol/地点拆分是否避免泄漏；
- X2Real 的真实硬件协议、仿真—真实相关置信区间与训练测试隔离实现；
- NASA NTRS、JPL、ESA 和出版社端新增的轮壤、低重力、传感器物理与持续同步数字孪生记录。
