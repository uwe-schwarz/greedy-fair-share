"""Exhaustive small integer cycles and a rational counterexample.

This tests a proposed structural lemma; it is not a proof for arbitrary N.
Python standard library only. Assertions are part of the research checks.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
import json
from pathlib import Path


def weights(n):
    return tuple(comb(n - r, 2) for r in range(n))


def advance(state, rank_weights):
    following = sorted(a + b for a, b in zip(state, rank_weights))
    return tuple(a - following[0] for a in following)


def components(cycle, rank_weights):
    n, period = len(rank_weights), len(cycle)
    parent = list(range(n * period))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for phase, state in enumerate(cycle):
        raw = [a + b for a, b in zip(state, rank_weights)]
        low = min(raw)
        target = cycle[(phase + 1) % period]
        assert advance(state, rank_weights) == target
        for rank, value in enumerate(raw):
            for destination, x in enumerate(target):
                if x == value - low:
                    parent[find(phase * n + rank)] = find(
                        ((phase + 1) % period) * n + destination)

    groups = defaultdict(lambda: [[] for _ in range(period)])
    for phase in range(period):
        for rank in range(n):
            groups[find(phase * n + rank)][phase].append(rank)
    result = []
    for ranks in groups.values():
        size = len(ranks[0])
        assert all(len(row) == size for row in ranks)
        mean_ties = []
        if size == 2:
            for phase, pair in enumerate(ranks):
                state = cycle[phase]
                if all(n * state[r] == sum(state) for r in pair):
                    mean_ties.append(phase)
        result.append({"size": size, "ranks_by_phase": ranks,
                       "binary_mean_tie_phases": mean_ties})
    return result


def exhaustive(n):
    spread = comb(n, 2)
    rank_weights = weights(n)
    seen, cycles = set(), []
    for tail in combinations_with_replacement(range(spread + 1), n - 1):
        state = (0,) + tail
        if state in seen:
            continue
        chain, local = [], {}
        while state not in seen:
            assert state[0] == 0 and state[-1] <= spread
            seen.add(state)
            local[state] = len(chain)
            chain.append(state)
            state = advance(state, rank_weights)
        if state in local:
            cycles.append(chain[local[state]:])
    assert len(seen) == comb(spread + n - 1, n - 1)
    counterexamples = []
    for cycle in cycles:
        groups = components(cycle, rank_weights)
        if any(c["binary_mean_tie_phases"] for c in groups):
            counterexamples.append({"cycle": cycle, "components": groups})
    return {"n": n, "spread_bound": spread, "states_exhausted": len(seen),
            "cycles": len(cycles),
            "cycle_lengths": sorted(map(len, cycles)),
            "counterexamples": counterexamples}


def rational_counterexample():
    n = 4
    centered = [
        tuple(map(Fraction, row)) for row in (
            ("-2", "-1/2", "0", "5/2"),
            ("-3/2", "0", "0", "3/2"),
            ("-3/2", "-1", "1/2", "2"),
            ("-1", "-1/2", "-1/2", "2"),
        )
    ]
    normalized = [tuple(x - row[0] for x in row) for row in centered]
    groups = components(normalized, weights(n))
    assert sorted(c["size"] for c in groups) == [2, 2]
    assert any(c["binary_mean_tie_phases"] for c in groups)
    assert any(x.denominator != 1 for row in normalized for x in row)
    return {"n": n, "scope": "Rational cycle outside integer-difference lattice",
            "centered_cycle": [[str(x) for x in row] for row in centered],
            "normalized_cycle": [[str(x) for x in row] for row in normalized],
            "components": groups}


if __name__ == "__main__":
    result = {
        "integer_tests": [exhaustive(n) for n in (3, 4, 5, 6, 7)],
        "rational_counterexample": rational_counterexample(),
        "general_integer_cycle_lemma_proved": False,
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("mean_cycle_probe.json").write_text(output)
    print(output)
