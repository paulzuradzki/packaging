import sys
import os
from pathlib import Path
from pprint import pprint

d = {
    '__file__': __file__,
    '__name__': __name__,
    '__package__': __package__,
    }

print('dir1_mod1.d:')
pprint(d)
print()

if __package__:
    print("running as package module")
    from pack.dir2 import dir2_mod1
else:
    print("running as module after modifying path")
    # get absolute path to parent directory of this file
    _abspath = os.path.abspath(Path(os.path.dirname(__file__)).parent)

    # add parent to path
    sys.path.insert(0, _abspath)
    from dir2 import dir2_mod1

print('dir2_mod1.x: ', dir2_mod1.x)
print()

print('dir2_mod1.d:')
pprint(dir2_mod1.d)