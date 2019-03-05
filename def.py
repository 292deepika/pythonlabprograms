#calling one function from other
def func5(a,b):
	print("Hii other function")
	c=a+b
	return c

def func6():
	print("hello, I am going to call other function")
	s = func5(4,8)
	print("addition is",s)
func6()	