"""Does exact rank-potential forcing remain a coboundary after one reduction?

Targeted obstruction check on the already studied N=8 network. The frozen
checkpoint files are only imported and are not modified.
"""
from collections import defaultdict,deque
from math import comb
from pathlib import Path
import json
from _support import REPO_ROOT
from structure_certificates import discover
from rank_holonomy_compact import analyze,routing

def probe(n):
 start,phases,_=discover(n,cap=600000);P=len(phases);base=analyze(n,phases,include_potentials=True);out=[]
 for c in base['components']:
  slots=c['slots'];s=len(slots);wires=list(range(n));rank_hist={i:[0]*n for i in slots};tot=[0]*n
  nodes=[];H={};ranks=[];paths=[]
  for t,(x,y,sl) in enumerate(phases):
   rr=[r for r,i in enumerate(wires) if i in rank_hist];ranks.append(rr)
   for r in rr:
    i=wires[r];node=t*n+r;nodes.append(node)
    H[node]=[c['phase0_rank_potentials'][i][k]+s*rank_hist[i][k]-tot[k] for k in range(n)]
   paths.append(list(wires))
   for r in rr:
    rank_hist[wires[r]][r]+=1;tot[r]+=1
   wires=[wires[r] for r in routing(n,x,y,sl)]
  graph={}
  for t,(x,y,sl) in enumerate(phases):
   nt=(t+1)%P;xx,yy,ss=phases[nt]
   target=defaultdict(list)
   for r in ranks[nt]:target[(xx[r],yy[r]+(ss[r] if nt==0 else 0),ss[r])].append(nt*n+r)
   raw=[x[r]+comb(n-r,2) for r in range(n)];lo=min(raw)
   for r in ranks[t]:graph[t*n+r]=target[(raw[r]-lo,y[r]+x[r],sl[r])]
  iterations=[];current=H
  for depth in range(1,7):
   costs={}
   for t,rr in enumerate(ranks):
    total=[sum(current[t*n+r][k] for r in rr) for k in range(n)]
    for r in rr:costs[t*n+r]=[s*current[t*n+r][k]-total[k] for k in range(n)]
   pot={nodes[0]:[0]*n};queue=deque([nodes[0]]);witness=None
   while queue:
    u=queue.popleft()
    for v in graph[u]:
     proposed=[a+b for a,b in zip(pot[u],costs[u])]
     if v not in pot:pot[v]=proposed;queue.append(v)
     else:
      delta=[a-b for a,b in zip(proposed,pot[v])]
      if any(delta) and witness is None:
       coeffs=[sum(delta[r]*(comb(2*n-r,k)+comb(r+1,k)) for r in range(n)) for k in range(2*n+1)]
       witness={'edge':[u,v],'rank_polynomial_vector':delta,'first_nonzero_germ_coefficient':next((k,a) for k,a in enumerate(coeffs) if a)}
   assert len(pot)==len(nodes)
   iterations.append({'potential_integration':depth,'is_coboundary':witness is None,'first_defect':witness})
   if witness:break
   current=pot
  out.append({'slots':slots,'size':s,'iterations':iterations})
 return {'n':n,'start_blocks':start,'period_blocks':P,'components':out}
if __name__=='__main__':
 r=probe(8);print(json.dumps(r));Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
