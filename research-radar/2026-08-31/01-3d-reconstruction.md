# 方向一：三维重建

本文件先把三维重建作为独立研究领域分析，不要求论文同时涉及行星或机器人。窗口为 2024-08-31 至 2026-08-31；重点来源为 CVPR、ICCV、ECCV、RSS。

## 近两年技术主线

### 1. 从成对几何到视觉几何基础模型

- [MASt3R](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9080_ECCV_2024_paper.php) 将图像匹配落到共同三维坐标中的点图。
- [VGGT](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) 在一个前馈模型中统一相机、深度、点图与点轨迹，是 2025 CVPR Best Paper。
- [Fast3R](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_Pass_CVPR_2025_paper.html) 将多图联合重建扩展到千图规模。
- [SLAM3R](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SLAM3R_Real-Time_Dense_Scene_Reconstruction_from_Monocular_RGB_Videos_CVPR_2025_paper.html) 采用局部重建 + learned local-to-world 对齐做在线稠密重建。
- [OmniVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_OmniVGGT_Omni-Modality_Driven_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html) 将深度和相机参数等任意可用几何模态注入 VGGT。

**判断**：研究中心正在从“为每个子任务设计网络”转向“共享三维表示 + 多任务 head + 少量几何后处理”。但经典多视几何没有消失，而是转化为稀疏约束、验证器和安全后端。

### 2. 学习先验与经典优化的重新组合

- [MASt3R-SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Murai_MASt3R-SLAM_Real-Time_Dense_SLAM_with_3D_Reconstruction_Priors_CVPR_2025_paper.html) 用学习点图做前端，同时保留跟踪、回环和全局优化。
- [Murre](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Multi-view_Reconstruction_via_SfM-guided_Monocular_Depth_Estimation_CVPR_2025_paper.html) 用稀疏 SfM 点引导扩散式单目深度，绕开脆弱的稠密匹配。
- [G3R](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/992_ECCV_2024_paper.php) 让网络读取可微渲染梯度，迭代修正场景表示，介于一次前馈和逐场景优化之间。

**判断**：值得探索的不是“学习还是几何”二选一，而是哪些约束应当进入训练、测试时优化、异常拒绝或全局图优化。

### 3. 地图表示从单一外观走向多场一致

- [Gaussian Splatting SLAM](https://openaccess.thecvf.com/content/CVPR2024/html/Matsuki_Gaussian_Splatting_SLAM_CVPR_2024_paper.html)、[SplaTAM](https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html) 与 [Photo-SLAM](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Photo-SLAM_Real-time_Simultaneous_Localization_and_Photorealistic_Mapping_for_Monocular_Stereo_CVPR_2024_paper.html) 建立在线 3DGS 地图路线。
- [PINGS](https://www.roboticsproceedings.org/rss21/p040.html) 在共享神经点上联合 SDF 与 3DGS，同时服务表面和渲染。
- [WildGS-SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_WildGS-SLAM_Monocular_Gaussian_Splatting_SLAM_in_Dynamic_Environments_CVPR_2025_paper.html) 用不确定性过滤动态干扰。

**判断**：3DGS 的下一阶段不是只提高 PSNR，而是与 metric surface、semantic/instance、动态和不确定性保持一致。

### 4. 长序列、低算力与异常输入

- [LiteVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_LiteVGGT_Boosting_Vanilla_VGGT_via_Geometry-aware_Cached_Token_Merging_CVPR_2026_paper.html)：几何感知 token 合并与跨层缓存。
- [QVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_QVGGT_Post-Training_Quantized_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html)：敏感度驱动的后训练混合精度量化。
- [FlashVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlashVGGT_Efficient_and_Scalable_Visual_Geometry_Transformers_with_Compressed_Descriptor_CVPR_2026_paper.html)：压缩帧描述子与递归注意力。
- [Emergent Outlier View Rejection](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Emergent_Outlier_View_Rejection_in_Visual_Geometry_Grounded_Transformers_CVPR_2026_paper.html)：从 VGGT 内部层提取无需再训练的异常视图分离能力。

## 独立值得探索的研究点

### R1. Learned reconstruction with explicit failure verification

为 VGGT/MASt3R 类模型增加显式的几何一致性检验、异常视图拒绝和失败类型输出。重点不是再做一个平均误差更低的 backbone，而是回答：模型在何时不可信、能否自动回退到 SfM/MVS 或局部优化。

- 最小实验：人为控制无重叠视图、运动模糊、重复纹理、曝光、内参漂移和动态比例。
- 指标：平均几何误差之外增加 failure AUROC、置信覆盖率、灾难性失败率和恢复成本。
- 风险：`low-risk`。

### R2. Streaming 3D foundation model with persistent state

把批量多视模型改造成固定内存的持续状态模型，同时显式处理回环、遗忘和地图版本冲突。

- 基线：MASt3R-SLAM、SLAM3R、Fast3R、FlashVGGT、传统 submap SLAM。
- 关键指标：每公里漂移、回环后表面一致性、内存随序列长度增长率、状态灾难性遗忘。
- 风险：`medium-risk`。

### R3. Unified geometry–radiance–dynamic representation

在 PINGS 的 SDF+3DGS 基础上加入对象/运动场，使几何、外观和动态使用共享锚点但允许不同时间尺度更新。

- 关键问题：静态表面与动态外观如何解耦；跨场约束何时互相帮助、何时产生负迁移。
- 风险：`high-risk/high-upside`。

### R4. Risk-preserving model compression

现有压缩方法优化平均几何误差；新的方向是保护薄结构、小障碍和高曲率区域，按几何/任务风险分配 token 与位宽。

- 最小实验：构造相同平均深度误差但尾部结构不同的测试集。
- 指标：薄结构 F-score、最小障碍召回、p95/p99 深度误差、功耗与延迟。
- 风险：`low-to-medium-risk`。

## 推荐精读顺序

1. VGGT：理解统一三维基础模型的任务定义与能力边界。
2. MASt3R-SLAM：观察学习几何先验如何进入完整 SLAM 系统。
3. PINGS：理解多场统一地图及其明确计算瓶颈。
4. LiteVGGT/QVGGT/FlashVGGT：比较三种不同的效率路径。
5. Murre 与 G3R：理解经典约束、扩散先验和测试时迭代的重新组合。
