#python program to generate random 5 day forcast
from random import *

Monday = randint(25,80)
Tuesday = randint(45,90)
Wednesday = randint(70,85)
Thursday = randint(67,99)
Friday = randint(45,104)

print("5-day weather forecast")
print("Monday:\t\t", Monday)
print("Tuesday:\t", Tuesday)
print("Wednesday:\t", Wednesday)
print("Thursday:\t", Thursday)
print("Friday:\t\t", Friday)