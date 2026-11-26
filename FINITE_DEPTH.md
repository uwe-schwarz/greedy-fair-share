# Every fixed moment depth has an eventual polynomial normal form

Research derivation, 2026-11-26. This extends the degree-four argument in
[TIE_DYNAMICS.md](TIE_DYNAMICS.md). The new conclusion still does **not** prove that a finite
moment depth suffices for each N >= 3.

## 1. Statement and conventions

Fix N >= 2 and B = 2N. Time m counts complete permutation/reversal blocks,
so the underlying turn boundary is t = Bm. Let M_(i,k)(m) be player i's
age moment of degree k at this boundary.

**Theorem A (fixed-depth normal form).** For each fixed integer d >= 0,
the unlabelled multiset of vectors

$$
\bigl(M_{i,0}(m),\ldots,M_{i,d}(m)\bigr),\qquad 0\le i<N,
$$

is eventually polynomial on each of finitely many time phases. More
precisely, there are integers m_0 and P > 0 and rational vector polynomials
P_(j,r)(m), indexed by phase j modulo P and sorted slot r, such that for all
m >= m_0 with m congruent to j modulo P, the lexicographically sorted
moment vectors are exactly P_(j,0)(m),...,P_(j,N-1)(m). Each degree-k moment
has polynomial degree at most k+1 in m.

The polynomials here describe the **absolute** moments. Their high-degree
common growth is harmless. In the earlier normalized coordinates, the
degree bounds can be smaller.

**Theorem B (finite-depth criterion).** For the canonical greedy sequence
at this fixed N, the following statements are equivalent:

1. The player sequence is eventually periodic.
2. There are integers d and m_0 such that, at every block boundary m >= m_0,
   the moment vectors through degree d are pairwise distinct.

Thus the all-N conjecture is equivalent to eventual bounded comparison
depth for each N >= 3. The bound may depend on N. Neither a universal
degree-four bound nor the existence of any such finite bound is proved here.

## 2. Exact triangular update

At a block boundary let r_i denote player i's rank in the next permutation.
For a fixed depth d, write the full moment column as u_i. The update is

$$
u'_i=A_d u_i+b_{r_i},
\qquad (A_d)_{k\ell}=\binom{B}{k-\ell},
\quad 0\le \ell\le k\le d,
$$

with zero entries above the diagonal, and

$$
(b_r)_k=\binom{B-r}{k}+\binom{r+1}{k}.
$$

The matrix A_d is constant and unipotent. Its integer
powers, and also A_d^m for a real formal variable m, are matrix polynomials
in m: if A_d = I+K with K nilpotent, use the finite binomial expansion.

The unlabelled update through any fixed depth is closed. Players tied in
all retained coordinates have identical numerical inputs. Assigning their
labels to the tied ranks differently leaves the unlabelled output multiset
unchanged.

## 3. The finite routing graph of polynomial lower profiles

Suppose Theorem A has been proved through degree d-1. Enlarge m_0 so all
nonidentical polynomial comparisons have their final signs. Put

$$
p_v(m)\in\mathbb Q[m]^d,
\qquad v=(j,r),\quad 0\le j<P,
$$

for the lower-moment polynomial profile of slot r in phase j. The variable
m is the absolute block time, not a separate phase counter. Profiles are
only sampled at the corresponding residue class, but are considered as
polynomials in an unrestricted formal variable when proving identities.

An edge from v=(j,r) to w=(j+1 mod P,s) is allowed precisely when

$$
p_w(m+1)=A_{d-1}p_v(m)+b_r^{<d}
\tag{1}
$$

as a polynomial identity. Any nonidentical pair of sides can coincide at
only finitely many m; increasing m_0 removes all such accidental matches.
Thus these are the movements compatible with the lower-moment profiles;
every actual later movement of a player is among these edges. Higher
moments can exclude some of the compatible choices.

