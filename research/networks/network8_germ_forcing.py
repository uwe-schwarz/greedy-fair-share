"""Exact sparse full-germ forcing for the two-gate examples."""
from pathlib import Path
from math import comb
import json

def add(*terms):
 out={}
 for sign,shift,poly in terms:
  for e,c in poly.items():out[e+shift]=out.get(e+shift,0)+sign*c
 return {e:c for e,c in out.items() if c}
def poly(exps):
 out={}
 for e in exps:out[e]=out.get(e,0)+1
 return out
def binom(n,k):
 return comb(n,k) if n>=0 else (-1)**k*comb(k-n-1,k)
def coeffs(p,d):return [sum(c*binom(e,k) for e,c in p.items()) for k in range(d+1)]
rs=json.loads(Path(__file__).with_name('network8_two_gate.json').read_text());out=[]
for r in rs:
 n=r['n'];s=2*n*r['first_gap_blocks'];t=2*n*r['second_gap_blocks']
 U,V,W=[poly(r['first_polynomial_exponents'][k]) for k in ['A','B','C']]
 E,F,G=[poly(r['second_polynomial_exponents'][k]) for k in ['O','Min','Max']]
 J=add((1,-s,W),(-1,-s,V))
 H=add((1,t,U),(1,0,E))
 P=add((1,0,H),(-1,t,V),(-1,0,G))
 Q=add((1,0,H),(-1,t,V),(-1,0,F),(-1,0,J))
 record={'n':n,'period_turns':s+t,'J_coefficients':coeffs(J,12),'P_coefficients':coeffs(P,12),'Q_coefficients':coeffs(Q,12),'P_sparse':P,'Q_sparse':Q}
 out.append(record)
 print(json.dumps({k:v for k,v in record.items() if 'sparse' not in k}))
Path(__file__).with_name('network8_germ_forcing.json').write_text(json.dumps(out,indent=2)+'\n')
