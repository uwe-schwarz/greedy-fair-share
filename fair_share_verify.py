#!/usr/bin/env python3
"""Exact all-future certificates for the infinitesimal greedy fair-share rule.

Usage: python3 fair_share_verify.py fair_share_certificates.json [3 4 ...]

Python standard library only. No floating point and no fixed positive hit
probability are used. The prefix is reconstructed from zero, not trusted from
the certificate. A proposed periodic tail is proved for every repetition by
the two-cycle lemma explained in fair_share_proof.md.

At the boundary of a 2*N-turn palindrome block, every player has equal zeroth
and first age moments. A row stores differences from player 0 of age moments
2, 3, and 4. Any tie unresolved by these moments is rejected (except at the
initial all-zero state, where players are numbered in order of first use).

This verifies particular N. It does not prove termination of a search for
every N > 2. A failed certificate is not a proof of aperiodicity.
"""

import argparse
import json
from math import comb
from pathlib import Path


class CertificateError(Exception):
    """A finite check did not establish the proposed infinite continuation."""


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def positive(row):
    """Whether the first nonzero coefficient is positive."""
    return next((value > 0 for value in row if value != 0), False)


class BlockDynamics:
    def __init__(self, n):
        require(type(n) is int and n >= 2, "N must be an integer >= 2")
        self.n = n
        self.width = 2 * n
        self.shift2 = comb(self.width, 2)
        self.weights = [
            tuple(comb(self.width - r, k) + comb(r + 1, k)
                  for k in (2, 3, 4))
            for r in range(n)
        ]

    def advance(self, rows, order):
        """Advance a prescribed permutation followed by its reversal."""
        rank = [0] * self.n
        for r, player in enumerate(order):
            rank[player] = r
        base2, base3, base4 = self.weights[rank[0]]
        result = []
        for player, (d2, d3, d4) in enumerate(rows):
            w2, w3, w4 = self.weights[rank[player]]
            result.append((
                d2 + w2 - base2,
                d3 + self.width * d2 + w3 - base3,
                d4 + self.width * d3 + self.shift2 * d2 + w4 - base4,
            ))
        return result

    def prefix(self, length, cycle):
        """Reconstruct and validate the exact greedy prefix of length blocks."""
        rows = [(0, 0, 0)] * self.n
        last_mismatch = -1
        for block in range(length):
            order = sorted(range(self.n), key=lambda player: (rows[player], player))
            if block:
                require(all(rows[a] != rows[b] for a, b in zip(order, order[1:])),
                        f"unresolved prefix tie at block {block}; need higher moments")
            expected = cycle[(block - length) % len(cycle)]
            if order != expected:
                first = next(r for r in range(self.n) if order[r] != expected[r])
                # Both words are palindromes, so the first mismatch in the
                # first half mirrors the last mismatch in the entire block.
                last_mismatch = self.width * block + self.width - 1 - first
            rows = self.advance(rows, order)
        return rows, last_mismatch


def differences(rows, order):
    return [tuple(rows[b][d] - rows[a][d] for d in range(3))
            for a, b in zip(order, order[1:])]


def least_word_period(cycle):
    """Exact prefix-function calculation of the repeated word's least period."""
    word = [player for order in cycle for player in [*order, *reversed(order)]]
    prefix = [0] * len(word)
    for i in range(1, len(word)):
        j = prefix[i - 1]
        while j and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    candidate = len(word) - prefix[-1]
    return candidate if len(word) % candidate == 0 else len(word)


def verify(certificate):
    n = certificate["n"]
    dynamics = BlockDynamics(n)
    start = certificate["certificate_start_blocks"]
    cycle = certificate["cycle"]
    require(type(start) is int and start > 0, "certificate start must be positive")
    require(certificate.get("degree", 4) == 4, "this verifier uses moments through 4")
    require(bool(cycle), "empty proposed cycle")
    require(certificate["period_blocks"] == len(cycle), "inconsistent period length")
    for order in cycle:
        require(all(type(i) is int for i in order)
                and sorted(order) == list(range(n)), "cycle entry is not a permutation")

    rows, last_mismatch = dynamics.prefix(start, cycle)
    if "initial" in certificate:
        require(rows == [tuple(row) for row in certificate["initial"]],
                "supplied initial state disagrees with reconstructed greedy prefix")

    # At a fixed phase of successive repetitions the FULL difference germ obeys
    # F_(k+1)(z) = (1+z)^L F_k(z) + C(z), where L = total period in turns.
    # If d is the first degree present in F_0 or F_1, all lower coefficients
    # vanish for every k, and [z^d]F_k = a + k*b. This follows algebraically;
    # it is not an empirical inference from two observed repetitions.
    first = []
    for phase, order in enumerate(cycle):
        comparisons = differences(rows, order)
        require(all(positive(row) for row in comparisons),
                f"first cycle has a wrong or unresolved order at phase {phase}")
        first.append(comparisons)
        rows = dynamics.advance(rows, order)

    counts = {2: 0, 3: 0, 4: 0}
    growing = 0
    for phase, order in enumerate(cycle):
        for adjacent, (f0, f1) in enumerate(zip(first[phase], differences(rows, order))):
            d = next((j for j in range(3) if f0[j] != 0 or f1[j] != 0), None)
            require(d is not None, "unresolved all-future comparison")
            a, b = f0[d], f1[d] - f0[d]
            require(a >= 0 and b >= 0,
                    f"N={n}, phase={phase}, comparison={adjacent}: "
                    f"first relevant coefficient is {a} + k*({b}); "
                    "it does not stay nonnegative")
            # a=0,b>0 is strict for k>=1. k=0 was already checked above
            # using the possibly higher first nonzero coefficient of F_0.
            counts[d + 2] += 1
            growing += b > 0
        rows = dynamics.advance(rows, order)

    return {
        "n": n,
        "certified_from_index": dynamics.width * start,
        "period_turns": dynamics.width * len(cycle),
        "least_period_turns": least_word_period(cycle),
        "minimal_preperiod_terms": last_mismatch + 1,
        "adjacent_comparisons": (n - 1) * len(cycle),
        "deciding_degree_counts": counts,
        "positive_slope_comparisons": growing,
        "result": "PROVED FOR EVERY FUTURE REPETITION",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("players", type=int, nargs="*")
    args = parser.parse_args()
    payload = json.loads(args.certificates.read_text(encoding="utf-8"))
    certificates = payload["certificates"] if isinstance(payload, dict) else payload
    requested = set(args.players)
    if requested:
        available = {c["n"] for c in certificates}
        require(requested <= available, f"missing certificates: {sorted(requested - available)}")
    for certificate in certificates:
        if not requested or certificate["n"] in requested:
            print(json.dumps(verify(certificate), sort_keys=True), flush=True)


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError) as error:
        raise SystemExit(f"NOT CERTIFIED: {error}")
