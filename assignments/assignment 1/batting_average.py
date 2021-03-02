'''
Progam for batting average for baseball player.

The batting average is calculated as the number of "hits" divided by the number of "at-bats."

Charlie Say
Program Assignment 1
January 16, 2019

prompt user for players name
prompt for hits
prompt for at-bats
display batting average

inputs: name, hits, at-bats, batting average
formula: average = hits/at-bats
variables: hits, at-bats, name
'''


name = input("What is the player's name? ")
hits = int(input("How many hits? "))
bats = int(input("how many at-bats? "))
average = hits/bats

print("{}'s batting average is {:.3f}".format(name, average))