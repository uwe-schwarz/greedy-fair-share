# Toward all N: moment dynamics and the remaining separation problem

Date: 2026-11-26. English is the canonical version of this research note.

**Extension:** [FINITE_DEPTH.md](FINITE_DEPTH.md) now proves the corresponding normal form at every fixed moment degree, and proves that eventual periodicity is equivalent to eventual separation at some finite degree. This note retains the detailed degree-three and degree-four calculations.

**Simpler coordinates:** [RECIPROCAL_FORCING.md](research/RECIPROCAL_FORCING.md) gives an equivalent integer update through degree four: `a' = a + binom(N-r,2)`, `b' = b + a`, and `c' = c + 4N^2 b + binom(N-r+1,4)`. It proves the exact triangular conversion between these coordinates and the original age moments. The formulas below remain valid in their original gauges.

**Result established here:** for every N >= 2, the unlabelled moment dynamics through degree four has an eventual polynomial form with finitely many repeating phases, after the stated common normalizations. Consequently, if comparisons are eventually strict through degree four, the labelled greedy sequence is eventually periodic.

**Not established:** eventual strictness through degree four for every N >= 3, or the original universal periodicity conjecture. The separation condition below is sufficient; it is not claimed to be necessary.

This extends the [existing proof](fair_share_proof.md), whose certificates already establish the required strictness separately for N = 3,...,24. The new argument uses Kohlberg's invariant-half-line theorem; the coordinate reductions and discrete recurrence arguments are given in full below. No claim of scientific priority or Lean formalization is made.

## Reading guide

Sections 1-6 establish the third-moment reduction and show why it still allows the N = 2 exception. Sections 7-10 extend the argument to degree four. Section 11 states the exact missing sufficient condition. The [research plan](NEXT_STEPS.md) describes how to attack it.

## 1. An exact coordinate change

Work at boundaries of paired blocks of B = 2N turns. Write

$$
w_k(r)=\binom{B-r}{k}+\binom{r+1}{k},\qquad 0\le r<N.
$$

The two arguments B-r and r+1 have constant sum B+1. Consequently,

$$
w_3(r)-w_3(s)=\frac{B-1}{2}\bigl(w_2(r)-w_2(s)\bigr).
$$

For moment differences D relative to one reference player, define

$$
\widehat x_i=\frac{D_{i,2}}2,
\qquad
\widehat y_i=\frac{2D_{i,3}-(B-1)D_{i,2}}{4B}.
$$

The exact moment recurrences give

$$
\widehat y'_i=\widehat y_i+\widehat x_i.
$$

To avoid moving reference-player coordinates, choose a common normalization for x and a compatible common normalization for y. Let

$$
x_i(m)=\frac{M_{i,2}(m)-\min_j M_{j,2}(m)}2,
\qquad
y_i(0)=0,
\qquad y_i(m+1)=y_i(m)+x_i(m).
$$

Here m counts paired blocks, not individual turns. These are integers, and their differences satisfy

$$
x_i-x_j=\frac{M_{i,2}-M_{j,2}}2,
\quad
y_i-y_j=\frac{2(M_{i,3}-M_{j,3})-(B-1)(M_{i,2}-M_{j,2})}{4B}.
$$

Thus lexicographic comparison by moments 2 and 3 is exactly comparison by (x_i,y_i). Higher moments matter only when both coordinates agree.

With

$$
v_r=\frac{(N-1-r)(N-r)}2,
$$

the normalized update is

$$
x'_i=x_i+v_{r_i}-\min_j(x_j+v_{r_j}),\qquad y'_i=y_i+x_i.
$$

At a tie of both x and y, assigning the tied labels to ranks in a different order cannot change the resulting **unlabelled** multiset of pairs. All tied inputs have identical numerical coordinates. Therefore the evolution of this multiset is independent of moments 4 and above.

## 2. The periodic comparison network

The sorted normalized x-vector is eventually periodic by the finite-state argument already proved in the repository. Fix its eventual period P and a starting phase.

At each phase, keep N slots sorted first by x and then by y. The x-values in these slots, the rank weights, and the partition into equal-x groups are now known and periodic. The update of the vector of y-values consists of:

1. Sorting y within the current equal-x groups.
2. Adding the fixed integer x-value of each slot.
3. Applying a fixed permutation that orders the new x-values.
4. Sorting y within the new equal-x groups.

The first sorting step is redundant on actual states but makes this an operator on **all of R^N**. Each step is continuous, order preserving and nonexpansive for the sup norm. Each sorting operation is piecewise a permutation. Thus the return map over P paired blocks is a continuous, finite-piece, piecewise-affine map

