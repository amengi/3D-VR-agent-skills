# 两两交叉与三方向闭环

以下交叉分析在三个方向独立完成选文后进行，不反向决定纳入论文。

## 两两交叉矩阵

| 组合 | 独立信号 | 可检验交叉问题 |
|---|---|---|
| 三维重建 × 仿真 | Slot3R/ReVar3R/Matisse 给出多状态记忆、对齐 UQ 与主动采集；MarsLab/RenderBench 提供可控场景和成对 twin | 能否用持久歧义与 gauge-calibrated 风险决定该补真实视角、提高 fidelity，还是承认 twin 不可信？ |
| 三维重建 × 机器人视觉 | VASC/4D-HOF 关注预算化几何与交互约束；DepthWorld/AssemblyWorld/VersaCamVLA 需要 metric multi-view 状态 | attention 和相机预算能否由任务部件、接触、视角贡献和故障风险联合分配？ |
| 仿真 × 机器人视觉 | MarsLab/RiCo/Real2Sim2Real 提供视觉与接触模拟；Blackout/DepthWorld/RFL 暴露视觉故障和主动采集问题 | 成对 twin 能否系统生成相机/接触失效，并预测真实视觉策略的危险行为排序与下一视角价值？ |

## 交叉 idea 1：gauge-calibrated 的行星模拟可信度地图

- **假设**：把 ReVar3R 的 gauge-aware uncertainty 与 MarsLab 的可控光照/尘埃/几何干预对齐，可区分“坐标 gauge 伪差”“重建认知不确定度”和“模拟 fidelity 缺口”。
- **相对已有工作的变化**：每个空间单元用 Slot3R 式多状态保留未决证据，同时维护真实/模拟重建差、跨扰动 UQ 和任务敏感度；主动采集与 fidelity 升级由预期风险下降/成本共同调度。
- **最小验证**：MarsLab 6 条路线与一组地球类比场，3 种重建器、4 档光照/尘埃；每条路线固定观测和高保真调用预算。
- **指标**：几何误差、AUSE/ECE、ATE、hazard miss、方法排序相关、主动视角数、高保真调用数、时延和计算成本。
- **关键基线**：MarsLab 默认、Slot3R、ReVar3R、Matisse、固定高保真、随机 fidelity、像素域差驱动调度、oracle error map。
- **消融**：单状态/多状态、无 gauge 对齐、无任务敏感度、无真实类比校准、只升 fidelity/只补视角、不同预算。
- **证伪条件**：三类误差无法分离，或调度不优于固定中/高 fidelity 与普通 NBV。
- **失败模式与风险**：真实—模拟无法精确配准；同一基础模型同时产生重建和调度偏差；代价模型错误。风险高。

## 交叉 idea 2：可重建、可故障注入的具身世界模型基准

- **假设**：用 RenderBench 式 real–twin–proxy 配对、DepthWorld metric depth 和 AssemblyWorld 任务，可判断世界模型的失败究竟来自几何、渲染域差、相机故障还是动作预测。
- **相对已有工作的变化**：对每个任务提供可编辑 twin 与真实/代理观测，系统注入 blackout、freeze、遮挡、外参漂移与 RiCo 式接触偏差；评价从画质扩展到故障下任务安全和主动视角收益。
- **最小验证**：12 个数字孪生场景、6 类装配/操作任务、4 种故障、2 个 world model；至少 3 个真实场景完全留出。
- **指标**：depth/pose error、FVD/PSNR、故障 AUROC、完整任务率、掉落/碰撞/非预期接触、sim–real 排名相关和风险覆盖曲线。
- **关键基线**：DepthWorld、VersaCamVLA、Rendering-Free Lookahead、RGB-only world model、RenderBench 原协议、无故障训练、域随机化、oracle twin/故障标签。
- **消融**：无几何配对、无动态配对、无 metric depth、无 provenance、逐类故障、无风险拒绝。
- **证伪条件**：结构化配对不能提高真实失败归因或策略排序，或 metric depth 改善离线误差却不改善安全指标。
- **失败模式与风险**：小场景基准过拟合；twin 与真实共享重建错误；故障分布不代表现场。风险高。

## 三方向闭环 idea：证据预算化的行星视觉数字孪生

- **假设**：闭环系统按风险在“稀疏注意力重建、主动补视角、提高模拟 fidelity、更新视觉世界模型、停止/人工接管”之间分配预算，可在等计算和观测成本下改善安全—覆盖 Pareto。
- **相对已有工作的变化**：Slot3R/ReVar3R/Matisse/VASC 提供持久、可靠且预算化的几何，MarsLab/RiCo/RenderBench 提供视觉—接触 fidelity 账本，DepthWorld/Blackout/VersaCam/RFL/WMM 提供 metric 预测、相机配置与故障证书；所有更新保留 evidence provenance。
- **最小验证**：一个 MarsLab—类比场 paired twin，30 条含强阴影、尘埃、低纹理、遮挡、相机冻结和未见地貌的导航/交互任务；保留一个地点完全不参与校准。
- **指标**：任务成功、覆盖率、ATE、几何误差、hazard miss、接触事故、UQ 校准、重看/高保真/停止次数、P95 时延、能耗和通信代理。
- **关键基线**：固定 fidelity、固定频率重建、纯视觉策略、无 world model、全程高保真、单一 uncertainty、oracle 调度。
- **消融**：逐一去掉 gauge 对齐、主动采集、稀疏 attention、twin provenance、metric depth、故障证书；严格等预算。
- **证伪条件**：联合系统不能改善安全—覆盖 Pareto，或收益完全来自更高拒绝率、更多传感与更多高保真计算。
- **失败模式与风险**：多个模块共享同一模拟偏差；复杂调度难以稳定；通信中断导致证据过期；过度保守阻断任务。风险高。
