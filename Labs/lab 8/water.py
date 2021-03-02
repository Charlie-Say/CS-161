#! /usr/bin/env python3
# # coding=utf-8
'''
write a program to find approximately how much water is in the photo graph

Given a high-resolution computer image of a map of an irregularly shaped
lake with several islands, determine the water surface area.
Assume that the x-y coordinates of every point on the map can be measured.

Charlie Say
Alex Nylund
CS 161 10:00 AM

__PSUEDO__

find width(x) and heigth(y)

generate random x coord
generate random y coord
look at pixel at random x,y
build list of color values
    do math

blue += 1
red += 1
'''


from PIL import Image  # Image module
import random
from random import randint

image_open = Image.open('lake.jpg')  # Import photo from directory
pix = image_open.load()

width = 1370  # pixels
heigth = 480  # pixels

blue = (163, 193, 255)

count = 0
not_blue = 0
n = 100000

for i in range(n):
    x_coord = random.randint(0, width)
    y_coord = random.randint(0, heigth)
    rand_point = pix[x_coord, y_coord]
    if rand_point == blue:
        count += 1
 
    else:
        not_blue += 1
        continue

print(count)
print(not_blue)
percent = (count/n) * 100
print(f"There is {percent:.2f}% of water in the picture")