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
4. The unlabelled dynamics through degree four has an eventual polynomial form with repeating phases, using the normalizations proved in [moment dynamics](TIE_DYNAMICS.md). This uses Kohlberg's invariant-half-line theorem and a finite-lattice argument.

The new reduction gives a concrete sufficient next theorem: for every `N ≥ 3`, there is a paired-block time after which distinct players always have distinct triples `(M₂, M₃, M₄)`. Once this is proved, the phasewise routing of labels becomes periodic; a finite power of its permutation restores every label. Section 11 of the research note gives the precise quantified statement and proof of this implication.

**This separation theorem is not proved.** Degree four suffices for the supplied certificates but is not an established bound for arbitrary `N`. The condition is also not claimed to be necessary: an eventually periodic sequence could still require higher moments to resolve some decisions. The two-player Thue–Morse sequence fails finite-degree separation and remains a necessary check on any proposed universal argument.

An alternative sufficient theorem would guarantee that every `N ≥ 3` eventually reaches a tail accepted by an exact finite-moment certificate checker. Termination of such a search remains unproved.

## 2. Analyze the recurring tie groups

The most direct next work is to study exact ties inside the now-understood lower-moment dynamics:

1. **Build the periodic comparison structure.** Compute the second-moment cycle and its possible player movements between equal-value groups. Record which groups of player positions remain closed under these movements.
2. **Extract the affine and quadratic regimes.** Use the proved coordinate changes to remove common growth. Identify the persistent ties through degree three, then through degree four. Record actual integer coefficients and exact equalities.
3. **Seek a separation invariant.** A modular obstruction to simultaneous equalities or a strictly decreasing integer quantity could prove that the degree-four tie cases cannot recur indefinitely from the canonical zero initial state. Neither obstruction has yet been established.
4. **Test the proposed statement directly.** Carry additional moment coefficients when degree four ties. Record the smallest deciding degree, the closed group involved, and the complete return map. A degree-four tie would challenge the strongest bound; it would not by itself disprove eventual separation or eventual periodicity.

The [component study](research/BINARY_COMPONENTS.md) provides an exact graph construction, an elementary binary return-map lemma, a structural derivation for `N = 7`, and a targeted `N = 78` example. In that example, one closed pair first needs degree four at turn index 3020004; its later behavior can be certified algebraically without generating billions of turns. This establishes that component's behavior, not the full `N = 78` sequence.

There is a useful algebraic lead. For `B = 2N`, rank-weight differences satisfy

$$
\Delta w_4=\frac{1}{12}\Delta\bigl(w_2^2+(B^2-6B+4)w_2\bigr).
$$

The fourth rank weight is a strictly convex quadratic function of the second rank weight, up to a common constant. Three or more available rank weights give information that is absent from a two-point weight set. This is a possible ingredient for a separation argument, not a proof: contributions along different histories may still cancel.

The binary false-start paper offers another model for the missing step. Its coefficient-cancellation process eventually leaves a nonzero arithmetic remainder for a non-Thue–Morse prefix. An analogous obstruction for a recurring multiplayer tie group would be useful. Its theorem cannot be applied merely by deleting other players' turns, because deletion changes the time exponents. See Khovanova and Madhavarapu, [*Fair Duels after a False Start*](https://arxiv.org/html/2610.00880v1), Theorems 1.1 and 4.6.

If degree four does not yield eventual separation for all N, the next mathematical task is to extend the moment normal form to higher fixed degrees and establish a sufficient degree depending on N. An all-degree induction is not included in the current proof.

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

## 5. Keep the research record clear

For each extension, distinguish a proposed candidate, an accepted exact certificate, and a formalized theorem. Retain the model definition and indexing convention next to the result. Refer to the full proof document for the original sources and historical context; the present repository does not claim priority for previously documented observations.
