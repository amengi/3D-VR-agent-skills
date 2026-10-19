# 方向一：三维重建

## 本轮新增代表论文

| 论文 | WHY | HOW | WHAT | 经典脉络中的位置与证据边界 |
|---|---|---|---|---|
| [Motion- and Gravity-Aware Feedforward 3D Reconstruction](https://arxiv.org/abs/2610.22177) | 外观注意力在动态物体、弱几何线索与复杂相机运动下不稳 | 以 LUPI 在训练期注入残余光流和重力方向，推理仍只需标准图像；对 VGGT 与 π3 采用不同层级注入 | 作者称标准基准上的精度与鲁棒性一致提升，且不增加测试期输入/复杂度 | 从纯图像前馈先验推进到“训练时物理先验”；预印本，摘要无完整数值，也未验证错误重力、真实 IMU 或月火域 |
| [SceneAE](https://arxiv.org/abs/2610.19708) | 视角绑定的视频 latent 不适合长期记忆、任意相机查询和相机可控生成 | 用带显式 3D 位置、隐式内容特征的稀疏 3D-anchored latent；几何先生成、内容后生成 | 同一场景 latent 可解码不同相机的 RGB-D，作者称生成质量、成本与相机可控性更优 | 从 view-centric video latent 走向 scene-centric queryable memory；预印本，长期更新、度量几何与闭环任务尚未证明 |
| [MicroSDF](https://doi.org/10.1109/TIP.2026.3678096) | 反光与非反光表面对几何/外观提出冲突建模需求 | 以 microfacet theory 约束宏/微法线，双分支颜色模型与检测引导融合，再分阶段优化 | 作者在 DTU、Shiny Blender、Ref-NeRF、DeepVoxels 报告高质量混合反射重建 | 把材质物理更深地嵌入 neural SDF；IEEE TIP 2026 正式论文，但行星风化层 BRDF、尘埃与极端照明未验证 |
| [MIRAGE](https://arxiv.org/abs/2610.12568)（补录） | 图像前馈几何缺 metric scale 且长轨迹漂移；LiDAR–IMU 有尺度却缺图像一致性 | 以 LiDAR–IMU 锚定视觉几何，并按 correspondence support 与跨模态一致性调节在线位姿修正 | 作者在 Oxford Spires、M2DGR、INS 报告准确 metric 轨迹，并新建长时室内视觉基准 | 从 feed-forward reconstruction 走向可靠 metric 传感融合；预印本，v1 本应落入上一轮窗口，因目录漏记而透明补录，v2 本周更新；跨模态失配和低资源部署待证 |

## 1. Motion- and Gravity-Aware Feedforward 3D Reconstruction（本轮首读）

- **WHY**：前馈 transformer 虽快，却可能只学到外观相关捷径；动态场景和弱纹理下，运动残差与重力方向提供互补结构。
- **HOW**：训练期把光流残差、重力作为 privileged information，引导 backbone 表征；部署时移除这些额外信号。作者还发现 VGGT 更适合中层注入、π3 更适合后层注入。
- **WHAT**：证据支持“无需增加测试期传感即可改善若干困难条件”，但摘要没有给出逐数据集增益，不能据此声称通用 SOTA 或错误先验鲁棒。
- **经典位置**：承接 DUSt3R/MASt3R/VGGT/π3 的图像前馈几何，把惯性/运动从输入融合改造成训练监督；适合作为行星场景“有 IMU 训练、单/多相机部署”的起点。

## 2. SceneAE、MicroSDF 与 MIRAGE

- SceneAE 把“场景本身”而非相机轨迹上的帧作为 latent，适合研究持久更新、跨视角查询与 world-model memory，但还缺 metric consistency 和在线遗忘评测。
- MicroSDF 是本轮唯一由 publisher DOI 核验的正式期刊论文；其 microfacet 机制可启发月壤/岩石反射建模，但不能直接等同 Hapke 或颗粒介质散射。
- MIRAGE 值得与上周 ReVar3R 对照：前者解决尺度/漂移与跨模态约束，后者处理 gauge 对齐后的扰动不确定度；两者都未自动解决稳定系统偏差。

## 独立研究点 A：重力—metric—可靠度三重一致的前馈重建

- **假设**：训练时重力/运动 LUPI、部署时稀疏 LiDAR–IMU metric 锚点，再加 gauge-aware UQ，能在长时动态序列上同时降低尺度漂移与过度自信。
- **相对已有工作的变化**：不把重力只当额外特征；建立视觉几何、重力轴、metric 轨迹和扰动置信度之间的冲突门控，冲突时输出拒绝/补采而非强制融合。
- **最小验证**：EuRoC、TUM Dynamic、M2DGR 与一个月面类比场；完整传感、稀疏锚点、视觉-only 三档，固定同一 VGGT/π3 backbone。
- **指标**：ATE/RPE、尺度误差、重力角误差、点云 accuracy/completeness、AUSE/ECE、risk–coverage、P95 时延。
- **关键基线**：VGGT、π3、Motion/Gravity LUPI、MIRAGE、ReVar3R、经典视觉惯性/激光惯性里程计。
- **消融**：无 motion、无 gravity、无 metric anchor、无跨模态门控、无 gauge 对齐、错误重力与时钟偏移。
- **证伪条件**：长轨迹尺度/可靠度不优于简单后端融合，或冲突门控在未见域不能预测真实误差。
- **失败模式与风险**：重力方向在剧烈运动中被污染；LiDAR 稀疏/尘埃回波误导尺度；所有分支共享训练域偏差。风险高。

## 独立研究点 B：材质物理约束的可查询 3D 场景 latent

- **假设**：在 SceneAE 的 3D-anchored latent 中显式分离几何、microfacet/BRDF 与内容，可在混合反射场景中同时提高新视角 RGB-D、几何和下游空间查询。
- **相对已有工作的变化**：将 MicroSDF 的材质物理从单场景优化器抽象为可持续更新的局部 latent 属性，并对材质不确定度与几何不确定度分别校准。
- **最小验证**：DTU、Shiny Blender、真实岩石/金属混合物和小型月壤类比台；固定视角预算，测试重建、生成和语义/可供性查询。
- **指标**：Chamfer/F-score、normal error、depth RMSE、PSNR/LPIPS、BRDF 参数误差、跨视角 query consistency、校准误差、显存/时延。
- **关键基线**：SceneAE、MicroSDF、NeuS/VolSDF、3DGS、无物理属性的 3D latent、oracle material mask。
- **消融**：无 microfacet consistency、单颜色分支、无几何—材质分离、无持续更新、错误材质先验。
- **证伪条件**：几何收益只来自更多参数，或物理分解在未见材质/照明下不比普通 latent 更稳。
- **失败模式与风险**：microfacet 模型不适合多孔颗粒表面；几何与反射不可辨识；更新时旧观测被灾难性遗忘。风险高。
