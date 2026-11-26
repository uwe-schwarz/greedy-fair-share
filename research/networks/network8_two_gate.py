"""Derive two-gate scalar and full-germ maps for N=8 and N=12."""
from math import comb,gcd
from pathlib import Path
import json,sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics
cs={c['n']:c for c in json.loads((ROOT / 'fair_share_certificates.json').read_text())['certificates']}

def advance(row,rank,B):
 return [sum(comb(B,k-j)*row[j] for j in range(k+1))+comb(B-rank,k)+comb(rank+1,k) for k in range(len(row))]
def path(row,ranks,B):
 for r in ranks:row=advance(row,r,B)
 return row

def derive(n,t0,t1,t2,labels):
 c=cs[n];B=2*n;dyn=BlockDynamics(n);states=[];rows=[tuple(r) for r in c['initial']]
 for o in c['cycle']:
  states.append(rows);rows=dyn.advance(rows,o)
 A,Blabel,C=labels
 initial=states[t0];o=c['cycle'][t0]
 assert o.index(A)<o.index(Blabel)
 assert initial[A][:2]==initial[Blabel][:2]
 initial_lower=[0,0,initial[C][0]-initial[A][0],initial[C][1]-initial[A][1],0]
 first={k:[c['cycle'][t].index(i) for t in range(t0,t1)] for k,i in [('A',A),('B',Blabel),('C',C)]}
 row1={k:path(([0]*5 if k!='C' else initial_lower),pp,B) for k,pp in first.items()}
 assert row1['B'][:4]==row1['C'][:4]
 J=row1['C'][4]-row1['B'][4]
 order1=c['cycle'][t1]
 assert order1.index(A) not in [order1.index(Blabel),order1.index(C)]
 lo,hi=sorted([Blabel,C],key=lambda i:order1.index(i))
 second={k:[c['cycle'][t].index(i) for t in range(t1,t2)] for k,i in [('O',A),('Min',lo),('Max',hi)]}
 ref=path(row1['A'],second['O'],B)
 out=path(row1['B'],second['Min'],B)
 pair=path(row1['B'],second['Max'],B)
 assert [u-v for u,v in zip(pair[:4],ref[:4])]==[0]*4
 assert [u-v for u,v in zip(out[:4],ref[:4])]==initial_lower[:4]
 P=ref[4]-pair[4];Q=ref[4]-out[4]-J
 a,b,zz=initial[A][2],initial[Blabel][2],initial[C][2]+J
 shift=a;a-=shift;b-=shift;zz-=shift
 def polynomial(pp):
  exps=[]
  for t,r in enumerate(pp):exps.extend([(len(pp)-1-t)*B+B-r,(len(pp)-1-t)*B+r+1])
  return sorted(exps)
 return {'n':n,'initial_phase':t0,'first_gap_blocks':t1-t0,'second_gap_blocks':t2-t1,'period_blocks':t2-t0,'labels_A_B_C':labels,'outside_lower_difference':initial_lower[:4],'outside_fourth_shift_J':J,'fourth_P':P,'fourth_Q':Q,'twice_Q_minus_P':2*Q-P,'gcd_P_Q':gcd(P,Q),'initial_a_b_z':[a,b,zz],'initial_residues':[v%gcd(P,Q) for v in [a,b,zz]],'first_paths':first,'second_paths':second,'first_polynomial_exponents':{k:polynomial(v) for k,v in first.items()},'second_polynomial_exponents':{k:polynomial(v) for k,v in second.items()}}
if __name__=='__main__':
 out=[derive(8,1,11,17,[1,0,6]),derive(12,0,15,72,[10,7,11])]
 Path(__file__).with_name('network8_two_gate.json').write_text(json.dumps(out,indent=2)+'\n')
 for q in out:print(json.dumps({k:v for k,v in q.items() if not ('paths' in k or 'exponents' in k)}))
