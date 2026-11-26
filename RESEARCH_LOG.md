# Research log

English is canonical. Entries distinguish proved statements, exact finite checks, and approaches that remain conjectural. The objective is eventual periodicity of the canonical greedy sequence for every integer N >= 3.

## 2026-11-26 — Universal-proof investigation, first checkpoint

Starting point: commit `61cd578` proves the fixed-depth normal form and finite-depth equivalence, supplies the binary parity and mean criteria, and records the component experiments. The all-N bounded-depth statement is not yet proved.

Three complementary lines are being investigated:

1. **Interacting components.** Derive a reusable arithmetic obstruction for a periodic network of pair comparisons. The three-player persistent component inside N=8 is the smallest known concrete test case. A fixed pair's occupancy invariant does not survive a change of partners, so applying the binary theorem separately to instantaneous pairs is invalid.
2. **Binary resonance.** Exclude the phase-aligned, purely periodic pair occupancy required by the monomial exception, using the canonical initial state and integer triangular loads. The stronger claim that every integer base cycle lacks a binary mean tie is also being tested. The known rational N=4 counterexample prevents an argument that discards integrality.
3. **An infinite hierarchy of ties.** Investigate whether persistent nontrivial components at every moment degree force an exceptional substitution or occupancy structure. The finite-depth theorem alone cannot exclude this, as N=2 demonstrates. Any argument must justify compatibility between the component partitions and phase periods at different depths.

No universal conclusion follows from these proposed routes yet. Intermediate lemmas and counterexamples will be added here as they are checked.

### Earlier observation found in a primary source

The historical observation predates the 2017 OEIS entry: in a comment dated **2012-11-01** on Zachary Abel's [*Dueling Dilettantes*](https://blog.zacharyabel.com/2012/02/dueling-dilettantes/), Anders Kaseorg reports eventual periods 54, 192, 500, and 864 for 3, 4, 5, and 6 players. The comment reports computation and supplies no all-N proof. The post itself is dated 2012-02-11; that is not the date of the multiplayer comment.

The [binary false-start paper](https://arxiv.org/html/2610.00880v1) proves an arithmetic termination theorem for two players after a noncanonical prefix. Its modulo-four argument uses the eventual decomposition into adjacent opposite-sign pairs. A multiplayer extension must establish an analogous decomposition; deleting other players' turns changes the time exponents and does not justify importing that theorem.

## 2026-11-26 — Second checkpoint: interacting groups and complete proofs through N=64

**Proved:** [integer graph charges](research/NETWORK_CHARGES.md) give a next-moment separation criterion for a component of any size. Centering over a component cancels the common polynomial growth and leaves integer edge increments. The gcd of closed-walk costs defines conserved residues. Distinct residues rule out every future unresolved comparison, including comparisons between changing partners.

**Exact finite applications:** the independently generated [structural certificates](research/STRUCTURE_PROOFS.md) pass for every N=3,...,64, including a 56-slot component for N=60. They reconstruct the genuine prefix and verify the lower affine regime for all future repetitions. They do not use a pre-existing repeating player word. The N=2 control is inconclusive. N=60,62,64 required raising the discovery cap from 200000 to 1000000 blocks; the first cap was not evidence against periodicity.

**Proved:** the [period bound](PERIOD_BOUND.md) restricts an eventual least period to prime factors at most N. At separating depth d, it divides `2N * lcm(1,...,N)^d`. The proof uses Euclidean nonexpansiveness and the fact that a periodic orbit of a piecewise coordinate permutation is governed by one coordinate permutation on its convex hull.

**Proved examples and reusable lemmas:** [two-gate networks](research/INTERACTING_COMPONENTS.md) yield a strict drift cut for the N=8 triple and a balanced max-subtraction rule for the N=12 triple. A binary component arising at any fixed lower level can use the physical parity criterion. For the specific N=8 lower profile, a drift cut followed by off-mean binary tests proves termination for every entering state arising from a paired-palindrome history.

**Proved binary reductions:** [BINARY_RESONANCE.md](research/BINARY_RESONANCE.md) gives one affine permutation on the recurrent second-moment set and excludes origin-aligned binary occupancy of period two. An initially proposed shortcut—forcing each individual load to return to zero after one occupancy period—was invalid; the corrected proof uses rank positions and the pair's total load.

**Failed stronger statements:** a realizable altered N=4 prefix produces a third-level network with graph modulus 4 and coincident charges. Thus the large moduli seen in canonical cases do not follow merely from the triangular weights or physical turn counts. The exact N=8 formal network also admits a Thue-Morse-type orbit for arbitrary, unrealizable entering germs. These examples identify where a universal proof must use the canonical history.

**Still open:** eventual bounded comparison depth for every N>=3. Success through N=64 and the new period restriction are not substitutes for this quantified step. The next investigation is the stronger observed rigidity of rank counts on the canonical third-level graphs and whether it yields a universal separation argument.