At each phase the relation is a disjoint union of **balanced complete
bipartite graphs**: every collection of source ranks having the same
updated lower profile can be matched with every target slot having that
profile, and the two collections have the same size. Equality of sizes
follows from equality of the actual unlabelled multisets at arbitrarily
late times. Distinct polynomial profiles cannot repeatedly coincide.

Consequently every edge lies on a directed cycle. To see this, choose a
perfect matching containing that edge in its complete bipartite fiber,
choose arbitrary perfect matchings in the other fibers and phases, and
combine them. On the finite set of all phase/slot vertices this is a
bijection, so each selected edge belongs to one of its cycles.

The weak components C of this graph are therefore closed groups of slots,
and each actual player stays inside one component. Moreover, every group
of equal lower profiles at a given phase lies inside one component: the
preceding phase's complete bipartite fiber connects all its target slots.

## 4. Polynomial-transport rigidity

**Lemma.** Under the preceding hypotheses, for each closed component C
there is one rational vector polynomial q_C(m) such that

$$
p_v(m)=q_C(m)+c_v\qquad(v\in C),
\tag{2}
$$

where c_v is a constant rational vector. Thus the entire time-dependent
part of the lower-moment profile is common inside a component.

**Proof.** Differentiate (1), which eliminates the constant rank weight:

$$
p'_w(m+1)=A_{d-1}p'_v(m).
$$

Define the vector polynomial

$$
h_v(m)=A_{d-1}^{-m}p'_v(m).
$$

The inverse power is polynomial because the matrix is unipotent. Along
every allowed edge,

$$
h_w(m+1)=h_v(m).
\tag{3}
$$

Every vertex belongs to a directed cycle. Following such a cycle of
length L gives h_v(m+L)=h_v(m). A polynomial with nonzero period is constant.
Write its value as h_v. Equation (3) now says h_w=h_v along every edge, so
there is one constant vector h_C on each component.

It follows that p'_v(m)=A_(d-1)^m h_C for every v in C. Choose a rational
polynomial antiderivative q_C of this common derivative. Each difference
p_v-q_C is constant, proving (2). ∎

This is the step that generalizes the transported third-moment slope used
in the degree-four proof. It handles the entire polynomial lower profile
at once.

## 5. Induction to the next moment

Write Y_i=M_(i,d). Its exact update has the form

$$
Y'_i=Y_i+\ell p_v(m)+(b_r)_d,
\qquad
\ell_k=\binom B{d-k},\quad 0\le k<d.
$$

For the component C containing v, use (2) and choose a rational polynomial
R_C satisfying the discrete antiderivative equation

$$
R_C(m+1)-R_C(m)=\ell q_C(m).
\tag{4}
$$

Every rational polynomial has such a rational polynomial antiderivative
for the finite-difference operator. This follows directly by expressing
it in the binomial-polynomial basis. Set Z_i=Y_i-R_C(m). Since a player's
component is preserved along its route, (4) gives

$$
Z'_i=Z_i+\ell c_v+(b_r)_d.
\tag{5}
$$

The increment is now a fixed rational constant for each phase and rank.
Subtracting R_C changes no comparison that needs degree d, because every
lower-moment tie group lies in one component and has the same subtraction.

For each phase, the unlabelled residual update is a composition of:

1. Sorting Z within the current equal-lower-profile groups.
2. Adding the fixed slot constants in (5).
3. A fixed permutation matching the updated lower profiles to target slots.
4. Sorting Z within the target equal-lower-profile groups.

The initial sorting extends the operator to all real vectors. Each phase
operator is continuous and nonexpansive in the sup norm, and has finitely
many polyhedral affine pieces. Each affine piece is a permutation matrix
plus a rational translation. The same holds for the P-step return map.

Choose a common denominator for its translations and the initial residual
state. Multiplying all coordinates by that denominator gives an integer
orbit of an integer-translation piecewise-permutation map. The proposition
already proved using Kohlberg's theorem in [TIE_DYNAMICS.md](TIE_DYNAMICS.md), section 3,
therefore implies eventual affine-periodicity of these residuals.

