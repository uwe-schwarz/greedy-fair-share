"""Exact slopes and cuts in certified third-moment comparison networks."""
import json,sys
from pathlib import Path
from collections import defaultdict
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from fair_share_verify import BlockDynamics
cs=json.loads((ROOT / 'fair_share_certificates.json').read_text())['certificates']
third={c['n']:c for c in json.loads((ROOT / 'research/third_components.json').read_text())}
out=[]
for c in cs:
 n=c['n'];dyn=BlockDynamics(n);init=[tuple(r) for r in c['initial']];rows=init;states=[];profiles=[]
 for order in c['cycle']:
  states.append(rows)
  pp=sorted((r[0],r[1]) for r in rows);aa,bb=pp[0]
  profiles.append(tuple((a-aa,b-bb) for a,b in pp))
  rows=dyn.advance(rows,order)
 slopes4=[r[2]-i[2] for i,r in zip(init,rows)]
 slopes3=[r[1]-i[1] for i,r in zip(init,rows)]
 size=len(c['cycle'])
 periods=[p for p in range(1,size+1) if size%p==0 and all(profiles[t]==profiles[(t+p)%size] for t in range(size))]
 comps=[]
 for cc in third[n]['nontrivial_components']:
  groups=defaultdict(list)
  for i in cc:groups[slopes4[i]].append(i)
  comps.append({'labels':cc,'fourth_drift_classes':[{'slope':k,'labels':v} for k,v in sorted(groups.items())]})
 rec={'n':n,'labelled_period_blocks':size,'unlabelled_lower_period_blocks':periods[0] if periods else None,'third_slopes':slopes3,'fourth_slopes':slopes4,'components':comps}
 out.append(rec)
 print(json.dumps(rec),flush=True)
Path(__file__).with_name('network8_slope_probe.json').write_text(json.dumps(out,indent=2)+'\n')
