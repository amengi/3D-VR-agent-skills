# 2026-10-12 可复现检索日志

## 范围与协议

- 检索日：2026-10-12（Asia/Shanghai）
- 主窗口：2024-10-12—2026-10-12
- 相对上一版差量：2026-09-28—2026-10-12；官方 arXiv 最近发布日为 2026-10-09
- 出版类型：官方 proceedings、出版社和 DOI 优先；没有正式记录的预印本标为 `preprint/emerging`
- 去重：先规范化 DOI；无 DOI 时用规范化标题 + 第一作者；与原 85 条已发布目录比较
- 排序：仓库六维 rubric，预印本 `source_quality ≤ 9`；不使用不稳定引用数

## 三个独立查询族

```text
(3D reconstruction OR multi-view geometry OR neural field OR NeRF OR 3DGS
 OR visual geometry foundation model OR dynamic OR 4D OR streaming)
AND (uncertainty OR reliable OR active OR sparse attention OR efficient OR interaction)
```

```text
(lunar OR moon OR martian OR mars OR planetary OR regolith OR low gravity
 OR simulation OR digital twin OR sensor physics OR multi-fidelity)
AND (SLAM OR visual localization OR wheel soil OR dust OR render-to-real
 OR continuous synchronization OR real2sim2real OR validation)
```

```text
(visual SLAM OR RGB-D OR point cloud OR multi-view OR open vocabulary map
 OR pose OR affordance OR active vision OR navigation OR VLN
 OR visual manipulation OR visual imitation OR VLA OR visual world model OR 4D world model)
AND (robot OR embodied OR rover OR manipulation OR assembly)
```

三个查询族先独立筛选；交叉价值只在确定纳入集后分析。

## `nature-academic-search` 路由与故障记录

1. 按 `multi-source-search` 工作流先运行 PubMed/Crossref/arXiv 多源预检；沙箱内三个端点均 DNS 失败。
2. 在获准联网环境重试一次，三个端点均因本机 TLS CA 链校验失败；没有关闭 SSL 验证，也没有绕过证书安全。
3. 依技能规则转用 arXiv 官方 `cs.CV/recent`、`cs.RO/recent`、`cs.GR/recent` 列表及逐篇官方摘要页；再用作者项目页和公开代码仓库核验 artifact/status。
4. 正式会议/期刊没有官方 proceedings、出版社页或 DOI 时，保持 `preprint`；作者声明只写入 venue/证据边界。

## 纳入结果（15）

### 三维重建（5）

- Slot3R — arXiv:2610.12282，2026-10-08；项目页已核验
- ReVar3R — arXiv:2610.07883，2026-10-06
- Matisse — arXiv:2609.38746，2026-09-30；项目页写明代码尚未开放
- VASC — arXiv:2610.01013，2026-10-01；公开仓库已核验
- 4D-HOF — arXiv:2610.08782，2026-10-06

### 仿真与数字孪生（4）

- MarsLab — arXiv:2609.34702，2026-09-28；项目/代码已核验；iSpaRo 2026 为作者声明
- RiCo — arXiv:2610.12333，2026-10-08
- RenderBench — arXiv:2610.08684，2026-10-06
- Digital Twin-Driven Real2Sim2Real — arXiv:2610.08339，2026-10-06
- 低重力、轮壤接触物理和持续在线同步数字孪生高相关差量：**本轮未检出**。

### 机器人视觉与具身视觉（6）

- DepthWorld — arXiv:2610.08780，2026-10-06；项目/代码已核验；CoRL 2026 为作者声明
- Blackout vs. Freeze — arXiv:2609.39145，2026-09-30
- VersaCamVLA — arXiv:2610.12451，2026-10-08；NeurIPS 2026 为作者声明
- Rendering-Free Lookahead — arXiv:2610.11039，2026-10-08；项目页已核验
- World Motion Models — arXiv:2610.01742，2026-10-01；NeurIPS 2026 Spotlight 为作者声明
- AssemblyWorld — arXiv:2609.40353，2026-09-30

## 去重、排除与观察池

- 15 条与原 85 条已发布目录按 URL/arXiv ID、规范化标题 + 第一作者去重，未发现重复；本轮新增均无 publisher DOI。
- HierGF（arXiv:2610.01056）与本轮 sparse-view/基础模型重建机制重叠，且 TMM 2026 仅有作者声明，进入观察池。
- Event-Driven Proactive Assistance（arXiv:2610.08344）含视觉语言事件检测和真实桌面辅助任务，但本轮机器人视觉已有更直接的几何世界模型与安全故障证据，进入观察池。
- GenIA（arXiv:2610.12388）和 DeltaSplat（arXiv:2610.09853）分别提供观测对齐的生成重建与 pose-free 3DGS 迭代 refinement；与本轮重建主线重叠，进入观察池。
- WARP-VLA（arXiv:2610.11508）对 wrist-camera 扰动很有价值，但与更通用的 VersaCamVLA 可变相机集合问题重叠，进入观察池。
- RAGNAROK（arXiv:2610.11531）代表 radar–vision–kinematic–inertial SLAM，但本轮未展开多模态定位深读，进入下一轮观察池。
- Uncertainty-Aware RL-Controlled Adaptive 3D Mapping（arXiv:2610.00188）首版早于差量窗口且以 RL 内存策略为主，不做跨周回填。
- LBA-CBF 等以纯控制/动力学安全为核心、没有视觉机制的论文按方向三边界排除。
- PrimitiveCAD 等生成/建模工作若不从观测恢复场景，不按三维重建纳入。

## 下一轮核验

- ReVar3R 的注册失败率、absolute calibration 与 systematic-bias 探针；Matisse 代码是否正式开放。
- MarsLab 的 iSpaRo 正式记录、许可证、火星传感器/尘埃真实性和可复现 benchmark 脚本。
- DepthWorld 与 World Motion Models 的正式会议记录、checkpoint/数据许可和跨实验室拆分。
- Slot3R 在万帧、回环和动态对象上的 memory growth；VersaCamVLA/RFL 的代码、真实相机动作与故障条件复现。
- NASA NTRS、JPL、ESA 与出版社端的低重力、轮壤、Hapke/尘埃传感器物理及持续同步 digital twin 新记录。
