"""Graph-modulus probe after arbitrary realizable paired-block prefixes."""
from network8_noncanonical import lower_cycle,component_gcd
from pathlib import Path
import random,json

def arbitrary_prefix(n,orders):
 v=[(n-1-r)*(n-r)//2 for r in range(n)]
 xx=[0]*n;yy=[0]*n
 for order in orders:
  rank=[0]*n
  for r,i in enumerate(order):rank[i]=r
  yy=[yy[i]+xx[i] for i in range(n)];m=min(yy);yy=[v-m for v in yy]
  xx=[xx[i]+v[rank[i]] for i in range(n)];m=min(xx);xx=[v-m for v in xx]
 return list(zip(xx,yy))

def main():
 rng=random.Random(2026112601);results=[];counts={'trials':0,'closed':0,'skipped':0,'nontrivial':0};failure=False
 for n in range(3,13):
  for trial in range(100):
   orders=[]
   for k in range(rng.randrange(1,25)):
    order=list(range(n));rng.shuffle(order);orders.append(order)
   init=arbitrary_prefix(n,orders);counts['trials']+=1
   cyc=lower_cycle(n,init,5000)
   if cyc is None:counts['skipped']+=1;continue
   counts['closed']+=1;mu,states,perms,keys=cyc
   comps=component_gcd(n,states,perms,keys)
   if comps:
    counts['nontrivial']+=len(comps)
    rec={'n':n,'trial':trial,'prefix_blocks':len(orders),'initial':init,'preperiod':mu,'period':len(states),'components':comps}
    results.append(rec)
    if any(not c['divisible_by_8N2'] for c in comps):
     rec['prefix_orders']=orders;rec['cycle_states']=states;rec['cycle_permutations']=perms
     print(json.dumps(rec),flush=True);failure=True;break
  print(json.dumps({'n_completed':n,'counts':counts}),flush=True)
  if failure:break
 Path(__file__).with_name('network8_physical_prefix.json').write_text(json.dumps({'seed':2026112601,'cap':5000,'counts':counts,'failure':failure,'results':results},indent=2)+'\n')
if __name__=='__main__':main()
