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

Use the exact coordinates y_i(0)=0 and y_i(m+1)=y_i(m)+x_i(m) from TIE_DYNAMICS.md. After the first block, x_j(1)=v_j for the label initially at rank j; consequently y_j(2)=v_j. At block 2 the only equal-x pairs are mirror labels j and N-1-j. The mirror with the larger initial rank has smaller v_j and hence smaller y, so it comes first. There are no unresolved third-moment ties here.

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

## 5. Additional exact evidence and its limits

The complete N=8 integer-state enumeration in resonance/resonance_integer_cycles.cpp checked all 6,724,520 sorted normalized states of spread at most binom(8,2). It found 6 cycles. One cycle has a mean tie; the component containing that tie has all 8 players. No closed binary mean tie occurs. This extends the prior exhaustive N=3,...,7 evidence by one value of N.

The exact N=8 output is in resonance/resonance_integer_cycles_details.json, with the mean contact recorded in resonance/resonance_integer_cycles_details.log:

```
period 8, phase 5, state (0,3,4,4,7,7,13,18), component size 8.
```

The exploratory resonance/resonance_general_aligned.py also tested all strictly decreasing weight sets with minimum zero, maximum at most 18, gcd one, and N=3,...,8. Among 62,435 maps it found no closed binary mean phase whose pair trajectory and rank occupancy were compatible with periodic continuation all the way from the origin. This finite experiment suggests that the weaker aligned-occupancy exclusion might hold more broadly than the mean-level exclusion. It is not a theorem, and it does not verify the higher-moment label choices when cross-component ties occur in the transient.

## 6. Remaining work

The common-permutation lemma makes the recurrent second-moment problem a finite family of difference inequalities. A possible route is to prove that an integer periodic point with an isolated binary zero contact cannot be reached from the all-zero state while preserving that pair's rank occupancy from time zero. The period-1 and period-2 cases are now excluded. No proof for arbitrary occupancy period p, nor a counterexample for the exact triangular weights, is currently obtained here.
