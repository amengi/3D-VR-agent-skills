# Synthesis and Gap Analysis

## Cross-lane matrix

| Layer | Typical outputs | Planetary stressors |
|---|---|---|
| Sensing/rendering | images, depth, LiDAR, thermal, dust artifacts | low texture, extreme illumination, dust, sparse labels |
| Reconstruction/map | mesh, DEM, point map, SDF, 3DGS, semantic map | scale drift, compute limits, long sequences, changing shadows |
| Physics/digital twin | terrain state, wheel forces, slip/sinkage, synthetic observations | uncertain regolith, low gravity, deformable terrain |
| Planning/control | traversability, next-best-view, path/policy | delay, safety, energy, irreversible hazards |
| Reality update | mission data assimilation, calibration, sim-to-real | sparse ground truth, domain shift, limited communication |

The strongest opportunities close a loop across at least three layers instead of improving one isolated metric.

## Gap types

- `empirical`: missing real or high-fidelity planetary data;
- `domain`: terrestrial pretraining fails under planetary appearance or geometry;
- `methodological`: photorealism, metric geometry, uncertainty, or physics are optimized separately;
- `systems`: reconstruction is not linked to planning/control or onboard resource budgets;
- `validation`: synthetic gains lack real, analogue, or mission-data confirmation;
- `benchmark`: no paired perception–physics–decision benchmark;
- `temporal`: a fast-moving foundation-model or representation result has not been retested in the planetary domain.

## Direction template

For each proposed direction provide the gap and supporting papers; borrowed method and transfer rationale; planetary constraint; minimum viable dataset/simulator; baselines and ablations; geometry, photometry, physics, navigation, and compute metrics as applicable; analogue/real-data validation; uncertainty reporting; and principal failure mode/risk tier.

Avoid claiming novelty from a zero-hit search. Use “not found within the documented search” until a broader systematic search supports a stronger statement.
