# Rank-count rigidity: a precise conjecture, consequences, and failed extensions

Research notes, 2026-11-26. The universal rank-count rigidity conjecture
below remains unproved. The algebraic consequences and counterexamples
are separate statements.

## 1. The exact graph property

Work in a certified eventual affine regime of the lower coordinates
(x,y), where x is the normalized second moment and y'=y+x. Let C be a
closed component of its compatible phase/rank routing graph, with s
slots per phase. Put e_r for the rth standard basis vector of Z^N.

For a source vertex v=(j,r), define the centered rank-count increment

$$
\gamma_v=s e_r-\sum_{q\in C_j}e_q\in\mathbb Z^N.
$$

**Rank-count rigidity** means that there are integer vector potentials
H_v such that

$$
\gamma_v=H_w-H_v\qquad\text{for every edge }v\to w.
\tag{1}
$$

Equivalently, every directed closed walk has zero total centered
rank-count increment. This is a finite exact condition. A directed
search assigns H along a spanning tree; every remaining edge must have
zero vector defect.

**Unproved target.** For the triangular weights
v_r=binom(N-r,2), starting at x=y=0, every component of the eventual
degree-three routing graph has rank-count rigidity.

This is a statement about the entire compatible graph, not merely the
rank frequencies of one known labelled continuation.

The expanded graph check in [network_rank_rigidity.py](rank/network_rank_rigidity.py) and the independent
compact check in [rank_holonomy_compact.py](rank/rank_holonomy_compact.py) both verify this property on
the tested canonical regimes. The expanded check uses phase/rank vertices
directly; the compact check uses per-wire rank histograms and tie/wrap
constraints. Neither computation is an all-N proof.

## 2. Consequence for the fourth-moment modulus

**Proposition.** If (1) holds on a component, every centered fourth-moment
closed-walk cost is a multiple of C_4=2(2N)^2=8N^2.

**Proof.** Let

$$
\alpha_v=s y_v-\sum_{q\in C_j}y_q.
$$

The common affine y slope cancels, so alpha_v is a fixed integer on
each phase/rank vertex. The lower update gives

$$
\alpha_w-\alpha_v=s x_v-\sum_{q\in C_j}x_q.
\tag{2}
$$

Let beta_v be the scalar potential obtained by weighting the vector
H_v in (1) by w_4(r). It satisfies

$$
\beta_w-\beta_v=s w_4(r)-\sum_{q\in C_j}w_4(q).
\tag{3}
$$

The centered fourth-moment increment is therefore

$$
c_v=C_4\alpha_v
 +D_4(\alpha_w-\alpha_v)+(\beta_w-\beta_v),
\qquad D_4=2(2N)(2N-1).
$$

Summing around a closed walk eliminates both potential differences and
leaves C_4 times an integer. QED.

The same argument applies to the reference-relative convention after
choosing a phase period that closes the reference route. The special
quartic formula for w_4 is not needed for this conditional proposition:
rank-count rigidity makes every rank-only reward a potential difference.
What remains unproved is why the canonical triangular lower process
always has the required rigidity.

## 3. Exact rank charges and a root-of-unity consequence

Let K_(i,r)(m) be the number of paired blocks before m in which player i
had rank r. If (1) holds, then

$$
Q_i=sK_i-\sum_{a\in C}K_a-H_v\in\mathbb Z^N
\tag{4}
$$

is an exact conserved vector for each label. At an equal-(x,y) tie,
the slots have the same H_v: they share an incoming predecessor and
the same edge increment. Hence at such a tie

$$
s(K_i-K_a)=Q_i-Q_a.
\tag{5}
$$

Thus a pair's rank-count difference at any later persistent lower tie
is independent of which tie phase it uses.

Put B=2N and write full score polynomials in x=1+z. For any Bth root of
unity zeta, a paired block's multiplication by x^B becomes one, so

$$
G_i(m,\zeta)=\sum_{r=0}^{N-1}K_{i,r}(m)
      (\zeta^{B-r}+\zeta^{r+1}).
\tag{6}
$$

Choose a prime power q=p^a dividing B and a primitive qth root zeta.
At a lower tie, equations (5)-(6) show that

$$
s(G_i-G_a)(m,\zeta)
=R_{i,a}(\zeta),\qquad
R_{i,a}(x)=\sum_r(Q_i-Q_a)_r(x^{B-r}+x^{r+1}).
\tag{7}
$$

The right side is fixed. If it is nonzero, the pair's order of vanishing
at x=1 is uniformly bounded. Indeed, if (G_i-G_a)(m,x) is divisible
by (x-1)^d in Z[x], then R_(i,a)(zeta) is divisible by (zeta-1)^d
in Z[zeta]. The algebraic norm of zeta-1 is p. Therefore

$$
p^d\mid\left|\operatorname{Norm}(R_{i,a}(\zeta))\right|,
$$

