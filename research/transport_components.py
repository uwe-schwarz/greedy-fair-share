"""Exact second-moment transport graphs and isolated binary return maps.

Research calculations, not a universal-periodicity proof. Standard library only.
"""

from collections import defaultdict
from fractions import Fraction
from math import comb
import json


def base_cycle(n):
    weights = [comb(n - r, 2) for r in range(n)]
    state = (0,) * n
    seen, states = {}, []
    while state not in seen:
        seen[state] = len(states)
        states.append(state)
        raw = sorted(x + w for x, w in zip(state, weights))
        state = tuple(x - raw[0] for x in raw)
    mu = seen[state]
    return mu, states[mu:], weights


def transport(n):
    mu, cycle, weights = base_cycle(n)
    period = len(cycle)
    parent = list(range(n * period))

    def find(i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        parent[find(i)] = find(j)

    edges = []
    for t, state in enumerate(cycle):
        raw = [x + w for x, w in zip(state, weights)]
        low = min(raw)
        for r, value in enumerate(raw):
            destinations = [s for s, x in enumerate(cycle[(t + 1) % period])
                            if x == value - low]
            edges.append((t, r, destinations))
            for s in destinations:
                union(t * n + r, ((t + 1) % period) * n + s)

    groups = defaultdict(list)
    for i in range(n * period):
        groups[find(i)].append((i // n, i % n))
    components = []
    for group in groups.values():
        ranks = [[r for t, r in group if t == phase] for phase in range(period)]
        size = len(ranks[0])
        assert all(len(row) == size for row in ranks)
        component = {"size": size, "ranks_at_phase_0": ranks[0]}
        if size == 2:
            ties = [t for t, rs in enumerate(ranks)
                    if cycle[t][rs[0]] == cycle[t][rs[1]]]
            component["tie_phases"] = ties
            component["rank_paths"] = ranks
        components.append(component)
    return mu, cycle, weights, components


def shifted_sum(row, turns, degree):
    return [sum(comb(turns, k - j) * row[j] for j in range(k + 1))
            for k in range(degree + 1)]


def rank_weights(n, rank, degree):
    return [comb(2 * n - rank, k) + comb(rank + 1, k)
            for k in range(degree + 1)]


def prefix_rows(n, count, degree=8):
    rows = [[0] * (degree + 1) for _ in range(n)]
    for block in range(count):
        order = sorted(range(n), key=lambda i: (rows[i], i))
        assert block == 0 or all(rows[a] != rows[b] for a, b in zip(order, order[1:]))
        for r, player in enumerate(order):
            shifted = shifted_sum(rows[player], 2 * n, degree)
            inc = rank_weights(n, r, degree)
            rows[player] = [a + b for a, b in zip(shifted, inc)]
    return rows


def binary_return(n, cycle, weights, ranks, phase, degree=8):
    """Start A in smaller rank, B in larger rank, return at next pair tie.

    The signed score difference B-A then obeys D_next=x**L*D+H.
    The other initial order gives the opposite H.
    """
    p = len(cycle)
    a, b = ranks[phase]
    assert cycle[phase][a] == cycle[phase][b]
    h = [0] * (degree + 1)
    path = []
    for elapsed in range(1, p + 1):
        t = (phase + elapsed - 1) % p
        path.append((a, b))
        wa, wb = rank_weights(n, a, degree), rank_weights(n, b, degree)
        h = [v + y - x for v, x, y in zip(shifted_sum(h, 2 * n, degree), wa, wb)]
        nxt = (t + 1) % p
        raw = [x + w for x, w in zip(cycle[t], weights)]
        low = min(raw)
        dest_a = [r for r in ranks[nxt] if cycle[nxt][r] == raw[a] - low]
        dest_b = [r for r in ranks[nxt] if cycle[nxt][r] == raw[b] - low]
        if len(dest_a) == 2:
            assert len(dest_b) == 2
            return {"blocks": elapsed, "H_coefficients_z_0_to_8": h, "rank_path_A_B": path}
        assert len(dest_a) == len(dest_b) == 1
        a, b = dest_a[0], dest_b[0]
    raise AssertionError("binary component did not return to a tie")


def investigate(n):
    mu, cycle, weights, components = transport(n)
    result = {"n": n, "base_preperiod_blocks": mu,
              "base_period_blocks": len(cycle),
              "component_sizes": sorted(c["size"] for c in components),
              "binary_components": []}
    for c in components:
        if c["size"] != 2:
            continue
        binary = dict(c)
        returns = []
        for phase in c["tie_phases"]:
            ret = binary_return(n, cycle, weights, c["rank_paths"], phase)
            ret["phase"] = phase
            rows = prefix_rows(n, mu + phase)
            order = sorted(range(n), key=lambda i: (rows[i], i))
            a, b = [order[r] for r in c["rank_paths"][phase]]
            d = [y - x for x, y in zip(rows[a], rows[b])]
            ret["actual_initial_D_coefficients_z_0_to_8"] = d
            dh = next((k for k, x in enumerate(ret["H_coefficients_z_0_to_8"]) if x), None)
            dd = next((k for k, x in enumerate(d) if x), None)
            ret["valuation_H_through_8"] = dh
            ret["valuation_D_through_8"] = dd
            if dh is not None and dd is not None and dd >= dh:
                ret["constant_D_over_minus_H"] = str(Fraction(-d[dh], ret["H_coefficients_z_0_to_8"][dh]))
            returns.append(ret)
        binary["returns"] = returns
        result["binary_components"].append(binary)
    return result


if __name__ == "__main__":
    print(json.dumps([investigate(n) for n in (2, 7, 10, 13, 23)], indent=2))
