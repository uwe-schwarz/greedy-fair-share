# What monomial parity resonance means for a physical binary component

Research derivation, 2026-11-26. This supplements the [parity criterion](PARITY_OBSTRUCTION.md) for
closed two-player components. It does not prove that monomial resonance
cannot occur for N >= 3.

Let B=2N. Fix a phase at absolute block m_0 of a closed binary component's
second-moment base cycle, whose period is P blocks or L=BP individual turns.
Write x=1+z. Let T_0 in F_2[x] be the union-of-positions polynomial of the
two players up to the phase in question, measured by ages at its boundary.
Let K be their union-of-positions polynomial over the following complete
base period, measured by ages at its end. Thus

$$
R=(x^L+1)T_0+K.
$$

Both T_0 and K have zero constant coefficient. If m_0>0, then
1 <= deg T_0 <= Bm_0 and 1 <= deg K <= L. Because every turn belongs to
only one player, their F_2 coefficients are exactly the zero-one occupancy
indicators; there is no cancellation within either union polynomial.
Consequently their ordinary integer Hamming weights are

$$
|T_0|=4m_0,\qquad |K|=4P.
$$

## Proposition

If R/K is a Laurent monomial x^c, then in fact

$$
c=Bm_0,
\qquad d=\gcd(L,c)=B\gcd(P,m_0).
$$

There is a polynomial W of degree at most d with W(0)=0 such that

$$
K=W\sum_{j=0}^{L/d-1}x^{jd},
\qquad
T_0=W\sum_{j=0}^{c/d-1}x^{jd}.
\tag{1}
$$

In particular, the pair's occupancy indicator is periodic from the first
turn onward, with a period d that divides both the selected whole-base
period L and the current prefix length Bm_0. This concerns occupancy by
either member of the pair, not the internal ordering of the two labels.

**Proof.** First suppose m_0>0. The term (x^L+1)T_0 has degree L+deg T_0,
which exceeds deg K. Thus R has degree L+deg T_0. If R=x^c K, then

$$
c=L+\deg T_0-\deg K>0.
$$

The identity R=x^c K becomes

$$
(x^L+1)T_0=(x^c+1)K.
$$

Set d=gcd(L,c). Euclid's algorithm for the exponents gives

$$
\gcd(x^L+1,x^c+1)=x^d+1
$$

over F_2 as well, with multiplicities included. After dividing by the
gcd, the two quotient polynomials are coprime, so

$$
K=W\frac{x^L+1}{x^d+1},
\qquad
T_0=W\frac{x^c+1}{x^d+1}
$$

for some W in F_2[x]. The degree bound on K gives deg W <= d. All quotient
polynomials have constant coefficient one, so W(0)=0 follows from K(0)=0.
Since d divides L and c, these quotients are exactly the geometric sums
in (1).

Copies of W in those sums do not overlap: deg W <= d, and a possible
degree-d term cannot collide with the next copy's constant term because
W(0)=0. Hence ordinary integer Hamming weights satisfy

$$
|K|=(L/d)|W|,\qquad |T_0|=(c/d)|W|.
$$

It follows that

$$
\frac cL=\frac{|T_0|}{|K|}
=\frac{m_0}{P},
$$

so c=Bm_0 and d=B gcd(P,m_0). Equation (1) shows that both the entire
past occupancy and each future base-period occupancy repeat the same
d-turn block. The phase is aligned because d divides both lengths.

If m_0=0, T_0=0 and R=K, so c=0, d=L, and the same statement holds with
the empty prefix. ∎

Conversely, if the occupancy indicator has already been periodic from
turn zero with a period dividing L and Bm_0, the geometric-sum identities
give R=x^(Bm_0)K. Thus the exceptional monomial condition has an elementary
combinatorial meaning at a phase where the occupancy pattern is aligned.

## Exact valuation in the monomial case

If R=x^c K, the parity recurrence gives

$$
(x^L+1)\overline D_k=K(x^{Lk+c}+1).
$$

For a nonzero exponent Lk+c,

$$
v_1(\overline D_k)
=v_1(K)+2^{v_2(Lk+c)}-2^{v_2(L)}.
$$

With the convention v_2(0)=+infinity, a monomial ratio can still give a bounded parity valuation if
v_2(c)<v_2(L). Unbounded parity valuations occur only in the resonant
congruence case c divisible by 2^(v_2(L)). Even then, this is an obstruction
to the parity proof, not a proof of aperiodicity over the integers.

## Potential next question

A sufficient way to exclude all binary parity exceptions would be to prove
that no nontrivial closed pair has a purely periodic occupancy indicator
from turn zero under the canonical greedy construction. This statement has
not been proved here and should itself be tested before being adopted as
a theorem target. The proposition above only translates the existing
algebraic exception into a concrete combinatorial condition.