and the fixed, nonzero integer on the right bounds d by its p-adic
valuation. Equivalently one can use the resultant of R_(i,a) and
the prime-power cyclotomic polynomial. This gives a finite-depth
certificate whenever every pair in every lower component is separated
at at least one such root.

It is important to use prime-power orders. For a cyclotomic order that
is not a prime power, zeta-1 can be an algebraic unit, so the norm argument
does not give the same bound.

This criterion is useful but incomplete even in known periodic cases.
The exact checks in [network_rank_characters.py](rank/network_rank_characters.py) find pairs with equal
vector rank charges at N=4,6,8. At N=10 and N=14 there are distinct
vector charges that agree at every prime-power root allowed by B.
The fourth-moment charge test nevertheless separates these cases.
Thus rank rigidity and exact vector charges alone do not finish the
universal separation proof; time-weighted rank history remains relevant.

## 4. Why zero origin without curvature is insufficient

Take N=4 and strictly decreasing affine weights (3,2,1,0), still with
canonical initial x=y=0. After four blocks all x and y values are common
again. Two compatible rank histories are

$$
(0,3,3,0),\qquad (1,2,2,1).
$$

They have different rank-count vectors in one persistent lower component.
Therefore zero origin and strict decrease alone do not imply (1).

## 5. Strict convexity and zero origin are also insufficient

There is an exact counterexample with N=6 and

$$
v=(27,18,10,5,2,0).
$$

Its successive gaps are (9,8,5,3,2), strictly decreasing and positive,
so the weights are strictly decreasing and strictly convex. The canonical
zero-origin lower process has a certified affine regime beginning at
block 62 with period 6 and a common y increment of 33 per period:

| Phase | Sorted x | Corresponding y |
|---:|:---|:---|
| 0 | (0,0,2,7,8,17) | (337,342,352,350,337,336) |
| 1 | (0,2,2,7,8,17) | (345,354,357,353,342,337) |
| 2 | (0,2,2,7,10,17) | (350,359,360,354,356,345) |
| 3 | (0,0,0,5,8,15) | (361,362,366,362,361,350) |
| 4 | (0,0,0,5,8,17) | (366,367,369,365,362,361) |
| 5 | (0,0,0,7,8,17) | (369,370,370,378,367,366) |

At phase 5, ranks 1 and 2 have a persistent equal-(x,y) tie. The routing
component contains all six players. One closed compatible walk beginning
at phase 5, rank 1 has the following twelve successive ranks:

$$
(1,4,0,5,3,1,4,1,4,0,5,3).
$$

It returns to the same phase/rank vertex. Its rank counts are
(2,3,0,2,3,2), whereas zero centered holonomy would require two visits
to every rank. The centered defect is

$$
6(2,3,0,2,3,2)-12(1,1,1,1,1,1)
=(0,6,-12,0,6,0)\ne0.
$$

Its x sum is 66, exactly twice the common y slope, so this is fully
compatible with the lower affine regime. The example was independently
verified with expanded and compact graph implementations. The exact
prefix discovery and six-phase certificate are in
[network_convex_probe.py](rank/network_convex_probe.py) / [network_convex_probe.jsonl](rank/network_convex_probe.jsonl), with an
independent result in [rank_holonomy_convex_control.json](rank/rank_holonomy_convex_control.json).

This is a counterexample to the proposed *extension of rank rigidity*.
It is not a counterexample to the original triangular fair-share problem.

## 6. A narrower quadratic question

The family

$$
v_r=k^2+a k,\qquad k=N-1-r,
$$

includes a positive scalar multiple of the triangular weights at a=1.
The narrow exact probe N=6,...,10 and a=0,1,2,3 found rank rigidity in
all twenty certified lower regimes. Data are in
[network_quadratic_probe.jsonl](rank/network_quadratic_probe.jsonl). This suggests examining the constant
second difference of the weights, rather than qualitative convexity.
It proves neither the quadratic-family assertion nor the original
all-N rank-rigidity conjecture.

The zero-origin process has a useful sensitivity interpretation: y is
the first coefficient obtained by perturbing the scalar multiplier in
sort((1+epsilon)x+v). Independent perturbations of each rank weight
produce rank-count path integrals. A possible proof would show that the
first multiplier coefficient separates all compatible cycles with
different rank-occupation vectors when v is quadratic. No such implication
has been established. The explicit strictly convex counterexample above
prevents replacing this missing step by a general convexity assertion.

## 7. A separate shortcut that is false

Even for the canonical triangular weights, equality of x and y at one
time does not imply equality of accumulated rank counts. At N=5, block 4,
a tied pair has rank-count difference (-1,2,-1,1,-1). The intended
conjecture is about zero *closed-walk* defects in the eventual component,
not about recovering the whole rank history from the present lower
coordinates during the transient.
