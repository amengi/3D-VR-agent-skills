# Six-Dimension Scoring Rubric

Score each paper from 0–100. Every dimension is capped and the total is recomputed.

| Dimension | Max | Question |
|---|---:|---|
| Topic match | 35 | How directly does it connect reconstruction, simulation, planetary environments, or robotics? |
| Method value | 20 | Is the technical method rigorous, reusable, and suitable for comparison or extension? |
| Source quality | 15 | Is the venue/status credible and the evidence inspectable? Preprints cannot receive more than 9 here. |
| Cross-lane bridge | 10 | Does it connect two or more radar lanes rather than optimize an isolated benchmark? |
| Applied value | 10 | Are code, data, system details, onboard feasibility, or validation useful for implementation? |
| Archival value | 10 | Is it likely to remain useful as a benchmark, representation, simulator, or conceptual anchor? |

Gate: reject from the ranked shortlist when `topic_match < 10`, even if the total is high.

- `A / core`: 80–100, directly shapes a project or benchmark.
- `B / bridge`: 65–79, strong transferable mechanism.
- `C / watch`: 50–64, emerging or narrower evidence.
- `<50`: archive only unless the user explicitly requests breadth.

Do not inflate source quality because a venue is famous. Do not award applied value for an unverified code claim. When the user supplies tracked authors, labs, missions, hardware, or datasets, state any rubric customization before scoring.
