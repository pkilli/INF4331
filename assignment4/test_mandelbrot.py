import numpy as np
from mandelbrot_2 import mandelbrot

def test(iterations, max_escape_time):
	""" checking if the region of the plane is entierly inside/ outside of the mandelbrot set
		after first iteration
		"""
	test = iterations - np.ones((iterations.shape[0],iterations.shape[1])) * max_escape_time == 0.0
	if(test.all() == 0.0):
		msg = "all numbers in mandelbrot set"
		print (msg)
	test = iterations - np.ones((iterations.shape[0],iterations.shape[1])) * max_escape_time == float(-max_escape_time)
	if(test.all()):
		msg = "all numbers outside mandelbrot set"
		print (msg)
mandelbrot_data, time = mandelbrot(3,4.,3,4,600,600,500, user_action = test)
mandelbrot_data, time = mandelbrot(-0.5,0.5,-0.5,0.5,600,600,500, user_action = test)