The finitely many intermediate phase maps preserve the resulting
phasewise affine form after increasing the phase period if necessary.
Restoring R_C proves that M_d has a rational polynomial form on each of
finitely many phases. Lower coordinates retain their prior polynomial
form on this refined period.

For the degree bound, assume the degree-k lower profile has polynomial
degree at most k+1. Then q_C has degree at most d, R_C has degree at most
d+1, and the new residual has degree at most one. Hence M_d has degree at
most d+1.

The induction begins at degree zero: every player has M_(i,0)(m)=2m, a
common linear polynomial. This proves Theorem A for every finite d. ∎

## 6. Bounded depth implies labelled periodicity

Assume all player moment vectors through some fixed degree d are pairwise
distinct at all sufficiently late boundaries. Apply Theorem A and refine
its phases until every polynomial comparison has its final sign.

The numerical slot profiles now determine a fixed routing permutation
between each consecutive pair of phases. The strictness hypothesis rules
out every unresolved label choice. Over a complete phase period the
labels undergo one fixed permutation sigma. Repeating that period
ord(sigma) times restores all labels. Each block's second half is the
reverse of its first half, so the individual-turn sequence is eventually
periodic.

## 7. Labelled periodicity implies bounded depth

Conversely, suppose the player word has an eventual period L in individual
turns. Replace L by a multiple if necessary so B divides L, and begin at a
sufficiently late paired-block boundary. There are only finitely many
block phases in this period and finitely many player pairs.

For a fixed phase and pair i,j let F_k(z)=G_j-G_i at the kth repetition.
Prescribed periodicity gives the exact recurrence

$$
F_{k+1}(z)=(1+z)^L F_k(z)+C(z),
\tag{6}
$$

with C independent of k. Let delta be the smaller of the orders of
vanishing at zero of F_0 and C, ignoring an identically zero polynomial.
At least one is nonzero: at a positive paired-block boundary both players
have appeared, and their distinct sets of turn positions cannot yield
identical score polynomials.

All coefficients below delta stay zero. At degree delta, (6) gives

$$
[z^\delta]F_k=a+kc,
\quad a=[z^\delta]F_0,\quad c=[z^\delta]C,
$$

where a and c are not both zero. This affine expression can vanish for
at most one k. Hence this pair is distinguished through degree delta at
every sufficiently late repetition of this phase.

Taking the maximum of the finitely many deltas, and discarding finitely
many exceptional repetitions, gives one finite depth d that separates
every pair at every subsequent block boundary. This proves the converse
and Theorem B. ∎

## 8. What remains open

The fixed-depth dynamics is now controlled at every degree. The remaining
question is whether the degrees needed to resolve comparisons stay bounded
for each fixed N >= 3. The two-player Thue-Morse sequence shows that this
does not follow from Theorem A: every finite projection has the polynomial
normal form, while unresolved ties can migrate to successively higher
degrees.

The degree-four separation claim remains a stronger, convenient sufficient
target. If it fails, Theorem B supplies the correct general target without
requiring a new normal-form proof at each larger degree.

This theorem is derived here from the paired-block recurrence and the
previously stated Kohlberg theorem. It is not attributed as a published
all-N fair-share result, and it does not establish the universal conjecture.

## External theorem used

The invariant-half-line input is Elon Kohlberg, *Invariant Half-Lines of Nonexpansive Piecewise-Linear Transformations*, Mathematics of Operations Research 5(3), 366–372 (1980), [DOI:10.1287/moor.5.3.366](https://doi.org/10.1287/moor.5.3.366). An accessible statement is Theorem 2.4 in [Akian, Gaubert, and Guterman](https://www.cmap.polytechnique.fr/~gaubert/COURSM2/SCHEDULINGGAMES/FURTHERREADING/AkianGaubertGutermanIJACfinal.pdf). The polynomial transport lemma, induction, and finite-depth equivalence are derived above.
