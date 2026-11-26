# Integer charges on a periodic comparison network

Research derivation, 2026-11-26. This note supplies a general arithmetic
separation criterion for interacting components of the fair-share process.
It applies to components of any size, including components whose pairwise
comparisons change partners. It does **not** prove that the criterion succeeds
for every N >= 3.

The fixed-depth polynomial normal form and the equivalence between bounded
comparison depth and eventual labelled periodicity are proved in
[FINITE_DEPTH.md](../FINITE_DEPTH.md). The results below begin after one such
lower-moment normal form has been obtained.

## 1. The component and its exact integer centering

Let d be the next moment to be examined. The lower moments are degrees
0,...,d-1. After a finite transient and a phase refinement, they have fixed
polynomial profiles on a finite routing graph. Its vertices are pairs
v=(j,r), where j is the phase modulo P and r is the sorted rank. Edges go
from phase j to phase j+1 modulo P.

The graph includes every movement compatible with the lower profiles.
Each phase relation is a disjoint union of balanced complete bipartite
fibers. Thus every weak component is strongly connected, contains the
same number s of vertices in each phase, and is closed under every possible
actual routing. Its actual player set C is fixed once the regime begins.

The polynomial transport lemma gives

$$
p_v(m)=q_C(m)+c_v\qquad(v\in C),
$$

where q_C is common to the whole component and c_v is a constant rational
vector. The raw next moment Y_i=M_(i,d) has an update

$$
Y_i'=Y_i+\ell p_v(m)+b_r.
$$

Here b_r denotes the degree-d rank contribution, not the entire moment
vector. Define the **integer centered coordinate**

$$
W_i=sY_i-\sum_{a\in C}Y_a.
\tag{1}
$$

Then

$$
W_i'=W_i+c_v^*,\qquad
c_v^*=s(\ell c_v+b_r)
 -\sum_{w\in C_j}(\ell c_w+b_{r(w)}).
\tag{2}
$$

The common polynomial term cancels. The increment c_v^* is independent
of time and depends only on the phase and rank. It is an integer: compute
the same expression from the actual integer lower moments at any one
sufficiently late occurrence of that phase. Formula (2) therefore requires
neither rational polynomial antiderivatives nor an additional denominator.

Also

$$
\sum_{i\in C}W_i=0,\qquad
W_i-W_a=s(Y_i-Y_a).
\tag{3}
$$

Thus centering preserves every next-moment comparison within C.

For d=4, put B=2N, C_4=2B^2, D_4=2B(B-1). In the integer coordinates
x,y of [TIE_DYNAMICS.md](../TIE_DYNAMICS.md), the uncentered increment, up to a common scalar,
is

$$
a_{j,r}=C_4 y_{j,r}+D_4 x_{j,r}
 +\binom{B-r}{4}+\binom{r+1}{4}.
$$

Hence c_v^*=s a_v-\sum_{w\in C_j}a_w. A common affine slope of y
cancels exactly, leaving integer constants. This is the centering used by
[structure_certificates.py](structure_certificates.py).

## 2. Graph potential and the closed-walk modulus

The following lemma applies to any strongly connected finite directed
graph with an integer edge increment. In the fair-share application the
increment c_v^* is the same on every edge leaving v.

Choose a root o. For each vertex v choose a directed path from o to v and
let h_v be its total increment, with h_o=0. Define

$$
g=\gcd\{c_v^*+h_v-h_w: v\to w\}.
\tag{4}
$$

The gcd is nonnegative; g=0 means that every listed integer is zero.

**Lemma 1.** The integer g is the gcd of the total increments of all
directed closed walks. In particular it is independent of the chosen
paths. Every allowed player movement preserves

$$
Q_i=W_i-h_v\pmod g.
\tag{5}
$$

When g=0, equation (5) means exact equality in Z, not a congruence modulo
zero.

