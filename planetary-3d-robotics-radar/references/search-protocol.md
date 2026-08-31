# Search Protocol

## Scope declaration

Always record the search date and exact date range; direct and adjacent lanes; included languages and publication types; and whether the goal is discovery, comparison, gap analysis, or monitoring.

## Query families

Run at least one query from each relevant family. Adapt terms instead of using one giant Boolean string.

- Planetary reconstruction: `(lunar OR moon OR martian OR mars OR planetary OR extraterrestrial) AND (3D reconstruction OR stereo OR photogrammetry OR shape from shading OR neural rendering OR Gaussian splatting OR radiance field OR DEM)`
- Physics and sensor simulation: `(lunar OR martian OR regolith) AND (digital twin OR terramechanics OR wheel soil interaction OR deformable terrain OR sensor simulation OR physically based rendering OR Hapke OR ray tracing)`
- Robot autonomy: `(lunar rover OR mars rover OR planetary robot) AND (SLAM OR localization OR traversability OR navigation OR active mapping OR hazard detection OR manipulation OR reinforcement learning)`
- Transferable methods: `(3D reconstruction OR neural SLAM OR spatial intelligence OR real-to-sim-to-real OR world model) AND (robot OR embodied AI OR active view OR digital twin)`
- Chinese expansion: combine `月球/月面/月壤/火星/巡视器/三维重建/数字孪生/地形仿真/轮壤作用/自主导航/同步定位与建图` when Chinese missions or engineering work is relevant.

## Source order

1. Official proceedings and publishers: CVF/ECVA, RSS, IEEE, ACM, Springer Nature, Wiley, Elsevier, and mission or agency archives.
2. DOI landing pages and arXiv for metadata or full preprints.
3. Official project and code repositories for artifacts, never as the sole evidence of peer review.
4. Broad web or scholarly indexes for discovery; verify inclusions against levels 1–2.

For fast-moving CS/robotics, inspect CVPR/ICCV/ECCV, ICRA, IROS, RSS, CoRL, SIGGRAPH/TOG, RA-L, T-RO, IJRR, Journal of Field Robotics, ISPRS journals, and relevant aerospace/planetary venues. Venue prestige is a filter aid, not evidence that a claim is correct.

## Screening

Include papers that contribute planetary data or mission evidence; reconstruction/localization under relevant constraints; physically grounded simulation or a validated digital twin; robot policy/planning using 3D representations; or a transferable mechanism with a concrete planetary validation path.

Exclude duplicates, unverifiable references, marketing-only pages, and papers whose connection is merely rhetorical. Keep high-value preprints with an `emerging` label.

## Verification and deduplication

Record title, authors, year, venue, DOI or stable identifier, authoritative URL, peer-review status, access level (`full_text`, `abstract`, `metadata`), verified code/data link, and search date.

Normalize DOI to lowercase without `https://doi.org/`. If absent, lowercase the title, remove punctuation and common articles, then match first author plus title-token Jaccard similarity of at least 0.90. Prefer richer publisher metadata and link the preprint as a secondary artifact.

Report a distribution warning if at least 70% of known entries fall into one year, one method family, one venue family, or one planetary body. This is an advisory, not an automatic defect.
