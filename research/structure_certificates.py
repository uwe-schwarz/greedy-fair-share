"""Discover exact lower affine regimes, then test centered fourth-moment charges.

The lower numerical evolution is independent of higher tie choices. A proposed
affine regime is checked for all repetitions by slope inequalities. The true
labelled prefix is reconstructed separately and rejects unresolved degree-four
ties. No fixed positive hit probability or floating point is used.
"""
from collections import defaultdict, deque
from pathlib import Path
from math import comb, gcd
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics

if not __debug__:
    raise SystemExit('Exact checks require ordinary Python; do not use -O.')


def weights(n):
    return [comb(n-r, 2) for r in range(n)]


def step(x, y, v):
    rawx = [a+b for a,b in zip(x,v)]
    low = min(rawx)
    rawy = [a+b for a,b in zip(y,x)]
    order = sorted(range(len(x)), key=lambda i:(rawx[i],rawy[i],i))
    return tuple(rawx[i]-low for i in order), tuple(rawy[i] for i in order)


def base_cycle(n, cap=100000):
    v=weights(n); x=(0,)*n; seen={}; states=[]
    while x not in seen:
        if len(states)>=cap: raise ValueError('base cap')
        seen[x]=len(states); states.append(x)
        raw=sorted(a+b for a,b in zip(x,v)); x=tuple(a-raw[0] for a in raw)
    return seen[x], len(states)-seen[x]


def certify(x, y, slope, period, v):
    x0,y0,s0=x,y,slope
    phases=[]
    for _ in range(period):
        for i in range(len(x)-1):
            if x[i]==x[i+1] and (y[i]>y[i+1] or slope[i]>slope[i+1]):
                return None
        phases.append((x,y,slope))
        rawx=[a+b for a,b in zip(x,v)]; low=min(rawx)
        rawy=[a+b for a,b in zip(y,x)]
        order=sorted(range(len(x)),key=lambda i:(rawx[i],rawy[i],slope[i],i))
        for a,b in zip(order,order[1:]):
            if rawx[a]==rawx[b] and slope[a]>slope[b]: return None
        x=tuple(rawx[i]-low for i in order)
        y=tuple(rawy[i] for i in order)
        slope=tuple(slope[i] for i in order)
    if x!=x0 or y!=tuple(a+b for a,b in zip(y0,s0)) or slope!=s0:
        return None
    # Move one whole cycle forward, removing every accidental initial tie
    # between unequal affine profiles while keeping persistent ties.
    return [(x,tuple(a+b for a,b in zip(y,s)),s) for x,y,s in phases]


