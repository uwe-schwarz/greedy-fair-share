# Toward a universal exclusion of binary resonance

Research notes, 2026-11-26. These are partial results. They do **not** prove the all-N conjecture or exclude every binary resonance.

## 1. Exact setting and remaining question

For N players, put

$$
v_r=\binom{N-r}{2},\qquad \mu=\frac{N^2-1}{6},\qquad 0\le r<N.
$$

The centered, sorted second-moment map is

$$
F(y)=\operatorname{sort}(y+v-\mu\mathbf 1),\qquad \sum_i y_i=0.
$$

The canonical orbit starts at y=0. Its normalized integer version is finite, hence eventually periodic. A closed binary transport component consists of two labels whose two rank slots at each recurrent phase cannot exchange labels with the other components.

The already proved parity-resonance lemma says that monomial resonance at absolute paired-block boundary m0, on a base cycle of period P, forces the component's **unordered rank occupancy** to be periodic all the way from block zero, with a block period p dividing gcd(P,m0). The pair's common centered load at the selected tie phase is zero.

The unresolved universal target is to exclude such phase-aligned, from-origin pair occupancy for N>=3. Merely having a binary mean tie is a stronger obstruction than needed, and a mean tie alone does not establish resonance.

## 2. A common affine permutation on the recurrent set

This lemma holds for arbitrary fixed real rank increments v, with mu their average.

**Lemma.** There is a single permutation of coordinates, denoted Pi, such that

$$
F(y)=\Pi(y+v-\mu\mathbf 1)
$$

for every periodic point y of F. Consequently, every cycle of Pi has average rank weight mu.

**Proof.** Sorting is nonexpansive in Euclidean norm. If y,z are periodic points with a common return time Q, then

$$
\|y-z\|_2=\|F^Q(y)-F^Q(z)\|_2
\le\cdots\le\|F(y)-F(z)\|_2\le\|y-z\|_2.
$$

All inequalities are equalities. Equality in the rearrangement inequality for squared matching distance says that the two raw vectors y+v-mu and z+v-mu cannot have a pair of coordinates in opposite strict orders. Thus, for each coordinate pair i,j, a strict raw order observed at one periodic point holds weakly at every periodic point.

These weak-order requirements admit a common total order. Indeed, a directed cycle of requirements, with at least one strict comparison witnessing an edge, would force a strict cycle at that witness point, since all other required comparisons hold weakly there. Therefore one common coordinate permutation sorts every recurrent raw vector.

On periodic points, F is consequently one affine permutation. Iterating around any cycle C of this permutation adds the constant

$$
\sum_{r\in C}(v_r-\mu)
$$

to the corresponding coordinate. Periodicity forces this sum to vanish, proving the average-weight assertion. The assertion is vacuous if there are no periodic points; in the present integer problem there are periodic points by finiteness. QED.

For example, for N=7 the source-to-destination permutation has cycles (0,6,4), (1,5), and (2,3). Their weight lists are (21,0,3), (15,1), and (10,6), all with average 8. Their cycle lengths explain the common recurrent period divisor lcm(3,2,2)=6. Transport components may join trajectories from different permutation cycles at equal-value contacts, so permutation cycles and label components must not be identified.

This reduction turns recurrent second-moment dynamics into an affine permutation subject to sorted-coordinate inequalities. It does not yet provide a universal arithmetic exclusion of binary mean contacts.

### 2.1 Exactly when the complete zero state can return

**Theorem.** For any strictly decreasing rank-weight vector v with average mu, the centered canonical orbit from zero returns to zero at a positive time if and only if

$$
v_r+v_{N-1-r}=2\mu\qquad(0\le r<N).
$$

When this condition holds, it returns after two blocks.

**Proof.** If zero returns, zero is a periodic point. Its raw coordinates v-mu are strictly decreasing, so the common recurrent permutation in section 2 must be the reversal R. The entire periodic orbit therefore follows F(y)=R(y+v-mu). Its second iterate is translation by

$$
(v-\mu\mathbf1)+R(v-\mu\mathbf1).
$$

A nonzero translation cannot have a finite orbit. Thus the translation vector is zero, giving the stated condition. Conversely, if the condition holds, then F(0)=R(v-mu) and F²(0)=0 directly. QED.

