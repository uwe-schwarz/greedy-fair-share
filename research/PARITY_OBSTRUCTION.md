# A parity obstruction to unbounded comparison depth

Research derivation, 2026-11-26. This is a sufficient criterion for a closed binary comparison component. It does not establish that the criterion holds for every component of every N, and it does not assume that degree four suffices.

## 1. The binary component modulo two

Write x = 1+z. Fix a closed two-player component of the finite second-moment transport graph, and fix one phase of its base cycle. Let L be the number of individual turns in a whole base period. Let D_k(x) be the full score-polynomial difference of the two fixed player labels at this phase after k base periods.

Modulo two, the signs of their contributions disappear. The union of the two players' positions during a base period is fixed by the component, independently of the unresolved internal label choices. Therefore, in F_2[x],

$$
\overline D_{k+1}=x^L\overline D_k+K,
$$

where K is the fixed indicator polynomial of that union of positions, measured by their ages at the end of the period. Define

$$
R=(x^L+1)\overline D_0+K.
$$

Then direct telescoping gives

$$
(x^L+1)\overline D_k=x^{Lk}R+K. \tag{1}
$$

The plus signs are also minus signs in characteristic two.

For a nonzero polynomial or rational function f, let v_1(f) be its order of vanishing at x=1. The first deciding moment of the integer difference D_k is v_1(D_k), equivalently its first nonzero coefficient as a polynomial in z=x-1. Reduction modulo two can only increase this order:

$$
v_1(D_k)\le v_1(\overline D_k).
$$

Consequently, a uniform finite bound on the right side of (1)'s valuation is enough to bound all moment degrees needed at this phase.

## 2. Rational functions that are not monomials cannot approximate monomials arbitrarily well

**Lemma.** Let a,b in F_2[x] be coprime, with a(0)=b(0)=a(1)=b(1)=1. Suppose a/b is not a square in F_2(x). For every integer j,

$$
v_1(a-x^j b)\le \deg a+\deg b+1. \tag{2}
$$

Negative j are allowed; the expression is then a Laurent polynomial, regular at x=1.

**Proof.** Let h=a-x^j b and epsilon=j modulo 2. Differentiation in F_2(x) gives

$$
xbh'-(\epsilon b+xb')h
=x(ba'-ab')-\epsilon ab=:C_\epsilon. \tag{3}
$$

Both possible C_epsilon are nonzero. If C_0=0, then (a/b)'=0, hence a/b is a square in F_2(x), contrary to hypothesis. If C_1=0, then (x a/b)'=0, hence x a/b is a square. Its order at x=0 is 1 because a(0)=b(0)=1, which a square cannot have.

Here we use the elementary characteristic-two fact that the kernel of d/dx on F_2(x) is F_2(x^2), the set of rational squares. It follows either from the basis {1,x} over F_2(x^2) or by writing a reduced fraction and comparing its irreducible-factor multiplicities.

