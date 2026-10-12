# 3D-VR Agent Skills

Reusable agent skills for research at the intersection of 3D reconstruction, simulation/digital twins, planetary exploration, and robotics.

## Included skill

### `planetary-3d-robotics-radar`

An evidence-traceable research radar that:

- searches a rolling two-year literature window;
- covers lunar/Martian reconstruction, planetary simulation, digital twins, SLAM, robot learning, and adjacent top-venue methods;
- verifies publication status and deduplicates records;
- ranks papers with a six-dimension rubric;
- extracts WHY/HOW/WHAT, limitations, transfer value, and research gaps;
- proposes testable project directions with validation plans and risk levels.

The machine-readable catalog contains 100 verified radar records from 2024–2026 and is intended for query expansion, not as a completeness claim.

## Validation

```bash
python3 planetary-3d-robotics-radar/scripts/validate_catalog.py \
  planetary-3d-robotics-radar/references/paper-catalog.json
python3 -m unittest discover -s planetary-3d-robotics-radar/tests -v
```

The skill has also passed the Codex `skill-creator` structural validator.

## Use

Invoke the skill as `$planetary-3d-robotics-radar`, or install/copy the skill directory into the skill path used by your compatible agent host.

## Research outputs

- [2026-10-12 weekly research radar](research-radar/2026-10-12/README.md): fifteen new emerging papers across reliable/streaming reconstruction, Mars and contact simulation, digital-twin validation, and vision-centered embodied tasks.
- [2026-09-28 weekly research radar](research-radar/2026-09-28/README.md): twelve new emerging papers across deployable reconstruction, simulation/digital-twin validation, and vision-centered robot tasks, with independent and cross-track experiments.
- [2026-09-21 weekly research radar](research-radar/2026-09-21/README.md): ten new emerging papers, two ECCV status upgrades, independent ideas for all three tracks, and assurance-oriented cross-track experiments.
- [2026-09-14 weekly research radar](research-radar/2026-09-14/README.md): nine independently selected additions across reconstruction, simulation/digital twins, and robot vision, one catalog backfill, and assurance-oriented cross-track ideas.
- [2026-09-07 weekly research radar](research-radar/2026-09-07/README.md): six new emerging papers, independent research ideas, cross-track ideas, and a reproducible zero-hit record for simulation/digital twins.
- [2026-08-31 planetary 3D robotics research radar](research-radar/2026-08-31/README.md): ranked recent papers, brief readings, cross-paper research directions, and a reproducible query log.
