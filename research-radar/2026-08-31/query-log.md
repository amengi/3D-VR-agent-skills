# 可复现检索日志

## 协议

- 检索日期：2026-08-31；重构补检：2026-09-01
- 主窗口：2024-09-01 至 2026-08-31
- 语言：英语为主；中文任务词用于后续扩展，本轮未对 CNKI/万方作系统覆盖
- 输出模式：发现 + 排序 + gap analysis + brief reading
- 组织方式：三个方向先独立检索和筛选，再进行两两交叉及三方向闭环综合
- 去重：优先规范化 DOI；无 DOI 时使用规范化标题 + 第一作者；出版版本优先于预印本

## 查询族

### 行星重建

```text
(lunar OR moon OR martian OR mars OR planetary) AND
(3D reconstruction OR stereo OR neural rendering OR Gaussian splatting OR radiance field OR DEM)
```

补充查询：

```text
planetary descent wide-angle neural 3D reconstruction
lunar rover landmark NeRF odometry correction map pruning
Mars rover multisensor high-resolution continuous 3D model
```

### 物理与传感仿真

```text
(lunar OR martian OR regolith) AND
(digital twin OR terramechanics OR deformable terrain OR sensor simulation OR Hapke OR ray tracing)
```

补充查询：

```text
lunar rover SPH CRM gravity offset wheel soil interaction
physics-based sensor simulation lunar ground operations Chrono dust
```

### 机器人自主性

```text
(planetary rover OR off-road robot) AND
(SLAM OR localization OR traversability OR active mapping OR navigation OR manipulation)
```

### 可迁移方法

```text
(visual geometry transformer OR 3D reconstruction prior OR Gaussian SLAM OR neural map) AND robot
(real-to-sim-to-real OR online dynamics adaptation OR multiphysics benchmark) AND robot
```

### 三维重建独立补检

```text
site:openaccess.thecvf.com/content/CVPR2025 3D reconstruction multi-view pointmap foundation model
site:openaccess.thecvf.com/content/CVPR2026 visual geometry transformer efficiency outlier reconstruction
site:ecva.net/papers/eccv_2024 generalizable reconstruction neural rendering
```

### 仿真/数字孪生独立补检

```text
site:roboticsproceedings.org/rss21 simulation platform digital twin robot 2025
lunar rover deformable terrain elastic wheel simulation 2025 2026
low-gravity granular scaling law wheel mobility slope
```

### 机器人视觉与具身视觉补检

```text
site:openaccess.thecvf.com/content/CVPR2025 robot perception 3D manipulation visual navigation world model
site:openaccess.thecvf.com/content/ICCV2025 embodied world model 4D robot vision
site:roboticsproceedings.org/rss21 visual perception navigation active mapping spatial VLA manipulation
site:2024.corl.org embodied Gaussian splatting robot visual imitation
site:roboticsconference.org/program/papers 2026 perception vision mapping manipulation world model
```

### 2026-09-01 发展脉络重构补检

```text
3D reconstruction milestones two-view geometry factorization SfM MVS KinectFusion NeRF Gaussian Splatting
robotics milestones A* impedance control subsumption RRT Monte Carlo localization robot learning
robot simulation milestones Gazebo MuJoCo CARLA Habitat Isaac Gym planetary rover terramechanics
site:roboticsconference.org 2026 awards accepted papers robotics
site:2026.ieee-icra.org awards robot learning perception automation
site:openaccess.thecvf.com/content/CVPR2026 3D reconstruction VGGT
2025 2026 lunar rover simulation digital twin terramechanics Journal of Field Robotics
```

其中 `robotics milestones ...` 属于上一版“机器人学本体”宽口径查询。本次根据用户澄清将方向三收窄为计算机视觉主导，A*、阻抗控制、RRT、执行器和纯动力学工作不再纳入方向三核心文献。

定向官方站点查询覆盖 CVF 2024–2026、ECCV 2024、RSS 2023–2026、ICRA 2024/2026、Wiley Journal of Field Robotics、Elsevier/DOI、IEEE、NASA NTRS、PMLR/JMLR 和 arXiv。

## 来源路由与实际覆盖

1. **T1 尝试**：`nature-academic-search` 的学术 MCP 未挂载。
2. **T1 后备脚本尝试**：OpenAlex 脚本首次在沙箱内发生 DNS 失败；获得网络权限后再次运行，因本地 CA 证书验证失败。连续两次失败后停止该路径。
3. **官方页面核验**：CVF Open Access、RSS proceedings、Wiley、DOI/出版社页面、DLR publication record。
4. **预印本补充**：arXiv 用于读取公开全文或确认 emerging/已发表工作的预印本版本。
5. **广域搜索**：只用于发现候选，纳入目录前回到官方或稳定记录核验。

## 纳入与排除

纳入：

- 对三个方向分别建立了学科范式或能解释当前路线来源的经典工作；
- 近两年在 CVPR/ICCV/ECCV、RSS/ICRA 或领域代表期刊发表且具有明确方法/系统代表性的工作；
- 仿真方向额外纳入直接使用月球/火星环境、轮壤、低重力或任务数字孪生的领域论文；
- 方向三要求核心贡献落在视觉表示、视觉感知/理解、视觉定位建图、主动视觉、视觉导航、视觉操作或视觉世界模型，并有机器人任务验证；
- 有官方会议、出版社、DOI 或明确预印本记录。

排除/降级：

- 只有营销页面或无法确认题录；
- 仅因标题含 digital twin/robot/3D 而没有清晰问题、方法或验证贡献；
- 把 arXiv 默认为同行评议；
- 只因能与另外两个方向交叉而入选、但在本方向本身缺乏代表性的论文；
- 纯机器人机构、材料、驱动器、控制、动力学辨识或不含视觉机制的一般 RL；
- 仅有平均指标提升、没有方法机制或可靠性信息的增量工作。

## 已知覆盖偏差

- 顶会方法仍偏重 CVPR/RSS，TPAMI/IJCV/TRO/IJRR/RA-L 和 ICRA/IROS 的近两年系统覆盖仍需扩展。
- 月球材料多于火星，尤其缺少近两年的火星真实任务闭环研究。
- 公开英文资源占主导，中文任务论文与学位论文尚未系统检索。
- 2026 年论文较新，引用数不稳定，因此本轮不使用引用数排序。
- `paper-catalog.json` 仍是上一版行星交叉雷达的机器可读目录，尚未扩展为本次三条独立发展线的完整经典/近期目录；精确窗口判断以三篇方向文档为准。

## 下一轮建议查询

```text
site:ieeexplore.ieee.org 2025 2026 Perseverance autonomous navigation reconstruction
site:agupubs.onlinelibrary.wiley.com Mars rover photogrammetry terrain reconstruction 2025
月面 三维重建 数字孪生 轮壤 自主导航 2025 2026
嫦娥 月球车 多源 三维 重建 地形 仿真
```

下一轮应优先补充：NASA/JPL 任务技术论文、嫦娥任务中文/英文记录、IROS/ICRA 2025–2026 官方 proceedings，以及公开代码/数据可用性核验。
