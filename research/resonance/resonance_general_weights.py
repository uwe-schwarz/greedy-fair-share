from itertools import combinations
from math import gcd
import json,time

def analyze(v,cap=10000):
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
  if sz[find(t*n+r)]==2*p:
   return {'v':v,'onset':onset,'period':p,'phase':t,'ranks':[r,r+1],'cycle':cy}
 return False

results=[];counts={};start=time.time()
for n in range(3,8):
 counts[n]=0
 for pos in combinations(range(1,15),n-1):
  v=tuple(reversed(pos))+(0,)
  if gcd(*v)!=1:continue
  counts[n]+=1
  result=analyze(v)
  if result:
   results.append(result); print(json.dumps(result),flush=True)
   if len(results)>=10:break
 if results:break
print(json.dumps({'counts':counts,'seconds':time.time()-start,'found':len(results)}),flush=True)
