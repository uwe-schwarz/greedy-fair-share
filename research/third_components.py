"""Persistent degree-three comparison components on certified cycles."""
import sys,json
from pathlib import Path
from collections import defaultdict
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics


def analyze(c):
    n=c['n'];dyn=BlockDynamics(n);cycle=c['cycle'];initial=[tuple(r) for r in c['initial']]
    end=initial
    for order in cycle:end=dyn.advance(end,order)
    assert all(a[0]==b[0] for a,b in zip(initial,end))
    slopes=[b[1]-a[1] for a,b in zip(initial,end)]
    parent=list(range(n));ties=[];max_group=1
    def find(a):
        while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
        return a
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b:parent[b]=a
    rows0=initial;rows1=end
    for phase,order in enumerate(cycle):
        groups=defaultdict(list)
        for player in range(n):
            assert rows0[player][0]==rows1[player][0]
            assert rows1[player][1]-rows0[player][1]==slopes[player]
            key=(rows0[player][0],rows0[player][1],slopes[player])
            groups[key].append(player)
        for group in groups.values():
            if len(group)>1:
                max_group=max(max_group,len(group))
                for b in group[1:]:union(group[0],b)
                ties.append({'phase':phase,'players':group,'ranks':[order.index(i) for i in group]})
        rows0=dyn.advance(rows0,order);rows1=dyn.advance(rows1,order)
    comps=defaultdict(list)
    for player in range(n):comps[find(player)].append(player)
    comp_list=sorted(comps.values(),key=lambda x:(len(x),x))
    return {'n':n,'certificate_start_blocks':c['certificate_start_blocks'],'period_blocks':len(cycle),
            'third_slopes_by_label':slopes,'persistent_tie_events':len(ties),
            'largest_simultaneous_tie_group':max_group,
            'component_sizes':sorted(len(g) for g in comp_list),
            'nontrivial_components':[g for g in comp_list if len(g)>1],
            'tie_events':ties}


def main():
    payload=json.loads((ROOT/'fair_share_certificates.json').read_text())
    out=[]
    for c in payload['certificates']:
        r=analyze(c);out.append(r)
        print(json.dumps({k:v for k,v in r.items() if k not in ('third_slopes_by_label','nontrivial_components','tie_events')}),flush=True)
    Path(__file__).with_name('third_components.json').write_text(json.dumps(out, separators=(',', ':'), sort_keys=True)+'\n')
if __name__=='__main__':main()
