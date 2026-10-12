# 方向二：仿真与数字孪生

## 本轮新增代表论文

| 论文 | WHY | HOW | WHAT | 经典脉络中的位置与证据边界 |
|---|---|---|---|---|
| [MarsLab](https://arxiv.org/abs/2609.34702) | 火星导航算法缺少兼顾任务地形、传感器、尘埃、光照和 ROS2 接口的开放验证底座 | 基于 Isaac Sim，用 HiRISE/程序化地形、岩石/陨坑、太阳照明和大气尘埃配置 Perseverance 级 rover，输出 RGB、深度、点云、LiDAR、IMU、里程计与真值 | 作者给出 SLAM/VPR 在传感、尘埃、几何、路线和光照变化下的基准，并开放[项目](https://kimhoyun-robotair.github.io/MarsLab/)与[代码](https://github.com/kimhoyun-robotair/MarsLab) | 从通用 rover sandbox 推进到可复现火星视觉任务环境；预印本，iSpaRo 2026 为作者声明，传感器/尘埃物理尚未与任务数据系统标定 |
| [RiCo](https://arxiv.org/abs/2610.12333) | 场景级端到端神经动力学容易忽略接触力只在局部近邻表面交换，既浪费计算又损失接触细节 | 用稀疏 contact-surface neighborhood 汇集相对几何、运动和物性，再在刚体内部传播局部接触影响 | MOVi 上作者报告 100 帧位置/方向误差分别降 31%–35%/约 38%，penetration-time 与 mean-depth 差为真值相对 11.0% 和 2.22 mm，并零样本扩到 270 对象 | 从全局点对交互推进到局部接触推理；预印本，刚体/MOVi 与多球碰撞证据不能外推到颗粒轮壤或低重力 |
| [RenderBench](https://arxiv.org/abs/2610.08684) | render-to-real 方法常没有成对、可编辑且经过几何/时间验证的 digital twin 数据，失败难定位 | 重建 12 个静态/动态真实场景，建立 real target—twin—proxy render—annotation 配对，并做几何与时间一致性筛查 | 1,496 对 real–proxy 帧中 14 个候选保留 12 个；可按对象、可见性、关节和运动定位失败 | 从“看起来像”推进到可审计的 twin benchmark；预印本、规模小且以室内场景为主，不能外推到行星环境 |
| [Digital Twin-Driven Real2Sim2Real](https://arxiv.org/abs/2610.08339) | 自动驾驶模拟数据的外观域差和地理错配会削弱 3D 检测迁移 | 重建地理对齐驾驶 digital twin，生成与真实场景成对的 simulator render，再用 diffusion 做 Sim2Real 外观转换和混合训练 | 作者报告 DETR3D 在未用目标图像训练检测器时达到 oracle mAP 的 93.18%，简单 co-training 甚至超过其 oracle | 从泛化域随机化走向地理配准的 paired Real2Sim2Real；预印本，数字孪生/扩散生成的泄漏、驾驶域偏置与行星迁移待审计 |

本轮对低重力、轮壤接触物理和持续在线同步数字孪生的定向差量检索为 **本轮未检出**；不降低来源标准，也不据此声称这些子方向没有新工作。

## 1. MarsLab（本轮首读）

- **WHY**：火星视觉算法不能只在地球驾驶或单一合成图上评估；路线、地貌、太阳高度、尘埃和传感器组合需要可控且可重复。
- **HOW**：把可配置火星地形/环境与 rover、多模态传感器和 ROS2 集成，并以 SLAM/VPR 的跨条件基准暴露域变化。
- **WHAT**：项目和代码已核验公开；当前证据能支持“可运行的开放仿真底座”，不能支持尘埃散射、BRDF、轮壤和真实火星 sensor transfer 已达到 mission-grade fidelity。
- **经典位置**：承接 AirSim/Isaac 类通用仿真与 LuSNAR 等行星数据集，向可交互、多条件、任务可测的火星研究平台推进。

## 2. RenderBench 与 Digital Twin-Driven Real2Sim2Real

- RenderBench 的价值不在场景数量，而在同一资产拥有真实目标、可编辑 twin、代理渲染和结构化失败标签，适合做 fidelity 归因。
- Digital Twin-Driven Real2Sim2Real 表明地理配准可能比无条件“变得更真实”更重要；超过 oracle 的结果也必须优先排查数据划分、配对泄漏和正则化效应。
- 二者都是通用/驾驶域证据，移植到月火环境前必须重新验证辐射传输、尺度、材质和任务相关性。

## 独立研究点 A：任务标定的 MarsLab 传感器物理验证阶梯

- **假设**：按“像素统计—几何量测—SLAM/VPR 排序—任务风险”四级标定 MarsLab 的光照、尘埃和深度/LiDAR 噪声，比只追求图像逼真更能预测真实火星或类比场算法失效。
- **相对已有工作的变化**：为每个 fidelity 模块建立可版本化证据卡，并用任务排名相关性决定是否值得提高物理复杂度；暂不声称完成轮壤或低重力建模。
- **最小验证**：MarsLab 三类地貌、四档太阳高度/尘埃；与 Mars 2020 公开影像/导航产品及一组地球类比序列对齐，测试 3 个 SLAM 与 3 个 VPR 方法。
- **指标**：颜色/频谱距离、深度噪声、ATE、回环 PR-AUC、方法 Spearman、排名翻转率、hazard miss、计算成本和置信区间。
- **关键基线**：MarsLab 默认、无尘埃、简单图像风格迁移、域随机化、全高保真、真实数据 oracle 排序。
- **消融**：逐项去掉太阳模型、尘埃、sensor noise、地形几何和任务级校准；不同真实样本预算。
- **证伪条件**：更高物理 fidelity 不能改善未见条件的方法排序或风险预测，且简单风格增强同等有效。
- **失败模式与风险**：真实火星数据没有稠密真值；运营选择造成分布偏差；像素相似掩盖错误几何。风险高。

## 独立研究点 B：可编辑、成对、无泄漏的数字孪生迁移基准

- **假设**：用 RenderBench 式结构化配对和几何/时间筛查约束 Real2Sim2Real，可区分几何、外观、动态和生成器泄漏对下游 3D 感知的贡献。
- **相对已有工作的变化**：每个 twin 修改都保留 provenance；按地点、资产和时间严格隔离，加入“错误 twin”负对照，不再只比较最终 mAP。
- **最小验证**：12–20 个室内/驾驶场景和至少 2 个火星类比场；静态/动态各半，3 个 3D detector 或视觉定位器。
- **指标**：mAP/NDS、深度/位姿误差、real–proxy 几何与时序误差、域差、跨地点泛化、泄漏检测率和生成成本。
- **关键基线**：无配对随机化、RenderBench 协议、普通 diffusion Sim2Real、直接 synthetic、real-only、oracle matched real。
- **消融**：无地理配准、无几何筛查、无时间筛查、无 provenance、无错误-twin 对照、不同 co-training 比例。
- **证伪条件**：严格隔离后收益消失，或外观生成改善 mAP 却恶化几何/时间一致性和未见地点表现。
- **失败模式与风险**：配对成本过高；扩散模型复制真实训练图；twin 的资产误差被网络当作类别特征。风险高。

## 独立研究点 C：局部接触图驱动的多保真轮壤代理

- **假设**：以 RiCo 的局部接触图作快速代理，并在高滑移/沉陷风险区域切换 DEM/SPH 高保真求解，可比全程高保真或场景级 neural simulator 更好地平衡接触误差与成本。
- **相对已有工作的变化**：把刚体点接触扩展为轮—颗粒/地形 patch 的异构局部图；代理输出误差界和升级请求，不把未知土壤吸收到单一黑箱 latent。
- **最小验证**：单轮土槽 3 种模拟土、3 档载荷/重力等效和 5 条轨迹；低保真局部图、高保真 DEM/SPH 与真实测量成三层配对。
- **指标**：slip、sinkage、drawbar pull RMSE，接触/穿透误差，100/500 步 rollout drift，升级召回率、ECE、速度、显存和能耗代理。
- **关键基线**：Bekker/Wong、DEM/SPH、RiCo、全局 GNN/neural simulator、固定多保真切换、oracle fidelity。
- **消融**：无局部性、无物性、无不确定度、无高保真升级、不同邻域半径、刚体点与颗粒 patch 表示。
- **证伪条件**：代理不优于传统快速 terramechanics，或误差分数不能预测何时需高保真求解；低重力等效改变接触规律后泛化崩溃。
- **失败模式与风险**：颗粒拓扑快速变化导致图爆炸；地面试验不能代表低重力；升级延迟造成不可逆陷车。风险高。
