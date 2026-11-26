"""Probe the observed graph-modulus divisibility on arbitrary integer lower states.

The lower state is (x,y), sorted lexicographically, with minima removed
independently. No claim that a randomized start is a canonical history.
"""
from math import comb,gcd
from collections import deque,defaultdict
from pathlib import Path
import random,json,argparse

def lower_cycle(n,init,cap):
 v=[(n-1-r)*(n-r)//2 for r in range(n)]
 state=tuple(sorted(init));seen={};states=[];perms=[];nextkeys=[]
 for t in range(cap):
  if state in seen:
   k=seen[state];return k,states[k:],perms[k:],nextkeys[k:]
  seen[state]=t;states.append(state)
  raw=[(x+v[r],y+x) for r,(x,y) in enumerate(state)]
  xmin=min(x for x,y in raw);ymin=min(y for x,y in raw)
  keys=[(x-xmin,y-ymin) for x,y in raw]
  order=sorted(range(n),key=lambda i:keys[i]);perm=[0]*n
  for r,i in enumerate(order):perm[i]=r
  perms.append(perm);nextkeys.append(keys)
  state=tuple(keys[i] for i in order)
 return None

def component_gcd(n,states,perms,nextkeys):
 P=len(states);B=2*n;total=P*n
 groups=[]
 for state in states:
  d=defaultdict(list)
  for i,k in enumerate(state):d[k].append(i)
  groups.append(d)
 def dest(t,r):
  return groups[(t+1)%P][nextkeys[t][r]]
 par=list(range(total))
 def find(a):
  while par[a]!=a:par[a]=par[par[a]];a=par[a]
  return a
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:par[b]=a
 for t in range(P):
  for r in range(n):
   for s in dest(t,r):union(t*n+r,((t+1)%P)*n+s)
 cc=defaultdict(list)
 for r in range(n):cc[find(r)].append(r)
 weights=[[2*B*B*y+2*B*(B-1)*x+comb(B-r,4)+comb(r+1,4) for r,(x,y) in enumerate(state)] for state in states]
 out=[]
 for ranks in cc.values():
  if len(ranks)<2:continue
  root=ranks[0];r=root;refs=[]
  for t in range(P*n):
   refs.append(r);r=perms[t%P][r]
   if (t+1)%P==0 and r==root:break
  else:raise AssertionError('reference path did not close')
  L=len(refs);pot={root:0};queue=deque([root]);edges=[]
  while queue:
   u=queue.popleft();t,r=divmod(u,n);nt=(t+1)%L
   cost=weights[t%P][r]-weights[t%P][refs[t]]
   for s in dest(t%P,r):
    w=nt*n+s;edges.append((u,w,cost))
    if w not in pot:pot[w]=pot[u]+cost;queue.append(w)
  g=0
  for u,w,cost in edges:g=gcd(g,pot[u]+cost-pot[w])
  out.append({'ranks':ranks,'reference_period':L,'modulus':g,'divisible_by_8N2':g%(8*n*n)==0,'vertices':len(pot),'edges':len(edges),'initial_potentials':{str(i):pot[i] for i in ranks if i in pot}})
 return out

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--max-n',type=int,default=8);parser.add_argument('--trials',type=int,default=50);parser.add_argument('--cap',type=int,default=5000);a=parser.parse_args()
 rng=random.Random(20261126);results=[];counts={'closed':0,'skipped':0,'nontrivial':0};start=None
 for n in range(2,a.max_n+1):
  for trial in range(a.trials):
   init=[(rng.randrange(0,20),rng.randrange(-20,21)) for i in range(n)]
   cyc=lower_cycle(n,init,a.cap)
   if cyc is None:counts['skipped']+=1;continue
   counts['closed']+=1;mu,states,perms,nextkeys=cyc
   comps=component_gcd(n,states,perms,nextkeys)
   if comps:
    counts['nontrivial']+=len(comps)
    rec={'n':n,'trial':trial,'initial':init,'preperiod':mu,'period':len(states),'components':comps}
    results.append(rec)
    print(json.dumps(rec),flush=True)
    if any(not c['divisible_by_8N2'] for c in comps):
     Path(__file__).with_name('network8_noncanonical.json').write_text(json.dumps({'scope':vars(a),'counts':counts,'results':results},indent=2)+'\n');return
 Path(__file__).with_name('network8_noncanonical.json').write_text(json.dumps({'scope':vars(a),'counts':counts,'results':results},indent=2)+'\n')
 print(json.dumps({'counts':counts}))
if __name__=='__main__':main()
