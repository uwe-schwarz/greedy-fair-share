# Research log

English is canonical. Entries distinguish proved statements, exact finite checks, and approaches that remain conjectural. The objective is eventual periodicity of the canonical greedy sequence for every integer N >= 3.

## 2026-11-26 — Universal-proof investigation, first checkpoint

Starting point: commit `61cd578` proves the fixed-depth normal form and finite-depth equivalence, supplies the binary parity and mean criteria, and records the component experiments. The all-N bounded-depth statement is not yet proved.

Three complementary lines are being investigated:

1. **Interacting components.** Derive a reusable arithmetic obstruction for a periodic network of pair comparisons. The three-player persistent component inside N=8 is the smallest known concrete test case. A fixed pair's occupancy invariant does not survive a change of partners, so applying the binary theorem separately to instantaneous pairs is invalid.
2. **Binary resonance.** Exclude the phase-aligned, purely periodic pair occupancy required by the monomial exception, using the canonical initial state and integer triangular loads. The stronger claim that every integer base cycle lacks a binary mean tie is also being tested. The known rational N=4 counterexample prevents an argument that discards integrality.
3. **An infinite hierarchy of ties.** Investigate whether persistent nontrivial components at every moment degree force an exceptional substitution or occupancy structure. The finite-depth theorem alone cannot exclude this, as N=2 demonstrates. Any argument must justify compatibility between the component partitions and phase periods at different depths.

No universal conclusion follows from these proposed routes yet. Intermediate lemmas and counterexamples will be added here as they are checked.

### Earlier observation found in a primary source

The historical observation predates the 2017 OEIS entry: in a comment dated **2012-11-01** on Zachary Abel's [*Dueling Dilettantes*](https://blog.zacharyabel.com/2012/02/dueling-dilettantes/), Anders Kaseorg reports eventual periods 54, 192, 500, and 864 for 3, 4, 5, and 6 players. The comment reports computation and supplies no all-N proof. The post itself is dated 2012-02-11; that is not the date of the multiplayer comment.

The [binary false-start paper](https://arxiv.org/html/2610.00880v1) proves an arithmetic termination theorem for two players after a noncanonical prefix. Its modulo-four argument uses the eventual decomposition into adjacent opposite-sign pairs. A multiplayer extension must establish an analogous decomposition; deleting other players' turns changes the time exponents and does not justify importing that theorem.
