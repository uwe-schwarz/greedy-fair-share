# Persistent third-moment comparison components

Date: 2026-11-26. Exact analysis of the already-certified N=3,...,24 tails; this is not a proof for new N.

## Construction

Use the certified player-period word as the phase period. Its full labelled schedule repeats, so every label returns to its original phase-zero slot. Replaying the cycle twice shows that the second-moment differences are periodic and the third-moment differences have a constant increment per label per cycle.

At a given phase, players i and j are permanently tied through degree three exactly when their D2 values, D3 intercepts, and D3 cycle increments all agree. An accidental tie with different cycle slopes is excluded.

Connect two labels whenever they have such a persistent tie at any phase. The connected components are the weak components of the phase/rank transport graph: each individual label supplies a closed path through the certified period, and a tie allows switching between the corresponding paths. Hence this graph records every potential exchange of labels that moments through degree three cannot distinguish.

## Results

Every simultaneous persistent tie group in these cases has size at most two. However, the resulting connected components can be much larger: different pairwise comparison events connect multiple players over a period.

| N | Persistent tie events | Largest simultaneous group | Closed component sizes |
|---:|---:|---:|:---|
| 3 | 0 | 1 | 1, 1, 1 |
| 4 | 2 | 2 | 1, 1, 2 |
| 5 | 8 | 2 | 1, 2, 2 |
| 6 | 2 | 2 | 1, 1, 1, 1, 2 |
| 7 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1 |
| 8 | 6 | 2 | 1, 1, 1, 2, 3 |
| 9 | 16 | 2 | 1, 1, 1, 1, 1, 2, 2 |
| 10 | 10 | 2 | 1, 1, 2, 2, 4 |
| 11 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 |
| 12 | 6 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 3 |
| 13 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 |
| 14 | 150 | 2 | 14 |
| 15 | 114 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3 |
| 16 | 60 | 2 | 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3 |
| 17 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 |
| 18 | 42 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3 |
| 19 | 96 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 |
| 20 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 |
| 21 | 24 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3 |
| 22 | 0 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 |
| 23 | 42 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2 |
| 24 | 315 | 2 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 8 |

The proposed simplification “every persistent third-level component is binary” is therefore false already for N=8, where one component has size three. N=14 has one component containing all 14 labels. N=24 has nontrivial components of sizes seven and eight.

This leaves periodic networks of interacting pairwise comparisons as a meaningful target. A binary-component theorem cannot be applied independently to each instantaneous pair when the pair changes partners later in the cycle.

The calculation uses exact integer arithmetic, checks the cycle increment identities at every phase of both replays, and trusts only the already-verified initial states and period words in the committed certificates. Reproduce with `third_components.py`; detailed events and player memberships are in `third_components.json`.
