
def func1(a,b,c):
	if (a>=b) and (a>=c):
		return a
	if (b>=a) and (b>=c):
		return b
	if (c>=a) and (c>=b):
		return c


v = func1(4,7,2)
print(v)