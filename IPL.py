# very basic cricket game
from random import *
import time

teams = ['Mumbai Indians',
        'Chennai Super Kings',
        'Sunrisers Hyderabad',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Rajasthan Royals',
        'Royal Challengers Bangalore']

points = [0, 1, 2, 3, 4, 6]
max_overs = 20.0
overs = 0.0
runs = 0

def play():
    p = randint(0,5)
    return points[p]

def get_points():
    p = randint(0,3)
    return points[p]

def accumulate(total):
    global runs
    runs += total

def clear_runs():
    global runs
    runs = 0
def clear_overs():
    global overs
    overs = 0.0

team_one = randint(0,6)
team_two = randint(0,6)

print(teams[team_one], " vs ", teams[team_two])



# make this a gameplay method

def gameplay():
    global overs
    while(overs < (max_overs - 0.4)):
        this_over = []
        if(round(overs % 1, 2) == 0.6):
            overs +=.4
        if(round(overs,2).is_integer()):
            print("starting over ", round(overs))
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(2)
        print("end of over", this_over)
        time.sleep(1.5)
        print("1's:", this_over.count(1), "|", "2's:", this_over.count(2), "|",  "3's:", this_over.count(3), "|", "4's:", this_over.count(4), "|", "6's:", this_over.count(6))
        total = sum(this_over)
        print("total runs", total)
        accumulate(total)
        time.sleep(1.3)

gameplay()
team_one_results = runs
print("Team one! ", team_one_results)

print("Team two begins ...")
clear_runs()
clear_overs()
# time.sleep(1)
gameplay()
team_two_results = runs
print("Team two! ", team_two_results)


for x in range(8):
    time.sleep(1)
    print("# Loading final  results....")


print(teams[team_one] , " " , team_one_results, teams[team_two] , " " , team_two_results)

if(team_one_results < team_two_results):
    print(teams[team_two], "wins the match!")
elif(team_one_results > team_two_results):
    print(teams[team_one], "wins the match!")
else:
    print("After a hard fought match, both teams have tied!")


# record match into a log file
log_file = "cricket_matches.txt"
# open(filename, a for append)
log = open(log_file, 'a')
log.write("%s - %d - %s - %d \n" % (teams[team_one], team_one_results, teams[team_two], team_two_results))
log.close()
