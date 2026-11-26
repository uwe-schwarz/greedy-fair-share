# Greedy Fair-Share Sequences

[![Verify certificates](https://github.com/uwe-schwarz/greedy-fair-share/actions/workflows/verify.yml/badge.svg)](https://github.com/uwe-schwarz/greedy-fair-share/actions/workflows/verify.yml)

Exact eventual-periodicity certificates for the multiplayer greedy duel rule discussed in Stand-up Maths' [*Taking turns isn't fair. We fixed it.*](https://www.youtube.com/watch?v=pOSSpd8mb4Y).

At each turn, give the next opportunity to the player with the smallest probability of having won so far, in the **termwise limit** as the common hit probability tends to zero.

English is the canonical language for the documentation. The [full proof](fair_share_proof.md) uses the default filename; the [German translation](fair_share_proof.de.md) is retained separately. Make substantive updates to the English version first, then update translations.

## Research status

- **Established for each `N = 3, …, 64`:** the exact structural checker certifies an eventual lower-moment regime and distinct conserved fourth-moment charges. This proves eventual periodicity. The earlier `N = 3, …, 24` word certificates additionally verify explicit least periods and minimal preperiods. See [structural proofs](research/STRUCTURE_PROOFS.md).
- **Written out by hand for `N = 3`:** the proof exhibits a closed nine-block cycle, giving least period 54 after 47 initial terms.
- **General reduction for every `N ≥ 2` and every fixed moment depth:** the unlabelled moment dynamics eventually has a polynomial form with repeating phases. Consequently, the labelled sequence is eventually periodic **if and only if** some finite moment depth eventually separates every player pair. See [the finite-depth theorem](FINITE_DEPTH.md). The sufficient depth may depend on `N`; its existence for every `N ≥ 3` remains unproved.
- **Arithmetic criterion for closed two-player groups:** a nonmonomial parity ratio bounds their required comparison depth. A tie away from the global mean is a simpler sufficient test. The [exact experiments](research/STRUCTURE_EXPERIMENTS.md) establish this criterion for 54 components, covering all 988 of their tie phases. This proves those components' eventual periodicity, not the full sequences for their player counts.
- **Arithmetic criterion for interacting groups of any size:** [integer graph charges](research/NETWORK_CHARGES.md) are conserved under all compatible routing. Distinct initial charges exclude all future ties at the next moment. This is the criterion used in the new structural proofs, including a component of size 56 for `N = 60`.
- **General restriction on period lengths:** if an eventual period exists, every prime factor of its least individual-turn period is at most `N`. At separating depth `d`, that least period divides `2N · lcm(1,…,N)^d`. See [PERIOD_BOUND.md](PERIOD_BOUND.md).
- **No complete return to equal second moments:** for every `N > 2`, the canonical sequence never regains the initial all-equal second-moment state at a positive paired-block boundary. The [proof](research/BINARY_RESONANCE.md#21-exactly-when-the-complete-zero-state-can-return) uses the common recurrent sorting permutation. This excludes a complete reset, but leaves proper subsets of players to be handled.
- **A further conditional separation theorem:** exact [rank-count invariants](research/RANK_RIGIDITY.md) give conserved values at prime-power roots of unity. A nonzero value bounds comparison depth; small unresolved classes can then be treated by the binary criterion. See [cyclotomic separation](research/CYCLOTOMIC_SEPARATION.md). The uniform canonical hypotheses remain unproved.
- **Not established:** eventual periodicity for every integer `N > 2`, or guaranteed termination of a search for certificates.
- **Verification level:** a mathematical soundness argument plus an executable Python checker using arbitrary-precision integers. No Lean formalization is included.

These certificates establish infinite continuations. Observing many equal finite blocks alone would not do so: the data also includes an `N = 15` candidate that repeats 25 times before breaking.

## Run the verifier

Python 3 is sufficient; there are no third-party dependencies.
GitHub Actions runs the full word-certificate verifier and reproduces all structural certificates through N=64 on pushes and pull requests.

```sh
# Small, fully documented example
python3 fair_share_verify.py fair_share_certificates.json 3

# Selected cases
python3 fair_share_verify.py fair_share_certificates.json 3 4 15

# All 22 certificates, including reconstruction of the long prefixes
python3 fair_share_verify.py fair_share_certificates.json
```

Each successful case emits one JSON object. A wrong or unresolved comparison aborts verification. The checker reconstructs the greedy prefix from zero rather than trusting a supplied initial state; it rejects any noninitial tie unresolved by the moments it carries.

The structural checker does not require an explicit eventual player word. It discovers and proves the lower numerical regime, reconstructs the actual prefix, and verifies the conserved charges:

```sh
# New cases, without constructing their full eventual words
python3 research/structure_certificates.py 25 30 60

# Reproduce the complete structural range
python3 research/structure_certificates.py --range 3 64 --cap 1000000

# Negative control: reports an inconclusive charge test
python3 research/structure_certificates.py 2
```

Run ordinary Python, without `-O`. A search cap or an equal-charge group is reported as unproved, never as an aperiodicity result. These structural proofs do not calculate least periods or minimal preperiods for the new cases.

## Selected results

Lengths count individual turns. The preperiod is both the number of initial terms and the zero-based index where the permanent periodic tail starts.

| Players | Minimal preperiod | Least period |
|---:|---:|---:|
| 3 | 47 | 54 |
| 4 | 46 | 192 |
| 15 | 330741 | 48600 |
| 24 | 50652467 | 532224 |

The committed [verification report](fair_share_verification.json) contains all 22 cases and 494314 certified comparisons. Its `certified_from_index` is the convenient paired-block boundary used by the certificate; `minimal_preperiod_terms` is determined separately and can be smaller.

## Why the finite check proves an infinite tail

With `q = 1 − p = 1/(1 + z)`, multiply each player's accumulated score by the common positive factor `q^(-t)`. The greedy rule then compares the integer age moments

$$
M_{i,d}(t)=\sum_{s<t,\ a_s=i}\binom{t-s}{d}
$$

lexicographically, starting at degree zero.

Every block of `2N` turns is a permutation followed by its reversal. At block boundaries the zeroth and first moments agree, so the checker tracks moment differences of degrees 2, 3, and 4. Higher moments are irrelevant whenever those differences already determine a strict order.

For a fixed phase of a proposed period of length `L`, a normalized score difference satisfies

$$
F_{k+1}(z)=(1+z)^L F_k(z)+C(z),
$$

where `C` is independent of the repetition count `k`. At the first degree present in either `F_0` or `F_1`, its coefficient is exactly

$$
a+kb.
$$

Checking `a ≥ 0`, `b ≥ 0`, and the initial strict comparison proves the required order for every `k ≥ 0`. The checker applies this criterion to adjacent players at every phase. It also verifies the least period of the resulting cyclic word and finds the last prefix term that disagrees with its periodic continuation.

The complete derivation, including the initial degree-four tie for `N = 3`, is in [the English proof document](fair_share_proof.md). A [German translation](fair_share_proof.de.md) is also available.

## Repository contents

| File | Purpose |
|---|---|
| [fair_share_proof.md](fair_share_proof.md) | Canonical English proof: full mathematical argument, hand-checkable `N = 3` tables, all results, and references. |
| [fair_share_proof.de.md](fair_share_proof.de.md) | German translation of the proof. |
| [fair_share_verify.py](fair_share_verify.py) | Standalone exact prefix and all-future certificate checker. |
| [fair_share_certificates.json](fair_share_certificates.json) | Certificates for `N = 3, …, 24` and the temporary `N = 15` cycle example. |
| [fair_share_verification.json](fair_share_verification.json) | Recorded results of independent verification. |
| [NEXT_STEPS.md](NEXT_STEPS.md) | The unresolved mathematical step and a possible Lean formalization plan. |
| [RESEARCH_LOG.md](RESEARCH_LOG.md) | Intermediate proof attempts, checked lemmas, counterexamples, and historical-source updates. |
| [FINITE_DEPTH.md](FINITE_DEPTH.md) | Polynomial normal form for every fixed moment degree; eventual periodicity is equivalent to eventual bounded comparison depth. |
| [PERIOD_BOUND.md](PERIOD_BOUND.md) | A depth-dependent period bound and the theorem excluding prime factors larger than N from the least period. |
| [TIE_DYNAMICS.md](TIE_DYNAMICS.md) | Detailed worked reduction through degree four and the stronger degree-four separation conjecture. |
| [research/BINARY_COMPONENTS.md](research/BINARY_COMPONENTS.md) | Closed comparison groups, exact research scripts, and a targeted binary-component case inside `N = 78`. |
| [research/PARITY_OBSTRUCTION.md](research/PARITY_OBSTRUCTION.md) | A rigorous finite-depth criterion for closed binary components, including variable forcing. |
| [research/PARITY_RESONANCE.md](research/PARITY_RESONANCE.md) and [research/MEAN_OBSTRUCTION.md](research/MEAN_OBSTRUCTION.md) | The occupancy meaning of the exceptional parity case and a sufficient test using the global mean. |
| [research/STRUCTURE_EXPERIMENTS.md](research/STRUCTURE_EXPERIMENTS.md) | Reproducible checks, exact scope, and the larger comparison networks that remain to be treated. |
| [research/NETWORK_CHARGES.md](research/NETWORK_CHARGES.md) | Integer centering, graph potentials, conserved residues, and their relation to higher-depth component refinement. |
| [research/STRUCTURE_PROOFS.md](research/STRUCTURE_PROOFS.md) | Exact eventual-periodicity proofs for N=3,...,64 and the structural checker's soundness. |
| [research/INTERACTING_COMPONENTS.md](research/INTERACTING_COMPONENTS.md) | Exact two-gate models, reusable drift and residue lemmas, and counterexamples to overly broad extensions. |
| [research/BINARY_RESONANCE.md](research/BINARY_RESONANCE.md) | A common recurrent affine permutation, the period-two occupancy exclusion, and remaining binary obstacles. |
| [research/RANK_RIGIDITY.md](research/RANK_RIGIDITY.md) and [research/RANK_RIGIDITY_CHECKS.md](research/RANK_RIGIDITY_CHECKS.md) | The rank-count rigidity conjecture, its proved consequences, independent graph checks, and exact counterexamples to stronger versions. |
| [research/CYCLOTOMIC_SEPARATION.md](research/CYCLOTOMIC_SEPARATION.md) | A root-of-unity depth bound and a conditional reduction of interacting groups to closed pairs. |
| [research/TERMINAL_COMPONENTS.md](research/TERMINAL_COMPONENTS.md) | A necessary flat-generating-function condition for an infinite-depth obstruction, with examples explaining why it is insufficient. |
| [research/FORCING_IDENTITIES.md](research/FORCING_IDENTITIES.md) | Exact quadratic-weight identities and a conditional change of coordinates for unresolved comparison networks. |
| [research/RECIPROCAL_FORCING.md](research/RECIPROCAL_FORCING.md) | A positive polynomial rank-force basis and the simpler exact integer `(a,b,c)` recurrence through degree four, with limits of curvature and energy arguments. |
| [research/rank/README.md](research/rank/README.md) | Reproduction commands for the rank and cyclotomic experiments. |

## Continuing the work

The current main target is to prove that, for each fixed `N ≥ 3`, some finite degree `d(N)` eventually resolves every comparison. The [general reduction](FINITE_DEPTH.md) proves that this is equivalent to the desired periodicity. Degree four remains a stronger sufficient conjecture, but the reduction now works at every fixed degree.

The charge criterion now handles interacting groups of arbitrary size. The missing universal step is to prove that the **canonical** history forces sufficient charge separation, at degree four or after finitely many refinements. A second possible route is to prove rank-count rigidity and show that its cyclotomic signature classes eventually reduce to nonresonant pairs. Neither route's all-N hypotheses are established. The special origin is material: explicit altered prefixes and formal initial states defeat several broader versions of the claim. The [research log](RESEARCH_LOG.md) records these failed routes and the current arithmetic target.

Lean would be useful for formally verifying the certificate criterion and its connection to the original greedy rule. It is not required to reproduce the current results, and formalizing the existing finite cases would not prove the universal conjecture. See [next steps](NEXT_STEPS.md).
