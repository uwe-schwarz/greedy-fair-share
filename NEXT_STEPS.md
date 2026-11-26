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

The missing implication is from the repeating **unlabelled second-moment configuration** to a repeating **labelled greedy sequence**. Equal second moments are resolved by higher moments, and those can change the player order. The two-player Thue–Morse sequence prevents treating the finite lower-moment state space as a proof by itself.

A sufficient next theorem would show that every `N ≥ 3` eventually reaches a tail accepted by an appropriate finite-moment certificate checker. Neither a universal bound on the required moment degree nor termination of that search has been proved here. Degree four is sufficient for the supplied certificates, not an established bound for arbitrary `N`.

## 2. Preserve exact certification when exploring further

Candidate discovery and proof checking have different roles. New searches may propose a prefix and period, but acceptance should still require exact prefix reconstruction and a proof of every future comparison.

Useful research records for new cases include:

- the certificate start and proposed period;
- the moment degree needed for prefix and tail comparisons;
- the first relevant coefficient `a + kb` at every comparison;
- an explicit negative-slope witness when an apparently stable cycle fails;
- the earliest mismatch with a proposed periodic continuation.

The current checker deliberately rejects a comparison unresolved through degree four. Such rejection means the checker has not established the candidate, not that the sequence is aperiodic. It must not be replaced by arbitrary tie breaking.

The `N = 15` example in the certificate data is a useful reference: a length-8100 candidate repeats 25 times but fails because a decisive coefficient is `30317118 − 1215000k`. This distinguishes a long transient from an infinite periodic tail.

## 3. Optional Lean formalization

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

## 4. Keep the research record clear

For each extension, distinguish a proposed candidate, an accepted exact certificate, and a formalized theorem. Retain the model definition and indexing convention next to the result. Refer to the full proof document for the original sources and historical context; the present repository does not claim priority for previously documented observations.
