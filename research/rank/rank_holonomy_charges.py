"""Exact cyclotomic rank signatures on established comparison networks."""
from collections import defaultdict
from pathlib import Path
import json,sys
from rank_holonomy_compact import analyze
from _support import REPO_ROOT
from structure_certificates import discover
from fair_share_verify import BlockDynamics

def prime_power_divisors(B):
 out=[];m=B;p=2
 while p*p<=m:
  if m%p==0:
   power=p
   while m%p==0:out.append((p,power));m//=p;power*=p
  p+=1
 if m>1:out.append((m,m))
 return out

def remainder(coeff,divisor):
 c=list(coeff)
 while c and c[-1]==0:c.pop()
 while len(c)>=len(divisor):
  d=len(c)-len(divisor);a=c[-1]
  for j,b in enumerate(divisor):c[d+j]-=a*b
  while c and c[-1]==0:c.pop()
 return tuple(c+[0]*(len(divisor)-1-len(c)))

def run(n):
 start,phases,meta=discover(n,cap=600000);r=analyze(n,phases,include_potentials=True)
 dyn=BlockDynamics(n);rows=[(0,0,0)]*n;hist=[[0]*n for i in range(n)]
 for t in range(start):
  order=sorted(range(n),key=lambda i:(rows[i],i))
  assert t==0 or all(rows[a]!=rows[b] for a,b in zip(order,order[1:]))
  for rank,i in enumerate(order):hist[i][rank]+=1
  rows=dyn.advance(rows,order)
 order=sorted(range(n),key=lambda i:(rows[i],i));B=2*n
 x,y,_=phases[0]
 for rank in range(n):
  assert rows[order[rank]][0]-rows[order[0]][0]==2*(x[rank]-x[0])
  assert rows[order[rank]][1]-rows[order[0]][1]==(B-1)*(x[rank]-x[0])+2*B*(y[rank]-y[0])
 moduli=[]
 for p,d in prime_power_divisors(B):
  phi=[0]*(d-d//p+1)
  for j in range(p):phi[j*(d//p)]=1
  moduli.append((d,phi))
 basis=[]
 for rank in range(n):
  poly=[0]*(B+1);poly[B-rank]+=1;poly[rank+1]+=1
  basis.append([remainder(poly,phi) for d,phi in moduli])
 out=[]
 for c in r['components']:
  assert c['rank_count_holonomy_zero']
  slots=c['slots'];s=len(slots);total=[sum(hist[order[t]][j] for t in slots) for j in range(n)]
  charge={order[t]:[s*hist[order[t]][j]-total[j]-c['phase0_rank_potentials'][t][j] for j in range(n)] for t in slots}
  assert all(sum(q)==0 for q in charge.values())
  rankclasses=defaultdict(list);cycloclasses=defaultdict(list)
  for label,q in charge.items():
   rankclasses[tuple(q)].append(label)
   signature=[]
   for k,(d,phi) in enumerate(moduli):signature.extend(sum(q[j]*basis[j][k][ell] for j in range(n)) for ell in range(len(phi)-1))
   cycloclasses[tuple(signature)].append(label)
  out.append({'size':s,'labels':[order[t] for t in slots],'equal_rank_charge_classes':sorted(rankclasses.values(),key=lambda a:(-len(a),a)),'equal_cyclotomic_charge_classes':sorted(cycloclasses.values(),key=lambda a:(-len(a),a)),'rank_charges':charge})
 return {'n':n,'start_blocks':start,'period_blocks':len(phases),'prime_power_orders':[d for d,phi in moduli],'components':out}
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('players',nargs='*',type=int,default=[4,8,12,14,30,60])
 parser.add_argument('--output',default=str(Path(__file__).with_name('rank_holonomy_cyclotomic_checks.json')))
 args=parser.parse_args();out=[]
 for n in args.players:
  r=run(n);out.append(r);print(json.dumps({**r,'components':[{k:v for k,v in c.items() if k!='rank_charges'} for c in r['components']]}),flush=True)
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
