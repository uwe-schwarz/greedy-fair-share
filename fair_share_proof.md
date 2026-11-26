# Greedy Fair-Share Sequences: Exact Periodicity Proofs

Canonical English version. [German translation](fair_share_proof.de.md).

Date: 2026-11-26

## Results and scope

For the greedy rule described in the video, in the termwise limit as the
hit probability tends to zero, this document provides:

1. A fully checkable proof for **N = 3**: least period 54, with periodicity
   starting at zero-based index 47, or the 48th term.
2. A general finite criterion for proving that a proposed periodic tail is
   valid for any fixed number of players.
3. Exact certificates for **every number of players from 3 to 24**. Each
   proves an infinite periodic continuation; the certificates do not rely
   merely on observing many identical blocks.
4. A concrete temporary repeating block for N = 15 whose apparent period
   must eventually fail.

**The universal theorem for all integers N > 2 is not proved.** In particular,
termination of the certificate search has not been proved for every number
of players. The finite list of 22 cases does not replace that step.

The proofs below are derived here from the construction rule. No claim of
scientific priority is made. References provide context for the problem;
they do not replace the proof steps given here.

## 1. Precise definition

The players are labelled 0, ..., N−1. Turns are indexed by t, starting at
t = 0. Let a_t denote the player selected at that turn. For q = 1−p, let

\[
S_i(t,q)=\sum_{\substack{0\le s<t\\a_s=i}}q^s.
\]

The probability that player i has already won is p S_i(t,q). The common
positive factor p does not affect the comparison. The next turn therefore
goes to the player with the smallest S_i(t,q) for q sufficiently close to
1 from below. Initially, players who have not yet appeared receive their
labels in the order of their first turns.

This is a **termwise limit**: the required upper bound on p may differ for
each finite prefix. We do not claim that a single fixed p > 0 generates
the entire infinite limiting sequence.

### Age moments

Set

\[
q=\frac1{1+z},\qquad z>0.
\]

Multiplying every player's score by the common positive factor q^(−t)
preserves their order. This gives

\[
G_i(t,z)=q^{-t}S_i(t,q)
=\sum_{\substack{s<t\\a_s=i}}(1+z)^{t-s}
=\sum_{k\ge0}M_{i,k}(t)z^k,
\]

\[
M_{i,k}(t)=\sum_{\substack{s<t\\a_s=i}}\binom{t-s}{k}.
\]

The greedy rule thus compares the integer vectors
(M_i,0, M_i,1, M_i,2, ...) lexicographically: the first differing
coefficient decides, with the smaller value receiving the earlier turn.

The exact update is

\[
M_{i,k}(t+1)=M_{i,k}(t)+M_{i,k-1}(t)
+\mathbf1_{a_t=i}\binom1k,
\]

where M_i,−1 = 0. This follows immediately from Pascal's identity.
Coefficients through degree d evolve independently of the higher
coefficients. A truncated vector determines the actual decision whenever
its lexicographic minimum is already unique.

## 2. General lemma: a permutation and its reversal

**Lemma.** For every N, each block beginning at index 2Nm consists of a
permutation π of the players followed by its reversal:

\[
\pi\,\operatorname{rev}(\pi).
\]

At every such block boundary, the moments M_i,0 and M_i,1 are equal for all
players.

**Proof.** Initially, all these values are zero. Suppose they are equal
at a block boundary. Since the degree-0 coefficient counts previous
turns, every player receives exactly one of the next N turns. Among
players not yet selected in this round, ageing alone does not change
the order of their G_i: it multiplies all of them by the same positive
factor. The first round is therefore a fixed permutation π.

Let r_i be player i's position in this permutation, with 0 ≤ r_i < N.
After the first round, the turn counts are equal again. The previously
equal first moments now differ only through the ages N−r_i of the turns
just assigned. The player selected last has the smallest first moment.
Consequently, the degree-1 comparison forces the reverse order in the
next round. Players already selected in that round are excluded by their
larger turn counts.

At the end of the paired block, each player has two new turns with ages

\[
2N-r_i\quad\text{and}\quad r_i+1.
\]

Their sum is always 2N+1. The turn counts and first moments are once again
equal for all players. Induction proves the lemma. ∎

### Updates at block boundaries

