"""Exact higher-moment probe of the explicit N=4 noncanonical prefix."""
from math import comb
from pathlib import Path
import json
n=4;B=8;degree=12
prefix=[[0,2,3,1],[2,3,0,1],[1,0,3,2],[3,0,1,2]]
weights=[[comb(B-r,k)+comb(r+1,k) for k in range(2,degree+1)] for r in range(n)]
shifts=[[comb(B,k-j) for j in range(2,k+1)] for k in range(2,degree+1)]
rows=[[0]*(degree-1) for i in range(n)]
orders=[];events=[];max_depth=0;unresolved=None
for t in range(20000):
 order=prefix[t] if t<len(prefix) else sorted(range(n),key=lambda i:(rows[i],i))
 if t>=len(prefix):
  for a,b in zip(order,order[1:]):
   d=next((j+2 for j,(u,v) in enumerate(zip(rows[a],rows[b])) if u!=v),None)
   if d is None:unresolved={'block':t,'players':[a,b]};break
   max_depth=max(d,max_depth)
   if d>=5:events.append({'block':t,'players':[a,b],'degree':d,'coefficient_gap':rows[b][d-2]-rows[a][d-2]})
  if unresolved:break
 orders.append(order)
 rank=[0]*n
 for r,i in enumerate(order):rank[i]=r
 nextrows=[]
 for i in range(n):
  nextrows.append([sum(c*z for c,z in zip(shifts[k],rows[i]))+weights[rank[i]][k] for k in range(degree-1)])
 base=nextrows[0]
 rows=[[z-b for z,b in zip(row,base)] for row in nextrows]
result={'n':n,'degree_cap':degree,'blocks_completed':len(orders),'initial_prefix_orders':prefix,'max_decision_degree':max_depth,'deep_events':events,'unresolved':unresolved,'last_orders':orders[-48:]}
Path(__file__).with_name('network8_false_start_depth.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('deep_events','last_orders')}))
print('deep event count',len(events),'first events',events[:20])
