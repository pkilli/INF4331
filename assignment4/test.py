from matplotlib.pyplot import imshow, show

import mandelbrot_3
import mandelbrot_2
import mandelbrot_1

print("timing various versions of computing")
print('____________________________________')

mandelbrot_data_cython, time_cython = mandelbrot_3.mandelbrot(-2,2.,-2,2,1000,1000,500)
mandelbrot_data_numpy, time_numpy 	= mandelbrot_2.mandelbrot(-2,2.,-2,2,1000,1000,500)
#mandelbrot_data_python, time_python = mandelbrot_1.mandelbrot(-2,2.,-2,2,1000,1000,50)

print("cython mandelbrot: {}".format(time_cython))
print("numpy mandelbrot: {}".format(time_numpy))
#print("python mandelbrot: {}".format(time_python))