$$
F:\mathbb R^N\longrightarrow\mathbb R^N,
\qquad F(u)=P_\alpha u+c_\alpha
$$

on each polyhedral piece, where P_alpha is a permutation matrix and c_alpha is an integer vector. It is nonexpansive in the sup norm and maps integer vectors to integer vectors.

## 3. Integer piecewise-permutation maps are eventually affine-periodic

**Proposition.** Let F be a continuous piecewise-affine self-map with finitely many polyhedral pieces of R^N, nonexpansive in a norm, with every affine piece a permutation matrix plus an integer vector. Then every integer orbit is eventually affine-periodic: there are a rational vector eta, integers K >= 0 and R >= 1 such that

$$
F^{k+R}(u)=F^k(u)+R\eta\qquad\text{for every }k\ge K.
$$

**Proof.** Kohlberg's invariant-half-line theorem supplies v and eta such that, after shifting v along the ray if necessary,

$$
F(v+t\eta)=v+(t+1)\eta\qquad(t\ge0).
$$

The ray eventually lies in one polyhedral piece: the signs of its finitely many defining affine inequalities eventually stabilize along the ray. Write that piece's affine formula as P u+c. Comparing coefficients of t gives

$$
P\eta=\eta,\qquad Pv+c=v+\eta.
$$

Along any cycle C of P, eta is constant. Summing the second equation over C gives

$$
\eta_i=\frac1{|C|}\sum_{j\in C}c_j\qquad(i\in C).
$$

Hence eta is rational. One may choose a common denominator dividing lcm(1,...,N).

Nonexpansiveness yields

$$
\|F^k(u)-(v+k\eta)\|\le\|u-v\|.
$$

Consequently the residuals e_k = F^k(u)-k eta lie in a bounded set and in the fixed lattice (1/Q) Z^N for a common denominator Q of eta. They belong to a finite set E. Equivalently, one could sample every Q steps; no unrecorded dependence on k modulo Q is being discarded.

For each fixed e in E, the ray e+t eta also eventually lies in one affine piece, say P_e u+c_e. Nonexpansiveness against v+t eta shows that F(e+t eta)-(t+1)eta remains bounded as t grows. Therefore P_e eta = eta. It follows that

$$
F(e+t\eta)-(t+1)\eta=P_e e+c_e-\eta
$$

is independent of t for all sufficiently large t. Since E is finite, one common threshold works for every e in E. Beyond it, e_(k+1) is a deterministic function of e_k on a finite set. The residuals are therefore eventually periodic. This proves the proposition. ∎

For an intermediate phase map G and each eventual residual e, the expression G(e+k eta) eventually has an affine formula in k. Its slope is independent of e, because nonexpansiveness bounds its difference from G(v+k eta). Its constant term is periodic as the residuals cycle. Thus every sorted-slot y-coordinate is eventually affine in the cycle number, with a periodic residual.

## 4. Consequence for second and third moments

For **every N >= 2**, the unlabelled pair configuration (normalized second moment, transformed third moment) eventually has a phasewise affine-periodic form. Second moments are periodic; transformed third moments may drift linearly, but their residuals are periodic.

This sharpens the finite-second-moment result. It does not make the labelled sequence finite-state: different labels may occupy numerically identical slots and their assignment still depends on higher moments.

## 5. The tie network left by degree three

At a fixed eventual phase, each y-value has the form k eta_i+b_i, after including the residual period in the phase. Two slots with equal x can remain tied for infinitely many k only if both their slopes and offsets agree. If their slopes differ, their comparison eventually has a fixed sign; if slopes agree but offsets differ, the comparison is always strict.

Thus all unresolved comparisons reduce to a finite, periodically repeating collection of **persistent equal-(x,y) groups**. Their numerical locations repeat; player identities pass through these groups and are ordered by moments 4 and above.

**Conditional corollary.** If, for a given N, all comparisons at paired-block boundaries are eventually strict through degree 3, then the labelled greedy sequence is eventually periodic.

Indeed, the phasewise sorting permutations are eventually periodic. Over one superperiod they permute the finite set of player labels by a fixed permutation sigma. Repeating the superperiod ord(sigma) times restores all labels. The paired-block reversal rule then gives periodicity of individual turns.

The supplied certificates show that this sufficient condition cannot be used universally as stated: N = 4 already has persistent comparisons first decided in degree 4.

## 6. Why this still permits N = 2 to be aperiodic

For N = 2, the normalized x-configurations alternate between (0,0) and (0,1). At the (0,0) phase, the return map over two paired blocks is

$$
F(a,b)=\operatorname{sort}(b,a+1),\qquad a\le b.
$$

