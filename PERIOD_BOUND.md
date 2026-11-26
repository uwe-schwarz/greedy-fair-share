# A bound on the prime factors and depth-dependent size of the period

Research derivation, 2026-11-26. This strengthens the fixed-depth normal
form using Euclidean nonexpansiveness. It does not prove bounded depth
for every N.

Put L_N=lcm(1,...,N) and B=2N.

**Theorem.** For every fixed degree d>=1, the phase period in the
fixed-depth polynomial normal form can be chosen to divide L_N^(d-1).
If comparisons are eventually strict through degree d, the labelled word
has an eventual period in paired blocks dividing L_N^d. Consequently, if
the canonical word is eventually periodic, every prime factor of its
least period in individual turns is at most N.

The exponent d is not bounded here as a function of N. Thus this theorem
restricts possible periods but does not settle eventual periodicity.

## 1. Periodic orbits of Euclidean nonexpansive piecewise permutations

**Lemma 1.** Let F:R^n->R^n be Euclidean nonexpansive and have finitely
many polyhedral affine pieces, each of the form P x+c with P a coordinate
permutation matrix. The least period of any periodic orbit divides
lcm(1,...,n).

**Proof.** Let E be a finite periodic orbit, of least period R. For any
u,v in E, periodicity and nonexpansiveness give

$$
\|u-v\|_2=\|F^R(u)-F^R(v)\|_2
\le\cdots\le\|F(u)-F(v)\|_2\le\|u-v\|_2.
$$

Thus F preserves every pair distance in E. If

$$
x=\sum_i\alpha_i u_i,\qquad
y=\sum_i\alpha_i F(u_i),\qquad
\alpha_i\ge0,\quad\sum_i\alpha_i=1,
$$

the variance identity and nonexpansiveness imply

$$
\begin{aligned}
\|F(x)-y\|_2^2
 +\frac12\sum_{i,j}\alpha_i\alpha_j
     \|F(u_i)-F(u_j)\|_2^2
 &=\sum_i\alpha_i\|F(x)-F(u_i)\|_2^2\\
 &\le\sum_i\alpha_i\|x-u_i\|_2^2\\
 &=\frac12\sum_{i,j}\alpha_i\alpha_j\|u_i-u_j\|_2^2.
\end{aligned}
$$

The two variance sums agree, so F(x)=y. In particular F is affine on
the convex hull H of E.

At least one of the finitely many polyhedral pieces has an intersection
with H containing a relatively open subset of its affine hull. On that
subset F=P x+c for one coordinate permutation P. Since both formulas
are affine on H, this identity holds throughout H, and therefore on E.

Let k be the order of P, so k divides lcm(1,...,n). Iterating the affine
formula along the orbit gives F^k(u)=u+a, where
a=\sum_(j=0)^(k-1) P^j c. Iterating this formula R times gives
u=F^(kR)(u)=u+Ra. Therefore a=0 and F^k(u)=u. The least period R
divides k. QED.

## 2. The eventual residual map has the same property

In the normal-form proof, a return map F is a composition of group
sortings, translations, and coordinate permutations. Each group sorting
is Euclidean nonexpansive, by the optimal matching/rearrangement
inequality. Thus F is nonexpansive both in the Euclidean norm and in the
sup norm. Its affine pieces are coordinate permutations plus translations.

Kohlberg's theorem and the integer-lattice argument already used in
[FINITE_DEPTH.md](FINITE_DEPTH.md) give an invariant half-line

$$
F(v+t\eta)=v+(t+1)\eta\qquad(t\ge0)
$$

and eventual periodicity of the residuals e_k=F^k(u)-k eta.
To apply Lemma 1 to those residuals, define

$$
F_\infty(x)=\lim_{t\to\infty}
\bigl(F(x+t\eta)-(t+1)\eta\bigr).
\tag{1}
$$

This is an eventual exact limit for each fixed x. Indeed, the ray
x+t eta eventually lies in one polyhedral piece P x+c. Nonexpansiveness
against v+t eta forces P eta=eta; otherwise the distance of their
images would grow linearly with t. The expression in (1) is therefore
eventually the constant P x+c-eta.

The map F_infinity is Euclidean nonexpansive: take limits in the
nonexpansive inequality for F(x+t eta) and F(y+t eta). It also has
finitely many polyhedral affine pieces of the same permutation form.
To see this, write a piece's inequalities as a·x<=b. Along a ray,
inequalities with a·eta>0 are eventually false, those with a·eta<0
are eventually true, and those with a·eta=0 remain the same inequality
in x. The resulting limiting pieces are still polyhedral and finite.

The eventual residual set E is finite. Hence the stabilization in (1)
is uniform over E, so e_(k+1)=F_infinity(e_k) for all sufficiently large
k. Lemma 1 shows that its eventual period divides L_N.

No extra period factor is needed for the denominator of eta or for the
rational coordinate gauges. Those denominators were used only to prove
that the bounded residual orbit lies in a finite lattice. Lemma 1 applies
to its actual least period.

## 3. Induction over the moment degree

At paired-block boundary m the zeroth and first age moments are common
to all players and are explicitly

$$
M_{i,0}(m)=2m,\qquad M_{i,1}(m)=Bm^2+m.
$$

Thus degree one has phase period P_1=1.

Suppose the polynomial profiles through degree d-1 have phase period
P_(d-1). The next-moment normal-form construction gives a return map over
that period. Section 2 shows that its residual period R divides L_N.
The intermediate phase maps preserve the phasewise affine residual form;
restoring the common polynomial gauges changes no phase period.
Therefore one may take

$$
P_d=P_{d-1}R,\qquad R\mid L_N.
$$

Induction gives P_d|L_N^(d-1). Removing the finitely many roots of
polynomial comparison differences increases only the initial transient,
not the phase period.

If the degree-d moment vectors are eventually pairwise distinct, the
routing over one such phase period is a fixed permutation sigma of the
N labels. Its order divides L_N. Hence a labelled paired-block period
divides P_d L_N, and therefore divides L_N^d.

Finally, the finite-depth equivalence proves that an eventually periodic
canonical word has some finite separating d. An individual-turn period
is B times the preceding block period. Its least period divides that
period, and every prime divisor of B=2N or of L_N is at most N. This
proves the theorem. QED.

## Scope

The statement does not predict a least period or a preperiod. It supplies
a depth-dependent divisibility bound. It remains compatible with the
two-player Thue-Morse exception: finite numerical projections can acquire
additional factors of two at successively higher degrees while no one
finite degree resolves all later comparisons.
