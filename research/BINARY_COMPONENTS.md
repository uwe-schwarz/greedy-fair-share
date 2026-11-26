# A structural route through comparison components

Research note, 2026-11-26. This gives a rigorous reduction and a small new
derivation of the already-certified N = 7 case. It does not prove the
conjecture for all N.

## 1. The exact finite transport graph

At a paired-block boundary let the sorted, normalized second moments be
`x[0] <= ... <= x[N-1]`, in the normalization of section 7 of the proof.
Set `w[r] = binom(N-r, 2)`. Their next state is exactly

`T(x) = sort(x + w) - min(x + w)`.

Once this finite state has entered its cycle of length p, form vertices
`(phase, rank)`. Put an edge from `(t,r)` to `(t+1 mod p,s)` when

`x[t][r] + w[r] - min(x[t] + w) == x[t+1][s]`.

These are every possible destination of the player currently at that
rank; higher moments choose among destinations with the same second
moment. Every player stays in one weakly connected component forever.
The number of ranks belonging to a component is the same at every phase:
each one-step relation is a disjoint union of balanced complete
bipartite graphs between equal-value input fibers and output buckets.
Thus the components are closed groups of players, independently of all
higher-moment choices. This statement does not require identifying weak
components with strongly connected components.

Exact examples from `transport_components.py`:

| N | Base preperiod (blocks) | Base period (blocks) | Component sizes |
|---:|---:|---:|:---|
| 2 | 0 | 2 | 2 |
| 7 | 6 | 6 | 1, 1, 1, 2, 2 |
| 10 | 20 | 10 | 2, 8 |
| 13 | 13 | 9 | 1, 2, 4, 6 |
| 23 | 20 | 23 | 1, 2, 20 |

All the listed size-two components contain actual comparison events,
not just a deterministic permutation of two isolated ranks. Therefore
N >= 3 by itself does **not** rule out embedded binary dynamics.

## 2. A useful elementary binary-component lemma

Suppose a closed size-two component reaches equal second moments at
comparison times. Between two consecutive comparison times the rank
paths are forced by the second moments. Write x = 1+z, and let D(z)
be the full score difference of two fixed player labels. If the first
player takes the smaller rank at the initial comparison, propagation
along these forced paths gives

`D_next = x^L D + H(z)`.

Swapping the two players negates H. At the next comparison both second
moments agree again, so H has zero coefficients through degree two.
If D has nonzero third coefficient d, the current label order is fixed
by its sign. Hence at successive comparison events

`d_next = d + h_phase * sign(d)`,

where `h_phase = [z^3]H` and the finite list of h values is periodic.

If all return paths have the same negative h = -K and d/K is not an
integer initially, then no subsequent d is zero. The normalized
coefficient follows

`u_next = u - sign(u)`.

After finitely many steps it alternates between r and r-1, where
0 < r < 1. The two players' routing therefore becomes periodic, and
all higher moments are irrelevant to their decisions.

More generally, for a periodic list h_0,...,h_(s-1), if an integer orbit
never hits zero, its signs are eventually periodic. At complete
periods, outside a bounded interval all intermediate signs agree, so
the return map is `d -> d + C*sign(d)`, with C = sum h. If C <= 0,
the sampled orbit is bounded. If C > 0, it either remains bounded or
eventually escapes with a fixed sign. A bounded integer orbit with
finite phase is eventually periodic. When the gcd is positive, a simple sufficient nonzero
condition is `d_initial mod gcd(h_0,...,h_(s-1)) != 0`.

This lemma handles genuine binary subdynamics without assuming the
entire process has a finite set of higher moments. It does not cover
an orbit that reaches d = 0; that case passes the decision to higher
coefficients and is the remaining source of difficulty.

## 3. N = 7 from two scalar recurrences

After six paired blocks the second-moment base has the following
six-phase cycle. The rank weights are (21,15,10,6,3,1,0).

| Phase | Sorted normalized second moments |
|---:|:---|
| 0 | (0,1,2,4,5,9,14) |
| 1 | (0,2,2,4,6,8,13) |
| 2 | (0,0,1,3,4,8,12) |
| 3 | (0,2,2,4,5,8,14) |
| 4 | (0,1,2,4,6,9,13) |
| 5 | (0,1,1,3,4,7,12) |