def discover(n, cap=200000, max_macros=10000):
    mu,p=base_cycle(n); v=weights(n)
    x=y=(0,)*n
    for _ in range(mu): x,y=step(x,y,v)
    xbase=x; ys=[y]; differences={}
    for j in range(min(max_macros, max(0,(cap-mu)//p))):
        for _ in range(p): x,y=step(x,y,v)
        assert x==xbase
        ys.append(y)
        change=tuple(b-a for a,b in zip(ys[j],y))
        if change in differences:
            i=differences[change]
            delta=tuple(b-a for a,b in zip(ys[i],ys[j]))
            phases=certify(xbase,ys[i],delta,(j-i)*p,v)
            if phases:
                return mu+j*p, phases, {'base_preperiod':mu,'base_period':p,
                                        'discovery_blocks':mu+(j+1)*p}
        differences[change]=j
    raise ValueError(f'lower discovery cap at {mu+(len(ys)-1)*p}')


def charge_test_expanded(n, start, phases):
    p=len(phases); v=weights(n); B=2*n; C=2*B*B; D=2*B*(B-1)
    size=n*p; edges=[[] for _ in range(size)]
    undirected=[[] for _ in range(size)]
    for j,(x,y,slope) in enumerate(phases):
        nxt=(j+1)%p; tx,ty,ts=phases[nxt]
        target=defaultdict(list)
        for r in range(n):
            key=(tx[r],ty[r]+(ts[r] if nxt==0 else 0),ts[r])
            target[key].append(nxt*n+r)
        rawx=[a+b for a,b in zip(x,v)]; low=min(rawx)
        for r in range(n):
            dest=target[(rawx[r]-low,y[r]+x[r],slope[r])]
            assert dest
            u=j*n+r
            for w in dest:
                edges[u].append(w); undirected[u].append(w); undirected[w].append(u)
    seen=set(); components=[]
    for root in range(size):
        if root in seen: continue
        seen.add(root); queue=[root]; nodes=[]
        for u in queue:
            nodes.append(u)
            for w in undirected[u]:
                if w not in seen: seen.add(w); queue.append(w)
        byphase=[[] for _ in range(p)]
        for u in nodes: byphase[u//n].append(u%n)
        s=len(byphase[0]); assert all(len(row)==s for row in byphase)
        if s==1: continue
        assert len({phases[u//n][2][u%n] for u in nodes})==1
        costs={}
        for j,ranks in enumerate(byphase):
            x,y,_=phases[j]
            raw={r:C*y[r]+D*x[r]+comb(B-r,4)+comb(r+1,4) for r in ranks}
            total=sum(raw.values())
            costs.update({j*n+r:s*raw[r]-total for r in ranks})
        h={root:0}; queue=deque([root]); g=0
        while queue:
            u=queue.popleft()
            for w in edges[u]:
                proposed=h[u]+costs[u]
                if w not in h: h[w]=proposed; queue.append(w)
                else: g=gcd(g,proposed-h[w])
        assert set(h)==set(nodes), 'component must be strongly connected'
        for u in nodes:
            for w in edges[u]: assert (h[u]+costs[u]-h[w])%g==0 if g else h[u]+costs[u]==h[w]
        components.append({'slots':byphase[0],'size':s,'modulus':g,'potentials':{r:h[r] for r in byphase[0]},
                           'aggregate_divisor':gcd(s,g),'potential_sum':sum(h[r] for r in byphase[0])})
    # Canonical labelled prefix, separate from unlabelled lower discovery.
    dyn=BlockDynamics(n); rows=[(0,0,0)]*n
    for m in range(start):
        order=sorted(range(n),key=lambda i:(rows[i],i))
        if m and any(rows[a]==rows[b] for a,b in zip(order,order[1:])):
            return {'prefix_unresolved_block':m,'components':components}
        rows=dyn.advance(rows,order)
    order=sorted(range(n),key=lambda i:(rows[i],i))
    x,y,_=phases[0]
    for r in range(n):
        for t in (0,):
            assert rows[order[r]][0]-rows[order[t]][0]==2*(x[r]-x[t])
            assert rows[order[r]][1]-rows[order[t]][1]==(B-1)*(x[r]-x[t])+2*B*(y[r]-y[t])
    for c in components:
        slots=c['slots']; s=c['size']; g=c['modulus']
        total=sum(rows[order[r]][2] for r in slots)
        charges={order[r]:s*rows[order[r]][2]-total-c['potentials'][r] for r in slots}
        if g: charges={a:q%g for a,q in charges.items()}
        classes=defaultdict(list)
        for a,q in charges.items(): classes[q].append(a)
        c['charges']=charges
        c['unresolved_charge_classes']=[ls for ls in classes.values() if len(ls)>1]
        c['all_distinct']=len(classes)==s
        c['forced_split_by_aggregate']=c['potential_sum']%c['aggregate_divisor']!=0
    return {'components':components,'all_components_separated':all(c['all_distinct'] for c in components)}


class PotentialUnion:
    """Integer constraints h[b]-h[a]=delta, retaining their cycle gcd."""
    def __init__(self,n):
        self.parent=list(range(n)); self.shift=[0]*n; self.modulus=[0]*n

    def find(self,a):
        if self.parent[a]!=a:
            old=self.parent[a]; self.parent[a]=self.find(old)
            self.shift[a]+=self.shift[old]
        return self.parent[a]

    def constrain(self,a,b,delta):
        ra=self.find(a); rb=self.find(b)
        da,db=self.shift[a],self.shift[b]
        if ra==rb:
            self.modulus[ra]=gcd(self.modulus[ra],delta+da-db)
        else:
            self.parent[rb]=ra; self.shift[rb]=delta+da-db
            self.modulus[ra]=gcd(self.modulus[ra],self.modulus[rb])


def route(x,y,slope,v):
    return sorted(range(len(x)),key=lambda r:(x[r]+v[r],y[r]+x[r],slope[r],r))


def tie_groups(x,y,slope):
    groups=defaultdict(list)
    for r,key in enumerate(zip(x,y,slope)): groups[key].append(r)
    return (rs for rs in groups.values() if len(rs)>1)


def charge_test(n,start,phases):
    """Contract the deterministic wire paths before computing the same gcd.

    A tie joins wire potentials at that phase; the final permutation joins
    each wire endpoint to its phase-zero slot. These constraints retain every
    closed-walk cost of the expanded phase/rank graph.
    """
    B=2*n; C=2*B*B; D=2*B*(B-1); v=weights(n)
    topology=PotentialUnion(n); wires=list(range(n))
    for x,y,slope in phases:
        for group in tie_groups(x,y,slope):
            for r in group[1:]: topology.constrain(wires[group[0]],wires[r],0)
        wires=[wires[r] for r in route(x,y,slope,v)]
    for rank,wire in enumerate(wires): topology.constrain(wire,rank,0)
    groups=defaultdict(list)
    for r in range(n): groups[topology.find(r)].append(r)
    component={r:topology.find(r) for r in range(n)}
    sizes={root:len(rs) for root,rs in groups.items()}
    potential=PotentialUnion(n); integral=[0]*n; wires=list(range(n))
    for x,y,slope in phases:
        for tied in tie_groups(x,y,slope):
            a=wires[tied[0]]
            for rank in tied[1:]:
                b=wires[rank]
                potential.constrain(a,b,integral[a]-integral[b])
        costs=[C*y[r]+D*x[r]+comb(B-r,4)+comb(r+1,4) for r in range(n)]
        totals=defaultdict(int)
        for r,wire in enumerate(wires): totals[component[wire]]+=costs[r]
        for r,wire in enumerate(wires):
            root=component[wire]
            integral[wire]+=sizes[root]*costs[r]-totals[root]
        wires=[wires[r] for r in route(x,y,slope,v)]
    for rank,wire in enumerate(wires): potential.constrain(wire,rank,integral[wire])
    components=[]
    for slots in groups.values():
        if len(slots)==1: continue
        root=potential.find(slots[0]); assert all(potential.find(r)==root for r in slots)
        h={r:potential.shift[r] for r in slots}; g=potential.modulus[root]; s=len(slots)
        components.append({'slots':slots,'size':s,'modulus':g,'potentials':h,
                           'aggregate_divisor':gcd(s,g),'potential_sum':sum(h.values())})
    dyn=BlockDynamics(n); rows=[(0,0,0)]*n
    for m in range(start):
        order=sorted(range(n),key=lambda i:(rows[i],i))
        if m and any(rows[a]==rows[b] for a,b in zip(order,order[1:])):
            return {'prefix_unresolved_block':m,'components':components}
        rows=dyn.advance(rows,order)
    order=sorted(range(n),key=lambda i:(rows[i],i)); x,y,_=phases[0]
    for r in range(n):
        assert rows[order[r]][0]-rows[order[0]][0]==2*(x[r]-x[0])
        assert rows[order[r]][1]-rows[order[0]][1]==(B-1)*(x[r]-x[0])+2*B*(y[r]-y[0])
    for c in components:
        slots=c['slots']; s=c['size']; g=c['modulus']
        total=sum(rows[order[r]][2] for r in slots)
        charges={order[r]:s*rows[order[r]][2]-total-c['potentials'][r] for r in slots}
        if g: charges={a:q%g for a,q in charges.items()}
        classes=defaultdict(list)
        for a,q in charges.items(): classes[q].append(a)
        c['charges']=charges; c['unresolved_charge_classes']=[ls for ls in classes.values() if len(ls)>1]
        c['all_distinct']=len(classes)==s
        c['forced_split_by_aggregate']=c['potential_sum']%c['aggregate_divisor']!=0
    return {'components':components,'all_components_separated':all(c['all_distinct'] for c in components)}


def run(n,cap=200000):
    start,phases,meta=discover(n,cap=cap)
    result={'n':n,'lower_regime_start_blocks':start,'lower_period_blocks':len(phases),**meta}
    result.update(charge_test(n,start,phases))
    canonicalize(result)
    return result


def canonicalize(result):
    """Remove the arbitrary spanning-tree gauge from the printed record."""
    for c in result.get('components',[]):
        c['slots']=sorted(c['slots'])
        h={int(r):v for r,v in c['potentials'].items()}
        q={int(i):v for i,v in c.get('charges',{}).items()}
        shift=h[c['slots'][0]]; g=c['modulus']
        h={r:(v-shift)%g if g else v-shift for r,v in sorted(h.items())}
        q={i:(v+shift)%g if g else v+shift for i,v in sorted(q.items())}
        c['potentials']=h; c['potential_sum']=sum(h.values())
        if q: c['charges']=q
        c['forced_split_by_aggregate']=c['potential_sum']%c['aggregate_divisor']!=0
    result.get('components',[]).sort(key=lambda c:c['slots'][0])
    if 'all_components_separated' in result:
        result['verdict']=('PROVED EVENTUALLY PERIODIC' if result['all_components_separated']
                           else 'INCONCLUSIVE: equal charges remain')
    elif 'prefix_unresolved_block' in result:
        result['verdict']='NOT CERTIFIED: prefix needs higher moments'
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('players',nargs='*',type=int)
    parser.add_argument('--range',dest='player_range',nargs=2,type=int,metavar=('FIRST','LAST'))
    parser.add_argument('--cap',type=int,default=200000)
    args=parser.parse_args()
    if args.players and args.player_range: parser.error('use explicit players or --range')
    if args.cap<=0: parser.error('--cap must be positive')
    if args.player_range and args.player_range[1]<args.player_range[0]: parser.error('LAST must be at least FIRST')
    ns=(list(range(args.player_range[0],args.player_range[1]+1)) if args.player_range
        else args.players or list(range(3,25)))
    if any(n<2 for n in ns): parser.error('every player count must be at least2')
    for n in ns:
        try: r=run(n,cap=args.cap)
        except ValueError as e: r={'n':n,'not_established':str(e)}
        print(json.dumps(r),flush=True)
