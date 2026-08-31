# 可复现检索日志

## 协议

- 检索日期：2026-08-31
- 主窗口：2024-08-31 至 2026-08-31
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

### 机器人独立补检

```text
site:roboticsproceedings.org/rss21 robot navigation planning control learning world model terrain
site:openaccess.thecvf.com/content/CVPR2025 robot navigation world models
site:roboticsproceedings.org/rss21 sim-to-real generalist policy spatial VLA task motion planning
```

定向官方站点查询覆盖 CVF 2025/2026、RSS 2024/2025、Wiley Journal of Field Robotics、Elsevier/DOI、IEEE 记录和 arXiv。

## 来源路由与实际覆盖

1. **T1 尝试**：`nature-academic-search` 的学术 MCP 未挂载。
2. **T1 后备脚本尝试**：OpenAlex 脚本首次在沙箱内发生 DNS 失败；获得网络权限后再次运行，因本地 CA 证书验证失败。连续两次失败后停止该路径。
3. **官方页面核验**：CVF Open Access、RSS proceedings、Wiley、DOI/出版社页面、DLR publication record。
4. **预印本补充**：arXiv 用于读取公开全文或确认 emerging/已发表工作的预印本版本。
5. **广域搜索**：只用于发现候选，纳入目录前回到官方或稳定记录核验。

## 纳入与排除

纳入：

- 直接使用月球/火星数据、仿真或任务约束；
- 将三维表示与定位、导航、控制或 sim-to-real 连接；
- 能明确迁移到行星约束的 CVPR/ICCV/RSS 等方法；
- 有官方会议、出版社、DOI 或明确预印本记录。

排除/降级：

- 只有营销页面或无法确认题录；
- 仅因标题含 digital twin/robot 而与三维、仿真或行星约束无实质关系；
- 把 arXiv 默认为同行评议；
- 仅有平均视觉质量提升、无法提出具体行星验证路径的泛 3D 论文。

## 已知覆盖偏差

- 顶会方法偏重 CVPR/RSS，工程期刊与任务档案仍需扩展。
- 月球材料多于火星，尤其缺少近两年的火星真实任务闭环研究。
- 公开英文资源占主导，中文任务论文与学位论文尚未系统检索。
- 2026 年论文较新，引用数不稳定，因此本轮不使用引用数排序。
- `paper-catalog.json` 只有年份字段；精确窗口判断在报告层完成，near-window 论文单列。

## 下一轮建议查询

```text
site:ieeexplore.ieee.org 2025 2026 Perseverance autonomous navigation reconstruction
site:agupubs.onlinelibrary.wiley.com Mars rover photogrammetry terrain reconstruction 2025
月面 三维重建 数字孪生 轮壤 自主导航 2025 2026
嫦娥 月球车 多源 三维 重建 地形 仿真
```

下一轮应优先补充：NASA/JPL 任务技术论文、嫦娥任务中文/英文记录、IROS/ICRA 2025–2026 官方 proceedings，以及公开代码/数据可用性核验。
