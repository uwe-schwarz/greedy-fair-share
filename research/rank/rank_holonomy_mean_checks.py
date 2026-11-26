"""Off-mean checks for every lower tie in cyclotomic residual-pair cases."""
from pathlib import Path
import json,argparse
from _support import REPO_ROOT
from structure_certificates import discover,tie_groups

def run(n):
 start,phases,_=discover(n,cap=600000);ties=[]
 for t,(x,y,slope) in enumerate(phases):
  for group in tie_groups(x,y,slope):
   ties.append({'phase':t,'slots':group,'normalized_load':x[group[0]],'all_player_load_sum':sum(x),'scaled_distance_from_mean':n*x[group[0]]-sum(x)})
 return {'n':n,'start_blocks':start,'period_blocks':len(phases),'all_tie_phases_off_mean':all(q['scaled_distance_from_mean']!=0 for q in ties),'tie_phases':ties}
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('players',nargs='*',type=int,default=[4,8,14]);parser.add_argument('--output',default=str(Path(__file__).with_name('rank_holonomy_cyclotomic_mean_checks.json')));a=parser.parse_args()
 rows=[run(n) for n in a.players]
 Path(a.output).write_text(json.dumps(rows,indent=2)+'\n')
 for r in rows:print(json.dumps({k:v for k,v in r.items() if k!='tie_phases'}))