Starting at (0,0),

$$
F^{2k}(0,0)=(k,k),\qquad
F^{2k+1}(0,0)=(k,k+1).
$$

The numerical state is perfectly affine-periodic, yet exact ties return indefinitely. Higher moments decide which player is which. This is fully consistent with Thue-Morse aperiodicity, and demonstrates precisely why the new proposition does not prove the desired all-N theorem.

## 7. An integer fourth-moment coordinate

Continue to use B = 2N and integer coordinates x_i,y_i satisfying

$$
M_{i,2}=2x_i+c_2(m),\qquad
M_{i,3}=(B-1)x_i+2B y_i+c_3(m),
$$

where c_2,c_3 are common to all players at paired-block time m. The zeroth and first moments are also common at these boundaries.

Choose a common scalar c_4(m), starting at zero, to absorb the common terms in the fourth-moment update, and put Z_i=M_{i,4}-c_4(m). Explicitly, choose

$$
c_4(m+1)-c_4(m)
=B c_3(m)+\binom B2c_2(m)+\binom B3M_1(m)+\binom B4M_0(m).
$$

The exact update then becomes

$$
Z'_i=Z_i+2B^2y_i+2B(B-1)x_i+w_4(r_i),
\tag{1}
$$

where w_4(r)=binom(B-r,4)+binom(r+1,4). All coordinates and increments here are integers. Z differences are exactly fourth-moment differences.

## 8. Put the lower coordinates into their established normal form

The preceding theorem supplies a sufficiently late starting block m_0 and a common phase period P such that, writing

$$
m=m_0+kP+j,\qquad 0\le j<P,
$$

the sorted slots have lower coordinates

$$
x_{j,s}=\text{constant},\qquad
y_{j,s}(k)=k\lambda_{j,s}+b_{j,s}.
\tag{2}
$$

Enlarge P to include all residual periods. Since each y-value is an integer, its increment over this period, lambda_(j,s), is an integer. The offsets b are integers as well. Increase m_0 if needed so that every comparison of distinct linear expressions in (2) has its final sign. The partition into equal-(x,y) groups is then fixed at each phase.

**Transport of lambda.** Along an actual player trajectory, y'_i-y_i=x_i is bounded and independent of k at a fixed slot. Therefore the coefficient lambda is unchanged when that player moves to the next phase. This holds also at the wrap from phase P-1 to phase 0, where the cycle counter becomes k+1: the extra constant lambda does not change the coefficient of k.

One may make the argument without tracking a specific trajectory: there are only finitely many possible source-slot/target-slot pairs. A pair with different lambdas can satisfy the required one-step equality for at most one k. Beyond their finitely many exceptional values, every possible routing preserves lambda.

Likewise, slots in a persistent equal-(x,y) group have the same lambda and the same b. All unresolved sorting decisions through degree three therefore occur inside a common lambda class.

## 9. Remove the common quadratic drift inside each class

Set C=2B^2. For a player carrying class parameter lambda at cycle k and phase j, define

$$
Q_\lambda(k,j)=C\lambda\left(\frac{Pk(k-1)}2+jk\right),
\qquad
\overline Z_i=Z_i-Q_\lambda(k,j).
\tag{3}
$$

This is an integer. For phases j<P-1,

$$
Q_\lambda(k,j+1)-Q_\lambda(k,j)=C\lambda k.
$$

At the wrap, the same identity holds:

$$
Q_\lambda(k+1,0)-Q_\lambda(k,P-1)=C\lambda k.
$$

Substituting (2) into (1) thus gives the time-independent, phase-dependent update

$$
\overline Z'_i=\overline Z_i+d_{j,r_i},
\qquad
d_{j,r}=C b_{j,r}+2B(B-1)x_{j,r}+w_4(r).
\tag{4}
$$

The quadratic subtraction does not change any fourth-moment comparison that is needed: such comparisons occur only inside a persistent equal-(x,y) group, whose members have identical lambda and hence identical Q_lambda(k,j).

## 10. Apply the same finite-piece theorem again

At each phase, the evolution of the unlabelled fourth coordinates is now:

1. Sort Zbar within the current equal-(x,y) groups.
2. Add the integer slot constants d_(j,r).
3. Apply a fixed permutation matching the updated lower-coordinate slots.
4. Sort Zbar within the target equal-(x,y) groups.

These target groups and fixed permutations are periodic and independent of k once (2) has stabilized. Every allowed sorting group and every source-target routing respects the transported lambda, as established above.

