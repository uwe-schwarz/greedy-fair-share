# Rank-count rigidity: independent checks and the remaining hypothesis

Date: 2026-11-26. No universal rigidity theorem is claimed.

## 1. Exact property

Fix an established periodic affine lower profile (x,y), and a connected
comparison component with s slots at each phase. On a source slot r of
phase j, assign the integer vector cost

    c_rank(j,r) = s e_r - sum_(q in C_j) e_q  in Z^N.

Rank-count rigidity means every directed cycle has total vector cost
zero. Equivalently, an integer vector potential H exists on the complete
phase/rank graph with

    H(v)-H(u)=c_rank(u)

on every allowed edge. By taking a scalar product with an arbitrary
rank function f(r), every centered rank-only scalar cost is then an
exact coboundary. This is strictly stronger than a divisibility check
for the particular fourth rank weight.

## 2. Independent compact implementation

rank_holonomy_compact.py imports only the exact lower-profile discovery
from structure_certificates.py. It contracts the deterministic wire
paths, retaining every tie and period-wrap constraint, and solves the
resulting vector constraints by ordinary graph breadth-first traversal.
It does not use the root's weighted potential-union implementation or
the other agent's expanded phase/rank graph.

Each wire carries its accumulated rank-count vector. If H_a,H_b are
those vectors at a tie, their centered potential difference must be
s(H_a-H_b). At a period endpoint the centered integral is
s H_a-T_C, where T_C is the component's total rank-count vector. A BFS
potential is checked against every retained constraint. The same
construction independently checks the centered x cost.

Results are in rank_holonomy_compact.json.

## 3. All requested new canonical regimes passed

| N | Lower start, blocks | Lower period, blocks | Nontrivial component sizes | Rank-count defects |
|---|---:|---:|---|---|
| 25 | 523 | 210 | 2 | All zero |
| 30 | 13230 | 1620 | 27 | All zero |
| 32 | 28042 | 512 | 3,5,3,2,3,3,2,3,3 | All zero |
| 36 | 5420 | 2520 | 4,3 | All zero |
| 48 | 42106 | 2592 | 2,27,2,2,2 | All zero |
| 60 | 373908 | 9600 | 56 | All zero |

These are 19 nontrivial components in total. Every centered x cycle
cost also vanishes. The lower regimes were rediscovered from zero and
certified for all future repetitions before checking their graphs.
No huge-period N=62 case was used.

The complete requested run took about 8.4 seconds. The largest
component (N=60, size56) required only 583 compact constraints for the
whole N-player network; 1103 checks between already assigned vertices were
made in the nontrivial component. These replace expansion of 576000
phase/rank vertices with 60 wire variables carrying integer vectors.

## 4. Exact reduction of fourth holonomy

Write B=2N, C=2B^2=8N^2 and D=2B(B-1). After the established common
gauges, fourth moments advance by

    Z' = Z + C y + D x + w4(r).

Within a component, let centering mean s times the slot value minus
the sum over that phase's component slots.

Centered x is always a coboundary: it is the increment of centered y,
because y'=y+x. The common affine y slope of a component cancels under
centering, including at the period wrap.

If rank-count rigidity holds, centered w4 is also a coboundary, since
w4 depends only on rank. Therefore every closed fourth-cost integral
is exactly C times its closed centered-y integral. If g4 denotes the
gcd of all fourth cycle costs and g_y the gcd of centered-y cycle
costs, then

    g4 = C g_y,

with the convention gcd{0}=0. Thus the large factor C in the canonical
fourth moduli has a precise conditional explanation. The claim still
requires the rank-count rigidity hypothesis; it has not been proved
for every canonical N.

For the recorded root charge data this gives, for example, g_y=27 for
the size27 components at N=30 and N=48, and g_y=8 for the size56
component at N=60.

## 5. The realizable N=4 false start fails rigidity

Take the four prescribed paired-block first-half orders

    [0,2,3,1], [2,3,0,1], [1,0,3,2], [3,0,1,2].

After 13 further greedy lower steps, the exact lower profile has period
12 and a size-three component. The independent compact rank-count
constraint has defect

    (6,-12,0,6),

while centered x holonomy remains zero. This agrees with the separately
verified fourth modulus g4=4 rather than a multiple of128.

Crucially, this false start lies on the SAME second-moment cycle as the
canonical N=4 run:

    (0,1,1,4), (0,2,2,4), (0,1,2,3), (0,0,1,3).

Therefore rigidity cannot be deduced merely from the recurrent
second-moment cycle or its affine reference permutation. The canonical
third-moment orbit carries additional information.

The rank-count property also fails on the unrefined canonical
second-moment graph itself for the tested N>=4. The third-moment
refinement is material.

## 6. Strict convexity of weights is insufficient

The other theory agent found a zero-origin counterexample using the
strictly convex decreasing weights

    v=(27,18,10,5,2,0).

Its adjacent gaps are9,8,5,3,2, strictly decreasing, and the lower system
has certified start62, period6 and common y increment33. A size-six
component has rank-count defect

    (0,-6,12,0,-6,0).

The compact implementation independently reproduces that vector and
zero centered x holonomy; see rank_holonomy_convex_control.json.
Thus a theorem based only on strict convexity and a zero initial state
is false. The exact quadratic triangular weights, or a comparably
specific arithmetic feature, must be used.

## 7. A tempting prefix invariant is also false

One cannot prove eventual rank rigidity by claiming that equal current
second and third moments imply equal rank counts from origin. For the
canonical N=5 process, the first four paired-block permutations are

    [0,1,2,3,4],
    [4,3,2,1,0],
    [2,3,1,4,0],
    [1,0,4,3,2].

At block4, labels3 and4 have equal moments two and three, but their
rank-count difference is

    (1,-2,1,-1,1).

The fourth moments distinguish them by212. This is a genuine canonical
prefix example, not a false start. Eventual vector holonomy can vanish
even though finite-prefix rank counts do not coincide at lower ties.
The broader bounded prefix probe is preserved in
rank_holonomy_prefix_probe.py/json, but this four-block example alone
suffices to disprove the proposed strengthening.

## 8. Remaining precise target

The observed universal candidate is now:

> For the zero-origin triangular-weight process, every connected
> persistent comparison component of the eventual affine (x,y) profile
> has zero centered rank-count holonomy.

This candidate survives the independent checks reported here. It is not
implied by periodicity, physical realizability, the canonical second
cycle, strict convexity, or equality of prefix rank counts at a tie.
A proof must explain the special interaction of the canonical
accumulated y history with the exact triangular weights. Even after
proving it, a separate argument is needed to show canonical fourth
charges separate (or that any equal-charge clusters terminate at a
higher finite degree).
