"""RPN calculator
interactive calculator which takes input in Reverse Polish Notation
When a number is input to the calculator, it is pushed to the end of the stack, and when an arithmetic operation(+, *, /) is input, it should pop the last two numbers of the stack, 
compute their sum/product/quotient, and push that to the end of the stack
"""
from math import sqrt, cos, sin
a = True
mylist = []

print ("press q to quit:")

def popNumbers(a, b):
	'deletes numbers being calculated'
	del mylist[a]
	del mylist[b]
	return
	
def function(a):
	"""returns eiter sqrt, sin cos value of the last number in the stack"""
	if a == 'v':
		print (np.sqrt(mylist[-1]))
	elif a == 'sin':
		print (np.sin(mylist[-1]))
	else :
		print (np.cos(mylist[-1]))
	return
	
while True:
	USER_INPUT = input()
	b = USER_INPUT.split()
	
	for i in range(len(b)):
		if b[i] == 'p':
			print (mylist[(len(mylist)-1)])
			
		elif b[i] == '+':
			a = mylist[(len(mylist)-1)] + mylist[(len(mylist)-2)]
			popNumbers((len(mylist)-1), (len(mylist)-2))
			mylist.append(a)
			
		elif b[i] == '*':
			a = mylist[(len(mylist)-1)] * mylist[(len(mylist)-2)]
			popNumbers((len(mylist)-1), (len(mylist)-2))
			mylist.append(a)
			
		elif b[i] == '/':
			a = mylist[(len(mylist)-1)] / mylist[(len(mylist)-2)]
			popNumbers((len(mylist)-1), (len(mylist)-2))
			mylist.append(a)
			
		elif b[i] == 'q':
			continue
		elif b[i] == 'v' or b[i] == 'cos' or b[i] == 'sin':
			function(b[i])
		else:
			mylist.append(int(b[i]))
	
	if USER_INPUT == 'q':
		break
print (mylist)