**Proof.** The sum of the edge residuals in (4) around a closed walk is
its total increment, since the h terms cancel. Thus g divides every
closed-walk increment. Conversely, fix an edge v->w and a directed return
path from w to o. The residual c_v^*+h_v-h_w is the difference between
the costs of two closed walks: the chosen o-to-v path followed by this
edge and the return path, and the chosen o-to-w path followed by the same
return path. The gcd of all closed-walk costs therefore divides each
residual. This proves equality of the two gcds. Finally,

$$
(W_i+c_v^*-h_w)-(W_i-h_v)=c_v^*+h_v-h_w,
$$

which is divisible by g, or is zero if g=0. QED.

A directed breadth-first or depth-first search can construct h. After all
vertices have potentials, one pass over all edges computes (4). It is
not necessary to enumerate closed walks.

## 3. Why different charges forbid a higher-moment tie

Suppose v,w are two slots at the same phase having identical lower
profiles. They are target vertices in one incoming complete bipartite
fiber. In particular, they share a predecessor u. The next-moment
increment on u->v and u->w is the same c_u^*. Equation (4) gives

$$
h_v\equiv h_w\pmod g.
\tag{6}
$$

For g=0 this is exact equality.

If players i,a occupy these slots and also tie in moment d, then W_i=W_a
by (3). Equations (5)-(6) therefore imply Q_i=Q_a in Z/gZ, or in Z when
g=0.

**Theorem 2 (charge separation).** Different charges can never participate
in an unresolved tie through degree d after this lower regime begins. If
all s players in each nontrivial lower component have distinct charges,
every comparison through degree d is strict from that point onward.
Consequently the labelled fair-share word is eventually periodic by the
finite-depth theorem.

The statement makes no binary-component assumption. A component of size
27 is treated by exactly the same invariant as a component of size two.
Equal charges are only inconclusive: they do not imply that the players
ever tie, still less that their labelled continuation is aperiodic.

Numerical components caused only by a permutation of label positions
over a short phase period are also harmless. A positive separation test
on such a component remains valid. One may refine the phase period to
remove this permutation before interpreting a negative test.

## 4. Compatibility with refinement to the next moment

A charge is attached to an actual label along every compatible trajectory.
To turn this into a static coloring of the *next* polynomial routing graph,
its phases may need further refinement.

For g>0, each centered next-moment slot profile is a rational polynomial
in the absolute block time. If D is a common denominator of its polynomial
coefficients, then a time shift divisible by Dg changes its value by a
multiple of g. Refine the phase period by such a multiple as well as the
previous phase period. Every slot then has a fixed value of W_v-h_v
modulo g. Every compatible next-depth edge preserves this residue by
the exact update. Hence every next-depth component is monochromatic.

For g=0, W_v-h_v is a rational polynomial on a phase and takes its values
in the finite set of actual conserved integer charges. A polynomial that
takes only finitely many values on an unbounded arithmetic progression is
constant. Thus the same monochromatic conclusion follows without a
modular phase refinement.

This qualification matters. A phase period describing the unlabelled
numerical state can be shorter than a period describing which charges
occupy the slots. Omitting the refinement could mistake this temporal
permutation for genuine interaction between different charges.

## 5. An aggregate obstruction

At a fixed phase write H_j=\sum_{v\in C_j}h_v. By (3), the sum of the
label charges satisfies

$$
\sum_{i\in C}Q_i\equiv-H_j\pmod g.
\tag{7}
$$

If all s charges were equal to one residue q, then

$$
sq\equiv-H_j\pmod g.
$$

This congruence has a solution only if

$$
\gcd(s,g)\mid H_j.
\tag{8}
$$

For g=0 the same condition reads s|H_j. Therefore failure of (8)
forces a nontrivial charge partition and a split of C at the next depth,
after the phase refinement just described. This test depends only on the
centered network, not on the initial higher-moment values.

The divisibility is independent of the potential convention: replacing
all potentials by a common constant changes H_j by s times that constant;
changing path choices changes each potential by a multiple of g. It is
also independent of phase. Indeed, choose any perfect matching between
the two consecutive phase fibers and sum its edge congruences. Since
\sum_{v\in C_j}c_v^*=0, one obtains H_j=H_(j+1) modulo g.

