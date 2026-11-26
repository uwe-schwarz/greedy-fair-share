"""Parity obstruction at every tie phase of closed binary components.

Full second-moment period; does not assume identical forcing between ties.
The prefix is generated with exact integer moments and unresolved ties abort.
"""
from pathlib import Path
import hashlib,json,sys,time
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics
from component_scan import transport
def normalize(p):
    if p == 0:
        return None, 0
    exponent = (p & -p).bit_length() - 1
    return exponent, p >> exponent


def fingerprint(p):
    return hashlib.sha256(p.to_bytes((p.bit_length()+7)//8,'little')).hexdigest()


def analyze(n):
    mu,cycle,w,comps,sizes=transport(n);p=len(cycle);B=2*n;L=B*p
    summary={'n':n,'base_preperiod_blocks':mu,'base_period_blocks':p,'component_sizes':sizes,'binary_components':[]}
    if not comps:return summary
    dyn=BlockDynamics(n);rows=[(0,0,0)]*n;orders=[]
    for block in range(mu+1):
        order=sorted(range(n),key=lambda i:(rows[i],i))
        if block and any(rows[a]==rows[b] for a,b in zip(order,order[1:])):
            raise ValueError(f'N={n}: unresolved prefix tie at block {block}; increase moment depth')
        orders.append(order)
        rows=dyn.advance(rows,order)
    for c in comps:
        a,b=[orders[mu][r] for r in c['ranks'][0]]
        D=0
        for order in orders[:mu]:
            ra,rb=order.index(a),order.index(b)
            D=(D<<B)^(1<<(B-ra))^(1<<(ra+1))^(1<<(B-rb))^(1<<(rb+1))
        gs=[]
        for ra,rb in c['ranks']:
            gs.append((1<<(B-ra))^(1<<(ra+1))^(1<<(B-rb))^(1<<(rb+1)))
        K=0
        for g in gs:K=(K<<B)^g
        assert D.bit_count() == 4 * mu, 'Pair prefix must contain four occupied turns per block'
        assert K.bit_count() == 4 * p, 'Pair period must contain four occupied turns per block'
        assert D.bit_length() - 1 <= B * mu and K.bit_length() - 1 <= L
        initialK=K;R=(D<<L)^D^K;Rlo,Rnorm=normalize(R)
        details=[]
        for phase in range(p):
            if phase in c['ties']:
                Klo,Knorm=normalize(K)
                ismono=bool(Knorm) and Rnorm==Knorm
                details.append({'phase':phase,'ranks':c['ranks'][phase],
                                'R_over_K_is_monomial_mod2':ismono,
                                'monomial_exponent':Rlo+B*phase-Klo if ismono else None,
                                'normalized_tied_load':cycle[phase][c['ranks'][phase][0]],
                                'global_normalized_load_sum':sum(cycle[phase]),
                                'tie_at_global_mean':n*cycle[phase][c['ranks'][phase][0]]==sum(cycle[phase]),
                                'K_nonzero':bool(K),'K_degree':K.bit_length()-1,
                                'K_lowest_x_power':Klo,'K_sha256':fingerprint(K)})
            K=(K<<B)^(gs[phase]<<L)^gs[phase]
        assert K==initialK
        summary['binary_components'].append({'ranks_at_phase_0':c['ranks'][0],
            'fixed_player_labels': [a,b],
            'initial_D_degree':D.bit_length()-1,'initial_D_sha256':fingerprint(D),
            'initial_pair_occupied_turns':D.bit_count(),'period_pair_occupied_turns':initialK.bit_count(),
            'R_degree':R.bit_length()-1,'R_lowest_x_power':Rlo,'R_nonzero':bool(R),'R_sha256':fingerprint(R),
            'tie_phases':details,
            'all_tie_phases_nonmonomial':all(not d['R_over_K_is_monomial_mod2'] for d in details)})
    return summary


def main():
    scan=[json.loads(line) for line in Path(__file__).with_name('component_scan.jsonl').read_text().splitlines()]
    assert not any('prefix_degree4_tie_block' in row for row in scan), 'Unresolved scan prefix; increase moment depth'
    ns=sorted({2,7,10,13,23}|{r['n'] for r in scan if r['binary']})
    results=[];start=time.monotonic()
    for n in ns:
        r=analyze(n);results.append(r)
        print(json.dumps({'n':n,'binary_components':len(r['binary_components']),
            'failures':[b for b in r['binary_components'] if not b['all_tie_phases_nonmonomial']]}),flush=True)
    payload={'date':'2026-11-26','scope':'All closed size-two components with second-moment ties for N=25..259, plus N=7,10,13,23 and the N=2 control; full-period parity test at every tie phase',
        'results':results}
    Path(__file__).with_name('parity_components.json').write_text(json.dumps(payload, separators=(',', ':'), sort_keys=True)+'\n')
if __name__=='__main__':main()
