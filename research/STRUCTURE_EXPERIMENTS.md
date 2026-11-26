# Exact experiments on comparison components

Research record, 2026-11-26. All scripts use Python's standard library and exact integer or rational arithmetic. Run ordinary Python, without `-O`, because assertions are part of these research checks.

This note records the earlier binary-component scan. The later [arbitrary-size charge method and structural proofs](STRUCTURE_PROOFS.md) establish complete eventual-periodicity results for N=3,...,64. The limits below remain the limits of the binary scan by itself.

## 1. Coverage and what is established

The second-moment transport scan completed every N from 25 through 259: **235 complete base graphs**. Its original requested range extended to 400, but N=260 reached the cap of 100000 base states. No result for N=260 or every N up to 400 is claimed. The default reproduction range now stops at the completed endpoint 259.

Among those graphs, 18 player counts contain 49 closed binary components with second-moment tie phases. Adding the previously studied N=7,10,13,23 gives **54 components for N>2, with 988 tie phases in total**. The tested player counts are

```
7, 10, 13, 23, 29, 33, 40, 50, 54, 57, 78,
79, 86, 93, 99, 122, 145, 164, 173, 182, 230, 242.
```

At every one of the 988 phases:

- The full-period parity ratio is not a Laurent monomial.
- The two equal second-moment loads are strictly away from the global mean.

Either test, with the [parity theorem](PARITY_OBSTRUCTION.md) and [finite-depth normal form](../FINITE_DEPTH.md), proves eventual periodicity within that closed component. The [mean obstruction](MEAN_OBSTRUCTION.md) explains why the second test implies the first.

The N=2 control has monomial ratio 1 at its initial phase and ties at the global mean, so these tests do not incorrectly certify Thue–Morse periodicity.

**These checks do not prove any complete new N>24 case.** Every completed N=25,...,259 has larger components still requiring other arguments. Of the additional small baselines, N=7 is covered entirely by singleton and binary components and already has an independent full-sequence certificate.

The [coverage metadata](scan_coverage.json) records the completed range, cap, tested counts, and limits. Exact labelled prefixes are replayed only where binary components are investigated, through the required initial phases. Counts without such a component receive only the unlabelled base-graph analysis. The scripts reject a noninitial comparison unresolved by the moments they carry; they do not silently break a tie.

## 2. Reproduce the component and parity calculations

From the repository root:

```sh
python3 research/component_scan.py 25 259
python3 research/parity_components.py
```

The first script discovers the second-moment cycles and their closed transport components. Its output is [component_scan.jsonl](component_scan.jsonl). The `unexpected` flag in that discovery record means an outward scalar drift rather than the initially sought restoring return map; it is a classification, not a failed proof. The full-period parity test covers both behaviors and also variable forcing between tie phases.

The second script reconstructs the necessary finite prefixes, builds the occupancy polynomials over a complete base period, and checks **every** second-moment tie phase in every selected binary component. The detailed output is [parity_components.json](parity_components.json). The nonmonomial comparison removes the power of x from each nonzero polynomial and compares the remaining binary coefficient strings exactly. Both tied load and total load are retained so the global-mean test can be checked as an integer equality.

The criterion bounds all future comparison degrees algebraically. It does not infer an infinite tail merely from a finite run, nor does it assert that the deciding degree is always at most four.

## 3. Pairwise ties can form larger networks

The already certified cycles for N=3,...,24 also allow an exact analysis of persistent ties through degree three. At each phase, compare second moments, third-moment intercepts, and third-moment increments per complete cycle. All three must agree; a one-time crossing of different affine profiles is excluded.

```sh
python3 research/third_components.py
```

The calculation trusts the initial states and words in the already verified certificates and checks the increment identities by two exact replays. It does not independently reconstruct their long prefixes again. Full results are in [third_components.json](third_components.json), with the complete table and graph interpretation in [THIRD_COMPONENTS.md](THIRD_COMPONENTS.md).

Every simultaneous persistent tie group in these 22 cases has size at most two. The connected groups over the whole cycle can nevertheless be larger:

| N | Sizes of closed persistent third-moment components |
|---:|:---|
| 8 | 1, 1, 1, 2, 3 |
| 10 | 1, 1, 2, 2, 4 |
| 14 | 14 |
| 24 | Nine singletons, 7, 8 |

Thus the proposed simplification that every persistent third-level component is binary is false. A binary theorem cannot simply be applied to each instantaneous pair when players change partners over the cycle. An argument for such interacting networks is a genuine remaining step toward all N.

## 4. Exhaustive integer-cycle test and a rational counterexample

The possible binary exception motivates the question whether any closed binary component can tie at the global mean. The following computation tests every normalized sorted integer state within the proved spread bound, rather than only the orbit from zero:

```sh
python3 research/mean_cycle_probe.py
```

Its [recorded output](mean_cycle_probe.json) gives:

| N | States exhausted | Distinct cycles | Binary mean-tie counterexamples |
|---:|---:|---:|---:|
| 3 | 10 | 1 | 0 |
| 4 | 84 | 3 | 0 |
| 5 | 1001 | 8 | 0 |
| 6 | 15504 | 1 | 0 |
| 7 | 296010 | 123 | 0 |

These are exhaustive finite checks, not an induction in N. The same script verifies a rational N=4 cycle with two closed binary components and a mean tie. Its normalized gaps are not all integers. Therefore the analogous statement over all real or rational states is false, and a possible general proof must use the integer lattice or a property of the canonical orbit.

The general integer-cycle conjecture, exclusion of every binary parity exception, and eventual periodicity for all N>2 remain open in this repository.
