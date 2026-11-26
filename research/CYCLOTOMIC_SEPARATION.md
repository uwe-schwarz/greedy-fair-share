# Cyclotomic rank charges and a reduction to binary components

Date: 2026-11-26. The separation theorem below is proved. Its uniform
canonical hypotheses remain unproved for arbitrary N.

## 1. Rank-count charges are exact integer invariants

Fix N, put B=2N, and consider a closed comparison component C of size s
in an established periodic lower-moment profile. A slot v has a phase
and rank r(v). Define the centered rank-count vector cost

    c(v)=s e_(r(v)) - sum_(w in C at the same phase) e_(r(w)).

Assume rank-count rigidity: there is a periodic integer vector potential
h_v with h_w-h_v=c(v) along every allowed edge v->w.

For a label i, let n_i(t) in Z^N record how many previous paired blocks
assigned each rank to it. Let n_C be the sum over the fixed labels in
the component, and define

    q_i = s n_i - n_C - h_(slot(i)).                     (1)

This vector is exactly invariant, not merely invariant modulo an
integer. The update of the first two terms is c(v), cancelled by the
potential increment.

Whenever two slots are compared because their lower coordinates tie,
their potentials agree: they are both possible outputs of a common
predecessor with the same edge cost. Therefore, at every such comparison
between labels i,j,

    s(n_i-n_j)=q_i-q_j.                                 (2)

All q_i have coordinate sum zero: every player has one rank per paired
block, and the vector edge costs and normalized potentials have
coordinate sum zero.

## 2. A full score difference at a root of unity

The rank-r score polynomial for one paired block is

    g_r(x)=x^(B-r)+x^(r+1),      0<=r<N.

A label's score at a paired-block boundary is a sum of these polynomials
multiplied by powers of x^B. For any root of unity zeta with zeta^B=1,
all these aging factors are 1. Thus at a lower-moment comparison,

    s(G_i-G_j)(zeta)
       = sum_r (q_i-q_j)_r g_r(zeta).                    (3)

The right side is a fixed algebraic integer, independent of the time
of the comparison. Define A_ij(x) as the integer polynomial obtained
by the same sum.

This argument requires the score history to consist of paired blocks
from turn zero. It does not apply verbatim to arbitrary false-start
words with unequal per-player turn counts.

## 3. Cyclotomic separation theorem

**Theorem.** Suppose zeta has prime-power order p^a dividing B. If
A_ij(zeta) is nonzero, then the order of vanishing at x=1 of every
future score difference G_i-G_j at a lower-moment comparison is at most

    v_p( |Norm_(Q(zeta)/Q) A_ij(zeta)| ).                (4)

In particular, the deciding-moment depth for this pair is uniformly
bounded, with no need to know its later label routing.

**Proof.** If the score difference vanishes to order d at x=1, then

    s(G_i-G_j)(x)=(x-1)^d Q(x)

for an integer polynomial Q, because division by the monic polynomial
(x-1)^d preserves integer coefficients. Evaluation at zeta and (3) give

    A_ij(zeta)=(zeta-1)^d Q(zeta).

The algebraic norm of zeta-1 has absolute value p, since
Phi_(p^a)(1)=p. Taking norms shows that p^d divides the fixed nonzero
integer Norm A_ij(zeta). This proves (4). The scaling by s may make
the bound larger than necessary but does not affect its finiteness. ∎

Only prime-power orders give this argument: for other root orders,
Norm(1-zeta) can be 1 and the divisibility need not bound d.

## 4. Computable signature classes

For every prime power d dividing B, reduce

    A_i(x)=sum_r (q_i)_r g_r(x)

modulo the monic cyclotomic polynomial Phi_d. The tuple of all integer
remainders is the label's cyclotomic signature. Two different signatures
supply a nonzero witness in the theorem. Hence only labels in the same
signature class can have arbitrarily deep later comparisons.

This test uses integer polynomial division only. No algebraic-number
package or numerical root approximation is needed to establish
noncollision. Norms are needed only to request an explicit numeric
upper bound on the depth.

### Special case: B is a power of two

In this case unequal rank-charge vectors necessarily have unequal
cyclotomic signatures. Indeed, if A_ij vanished at every nontrivial
B-th root, then (x^B-1)/(x-1) would divide A_ij. Its coordinate-sum
condition gives A_ij(1)=0, so x^B-1 divides A_ij. But deg A_ij<=B and
its constant coefficient is zero. Thus A_ij must vanish identically.
Finally, the exponent pairs {B-r,r+1}, 0<=r<N, are disjoint and cover
{1,...,B}; therefore A_ij=0 implies q_i=q_j.

