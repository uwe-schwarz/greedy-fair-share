"""Independent compact rank-count holonomy checks on exact lower regimes.

A deterministic wire routing contracts phase paths. At tied lower slots,
wire potential differences equal differences of their accumulated costs.
At the period boundary, endpoints are attached to phase-zero slots. We
solve these vector constraints by a plain graph BFS, independently of the
potential-union implementation used for fourth charges.

Only lower-regime discovery is imported from the root's script.
"""
from collections import defaultdict,deque
from pathlib import Path
from math import comb
import argparse,json,time
from _support import REPO_ROOT
from structure_certificates import discover


def ties(x,y,slope):
 groups=defaultdict(list)
 for r,key in enumerate(zip(x,y,slope)):groups[key].append(r)
 return [g for g in groups.values() if len(g)>1]

def routing(n,x,y,slope,v=None):
 if v is None:v=[comb(n-r,2) for r in range(n)]
 return sorted(range(n),key=lambda r:(x[r]+v[r],y[r]+x[r],slope[r],r))

def analyze(n,phases,v=None,include_potentials=False):
 p=len(phases);wires=list(range(n));par=list(range(n))
 def find(a):
  while par[a]!=a:par[a]=par[par[a]];a=par[a]
  return a
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:par[b]=a
 for x,y,slope in phases:
  for group in ties(x,y,slope):
   for r in group[1:]:union(wires[group[0]],wires[r])
  wires=[wires[r] for r in routing(n,x,y,slope,v)]
 for rank,wire in enumerate(wires):union(wire,rank)
 components=defaultdict(list)
 for i in range(n):components[find(i)].append(i)
 component={i:find(i) for i in range(n)}
 size={r:len(g) for r,g in components.items()}
 hist=[[0]*n for _ in range(n)];totals={r:[0]*n for r in components}
 xhist=[0]*n;xtotals={r:0 for r in components}
 graph=[[] for _ in range(n)];wires=list(range(n));constraint_count=0
 def constrain(a,b,delta,xdelta,where):
  nonlocal constraint_count
  assert component[a]==component[b]
  graph[a].append((b,delta,xdelta,where))
  graph[b].append((a,[-x for x in delta],-xdelta,where))
  constraint_count+=1
 for phase,(x,y,slope) in enumerate(phases):
  for group in ties(x,y,slope):
   a=wires[group[0]];s=size[component[a]]
   for rank in group[1:]:
    b=wires[rank]
    constrain(a,b,[s*(u-v) for u,v in zip(hist[a],hist[b])],s*(xhist[a]-xhist[b]),{'kind':'tie','phase':phase,'slots':[group[0],rank]})
  for rank,wire in enumerate(wires):
   root=component[wire];hist[wire][rank]+=1;totals[root][rank]+=1
   xhist[wire]+=x[rank];xtotals[root]+=x[rank]
  wires=[wires[r] for r in routing(n,x,y,slope,v)]
 for rank,wire in enumerate(wires):
  root=component[wire];s=size[root]
  constrain(wire,rank,[s*u-v for u,v in zip(hist[wire],totals[root])],s*xhist[wire]-xtotals[root],{'kind':'wrap','phase':p,'slots':[wire,rank]})
 out=[]
 for root,slots in components.items():
  if len(slots)==1:continue
  h={slots[0]:[0]*n};hx={slots[0]:0};queue=deque([slots[0]])
  defects=[];xdefects=[];checked=0
  while queue:
   a=queue.popleft()
   for b,delta,xdelta,where in graph[a]:
    proposed=[u+v for u,v in zip(h[a],delta)];px=hx[a]+xdelta
    if b not in h:h[b]=proposed;hx[b]=px;queue.append(b)
    else:
     checked+=1
     defect=[u-v for u,v in zip(proposed,h[b])]
     if any(defect):
      if len(defects)<5:defects.append({'from_wire':a,'to_wire':b,'where':where,'rank_count_defect':defect})
     if px!=hx[b] and len(xdefects)<5:xdefects.append({'where':where,'defect':px-hx[b]})
  assert set(h)==set(slots)
  out.append({'slots':slots,'size':len(slots),'rank_count_holonomy_zero':not defects,'x_holonomy_zero':not xdefects,'first_rank_defects':defects,'first_x_defects':xdefects,'closed_constraints_checked':checked,'centered_rank_totals':totals[root]})
  if include_potentials:out[-1]['phase0_rank_potentials']=h
 return {'period_blocks':p,'constraint_count':constraint_count,'components':out,'all_rank_count_holonomy_zero':all(c['rank_count_holonomy_zero'] for c in out),'all_x_holonomy_zero':all(c['x_holonomy_zero'] for c in out)}

def false_start():
 # Reconstruct the physical control locally, avoiding a dependency on
 # the exploratory false-start scanners.
 n=4;v=[comb(n-r,2) for r in range(n)]
 prefix=[[0,2,3,1],[2,3,0,1],[1,0,3,2],[3,0,1,2]]
 xx=yy=[0]*n
 for order in prefix:
  rank=[0]*n
  for r,i in enumerate(order):rank[i]=r
  rawy=[yy[i]+xx[i] for i in range(n)];lo=min(rawy);yy=[a-lo for a in rawy]
  rawx=[xx[i]+v[rank[i]] for i in range(n)];lo=min(rawx);xx=[a-lo for a in rawx]
 state=tuple(sorted(zip(xx,yy)));seen={};states=[]
 while state not in seen:
  assert len(states)<5000,'control cycle cap'
  seen[state]=len(states);states.append(state)
  raw=[(x+v[r],y+x) for r,(x,y) in enumerate(state)]
  lx=min(x for x,y in raw);ly=min(y for x,y in raw)
  state=tuple(sorted((x-lx,y-ly) for x,y in raw))
 mu=seen[state];states=states[mu:]
 # Common y normalization does not change any centered cost or tie.
 phases=[(tuple(x for x,y in st),tuple(y for x,y in st),(0,)*n) for st in states]
 r={'n':4,'kind':'realizable_noncanonical_prefix','prescribed_orders':prefix,'lower_regime_start_blocks':len(prefix)+mu}
 r.update(analyze(4,phases));return r


def main():
 parser=argparse.ArgumentParser();parser.add_argument('players',type=int,nargs='*',default=[25,30,32,36,48,60]);parser.add_argument('--cap',type=int,default=600000);parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'));a=parser.parse_args()
 if any(n<2 for n in a.players) or a.cap<1:parser.error('Player counts must be at least 2 and the cap positive')
 records=[]
 r=false_start();records.append(r);print(json.dumps(r),flush=True)
 for n in a.players:
  began=time.monotonic();start,phases,meta=discover(n,cap=a.cap)
  r={'n':n,'kind':'canonical','lower_regime_start_blocks':start,**meta};r.update(analyze(n,phases));r['elapsed_seconds']=round(time.monotonic()-began,3)
  records.append(r);print(json.dumps(r),flush=True)
  a.output.write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__':main()