For the triangular rank weights, the mirror sums at r=0 and r=1 differ by N-2. They are nonconstant whenever N>2. Therefore **the complete all-equal second-moment state never returns after the initial state for any N>2**. This is a universal statement, but it does not exclude a proper subset of labels from returning to equal loads and does not prove eventual periodicity.

## 3. Origin-aligned occupancy cannot have period two

The existing gcd exclusion handles p=1. Here is a separate exclusion of p=2, including the ordering point that is necessary for a valid proof.

**Proposition.** For N>=3, a resonant closed binary component cannot have unordered rank occupancy of block period 2 from the origin. Consequently, a binary tie phase with gcd(P,m0)<=2 is nonmonomial.

**Proof.** At the selected recurrent phase the two centered loads are both zero. Their ranks are adjacent; write the origin-aligned rank pair as {r,r+1}. Since this is a closed binary component and N>=3, no other centered load is zero at that phase. Therefore the zero pair is neither the minimum pair nor the maximum pair:

$$
1\le r\le N-3.\tag{1}
$$

In particular, N>=4. Initially all loads are zero. The first block assigns the strictly decreasing weights v_r, so the second block's ranks are the reversal of the initial ranks. Thus a label initially at rank j has load

$$
s_j=v_j+v_{N-1-j}
$$

after two blocks, with centered value

$$
a_j=s_j-2\mu
=\left(j-\frac{N-1}{2}\right)^2-\frac{N^2-1}{12}.\tag{2}
$$

If pair occupancy has period 2, those same two labels must occupy rank set {r,r+1} after these two blocks. The symmetry and strict convexity of s_j make its possible sorted rank positions explicit.

On the left half, away from the singleton middle point when N is odd, a label j has possible rank positions

$$
\{N-2j-2,\;N-2j-1\}.
$$

For adjacent initial labels r,r+1 on this half, s_{r+1}<s_r. To occupy ranks r,r+1 after two blocks, the lower label r+1 must take rank r and the higher label r must take rank r+1. The two possible-position conditions are

$$
r\in\{N-2r-4,N-2r-3\},\quad
r+1\in\{N-2r-2,N-2r-1\}.
$$

Their unique common solution is

$$
3r=N-3.\tag{3}
$$

On the right half the analogous possible-position sets are {2j-N,2j-N+1}, and the same reasoning forces r=N-1, which is impossible even for an adjacent pair. When N is even, the two central labels have equal minimum load and occupy {0,1}; equality with the origin rank set would force N=2. When N is odd, any adjacent pair containing the unique central label has that label at rank zero after two blocks, contradicting (1). Thus (3) is the only possible proper interior case.

Now use the pair **sum**, not the unjustified claim that each label individually returns to zero. Because its rank occupancy repeats every two blocks, the pair receives the same total increment A in every two-block period. Its centered sum at time 2k is k(A-4mu). Bounded second-moment spread forces A=4mu, so its centered sum after the first two blocks must be zero.

But substituting r=N/3-1 into (2) gives

$$
a_r+a_{r+1}=\frac{6-N^2}{9}<0,
$$

a contradiction. QED.

**Important failed shortcut.** A two-block occupancy period does not imply that the two individual centered loads both return to zero after two blocks. The pair's internal difference may alternate over two occupancy periods. Only its aggregate centered sum is forced to return to zero. The rank-position argument above is what excludes this possibility for the triangular weights.

The possible-position case split and the negative sum were independently checked with exact integer arithmetic for N=3,...,300. These checks support the algebraic derivation; the proof itself covers every N.

### 3.1 A shorter proof using the canonical third-moment ordering

For the actual canonical prefix there is a simpler proof, which excludes a rank-occupancy period of 1 or 2 without needing the mean calculation.

Use the exact coordinates y_i(0)=0 and y_i(m+1)=y_i(m)+x_i(m) from [TIE_DYNAMICS.md](../TIE_DYNAMICS.md). After the first block, x_j(1)=v_j for the label initially at rank j; consequently y_j(2)=v_j. At block 2 the only equal-x pairs are mirror labels j and N-1-j. The mirror with the larger initial rank has smaller v_j and hence smaller y, so it comes first. There are no unresolved third-moment ties here.

Combining this strict mirror order with the symmetric quadratic load s_j gives the exact permutation

$$
\rho_2(j)=
\begin{cases}
N-1-2j,&0\le j\le\lfloor(N-1)/2\rfloor,\\
2j-N,&\lceil N/2\rceil\le j<N.
\end{cases}
$$

