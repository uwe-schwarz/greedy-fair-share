# Reciprocal rank forces and an integer degree-four normal form

Research note, 2026-11-26. The algebraic statements in Sections 1--4 are
proved here. They do **not** prove eventual finite comparison depth for
the canonical process with every `N >= 3`. Sections 5--6 give exact
obstructions to two tempting local proof arguments.

## 1. An exact common normalization

Here x is the age variable, the reciprocal of the original failure
probability. Let `B = 2N`, let `x = 1 + z` with `z` a positive
infinitesimal, and put

$$
g_r(x)=x^{B-r}+x^{r+1},\qquad
k=N-1-r,\qquad
v_k=\frac{k(k+1)}2.
$$

Thus `k` runs from `N-1` at the first rank to zero at the last rank. Set

$$
\alpha(x)=(x-1)^2(x+1)x^{N-1},
\qquad s=x+x^{-1}-2.
$$

The factor `alpha` is positive as a formal germ and has order two at
`x=1`. Direct factorization gives

$$
\begin{aligned}
g_r(x)-g_{N-1}(x)
 &=x^{N-k}(1-x^k)(1-x^{k+1}),\\
\frac{g_r(x)-g_{N-1}(x)}{\alpha(x)}
 &=x^{1-k}{k+1\brack2}_x=:f_k(s).
\end{aligned}\tag{1}
$$

For `k=0`, define `f_0=0`. The Gaussian binomial in (1) has degree
`2(k-1)`, so its multiplication by `x^(1-k)` is reciprocal invariant.
Consequently it is a polynomial in `x+x^(-1)`, and hence in `s`.

Let the common scalar `A_m(x)` satisfy

$$
A_0=0,\qquad A_{m+1}=x^B A_m+g_{N-1}(x).
$$

Define the normalized score

$$
H_i(m,x)=\frac{G_i(m,x)-A_m(x)}{\alpha(x)}.
$$

The exact dynamics is

