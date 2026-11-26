# Exact structural proofs for N=3,...,64

Date: 2026-11-26. For every integer N in this finite range, the method below proves eventual periodicity of the canonical greedy sequence. It does not prove the statement for arbitrary N. It does not compute new least periods or minimal preperiods.

## 1. What the checker establishes

The proof combines [the graph-charge theorem](NETWORK_CHARGES.md) with the [finite-depth normal form](../FINITE_DEPTH.md). It uses moments through degree four, but it does not assume that the whole labelled word is periodic while finding the lower regime.

At paired-block boundaries, let x be the sorted normalized second-moment loads, and let y be the integer third coordinate, initially zero, with the exact update

$$
x_i'=x_i+\binom{N-r_i}{2}-\min_j\left(x_j+\binom{N-r_j}{2}\right),
\qquad y_i'=y_i+x_i.
$$

Sorting these pairs gives a closed unlabelled numerical evolution. Higher moments choose labels at a tie and cannot change the sorted numerical multiset.

The checker establishes five facts:

1. **An exact lower regime.** It proposes a phase period P and a vector slope. At every phase it checks that each required third-coordinate inequality has nonnegative intercept and nonnegative slope, transports the slopes through the sorting operation, and verifies the exact affine return after P blocks. Those identities prove the proposed lower regime for every future repetition.
2. **Persistent ties only.** It moves one full period forward. Any initial equality of different affine profiles is then strict. The remaining tied groups are polynomial identities, so the phase/rank routing graph includes exactly the lower-compatible choices needed for the subsequent proof.
3. **Integer next-moment increments.** For a closed component C of size s, use W_i=s M_(i,4)-sum_(a in C) M_(a,4). The common lower slope cancels. The increment in W is therefore an exact integer constant for each phase/rank slot.
4. **Conserved charges.** A graph potential h and the gcd g of all closed-walk increments give the invariant W_i-h_v modulo g; when g=0 it is an exact integer invariant. Comparator slots have congruent potentials. Distinct charges therefore exclude every future fourth-moment tie, for all compatible higher routing choices.
5. **The genuine initial charges.** A separate reconstruction of the canonical labelled prefix supplies the fourth moments at entry. Every noninitial prefix comparison must be strict through degree four. An unresolved comparison aborts this part of the proof; it is never silently decided by label number.

Every component passed the distinct-charge test for N=3,...,64. Hence every sufficiently late comparison is resolved through degree four. The finite-depth theorem then proves eventual labelled periodicity.

The recorded `lower_regime_start_blocks` is the start of the proved lower regime and fourth-depth bound. It is **not** asserted to be the minimal preperiod of the player word, or even the first block of its eventual periodic tail. The fourth numerical ordering may have a further finite transient.

## 2. Results and scope

The complete machine-readable record is [structure_verification.json](structure_verification.json). It includes the lower-regime start, phase period, component sizes, graph moduli, and conserved charges.

| N | Lower-regime start, paired blocks | Lower phase period, paired blocks | Largest recorded component |
|---:|---:|---:|---:|
| 25 | 523 | 210 | 2 |
| 30 | 13230 | 1620 | 27 |
| 32 | 28042 | 512 | 5 |
| 48 | 42106 | 2592 | 27 |
| 60 | 373908 | 9600 | 56 |
| 62 | 402699 | 327600 | 3 |
| 64 | 226343 | 225420 | 1 |

The short numerical phase period can make a graph component contain several labels purely because a deterministic permutation rotates them across successive periods. Such a component is harmless for a successful charge test. Therefore these component sizes need not match a graph unfolded over a full labelled period, and are not all counts of genuinely interacting labels.

The N=2 control fails the separation test, as required by its Thue-Morse continuation. The initial search cap of 200000 blocks was reached for N=60,62,64. Increasing that cap to 1000000 resolved all three. The cap is a resource limit, not a mathematical stopping bound for arbitrary N.

The earlier explicit word certificates for N=3,...,24 remain independently available. The new method proves eventual periodicity for the additional N=25,...,64 cases without generating their complete repeating words.

## 3. Reproduction

From the repository root, using Python 3 and its standard library:

```sh
python3 research/structure_certificates.py --range 3 64 --cap 1000000
python3 research/structure_certificates.py 2
```

Do not use `-O`; the script explicitly rejects it. A successful case emits `PROVED EVENTUALLY PERIODIC`. A search cap, an unresolved prefix comparison, or equal charges is explicitly inconclusive. Equal charges do not prove that any actual tie occurs.

The implementation keeps a small constraint graph on the reference wires rather than every phase/rank vertex. Along a wire, integrate its edge increments. A comparator equates the two potentials at that phase; the end-of-period permutation connects each wire back to its phase-zero slot. These relations retain every closed-walk increment of the expanded graph. A weighted union-find constructs potentials and their residual gcds.

The expanded-graph implementation is retained as `charge_test_expanded` for independent comparison. Its moduli and charge differences agree exactly with the contracted graph on N=2,3,4,8,12,14,25,30, including deterministic monodromy and a large interacting component. A second implementation based on explicit graph breadth-first traversal independently reproduces all 31 nontrivial components of the old labelled certificates; see [network8_lattice_probe.py](networks/network8_lattice_probe.py).

## 4. What an all-N proof still needs

This is a general sufficient certificate with 62 proved instances. The search's termination and success are not established uniformly in N. The normal-form theorem guarantees a finite lower regime, but it does not force the fourth charges to be distinct. A universal proof must explain why the canonical history supplies enough separation at degree four or after finitely many higher-degree refinements.
