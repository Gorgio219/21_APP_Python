from distutils.core import setup, Extension
from Cython.Build import cythonize
# python3 setup.py build_ext --inplace
extensions = [Extension('matrix', ["multiply.pyx"])]
setup(name="matrix", ext_modules=cythonize("multiply.pyx"))
