# Interacting comparison networks: exact drift cuts and integer charges

Date: 2026-11-26. Research note; no all-N theorem is claimed.

## 1. A common two-gate normal form

Let a periodic lower-moment profile contain three wires. At the beginning
of a return, two wires have equal moments through degree three. Write their
full score germs as A <= B, and write C for the third wire. After the first
transport segment, B and C meet at the second gate while A bypasses it. The
lower output of this second gate becomes the outside wire on return; its
upper output and A form the next first gate.

For a rank path rho=(r_0,...,r_(m-1)) of paired blocks of width B0=2N,
put

    G_rho(x) = sum_t [x^((m-1-t) B0+B0-r_t)
                      +x^((m-1-t) B0+r_t+1)].

The exact transport of a score is x^(m B0) F + G_rho. Let U,V,W be
these transport polynomials for the first-stage A,B,C paths, and let
E,F,G be those for the second-stage outside, lower, upper paths.
Let the two segment lengths in turns be s,t, and put r=x^(s+t). Define

    J = x^(-s) (W-V),
    H = x^t U + E,
    P = H - x^t V - G,
    Q = H - x^t V - F - J,
    Z = C + J.

Laurent powers are harmless because x=1+z is a unit near z=0. Subtracting
the common output H gives the exact full-germ map

    (A,B,Z) -> ( sort(r A, r max(B,Z)-P),
                r min(B,Z)-Q ).                         (1)

The first two output coordinates are sorted. Formula (1) is an identity
of ordered Laurent germs, not a truncation of the greedy rule.

In both examples below A,B,Z agree through degree three, while P,Q
vanish through degree three. Consequently their fourth coefficients,
a <= b and z, obey the scalar map

    T(a,b,z) = ( sort(a, max(b,z)-p), min(b,z)-q ),         (2)

where p=[(x-1)^4]P and q=[(x-1)^4]Q. Common fourth translations can be
removed freely. Higher coefficients matter only if a gate ties in (2).

## 2. General drift-cut lemma

**Lemma.** Suppose p>0 and 2q>p in (2). Every scalar orbit eventually has
z<b permanently. Thereafter the second gate has a strict scalar order,
and the gap d=b-a of the remaining pair obeys d -> |d-p|.

**Proof.** Let S=a+b+z and L=3z-S. Sorting preserves sums, hence

    S' = S-p-q,
    z' = min(b,z)-q <= z-q,
    L' <= L+p-2q.

Thus L eventually becomes strictly negative. Since L=2z-a-b, this
means z<(a+b)/2<=b. In this region z'=z-q and the pair sum drops by p,
so L'=L+p-2q<0; the region is forward invariant. The pair update is
sort(a,b-p), whose gap is |d-p|. This proves the claim.

For p>0, repeated subtraction brings d into [0,p], and then the gap is
a two-cycle d,p-d. If the entering d is not divisible by p, neither
value is zero and all future gates are decided at this scalar degree.
If d is divisible by p, scalar ties recur; the lemma alone does not
resolve their higher-moment decisions. The previously proved binary
parity obstruction can be applied to that residual binary component
when its nonresonance hypothesis holds.

The argument is elementary and applies to any network having (1), at
any first nonzero scalar degree after lower terms are equalized.

## 3. N=8: a strict drift cut

The lower (second,third) profile has period 16 paired blocks. At phase 1
of the stored certificate the interacting third-level component consists
of labels {0,1,6}. The first gate is at phase 1 and the second at phase 11;
the gaps are 10 and 6 blocks. Assign A=label1, B=label0, C=label6.

The first-stage rank paths are

    A: 2,5,0,7,5,0,7,4,1,6
    B: 3,2,4,1,6,3,2,5,0,7
    C: 0,7,5,0,7,4,1,6,3,2.

The second-stage paths are

    outside: 3,2,4,1,6,3
    lower:   4,1,6,3,2,5
    upper:   5,0,7,4,1,6.

The outside wire initially differs from the first pair in moments two
and three by (-6,-301). The correction J cancels these lower differences
and has fourth coefficient 23083. Exact moment transport gives

    p=61440=15*4096,
    q=45056=11*4096,
    2q-p=28672>0.

In a gauge with a=0 the initial fourth coordinates are

    (a,b,z)=(0,9070,-309248).

Already z<(a+b)/2. The cross gate stays strictly separated, and the pair
gap cycles as 9070,52370,9070,... . The lower profile period doubles to
32 paired blocks in the labelled dynamics of this component.

There is also a useful immediate congruence proof: every update in (2)
permutes the three coordinates and adds multiples of 4096. The three
initial residues are 0,878,2048, all distinct. Thus neither gate can
ever tie in fourth degree, independently of the drift argument.

