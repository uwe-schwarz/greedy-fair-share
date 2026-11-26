"""Test whether every rank-only cost has zero centered holonomy.

This is a structural test of a certified lower affine regime, not an all-N
proof. It imports the separate lower-regime discovery routine and never uses
the known full-word certificates.
"""
from collections import defaultdict, deque
from math import gcd
import json
import sys

from _support import REPO_ROOT
from structure_certificates import discover, weights


def analyze(n, phases, v=None, include_potentials=False):
    if v is None:
        v = weights(n)
    p = len(phases)
    size = n * p
    edges = [[] for _ in range(size)]
    weak = [[] for _ in range(size)]
    for j, (x, y, slope) in enumerate(phases):
        nxt = (j + 1) % p
        tx, ty, ts = phases[nxt]
        targets = defaultdict(list)
        for r in range(n):
            key = (tx[r], ty[r] + (ts[r] if nxt == 0 else 0), ts[r])
            targets[key].append(nxt * n + r)
        raw = [a + b for a, b in zip(x, v)]
        low = min(raw)
        for r in range(n):
            u = j * n + r
            for w in targets[(raw[r] - low, y[r] + x[r], slope[r])]:
                edges[u].append(w)
                weak[u].append(w)
                weak[w].append(u)

    seen = set()
    result = []
    for root in range(size):
        if root in seen:
            continue
        seen.add(root)
        nodes = [root]
        for u in nodes:
            for w in weak[u]:
                if w not in seen:
                    seen.add(w)
                    nodes.append(w)
        byphase = [[] for _ in range(p)]
        for u in nodes:
            byphase[u // n].append(u % n)
        s = len(byphase[0])
        assert all(len(rs) == s for rs in byphase)
        if s == 1:
            continue
        base = [tuple(-int(r in rs) for r in range(n)) for rs in byphase]
        h = {root: (0,) * n}
        queue = deque([root])
        moduli = [0] * n
        first_defect = None
        while queue:
            u = queue.popleft()
            j, r = divmod(u, n)
            proposed = tuple(h[u][k] + base[j][k] + (s if k == r else 0)
                             for k in range(n))
            for w in edges[u]:
                if w not in h:
                    h[w] = proposed
                    queue.append(w)
                else:
                    defect = tuple(a - b for a, b in zip(proposed, h[w]))
                    if first_defect is None and any(defect):
                        first_defect = {'source': u, 'target': w, 'vector': defect}
                    moduli = [gcd(a, b) for a, b in zip(moduli, defect)]
        assert set(h) == set(nodes)
        item = {'size': s, 'rank_moduli': moduli,
                'all_rank_holonomies_zero': not any(moduli),
                'first_defect': first_defect}
        if include_potentials:
            item['phase_zero_slots'] = byphase[0]
            item['phase_zero_potentials'] = {r:h[r] for r in byphase[0]}
        result.append(item)
    return result


if __name__ == '__main__':
    for n in list(map(int, sys.argv[1:])) or list(range(2, 33)):
        try:
            start, phases, meta = discover(n)
            components = analyze(n, phases)
            result = {'n': n, 'start': start, 'period': len(phases),
                      'components': components,
                      'all_rank_holonomies_zero': all(
                          c['all_rank_holonomies_zero'] for c in components)}
        except ValueError as exc:
            result = {'n': n, 'not_established': str(exc)}
        print(json.dumps(result), flush=True)
