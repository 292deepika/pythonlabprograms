class test:
	Rollno = 0
	def myfunc():
		print("Hiii! I am member of the class")
	def roll (self,k):
		self.rollno = k
		print("hii, I am",self.rollno)


o = test()
o.roll(101)
o1= test()
o1roll(102)
print(o.rollno)
print(o1.rollno)