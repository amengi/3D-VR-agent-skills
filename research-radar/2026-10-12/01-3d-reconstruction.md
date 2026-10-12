# 方向一：三维重建

## 本轮新增代表论文

| 论文 | WHY | HOW | WHAT | 经典脉络中的位置与证据边界 |
|---|---|---|---|---|
| [Slot3R](https://arxiv.org/abs/2610.12282) | 流式重建若按空间邻近直接融合 memory pointer，会把同位置的不同表面、视角或可见状态过早平均掉 | 冻结 Point3R，以 set-associative retrofit 允许同一空间地址保留多个状态，并用有界稀疏 readout 解耦持久存储与逐帧读取 | 300–500 帧时作者报告 7Scenes 点云 Acc error 降 57.1%–63.1%、NeuralRGBD 降 64.0%–72.0%；600–1000 帧约 19 FPS，而两基线在 800 帧后 OOM | 从“单地址单状态”推进到保留歧义的流式空间记忆；预印本，项目页可见，但更长序列、闭环重复访问和动态场景仍未证明 |
| [ReVar3R](https://arxiv.org/abs/2610.07883) | 对前馈重建做输入扰动时，输出会在任意相似变换 gauge 中漂移，直接计算点方差会把坐标变化错当模型不确定度 | 先把各次预测注册到共同 similarity frame，再按点聚合 perturbation variance；无需训练 | 作者在 VGGT、π3、MASt3R 和 6 个数据集上报告 18 个条件中 15 个的 AUSE 低于模型内置 confidence | 从“预测置信度”推进到 gauge-aware 几何 UQ；预印本，不能发现跨扰动稳定的系统偏差，也未证明跨域校准 |
| [Matisse](https://arxiv.org/abs/2609.38746) | 主动重建需要用有限视角优先观察真正缺失或含混的几何，而不只追逐覆盖率 | 从预训练生成式 3D 模型的 cross-attention evidence 构造 evidential uncertainty 与 information gain，训练自由地选视角/关键帧 | 作者报告 GSO30、YCB-V、Replica 的 Chamfer 分别改善 12.7%、3.8%、9.2%，并称比 Stream3D 快 1.5×、用 14% 视角达到相当质量 | 从手工几何熵走向基础模型证据驱动的 active reconstruction；预印本，项目页写明代码尚未开放，先验偏差可能误导采集 |
| [VASC](https://arxiv.org/abs/2610.01013) | VGGT/π3 类全局注意力随 token 数平方增长，难在长序列或板端持续重建 | 以 token 价值选择稀疏 attention，并用 execution-aware cross-layer memory 避免重复计算 | 作者报告 VGGT 最高 2.29× 加速，并在 7Scenes、NeuralRGB-D 的位姿/几何上优于 FasterVGGT | 从离线前馈重建走向预算化推理；预印本，已核验[公开实现](https://github.com/kosakayamahoo-design/VASC)，但能耗、长时漂移和嵌入式结果未证明 |
| [4D-HOF](https://arxiv.org/abs/2610.08782) | 手—物交互的 4D 重建既要补全遮挡，又要满足接触与运动物理，单帧或纯回归容易产生不可能状态 | 以视觉基础模型的粗状态为条件，用 conditional flow matching 生成轨迹，并在测试时用物理约束和 2D 证据引导 | 作者报告在 OOD 交互上达到其比较中的最佳结果 | 从静态/动态几何走向受交互约束的 4D reconstruction；预印本摘要没有足够数值，物理约束的真实接触有效性待复现 |

## 1. Slot3R（本轮首读）

- **核心问题**：空间接近只说明观测应写入同一地址附近，不代表它们属于可立即平均的同一隐状态；遮挡边界和重复观察尤其容易把互补证据抹掉。
- **方法机制**：同址多 slot 保存候选状态，读出时只取有界稀疏集合；训练自由、冻结 Point3R，使改进可归因于记忆组织而非重新训练。
- **最小复现**：在 7Scenes、NeuralRGBD 和含回环/动态遮挡的长序列上，固定帧数、显存与 backbone，比单状态融合、多 slot、无界检索和简单关键帧缓存。
- **不能据此断言**：短于 1000 采样帧的 19 FPS 与 Sim(3)-aligned 指标不能证明无限记忆、闭环全局一致、动态身份保持或板端实时性。

## 2. ReVar3R

- **核心问题**：扰动式不确定度只有在输出先进入同一坐标系后才有物理意义；否则模型每次任意选择的 scale/rotation/translation 会污染方差。
- **方法机制**：训练自由地做多次输入扰动与前馈预测，将结果用 similarity registration 对齐，再估计每点变异。
- **最小复现**：固定 VGGT/π3/MASt3R 权重，在室内、室外、低纹理和重复纹理上比较内置 confidence、未对齐 variance、对齐 variance；严格隔离注册失败样本。
- **不能据此断言**：低 AUSE 不代表绝对尺度正确，也不代表模型能发现所有稳定的深度偏差、反光表面错误或分布外失效。

## 3. Matisse、VASC 与 4D-HOF

- Matisse 把基础模型内部 evidence 变成下一最佳视角/关键帧信号，但项目页明确为 `Code coming soon`，本轮不把它计作可复现实作。
- VASC 说明 attention token 预算可由几何价值而非规则下采样决定；下一步应把吞吐提升换算为能耗、时延尾部与精度风险。
- 4D-HOF 把测试时物理引导引入交互重建，适合检验“视觉似然高但接触不可能”的失效，不宜仅按渲染质量评价。

## 独立研究点 A：带系统偏差探针的 gauge-aware 主动重建

- **假设**：用 ReVar3R 的 gauge-aligned perturbation uncertainty 过滤坐标伪差，再以 Matisse 的 evidence gain 选视角，并额外加入稳定偏差探针，可在等视角预算下同时降低几何误差和过度自信。
- **相对已有工作的变化**：不仅用 uncertainty 排序视角，还将“扰动方差低但与多视重投影/稀疏量测持续冲突”的区域标为 systematic-bias candidate。
- **最小验证**：Replica、YCB-V、GSO30 加低纹理/高光合成集；每场景固定 7、14、28 个视角，并保留一组未见相机轨迹。
- **指标**：Chamfer、F-score、ATE、AUSE、ECE、risk–coverage AUC、视角数、重建时延和稳定偏差召回率。
- **关键基线**：ReVar3R、Matisse、模型内置 confidence、未对齐扰动方差、随机/NBV 几何熵、oracle error map。
- **消融**：无 gauge registration、无 evidence gain、无偏差探针、不同扰动族、无关键帧淘汰。
- **证伪条件**：对齐 UQ 不能改善错误排序，或主动选择收益完全来自更多覆盖而非可靠 uncertainty；偏差探针在未见材质上不优于随机报警。
- **失败模式与风险**：注册在低重叠视角失败；基础模型 evidence 与真实几何误差不相关；探针过度拒绝高光/无纹理区域。风险高。

## 独立研究点 B：保留歧义且可校准的流式稀疏注意力重建

- **假设**：先用 Slot3R 的同址多状态保留歧义，再以 VASC 的价值稀疏读出按“几何新颖性 + 交互违反 + 不确定度”分配预算，可在固定时延下减少错误融合并保留关键接触证据。
- **相对已有工作的变化**：把“写入时是否融合”和“读取时是否计算”分开；被合并/剪除状态都必须给出对遮挡恢复、接触和轨迹 UQ 的影响证书。
- **最小验证**：7Scenes/NeuralRGB-D 的静态长序列，加公开手—物交互视频；在 25、50、100 ms/帧三档预算下做离线与流式比较。
- **指标**：ATE、Chamfer、4D trajectory error、接触时刻/穿透率、ECE、吞吐、峰值显存、P95 时延和能耗代理。
- **关键基线**：Point3R、Slot3R、dense VGGT/π3、FasterVGGT、VASC、均匀 pruning、4D-HOF 原模型、oracle state/token importance。
- **消融**：单 slot/多 slot、无 cross-layer memory、无交互违反项、无 UQ、固定稀疏率、只按 attention magnitude。
- **证伪条件**：等预算下动态/接触指标明显劣于简单均匀下采样，或 importance 分数不能预测被剪 token 的任务损失。
- **失败模式与风险**：罕见接触在进入注意力前已被剪掉；记忆累积错误；吞吐提升被数据搬运抵消。风险高。
