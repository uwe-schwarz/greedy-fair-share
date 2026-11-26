"""Prime-power root-of-unity characters of exact rank-count charges."""
from collections import defaultdict
import json

from _support import REPO_ROOT
from structure_certificates import discover, BlockDynamics
from network_rank_rigidity import analyze


def prime_power_factors(b):
    result=[]
    p=2
    while p*p <= b:
        if b%p==0:
            q=1
            while b%p==0:
                b//=p; q*=p
                result.append((p,q))
        p+=1
    if b>1:
        result.append((b,b))
    return result


def remainder(coefficients, p, q):
    # Phi_(p^a)(x) = sum_(j=0)^(p-1) x^(j*p^(a-1)).
    step=q//p
    degree=q-step
    coefficients=list(coefficients)
    for k in range(len(coefficients)-1, degree-1, -1):
        c=coefficients[k]
        if c:
            for j in range(p):
                coefficients[k-degree+j*step]-=c
    return tuple(coefficients[:degree])


def signature(rank_vector, n):
    b=2*n
    coefficients=[0]*(b+1)
    for r,c in enumerate(rank_vector):
        coefficients[b-r]+=c
        coefficients[r+1]+=c
    return tuple(remainder(coefficients,p,q) for p,q in prime_power_factors(b))


def run(n):
    start,phases,meta=discover(n)
    cs=analyze(n,phases,include_potentials=True)
    dyn=BlockDynamics(n)
    rows=[(0,0,0)]*n
    counts=[[0]*n for _ in range(n)]
    for m in range(start):
        order=sorted(range(n),key=lambda i:(rows[i],i))
        assert m==0 or all(rows[a]!=rows[b] for a,b in zip(order,order[1:]))
        for r,a in enumerate(order):
            counts[a][r]+=1
        rows=dyn.advance(rows,order)
    order=sorted(range(n),key=lambda i:(rows[i],i))
    result=[]
    for c in cs:
        s=c['size']; slots=c['phase_zero_slots']
        totals=[sum(counts[order[r]][k] for r in slots) for k in range(n)]
        charges={order[r]:tuple(s*counts[order[r]][k]-totals[k]
                                  -c['phase_zero_potentials'][r][k]
                                  for k in range(n)) for r in slots}
        classes=defaultdict(list)
        for a,vector in charges.items():
            classes[signature(vector,n)].append(a)
        result.append({'size':s,
                       'rank_rigid':c['all_rank_holonomies_zero'],
                       'rank_charge_vectors_distinct':len(set(charges.values()))==s,
                       'prime_power_characters_distinct':len(classes)==s,
                       'unresolved_classes':[a for a in classes.values() if len(a)>1],
                       'rank_charges':charges})
    return {'n':n,'start':start,'period':len(phases),'components':result,
            'all_components_separated':all(c['rank_rigid'] and c['prime_power_characters_distinct'] for c in result)}


if __name__=='__main__':
    for n in range(2,25):
        print(json.dumps(run(n)),flush=True)
