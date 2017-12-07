""" user interface for mandelbrot set"""
USER_HANDLE = True
def inputs():
	xmin = float(input('xmin: '))
	xmax = float(input('xmax: '))
	ymin = float(input('ymax: '))
	ymax = float(input('ymax: '))
	Nx = int(input('number of x values: '))
	Ny = int(input('number of y values: '))
	max_escape_time = int(input('max_escape_time: '))
	print("do you want a plot?")
	input_2 = input('Y/N: ')
	if(input_2 == 'Y'):
		filename = input('filename of plot: ')
	else:
		filename = None
	return xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time, filename
		



while USER_HANDLE :
	print (">>>>> computing mandelbrot set <<<<<")
	print ("what method do you want to use")
	print ("press 1 for classic python")
	print ("press 2 for vectorised numpy")
	print ("press 3 for cython")
	print ("q to quit")
	print ("press --help for instructions")
	print ("------------------------------------")
	input_1 = input("Give input: " )
	if input_1 == "q":
		USER_HANDLE = False
	elif input_1 == '1':
		import mandelbrot_1
		xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename = inputs()
		mndlbrt, time = mandelbrot_1.mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename)
		print("python mandelbrot: {}".format(time))
		print ("----------------------------------")
	elif input_1 == '2':
		import mandelbrot_2
		xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename = inputs()
		mndlbrt, time = mandelbrot_2.mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename)
		print("numpy mandelbrot: {}".format(time))
		print ("----------------------------------")
	elif input_1 == '3':
		import mandelbrot_3
		xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename = inputs()
		mndlbrt, time = mandelbrot_3.mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,filename)
		print("cython mandelbrot: {}".format(time))
		print ("----------------------------------")
	elif input_1 == 'help':
		print ("There are three different scripts that computes the mandelbrot set.")
		print ("The scripts chooses some rectangle in the complex plane, and if you wish, the numbers that are in the mandelbrot ")
		print ("set can be drawn.")
		
