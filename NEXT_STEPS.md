# Next steps

The [English proof](fair_share_proof.md) is the canonical version. Update it first when extending or correcting the argument, then synchronize the [German translation](fair_share_proof.de.md).

## 1. Isolate the missing universal theorem

The available certificates prove eventual periodicity separately for every `N = 3, …, 24`. The open target is

$$
\forall N\ge3,\quad\exists H,L>0,\quad
\forall t\ge H,\ a_{t+L}=a_t.
$$

Current general results establish:

1. Every paired round has the form `π reverse(π)`.
2. The sorted second-moment differences, after subtracting their minimum and dividing by two, lie in a finite state space and eventually repeat.
3. A proposed periodic tail can be certified by finitely many exact coefficient comparisons.
4. At **every fixed moment depth**, the unlabelled dynamics has an eventual polynomial form with repeating phases. The [general induction](FINITE_DEPTH.md) uses polynomial transport along a finite graph, Kohlberg's invariant-half-line theorem, and a finite-lattice argument.
5. Eventual periodicity is **equivalent** to eventual separation at some finite moment depth. The depth may depend on N.

The exact remaining target can therefore be written as

$$
\forall N\ge3\;\exists d,m_0\;\forall m\ge m_0\;\forall i\ne j,
\qquad (M_{i,0}(m),\ldots,M_{i,d}(m))
\ne (M_{j,0}(m),\ldots,M_{j,d}(m)).
$$

Here m counts paired blocks of 2N turns. If a finite depth separates all players, its eventual polynomial profiles determine periodic routing of labels. A finite power of the routing permutation restores every label. Conversely, a periodic player word has a first distinguishing coefficient bounded uniformly over its finitely many phases and player pairs. Both directions are proved in [FINITE_DEPTH.md](FINITE_DEPTH.md).

**The existence of such a finite depth for every N >= 3 is not proved.** Degree four suffices for the supplied certificates and remains a stronger sufficient conjecture. We no longer need a new normal-form argument if a higher degree is required. The two-player Thue–Morse sequence fails every finite-depth separation condition and remains a necessary check on a universal argument.

An alternative sufficient theorem would guarantee that every `N ≥ 3` eventually reaches a tail accepted by an exact finite-moment certificate checker. Termination of such a search remains unproved.

## 2. Extend the arithmetic obstruction to interacting groups

The [parity theorem](research/PARITY_OBSTRUCTION.md) now supplies an arithmetic obstruction for a closed two-player component. Modulo two, its score difference becomes the indicator of the turns occupied by either player. That union is independent of the internal ordering of the two labels. Its fixed affine recurrence bounds the comparison depth unless a rational-function ratio is a Laurent monomial.

The [physical interpretation](research/PARITY_RESONANCE.md) shows that this monomial exception requires the pair's occupancy to have been periodic from turn zero, aligned with the selected prefix and base period. At a second-moment tie it also requires both players to be at the global mean load. Thus an [off-mean tie](research/MEAN_OBSTRUCTION.md) gives a simpler sufficient test. All 988 tie phases of the 54 investigated N>2 binary components pass it. These are component theorems, not complete new player-count cases; see [the exact scope](research/STRUCTURE_EXPERIMENTS.md).

The next mathematical tasks are:

1. **Treat networks of changing pairs.** The persistent third-moment comparison graph already contains a component of size three for N=8 and one of size fourteen for N=14. Every instantaneous tie in these examples has size two, but the same player can meet different partners. A fixed pair's union of turns is then no longer independent of the other comparisons. We need an invariant or arithmetic argument for the whole interacting component. The [exact graph calculations](research/THIRD_COMPONENTS.md) give small concrete cases for testing such a lemma.
2. **Resolve the exceptional closed binary case.** Prove that the canonical integer dynamics cannot produce the mean-level, phase-aligned occupancy resonance, or show that integer information beyond parity still bounds its depth. Exhaustive checks of the complete integer state spaces for N=3,...,7 find no binary mean ties. An explicit rational N=4 counterexample shows why a proof must retain integrality or canonical reachability. This remains a conjectural structural step.
3. **Test degree four without assuming it.** Carry additional moment coefficients whenever degree four ties. Record the first deciding degree, the component, and the complete return map. A degree-four tie challenges the stronger bound; it does not refute eventual periodicity. The correct target is a finite bound depending on N.

