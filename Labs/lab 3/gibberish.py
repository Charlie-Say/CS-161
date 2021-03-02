from PIL import Image
import random
from random import randint

image_open = Image.open('lake.jpg')
pix = image_open.load()

width = 1374  # pixels
heigth = 483  # pixels

x_coord = random.randint(0, width)
y_coord = random.randint(0, heigth)


blue = (163, 193, 255)

count = 0
n = 1000
for i in range(n):
    rand_point = pix[x_coord, y_coord]
    if rand_point == blue:
        count += 1

print(count)

