"""Challenge the proposed extension of rank rigidity to convex rank weights."""
from itertools import combinations
import json

from _support import REPO_ROOT
from structure_certificates import step, certify
from network_rank_rigidity import analyze


def discover_weights(v, cap=50000, max_macros=5000):
    n = len(v)
    x = (0,) * n
    seen = {}
    while x not in seen:
        if len(seen) >= cap:
            raise ValueError('base cap')
        seen[x] = len(seen)
        raw = sorted(a+b for a,b in zip(x,v))
        x = tuple(a-raw[0] for a in raw)
    mu, p = seen[x], len(seen)-seen[x]
    x = y = (0,) * n
    for _ in range(mu):
        x, y = step(x, y, v)
    xbase = x
    ys = [y]
    changes = {}
    for j in range(min(max_macros, max(0, (cap-mu)//p))):
        for _ in range(p):
            x, y = step(x, y, v)
        assert x == xbase
        ys.append(y)
        change = tuple(b-a for a,b in zip(ys[j],y))
        if change in changes:
            i = changes[change]
            delta = tuple(b-a for a,b in zip(ys[i],ys[j]))
            phases = certify(xbase, ys[i], delta, (j-i)*p, v)
            if phases:
                return mu+j*p, phases, {'base_start':mu, 'base_period':p}
        changes[change] = j
    raise ValueError('lower cap')


def test(v):
    try:
        start, phases, meta = discover_weights(v)
        cs = analyze(len(v), phases, v)
        result = {'weights':v, 'start':start, 'period':len(phases), **meta,
                  'components':cs,
                  'all_rank_holonomies_zero': all(c['all_rank_holonomies_zero'] for c in cs)}
        if not result['all_rank_holonomies_zero']:
            result['certified_phases'] = phases
        return result
    except ValueError as exc:
        return {'weights':v, 'not_established':str(exc)}


if __name__ == '__main__':
    special = [(3,2,1,0), (11,6,3,1,0)]
    for v in special:
        print(json.dumps(test(v)), flush=True)
    for n, bound in [(4,10), (5,9), (6,9)]:
        for gaps in combinations(range(1,bound+1), n-1):
            v = tuple(sum(gaps[:n-1-r]) for r in range(n))
            result = test(v)
            print(json.dumps(result), flush=True)
            if result.get('all_rank_holonomies_zero') is False:
                raise SystemExit(0)