Adjacent initial ranks within either branch map to ranks separated by 2. The unique adjacent pair straddling the two branches maps to {0,1}; its initial rank set equals {0,1} only when N=2 (or the irrelevant degenerate N=1 case). Thus, for N>=3, **no adjacent initial pair occupies its original adjacent rank set again at block 2**.

A binary resonant phase has an origin-aligned adjacent pair. A rank-occupancy period of 1 or 2 would make that pair's rank set at block 2 equal its initial rank set, contradicting the explicit permutation. This supplies the same gcd(P,m0)<=2 exclusion using the actual canonical tie rule. The preceding proof remains useful because it requires only second-moment ordering and the mean condition.

### 3.2 Two necessary identities for a second-moment-closed resonant pair

Here is the exact implication needed for a possible generalization of the two-block argument.

**Lemma.** Let A,B be two labels in the canonical process. Suppose:

1. From some block onward the second-moment state is periodic, and {A,B} is closed under **every** movement compatible with those second moments. Equivalently, it is a size-two component of the second-moment transport graph, allowing a phase lift if needed.
2. At a sufficiently late block m0 their second moments tie.
3. Their unordered rank-set sequence C_t is periodic from block zero with a period p dividing m0.

Let Pi be any common affine permutation on the recurrent second-moment states, viewed as a source-rank-to-destination-rank bijection. Then C_0={r,r+1} for some r, and

$$
\boxed{\quad\Pi(C_0)=\operatorname{rev}(C_0),\qquad
\Pi^2(C_0)=\rho_2(C_0).\quad}\tag{3}
$$

Here rev(j)=N-1-j and rho_2 is the exact canonical block-2 permutation in section 3.1.

**Proof.** At block m0 the tied pair occupies adjacent ranks. There cannot be a third equal-second-moment label at that phase: the incoming balanced complete bipartite fiber would connect it to the supposedly closed size-two component. Thus C_m0 is an adjacent pair. The origin-aligned occupancy assumption gives C_m0=C_0.

At every recurrent phase, Pi is one of the allowed second-moment matchings. Closure under every such matching therefore gives Pi(C_t)=C_(t+1) for all sufficiently large t. Apply this at m0 and m0+1, and use p|m0 to identify C_(m0+j)=C_j for j=0,1,2. Hence Pi(C_0)=C_1 and Pi^2(C_0)=C_2.

The actual canonical first block reverses the initial ranks, giving C_1=rev(C_0). Section 3.1 gives C_2=rho_2(C_0). This proves both identities. No comparison of individual centered pair trajectories is needed for this implication. QED.

**Scope warning.** Closure only at a higher moment depth does not imply closure under every second-moment matching: Pi may send a pair slot to an outside label's second-moment-equal slot. Therefore (3) cannot be asserted for an arbitrary higher-level closed binary component. It remains valid if one separately knows that a common recurrent second-moment permutation respects that component at every phase.

For all computed recurrent permutations through N=259, no adjacent initial pair satisfied both identities (3). This is an observed necessary-condition failure, not a universal proof of failure. Proving that no recurrent affine permutation for triangular weights can satisfy these two identities would exclude every second-moment-closed binary parity resonance at once, with no bound on its occupancy period.

The identities have an oriented strengthening. At the recurrent tie, the two source loads are equal and v_r>v_(r+1). Hence

$$
\Pi(r)=N-1-r,\qquad \Pi(r+1)=N-2-r.
$$

If the two canonical block-2 loads differ, their order similarly forces Pi²(r)=rho_2(r) and Pi²(r+1)=rho_2(r+1). The even-N central pair is the equal-load exception; its set identities already fail for N>2.

## 4. Why convexity and integrality alone are insufficient

Replacing the exact triangular weights by the strictly decreasing, strictly convex integer weights

$$
(11,6,3,1,0)
$$

at N=5 yields a canonical zero-origin second-moment orbit with preperiod 3 and period 5. Its normalized cycle is

```
(0,1,2,3,7)
(0,1,3,3,7)
(0,2,3,3,7)
(0,2,3,4,7)
(0,1,2,3,6).
```

At absolute block 5 (phase 2), ranks 2,3 form a closed binary component and tie at the global mean. This changes only the largest triangular weight, from 10 to 11. Therefore a proof of the stronger mean-level exclusion must use more than integrality and strict convexity.

