# Welcome to basketball simulation
# Developed by michaeljivan
# Program wil run a game between nba teams and top 3 players
# to 21 points then log it into a separate text file after a game completes.

# import random lib for number generation
from random import *
import time

# Home/Away teams
home = ""
away = ""

# NBA Teams
teams = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets',
	'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers',
	'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 
	'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 
	'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 
	'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 
	'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder',
	'Orlando Magic', 'Philadelphia Sixers', 'Phoenix Suns', 
	'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 
	'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
	
# Top 3 players from each team
# guards 0,1 bigs 2 in array
hawks = ['Dennis Schroder', 'Tyler Dorsey', 'John Collins']
celtics = ['Kyrie Irving', 'Jason Tatum', 'Al Horford']
nets = ['Dangelo Russell', 'Jeremey Lin', 'Rondae Hollis-Jefferson']
hornets = ['Kemba Walker', 'Nicolas Batum', 'Dwight Howard']
bulls = ['Zach LaVine', 'Kris Dunn', 'Robin Lopez']
cavaliers = ['JR Smith', 'LeBronJames', 'Kevin Love']
mavericks = ['Harrison Barnes', 'Wesley Matthews', 'Dirk Nowitzki']
nuggets = ['Nikola Jokic', 'Jamal Murray', 'Kenneth Faried']
pistons = ['Reggie Jackson', 'Stanley Johnson', 'Andre Drummond']
warriors = ['Steph Curry', 'Kevin Durant', 'Klay Thompson']
rockets = ['Chris Paul', 'James Harden', 'Clint Capela']
pacers = ['Victor Oladipo', 'Darren Collison', 'Lance Stephenson']
clippers = ['Lou Williams', 'Blake Griffin', 'DeAndre Jordan']
lakers = ['Kobe Bryant', 'Kyle Kuzma', 'Julius Randle']
grizzlies = ['Mike Conley', 'Tony Allen', 'Marc Gasol']
heat = ['Dwyane Wade','Hassan Whiteside','Udonis Haslem']
bucks = ['Eric Bledsoe', 'Jabari Parker', 'Giannis Anteokounmpo']
timberwolves = ['Andrew Wiggins', 'Jimmy Butler', 'Karl-Anthony Towns']
pelicans = ['Rajon Rondo', 'Jrue Holiday', 'Anthony Davis']
knicks = ['Frank Ntilikina', 'Enes Kanter', 'Kristaps Porzingis']
thunder = ['Russell Westbrook', 'Paul George', 'Steven Adams']
magic = ['Elfrid Payton', 'Evan Fournier', 'Nikola Vucevic']
sixers = ['Ben Simmons', 'J. J. Redick', 'Joel Embiid']
suns = ['Devin Booker', 'Josh Jackson', 'Marquese Chriss']
blazers = ['Damian Lillard', 'CJ McCollum', 'Jusuf Nurkic']
kings = ['DeAaron Fox', 'Buddy Hield', 'Willie Cauley-Stein']
spurs = ['Tony Parker', 'Manu Ginobili', 'LaMarcus Aldridge']
raptors = ['Kyle Lowry', 'DeMar DeRozen', 'Jonas Valanciunas']
jazz = ['Ricky Rubio', 'Donovan Mitchell', 'Rudy Gobert']
wizards = ['John Wall', 'Bradley Beal', 'Marcin Gortat']

# Select Random Teams
a = randint(0,29)
b = randint(0,29)
if(a!=b):	
	home = teams[a]
	away = teams[b]
else:
		print("Restart Program.")

print("                ")
print("Welcome everybody, tonight's matchup will be the")
print("  ", away,"vs", home)


print("                ")

# Game Rules
# The match will go up to 21, Standard take out system
# Tipoff starts at half court
# Free Throw implementation not needed - optional
# top 3 players from each of the 30 nba teams will be available

# 5 variations of each scoring opportunity to keep the simulation a bit more interesting
def miss(player):
	outcome = randint(0,4)
	if(outcome == 0):
		print(player, " trys to lay it up inside, won't go.")
	if(outcome == 1):
		print(player, " puts it up from way downtown, misses.")
	if(outcome == 2):
		print(player, " strikes and misses!")
	if(outcome == 3):
		print(player, " tries the jumper won't go!")
	if(outcome == 4):
		print(player, " trys one up, can't get it to fall!")

def hit(player):
	outcome = randint(0,4)
	if(outcome == 0):
		print(player, " takes a 15 footer gets it to go!")
	if(outcome == 1):
		print(player, " hits the jumper!")
	if(outcome == 2):
		print(player, " slams it down!")
	if(outcome == 3):
		print(player, " drills the shot!")
	if(outcome == 4):
		print(player, " takes a quick jumper gets it to fall.")

def bang(player):
	outcome = randint(0,4)
	if(outcome == 0):
		print(player, " for three, BANG!!")
	if(outcome == 1):
		print(player, " tries the triple, got it!")
	if(outcome == 2):
		print(player, " throws up a prayer, BANG!")
	if(outcome == 3):
		print(player, " goes for three, nails it!")
	if(outcome == 4):
		print(player, " for THREE, GETS IT TO FALL!")

def home_scores(player):
	global home_score
	outcome = randint(0,2)
	if(outcome == 0):
		miss(player)
	if(outcome == 1):
		hit(player)
		home_score += 2
	if(outcome == 2):
		bang(player)
		home_score += 3	
		
def away_scores(player):
	global away_score 
	outcome = randint(0,2)
	if(outcome == 0):
		miss(player)
	if(outcome == 1):
		hit(player)
		away_score += 2
	if(outcome == 2):
		bang(player)
		away_score += 3	