$$
\boxed{\quad H_i'=x^B H_i+f_{N-1-r_i}(s),\qquad H_i(0)=0.\quad}\tag{2}
$$

The scores `H_i` have the same ordering as the original scores `G_i`.
They are analytic formal germs at `x=1`; Laurent powers of `x` in (1)
cause no singularity there.

## 2. Positive binomial coefficients and a Newton basis

For every integer `k >= 0`,

$$
\boxed{\quad
f_k(s)=\sum_{j=0}^{k-1}\binom{k+j+1}{2j+2}s^j.
\quad}\tag{3}
$$

The sum is empty for `k=0`. In particular,

$$
\begin{aligned}
f_0&=0,\\
f_1&=1,\\
f_2&=3+s,\\
f_3&=6+5s+s^2,\\
f_4&=10+15s+7s^2+s^3.
\end{aligned}
$$

Here is a short proof of (3). From (1), or directly by subtracting
adjacent forces,

$$
f_k-f_{k-1}=x^{-(k-1)}(1+x^2+\cdots+x^{2k-2}).
$$

These adjacent differences satisfy the Chebyshev recurrence with
multiplier `x+x^(-1)=s+2`. Summing that recurrence gives

$$
f_{k+1}-2f_k+f_{k-1}=s f_k+1,\qquad f_0=0,\quad f_1=1.\tag{4}
$$

The right side of (3) has these same initial values and recurrence.
Indeed, the second difference in `k` of its constant coefficient is
one, while for `j >= 1`, Pascal's identity gives

$$
\binom{k+j+2}{2j+2}
-2\binom{k+j+1}{2j+2}
+\binom{k+j}{2j+2}
=\binom{k+j}{2j},
$$

which is its coefficient of `s^(j-1)`. This proves (3).

The coefficients also have the exact Newton form

$$
\boxed{\quad
\binom{k+j+1}{2j+2}
=\frac{2^{j+1}}{(2j+2)!}
  \prod_{\ell=0}^{j}\left(v_k-\frac{\ell(\ell+1)}2\right).
\quad}\tag{5}
$$

To verify (5), pair the factors of
`(k-j)(k-j+1)...(k+j+1)` around `k+1/2`:

$$
(k-\ell)(k+\ell+1)
=k(k+1)-\ell(\ell+1).
$$

At the triangular values `v_k`, (5) vanishes for `j >= k`, as required.
The first two nonconstant-in-rank coefficients are

$$
[s^0]f_k=v_k,\qquad
[s]f_k=\binom{k+2}{4}=\frac{v_k(v_k-1)}6.\tag{6}
$$

All displayed binomial coefficients are nonnegative, and are positive
when `0 <= j < k`. The polynomials `f_1,...,f_(N-1)` form a basis of the
polynomials of degree at most `N-2`, because `f_k` is monic of degree
`k-1`. In particular, for `N>2` the rank-force family cannot be made
constant in `s` merely by dividing every force difference by one common
analytic unit: `f_1=1` would fix that unit while `f_2=3+s` varies.

This last global statement must not be confused with the two-rank
normalization in Section 5, where one difference is all that matters.

## 3. Clean integer coordinates through degree four

Use the multiplier itself as the local parameter:

$$
u=x^B-1,\qquad x=(1+u)^{1/B}.
$$

This preserves formal order because `u=Bz+O(z^2)` has positive linear
coefficient. Its reciprocal variable has expansion

$$
s=(1+u)^{1/B}+(1+u)^{-1/B}-2
 =\frac{u^2}{B^2}-\frac{u^3}{B^2}+O(u^4).
$$

Write

$$
H_i=a_i+b_i u+\frac{c_i}{B^2}u^2+O(u^3).
\tag{7}
$$

Substituting (6)--(7) in the exact update (2) gives

$$
\boxed{\begin{aligned}
a_i'&=a_i+v_k,\\
b_i'&=b_i+a_i,\\
c_i'&=c_i+B^2b_i+\binom{k+2}{4},
\qquad k=N-1-r_i.
\end{aligned}}\tag{8}
$$

All three coordinates start at zero and remain integers. In particular,
there is no denominator in the canonical degree-four evolution.
The only rank-dependent reward newly appearing in the third line is

$$
\binom{k+2}{4}=\frac{v_k(v_k-1)}6.
$$

The first coordinate is the absolute triangular load. The second is its
accumulated sum. If `x_i=a_i-min_j a_j` and the earlier convention is
`y_i'=y_i+x_i`, then `b_i-b_j=y_i-y_j`: normalization changes only a
common scalar. Thus (8) is compatible with the established lower
`(x,y)` dynamics.

The binomial term is zero for both ranks available at `N=2`, since then
`k` is zero or one. It is nonzero for `k>=2`. This is an exact structural
distinction, but Section 5 explains why it is not by itself a proof that
every higher-player binary component separates.

For completeness, the absolute common sums are explicit. With

$$
V_N=\sum_{k=0}^{N-1}v_k=\binom{N+1}{3},\qquad
J_N=\sum_{k=0}^{N-1}\binom{k+2}{4}=\binom{N+2}{5},
$$

the zero-origin recurrence gives, after `m` paired blocks,

$$
\sum_i a_i=mV_N,\qquad
\sum_i b_i=\binom m2V_N,\qquad
\sum_i c_i=B^2\binom m3V_N+mJ_N.
$$

These are exact common gauges, independent of all tie choices.

## 4. Exact relation to the original moments

Let `D_j=M_(i,j)-M_(h,j)` be a difference of original age moments, and
write `Delta a=a_i-a_h`, and similarly for `b,c`. The common term `A_m`
cancels between players. The prefactor in (1) has expansion

$$
\alpha(x)
=2z^2+(B-1)z^3+(N-1)^2z^4+O(z^5),
$$

and `u=Bz+binom(B,2)z^2+O(z^3)`. Multiplication now gives

$$
\boxed{\begin{aligned}
D_2&=2\,\Delta a,\\
D_3&=(B-1)\Delta a+2B\,\Delta b,\\
D_4&=(N-1)^2\Delta a
      +2B(B-1)\Delta b+2\,\Delta c.
\end{aligned}}\tag{9}
$$

Therefore lexicographic comparison of `(a,b,c)` is precisely comparison
by moments through degree four. At a tie of the first two coordinates,
`D_4=2 Delta c`.

### An independent direct binomial proof

The same normal form can be derived without Gaussian binomials or a
formal change of parameter. Put

$$
w_j(r)=\binom{B-r}{j}+\binom{r+1}{j},\qquad
h_k=\binom{k+2}{4}.
$$

The rank-dependent parts satisfy

$$
\begin{aligned}
w_2(r)-w_2(N-1)&=2v_k,\\
w_3(r)-w_3(N-1)&=(B-1)v_k,\\
w_4(r)-w_4(N-1)&=(N-1)^2v_k+2h_k.
\end{aligned}\tag{10}
$$

For the fourth identity, write

$$
W(k)=\binom{N+k+1}{4}+\binom{N-k}{4}.
$$

Pascal's identity gives

$$
W(k+1)-W(k)
=\binom{N+k+1}{3}-\binom{N-k-1}{3}
=(N-1)^2(k+1)+2\binom{k+2}{3}.
$$

The last equality follows by writing
`binom(t,3)=((t-1)^3-(t-1))/6`. Summing from zero to `k-1`
proves the fourth identity in (10). The lower two follow in the same
way, or by expanding their quadratic and cubic binomials.

Now substitute (9)--(10) in the triangular moment updates

$$
\begin{aligned}
D_2'&=D_2+\Delta w_2,\\
D_3'&=D_3+B D_2+\Delta w_3,\\
D_4'&=D_4+B D_3+\binom B2D_2+\Delta w_4.
\end{aligned}
$$

They give the difference form of (8) exactly. Starting all the
coordinates at zero fixes the displayed common gauges. This provides
an independent algebraic verification of the integer normal form.

If rank-only rewards are coboundaries on an eventual lower comparison
network, then the third line of (8) immediately makes every closed
centered `c`-cost a multiple of `B^2`. In original fourth coordinates
this is the familiar factor `2B^2=8N^2`. This deduction is conditional
on the rank-coboundary property; (8) does not prove that property.

## 5. Positive force curvature does not locally exclude Thue--Morse

Here is an exact counterexample to a possible proof step, not a
counterexample to the canonical `N>2` conjecture.

Consider an abstract closed two-slot system which always uses the same
two distinct Gaussian rank forces `f_a(s)<f_b(s)`. Let

$$
\delta(x)=f_b(s)-f_a(s),\qquad \lambda=x^B.
$$

The difference `delta` is a positive analytic unit at `x=1`, with
constant coefficient `v_b-v_a>0`. Assign the larger force to the lower
score. If `D` is the difference of the two scores, then away from a
complete tie,

$$
D'=\lambda D-\operatorname{sgn}(D)\delta(x).
$$

Dividing by `delta` preserves every comparison and gives

$$
\boxed{\quad d'=\lambda d-\operatorname{sgn}(d).\quad}\tag{11}
$$

Start at a complete pair tie and choose the initial orientation so that
`d_1=1`. Let `tau_n=(-1)^(binary digit sum of n)`. The polynomials

$$
d_n(\lambda)=\sum_{t=0}^{n-1}\tau_t\lambda^{n-1-t}
$$

obey (11) in the formal germ `lambda=1+u`, `u>0`. A direct proof uses

$$
\begin{aligned}
d_{2m}(\lambda)&=(\lambda-1)d_m(\lambda^2),\\
d_{2m+1}(\lambda)&=\lambda(\lambda-1)d_m(\lambda^2)+\tau_m.
\end{aligned}
$$

The odd expression has sign `tau_m=-tau_(2m+1)`. The even expression
has the sign of `d_m`, so induction gives `sgn(d_n)=-tau_n` for every
`n>=1`, exactly the greedy rule. Consequently

$$
\boxed{\quad
d_{2^h}(\lambda)=\prod_{j=0}^{h-1}(\lambda^{2^j}-1).
\quad}\tag{12}
$$

Its order of vanishing at `x=1` is `h`, which is unbounded. This remains
true, for example, for `f_a=1` and `f_b=3+s`, where the difference
`delta=2+s` has nonzero positive curvature. That curvature is removed
by a harmless positive common factor in the two-score difference.

Thus neither positive coefficient formulas nor nonconstant fourth-order
forcing alone can rule out a binary infinite-depth mechanism. To apply
(11) as a counterexample to the original process, one would have to
embed this two-slot schedule into the canonical full `N`-player orbit.
No such embedding is claimed here. The restrictions on global rank
occupancy and the canonical starting history are exactly the missing
information in this abstract construction.

## 6. A reciprocal energy identity, and its exact limitation

For a fixed rank-history word, center `H_i` by their player average and
call the result `U_i`. Let

$$
w_r(x)=f_{N-1-r}(s)-\frac1N\sum_{k=0}^{N-1}f_k(s).
$$

Every `w_r` is reciprocal invariant. Hence the quadratic expression

$$
E(x)=\sum_i U_i(x)U_i(x^{-1})
$$

satisfies the exact update

$$
E'-E
=\sum_i w_{r_i}(x)
 \bigl(\lambda U_i(x)+\lambda^{-1}U_i(x^{-1})\bigr)
 +\sum_r w_r(x)^2.
\tag{13}
$$

No sign for the right side follows merely from the greedy rule. The
rule sorts `U_i(x)` for `x=1+z`, whereas reciprocal substitution reverses
the signs of odd first-differing coefficients. The same rank order
need not sort `U_i(x^(-1))`.

Moreover the reciprocal quadratic expression itself is not positive
on formal germs. In the two-slot construction, after two steps the
score difference is `D_2=delta(lambda-1)`, so

$$
E_2=\frac12D_2(x)D_2(x^{-1})
=-\frac{\delta(x)^2(\lambda-1)^2}{2\lambda}<0.
$$

Thus (13) is an exact identity, but it is not automatically a positive
or monotone energy. An argument using it to force separation would
need an additional inequality that is not established here.

## 7. Remaining gap

The reciprocal force basis and (8)--(9) are complete identities valid
for every `N`. They offer a simpler exact presentation of the
degree-four dynamics and identify its special triangular reward.
They do not prove any of the following:

1. Zero centered rank-count holonomy for every canonical eventual
   lower `(x,y)` comparison network.
2. Distinct canonical fourth-coordinate charges in all its components.
3. Termination after finitely many higher-moment refinements if the
   fourth coordinate does not already separate every label.

The independent no-global-return theorem for the canonical scalar
state is proved in [BINARY_RESONANCE.md](BINARY_RESONANCE.md), Section 2.1. It does not resolve the
proper-component obstruction illustrated in Section 5.
