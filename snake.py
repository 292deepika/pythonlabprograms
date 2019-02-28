import random

d = 0
p = 0

while True:
	r = input("Press r to roll, q to quit : ")

	if r == 'r':
	 	d = random.randint(1,6)
	 	print("You got :",d)
	 	if d == 6:
	 		print("Congratulations, you can play now.")
	 		break
	 	else:
	 		print("Roll again, till you get 6,")

while True:
	r = input("Press r to roll, q to quit : ")
	if r =='r':
		d = random.randint(1,6)
		print("You got :".d)

		p = p+d
		if p > 100:
			p = p-d
			print("wait till you get", 100-p,"or less.")

		print("Your new position is :",p)

		if p == 100:
				print("You won!")
				exit()
		if p == 8:
			p = 37
			print("Wow, a ladder. Go to",p)
		if p == 12:
			p = 34
			print("Wow, a ladder. Go to",p)
		if p == 40:
			p = 68
			print("Wow, a ladder. Go to",p)
		if p == 52:
			p = 81
			print("Wow, a ladder. Go to",p)
		if p == 76:
		    p = 97
		    print("Wow, a ladder. Go to",p)
		if p == 11:
			p = 2
			print("oh!, snake bite, go to",p)
		if p == 25:
			p = 4
			print("oh!, snake bite, go to",p)
		if p == 38:
			p = 9
			print("oh!, snake bite, go to",p)
		if p == 65:
			p = 46
			print("oh!, snake bite, go to",p)
		if p == 89:
			p = 70
			print("oh!, snake bite, go to",p)
		if p == 93:
			p = 64
			print("oh!, snake bite, go to",p)

	elif r == 'q':
		print("Bye!")
		exit()
	
			