If v_1(h)=m, then v_1(h') is at least m-1. Since all other multipliers in the left side of (3) are regular at x=1, v_1(C_epsilon) is at least m-1. On the other hand, C_epsilon is a nonzero polynomial of degree at most deg a+deg b. Hence m is at most deg a+deg b+1. This proves (2).

## 3. An explicit bound for arbitrary nonmonomial ratios

Assume R and K are nonzero. Compute their polynomial gcd G in F_2[x] and write

$$
R=G x^r A^{2^s},\qquad K=G x^t B^{2^s}, \tag{4}
$$

where A(0)=B(0)=1 and s is chosen as large as possible after removing the powers of x. The reduced A,B are coprime. If R/K is not a Laurent monomial x^c, then A,B are not both 1, and A/B is not a square.

If A(1) and B(1) differ, the factor after G in x^{Lk}R+K is nonzero at x=1 for every k. In this case

$$
v_1(\overline D_k)=v_1(G)-2^{v_2(L)}.
$$

Otherwise A(1)=B(1)=1, because they are coprime. In this case define

$$
\mathcal B=v_1(G)+2^s(\deg A+\deg B+1)-2^{v_2(L)}. \tag{5}
$$

Then every k satisfies

$$
v_1(D_k)\le v_1(\overline D_k)\le\mathcal B. \tag{6}
$$

**Proof.** Set n=Lk+r-t. The factor after G and a harmless power of x is

$$
x^n A^{2^s}+B^{2^s}.
$$

If 2^s does not divide n, its order at x=1 is exactly 2^{v_2(n)}, which is less than 2^s: the two Frobenius-power factors are constant modulo (x-1)^{2^s}, while x^n-1 has that smaller order. This also holds for negative n. If 2^s divides n, write n=2^s j. The expression is

$$
(x^j A+B)^{2^s},
$$

and the preceding lemma, with (a,b)=(B,A), bounds its order by 2^s(deg A+deg B+1). Finally,

$$
v_1(x^L+1)=2^{v_2(L)},
$$

so (1) gives (5)-(6). In particular, the bound is explicit and uniform in k.

If exactly one of R,K vanishes, (1) directly gives a constant finite valuation instead. If both vanish, this argument gives no bound. In the physical binary component K is nonzero, since the component occupies turns.

## 4. Consequence for closed binary comparison components

**Criterion.** At every phase at which the two players' second moments agree, form R and K as above. If every nontrivial ratio R/K is not a Laurent monomial in F_2(x), then there is a finite uniform bound on all moment degrees needed for comparisons inside this component.

There are finitely many phases, so take the maximum of their bounds and degree two. Phases with unequal second moments already decide at degree two. The criterion is unaffected by the actual higher-moment tie choices: the modulo-two recurrence used only the fixed union of the two players' positions.

Together with the [finite-depth normal-form theorem](../FINITE_DEPTH.md), this yields eventual periodicity of the labels inside this component. The component's other moment values may keep growing; the theorem supplies eventual phasewise polynomial values after normalization.

A monomial ratio makes this criterion **inconclusive**. It does not establish aperiodicity. For example, the unperturbed N=2 component has the monomial resonance and does exhibit Thue-Morse aperiodicity, but other resonant initial states could still terminate by information lost modulo two.

## 5. Constant-forcing special case without importing a higher-layer theorem

When the full integer return is

$$
D_{k+1}=U D_k-\operatorname{sign}(D_k)K,
\qquad U=x^L,
$$

with K positive as a germ at x=1 from above, bounded comparison depth also gives an elementary termination proof.

Let q=v_1(K), and inspect the coefficient of degree q in D. If a lower coefficient is nonzero, it fixes the sign forever. Otherwise this coefficient follows the scalar correction d -> d-sign(d)K_q. A nonintegral d/K_q reaches a strict two-cycle. If d/K_q is an integer, finitely many steps bring it to zero. At such a zero, the next two signs are opposite, and the two-step map is

$$
D_{k+2}=U^2D_k-\operatorname{sign}(D_k)(U-1)K.
$$

Its forcing has valuation q+1. Repeating this construction could only continue indefinitely if the actual difference attained arbitrarily high valuations. The parity bound rules that out. Thus it stops at a finite level and gives a periodic sign word. This argument does not need a uniform degree-four bound.

## 6. Current scope

The explicit bound is intentionally loose. Its role is to prove finite termination, not to predict the observed period efficiently. It can be computed using polynomial gcds, powers of x, formal derivatives, and Frobenius roots; no irreducible factorization is necessary.

The [reproducible component experiments](STRUCTURE_EXPERIMENTS.md) check the full-period criterion at every tie phase of 54 closed binary components for N>2, including variable-forcing cases. All pass. The N=2 control is monomial, as expected. This certifies those components, not the complete sequences for their player counts.

The outstanding universal tasks are to show that all relevant components satisfy an appropriate nonresonance condition, to treat resonant binary components, and to handle components with more than two labels. No such all-N conclusion is asserted here.

The [physical resonance lemma](PARITY_RESONANCE.md) identifies the monomial exception with a pair-occupancy pattern already periodic from turn zero, with a period dividing both the base period and the selected prefix length. The [mean obstruction](MEAN_OBSTRUCTION.md) gives a cheaper sufficient test for excluding it.
