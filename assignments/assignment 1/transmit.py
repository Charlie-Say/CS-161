'''
write a program that calcutes how long it takes a photo to reach earths orbit.

Light travels at 186000. The distance between earth and orbit is 34 million miles.

Charlie Say
Program Assignment 1
January 16, 2019

create variables and input values
print string and variables/calculation

variables: seconds, minutes
formula: 340000000/186000
'''


seconds = 34000000/186000
minutes = seconds/60

print("It will take {:.2f} minutes for a photo from Curiosity to reach NASA when Mars is at its closest orbit to Earth.".format(minutes))
