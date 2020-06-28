from distutils.core import setup
from Cython.Build import cythonize
import os

setup(
    name="blubb",
    ext_modules=cythonize("test_cy_easy.pyx", language_level=3),
    build_dir="../../build"
)
