import numpy
import time
cimport numpy 
cpdef mandelbrot(double xmin, double xmax, double ymin, double ymax,int Nx, int Ny, int max_escape_time = 30, plot_filename=None, user_action = None):
	cdef int i
	
	cdef numpy.ndarray[numpy.double_t, ndim=2] values_real
	values_real = numpy.linspace(xmin,xmax,Nx).reshape((Nx,1))
	
	cdef numpy.ndarray[numpy.double_t,ndim=2] values_imag
	values_imag = numpy.linspace(ymin,ymax, Ny).reshape((1,Ny))
	
	cdef numpy.ndarray[numpy.complex_t,ndim=2] c
	c = values_real + values_imag*1j
	
	cdef numpy.ndarray[numpy.complex_t,ndim=2] f_c
	f_c = c
	
	cdef numpy.ndarray[numpy.double_t, ndim = 2] iterations
	iterations = numpy.ones((values_real.shape[0],values_imag.shape[1]))*max_escape_time
	
	t0 = time.clock()
	for k in range(max_escape_time):
		f_c = f_c*f_c + c
		divergence = f_c*numpy.conj(f_c) > 2**2
		divergence = divergence & (iterations == max_escape_time)
		iterations[divergence] = k
		if(user_action is not None):
			if(k == 1):
				user_action(iterations, max_escape_time)
	
	if plot_filename is not None:
		from matplotlib.pyplot import imshow, show, savefig
		print ("chose colour:")
		print(" hot , spectral, gist_rainbow")
		color = input('chose colour: ')
		imshow(iterations, cmap=color)
		savefig(plot_filename + '.png')
		show()
	cpu_time = time.clock() - t0
	return iterations, cpu_time

if "__name__"=="__main__":	
	pass
