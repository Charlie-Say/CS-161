import math


side_length = float(input("Enter length of side of garden (feet): "))
plant_space = float(input("Enter spacing between plants (feet): "))
depth_soil = float(input("Enter depth of garden soil (feet): "))
depth_fill = float(input("Enter depth of fill (feet): "))


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


print("Plants for each semicircle garden: ", round(plant_num_semi))
print("Plants for each circle garden: ", round(plant_num_cir))
print("Total plants for garden: ", round(plant_num_total))


##############################################
'''
VOLUME OF SOIL AND FILL
'''

soil_semi = (semi_cir_area * depth_soil) / 27

soil_cir = (soil_semi * 2)

total_soil = (soil_cir * 3)

total_stone = (stone_area * depth_fill) / 27

print("Soil for each semicircle garden: ", round(soil_semi, 1), "cubic yards")
print("Soil for the circle garden: ", round(soil_cir, 1), "cubic yards")
print("Total soil for the garden: ", round(total_soil, 1), "cubic yards")
print("Total fill for the garden: ", round(total_stone, 1), "cubic yards")