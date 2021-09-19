This package is meant to illustrate:
1) importing a module (`.py` file) in a subdirectory from another subdirectory by modifying the path
2) vs. running that same module as a *package* module as a script (using `-m` flag)

Notes
* `packaging` is the top-level directory outside the `pack` package. `pack` is a valid Python package that includes two subpackages `dir1` and `dir2`.
* The `__init__.py` files tell Python that `pack`, `dir1`, and `dir2` can have modules that are part of a package.
* The `if` block in `pack/dir1/dir1_mod1.py` detects whether the module is being run as part of a package or not.

### Directory structure
```bash
$ pwd
/packaging

$ tree
.
├── ReadMe.md
└── pack
    ├── __init__.py
    ├── dir1
    │   ├── __init__.py
    │   └── dir1_mod1.py
    └── dir2
        ├── __init__.py
        └── dir2_mod1.py

3 directories, 6 files.
```

### Python file contents
```python
# pack/dir1/dir1_mod1.py 
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
    from pack.dir2 import dir2_mod1
else:
    # get absolute path to parent directory of this file
    _abspath = os.path.abspath(Path(os.path.dirname(__file__)).parent)

    # add parent to path
    sys.path.insert(0, _abspath)
    from dir2 import dir2_mod1

print('dir2_mod1.x: ', dir2_mod1.x)
print()

print('dir2_mod1.d:')
pprint(dir2_mod1.d)
```

```python
# pack/dir2/dir2_mod1.py
x = "hello from dir2_mod1.py"

d = {
    '__file__': __file__,
    '__name__': __name__,
    '__package__': __package__,
    }
```

## Executing from different contexts

Run module and import by modifying path.

```bash
$ python pack/dir1/dir1_mod1.py

dir1_mod1.d:
{'__file__': 'pack/dir1/dir1_mod1.py',
 '__name__': '__main__',
 '__package__': None}

running as module after modifying path
dir2_mod1.x:  hello from dir2_mod1.py

dir2_mod1.d:
{'__file__': '/Users/pzuradzki/code/packaging/pack/dir2/dir2_mod1.py',
 '__name__': 'dir2.dir2_mod1',
 '__package__': 'dir2'}
```

Run module as script via `-m` flag. Module can import from other subpackages.

```bash
$ python -m pack.dir1.dir1_mod1

dir1_mod1.d:
{'__file__': '/Users/pzuradzki/code/packaging/pack/dir1/dir1_mod1.py',
 '__name__': '__main__',
 '__package__': 'pack.dir1'}

running as package module
dir2_mod1.x:  hello from dir2_mod1.py

dir2_mod1.d:
{'__file__': '/Users/pzuradzki/code/packaging/pack/dir2/dir2_mod1.py',
 '__name__': 'pack.dir2.dir2_mod1',
 '__package__': 'pack.dir2'}
```