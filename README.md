# Greedy Fair-Share Sequences

[![Verify certificates](https://github.com/uwe-schwarz/greedy-fair-share/actions/workflows/verify.yml/badge.svg)](https://github.com/uwe-schwarz/greedy-fair-share/actions/workflows/verify.yml)

Exact eventual-periodicity certificates for the multiplayer greedy duel rule discussed in Stand-up Maths' [*Taking turns isn't fair. We fixed it.*](https://www.youtube.com/watch?v=pOSSpd8mb4Y).

At each turn, give the next opportunity to the player with the smallest probability of having won so far, in the **termwise limit** as the common hit probability tends to zero.

English is the canonical language for the documentation. The [full proof](fair_share_proof.md) uses the default filename; the [German translation](fair_share_proof.de.md) is retained separately. Make substantive updates to the English version first, then update translations.

## Research status

- **Established for each `N = 3, …, 24`:** an exact finite certificate proves the proposed tail follows the greedy rule for every future repetition.
- **Written out by hand for `N = 3`:** the proof exhibits a closed nine-block cycle, giving least period 54 after 47 initial terms.
- **General reduction for every `N ≥ 2`:** the unlabelled moment dynamics through degree four eventually has a polynomial form with repeating phases. Eventual strictness through degree four would therefore imply labelled periodicity. See [moment dynamics](TIE_DYNAMICS.md) for the proof and the remaining separation conjecture.
- **Not established:** eventual periodicity for every integer `N > 2`, or guaranteed termination of a search for certificates.
- **Verification level:** a mathematical soundness argument plus an executable Python checker using arbitrary-precision integers. No Lean formalization is included.

These certificates establish infinite continuations. Observing many equal finite blocks alone would not do so: the data also includes an `N = 15` candidate that repeats 25 times before breaking.

## Run the verifier

Python 3 is sufficient; there are no third-party dependencies.
GitHub Actions runs the full verifier on pushes and pull requests.

```sh
# Small, fully documented example
python3 fair_share_verify.py fair_share_certificates.json 3

# Selected cases
python3 fair_share_verify.py fair_share_certificates.json 3 4 15

# All 22 certificates, including reconstruction of the long prefixes
python3 fair_share_verify.py fair_share_certificates.json
```

Each successful case emits one JSON object. A wrong or unresolved comparison aborts verification. The checker reconstructs the greedy prefix from zero rather than trusting a supplied initial state; it rejects any noninitial tie unresolved by the moments it carries.

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
| [TIE_DYNAMICS.md](TIE_DYNAMICS.md) | General moment reduction through degree four, a conditional periodicity theorem, and the precise remaining separation problem. |
| [research/BINARY_COMPONENTS.md](research/BINARY_COMPONENTS.md) | Closed comparison groups, exact research scripts, and a targeted binary-component case inside `N = 78`. |

## Continuing the work

The current main target is an eventual separation theorem: for every `N ≥ 3`, show that no two players keep the same second, third, and fourth moments at arbitrarily late paired-block boundaries. The [new reduction](TIE_DYNAMICS.md) proves that this condition would imply the desired periodicity. The condition is sufficient and remains unproved; if degree four does not suffice, the reduction must be extended to higher moments.

Lean would be useful for formally verifying the certificate criterion and its connection to the original greedy rule. It is not required to reproduce the current results, and formalizing the existing finite cases would not prove the universal conjecture. See [next steps](NEXT_STEPS.md).