Subtract player 0's moments as a common reference:

\[
D_{i,k}=M_{i,k}-M_{0,k}.
\]

At block boundaries, D_i,0 = D_i,1 = 0. With B = 2N and

\[
w_k(r)=\binom{B-r}{k}+\binom{r+1}{k}
\]

the exact update is

\[
D'_{i,k}=\sum_{j=2}^{k}\binom{B}{k-j}D_{i,j}
+w_k(r_i)-w_k(r_0).
\]

For degrees 2, 3, and 4, this means

\[
\begin{aligned}
D'_{i,2}&=D_{i,2}+w_2(r_i)-w_2(r_0),\\
D'_{i,3}&=D_{i,3}+B D_{i,2}+w_3(r_i)-w_3(r_0),\\
D'_{i,4}&=D_{i,4}+B D_{i,3}+\binom B2D_{i,2}
+w_4(r_i)-w_4(r_0).
\end{aligned}
\]

These three formulas describe the entire dynamics used by the accompanying
verifier. If they do not determine an order, it stops; it never replaces an
unknown higher coefficient with an arbitrary choice.

## 3. Complete proof for N = 3

Write A, B, C for players 0, 1, 2. Set

\[
x_i=D_{i,2},\qquad y_i=D_{i,3},\qquad z_i=D_{i,4}.
\]

The reference player A always has (x_A,y_A,z_A) = (0,0,0).
The rank weights are

\[
w_2=(15,11,9),\qquad w_3=(20,10,5),\qquad w_4=(15,5,1).
\]

Thus

\[
\begin{aligned}
x'_i&=x_i+w_2(r_i)-w_2(r_A),\\
y'_i&=y_i+6x_i+w_3(r_i)-w_3(r_A),\\
z'_i&=z_i+6y_i+15x_i+w_4(r_i)-w_4(r_A).
\end{aligned}
\]

### 3.1 The finite prefix

The following table can be checked directly using these three integer
formulas. Here π denotes the first half of the next six-turn block.

| Index t | x_B | x_C | y_B | y_C | z_B | z_C | π |
|---:|---:|---:|---:|---:|---:|---:|:---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | ABC |
| 6 | −4 | −6 | −10 | −15 | −10 | −14 | CBA |
| 12 | −2 | 0 | −29 | −36 | −126 | −180 | BCA |
| 18 | 4 | 2 | −26 | −31 | −316 | −392 | ACB |
| 24 | −2 | −2 | −17 | −29 | −426 | −558 | CBA |
| 30 | 0 | 4 | −24 | −26 | −554 | −748 | BAC |
| 36 | 4 | 2 | −14 | −7 | −688 | −848 | ACB |
| 42 | −2 | −2 | −5 | −5 | −726 | −870 | CBA |
| 48 | 0 | 4 | −12 | −2 | −782 | −916 | BAC |

Only the initial state is a complete tie. At t = 42, B and C agree through
degree 3, but the fourth coefficient, −870 < −726, puts C before B. This
is why coefficients above degree 3 cannot simply be discarded from the
start.

The first 48 symbols are therefore

```text
ABCCBA CBAABC BCAACB ACBBCA CBAABC BACCAB ACBBCA CBAABC
```

### 3.2 The infinite tail

From t = 48 onward, the two coordinates x and y suffice for every order
comparison in the following table:

| Index t | (x_B, y_B) | (x_C, y_C) | Next six turns |
|---:|:---|:---|:---|
| 48 | (0, −12) | (4, −2) | BACCAB |
| 54 | (4, −2) | (2, 17) | ACBBCA |
| 60 | (−2, 7) | (−2, 19) | BCAACB |
| 66 | (4, 10) | (0, 12) | ACBBCA |
| 72 | (−2, 19) | (−4, 2) | CBAABC |
| 78 | (0, 12) | (2, −7) | ABCCBA |
| 84 | (−4, 2) | (−4, −10) | CBAABC |
| 90 | (−2, −17) | (2, −19) | BACCAB |
| 96 | (2, −19) | (0, −12) | CABBAC |
| 102 | (0, −12) | (4, −2) | State at t = 48 |

In every row, the three pairs (0,0), (x_B,y_B), and (x_C,y_C) are
distinct. The order is therefore uniquely determined, independently of
all higher moments. For example, at t = 48,

