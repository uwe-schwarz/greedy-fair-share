"""Locate the repository's exact arithmetic helpers for standalone research scripts."""

from pathlib import Path
import sys

if not __debug__:
    raise SystemExit("Exact checks require ordinary Python; do not use -O.")

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "research"))
