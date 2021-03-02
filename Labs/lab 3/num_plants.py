'''
put in stuff docstring
'''


import math


side_length = float(input("How many feet do you want for the garden: "))
plant_space = float(input("How much spacing in between plants: "))


garden_area = side_length * side_length

# circle area
cir_r = 1/4 * side_length

cir_area = (math.pi * (cir_r ** 2))
semi_cir_area = cir_area / 2
total_cir_area = semi_cir_area * 6

stone_area = garden_area - total_cir_area

# plant area - each plant takes up this much spacing in the total area of the circle
plant_area = plant_space ** 2


plant_num_semi = semi_cir_area // plant_area
plant_num_cir = plant_num_semi * 2
plant_num_total = plant_num_cir * 3




print("Plants for each semicircle garden: ", plant_num_semi)
print("Plants for each circle garden: ", plant_num_cir)
print("Total plants for garden: ", plant_num_total)
print("stone area = ", stone_area)