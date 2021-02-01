import ntpath
import os
import sys
import tempfile

FUNC_NAME = 'func'


def _create_func(arg):
    return f"""
def {FUNC_NAME}():
    return 'yo: {arg}'
"""


# creates a temp folder, fills it with python files and runs them all
with tempfile.TemporaryDirectory() as tmp_dir:
    files = []
    for i in range(12):
        with open(f'{tmp_dir}\\{i}.py', 'w') as file:
            file.write(_create_func(i))
            files.append(ntpath.basename(file.name))

    sys.path.append(tmp_dir)
    for f in files:
        mod = __import__(os.path.splitext(f)[0])
        print(getattr(mod, FUNC_NAME)())
