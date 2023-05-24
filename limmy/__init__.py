import sys
if sys.version_info < (3, 3):
    raise SystemExit("Invalid Python version. limmy requires Python 3.3 or greater.")

from limmy.protocol import *
from limmy.VESC import *
