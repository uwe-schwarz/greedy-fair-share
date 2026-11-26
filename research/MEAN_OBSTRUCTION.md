# A mean-load obstruction to binary parity resonance

Research derivation, 2026-11-26. This supplies a cheap sufficient test for the nonmonomial hypothesis of the binary parity criterion. It is not an exclusion theorem for every N.

## 1. Absolute triangular loads

Let B=2N and let v_r=binom(N-r,2), for 0 <= r < N. Define integer loads

$$
\ell_i(0)=0,\qquad \ell_i(m+1)=\ell_i(m)+v_{r_i(m)}.
$$

Their differences are half the second-moment differences. The normalized sorted values x_i=ell_i-min ell are exactly the finite-state second-moment system.

Because every block assigns every rank once,

$$
\sum_i\ell_i(m)=m\sum_{r=0}^{N-1}v_r,
\qquad
\overline\ell(m)=m\mu,
\qquad \mu=\frac{N^2-1}{6}.
$$

The proved bound on the spread of normalized second moments implies that ell_i(m)-m mu is bounded for every player, uniformly in m for fixed N.

## 2. Necessary mean condition for a resonant closed pair

**Proposition.** Fix a closed binary comparison component and a phase m_0 at which its two second moments agree. If that phase has monomial parity ratio R/K, then the common second-moment load of the pair equals the mean load of all N players. Equivalently, in the normalized state at that phase,

$$
x_a=x_b=\frac1N\sum_i x_i. \tag{1}
$$

Thus a binary tie strictly above or below the global mean is automatically nonmonomial and has a uniform finite comparison-depth bound from the [parity criterion](PARITY_OBSTRUCTION.md).

**Proof.** The [physical resonance lemma](PARITY_RESONANCE.md) proves that a monomial ratio forces the pair's occupancy pattern to be periodic from turn zero with a period Bp, where p divides both the base period P and the prefix length m_0 in paired blocks. Because a player's two turn positions in a paired block determine its rank, the unordered pair of assigned ranks is therefore periodic from block zero with period p.

Let A be the sum of v_r over those two ranks during one p-block period. At every complete such period,

$$
\ell_a(kp)+\ell_b(kp)=kA.
$$

The two labels may exchange ranks, but their sum does not depend on the exchange. The bounded-spread property implies

$$
\ell_a(kp)+\ell_b(kp)-2kp\mu=O(1).
$$

Therefore A=2p mu. Since p divides m_0, the pair's sum at the selected phase is 2m_0 mu. The phase is a second-moment tie, so the two loads are equal and each is m_0 mu, the global mean. Subtracting the common minimum proves (1). ∎

This condition is only necessary for resonance. A pair at the global mean may still be nonmonomial because its earlier occupancy does not match the periodic continuation.

## 3. A special arithmetic exclusion

**Corollary.** If N >= 3 and gcd(P,m_0)=1 at a binary tie phase, then the phase is nonmonomial.

**Proof.** Monomial resonance would give p=1 in the physical resonance lemma. The unordered rank pair would therefore be the same in every paired block from block zero onward.

The initial permutation is the canonical order, and the next paired block's permutation is its reversal, because the first block gives strictly decreasing second-moment rank weights. Hence a fixed unordered rank pair must be symmetric under r -> N-1-r.

At a closed binary tie, the two equal second moments occupy adjacent ranks. The fixed rank pair must therefore be the two central ranks, and N must be even. For N >= 4 these are {N/2-1,N/2}.

After the first two blocks, a player initially at rank r has triangular load

$$
v_r+v_{N-1-r}=\binom{N-r}{2}+\binom{r+1}{2}.
$$

This strictly convex symmetric quadratic is minimized precisely at the two central ranks when N is even. Thus those two players occupy ranks {0,1} in the third block. This differs from their original central rank pair for every N >= 4, a contradiction. For odd N, no symmetric adjacent pair existed in the first place. Only N=2 avoids the contradiction. ∎

To certify an entire component using this corollary alone, the condition must hold at every phase where the two second moments tie. Alternatively, combine it with the general parity test or the mean obstruction for the other phases.

## 4. Exact finite enumeration

[mean_cycle_probe.py](mean_cycle_probe.py) exhaustively enumerates every sorted normalized integer state with spread at most binom(N,2), for N=3,...,7. This is the complete finite state space used in the second-moment bound, not just the orbit reached from zero.

| N | Enumerated states | Distinct cycles | Closed binary components tied at the global mean |
|---:|---:|---:|---:|
| 3 | 10 | 1 | 0 |
| 4 | 84 | 3 | 0 |
| 5 | 1001 | 8 | 0 |
| 6 | 15504 | 1 | 0 |
| 7 | 296010 | 123 | 0 |

The machine-readable report is [mean_cycle_probe.json](mean_cycle_probe.json). These finite checks support a structural conjecture; they do not prove the absence of such components for arbitrary N. Integrality matters: an exact rational N=4 cycle outside this integer lattice can have a closed binary component tied at the global mean.

The useful universal subproblem is now narrower: can a closed binary component for N>=3 contain the particular mean-level, phase-aligned occupancy resonance described above? Excluding such components would settle all binary components at once, even when their deciding degree is greater than four. Components with more than two labels require additional arguments.

## Reproducible checks and a limitation

The [component experiments](STRUCTURE_EXPERIMENTS.md) verify the off-mean condition at all 988 tie phases of the 54 investigated binary components for N>2. The two-player control ties at the mean.

The exact script [mean_cycle_probe.py](mean_cycle_probe.py) enumerates every normalized integer state within the proved spread bound for N=3,...,7. It also verifies a rational N=4 counterexample outside the integer-difference lattice. The [recorded results](mean_cycle_probe.json) therefore provide both finite evidence for the integer conjecture and a reason that integrality cannot be discarded. They are not an all-N proof.
