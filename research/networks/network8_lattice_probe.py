"""Static integer charges in periodic lower-moment comparison networks.

For one persistent third-moment component use an actual periodic reference
wire. Its moment-2 and moment-3 differences make the fourth coordinate an
integer additive edge transport. A directed spanning tree supplies vertex
potentials; the gcd of edge defects is an invariant charge modulus.
"""
from pathlib import Path
from collections import deque,defaultdict
from math import comb,gcd
import json,sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics


def analyze(c,component):
 n=c['n'];B=2*n;dyn=BlockDynamics(n);T=len(c['cycle']);m=len(component)
 ref=component[0];initial=[tuple(row) for row in c['initial']];rows=initial
 states=[];weights=[];keys=[]
 for t,order in enumerate(c['cycle']):
  states.append(rows)
  rank={p:r for r,p in enumerate(order)}
  u0,v0,z0=rows[ref];rw=dyn.weights[rank[ref]][2]
  weights.append([B*(rows[i][1]-v0)+comb(B,2)*(rows[i][0]-u0)+dyn.weights[rank[i]][2]-rw for i in component])
  keys.append([(rows[i][0]-u0,rows[i][1]-v0) for i in component])
  rows=dyn.advance(rows,order)
 finalkeys=[(rows[i][0]-rows[ref][0],rows[i][1]-rows[ref][1]) for i in component]
 assert finalkeys==keys[0],(n,component,'lower component is not periodic')
 # Every actual label path is a period-T cycle. Equal next lower keys are
 # all allowable destinations of each incoming wire.
 groups=[]
 for kk in keys:
  d=defaultdict(list)
  for i,key in enumerate(kk):d[key].append(i)
  groups.append(d)
 def neighbours(v):
  t,i=divmod(v,m);nt=(t+1)%T
  return [nt*m+j for j in groups[nt][keys[nt][i]]]
 potential=[None]*(T*m);potential[0]=0;q=deque([0])
 while q:
  v=q.popleft();t,i=divmod(v,m)
  for w in neighbours(v):
   if potential[w] is None:
    potential[w]=potential[v]+weights[t][i];q.append(w)
 assert all(x is not None for x in potential),'comparison component not strongly connected'
 g=0;edges=0
 for v in range(T*m):
  t,i=divmod(v,m)
  for w in neighbours(v):
   edges+=1;g=gcd(g,potential[v]+weights[t][i]-potential[w])
 charges=[initial[p][2]-initial[ref][2]-potential[i] for i,p in enumerate(component)]
 if g:charges=[z%g for z in charges]
 collisions=[[component[i],component[j]] for i in range(m) for j in range(i+1,m) if charges[i]==charges[j]]
 # Every comparator's incoming coordinates share the same potential modulo g.
 comparator_checks=0
 for t,groups_t in enumerate(groups):
  for group in groups_t.values():
   for i in group[1:]:
    defect=potential[t*m+i]-potential[t*m+group[0]]
    assert defect%g==0 if g else defect==0
    comparator_checks+=1
 return {'n':n,'component':component,'reference':ref,'period_blocks':T,'vertices':T*m,'edges':edges,'modulus':g,'charges':charges,'collision_pairs':collisions,'distinct_charges':not collisions,'comparator_checks':comparator_checks}


def main():
 cs=json.loads((ROOT / 'fair_share_certificates.json').read_text())['certificates']
 third={c['n']:c for c in json.loads((ROOT / 'research/third_components.json').read_text())}
 out=[]
 for c in cs:
  for comp in third[c['n']]['nontrivial_components']:
   r=analyze(c,comp);out.append(r);print(json.dumps(r),flush=True)
 Path(__file__).with_name('network8_lattice_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
