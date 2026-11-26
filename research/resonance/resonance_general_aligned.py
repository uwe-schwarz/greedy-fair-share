from itertools import combinations
from math import gcd
import json,time

def probe(v,cap=10000):
 n=len(v);x=(0,)*n;seen={};orbit=[]
 while x not in seen:
  if len(orbit)>cap:return None
  seen[x]=len(orbit);orbit.append(x)
  raw=sorted(a+b for a,b in zip(x,v));low=raw[0];x=tuple(a-low for a in raw)
 onset=seen[x];cy=orbit[onset:];p=len(cy)
 candidates=[]
 for t,x in enumerate(cy):
  s=sum(x)
  if s%n:continue
  mean=s//n
  for r in range(n-1):
   if x[r]==x[r+1]==mean:candidates.append((t,r))
 if not candidates:return False
 ds=list(range(p*n));sz=[1]*(p*n)
 def find(a):
  while ds[a]!=a:ds[a]=ds[ds[a]];a=ds[a]
  return a
 def join(a,b):
  a=find(a);b=find(b)
  if a!=b:ds[b]=a;sz[a]+=sz[b]
 for t,x in enumerate(cy):
  raw=[a+b for a,b in zip(x,v)];low=min(raw); nxt=cy[(t+1)%p]
  for r in range(n):
   for s in range(n):
    if raw[r]-low==nxt[s]:join(t*n+r,((t+1)%p)*n+s)
 for t,r in candidates:
  if sz[find(t*n+r)]!=2*p:continue
  component=find(t*n+r)
  ranks=[[r for r in range(n) if find(((t+j)%p)*n+r)==component] for j in range(p)]
  pp=next(q for q in range(1,p+1) if p%q==0 and all(ranks[j]==ranks[j%q] for j in range(p)))
  if (onset+t)%pp:continue
  if ranks[1%p]!=[n-r-2,n-r-1]:continue
  valid=True
  for m,cur in enumerate(orbit):
   js=ranks[m%p];ref=cy[(t+m)%p]
   if [n*cur[j]-sum(cur) for j in js]!=[n*ref[j]-sum(ref) for j in js]:valid=False;break
  if valid:return {'v':v,'onset':onset,'period':p,'phase':t,'pairperiod':pp,'ranks':ranks,'cycle':cy}
 return False

if __name__=='__main__':
 results=[];counts={};start=time.time()
 for n in range(3,9):
  counts[n]=0
  for pos in combinations(range(1,19),n-1):
   v=tuple(reversed(pos))+(0,)
   if gcd(*v)!=1:continue
   counts[n]+=1
   result=probe(v)
   if result:
    results.append(result); print(json.dumps(result),flush=True)
    if len(results)>=5:break
  if results:break
 print(json.dumps({'counts':counts,'seconds':time.time()-start,'found':len(results)}),flush=True)