This construction extends to all real vectors by including the initial group sorting. Its P-step return map is again continuous, nonexpansive, and finite-piece piecewise-affine, with a permutation matrix and an integer translation on every piece. The proved corollary of Kohlberg's theorem therefore applies to Zbar.

Hence Zbar has an eventual affine-periodic orbit. Restoring (3), the sorted-slot Z-values are eventually quadratic polynomials in k with periodic residuals and phase-dependent coefficients. Equivalently, after further enlarging the phase period, each sorted-slot fourth coordinate is a polynomial of degree at most two in the cycle number.

The numerical unlabelled configuration through degree four is independent of moments five and above, because labels tied in all three coordinates (x,y,Z) have identical numerical inputs. Higher moments can only decide which labels occupy those equal slots.

## 11. A precise sufficient condition for the all-N theorem

**Corollary for a fixed N.** If there is a time after which every pair of distinct players has different triples (M_2,M_3,M_4) at every paired-block boundary, then the greedy player sequence is eventually periodic.

**Proof.** The unlabelled slot coordinates through degree four have the eventual polynomial-periodic form just proved. Each difference of two slot coordinates is a polynomial in the cycle number at a fixed phase. A nonzero polynomial has a final sign; an identically zero one stays tied. There are finitely many phases and comparisons. Consequently, all sorting permutations determined through degree four eventually repeat by phase. The strictness hypothesis excludes unresolved ties, so the numerical permutations also determine how labels move. Over one phase superperiod they apply a fixed permutation sigma to the N labels. Repeating this superperiod ord(sigma) times restores every label. The permutation/reversal block lemma then gives periodicity in individual turns. ∎

This gives a concrete remaining theorem target:

$$
\forall N\ge3\ \exists m_0\ \forall m\ge m_0\ \forall i\ne j:
\quad (M_{i,2}(m),M_{i,3}(m),M_{i,4}(m))
\ne(M_{j,2}(m),M_{j,3}(m),M_{j,4}(m)).
\tag{5}
$$

**Statement (5) is not proved.** It is a sufficient condition, not a reformulation known to be equivalent to eventual periodicity. A sequence could be eventually periodic even if higher moments continue to be needed.

The existing certificates establish this eventual degree-four strictness separately for N=3,...,24. A failure of (5) for another N would rule out this particular route at degree four, but would not refute eventual periodicity itself.

The argument above stops at degree four. The [all-fixed-degree induction](FINITE_DEPTH.md) extends this normal form to every finite depth. It proves that eventual separation at some finite depth is equivalent to eventual periodicity. It does not prove that degree four, or any other finite degree, suffices for every N >= 3.

## 12. A small exact experiment behind the reduction

The normalized second-moment orbit is much smaller than the labelled sequence in some of the certified cases:

| N | Second-moment transient, paired blocks | Second-moment period, paired blocks | Minimal labelled preperiod, turns |
|---:|---:|---:|---:|
| 3 | 3 | 3 | 47 |
| 4 | 3 | 4 | 46 |
| 24 | 101 | 24 | 50652467 |

A paired block has 2N turns. For N = 24, the numerical base is therefore already periodic at turn boundary 4848, with period 1152 turns. The much longer labelled transient is entirely compatible with this: higher moments determine the remaining tie decisions.

The first two numerical columns can be reproduced independently with:

```python
def second_moment_cycle(n):
    assert n >= 2
    weights = [(n - 1 - r) * (n - r) // 2 for r in range(n)]
    state = (0,) * n
    seen = {}
    while state not in seen:
        seen[state] = len(seen)
        following = sorted(x + w for x, w in zip(state, weights))
        state = tuple(x - following[0] for x in following)
    return seen[state], len(seen) - seen[state]

for n in (3, 4, 24):
    print(n, second_moment_cycle(n))
```

Termination of this small program for each fixed N follows from the finite-state bound in the original proof. The last column is taken from the committed [certificate verification report](fair_share_verification.json).

## Sources


- Elon Kohlberg, *Invariant Half-Lines of Nonexpansive Piecewise-Linear Transformations*, Mathematics of Operations Research 5(3), 366–372 (1980). DOI: https://doi.org/10.1287/moor.5.3.366
- An accessible precise statement is Theorem 2.4 of Marianne Akian, Stephane Gaubert and Alexander Guterman, *Tropical polyhedra are equivalent to mean payoff games*: https://www.cmap.polytechnique.fr/~gaubert/COURSM2/SCHEDULINGGAMES/FURTHERREADING/AkianGaubertGutermanIJACfinal.pdf

The coordinate reduction and discrete affine-periodicity corollary above are derived here. The cited theorem supplies the invariant half-line; no published all-N fair-share theorem is claimed.
