class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test
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
    		
""" better_addition function failes when sending in number:times = 0
 sum_computations = [a + b for n in range(num_rechecks)] is not beeing initiated and the function returns 
no value
 """