## 4. Balanced max-subtraction lemma and N=12

When q=0 and p>0, (2) replaces the largest of the three values by that
value minus p, then permutes the three coordinates. Each label's residue
modulo p is invariant.

If these three residues are distinct, equality at a scalar comparison
is impossible. The range of the values eventually becomes strictly
less than p: while the range is at least p, the current minimum does
not decrease, and the nonnegative integer quantity
sum_i floor((value_i-initial_min)/p) drops by one on every such step.
Once the range is below p, subtracting p moves the unique maximum
strictly below both other values and preserves range<p. Hence maximum
selection rotates through the three labels. In the particular slot
map (2), after at most two such steps z>b>a; subsequently

    T(a,b,z)=(z-p,a,b),

and T^3 subtracts p from all coordinates. The labelled return decisions
therefore have period three from that point.

N=12 provides an exact equal-drift example where a strict drift cut is
unavailable. Its component {7,10,11} has lower period 72 blocks and gates
at phases 0 and 15. With A=label10, B=label7, C=label11, the outside
lower difference is (18,207), the fourth correction is J=-55291, and

    p=165888,
    q=0,
    (a,b,z)=(0,13884,24080).

The initial range is already below p and z>b>a. Thus the return is an
exact cyclic rotation at fourth degree, and the component has period
3*72=216 paired blocks. No fourth drift separates its three labels;
the conserved residues supply the obstruction to deeper cancellation.

The full rank paths and sparse score polynomials for both cases are
recorded in networks/network8_two_gate.json and regenerated by
networks/network8_two_gate.py. This derivation uses exact integer binomial moments.

## 5. A general charge criterion on the whole network

Consider any finite periodic comparison network whose first unresolved
scalar coordinate is transported along a directed edge e:u->v as

    y' = y + c_e,     c_e in Z.

Assume every comparator's possible output vertices have a common
predecessor with the same c_e. This is exactly the phase/rank graph of
sorting inside tied lower-moment groups.

Choose a directed spanning tree of a strongly connected component and
assign integer potentials h_v by summing c along the tree. Define

    g = gcd_e (h_u+c_e-h_v).

For g>0, each label has invariant charge y-h_v modulo g. For g=0,
y-h_v itself is invariant. The two output potentials of a comparator
are congruent modulo g (or equal when g=0), because their common
predecessor supplies two edges with identical increments. Thus a
scalar equality at a comparator is possible only between equal-charge
labels. Pairwise distinct initial charges in a component exclude all
future scalar ties there, for every admissible routing.

This criterion works for an interacting component of any size. It does
not require that the next scalar dynamics has already become periodic.
The graph and increments depend only on the established lower profile.

For fourth moments, a periodic reference wire with rank r_ref supplies

    c_(t,i) = B*(D3_i-D3_ref)
              + binom(B,2)*(D2_i-D2_ref)
              + w4(r_i)-w4(r_ref).

The lower differences are periodic within a persistent third-moment
component. This removes a common fourth translation and gives the
integer additive model required above. A fictitious reference path is
sufficient; it need not be an actual greedy label path.

## 6. Exact charge checks on the existing finite certificates

networks/network8_lattice_probe.py independently constructs every edge, an
integer directed-tree potential, every edge defect and its gcd, and
checks the common-predecessor congruence at every comparator.

All 31 nontrivial persistent third-level components in the certificates
for N=3,...,24 have pairwise distinct fourth charges. Selected examples:

| N | Component size | g | Charges in the probe's reference gauge |
|---|---:|---:|---|
| 8 | 3 | 4096 | 0,3218,1170 |
| 12 | 3 | 165888 | 0,152004,10196 |
| 14 | 14 | 1568 | 0,232,930,670,1480,1218,1056,218,458,700,430,970,572,568 |
| 24 | 7 | 18432 | 0,17310,12482,11072,15928,1196,12798 |
| 24 | 8 | 18432 | 0,10630,16374,7038,8368,16342,8076,7216 |

Changing the reference or potential changes the displayed residues;
noncollision is the invariant conclusion.

Every measured g is divisible by 8N^2=2B^2. This divisibility is an
observation, not a theorem. The coarser modulus 8N^2 already separates
all measured components except the N=4 pair, N=6 pair, and the N=8
triple. Their full graph moduli still separate all labels.

Fourth drift cuts also give useful information, but are insufficient
alone. The N=14 component splits by fourth drift into groups of sizes
2,5,5,2. Equal-drift triples remain in N=12,15,16,18,21, and the two
N=24 components retain equal-drift groups of sizes 6 and 7.

## 7. What remains to reach all N

