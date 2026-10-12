# 方向三：机器人视觉与具身视觉

只收视觉表示、定位、感知、空间理解、视觉预测或主动视觉为核心贡献、机器人承担任务载体和闭环验证的工作；纯机构、本体、材料、执行器、控制、动力学辨识和无视觉机制的一般强化学习不纳入。

## 本轮新增代表论文

| 论文 | WHY | HOW | WHAT | 经典脉络中的位置与证据边界 |
|---|---|---|---|---|
| [DepthWorld](https://arxiv.org/abs/2610.08780) | 跨机器人视频混有不同相机、运动学和视角，纯 RGB world model 难获得可迁移的 metric 3D 监督 | 用 learned stereo depth 与联合 factor graph 汇集每台机器人的多 episode，校准共享运动学/逐场景外参；再用 spatial latent tiling 联合生成多视 RGB 与 metric depth | 作者项目页称 DROID-3D 含 71,100 episodes、28 台机器人、13 个实验室；摘要报告 90% 外部相机 episode 重投影误差低于 0.7 px，深度监督使同架构 PSNR 增 1.48 dB | 从像素 video prediction 推进到多本体、metric-depth 世界模型；预印本，CoRL 2026 为作者声明，已核验[项目](https://jaibardhan.com/depthworld/)与[代码](https://github.com/Jai2500/depthworld) |
| [Blackout vs. Freeze](https://arxiv.org/abs/2609.39145) | VLA 在摄像头黑屏或画面冻结时可能继续输出危险动作，而任务成功率会掩盖意外接触 | 对 π0.5、GR00T 系统注入 camera blackout/freeze，比较有无 proprioception 与多种缓解策略，并做真实机器人试验 | 作者观察 freeze 可触发极端关节行为，抓取后的 blackout 易掉落；缓解虽提高成功率却可能增加非预期接触 | 从平均成功率推进到视觉故障下的安全行为审计；预印本、模型与任务范围有限，不能等同通用 VLA 安全结论 |
| [VersaCamVLA](https://arxiv.org/abs/2610.12451) | 固定相机数量/位姿训练的 VLA 在部署换视角时脆弱，直接拼接多视图也不能处理可变相机集合 | 将任意 posed RGB view set 映射为固定数量 scene tokens，以 target-view prediction 与 wrist-augmented pose sampling 学相机不变表示，再轻量注入预训练 VLA | 作者报告 RoboTwin、LIBERO 和真实机器人上优于 VLA/直接多视基线，并在未见相机数量/位姿下保持性能 | 从固定视角策略推进到 camera-configurable VLA；NeurIPS 2026 仅作者声明，隐 token 的 metric geometry、故障检测与标定误差敏感性待核验 |
| [Rendering-Free Lookahead](https://arxiv.org/abs/2610.11039) | 主动视觉必须预判未见视角能否回答任务问题，但在线渲染每个候选未来视图代价高 | 训练时在 3DGS 场景渲染一/两步候选视图，用冻结 VLM 产生 answerability target；两阶段蒸馏后部署只由问题、历史观测和候选动作预测价值 | 作者在 377 个未见环境 episode 上报告 mean judge score 较同 VLM 的 direct-action 基线高 43% | 从几何 NBV 推进到问题驱动的 rendering-free 视觉动作价值；预印本，VLM judge/3DGS teacher 偏差和真实机器人证据不足 |
| [World Motion Models](https://arxiv.org/abs/2610.01742) | RGB/视频世界模型难统一关节物体、人、手—物、相机与机器人状态，也难直接供控制与 retargeting 使用 | 用稀疏 SE(3) trajectories 统一实体和动作，以 flow matching、逐 token 噪声和 any-to-any mask 支持预测、补全、MPC、IK 与 retargeting | 作者展示 6 类应用；NeurIPS 2026 Spotlight 仅按作者/arXiv 声明记录 | 从像素预测走向可组合 3D 运动 token；预印本，跨任务共用表示的长期误差、视觉观测生成过程和真实闭环安全待核验 |
| [AssemblyWorld](https://arxiv.org/abs/2609.40353) | 现有具身基准常允许访问 mesh/状态，不能测量 agent 能否从 2D 视图理解零件并完成精确装配 | 构建交互 3D 环境，agent 只能检查 rendered 2D views 并操作刚体零件；包含 100 个任务、80 个对象 | 8 个 agent 中最强者零件正确率 80.9%，但完整装配仅 59.4% | 从视觉问答/粗粒度 manipulation 推进到多视几何约束的长程装配；预印本，仿真视觉、刚体假设和任务规模限制外推 |

## 1. DepthWorld（本轮首读）

- **核心价值**：先把跨实验室机器人视频变成可量测的相机—机器人几何，再训练同时预测 RGB 和 metric depth 的 world model，减少“视频合理但空间尺度错误”。
- **方法机制**：用多 episode 联合图优化共享机器人运动学与逐场景外参；生成模型通过空间 latent tiling 保留预训练 VAE，同时对齐多视图和深度。
- **首要复现**：按机器人、实验室和相机位置严格留一；独立复测标定误差、深度尺度、长 rollout 漂移和下游规划收益。
- **不能据此断言**：PSNR/重投影误差改善不能自动证明接触、安全或视觉故障下的闭环成功；作者声明的会议状态需等正式记录。

## 2. Blackout vs. Freeze、World Motion Models 与 AssemblyWorld

- Blackout vs. Freeze 的关键发现是“成功”可能伴随危险接触，因此 VLA 评测必须同时记录行为 envelope、接触和传感器 freshness。
- World Motion Models 用 SE(3) 轨迹把视觉世界状态变成可供 MPC/IK 使用的稀疏 token，但需检查稀疏抽象是否丢掉接触表面与可见性。
- AssemblyWorld 用只读 2D 视图隔离视觉—空间理解能力；零件级 80.9% 到完整任务 59.4% 的落差提示误差会沿多步装配累积。

## 独立研究点 A：可检测相机故障的几何认证视觉世界模型

- **假设**：让 DepthWorld 同时预测 metric depth、跨视重投影和 sensor-freshness/fault state，可在 camera blackout/freeze 时比纯 RGB likelihood 更早拒绝不安全 rollout。
- **相对已有工作的变化**：训练数据显式加入冻结、黑屏、延迟和单视图失配；world model 输出“可用于控制/仅可用于预测/必须停止”三态证书，而非无条件生成。
- **最小验证**：DROID-3D 子集加 Blackout vs. Freeze 的故障协议；至少 3 台机器人、6 类视觉操作、留一实验室测试。
- **指标**：PSNR、depth RMSE、重投影误差、故障检测 AUROC/延迟、risk–coverage、掉落/碰撞/非预期接触、任务成功和校准误差。
- **关键基线**：DepthWorld、RGB-only video model、帧差/freshness detector、π0.5/GR00T 原策略、简单 stop-on-black、oracle fault state。
- **消融**：无 depth、无多视一致性、无故障注入、无 proprioception、二态/三态证书、不同故障持续时间。
- **证伪条件**：几何一致性不能比简单像素帧差更早预测危险，或安全收益只来自全程保守停止并显著损失正常任务覆盖。
- **失败模式与风险**：场景静止被误判 freeze；生成模型自洽地延续错误画面；proprioception 掩盖相机故障。风险高。

## 独立研究点 B：由视觉证据约束的 SE(3) 装配世界模型

- **假设**：从 AssemblyWorld 多视 2D 证据估计带协方差的 part-level SE(3) tokens，再用 World Motion Models 的 any-to-any trajectory infilling，可减少多步装配中的累计位姿错误。
- **相对已有工作的变化**：不读取 mesh/真值状态；每个 motion token 必须链接到支持它的视角、遮挡状态与接触证据，并允许主动请求下一视角。
- **最小验证**：AssemblyWorld 100 任务中按对象族留出 20%，限定每步 1/3/5 个视角；再迁移 10 个真实桌面装配任务。
- **指标**：part pose ADD-S/旋转平移误差、完整装配率、步骤恢复率、接触/穿透错误、视角数、轨迹 NLL/ECE 和推理时延。
- **关键基线**：AssemblyWorld 最强 agent、World Motion Models、逐帧 pose + planner、像素 video world model、oracle part pose。
- **消融**：无视觉 provenance、无 covariance、无 trajectory infilling、无主动视角、无接触 token、不同 token 稀疏度。
- **证伪条件**：SE(3) 表示不改善完整装配率，或姿态指标改善却因接触几何缺失导致更多装配失败。
- **失败模式与风险**：对称零件姿态多解；遮挡使 token 过度自信；仿真渲染捷径；真实摩擦/公差未建模。风险高。

## 独立研究点 C：可变相机集合下的任务主动视觉 VLA

- **假设**：用 VersaCamVLA 的 set-level scene tokens 表示当前任意相机集合，再用 Rendering-Free Lookahead 的 answerability 选择“保留、移动或新增哪台相机”，可在等观测成本下降低未见位姿造成的操作失败。
- **相对已有工作的变化**：从被动适配相机配置扩展为主动配置；scene token 必须输出视角贡献、外参不确定度和 freshness，避免把冻结/误标定相机当有用证据。
- **最小验证**：RoboTwin/LIBERO 各 10 任务和 5 个真实桌面任务；随机改变 1–4 台相机数量、位姿、遮挡、冻结与外参噪声，每步至多一次相机动作。
- **指标**：任务成功、相机动作数、answerability、未见位姿 gap、故障 AUROC、外参噪声曲线、非预期接触、时延与 scene-token 校准。
- **关键基线**：固定相机 VLA、直接多视拼接、VersaCamVLA、WARP-VLA、Rendering-Free Lookahead、随机/几何 NBV、oracle camera set。
- **消融**：无 target-view prediction、无 WAPS、无主动视角、无 freshness/外参 UQ、单步/两步 lookahead、不同 token 数。
- **证伪条件**：主动配置不优于随机/固定多视，或收益只来自更多图像；scene token 在未见外参与故障下持续高置信错误。
- **失败模式与风险**：相机运动干扰操作；VLM answerability 与成功率错位；token 压缩抹掉精细接触几何。风险高。