def home_team_get_players(team, index):
	if(team == 'Atlanta Hawks'):
		home_scores(hawks[index])
	if(team == 'Boston Celtics'):
		home_scores(celtics[index])
	if(team == 'Brooklyn Nets'):
		home_scores(nets[index])
	if(team == 'Charlotte Hornets'):
		home_scores(hornets[index])
	if(team == 'Chicago Bulls'):
		home_scores(bulls[index])
	if(team == 'Cleveland Cavaliers'):
		home_scores(cavaliers[index])
	if(team == 'Dallas Mavericks'):
		home_scores(mavericks[index])
	if(team == 'Denver Nuggets'):
		home_scores(nuggets[index])
	if(team == 'Detroit Pistons'): 
		home_scores(pistons[index])
	if(team == 'Golden State Warriors'):
		home_scores(warriors[index])
	if(team == 'Houston Rockets'): 
		home_scores(rockets[index])
	if(team == 'Indiana Pacers'):
		home_scores(pacers[index])
	if(team == 'Los Angeles Clippers'): 
		home_scores(clippers[index])
	if(team == 'Los Angeles Lakers'): 
		home_scores(lakers[index])
	if(team == 'Memphis Grizzlies'): 
		home_scores(grizzlies[index])
	if(team == 'Miami Heat'):
		home_scores(heat[index])
	if(team == 'Milwaukee Bucks'):
		home_scores(bucks[index])
	if(team == 'Minnesota Timberwolves'):
		home_scores(timberwolves[index])
	if(team == 'New Orleans Pelicans'):
		home_scores(pelicans[index])
	if(team == 'New York Knicks'):
		home_scores(knicks[index])
	if(team == 'Oklahoma City Thunder'):
		home_scores(thunder[index])
	if(team == 'Orlando Magic'):
		home_scores(magic[index])
	if(team == 'Philadelphia Sixers'):
		home_scores(sixers[index])
	if(team == 'Phoenix Suns'):
		home_scores(suns[index])
	if(team == 'Portland Trail Blazers'):
		home_scores(blazers[index])
	if(team == 'Sacramento Kings'):
		home_scores(kings[index])
	if(team == 'San Antonio Spurs'):
		home_scores(spurs[index])
	if(team == 'Toronto Raptors'):
		home_scores(raptors[index])
	if(team == 'Utah Jazz'):
		home_scores(jazz[index])
	if(team == 'Washington Wizards'):
		home_scores(wizards[index])
	
def away_team_get_players(team, index):
	if(team == 'Atlanta Hawks'):
		away_scores(hawks[index])
	if(team == 'Boston Celtics'):
		away_scores(celtics[index])
	if(team == 'Brooklyn Nets'):
		away_scores(nets[index])
	if(team == 'Charlotte Hornets'):
		away_scores(hornets[index])
	if(team == 'Chicago Bulls'):
		away_scores(bulls[index])
	if(team == 'Cleveland Cavaliers'):
		away_scores(cavaliers[index])
	if(team == 'Dallas Mavericks'):
		away_scores(mavericks[index])
	if(team == 'Denver Nuggets'):
		away_scores(nuggets[index])
	if(team == 'Detroit Pistons'): 
		away_scores(pistons[index])
	if(team == 'Golden State Warriors'):
		away_scores(warriors[index])
	if(team == 'Houston Rockets'): 
		away_scores(rockets[index])
	if(team == 'Indiana Pacers'):
		away_scores(pacers[index])
	if(team == 'Los Angeles Clippers'): 
		away_scores(clippers[index])
	if(team == 'Los Angeles Lakers'): 
		away_scores(lakers[index])
	if(team == 'Memphis Grizzlies'): 
		away_scores(grizzlies[index])
	if(team == 'Miami Heat'):
		away_scores(heat[index])
	if(team == 'Milwaukee Bucks'):
		away_scores(bucks[index])
	if(team == 'Minnesota Timberwolves'):
		away_scores(timberwolves[index])
	if(team == 'New Orleans Pelicans'):
		away_scores(pelicans[index])
	if(team == 'New York Knicks'):
		away_scores(knicks[index])
	if(team == 'Oklahoma City Thunder'):
		away_scores(thunder[index])
	if(team == 'Orlando Magic'):
		away_scores(magic[index])
	if(team == 'Philadelphia Sixers'):
		away_scores(sixers[index])
	if(team == 'Phoenix Suns'):
		away_scores(suns[index])
	if(team == 'Portland Trail Blazers'):
		away_scores(blazers[index])
	if(team == 'Sacramento Kings'):
		away_scores(kings[index])
	if(team == 'San Antonio Spurs'):
		away_scores(spurs[index])
	if(team == 'Toronto Raptors'):
		away_scores(raptors[index])
	if(team == 'Utah Jazz'):
		away_scores(jazz[index])
	if(team == 'Washington Wizards'):
		away_scores(wizards[index])
		
# Matchup array
matchup = [home, away]

#Game started bool value
game_started = True

# Scores
home_score = 0
away_score = 0

time.sleep(2.1)

def tipoff():
	result = randint(0,1)
	player_index = randint(0,2)
	
	print(matchup[result], "got the tip")
	
	if(matchup[result] == home):
		home_team_get_players(home, player_index)
	else:
		away_team_get_players(away, player_index)

tipoff()

#while(game_started and (home_score < 21 or away_score < 21)):	
while(game_started and not(home_score or away_score) >21):
	player_index = randint(0,2)
	time.sleep(2.5)
	home_team_get_players(home, player_index)
	time.sleep(2.5)
	away_team_get_players(away, player_index)

print("The game has ended, please check the Bball_sim_log.txt file to see the results!")
#end of game log all the statistics nicely formatted
filename = "Bball_sim_log.txt"
log = open(filename, 'a')

log.write("%s %d\t %s %d \n" % (away, away_score, home, home_score))
log.close()