There are three singleton components and two binary components.

The first binary component compares once per six blocks, at phase 2.
The initial third coefficient at absolute block 8 is d = 476, and its
return increment is h = -420. Therefore d/K = 17/15. After one return
the scalar is in its strict two-cycle. Its label routing has period
12 blocks, beginning no later than absolute block 14.

The second binary component compares every two blocks. Its rank path
for players assigned smaller/larger rank at a comparison is always
`(1,2), (5,3)`. Thus the full forcing polynomial is the same at all
three comparison phases, not just its observed leading coefficients.
At absolute block 7 its third difference is d = 616 and h = -140,
giving d/K = 22/5. After four returns the scalar is in its strict
two-cycle, at absolute block 15. Its label routing has period four
blocks.

The singleton rank paths repeat every six blocks. Consequently the
whole labelled sequence is periodic from block 15 with a valid period
`lcm(12,4,6) = 12` blocks, or 168 turns. The starting index is 210.
This agrees with the existing certificate. This argument alone does
not claim that 210 is the minimal onset or that 168 is the least
period; those refinements are already checked by the repository's
separate minimality computation.

The exact finite prefix used for these quantities is generated by the
same binomial update, carrying coefficients through degree eight and
rejecting any unresolved tie. It is recorded in the accompanying script;
there is no floating-point arithmetic.

## 4. Why the all-N step is still substantive

For N = 2 the corresponding scalar starts at zero, precisely the
case excluded by the strict binary lemma. Resolving repeated zeros
through successively higher coefficients produces the Thue-Morse
exception. For N >= 3, the presence of noninteger scalar offsets in
the examples explains why some embedded binary components stop this
recursion. A universal proof must establish a suitable finite-depth
separation property for every recurrent component, including larger
components, or characterize and exclude all Thue-Morse-like resonances.

For N = 10 and N = 13 the isolated binary offsets are respectively
52/5 and 32/91, so the same elementary lemma resolves those components.
For N = 23 the two return increments are -3680 and 1564. The initial
coefficient is 22908, and a direct finite scalar computation enters
the strict four-event cycle (184,1748,-1932,-3496). Thus that binary
component also resolves, although the simple nonzero-residue condition
does not apply (the gcd is 92 and the initial residue is zero).

The useful next experiment is to construct these component graphs,
derive their exact return increments, and record which components
ever need another moment level. This probes the precise missing
separation theorem far more directly than merely adding large N
certificates.

## 5. Rank-weight identities and a possible energy approach

Writing B = 2N and
`w_k(r)=binom(B-r,k)+binom(r+1,k)`, differences of rank weights satisfy

`Delta w_3 = ((B-1)/2) Delta w_2`,

`Delta w_4 = (1/12) Delta(w_2^2 + (B^2-6B+4)w_2)`.

The fourth rank weight is therefore a strictly convex quadratic in
the second rank weight, up to an additive constant. For N = 2 any
function on the two available weights is affine; for three or more
rank weights the quadratic term adds independent information.
This is a concrete possible ingredient for a Lyapunov or separation
argument. No monotone potential or universal termination theorem is
proved by this identity alone; sums along different histories can
still cancel.

## 6. A targeted N = 78 stress case: degree four resolves a deep binary tie

This section concerns only one closed binary component, not a proof of
periodicity for the entire 78-player sequence. The exact calculation is
reproducible with `python global_routes_n78.py`; output is recorded in
`global_routes_n78.json`.

The second-moment base has preperiod 309 blocks and period 72. Its
component occupying ranks 6 and 7 at phase zero is a closed pair. The
same two rank paths recur between every comparison, six blocks apart.
For this pair the full signed difference obeys

`D_next = (1+z)^936 D - sign(D) K(z)`,

where K has first nonzero coefficient `K_3 = 936`. At the first
comparison, absolute block 309, the two fixed player labels are
A = 46 and B = 27 (zero-based), and `D = G_B - G_A` has

