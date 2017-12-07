from distutils.core import setup, Extension
import numpy
import os

os.environ['CC'] = 'g++';
setup(name='mandelbrot', version='1.0', ext_modules =[Extension('_mandelbrot_4',
 ['mandelbrot_4.cc', 'mandelbrot_4.i'], include_dirs = [numpy.get_include(),'.'])])