Condition (8) is only necessary for all charges to coincide. Its validity
does not establish equal charges. The individual residues give the
stronger practical test.

## 6. Other common gauges and a possible loss from centering

More generally one can subtract any common scalar trajectory from the
next coordinates, provided the resulting increments are constant on
phase/rank slots and have a common integer denominator. After clearing
that denominator, Lemma 1 and Theorem 2 apply unchanged.

For example, choose a periodic compatible route as a fictitious reference,
enlarging the phase period so this route closes. Subtract its accumulated
increments from every coordinate. Its own closed-walk increment is now
zero. This is the reference convention in [network8_lattice_probe.py](networks/network8_lattice_probe.py); the
reference need not be followed by any particular actual player.

Centering is particularly convenient and exact, but the elementary
modular test with a fixed, short phase period can be weaker than the
reference convention. In an abstract one-phase complete network with
increments (0,2), initial coordinates (0,1) have distinct reference charges
modulo 2. Their centered coordinates (-1,1) coincide modulo 2. This is
not a fair-share counterexample; it illustrates a general effect of
multiplying coordinate differences by s without necessarily multiplying
the closed-walk gcd by s.

There is a simple repair if comparison with a reference gauge is desired.
Suppose its increment modulus is g_ref and it has phase period P. Let
T_j be the sum of its increments over the s component slots in phase j,
and T=\sum_j T_j. A choice of perfect matchings decomposes the full set of
these edges into directed cycles, so g_ref divides T. Centered increments
are s c_v-T_j. On the phase lift of period sP, every closed walk has length
ksP and centered cost

$$
s\bigl(\text{reference-relative walk cost}-kT\bigr),
$$

which is divisible by s g_ref. At a fixed lifted phase the corresponding
potential differences also agree with s times the reference potential
differences modulo s g_ref. Thus any pair separated by the reference
charges is separated by the centered charges on this lifted graph.

The proof above is for g_ref>0. If g_ref=0, every reference closed walk
has zero cost and T=0, so the same argument uses exact differences.
Lifting can split the old component; that already constitutes useful
separation. A successful short-period centered test needs no repair.

## 7. A rigorous description of any remaining infinite-depth obstruction

One can choose the fixed-depth normal forms with nested phase periods,
discarding finitely many additional initial blocks at each stage. Each
higher-depth routing edge projects to a lower-depth routing edge. Hence
the resulting partitions of the actual finite player set refine as the
depth increases.

When desired, multiply a phase period by N! to remove any component that
is present only because of a deterministic permutation over the old
period. If a lower graph has no unresolved tie, all its vertices have
unique successors, and this phase refinement splits it into components
containing one label each.

Since there are only N labels, the nested label partitions can strictly
refine only finitely often. If no finite depth gives eventual strictness,
at least one stabilized part C has size s>=2. For every fixed degree k,
choose a sufficiently high stage at which C has stabilized. The polynomial
transport lemma makes the entire degree-k time-dependent polynomial
common to C, leaving only finitely many phase/slot constants. Consequently

$$
\sup_{m\ge m_k}|M_{i,k}(m)-M_{a,k}(m)|<\infty
\quad(i,a\in C).
\tag{9}
$$

Each bound may depend on k; there is no asserted uniform bound over all
degrees. The aggregate turn occupancy of C is eventually periodic,
because already at any one stabilized lower stage it occupies a fixed
set of ranks in each recurring phase. At every higher charge test that
does not further split C, all its labels must have the same charge.

Thus an all-N proof can be reduced to excluding such a nontrivial terminal
component for the canonical rank weights. This is a rigorous necessary
structure, not yet an exclusion theorem. The two-player Thue-Morse case
has bounded discrepancies at every fixed degree while the depth needed
to decide some comparisons keeps increasing, so (9) alone is insufficient.

## 8. Why the binary characteristic-two argument does not directly extend

For two players, subtraction and addition agree modulo 2. The difference
of their score polynomials is therefore determined modulo 2 by their
aggregate occupancy. This is the invariant used in
[PARITY_OBSTRUCTION.md](PARITY_OBSTRUCTION.md) and [PARITY_RESONANCE.md](PARITY_RESONANCE.md).

