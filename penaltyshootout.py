goal = input("pick 0 1 2 3: ")

if(goal == '0'):
	print("Hits the cross bar!")
	input("Press ENTER key to continue...")

if(goal == '1'):
	print("Far Corner, GOOOOOOALLLL!!")
	input("Press ENTER key to continue...")

if(goal == '2'):
	print("GOOOOOOALLLLLLL!!!")
	input("Press any key to continue...")

if(goal == '3'):
	print("off the post!!")
	input("Press any key to continue...")

def start(s):
	print("Lets begin the match")
	list = []
	list.append(s)
	print(list)


start("start")
input("Enter")