\[
(0,-12)<_{\mathrm{lex}}(0,0)<_{\mathrm{lex}}(4,-2),
\]

so π = BAC and the paired block is BACCAB.

After nine paired blocks, or 54 turns, the four deciding coordinates are
exactly the same again. Their update requires neither the absolute time
nor higher coefficients. Induction therefore proves

\[
a_{t+54}=a_t\qquad\text{for all }t\ge48.
\]

The permanently repeating block beginning at this index is

```text
BACCAB ACBBCA BCAACB ACBBCA CBAABC ABCCBA CBAABC BACCAB CABBAC
```

This proves infinite periodicity, rather than merely computing another
finite segment.

### 3.3 Least period and starting index

The preceding symbols also agree: a_47 = a_101 = C. Periodicity therefore
already begins at index 47, the 48th term. One step earlier, however,
a_46 = B and a_100 = A.

The displayed 54-symbol block is primitive. Every proper divisor of 54
divides either 18 or 27; both of these candidate subperiods already fail
at the first symbol, since the block begins with B whereas its symbols
at zero-based positions 18 and 27 are both A. The least period of any
54-periodic infinite word divides 54. Hence the least period is exactly
54.

Nor could a larger period move the starting point before index 47:
every period of this tail with primitive period 54 is a multiple of 54,
and the corresponding tail position after index 46 always contains A
instead of B. The minimal preperiod length is therefore 47.

## 4. General two-cycle criterion

For larger N, even the first four moment differences need not return as
a complete state. Individual coordinates may drift without changing the
decisions. The following stronger criterion suffices.

**Theorem.** Given a verified greedy prefix and a proposed repeating block
of length L, fix a phase of this block and a comparison between two
players i, j required at that phase. Let F_k(z) be the difference G_j−G_i
at this phase after k repetitions of the proposed block, initially
computed for the prescribed sequence without assuming that it follows
the greedy rule. Then

\[
F_{k+1}(z)=(1+z)^L F_k(z)+C(z),
\]

where C(z) does not depend on k.

Let d be the smallest degree at which F_0 or F_1 has a nonzero
coefficient. Set

\[
a=[z^d]F_0(z),\qquad b=[z^d]\bigl(F_1(z)-F_0(z)\bigr).
\]

Then all lower coefficients are zero for every k, and

\[
[z^d]F_k(z)=a+kb.
\]

In particular, the comparison remains strictly correct for every k ≥ 0
if a ≥ 0, b ≥ 0, and F_0 is already strictly positive in the lexicographic
sense. Here a and b cannot both be zero, because d was defined as the
first degree that occurs.

**Proof.** During the next L turns, every old contribution ages by L;
this multiplies it by (1+z)^L. The contributions added during those L
turns always have the same ages and player assignments at the phase
under consideration. Their difference is therefore a fixed C(z). This
proves the recurrence.

Since the constant coefficient of (1+z)^L is 1, this recurrence is
triangular in its coefficients. For every degree j < d, the coefficients
in F_0 and F_1 are zero. Induction on j gives C_j = 0 and then F_k,j = 0
for every k. At degree d, only the additive recurrence remains:

\[
F_{k+1,d}=F_{k,d}+C_d,
\qquad C_d=F_{1,d}-F_{0,d}=b.
\]

It yields a+kb. If a > 0, this expression is always positive when b ≥ 0.
If a = 0, then b > 0; this degree decides the comparison for every k ≥ 1,
while for k = 0 the separately checked positivity of F_0 applies.
Higher coefficients cannot reverse an already strictly positive first
coefficient. ∎

### Application to the actual greedy sequence

The proposed periodic tail is initially only a candidate. Checking the
criterion for every required comparison at every phase implies, by
induction on the turns, that the actual greedy rule always produces
exactly this candidate. The prescribed repetition therefore introduces
no circular reasoning.

By the paired-block lemma, it suffices to compare the N−1 adjacent
players of the proposed permutation at each block boundary. These
comparisons determine the entire strict order. The reversal in the
second half already follows from the lemma.

**Two simulated repetitions alone are not enough.** The decisive ingredient
is the proved formula a+kb, particularly the sign condition b ≥ 0.
For example, the values 2 and 1 look correct for the first two
repetitions, but the corresponding formula 2−k fails later.

