# very basic cricket game
from random import *
import time

teams = ['Mumbai Indians', 'Delhi Capitals', 'Chennai Super Kings', 'Sunrisers Hyderabad', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Rajasthan Royals', 'Royal Challengers Bangalore']

points = [0, 1, 2, 3, 4, 6, 'W']
max_overs = 5.0
overs = 0.0
runs = 0
wickets = 0

def play():
    p = randint(0,6)
    return points[p]

def get_points():
    p = randint(0,3)
    return points[p]

def accumulateRuns(total):
    global runs
    runs += total

def accumulateWickets(wicket):
    global wickets
    wickets += wicket
    # if(wickets >= 1):
    #     print("game over")
    # else:
    #     wickets += wicket

def clear_runs():
    global runs
    runs = 0

def clear_wickets():
    global wickets
    wickets = 0

def clear_overs():
    global overs
    overs = 0.0

def save_match(team1, team1Results, team2, team2Results):
    # record match into a log file
    log_file = "cricket_matches.txt"
    # open(filename, a for append)
    log = open(log_file, 'a')
    log.write("%s - %d - %s - %d \n" % (team1, team1Results, team2, team2Results))
    log.close()


# Random Team Selection
team_one = randint(0,6)
team_two = randint(0,6)

print(teams[team_one] + " vs " + teams[team_two])

# Start Match
def gameplay():
    global overs
    while(overs < (max_overs - 0.4)):
        this_over = []
        if(round(overs % 1, 2) == 0.6):
            overs +=.4
        if(round(overs,2).is_integer()):
            print("starting over ")
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print(round(overs,2))
        this_over.append(play())
        overs += 0.1
        time.sleep(1)
        print("" + str(this_over))
        time.sleep(1.5)
        print("1's: " + str(this_over.count(1)) + "| 2's: " + str(this_over.count(2)) + " | 3's: " + str(this_over.count(3)) + " | 4's: " + str(this_over.count(4)) + " | 6's: " + str(this_over.count(6)) + " | W's: " + str(this_over.count("W")))
        # total = sum(this_over)
        total = 0
        wicketsThisOver = 0
        for x in this_over:
            if(x == 'W'):
                total += 0
                wicketsThisOver += 1
            else:
                total += x

        accumulateRuns(total)
        accumulateWickets(wicketsThisOver)

# Main Method
def start_match():
    print(teams[team_one] + " starting to bat.")

    gameplay()

    team_one_results = runs
    print(teams[team_one] + " " + str(team_one_results) + "-" + str(wickets))

    print(teams[team_two] + " starting to bat.")

    clear_runs()
    clear_wickets()
    clear_overs()

    gameplay()

    team_two_results = runs

    print(teams[team_two] + " " + str(team_two_results) + "-" + str(wickets))

    print(teams[team_one] + " " + str(team_one_results)+ " " + teams[team_two] + " " + str(team_two_results))

    if(team_one_results < team_two_results):
        print(teams[team_two] + " win the match!")
    elif(team_one_results > team_two_results):
        print(teams[team_one] + " win the match!")
    else:
        print("After a hard fought match, both teams have tied!")

    # Save game output to 'cricket_matches.txt'
    save_match(teams[team_one], team_one_results, teams[team_two], team_two_results)


#Start match
start_match()