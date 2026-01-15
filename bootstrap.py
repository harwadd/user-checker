# bootstrap.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

# add the /src in the sys.path if not already present
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
