import random
l=["r","p","s"]
while True:
	u=input("enter your choice,press n to discontinue")
	if u=='n':
		print("Game over")
		exit()
	c=random.choice(l)
	print("computer chooses",c)
	if u ==c:
		print("tie")
	elif u=='r' and c=='p':
		print("comp wins")
	elif u== 'r'and c=='s':
		print("user wins")
	elif u=='s' and c=='p':
		print("comp wins")
	elif u=='p' and c=='s':
		print("comp wins")
	elif u=='p'and c=='r':
		print("user wins")				

