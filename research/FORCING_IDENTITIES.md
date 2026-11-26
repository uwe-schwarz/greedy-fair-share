# Exact identities for the unresolved universal step

Date: 2026-11-26. The identities and conditional conjugation below are
proved; they do not prove universal terminal-component binarization.

## 1. The quadratic increment is a uniform pair/triple minimum rule

Write k=N-1-r for the number of players after rank r. Then

    v_r=binom(N-r,2)=k+binom(k,2).

For a strict ordering of x, the rank-assigned increment vector is the
gradient of the concave piecewise-linear potential

    Phi(x)=sum_(unordered pairs {i,j}) min(x_i,x_j)
           +sum_(unordered triples {i,j,k}) min(x_i,x_j,x_k).

Indeed, a player with k larger opponents is the minimum in exactly k
pairs and binom(k,2) triples. At ties, the lexicographic order supplies
one consistent winner in each pair and triple.

Thus each block simultaneously awards one triangular-load unit to the
least player in every pair and every triple. The uniform triple term
is absent exactly at N=2. Adjacent ranks r,r+1 differ by
N-r-1=1 plus the number of players after that pair.

This identifies a specific feature that a universal proof could use.
It is not a proof that positive triple coupling prevents unlimited
cancellation: the lower dynamics can have large interacting components,
and the relevant high-depth ties need not be simultaneous.

## 2. Exact full-score rank differences

For r<s,

    g_r(x)-g_s(x)
       =x^(r+1) (x^(s-r)-1) (x^(B-r-s-1)-1),  B=2N.

Both exponents are positive, and they have opposite parity. Over F2,
ord_(x=1)(x^m-1)=2^v2(m). Consequently every nonzero rank-forcing
difference has order

    2^v2(s-r)+2^v2(B-r-s-1)=1+2^a,   a>=1.

For adjacent ranks the even exponent is2(N-r-1), giving order
1+2^(1+v2(N-r-1)). Different adjacent gates can therefore have different
parity-adic forcing orders. This is a restriction on rank forcing, not
yet a restriction on accumulated history polynomials: their
cancellations may involve many blocks and gates.

## 3. Full-germ conjugation supplied by rank rigidity

Fix a rank-rigid component and let h_v in Z^N be its exact centered
rank-count potential. Form the polynomial potential

    H_v(x)=sum_r (h_v)_r g_r(x).

For centered score X_i=s G_i-sum_(j in C)G_j and an allowed edge v->w,
rank rigidity gives the exact recurrence

    X_i' = x^B X_i + H_w-H_v.

Set Y_i=X_i-H_v. Then

    Y_i'=x^B Y_i+(x^B-1)H_v.

Dividing by the common positive germ x^B-1 gives

    W_i=Y_i/(x^B-1),
    W_i'=x^B W_i+H_v.                                 (1)

At a comparator, the two H potentials agree exactly, because the slots
have a common predecessor. Subtracting them therefore preserves the
comparison. Division by x^B-1 is positive for x>1 and also preserves
order, while reducing the order of every compared difference by one.
Thus (1) is an exact conjugation of the unresolved comparison dynamics,
not a Taylor truncation.

The centered forcing has vanishing constant and first coefficients,
so the potentials can be normalized likewise; the local division is
well-defined as a Laurent germ, and in the present centered score
setting is regular at x=1.

This transformation exposes the source of deeper forcing as the
finite vertex potential H. It does not immediately terminate the
hierarchy: H need not itself be a coboundary. Its fourth-moment
obstruction is the centered-y holonomy already identified in
RANK_RIGIDITY_CHECKS.md.

### 3.1 When one reduction is integral and decreases polynomial degree

Suppose every label in the component has the same exact rank-charge
vector q. Put Q(x)=sum_r q_r g_r(x) and define the shifted potential
\(\widetilde H_v=H_v+Q\). This common change leaves every edge increment
and every comparison unchanged. Modulo x^B-1, aging disappears, and
the rank-charge identity gives \(X_i-\widetilde H_v=0\). Therefore

$$
W_i=\frac{X_i-\widetilde H_v}{x^B-1}\in\mathbb Z[x],
\qquad W_i'=x^B W_i+\widetilde H_v.
$$

Since H_v and Q have degree at most B, at a fixed entry time the
quotient has degree at most max(deg X_i,B)-B, with the zero polynomial
handled separately. Thus this one reduction has an exact polynomial
degree descent. Equal cyclotomic signatures alone are insufficient
when B has several distinct prime factors: they need not imply
divisibility by the entire polynomial x^B-1.

The argument does not automatically iterate. The new forcing H_v is
phase dependent, and rank rigidity of the original forcing does not
make H_v a coboundary. Also, advancing the entry time before each
reduction can increase the degree again. A terminating descent would
need an additional theorem preserving integrality and controlling one
fixed starting history through successive refinements.

### 3.2 Exact counterexample to automatic iteration

The canonical N=8 triple is rank rigid, but integrating its first
centered vector potential around the same graph gives the nonzero
defect

$$
(72,-24,-24,-120,-24,72,-24,72).
$$

The corresponding combination of the rank-score polynomials has its
first nonzero coefficient at degree four, with value 9408. Therefore
the next potential is not a coboundary on this graph. The other binary
component at N=8 also fails, with first nonzero coefficient -1472.

The [exact probe](rank/rank_holonomy_desubstitution_probe.py) and
[recorded defects](rank/rank_holonomy_desubstitution_probe.json) reproduce
this obstruction. It blocks an inference of repeated rigidity from
one successful vector-potential test; it does not obstruct a later
refinement using additional moments.

## 4. A precise local obstruction to a multi-player two-block reset

Suppose an isolated tied group of m players uses the same consecutive
ranks r,...,r+m-1 in two successive blocks. Equal initial loads make
the second assignment the reverse of the first. For j=0,...,m-1,

    v_(r+j)+v_(r+m-1-j)
      =constant+j^2-(m-1)j.

This is constant for m=2 and nonconstant for every m>=3. Thus the
quadratic rule forbids a full two-block second-moment reset of such an
isolated group of size at least three. Applied at the global initial
state, it explains why the immediate binary Thue-Morse doubling does
not extend unchanged to N>=3.

The unproved global step is substantial: an arbitrary terminal
comparison component need not meet simultaneously, remain on the same
consecutive ranks, or reset after two blocks. Large examples such as
the N14 component interact through many pair gates. The local identity
must not be promoted to a theorem that every unbounded-depth component
is binary.

## 5. Obstacles any attempted universal argument must respect

- The same canonical second-moment cycle can support a noncanonical
  physical third-level orbit with nonzero rank-count holonomy (N4).
- Strict convexity plus zero origin does not force rank rigidity; the
  six-weight counterexample is preserved separately.
- Equal lower moments do not imply equal rank counts even in a short
  canonical prefix (N5, block4).
- An abstract connected N8 full-germ network admits a resonant binary
  Thue-Morse orbit for unrealizable entering germs. Physical paired
  history is a necessary input to the successful nonresonance argument.

The cyclotomic signature theorem supplies one rigorous way to turn
rank rigidity into a terminal-class restriction. Proving that the
canonical signature classes are always at most binary remains open
within this investigation.
