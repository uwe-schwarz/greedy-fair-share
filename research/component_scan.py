"""Search exact isolated binary components; no heuristic tie choices."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from math import comb
import sys, json, time
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics


def base_cycle(n, cap=100000):
    w=[comb(n-r,2) for r in range(n)]
    state=(0,)*n;seen={};states=[]
    while state not in seen:
        if len(states)>=cap:raise RuntimeError('base cap')
        seen[state]=len(states);states.append(state)
        raw=sorted(a+b for a,b in zip(state,w));lo=raw[0]
        state=tuple(v-lo for v in raw)
    mu=seen[state]
    return mu,states[mu:],w


def transport(n):
    mu,cycle,w=base_cycle(n);p=len(cycle);parent=list(range(n*p))
    def find(x):
        while x!=parent[x]:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b:parent[b]=a
    for t,x in enumerate(cycle):
        raw=[a+b for a,b in zip(x,w)];lo=min(raw)
        dest={}
        for s,val in enumerate(cycle[(t+1)%p]):dest.setdefault(val,[]).append(s)
        for r,val in enumerate(raw):
            ss=dest[val-lo];a=t*n+r
            for s in ss:union(a,((t+1)%p)*n+s)
    sizes=defaultdict(int)
    for r in range(n):sizes[find(r)]+=1
    wanted={k for k,size in sizes.items() if size==2}
    comps={k:[[] for _ in range(p)] for k in wanted}
    for t in range(p):
        for r in range(n):
            k=find(t*n+r)
            if k in wanted:comps[k][t].append(r)
    binaries=[]
    for ranks in comps.values():
        assert all(len(rs)==2 for rs in ranks)
        ties=[t for t,rs in enumerate(ranks) if cycle[t][rs[0]]==cycle[t][rs[1]]]
        if ties:binaries.append({'ranks':ranks,'ties':ties})
    return mu,cycle,w,binaries,sorted(sizes.values())


def paths_for(cycle,w,ranks,ties):
    p=len(cycle);paths=[]
    for phase in ties:
        a,b=ranks[phase];path=[]
        for elapsed in range(p):
            t=(phase+elapsed)%p;path.append((a,b));nt=(t+1)%p
            raw=[x+v for x,v in zip(cycle[t],w)];lo=min(raw)
            va,vb=raw[a]-lo,raw[b]-lo
            if va==vb:break
            aa=[s for s in ranks[nt] if cycle[nt][s]==va]
            bb=[s for s in ranks[nt] if cycle[nt][s]==vb]
            assert len(aa)==len(bb)==1
            a,b=aa[0],bb[0]
        else:raise AssertionError('no return tie')
        paths.append(path)
    return paths


def forcing(n,path,degree=4):
    b=2*n;h=[0]*(degree+1);bc=[comb(b,j) for j in range(degree+1)]
    for a,c in path:
        h=[sum(bc[k-j]*h[j] for j in range(k+1))
           +comb(b-c,k)+comb(c+1,k)-comb(b-a,k)-comb(a+1,k)
           for k in range(degree+1)]
    return h


def scan(n):
    mu,cycle,w,comps,sizes=transport(n);p=len(cycle)
    row={'n':n,'mu':mu,'p':p,'component_sizes':sizes,'binary':[]}
    if not comps:return row
    phases=sorted({c['ties'][0] for c in comps});targets={mu+s for s in phases}
    dyn=BlockDynamics(n);rows=[(0,0,0)]*n; snapshots={}
    for block in range(max(targets)+1):
        order=sorted(range(n),key=lambda i:(rows[i],i))
        if block and any(rows[a]==rows[b] for a,b in zip(order,order[1:])):
            row['prefix_degree4_tie_block']=block
            return row
        if block in targets:snapshots[block]=(rows,order)
        rows=dyn.advance(rows,order)
    for c in comps:
        paths=paths_for(cycle,w,c['ranks'],c['ties']);phase=c['ties'][0]
        entry={'ranks0':c['ranks'][0],'ties':len(c['ties']),'first_phase':phase}
        if any(path!=paths[0] for path in paths):
            entry['constant_forcing']=False;row['binary'].append(entry);continue
        path=paths[0];h=forcing(n,path);L=2*n*len(path)
        initial,order=snapshots[mu+phase];a,b=[order[r] for r in c['ranks'][phase]]
        d=[y-x for x,y in zip(initial[a],initial[b])]
        entry.update({'constant_forcing':True,'return_blocks':len(path),'labels':[a,b],'D234':d,'H01234':h})
        assert d[0]==0 and h[:3]==[0,0,0]
        if h[3]>=0 or d[1]<0:
            entry['unexpected']=True
        elif d[1]%(-h[3]):
            entry['deciding_degree']=3
        else:
            k=d[1]//(-h[3])
            # d3 is a+kh3. d4 increment per return is L*d3+h4.
            d4=d[2]+L*(k*d[1]+h[3]*k*(k-1)//2)+k*h[4]
            step=-L*h[3]
            entry.update({'third_zero_after':k,'third_zero_block':mu+phase+k*len(path),'D4_at_zero':d4,'fourth_step':step,'fourth_residue':d4%step,'deciding_degree':4 if d4%step else '5+'})
        row['binary'].append(entry)
    return row


def main():
    low=int(sys.argv[1]) if len(sys.argv)>1 else 25
    high=int(sys.argv[2]) if len(sys.argv)>2 else 259
    out=Path(sys.argv[3]) if len(sys.argv)>3 else Path(__file__).with_name('component_scan.jsonl')
    start=time.monotonic()
    with out.open('w') as f:
        for n in range(low,high+1):
            r=scan(n);f.write(json.dumps(r)+'\n');f.flush()
            interesting=[b for b in r['binary'] if b.get('deciding_degree') in (4,'5+')]
            if interesting or 'prefix_degree4_tie_block' in r:
                print(json.dumps({'n':n,'interesting':interesting,'prefix_tie':r.get('prefix_degree4_tie_block')}),flush=True)
            if n%25==0:print(json.dumps({'progress':n,'seconds':round(time.monotonic()-start,1)}),flush=True)
    print(json.dumps({'done':high,'seconds':round(time.monotonic()-start,1)}),flush=True)
if __name__=='__main__':main()
