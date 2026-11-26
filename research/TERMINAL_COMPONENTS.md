# A terminal component has a flat signed generating function

Research derivation, 2026-11-26. This is a necessary condition for an
infinite-depth obstruction, not a proof that the obstruction is impossible.

## 1. Precise statement

The [terminal-component reduction](NETWORK_CHARGES.md) gives a
fixed player set C of size s>=2 such that every fixed age-moment discrepancy
between its members is bounded in time. Its aggregate turn occupancy is
eventually periodic.

For i in C define the bounded integer turn sequence

$$
a_t=s\mathbf1_{\{\text{turn }t\text{ belongs to }i\}}
 -\mathbf1_{\{\text{turn }t\text{ belongs to }C\}},
\qquad
A_i(q)=\sum_{t\ge0}a_tq^t\quad(0<q<1).
$$

Then, for every integer k>=0,

$$
A_i(q)=O((1-q)^k)\qquad(q\uparrow1).
\tag{1}
$$

In particular, writing F_i(q) for player i's turn generating function and
F_C(q) for the aggregate, every F_i has the same full asymptotic expansion
as F_C/s at q=1. The aggregate F_C is rational, since its coefficient word
is eventually periodic. The remainder in (1) is called flat at q=1.

## 2. Proof

Let

$$
D_k(n)=\sum_{t<n}a_t\binom{n-t}{k}.
$$

At paired-block boundaries these are centered age moments, hence bounded
for every fixed k. The finitely many intermediate turns preserve boundedness:
aging for at most B-1 steps is a fixed triangular binomial transformation,
and there are only finitely many new bounded contributions. A finite initial
transient also has a finite maximum. Thus |D_k(n)|<=C_k for all n.

For k>=1, absolute convergence at 0<q<1 permits changing the summation order:

$$
\begin{aligned}
\sum_{n\ge0}D_k(n)q^n
 &=\sum_{t\ge0}a_tq^t\sum_{h\ge1}\binom hkq^h\\
 &=A_i(q)\frac{q^k}{(1-q)^{k+1}}.
\end{aligned}
$$

The left side has absolute value at most C_k/(1-q). Consequently

$$
|A_i(q)|\le C_k q^{-k}(1-q)^k,
$$

which proves (1). QED.

## 3. What this does not imply

Flatness does not itself force a simultaneous tie, a reset from the
origin, a binary component, or a Thue-Morse word. Multicolor Prouhet
constructions show why an additional greedy-dynamics theorem is necessary.

For example, color a nonnegative integer t by its base-s digit sum modulo
s. For each nontrivial sth root of unity omega, the signed generating
polynomial of a complete block of length s^h factors as

$$
\sum_{t=0}^{s^h-1}\omega^{\operatorname{digitsum}_s(t)}x^t
=\prod_{j=0}^{h-1}
  \left(\sum_{r=0}^{s-1}\omega^r x^{r s^j}\right).
$$

Every factor vanishes at x=1, so this polynomial is divisible by
(x-1)^h. Fourier inversion over the colors implies equal power sums
through degree h-1 in each complete block. The same holds for any
aligned block of length s^h: its high digits merely permute the colors.

For a fixed moment degree k, take h>k and decompose any prefix into aligned
complete blocks of length s^h plus a final remainder shorter than s^h.
The complete blocks contribute zero to every centered age moment through
degree k, including after aging, since age moments are polynomials in the
turn positions. The remainder has uniformly bounded length and age.
Thus this multicolor sequence also has bounded centered age moments at
every fixed degree and flat signed generating functions.

This example concerns the necessary discrepancy condition only. It does
not follow the canonical greedy fair-share rule and is not a counterexample
to the conjectured periodicity. It demonstrates the exact logical gap in
trying to infer a binary origin reset from all-orders bounded discrepancy
or flatness alone.

The period-prime restriction on finite projections likewise does not
remove this gap: such Prouhet constructions have finite projection periods
supported on primes dividing s, already among the primes at most N when
s<=N.

## 4. Even a prescribed finite prefix does not force an obstruction

The necessary bounded-discrepancy property also admits arbitrary finite
starting words when the greedy rule is dropped. Let a prescribed word
of length L use colors in Z/sZ. For block index b and within-block
position r, give turn Lb+r the color

$$
c_r+\operatorname{digitsum}_s(b)\pmod s.
$$

Block zero is exactly the prescribed word. For each fixed r and each
nontrivial Fourier character of the colors, a complete aligned run of
s^h blocks has the Prouhet product from section 3, multiplied by a
constant phase and evaluated at x^L. Hence its centered moments through
degree h-1 vanish. Summing over r preserves that property. Decomposing
any prefix into complete blocks of length Ls^h and a bounded remainder
proves bounded discrepancies at every fixed degree, just as above.

In the binary case this is the familiar signed-series product
P(q)T(q^L), with P encoding the prescribed finite prefix and T the
signed Thue-Morse series. Its coefficients are still signs because the
copies of P occupy disjoint blocks.

Thus initial history plus all-orders bounded discrepancy does not force
an origin reset. Any such reset theorem for the present problem must
use the greedy choices throughout the continuation.
