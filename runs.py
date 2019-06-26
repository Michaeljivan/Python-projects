import random
run_types = [1,2,3,4,6]
o = 0.0
score = 0

for i in range(6):
	o += 0.1
	print ("Over " + str(o))
	r = run_types[random.randint(0,4)]
	score += r
	print(r)


print("You scored " + str(score) + " runs!")