The two-gate lemmas and the arbitrary-network charge lemma are general
statements. Their hypotheses have been checked here only for the
specific recorded networks. They do not prove that all canonical
fair-share lower-profile components have distinct charges, nor that
equal-charge components must split at a higher finite moment.

An all-N proof could establish one of these structural alternatives:

1. A universal charge separation theorem for the eventual third-level
   networks, using their special triangular rank weights and canonical
   initial prefix; or
2. A theorem that every equal-charge cluster has either a strict drift
   cut at a higher degree or a nonresonant arithmetic obstruction to
   unlimited cancellation.

Arbitrary comparator networks cannot be expected to terminate in all
initial conditions: a network can contain a resonant binary subsystem
with the Thue-Morse obstruction. The canonical prefix and fair-share
rank weights must be used in any universal nonresonance argument.

## 8. Counterexamples that isolate the needed hypotheses

### 8.1 The large modulus is not automatic, even for realizable histories

For N=4, prescribe four paired blocks whose first-half orders are

    [0,2,3,1], [2,3,0,1], [1,0,3,2], [3,0,1,2],

and then follow the lower greedy rule. These are valid paired-block
histories, although their first choices are not the canonical greedy
prefix. They produce integer lower coordinates

    [(6,17),(0,0),(2,15),(4,4)].

After 13 further blocks the sorted lower profile has exact period 12.
The component occupying phase-zero ranks 1,2,3 has graph modulus g=4,
not a multiple of 8N^2=128. At its genuine full-score entry, the charges
are 0,2,0 modulo4, so the sufficient distinct-charge test also fails.

This is checked independently by two closed paths of 24 blocks starting
and ending at the same lower slot. The reference path is

    [1,1,2,0,3,2,0,3,2,0,3,1]

repeated twice. Another allowed closed path is

    [1,1,2,1,1,1,2,1,1,1,2,0,3,1,2,0,3,2,0,3,2,0,3,1].

Directly forming their occupied-turn polynomials and expanding at x=1
gives difference coefficients

    degree 0,1,2,3: 0,0,0,0;
    degree 4: -2956.

The fourth differences of all five closed 24-block paths are
0,-1536,-2956,-1652,-3072, with gcd4. This is an explicit obstruction to
proving the observed canonical divisibility solely from periodicity,
triangular weights, or physical occupation counts.

The example is not evidence of aperiodicity: a separate exact run of
20,000 blocks, carrying moments through degree12 and refusing unresolved
ties, used only degrees2..4 throughout. Charge separation is sufficient,
not necessary. The artifacts networks/network8_physical_prefix.json,
networks/network8_noncanonical_witness.json, and networks/network8_false_start_depth.json
preserve the prefix, cycle, paths and finite simulation scope.

### 8.2 An interacting three-wire network can contain Thue-Morse resonance

Even the exact full-germ N=8 network in (1) has nonperiodic orbits when
arbitrary formal initial germs are permitted. Retain its rank-derived
P,Q and r=x^256, but choose A=0, B=P and place Z sufficiently low at
fourth degree. Since 2q>p, the third wire remains separated. The pair
difference then obeys

    D_(n+1) = |r D_n-P|,  D_0=P.

Writing D_n=P F_(n+1)(r) gives the usual two-player recurrence
F_(t+1)=|r F_t-1| with F_1=1. At its dyadic times,

    D_(2^k-1) = P product_(j=0,...,k-1) (r^(2^j)-1).

Its order at x=1 is 4+k, unbounded. Thus mere connectedness of the
three-wire lower comparison graph and the special N=8 forcing do not
imply termination for arbitrary germs. The binary recurrence supplies a
fully explicit nonperiodic orbit.

These chosen germs have not been shown to be realizable as disjoint
player histories entering the N=8 lower profile. In fact, the physical
binary nonresonance/mean obstruction may rule them out. This distinction
is precisely why an all-N argument must use realizable history or the
canonical prefix, beyond the abstract comparison network alone.

### 8.3 The balanced N=12 full forcing is not zero at the next degree

Although its fourth coefficient q is zero, the Laurent germ Q is not
identically zero. Exact sparse polynomial expansion gives

    P_4=165888, P_5=241284096;
    Q_4=0,      Q_5=92897280.

Thus the max-subtraction description in section4 is a statement about
the fourth scalar coordinate. It completely resolves the canonical
N=12 case because its fourth residues are distinct. It must not be
used as a full-germ identity for a hypothetical equal-residue orbit.
The complete sparse P,Q and their coefficients through degree12 are
saved in networks/network8_germ_forcing.json.

## 9. Drift cuts followed by physical binary nonresonance

