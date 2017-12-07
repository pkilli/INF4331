from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "mandelbrot",
    ext_modules = cythonize("*.pyx"),
)
