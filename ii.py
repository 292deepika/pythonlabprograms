class Test:
	h=0

	def __init__(self):
		self.h = 6

	def my_func(self,k):
		print("hii, I am in the class")
		self.h=k
		print(self.h)
o =Test()
print(o.h)
o1 = Test()
print(o1.h)
o.my_func(2)
o1.my_func(4)
o3=Test()
print(o3.h)			