This example is not a parity-resonance counterexample: its pair rank set after the next block is {0,1}, whereas a pair initially at ranks {2,3} from the zero origin would next occupy {1,2}. The required origin-aligned occupancy already fails in the first block.

### A weaker canonical zero-return condition also fails

It is not enough to require that two adjacent initial labels later both return to centered second load zero. The canonical N=4 process already does this at block 4 for initial labels 2 and 3. The exact prefix is:

| Block | Greedy rank order of initial labels | Absolute triangular loads by initial label |
|---:|:---|:---|
| 0 | (0,1,2,3) | (0,0,0,0) |
| 1 | (3,2,1,0) | (6,3,1,0) |
| 2 | (2,1,3,0) | (6,4,4,6) |
| 3 | (0,3,1,2) | (6,7,10,7) |
| 4 | (1,3,2,0) | (12,8,10,10) |

At block 4 the global mean is 10, and exactly labels 2,3 attain it. They now occupy ranks {1,2}, while their initial rank set was {2,3}; the required phase-aligned occupancy does not hold. The prefix orders are strict through degree four after the initial all-player tie.

### Strict convexity does not exclude even the oriented two-block pattern

The exact triangular weights matter for a proposed universal two-block incompatibility theorem. At N=10 take

$$
v=(148,58,28,21,15,10,6,3,1,0),\qquad \mu=29.
$$

Its adjacent differences (90,30,7,6,5,4,3,2,1) are strictly decreasing, so these weights are strictly convex. The strictly increasing centered fixed point

$$
h=\frac15(-188,-168,-163,-123,-118,-23,-8,122,262,407)
$$

has source-to-destination permutation

$$
\Pi=(9,5,1,2,0,4,3,6,7,8).
$$

Indeed h_(Pi(i))-h_i=v_i-29 for every i. Since h is strictly sorted, this permutation is the unique common recurrent order. At r=5 it satisfies all four oriented identities:

$$
\Pi(5)=4,\quad\Pi(6)=3,\quad
\Pi^2(5)=0=\rho_2(5),\quad
\Pi^2(6)=2=\rho_2(6).
$$

Thus strict convexity alone cannot prove the oriented exclusion. This is not a counterexample for the triangular weights and does not establish an origin-aligned mean-pair resonance for these modified weights. The displayed values provide an exact rational check, independent of the exploratory linear program that found them.

## 5. Exact finite certificates and their limits

The accompanying [mean_pair_certificates.py](resonance/mean_pair_certificates.py) implements one reusable exact criterion, with a compact scientific report in [mean_pair_certificates.json](resonance/mean_pair_certificates.json). It replaces state enumeration by a difference-constraint calculation in N variables. All calculations in the verifier use arbitrary-precision Python integers through NumPy's object arrays; no floating-point optimizer is used.

### 5.1 Exact difference constraints replace state enumeration

The common-permutation lemma gives a much smaller exact certification problem. This is a finite-N criterion, not an automatic success theorem.

Suppose a known periodic orbit has a strict ordering of the averages of its raw coordinates y_i+v_i-mu. Since all periodic points have compatible raw orders, this strict witness determines the unique common permutation Pi for **every** recurrent point. Let q be its order. Every cycle of Pi has zero total centered increment, so the affine map Pi(y+v-mu) has q-th iterate equal to the identity.

At phase t write its coordinates as

$$
Y_j(t)=y_{o(t,j)}+a(t,j)/N,
$$

where o(t,.) is a permutation and a(t,j) are known integers. At a fixed phase all a(t,j) have the same residue modulo N. Thus every required sorted-order inequality is an integer difference constraint

$$
y_{o(t,j+1)}-y_{o(t,j)}
\ge \frac{a(t,j)-a(t,j+1)}N.
$$

Now test a proposed mean pair at adjacent ranks r,r+1. Set y_r=y_(r+1)=0. A mean tie in an integer-load orbit makes **every** centered coordinate at this phase an integer: the common mean is itself the integer load of either tied player. At every later phase, differences remain integers. Hence isolation of this pair from every other label requires a gap at least 1 wherever an adjacent boundary has one pair label and one other label. Add 1 to the corresponding lower-bound constraints over all q phases.

Also impose the necessary recurrent spread bound y_(N-1)-y_0<=M, with M=binom(N,2). This bound follows directly from

