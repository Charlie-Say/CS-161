from PIL import Image  # Image module
import random
from random import randint

image_open = Image.open('misty.jpg')  # Import photo from directory
pix = image_open.load()
rgb_im = image_open.convert('RGB')

width = 300  # pixels
heigth = 250  # pixels

hair_color = (71, 67, 117)

count = 0
not_blue = 0
n = 100000

# for i in range(n):
#     x_coord = random.randint(1, width)
#     y_coord = random.randint(1, heigth)
#     rand_point = pix[x_coord, y_coord]
#     if rand_point == hair_color:
#         count += 1
 
#     else:
#         not_blue += 1
#         continue

r, g, b = rgb_im.getpixel((75, 50))
print(r, g, b)
percent = (count/n) * 100
print(f"{percent:.2f}% of this picture is booty.")

