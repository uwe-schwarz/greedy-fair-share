#!/usr/bin/env python3
"""Exact finite-N certificates excluding closed binary second-mean ties.

Requires Python 3 and NumPy. All arithmetic that can grow uses Python integers
via NumPy dtype=object; there is no floating-point solver or integer overflow.

Examples:
    python3 mean_pair_certificates.py
    python3 mean_pair_certificates.py 7 40 146
    python3 mean_pair_certificates.py --range 3 60 --output mean_pairs.json

This is a sufficient finite certificate. An ambiguous witness, a configured
cap, or an inconclusive mean interval is reported as not_established.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from math import lcm
from pathlib import Path
import sys

import numpy as np

if not __debug__:
    raise RuntimeError(
        "Run without -O: certificate consistency assertions are required."
    )


def max_plus_closure(weights: np.ndarray, present: np.ndarray):
    """Longest-path closure, or a positive directed closed-walk witness.

    Missing edges are represented by a separate Boolean mask, not by a finite
    surrogate for minus infinity. Therefore every comparison is exact.
    """
    distance = weights.copy()
    reachable = present.copy()
    n = len(distance)
    for k in range(n):
        via_k = reachable[:, k, None] & reachable[None, k, :]
        candidate = distance[:, k, None] + distance[None, k, :]
        improve = via_k & (~reachable | (candidate > distance))
        distance[improve] = candidate[improve]
        reachable |= via_k
        for i in range(n):
            if reachable[i, i] and distance[i, i] > 0:
                return distance, reachable, {
                    "vertex": i,
                    "positive_closed_walk_weight": int(distance[i, i]),
                }
    return distance, reachable, None


def set_edge(weights, present, source: int, destination: int, cost: int):
    if not present[source, destination] or cost > weights[source, destination]:
        weights[source, destination] = cost
        present[source, destination] = True


def recurrent_order_constraints(n: int, max_blocks: int, max_order: int):
    rank_weights = [(n - r) * (n - r - 1) // 2 for r in range(n)]
    total_weight = sum(rank_weights)
    state = (0,) * n
    seen = {}
    orbit = []
    record = {"n": n}

    while state not in seen:
        if len(orbit) >= max_blocks:
            record.update(
                status="not_established",
                reason="base_orbit_cap",
                examined_blocks=len(orbit),
            )
            return record, None
        seen[state] = len(orbit)
        orbit.append(state)
        raw = sorted(a + b for a, b in zip(state, rank_weights))
        state = tuple(a - raw[0] for a in raw)

    onset = seen[state]
    cycle = orbit[onset:]
    record.update(base_preperiod_blocks=onset, base_period_blocks=len(cycle))
    raw_totals = [
        sum(s[i] + rank_weights[i] for s in cycle) for i in range(n)
    ]
    if len(set(raw_totals)) != n:
        record.update(
            status="not_established", reason="ambiguous_common_order_witness"
        )
        return record, None

    order = sorted(range(n), key=lambda i: raw_totals[i])
    permutation = [0] * n
    for destination, source in enumerate(order):
        permutation[source] = destination
    assert all(
        [s[i] + rank_weights[i] for i in order]
        == sorted(s[i] + rank_weights[i] for i in range(n))
        for s in cycle
    )

    # A strict raw-order witness, together with Euclidean nonexpansiveness,
    # makes this permutation common to every recurrent second-moment state.
    remaining = set(range(n))
    permutation_order = 1
    while remaining:
        i = min(remaining)
        part = []
        while i in remaining:
            remaining.remove(i)
            part.append(i)
            i = permutation[i]
        assert n * sum(rank_weights[j] for j in part) == len(part) * total_weight
        permutation_order = lcm(permutation_order, len(part))

    record["permutation_order"] = permutation_order
    if permutation_order > max_order:
        record.update(status="not_established", reason="permutation_order_cap")
        return record, None

    weights = np.zeros((n, n), dtype=object)
    present = np.eye(n, dtype=bool)
    origins = np.arange(n)
    offsets = np.zeros(n, dtype=object)
    increment = np.array(
        [n * w - total_weight for w in rank_weights], dtype=object
    )
    target = np.array(permutation, dtype=int)

    for _ in range(permutation_order):
        for j in range(n - 1):
            delta = offsets[j] - offsets[j + 1]
            assert delta % n == 0
            set_edge(
                weights,
                present,
                int(origins[j]),
                int(origins[j + 1]),
                int(delta // n),
            )
        next_origins = np.empty(n, dtype=int)
        next_offsets = np.empty(n, dtype=object)
        next_origins[target] = origins
        next_offsets[target] = offsets + increment
        origins, offsets = next_origins, next_offsets

    assert np.array_equal(origins, np.arange(n))
    assert all(a == 0 for a in offsets)
    set_edge(weights, present, n - 1, 0, -n * (n - 1) // 2)
    return record, (weights, present)


def certify(n: int, max_blocks: int = 100_000, max_order: int = 100_000):
    if n < 3:
        raise ValueError("This certificate concerns N >= 3.")
    record, graph = recurrent_order_constraints(n, max_blocks, max_order)
    if graph is None:
        return record
    weights, present = graph
    distance, reachable, positive = max_plus_closure(weights, present)
    assert positive is None  # The known recurrent orbit satisfies these bounds.
    assert reachable.all()  # The ordered chain and spread edge connect all ranks.

    # A proper pair at the mean cannot be the minimum or maximum pair.
    candidates = []
    for r in range(1, n - 2):
        if distance[r, r + 1] > 0:
            continue
        assert distance[r, r + 1] == 0
        # Add y_(r+1) -> y_r with weight zero to pin the equal pair.
        pinned = np.maximum(
            distance, distance[:, r + 1, None] + distance[None, r, :]
        )
        sum_lower = sum(pinned[r, :])
        sum_upper = -sum(pinned[:, r])
        if sum_lower <= 0 <= sum_upper:
            candidates.append(r)

    cases = []
    for r in candidates:
        isolated_weights = weights.copy()
        isolated_present = present.copy()
        in_pair = np.zeros(n, dtype=bool)
        in_pair[r : r + 2] = True
        cross_boundary = (
            np.logical_xor(in_pair[:, None], in_pair[None, :]) & present
        )
        isolated_weights[cross_boundary] += 1
        set_edge(isolated_weights, isolated_present, r + 1, r, 0)
        bounded, reached, positive = max_plus_closure(
            isolated_weights, isolated_present
        )
        if positive is not None:
            cases.append(
                {"pair_ranks": [r, r + 1], "excluded_by": "positive_cycle", **positive}
            )
            continue
        assert reached.all()
        sum_lower = int(sum(bounded[r, :]))
        sum_upper = int(-sum(bounded[:, r]))
        excluded = sum_lower > 0 or sum_upper < 0
        cases.append(
            {
                "pair_ranks": [r, r + 1],
                "excluded_by": "mean_interval" if excluded else None,
                "sum_lower": sum_lower,
                "sum_upper": sum_upper,
            }
        )

    success = all(case["excluded_by"] is not None for case in cases)
    record.update(
        status="certified" if success else "not_established",
        real_mean_pair_ranks=candidates,
        isolation_cases=cases,
    )
    if not success:
        record["reason"] = "isolation_constraints_inconclusive"
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", nargs="*", type=int, help="Selected player counts, each >= 3")
    parser.add_argument("--range", dest="span", nargs=2, type=int, metavar=("FIRST", "LAST"))
    parser.add_argument("--max-blocks", type=int, default=100_000)
    parser.add_argument("--max-permutation-order", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    selected = list(args.n)
    if args.span:
        first, last = args.span
        if first > last:
            parser.error("--range FIRST LAST requires FIRST <= LAST")
        selected.extend(range(first, last + 1))
    if not selected:
        selected = list(range(3, 9))
    if min(selected) < 3:
        parser.error("Player counts must be >= 3")
    if args.max_blocks < 1 or args.max_permutation_order < 1:
        parser.error("Both configured caps must be positive")
    selected = sorted(set(selected))
    records = [
        certify(n, args.max_blocks, args.max_permutation_order) for n in selected
    ]
    report = {
        "date": datetime.now(timezone.utc).date().isoformat(),
        "claim": "No closed binary mean tie on any integer recurrent second-moment cycle",
        "scope": "Finite selected player counts; not an all-N or full-word periodicity theorem",
        "method": "Exact arbitrary-precision integer difference constraints with a strict common-order witness",
        "caps": {
            "base_blocks": args.max_blocks,
            "permutation_order": args.max_permutation_order,
        },
        "selected": selected,
        "certified_count": sum(r["status"] == "certified" for r in records),
        "not_established_count": sum(r["status"] != "certified" for r in records),
        "results": records,
    }
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    sys.stdout.write(encoded)


if __name__ == "__main__":
    main()