The [component study](research/BINARY_COMPONENTS.md) provides an exact graph construction, an elementary binary return-map lemma, a structural derivation for `N = 7`, and a targeted `N = 78` example. In that example, one closed pair first needs degree four at turn index 3020004; its later behavior can be certified algebraically without generating billions of turns. This establishes that component's behavior, not the full `N = 78` sequence.

There is a useful algebraic lead. For `B = 2N`, rank-weight differences satisfy

$$
\Delta w_4=\frac{1}{12}\Delta\bigl(w_2^2+(B^2-6B+4)w_2\bigr).
$$

The fourth rank weight is a strictly convex quadratic function of the second rank weight, up to a common constant. Three or more available rank weights give information that is absent from a two-point weight set. This is a possible ingredient for a separation argument, not a proof: contributions along different histories may still cancel.

The binary false-start paper offers another model for the missing step. Its coefficient-cancellation process eventually leaves a nonzero arithmetic remainder for a non-Thue–Morse prefix. An analogous obstruction for a recurring multiplayer tie group would be useful. Its theorem cannot be applied merely by deleting other players' turns, because deletion changes the time exponents. See Khovanova and Madhavarapu, [*Fair Duels after a False Start*](https://arxiv.org/html/2610.00880v1), Theorems 1.1 and 4.6.

The new all-fixed-degree induction has completed the normal-form part of this route. The work left is to bound the depth of the unresolved comparison networks, not to reprove the reduction at each degree.

## 3. Preserve exact certification when exploring further

Candidate discovery and proof checking have different roles. New searches may propose a prefix and period, but acceptance should still require exact prefix reconstruction and a proof of every future comparison.

Useful research records for new cases include:

- the certificate start and proposed period;
- the moment degree needed for prefix and tail comparisons;
- the first relevant coefficient `a + kb` at every comparison;
- an explicit negative-slope witness when an apparently stable cycle fails;
- the earliest mismatch with a proposed periodic continuation.

The current checker deliberately rejects a comparison unresolved through degree four. Such rejection means the checker has not established the candidate, not that the sequence is aperiodic. It must not be replaced by arbitrary tie breaking.

The `N = 15` example in the certificate data is a useful reference: a length-8100 candidate repeats 25 times but fails because a decisive coefficient is `30317118 − 1215000k`. This distinguishes a long transient from an infinite periodic tail.

## 4. Optional Lean formalization

Lean is an additional assurance step. The existing work is a written mathematical proof with exact executable certificates; the Python checker itself is not a Lean-verified implementation.

A focused formalization should begin with the reusable soundness argument:

1. **Define the rule precisely.** Encode finite player words and comparison of their score polynomials near `q = 1` from below. Preserve the termwise-limit interpretation and the initial numbering convention.
2. **Prove the age-moment equivalence.** Establish the change of variable `q = 1/(1 + z)` and lexicographic comparison of binomial coefficients. Prove the triangular update identities.
3. **Prove the paired-round lemma.** Derive equal zeroth and first moments at block boundaries and the permutation/reversal structure.
4. **Prove the two-cycle lemma.** From `F_(k+1) = (1 + z)^L F_k + C`, derive the affine first relevant coefficient and the conditions ensuring every comparison remains strict for all natural `k`.
5. **Prove checker soundness.** Connect accepted finite certificate data to the actual greedy continuation. Include strict-order and unresolved-tie conditions; a certificate should never be accepted merely because two observed words match.
6. **Instantiate `N = 3` first.** Its small closed cycle is a manageable end-to-end formal theorem. Extend to other certificate data after the general checker theorem is established.

Minimal period and minimal preperiod are separate claims from eventual periodicity. If they are included in the formal statements, the cyclic-word period check and the last-prefix-mismatch argument also need proofs.

For the larger cases, choose a proof-producing or otherwise explicitly justified computation path, and document its trusted assumptions. Importing the Python result as an assertion would not formally verify the computation.

Formalizing these results would strengthen confidence in the current finite-case proofs. It would leave the universal existence theorem in section 1 as a distinct mathematical task.

The polynomial-transport lemma in [FINITE_DEPTH.md](FINITE_DEPTH.md), section 4, is another compact candidate for formalization: a unipotent matrix recurrence on a finite graph forces all time-dependent polynomial terms to agree inside a closed component. Formalizing the whole fixed-depth induction would additionally require the nonexpansive piecewise-affine theorem or a replacement proof.

## 5. Keep the research record clear

For each extension, distinguish a proposed candidate, an accepted exact certificate, and a formalized theorem. Retain the model definition and indexing convention next to the result. Refer to the full proof document for the original sources and historical context; the present repository does not claim priority for previously documented observations.
