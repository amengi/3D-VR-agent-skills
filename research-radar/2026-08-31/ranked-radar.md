# 排序论文雷达

> 本文件是跨方向统一评分索引。三个方向的独立技术脉络与研究点请分别阅读 [三维重建](01-3d-reconstruction.md)、[仿真与数字孪生](02-simulation-digital-twins.md)、[机器人](03-robotics.md)；交叉机会单列在 [04-cross-track-opportunities.md](04-cross-track-opportunities.md)。

评分采用 skill 的六维量表：主题匹配 35、方法价值 20、来源质量 15、跨方向桥接 10、应用价值 10、长期价值 10。`A/core` 为 80–100，`B/bridge` 为 65–79。分数用于研究优先级，不等同于论文质量或引用影响力。

## A. 行星直接相关

| 分数 | 论文 | 年份/来源 | 状态 | 为什么值得看 |
|---:|---|---|---|---|
| 93 | [StereoLunar](https://openaccess.thecvf.com/content/ICCV2025W/3D-VAST/html/Grethen_Adapting_Stereo_Vision_From_Objects_To_3D_Lunar_Surface_Reconstruction_ICCVW_2025_paper.html) | 2025 ICCV Workshop | workshop peer-reviewed | 物理渲染月球南极数据 + MASt3R 微调，直接证明通用模型需要行星域适配 |
| 91 | [A Physics-Based Sensor Simulation Environment for Lunar Ground Operations](https://doi.org/10.1109/AERO63441.2025.11068496) | 2025 IEEE Aerospace | peer-reviewed | 把 Hapke 光度、光线追踪、尘埃和可变形地形动力学放入同一仿真链 |
| 91 | [Landmark-aware autonomous odometry correction and map pruning for planetary rovers](https://doi.org/10.1016/j.actaastro.2024.10.025) | 2025 Acta Astronautica | peer-reviewed | 用 NeRF 地标做漂移修正和地图裁剪，连接神经渲染与长期定位 |
| 90 | [CLVSim](https://onlinelibrary.wiley.com/doi/10.1002/rob.22421) | 2025 Journal of Field Robotics | peer-reviewed | SPH 软土、悬架、轮、电机和驾驶员的系统级月球车仿真与分系统验证 |
| 89 | [Neural 3D Reconstruction of Planetary Surfaces from Descent-Phase Wide-Angle Imagery](https://openaccess.thecvf.com/content/CVPR2026W/AI4Space/html/de_Almeida_Neural_3D_Reconstruction_of_Planetary_Surfaces_from_Descent-Phase_Wide-Angle_Imagery_CVPRW_2026_paper.html) | 2026 CVPR Workshop | workshop peer-reviewed | 用神经高度场处理广角畸变、弱视差和近天底下降轨迹 |
| 87 | [A Study Demonstrating That Using Gravitational Offset…Is Misleading](https://onlinelibrary.wiley.com/doi/10.1002/rob.22597) | 2025 Journal of Field Robotics | peer-reviewed | 指出只做重力补偿不能代表低重力轮壤相互作用，迫使验证设计更诚实 |
| 84 | [High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909) | 2026 IEEE CAI | peer-reviewed；链接为预印本 | ROS2/rosbag、COLMAP、NeRF/3DGS 的工程基线，适合作为可复现实验起点 |
| 82 | [Passivity-Based Tracking Control of a Planetary Rover With Robotic Arm](https://elib.dlr.de/225596/) | 2026 IEEE T-FR | peer-reviewed | 为“地图/地形估计最终如何进入移动操作控制”提供终端任务 |

## B. 可迁移的顶会核心方法

| 分数 | 论文 | 年份/来源 | 状态 | 行星迁移价值 |
|---:|---|---|---|---|
| 93 | [PINGS](https://www.roboticsproceedings.org/rss21/p040.html) | 2025 RSS | peer-reviewed | 一个点式隐式地图同时承载 SDF 几何和 3DGS 辐射场，适合加入地形物理层 |
| 93 | [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](https://www.roboticsproceedings.org/rss21/p007.html) | 2025 RSS | peer-reviewed | 把里程计误差转成局部安全区收缩，避免“地图漂亮但规划不安全” |
| 91 | [MASt3R-SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Murai_MASt3R-SLAM_Real-Time_Dense_SLAM_with_3D_Reconstruction_Priors_CVPR_2025_paper.html) | 2025 CVPR | peer-reviewed | 学习型点图先验 + 实时跟踪/回环/全局优化，是月面 SLAM 的强基线 |
| 90 | [Verti-Bench](https://www.roboticsproceedings.org/rss21/p138.html) | 2025 RSS | peer-reviewed | 交互式、多物理、刚性/可变形地形 benchmark，可改造成月球移动性基准 |
| 89 | [GauSS-MI](https://www.roboticsproceedings.org/rss21/p030.html) | 2025 RSS | peer-reviewed | 3DGS 不确定性和互信息驱动 next-best-view，可扩展到安全/能耗/科学收益 |
| 88 | [VGGT](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) | 2025 CVPR Best Paper | peer-reviewed | 单模型输出相机、深度、点图和轨迹，是行星多任务几何 backbone 候选 |
| 88 | [Learned Perceptive Forward Dynamics Model](https://www.roboticsproceedings.org/rss21/p001.html) | 2025 RSS | peer-reviewed | 从几何 + 本体感受预测失败风险，启发视觉地形与轮壤响应联合规划 |
| 88 | [Meta-Learning Online Dynamics Model Adaptation](https://www.roboticsproceedings.org/rss21/p139.html) | 2025 RSS | peer-reviewed | 在线更新未知地形动力学，可用于稀疏安全探索中的月壤参数适配 |
| 87 | [OmniVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_OmniVGGT_Omni-Modality_Driven_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html) | 2026 CVPR | peer-reviewed | 可随机接收 RGB、深度、内外参等模态，贴合行星多传感器间歇可用情形 |
| 86 | [SLAM3R](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SLAM3R_Real-Time_Dense_Scene_Reconstruction_from_Monocular_RGB_Videos_CVPR_2025_paper.html) | 2025 CVPR | peer-reviewed | 前馈式在线稠密重建速度高，但定位与全局一致性需要额外安全后端 |
| 84 | [LiteVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_LiteVGGT_Boosting_Vanilla_VGGT_via_Geometry-aware_Cached_Token_Merging_CVPR_2026_paper.html) | 2026 CVPR | peer-reviewed | 几何感知 token 合并与缓存，适合长序列/低算力，但须保护小障碍物 |
| 83 | [QVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_QVGGT_Post-Training_Quantized_Visual_Geometry_Grounded_Transformer_CVPR_2026_paper.html) | 2026 CVPR | peer-reviewed | 后训练混合精度量化为 onboard 部署提供可直接验证的压缩路线 |
| 81 | [Fast3R](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_Pass_CVPR_2025_paper.html) | 2025 CVPR | peer-reviewed | 千图联合重建适合离线/地面站大批量处理，但不天然适合流式 onboard |
| 79 | [FlashVGGT](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlashVGGT_Efficient_and_Scalable_Visual_Geometry_Transformers_with_Compressed_Descriptor_CVPR_2026_paper.html) | 2026 CVPR | peer-reviewed | 压缩描述子注意力支撑千帧级扩展，是长航程子图后端候选 |

## Near-window 锚点

[CraterGrader](https://www.roboticsproceedings.org/rss20/p018.html)（RSS 2024，98 分）发表于 2024 年 7 月，早于精确窗口约一个多月。它仍被保留，因为它把在线感知、可变形地形地图、能耗优化、无 GPS 定位和铲运控制闭合成完整月面工程系统；这是判断新重建/仿真方法是否真正有任务价值的稀缺基准。

## 分布警告

排序集明显集中在 CVPR/RSS 与 2025–2026 年，且月球多于火星。它适合形成技术路线，但不应当被解释为对行星科学、航天工程期刊或中文任务文献的完整覆盖。