For a component of s>2 players, its aggregate does not determine the
difference of a selected pair. A prime divisor of s makes the centered
scores have the same aggregate residue, but does not determine which
pair collides. Similarly, the discriminant product of all pair differences
depends on further symmetric functions, not just on the aggregate sum.

Connectivity through a succession of pair ties does not imply that all
s players tie simultaneously. Nor does an unbounded comparison depth for
some pair at some phases supply a simultaneous high-order tie of the
whole component. Any extension that uses one of these implications needs
a separate synchronization theorem. None has been proved here.

## 9. The observed fourth-moment modulus needs more than binomial algebra

The independently checked N=3,...,24 networks with labelled certificate
phases have 31 nontrivial degree-three components. In these calculations,
all initial fourth-moment reference charges are distinct, and every
computed modulus is a multiple of 2B^2=8N^2. This is finite evidence,
not a universal divisibility theorem.

There is a useful exact warning about attempting to derive this
divisibility from binomial identities alone. At N=3, B=6, the triangular
rank weights are (3,1,0), while the raw rank moments are

| Rank | w_2 | w_3 | w_4 |
|---:|---:|---:|---:|
| 0 | 15 | 20 | 15 |
| 1 | 11 | 10 | 5 |
| 2 | 9 | 5 | 1 |

Consider two formal three-block rank histories

$$
r_A=(2,0,2),\qquad r_B=(1,1,1).
$$

Starting with zero differences, use

$$
D_2'=D_2+\Delta w_2,\quad
D_3'=D_3+6D_2+\Delta w_3,\quad
D_4'=D_4+6D_3+15D_2+\Delta w_4.
$$

The successive differences A-B are

$$
(-2,-5,-4),\quad (2,-7,-54),\quad(0,0,-70).
$$

Therefore equality through degree three does not, by itself, force the
fourth difference to be divisible by 72=2B^2. These histories cannot be
used as a canonical counterexample: after the first two blocks A has
triangular load 3, B has load 2, and the remaining player has load 3.
B must receive rank zero next, contrary to the stipulated third rank
one. Any proof of the observed modulus divisibility must exploit the
greedy routing constraints or an equally strong property of the reachable
periodic network.

## 10. Independent review of the new lower-regime certifier

[structure_certificates.py](structure_certificates.py) does not assume a periodic labelled word.
It first proposes an affine regime for the independent lower numerical
process. Its `certify` routine checks both the intercept order and the
slope order at every equal-second-moment group, transports the slopes,
and verifies the exact affine return after one proposed period. These
conditions imply the same numerical regime for every later repetition.
Moving one entire period forward removes accidental equalities between
distinct affine profiles.

It then builds the complete compatible routing graph, including the
cycle-counter increment at the phase wrap. The centered fourth-moment
costs are precisely (2). A directed search computes h and the gcd (4).
Finally, a separately reconstructed genuine labelled prefix supplies the
initial charges. If this prefix ever encounters an unresolved tie through
degree four, the routine reports that obstruction instead of silently
choosing its continuation.

Independent runs during this review gave:

| N | Lower-regime start, blocks | Phase period, blocks | Charge result |
|---:|---:|---:|:---|
| 2 | 4 | 4 | inconclusive, as expected |
| 3 | 12 | 3 | all components separated |
| 8 | 110 | 16 | all components separated |
| 25 | 523 | 210 | all components separated |
| 30 | 13230 | 1620 | all components separated |

The N=30 calculation includes a component of 27 players with modulus
194400 and distinct charges. These are exact checks for those particular
N, not a universal proof or a prediction of the least labelled period.

## 11. Remaining theorem target

The graph-charge invariant now handles arbitrary interacting components
and gives an exact finite certificate when it separates the initial
labels. What is missing is a proof that the canonical data force enough
separation, at degree four or after finitely many refinements, for every
N>=3. Neither the repeated success of the calculations nor the terminal
component reduction establishes that last step.
