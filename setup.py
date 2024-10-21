from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("mylibrary", ["mylibrary.pyx"]),
]

setup(
    name="mylibrary",
    version="0.1",
    ext_modules=cythonize(extensions),
    zip_safe=False,
)

# Execute python setup.py build_ext --inplace
'''
This will create a compiled file 
(e.g., mylibrary.cpython-39-x86_64-linux-gnu.so on Linux or 
mylibrary.cp39-win_amd64.pyd on Windows).
Import the module in this compiled file in your python application code as follows:
import mylibrary
and use the functions and classes from mylibrary.py. 
The functions and classes need to be exported as API document
For example if you want to use the function add() from mylibrary.py,
you can use the following code:
import mylibrary
mylibrary.add(1, 2)
'''