## 5. Exact certificates for 3 ≤ N ≤ 24

The verifier `fair_share_verify.py` and the data in
`fair_share_certificates.json` accompany this document.

For each number of players, the verifier reconstructs the prefix from
the zero state, checks every required comparison through degree 4,
computes the proposed tail twice, and then checks the inequalities of
the two-cycle theorem. All numbers are arbitrary-precision Python
integers. No floating-point numbers or numerical choice of a small p
are used.

The block certificates initially prove a sufficient starting index and
a valid period. The verifier additionally determines the least period
of the cyclic word using the exact prefix function. While reconstructing
the prefix, it compares every turn with the periodic tail extended
backwards. One plus the last differing index is the minimal preperiod
length: every other eventual period must be a multiple of the least
tail period and would require the same incorrect symbol at that last
differing index.

All lengths in the table count individual turns. The preperiod length
is also the zero-based index at which the permanent periodic tail begins.

| N | Minimal preperiod length | Least period | Block certificate start |
|---:|---:|---:|---:|
| 3 | 47 | 54 | 48 |
| 4 | 46 | 192 | 48 |
| 5 | 588 | 500 | 590 |
| 6 | 1197 | 864 | 1200 |
| 7 | 207 | 168 | 210 |
| 8 | 2429 | 512 | 2432 |
| 9 | 14468 | 4860 | 14472 |
| 10 | 5374 | 1600 | 5380 |
| 11 | 764 | 1056 | 770 |
| 12 | 66258 | 5184 | 66264 |
| 13 | 1007 | 936 | 1014 |
| 14 | 4380121 | 32928 | 4380124 |
| 15 | 330741 | 48600 | 330750 |
| 16 | 2822039 | 67584 | 2822048 |
| 17 | 1219 | 15708 | 1224 |
| 18 | 2781674 | 54432 | 2781684 |
| 19 | 432243 | 118560 | 432250 |
| 20 | 3752 | 28800 | 3760 |
| 21 | 19032663 | 26460 | 19032678 |
| 22 | 3156 | 34848 | 3168 |
| 23 | 309612 | 63480 | 309626 |
| 24 | 50652467 | 532224 | 50652480 |

Run with Python 3, without additional packages:

```sh
python3 fair_share_verify.py fair_share_certificates.json
```

To check only selected cases:

```sh
python3 fair_share_verify.py fair_share_certificates.json 3 4 15
```

The expensive part is reconstructing long prefixes. Verifying the
infinite tail itself requires only two prescribed repetitions and the
proved coefficient formula for each case.

The accompanying report `fair_share_verification.json` contains the
results of the separately written two-cycle verifier. The certificate
search used a different implementation with exact polynomials in the
repetition count. In addition, N = 3 and N = 4 were independently
cross-checked using full polynomials and symbolic sums, respectively.

For N = 24, the independent check gives a minimal preperiod length of
**50652467 turns** and a least period of **532224 turns**. The permanent
periodic tail therefore begins with turn 50652468 when counting from
one. Under this greedy rule, the preperiod for 24 players is therefore
far from short.

## 6. An apparent loop that eventually breaks

For N = 15, a candidate block of length 8100 appears starting at index
30600. It repeats completely 25 times and therefore looks very stable.
Nevertheless, this repetition eventually ends.

At phase 219 of the candidate's 270 paired blocks, the fourth age
coefficient determines the order of players 8 and 5, labelled from
zero. Under the hypothetical infinite repetition, the deciding
difference is

\[
30317118-1215000k.
\]

It is positive for k = 0, ..., 24 and negative for k = 25. Higher
coefficients cannot change this sign because all lower differences
are zero. In fact, the first deviation from the proposed word occurs
at index

\[
30\bigl(1020+25\cdot270+219\bigr)=239670.
\]

The candidate requires player 8 there, whereas the actual greedy rule
selects player 5. The subsequently certified period is 48600, with a
sufficient starting index of 330750.

This refutes **this proposed 8100-turn block**, not eventual periodicity
for N = 15. It gives a concrete reason why even many observed
repetitions cannot replace an infinite-continuation proof. These
statements concern the sequence computed exactly here; they do not
assume that the video identifies this particular block as the final
period.