This is not asserted for B with several distinct prime factors. The
N=14 example below has distinct rank-charge vectors but one pair of
coincident cyclotomic signatures.

## 5. Conditional binary reduction for an arbitrarily large component

Assume rank-count rigidity and that every cyclotomic signature class
has size at most two.

For every pair in different classes, choose a finite bound from the
separation theorem. There are finitely many pairs. Let D exceed all
these bounds and include the depth defining the existing lower
profile. Then no comparison between different signature classes can
remain unresolved through degree D.

The finite-depth normal-form theorem supplies a sufficiently late
periodic polynomial profile through degree D. Refine its phase period
to include the signature-class assignment to slots: a tied degree-D
group contains only one class, so class routing is deterministic,
regardless of any permutation within that class. The finite state
consisting of the numerical phase and each slot's class is therefore
eventually periodic. After this phase lift, every compatible transport
edge preserves a fixed class. Hence every remaining component is a
singleton or a closed pair, even if the original component had dozens
of labels. Including this lift prevents a deterministic permutation
over a shorter numerical period from joining different classes in
the graph merely through phase wraparound.

For a residual pair, the unordered rank occupancy is now periodic,
possibly after enlarging the phase period. The binary parity criterion
therefore applies. In particular, if every original lower tie phase
available to this pair is off the global second-moment mean, the
physical mean obstruction excludes monomial resonance at every lifted
phase. Each pair then has bounded comparison depth. The finitely many
singletons and pairs together give a finite global depth bound and
therefore eventual labelled periodicity.

The essential point about phase enlargement is that it does not change
the original lower x profile: a refined tie lies over one of its
original lower tie phases. Off-mean checks at all those original
phases remain valid after every lift.

This is a general theorem with finite hypotheses. It does not prove
that rank rigidity, binary signature classes, or binary nonresonance
hold for every canonical N.

## 6. Targeted tests of the proposed binarization hypothesis

The test was deliberately challenged on existing interacting networks,
including the size 27 and size 56 cases. These checks do not extend the
previous finite-N catalogue.

| N | Lower start | Lower period | Relevant component size | Cyclotomic class sizes |
|---|---:|---:|---:|---|
| 4 | 15 | 12 | 2 | 2 |
| 8 | 110 | 16 | 3 | 2,1 |
| 8 | 110 | 16 | 2 | 1,1 |
| 12 | 449 | 72 | 3 | 1,1,1 |
| 14 | 5789 | 196 | 14 | 2 and twelve singletons |
| 30 | 13230 | 1620 | 27 | All singletons |
| 60 | 373908 | 9600 | 56 | All singletons |

The residual doubletons, using zero-based labels in the reconstructed
canonical prefix, are

    N=4:  {1,3};
    N=8:  {1,6};
    N=14: {8,10}.

For N4, N8 and N14, every persistent third-level tie phase is off the
global second-moment mean: respectively 1, 3, 25 events were checked.
Thus all the residual doubletons satisfy the higher-level binary mean
criterion, after any required refinement of the phase period.

At N=30 and N=60 every label in the large component is already separated
by the cyclotomic theorem. No residual binary criterion is needed for
those components. At N=12 the same is true for its triple.

The N=60 test reconstructs all 373908 paired blocks of the genuine
canonical prefix. Comparisons are carried through degree 4, and any
unresolved prefix tie aborts; none occurred. The reconstructed second
and third moments are checked against the discovered lower profile
before charges are assigned.

## 7. Reproduction and dependencies

All rank and cyclotomic scripts use the Python standard library. The
[reproduction guide](rank/README.md) lists the independent expanded and
contracted checks, controls, and exact dependencies.

From the repository root, reproduce the signatures and residual-pair checks:

```sh
python3 research/rank/rank_holonomy_charges.py --output signatures_actual.json
python3 research/rank/rank_holonomy_mean_checks.py --output means_actual.json
```

Compare these outputs with [the signature report](rank/rank_holonomy_cyclotomic_checks.json)
and [the mean-check report](rank/rank_holonomy_cyclotomic_mean_checks.json).
They contain exact integer values and no timing fields. The signature
generator verifies the entry moments and rejects any unresolved
fourth-degree comparison in the canonical prefix.

## 8. The remaining all-N problem

The new route does not require a universal degree-four bound. It would
suffice to prove that the canonical triangular-weight process eventually
has rank-rigid lower components whose cyclotomic signature classes are
at most binary, and to rule out physical resonance in the resulting
pairs. The required depth could depend on N and on the particular
cyclotomic norms.

The tests above support that route, including two large interacting
components, but do not establish its hypotheses uniformly. No argument
currently proves that an arbitrary canonical terminal component with
unbounded depth must belong to a binary signature class.
