# Seed Radar — 2024–2026

This seed set was assembled on 2026-08-31 from official publisher/proceedings pages and arXiv records. It is a launch point for query expansion, not a complete review. Machine-readable records and scores are in `paper-catalog.json`.

## High-signal clusters

- Planetary reconstruction/data: StereoLunar, LuSNAR, Zhurong multisensor reconstruction, multimodal lunar reconstruction, and emerging radiance-field planetary mapping.
- Planetary digital twins/simulation: the Yutu-2 mission digital twin; Chrono sensor, dust, and deformable-terrain simulation; CLVSim; and gravity/terramechanics validation.
- Online robot maps: DUSt3R, MASt3R, VGGT, Gaussian Splatting SLAM, SplaTAM, Photo-SLAM, MISO, PINGS, and GauSS-MI.
- Simulation-to-robot transfer: CASHER, ManiSkill3, and RoboSpatial.

## Most promising synthesis directions

1. A geometry–photometry–terramechanics map jointly estimating shape, reflectance, slip/sinkage parameters, and uncertainty.
2. Lunar/Martian adaptation of visual-geometry foundation models using physically rendered supervision, mission-image self-training, calibration, and onboard scaling.
3. Active reconstruction where next-best-view utility includes traversability and science value rather than rendering quality alone.
4. Real-to-sim-to-real planetary digital twins updated from sparse mission or analogue data and evaluated on perception and control.
5. Onboard-efficient long-sequence reconstruction using compressed descriptors, submaps, and hybrid SDF–3DGS maps under power/memory limits.

## Limitations

- The seed emphasizes English-language and openly discoverable sources.
- Some planetary entries are preprints or workshop papers and are labeled in the catalog.
- Citation counts are omitted because provider/date-sensitive metrics age quickly.
- The exact rolling 24-month cutoff must be recomputed on every use; 2024 near-window seeds remain useful for query expansion.