The binary parity criterion and the mean-load obstruction extend to a
closed pair at **any** fixed lower-moment level. The proof uses only the
pair's eventually periodic unordered rank occupancy, together with its
actual earlier paired-block history. It does not require that the pair
was already a size-two component of the second-moment graph.

Precisely, assume the history from turn zero consists of paired
palindrome blocks for the same N, so every player receives two turns per
block. Suppose a fixed lower-moment profile has become periodic, and a
closed pair in its comparison network has periodic unordered rank sets.
At each phase where higher moments can still be needed, apply the same
full-period parity ratio R/K. If the pair's second moments tie strictly
off the all-player mean at that phase, the physical mean-load lemma
excludes monomial resonance. The parity argument then bounds the needed
degree there. Finitely many phases give a finite depth bound for the
pair, hence eventual periodicity by the finite-depth theorem.

This composes with the two-gate drift lemma: when 2q>p, the third wire
separates at the scalar degree and the remaining pair has periodic
unordered occupancy. If its unresolved phases are off the global
second-moment mean, all physically realizable entering states terminate,
even when their scalar charges collide.

For the N=8 triple, at its first-gate phase the full list of relative
second moments is

    [0,0,8,20,28,-2,-6,8].

The residual pair's common value is0, whereas the global mean is7.
This phase repeats every16 blocks; the other triple gate is permanently
resolved by the strict fourth drift cut. Therefore **any entering state
realized by a paired-palindrome history from turn zero, with this same
lower profile, has bounded comparison depth in this triple**. The
canonical initial fourth values give the stronger explicit degree-four
bound in section3. The resonant arbitrary-germ construction of
section8.2 cannot be a realizable state of this kind.

The paired-history assumption is material. This statement does not
cover an arbitrary false-start word with unequal per-player turn counts,
because the Hamming-count and triangular-load arguments require those
counts at paired-block boundaries.

## 10. The whole strict interior parameter regime

There is a useful extension of the q=0 scalar lemma. Let p,q be integers,
p>0, and

    -p < q < p/2.

Set

    lambda=-(p+q)/3,
    v=(0,(p+q)/3,(2p-q)/3).

Then T(v)=v+lambda*(1,1,1). Along this reference orbit, both nontrivial
sorting gates have strictly nonzero gaps: (p-2q)/3 at the B,Z gate and
(p+q)/3 at the return-pair gate. The routing is

    T(a,b,z)=(z-p,a,b-q).                               (3)

Every integer orbit of T eventually follows this same numerical affine
formula, with equality at a gate still permitted. Consequently

    T^3(u)=u-(p+q)*(1,1,1)

from some finite time onward.

**Proof.** Track squared Euclidean distance between the actual state
and the reference state v+n*lambda. Translations and fixed permutations
preserve the distance. A two-input sorting gate cannot increase it. If
the actual two inputs have strictly opposite order from the reference
inputs, sorting decreases squared distance by twice the product of the
two input gaps. The reference gaps have a fixed positive lower bound,
and the actual strict gaps are integers of magnitude at least one.
Hence each strict routing disagreement causes a uniform positive drop.
The distance is nonnegative, so only finitely many such disagreements
occur. After the last one, every actual gate either follows the
reference routing or has equal inputs, in which case the reference
permutation gives the same numerical result. Thus (3) holds thereafter.
Its third iterate subtracts p+q from every coordinate. This proves the
claim without an invariant-half-line theorem.

This is numerical periodicity. A zero scalar gap may still require
higher moments to decide labels; the charge criterion or a further
nonresonance argument is needed in that case.

The opposite strict drift regime q<-p also has an elementary binary
cut. Since a'=min(a,max(b,z)-p)<=a and S'=S-p-q, the quantity 3a-S drops
by at least -(p+q)>0 per step. Eventually 3a-S<-2p, so
max(b,z)>a+p and the first output is permanently a. The remaining two
coordinates follow

    (b,z) -> (max(b,z)-p, min(b,z)-q),

whose unordered gap obeys d -> |d-(p-q)|. Thus the two strict exterior
regimes reduce to a binary component, while the strict interior has an
eventual three-step numerical affine return. The boundary parameters
q=-p and q=p/2 require separate treatment; no conclusion for them is
asserted here.

The same argument covers the entire N=8 lower-profile basin. Its only
other nontrivial third-level component is the closed pair occupying
labels2,3 in the stored representative. At phase0 it ties at relative
second moment-2 while the all-player mean is6. Hence it is also
nonresonant for every physically realizable paired-history entry. All
remaining components are singletons. Therefore every such entry into
this exact 16-block lower profile has bounded deciding depth and an
eventually periodic labelled continuation. This is a theorem about a
specific lower-profile basin, not a proof that arbitrary N, or every
N=8 lower profile, reaches one of these basins.
