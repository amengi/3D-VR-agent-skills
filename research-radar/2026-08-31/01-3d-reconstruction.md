# 方向一：三维重建——从多视几何到视觉几何基础模型

> 更新日：2026-09-01；近两年窗口：2024-09-01—2026-08-31。

本章只讨论三维重建本身，不以行星或机器人应用作为入选条件。核心问题是：如何从图像、视频或多模态观测中恢复相机、几何、外观与动态，并给出可验证的尺度、完整性和不确定性。

## 1. 学科主线

```text
解析多视几何 → 特征与全局优化 → 实时稠密重建 → 学习式深度/MVS
     → 神经辐射场与 3DGS → 点图/视觉几何基础模型 → 流式、动态、可靠与高效重建
```

三维重建的长期张力是：**几何正确性、外观逼真度、全局一致性、计算效率和失败可知性**很难同时最大化。近年的模型变化很大，但相机模型、重投影、bundle adjustment 和多视一致性仍是判断结果是否可信的底层语言。

## 2. 代表性经典论文与发展脉络

| 阶段 | 代表工作 | 历史作用 | 尚未解决的问题 |
|---|---|---|---|
| 两视几何（1981） | [A Computer Algorithm for Reconstructing a Scene from Two Projections](https://doi.org/10.1038/293133a0) | 用极几何从对应点恢复相机相对运动与三维结构 | 退化构型、错误匹配、尺度与非刚体场景 |
| 多帧因子分解（1992） | [Shape and Motion from Image Streams under Orthography](https://doi.org/10.1007/BF00129684) | 以低秩分解联合恢复形状与运动，奠定多帧整体估计思路 | 透视、遮挡、缺失轨迹和非刚体 |
| 稳健局部特征（2004） | [Distinctive Image Features from Scale-Invariant Keypoints](https://doi.org/10.1023/B:VISI.0000029664.99615.94) | SIFT 使宽基线匹配与大规模 SfM 更可靠 | 重复/弱纹理、强光照变化和可学习域偏差 |
| 互联网级 SfM（2006） | [Photo Tourism](https://doi.org/10.1145/1141911.1141964) | 把特征匹配、增量式 SfM 和 bundle adjustment 组织成大规模系统 | 计算增长、顺序依赖、错误回环和稠密度 |
| 稠密多视立体（2010） | [Accurate, Dense, and Robust Multiview Stereopsis](https://doi.org/10.1109/TPAMI.2009.161)（PMVS） | 建立从稀疏相机到稠密 patch 扩展与过滤的经典 MVS 路线 | 反光、无纹理、薄结构和遮挡边界 |
| 实时 RGB-D / 单目稠密（2011） | [KinectFusion](https://doi.org/10.1109/ISMAR.2011.6092378)；[DTAM](https://doi.org/10.1109/ICCV.2011.6126513) | 展示相机跟踪与稠密地图可实时联合运行 | 大场景、漂移、动态与传感器依赖 |
| 学习式 MVS（2018） | [MVSNet](https://doi.org/10.1007/978-3-030-01237-3_20) | 以可微单应变换和 3D cost volume 学习多视深度 | 内存随深度/分辨率增长，跨域和置信校准困难 |
| 神经场（2020） | [NeRF](https://doi.org/10.1007/978-3-030-58452-8_24) | 以可微体渲染优化连续辐射场，重塑新视角合成与隐式场研究 | 训练慢，几何不一定 metric 或表面准确，动态处理复杂 |
| 显式可微渲染（2023） | [3D Gaussian Splatting](https://doi.org/10.1145/3592433) | 用可微 Gaussian 显式基元取得实时、高质量渲染 | densification、内存、几何表面和动态一致性 |
| 无相机先验点图（2024，窗口前锚点） | [DUSt3R](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html) | 将匹配、深度和相机关系统一成两图 pointmap 预测 | 多图仍需对齐优化，尺度/内参与失败检测仍不稳 |

### 脉络判断

发展不是“深度模型取代几何”，而是几何约束从显式求解器迁移到训练数据、损失、网络表示和测试时校验中。当前最有价值的问题是明确哪些约束可被模型吸收，哪些必须保留为优化器、验证器或安全回退。

## 3. 近两年顶会顶刊代表作

| 主线 | 代表论文 | Venue / 年份 | 贡献位置 | 主要边界 |
|---|---|---|---|---|
| 两图通用几何 | [MASt3R](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9080_ECCV_2024_paper.php) | ECCV 2024 | 在共同三维坐标中学习 pointmap 与局部描述子，增强 DUSt3R 的稠密匹配与下游几何能力 | 两图为基本单元，多图仍有对齐与累计误差 |
| 统一几何基础模型 | [VGGT](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) | CVPR 2025 Best Paper | 单次前馈统一预测相机、深度、pointmap 和 point track，把多项几何任务收敛到共享 backbone | 大模型/全局注意力开销高；域外错误和 metric 可靠性需独立检查 |
| 千图前馈重建 | [Fast3R](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_Pass_CVPR_2025_paper.html) | CVPR 2025 | 将联合前馈重建扩展到 1000+ 图像，正面处理可扩展性 | 大图集合中的全局一致、显存和异常视图仍是难点 |
| 学习先验 + SLAM | [MASt3R-SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Murai_MASt3R-SLAM_Real-Time_Dense_SLAM_with_3D_Reconstruction_Priors_CVPR_2025_paper.html) | CVPR 2025 | 把学习 pointmap 放入跟踪、回环与二阶全局优化的完整系统 | 先验可能高置信出错；长期动态与嵌入式资源仍受限 |
| 在线单目稠密 | [SLAM3R](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SLAM3R_Real-Time_Dense_Scene_Reconstruction_from_Monocular_RGB_Videos_CVPR_2025_paper.html) | CVPR 2025 | 以局部重建和 learned local-to-world registration 处理流式视频 | 局部错误可能传播到持久地图；回环边界需细看 |
| 几何—辐射统一地图 | [PINGS](https://www.roboticsproceedings.org/rss21/p040.html) | RSS 2025 | 在共享神经点上联合 SDF 与 3DGS，使表面、渲染和里程计相互约束 | 在线辐射更新昂贵，显式动态建模不足 |
| 动态 3DGS-SLAM | [WildGS-SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_WildGS-SLAM_Monocular_Gaussian_Splatting_SLAM_in_Dynamic_Environments_CVPR_2025_paper.html) | CVPR 2025 | 用不确定性与动态过滤增强单目 Gaussian SLAM | 动静分解错误和长期对象状态仍会污染地图 |
| 线性扩展的全局表示 | [VGG-T³](https://openaccess.thecvf.com/content/CVPR2026/html/Elflein_VGG-T3_Offline_Feed-Forward_3D_Reconstruction_at_Scale_CVPR_2026_paper.html) | CVPR 2026 | 以 test-time training 将可变长 KV 场景表示蒸馏为固定大小 MLP；官方摘要报告 1k 图 54 秒 | test-time training 带来新的优化稳定性与场景特异成本 |
| 多模态几何输入 | [OmniVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_OmniVGGT_Omni-Modality_Driven_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html) | CVPR 2026 | 允许深度、相机等任意可用几何模态条件化基础模型 | 缺失/冲突传感器的置信融合和标定误差值得单独测试 |
| 高效部署 | [LiteVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_LiteVGGT_Boosting_Vanilla_VGGT_via_Geometry-aware_Cached_Token_Merging_CVPR_2026_paper.html)；[QVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_QVGGT_Post-Training_Quantized_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html)；[FlashVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlashVGGT_Efficient_and_Scalable_Visual_Geometry_Transformers_with_Compressed_Descriptor_CVPR_2026_paper.html) | CVPR 2026 | 分别从 token 合并/缓存、混合精度量化、压缩描述子处理效率 | 平均误差可能掩盖薄结构、小障碍和高曲率尾部损失 |

### 近两年真正发生的变化

1. **任务专用网络 → 共享视觉几何模型**：相机、深度、pointmap、track 开始由同一表示联合预测。
2. **成对预测 → 多图联合与持久状态**：Fast3R、SLAM3R、VGG-T³ 分别探索批量、在线与 test-time scene memory。
3. **纯外观地图 → 多场一致地图**：PINGS 和 3DGS-SLAM 路线开始要求表面、外观、运动与位姿彼此一致。
4. **SOTA 精度 → 可靠性和部署**：压缩、异常视图、动态过滤与资源上限成为正式研究变量。

## 4. 重点论文简要 Reading

### 4.1 VGGT：统一前馈视觉几何

- **WHY**：传统 pipeline 针对相机、深度、匹配分别设计模块，多图又需要昂贵后处理。
- **HOW**：用标准大 Transformer 在帧内与全局注意力间交替，从一到数百幅图像统一输出相机参数、深度、pointmap 和 point track。
- **WHAT**：CVPR 官方论文显示其无需任务专用几何结构也能在多项任务上强于 DUSt3R/MASt3R 路线；并获 2025 Best Paper。
- **读后判断**：贡献是统一接口和数据规模，不是证明 bundle adjustment 或几何验证已无必要。
- **应补实验**：构造无重叠、重复纹理、内参漂移、动态、模糊和异常视图，测 failure AUROC 与灾难性误差，而非只测均值。

### 4.2 MASt3R-SLAM：基础模型进入完整系统

- **WHY**：两图 pointmap 很强，但机器人/视频系统还需要持续跟踪、关键帧、回环和全局一致。
- **HOW**：以 MASt3R 几何先验作为前端，加入快速匹配、局部融合、图构建和二阶全局优化。
- **WHAT**：它说明学习几何先验与经典 SLAM 后端可以形成互补系统。
- **读后判断**：这是研究“模型应替代哪一层、又应被哪一层检查”的优先基线。
- **应补实验**：统一比较纯学习、纯几何和混合系统在域外错误、恢复时间、算力和置信覆盖率上的 Pareto。

### 4.3 PINGS：一张地图服务不同物理含义

- **WHY**：radiance field 擅长渲染，SDF 擅长表面；分开维护会浪费观测并产生地图冲突。
- **HOW**：共享弹性神经点承载 SDF 与 3DGS，两种场以几何一致性相互约束。
- **WHAT**：论文在大尺度 LiDAR-视觉数据上联合评价渲染、表面、里程计和内存。
- **读后判断**：共享锚点是强设计，但共享并不自动保证正迁移；不同场的更新频率与冲突应成为显式研究对象。
- **应补实验**：按静态/动态、纹理/几何、近场/远场分桶，测两个场何时互相帮助、何时负迁移。

### 4.4 VGG-T³：场景记忆也可以 test-time 学习

- **WHY**：全局 attention 的时间和内存随图像数二次增长，限制大场景前馈重建。
- **HOW**：把可变长 KV 场景表示在测试时蒸馏成固定大小 MLP，使处理随视图数近似线性扩展。
- **WHAT**：官方页面报告 1k 图重建 54 秒及相对 softmax-attention 基线的 11.6× 加速，同时保留全局聚合和未见图像定位能力。
- **读后判断**：这把“优化”从几何变量转移到场景记忆参数，值得与传统 BA、submap 和 recurrent state 做同预算比较。
- **应补实验**：测 test-time 优化对输入顺序、异常图像、场景重复结构和增量追加图像的稳定性。

## 5. 未来值得研究的独立方向

### G1. 显式失败验证与可校准重建

**假设**：将重投影、多视循环一致性和 conformal calibration 接到基础模型输出，可在小幅牺牲覆盖率时显著降低灾难性几何失败。

- 最小实验：六类可控退化 + 真实域外集合。
- 指标：failure AUROC、risk-coverage、p95/p99 几何误差、自动回退成功率。
- 证伪：置信度不能跨数据集保持覆盖，或验证器只复现模型训练偏差。

### G2. 固定内存的流式视觉几何基础模型

**假设**：结构化 scene memory + 局部更新 + 显式回环，比简单窗口化注意力更能保持长序列全局一致且内存有界。

- 对照：SLAM3R、VGG-T³、submap SLAM、recurrent memory。
- 指标：每公里漂移、闭环前后表面一致性、内存增长率、历史查询精度、错误写入恢复时间。

### G3. 几何—外观—动态的可分离共享表示

**假设**：共享空间锚点但为表面、radiance 和 motion 使用不同时间尺度与不确定性，可减少动态污染又保留跨场互助。

- 关键消融：完全共享、完全分离、共享锚点/独立 head、对象级 motion field。
- 证伪：共享结构在动态比例升高时持续负迁移，或计算成本超过独立地图。

### G4. 风险保持的模型压缩

**假设**：按几何曲率、可见性与任务风险分配 token/位宽，能在相同算力下更好保留薄结构和小物体。

- 指标：薄结构 F-score、边界完整率、p99 深度误差、功耗、延迟。
- 警示：不能只用纹理显著性做代理，因为危险几何可能低纹理。

### G5. 主动采集与重建联合设计

**假设**：直接优化“下一观测对几何歧义的期望消除量”，比最大覆盖率或渲染不确定性更高效。

- 最小场景：遮挡严重的室内/工业对象或大型室外结构。
- 指标：单位路径/帧数的表面完整度、尺度误差、不确定性下降及采集安全成本。

### G6. 可编辑、可更新的长期三维表示

**假设**：把持久结构、周期变化、瞬态对象和观测证据分层存储，可避免重建系统在长期运行中把变化误当噪声或把旧状态永久遗忘。

- 评价：跨天/月更新、版本查询、变化检测 precision/recall、地图回滚和存储增长率。

## 6. 推荐阅读顺序

1. Longuet-Higgins、Tomasi–Kanade、SIFT：理解相机几何、低秩结构与匹配。
2. Photo Tourism、PMVS、KinectFusion/DTAM：理解经典系统怎样把稀疏、稠密和实时连接起来。
3. MVSNet、NeRF、3DGS：理解学习深度、隐式场和显式可微渲染三次表示转向。
4. DUSt3R、MASt3R、VGGT：理解 pointmap 与几何基础模型。
5. MASt3R-SLAM、PINGS、VGG-T³：理解系统化、多场一致和可扩展场景记忆。
6. OmniVGGT 与 Lite/Q/FlashVGGT：理解多模态输入及部署问题。

## 7. 选题警示

- 新视角合成好看不等于 metric reconstruction 准确；PSNR/SSIM/LPIPS 不能替代表面、相机和尺度指标。
- 平均误差不能代表可靠性；必须报告尾部、失败检测和异常输入。
- 在单个静态数据集上提高一点精度，很难支撑“基础模型”或“通用重建”的结论。
