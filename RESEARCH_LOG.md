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

## 2026-11-26 — Third checkpoint: exact rank invariants and limits of reset arguments

**Proved for all N>2:** the complete all-equal second-moment state never returns after the initial state. More generally, for strictly decreasing weights v, a zero return occurs exactly when `v_r + v_(N-1-r) = 2 mean(v)` for every rank. A return forces the common recurrent permutation to be reversal; its square is a translation, which must vanish on a finite orbit. Triangular weights fail the mirror-sum condition by N-2 between the first two ranks. This rules out a complete reset, not every proper tied group. See [BINARY_RESONANCE.md](research/BINARY_RESONANCE.md).

**Proved conditional arithmetic separation:** [cyclotomic rank charges](research/CYCLOTOMIC_SEPARATION.md) are exact integer invariants whenever the finite routing graph has rank-count rigidity. At a root of unity of prime-power order p^a dividing 2N, a nonzero fixed charge value bounds the order of cancellation at x=1 by the p-adic valuation of its algebraic norm. This gives a route to a finite depth bound without assuming degree four.

**Targeted applications:** all 27 labels in the large N=30 component and all 56 in the N=60 component have different cyclotomic signatures. The remaining classes in N=4,8,14 are pairs, and every relevant original lower tie is off the global second-moment mean. Finite-depth refinement and the physical binary criterion therefore finish these cases by a second structural argument. These are alternative proofs within the already established range, not additional full player-count cases.

**Exact finite binary certificates:** a reusable arbitrary-precision [difference-constraint checker](research/resonance/mean_pair_certificates.py) excludes closed binary mean ties on every integer recurrent second-moment cycle for every N=3,...,60, and for 237 specified values through N=259. Twenty other values through 259 and N=260 remain explicitly unestablished under the stated witness and search caps. Larger comparison components and pairs closed only at higher moments are outside this finite certificate's conclusion.

**Rank rigidity remains a conjecture:** expanded and independently contracted graph checks agree on the tested canonical networks. Rigidity would explain the factor 8N^2 in fourth-moment cycle moduli. A canonical N=5 transient already disproves the stronger claim that equal lower moments determine equal past rank counts. A realizable N=4 altered prefix disproves dependence on the second-moment cycle alone. Strictly convex weights `(27,18,10,5,2,0)` at N=6 also fail rank rigidity despite a zero initial state. See [RANK_RIGIDITY.md](research/RANK_RIGIDITY.md) and its [independent checks](research/RANK_RIGIDITY_CHECKS.md).

**Necessary condition, not a reset theorem:** an infinite-depth terminal component has bounded discrepancies in every fixed age moment, hence [flat signed generating functions](research/TERMINAL_COMPONENTS.md) at q=1. Explicit multicolor Prouhet constructions have the same property without obeying the greedy rule. Even prescribed finite prefixes admit such completions when greediness is dropped. Therefore flatness, moment bounds, and allowed period primes cannot establish the missing origin reset.

**Further failed shortcut:** common recurrent affine permutations and strict convexity do not exclude even the oriented first-two-block pattern. The binary note gives an exact ten-player rational fixed point satisfying that pattern for modified convex weights. Any successful exclusion must use the exact triangular weights or additional canonical reachability information.

**Descent attempt:** exact equal rank-charge vectors allow one integral change of coordinates dividing by x^(2N)-1 and reducing the degree of a fixed physical prefix. But the new forcing is a vertex potential, not another rank-only forcing. An exact N=8 counterexample shows that this potential already has nonzero next holonomy. Repeated descent therefore requires a new invariant or a justified refinement step; it does not follow from the first rank-rigidity test. See [FORCING_IDENTITIES.md](research/FORCING_IDENTITIES.md).

**Simpler exact coordinates:** [RECIPROCAL_FORCING.md](research/RECIPROCAL_FORCING.md) proves the update `a' = a + binom(N-r,2)`, `b' = b + a`, `c' = c + 4N^2 b + binom(N-r+1,4)`, starting at zero. Lexicographic comparison of `(a,b,c)` is exactly the original comparison through degree four. Two symbolic derivations and independent prefix comparisons with the original moment updater agree; the N=2 control reaches an unresolved degree-four tie at block 8. A reciprocal Gaussian-binomial force basis explains the quartic reward. Positive force curvature alone cannot prove separation: an abstract two-slot restriction still normalizes to the Thue-Morse recurrence. The proposed reciprocal quadratic energy also lacks the positivity needed for a monotonicity proof.

The remaining all-N target is unchanged: prove eventual separation at some finite depth for each canonical N>=3. The new invariants identify possible sufficient hypotheses and provide complete finite certificates, but their uniform validity is not proved. No universal-periodicity theorem is claimed at this checkpoint.