$$
\operatorname{spread}(F(y))\le
\max\{M,\operatorname{spread}(y)-1\}.
$$

Represent a lower bound y_j-y_i>=c as a directed edge i->j of weight c. Add both zero-weight edges between the pinned pair. A directed cycle of positive total weight is an immediate inconsistency. Otherwise let D_ij be the largest weight of a path from i to j. All these values are finite because the sorted-order chain together with the spread-bound edge makes the graph strongly connected. Every feasible pinned point obeys

$$
\ell_j:=D_{rj}\le y_j\le -D_{jr}=:u_j.
$$

Consequently either

$$
\sum_j\ell_j>0\qquad\hbox{or}\qquad\sum_j u_j<0
$$

excludes the zero global mean. Max-plus Floyd-Warshall computes these bounds using only integer additions and comparisons. No mixed-integer or floating-point optimizer is needed.

The exact criterion proves the absence of closed binary mean ties on **all integer recurrent cycles** for every N=3,...,60. It is stronger than checking only the canonical orbit; the strict raw-average witness makes the chosen permutation valid for every recurrent point.

The implementation first tests whether a real recurrent mean pair is possible before imposing unit separation. The recorded finite run certified 237 values among N=3,...,259. The following 20 values are explicitly inconclusive because the sampled raw-order witness has ties or the permutation-order cap was reached:

```
68,89,103,119,137,179,185,204,209,211,
219,221,223,227,233,235,239,247,251,257.
```

N=260 hit the base-orbit cap and has no conclusion. No case within the processed range produced a counterexample. The report distinguishes every `certified` result from each `not_established` result and records both configured caps. Its 237 successful results do not imply that the complete labelled words are eventually periodic for those N: components with more than two players remain outside this mean-pair criterion.

Only nine of the 237 certified player counts admitted a real mean pair before unit separation was imposed: N=4,5,6,7,8,18,40,53,146. The unit-separation constraints gave positive cycles in five cases. The remaining four had strictly positive exact total-sum intervals:

| N | Pair ranks | Possible total-sum interval after pinning the pair to zero and imposing unit separation |
|---:|:---|:---|
| 4 | 1,2 | [1,1] |
| 7 | 3,4 | [1,5] |
| 40 | 23,24 | [8,74] |
| 146 | 87,88 | [134,372] |

These exact positive intervals are incompatible with the required centered sum zero. They suggest a possible geometric universal theorem: a recurrent binary mean contact for triangular weights must come within distance less than 1 of an outside label somewhere in its cycle. That universal statement is not proved here.

Run the verifier without Python's `-O` option, since its consistency assertions are part of the checked computation. Its default selection is N=3,...,8; selected values and inclusive ranges are supported:

```sh
python3 research/resonance/mean_pair_certificates.py
python3 research/resonance/mean_pair_certificates.py 7 40 146
python3 research/resonance/mean_pair_certificates.py --range 3 60 --output mean_pairs.json
```

The optional `--max-blocks` and `--max-permutation-order` settings are explicit resource caps. Reaching either cap gives `not_established`, and there is no wall-time cutoff. The script also reports `not_established` if its sampled common-order witness is ambiguous or if the exact isolation inequalities remain inconclusive. None of these outcomes is a counterexample.

### 5.2 Scope beyond second-moment components

The parity recurrence, physical origin-alignment lemma, and necessary second-mean condition apply to any closed binary component whose unordered rank occupancy is periodic. A component closed only after a higher fixed-depth normal form also has this property. The canonical block-2 exclusion in section 3.1 therefore extends to such higher-level binary components.

The difference-constraint certificates in section 5.1 have a narrower scope: they require the pair to be isolated already in second-moment transport. A higher-level binary component may share its second moment with outside labels and be separated from them only by higher moments; unit second-moment gaps cannot then be imposed.

## 6. Remaining work

The common-permutation lemma makes the recurrent second-moment problem a finite family of difference inequalities. A possible route is to prove the geometric unit-gap obstruction in section 5.1 uniformly in N. A weaker route would show that an integer periodic point with an isolated binary zero contact cannot be reached from the all-zero state while preserving that pair's rank occupancy from time zero. The period-1 and period-2 cases are now excluded. No proof for arbitrary occupancy period p, nor a counterexample for the exact triangular weights, is currently obtained here.