## 7. What is already known for arbitrary N, and what is missing

For every number of players, part of the dynamics is governed by a
general finite state space. Consider the sorted second moments at
paired-block boundaries. Subtract their minimum and divide by 2.
These differences are integers. After subtracting a common term and
dividing by 2, the rank weights are

\[
w_r=\frac{(N-1-r)(N-r)}2,
\qquad 0\le r<N.
\]

The smallest current load receives the largest weight, and so on.
When loads are equal, the higher moments affect the player labels
but not the resulting unlabelled multiset. The next sorted, normalized
load vector is therefore a deterministic function of the current
sorted, normalized load vector.

Set M = N(N−1)/2. The spread of the loads remains at most M.
Indeed, for two ordered loads ℓ_i ≤ ℓ_j, the weights are ordered
oppositely, w_i ≥ w_j. The new difference is

\[
(\ell_i+w_i)-(\ell_j+w_j)
=-(\ell_j-\ell_i)+(w_i-w_j),
\]

which lies between the negative old spread and M. The new spread
therefore does not exceed the maximum of the old spread and M.
Initially, it is zero.

Consequently, there are at most

\[
\binom{M+N-1}{N-1}
\]

sorted, normalized states: the first entry is zero, and the remaining
N−1 entries are a nondecreasing sequence of values from {0,...,M}.
This **unlabelled configuration of second moments** is therefore
eventually periodic for every N.

The missing step concerns player labels when ties occur. These
decisions depend on higher moments. A periodic multiset of second
moments does not imply a periodic sequence of player labels. Already
N = 2 shows that ignoring this distinction would produce an invalid
proof.

To prove the general conjecture, one could, for example, establish a
theorem guaranteeing that a valid periodicity certificate is eventually
reached for every N ≥ 3. No such theorem is derived here. The exact
individual-case proofs and the certification criterion are complete;
the universal existence step remains open.

## 8. Literature and historical context

A search through 2026-11-26 found no published proof for all N ≥ 3.
This describes the outcome of the search; it does not prove that no
such text exists.

- Joshua N. Cooper and Aaron M. Dutle, *Greedy Galois Games*,
  American Mathematical Monthly 120 (2013), 441–451.
  [arXiv:1110.1137](https://arxiv.org/abs/1110.1137),
  [authors' version](https://people.math.sc.edu/cooper/ThueMorseDueling.pdf).
  The relevant proved limiting theorem concerns two players.
- [OEIS A287150](https://oeis.org/A287150): the three-player sequence.
  The entry consulted describes periodicity as an observation of the
  first 5000 terms and identifies the 54-term block beginning at the
  48th term.
- kram1032, [*What's the fairest turn sequence for n players?*](https://math.stackexchange.com/questions/2078609/whats-the-fairest-turn-sequence-for-n-players),
  Mathematics Stack Exchange: the explicit coefficient rule and its
  implementation.
- Anders Kaseorg, comment dated 2012-11-01 on Zachary Abel's
  [*Dueling Dilettantes*](https://blog.zacharyabel.com/2012/02/dueling-dilettantes/):
  already reports observed periods 54, 192, 500, and 864 for three to
  six players. The documented history therefore predates the OEIS
  entry from 2017.
- A. Zabolotskii, *Плохие стрелки* (*Bad Shots*), Kvant 2022,
  no. 7, pp. 22–24,
  [official article page](https://www.kvant.digital/issues/2022/7/zabolotskiy-plohie_strelki-99fb3197/),
  [DOI:10.4213/kvant20220702](https://doi.org/10.4213/kvant20220702).
  The article explicitly poses periodicity for three or more players
  as an open problem. This describes the state reported in the 2022
  article.
- Tanya Khovanova and Tejo Madhavarapu, *Fair Duels after a False Start*,
  [arXiv:2610.00880v1](https://arxiv.org/html/2610.00880v1), 2026-10-01.
  Theorem 1.1 concerns two players with a prescribed finite prefix
  that is neither a Thue–Morse prefix nor its complement. It is not
  a theorem for arbitrarily many players.

The individual-case proofs presented here are consistent with this
historical context: a finite exact certificate can settle a particular
case without settling the general existence claim.
