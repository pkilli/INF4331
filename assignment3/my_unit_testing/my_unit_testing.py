class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test
    	""" Takes four arguments
    	func is a function to be resolved
    	args/kwargs is the parameters to be put in the function
    	res is wanted result.
    	UnitTest tests the return statement from the function against the wanted result.
    	Returns True if the test is passed, False if i fails.
    	"""
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test
    	try:
    		if self.func(*self.args, **self.kwargs) == self.res:
    			return True
    	
    	except Exception:
    		return False
    		