`D_3 = 2971800`, `D_4 = 95006987238`.

The third coefficient decreases by 936 for 3175 comparison events,
so it first reaches zero at block 19359, or turn index 3020004.
At that exact point the fourth coefficient is

`D_4 = 4448685071838 > 0`.

Thus degree four decides the actual next order. No proposed word is
continued blindly through this zero.

Let X = (1+z)^936. Whenever the third coefficient is zero, the next
comparison has the opposite sign, because its third coefficient is
`-sign(D) * 936`. Two comparisons therefore give the exact return map

`D_next_next = X^2 D - sign(D) (X-1)K`.

Its first forcing coefficient is now at degree four and equals
`936^2 = 876096`. At the first degree-three zero, the normalized
degree-four value is

`4448685071838 / 876096 = 741447511973 / 146016`.

This is not an integer. Its remainder modulo 876096 is 122142.
Consequently degree four never vanishes at these two-comparison return
times, and the elementary binary lemma certifies all future choices
of this pair. No fifth or higher coefficient is ever needed thereafter.

The integer part of this ratio is 5077851, so the simple sufficient
onset of the pair's strict final cycle is block

`19359 + 12 * 5077851 = 60953571`,

equivalently turn index `9508757076`. A valid period of the pair's
label routing is 24 blocks, or 3744 turns. These are component bounds;
they are not a certificate, minimal preperiod, or least period for
the complete N = 78 sequence.

This is a useful discriminator for the proposed universal route:
degree three alone really does encounter a late exact tie, while the
fourth moment settles that component algebraically. A brute-force
extension to billions of turns is unnecessary for this calculation.


## 6. A late fourth-moment decision inside N = 78

This calculation concerns **one closed binary component**, not the complete 78-player sequence. It is reproduced by `n78_component.py`, with recorded output in [n78_component.json](n78_component.json).

The second-moment cycle begins at block 309 and has period 72 blocks. The selected closed pair occupies ranks 6 and 7 at phase zero. Its full rank paths between consecutive comparisons repeat every six paired blocks, or 936 turns. For fixed zero-based player labels A = 46 and B = 27, put D = G_B - G_A. The return map is

$$
D_{\rm next}=U D-\operatorname{sign}(D)K,
\qquad U=(1+z)^{936}.
$$

The relevant initial coefficients at block 309 are

$$
[z^3]D=2971800,\qquad [z^4]D=95006987238,
\qquad [z^3]K=936.
$$

After exactly 3175 returns, the third coefficient is zero. This occurs at **block 19359**, corresponding to **turn index 3020004**. At this point

$$
[z^4]D=4448685071838>0.
$$

An independent replay of all prefix decisions using the main repository's degree-four dynamics confirms the difference triple `(0, 0, 4448685071838)` between players 27 and 46 at that boundary. Every noninitial prefix order in that replay is strict through degree four.

Starting at such a third-moment zero, the next two comparisons have opposite signs. The exact two-return map is therefore

$$
D_{\rm next,next}=U^2D-\operatorname{sign}(D)(U-1)K.
$$

Its first forcing coefficient is at degree four and equals `936² = 876096`. The current fourth coefficient divided by 876096 is not an integer: its remainder is **122142**. The binary lemma consequently proves that every future comparison of this component is resolved by degrees at most four.

The quotient is 5077851. After that many further two-return steps, a strict two-cycle is reached. This gives a sufficient component stabilization point of block **60953571**, or turn **9508757076**, and a valid component routing period of 24 blocks, or 3744 turns. These are sufficient component-level values; this calculation does not establish a minimal onset, a least period, or eventual periodicity of the entire N = 78 sequence.

## Reproduce the experiments

Run from the repository root with ordinary Python 3 (without `-O`, since the research scripts use assertions):

```sh
python3 research/transport_components.py
python3 research/n78_component.py
```

Both scripts use exact integer arithmetic and the standard library. The output is recorded in [transport_components.json](transport_components.json) and [n78_component.json](n78_component.json). The scripts are research aids; the general proof and the limited scope of each conclusion are stated above.
