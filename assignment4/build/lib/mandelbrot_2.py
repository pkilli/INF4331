#!/user/bin/env python3
"""Python script which chooses some rectangle in the complex plane,
colors each complex number c if it is in the Mandelbrot set, and otherwise color it according
to how many times you need to apply f_c to 0 to get above 2, and saves the coloring as
an image."""
import numpy
from matplotlib.pyplot import imshow, show, savefig
import time


def mandelbrot(xmin, xmax, ymin, ymax,Nx,Ny, max_escape_time = 30, plot_filename=None, user_action = None) :
	m = Ny # Height of plot
	n = Nx # Width of plot
	values_real = numpy.linspace(xmin, xmax, n).reshape((n,1))
	values_imag = numpy.linspace(ymin, ymax, m).reshape((1,m))
	c = values_real + values_imag*1j
	f_c = c
	iterations = numpy.ones(c.shape)*max_escape_time
	t0 = time.clock()
	for i in range(max_escape_time):
		f_c = f_c * f_c + c
		divergent = f_c * numpy.conj(f_c) > 2**2
		divergent = divergent & (iterations == max_escape_time)
		iterations[divergent] = i
		if(user_action is not None):
			if i == 1:
				user_action(iterations, max_escape_time)
			
	
	if plot_filename is not None:
		from matplotlib.pyplot import imshow, show, savefig
		imshow(iterations, cmap='inferno')
		savefig(plot_filename + '.png')
		show()
	cpu_time = time.clock()-t0
	return iterations, cpu_time


if "__name__" == "__main__":   
	mandelbrot_data, time = mandelbrot(-2,2.,-2,2,1000,1000,500)
