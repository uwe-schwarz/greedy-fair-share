# Rank-count experiments and exact separation criteria

Date: 2026-11-26. All scripts in this directory use Python's arbitrary-precision integers and the standard library. Run ordinary Python, without `-O`, from the repository root.

The mathematical statements and their scope are in [RANK_RIGIDITY.md](../RANK_RIGIDITY.md), [RANK_RIGIDITY_CHECKS.md](../RANK_RIGIDITY_CHECKS.md), and [CYCLOTOMIC_SEPARATION.md](../CYCLOTOMIC_SEPARATION.md). Rank rigidity is an exact condition on a finite graph; its validity for every canonical player count remains a conjecture.

## Reproduce the canonical graph checks

```sh
# Expanded phase/rank implementation, including the N=2 control
python3 research/rank/network_rank_rigidity.py 2 3 4 8 12 14 24

# Independent contracted implementation, including the realizable N=4 false start
python3 research/rank/rank_holonomy_compact.py 25 30 32 36 48 60 --output compact_actual.json

# Exact prefix reconstruction and cyclotomic signature classes
python3 research/rank/rank_holonomy_charges.py --output signatures_actual.json

# All original lower tie phases for the remaining pair cases
python3 research/rank/rank_holonomy_mean_checks.py --output means_actual.json
```

The compact and expanded implementations solve the vector-potential problem independently. Both import the separately certified lower profile from [structure_certificates.py](../structure_certificates.py). Signature calculations additionally reconstruct the actual greedy prefix through degree four, reject any unresolved prefix comparison, and compare the entry moments with the discovered lower profile.

The recorded compact report contains elapsed-time fields, which can change between runs. Its mathematical fields must reproduce exactly. The other signature and mean reports contain no timing fields.

## Controls that disprove stronger conjectures

The compact script always includes the realizable altered N=4 prefix. Its nonzero rank-count defect shows why canonical starting history matters.

The strictly convex N=6 counterexample can be reproduced directly:

```sh
PYTHONPATH=research/rank python3 - <<'PY'
import json
from network_convex_probe import test
print(json.dumps(test((27,18,10,5,2,0)), indent=2))
PY
```

The full exploratory search is preserved as `network_convex_probe.py` and `network_convex_probe.jsonl`. The independent compact result is `rank_holonomy_convex_control.json`.

To reproduce the narrow quadratic probe in `network_quadratic_probe.jsonl`:

```sh
PYTHONPATH=research/rank python3 - <<'PY'
import json
from network_convex_probe import test
for n in range(6,11):
    for a in range(4):
        v=tuple(k*k+a*k for k in range(n-1,-1,-1))
        print(json.dumps(test(v)))
PY
```

Twenty positive cases do not establish a quadratic-family theorem. The controls concern extensions of a proposed invariant; they are not counterexamples to eventual periodicity of the original fair-share sequences.
