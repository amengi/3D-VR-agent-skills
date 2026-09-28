# 方向一：三维重建

## 本周新增代表论文

| 论文 | WHY | HOW | WHAT | 脉络位置与证据边界 |
|---|---|---|---|---|
| [EliGSiR](https://arxiv.org/abs/2609.20348) | 闭集 3DGS 长优化不适合持续到来的 RGB-D 与固定算力预算 | 地图引导视图调度、按负载改变监督分辨率、只在重复证据指示缺几何处增长 Gaussian | 作者报告 Replica/TUM/ScanNet++/真实传感器上改善全程地图和最终地图的预算利用 | 从离线 3DGS 到“随时可用”的持续地图；预印本，主要依赖室内 RGB-D |
| [AMB3R-SLAM](https://arxiv.org/abs/2609.19518) | 万帧/公里级单目 SLAM 需要低延迟前端与跨尺度一致性 | 轻量前端配合 local–mid–global 分层后端，并可接入 stereo/RGB-D/LiDAR | 作者报告单张消费级 GPU 上 10k+ 帧、公里轨迹和九数据集跟踪结果 | 从局部在线重建推进到分层全局一致性；预印本，完整算力/内存与动态处理证据待复现 |
| [RawSLAM](https://arxiv.org/abs/2609.20589) | 8-bit tone mapping 在阴影/高光下触发跟踪漂移与建图崩溃 | 直接处理 16-bit 线性 RAW/HDR；对数 Gaussian 颜色、范围压缩损失和结构梯度加权 | 作者报告可移植到多个 Gaussian SLAM，并在困难光照序列消除其跟踪失败 | 将传感器辐射度而非显示图像作为 SLAM 输入；预印本，数据仅 10 个室内序列且代码尚未公开 |
| [SplashSplat](https://arxiv.org/abs/2609.20818) | 飞溅液体近乎无纹理、快速拓扑变化且难跨帧跟踪 | 每帧 mask 融合 SDF，level-set 传输得粗速度场，Lagrangian carriers 解码局部 Gaussians | 提供 20 场景、7 台同步 4K/60fps 相机基准；作者报告优于动态 GS 方法 | 从柔性动态场景扩展到物理受限高速流体；预印本，物理量与真实流场真值有限 |
| [PersistBench](https://arxiv.org/abs/2609.20819) | 像素指标无法判断 4D 模型是否记得离开视野的对象 | 用 360° 视频作 omniscient ground truth，评估对象永久性、运动连续性和外观保持 | 多类 4D 模型仅保持短期一致性，物体离场后显著退化 | 为 4D foundation model 增加对象级记忆审计；预印本，基准不等于新重建方法 |

## 正式状态更新

- [Scal3R](https://eccv.ecva.net/Conferences/2026/AcceptedPapers) 已由作者声明升级为 ECCV 2026 官方 accepted-paper 列表可核验。
- [Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion](https://eccv.ecva.net/Conferences/2026/AcceptedPapers) 同样已由官方列表核验为 ECCV 2026。
- 官方列表仍标注 publisher checks 未完成，因此暂不猜测 Springer DOI/卷页。

## 1. EliGSiR（本周首读）

- **核心问题**：持续建图的质量不只取决于表示，还取决于每一时刻把有限优化预算分配给哪一帧、什么分辨率和哪些缺失几何。
- **方法机制**：把 view、fidelity、growth 三种资源选择显式化；在采集过程中评估地图，而不只比较最终 PSNR。
- **首要复现**：在统一跟踪器和 wall-clock 预算下画出任意时刻的几何/渲染质量—计算曲线，并分离调度收益与更好 pose 的收益。
- **不能据此断言**：室内 RGB-D 结果不能直接证明在单目、户外长航迹或月面极端光照下稳定。

## 2. RawSLAM、SplashSplat 与 PersistBench

- RawSLAM 说明传感器辐射度链路是几何系统的一部分，不能把 tone mapping 当无害预处理。
- SplashSplat 说明动态重建中的物理结构应只施加在观测可约束处，而不是全局硬套刚体或连续流假设。
- PersistBench 把“短时像素相似”与“对象离场后仍被正确记忆”分开，补足 4D 模型的长期可靠性指标。

## 独立研究点 A：带一致性证书的预算自适应持续重建

- **假设**：以局部几何缺口、全局位姿风险和新视图信息量共同调度计算，比只按新颖度或负载分配预算更能维持长序列“随时可用”地图。
- **相对已有工作的变化**：在 EliGSiR 的 view/fidelity/growth 调度上加入 AMB3R 式分层一致性风险与拒绝更新，显式输出地图适用域。
- **最小验证**：Replica、TUM、ScanNet++ 和一组 5k–10k 帧户外 RGB-D/单目序列；固定 GPU 时间和峰值显存。
- **指标**：全程/最终 F-score、PSNR、ATE、错误增长率、风险覆盖曲线、FPS、峰值显存与每帧优化预算。
- **关键基线**：SplaTAM、CaRtGS、EliGSiR、AMB3R、固定窗口/固定分辨率版本。
- **消融**：去掉几何缺口、位姿风险、拒绝分支或分层后端；等算力对照。
- **证伪条件**：联合调度在相同预算下不改善任何时刻质量，或收益完全来自更少处理视图。
- **失败模式与风险**：罕见新区域被拒绝；风险分数跨域失校准；调度开销吞噬节省。风险中高。

## 独立研究点 B：遮挡后可验证的对象级 4D 记忆

- **假设**：显式维护对象身份、运动不确定度和外观记忆，并在重现时执行几何一致性校验，可显著改善 4D 模型的离场对象恢复，而不牺牲快速变化区域。
- **相对已有工作的变化**：把 PersistBench 的诊断转为可更新/可撤销的对象记忆，并借鉴 SplashSplat 的“仅在可约束处施加物理结构”。
- **最小验证**：PersistBench 加合成遮挡长度、相机回访和对象拓扑变化；再用 SplashSplat 的快速动态序列作反例压力测试。
- **指标**：object permanence、motion continuity、appearance preservation、身份切换、重现几何误差、校准与延迟。
- **关键基线**：无记忆 4D 模型、固定 latent cache、视频 memory transformer、仅运动先验、oracle 可见性。
- **消融**：无身份状态；无不确定度；无重现校验；刚体/非刚体分别移除；不同记忆容量。
- **证伪条件**：对象记忆只改善静态/缓慢对象，或离场恢复提升以可见动态区域显著退化为代价。
- **失败模式与风险**：错误身份长期固化；快速拓扑变化不适合对象状态；360° 基准先验过强。风险高。
