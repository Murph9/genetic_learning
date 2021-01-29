import importlib
import glob
import os

def _create_fuzz():
    return 

print('Removing old fuzz files')
files = glob.glob('.\\fuzz\\*')
for f in (x for x in files if not x.endswith("__")):
    print(f"removing {f}")
    os.remove(f)
print('Done')

with open('.\\fuzz\\test.py', 'w') as file:
    file.write("""
def func():
    return 'yo'
""")
print('created file .\\fuzz\\test.py')
print('----- running file')

fuzz = importlib.import_module('fuzz.test')
print(fuzz.func())
