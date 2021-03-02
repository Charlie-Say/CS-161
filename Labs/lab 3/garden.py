'''
program will take a user input for the dimensions for a square garden with circles and semi-circle planting areas for flowers.

This program will ask the user for the side length of the garden, plant spacing, the depth of garden soil, and the depth of the garden fill(stone). The program will then give the amount of flowers needed, soil, and stone for a circle and semi-circle garden.

Charlie Say
Alex Nylund
CS 161
10:00 AM


side length = input
depth soil = input
depth fill = input

garden area = side length * side length

# round numbers to whole numbers

calculate circle area = expression
semi circle = circle area / 2
total circle area = semi circle area * 6(this is the total of semi circles)

calculate area of each plant = plant spacing ** 2
calculate area of stone = garden area - total of circle area

plant per semi circle = semi circle area // plant area
plant per full circle = plant number for semi circle * 2
plants total = plant numbers for full circle * 3(number of full circles in the garden)

print statements

##### volume of soil #####
# round down to nearest whole number
soil for semi circle = semi circle area * input_depth / 27(27 ft^3 = 1 yrd^3)
soil for full circle = soil semi circle * 2
soil total = soil full circle * 3
stone/fill total = fill area * input_depth / 27(27 ft^3 = 1 yrd^3)

print statements

'''


import math

def main():
        '''
        this function will take input from user(side length, plant space, depth of soil, depth of fill. calculate the area of the semi circle and full circle.
        calculate the number of plants.
        calculate the volume of the soil and stone needed for the garden.
        '''


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

        # plant area
        plant_area = plant_space ** 2

        # number of plants
        plant_num_semi = semi_cir_area // plant_area
        plant_num_cir = plant_num_semi * 2
        plant_num_total = plant_num_cir * 3


        print("Plants for each semicircle garden: ", round(plant_num_semi))
        print("Plants for each circle garden: ", round(plant_num_cir))
        print("Total plants for garden: ", round(plant_num_total))



        # this will calculate the volume of soil and stone/fill

        soil_semi = (semi_cir_area * depth_soil) / 27

        soil_cir = (soil_semi * 2)

        total_soil = (soil_cir * 3)

        total_stone = (stone_area * depth_fill) / 27

        print("Soil for each semicircle garden: ", round(soil_semi, 1), "cubic yards")
        print("Soil for the circle garden: ", round(soil_cir, 1), "cubic yards")
        print("Total soil for the garden: ", round(total_soil, 1), "cubic yards")
        print("Total fill for the garden: ", round(total_stone, 1), "cubic yards")


main()


#       QUESTIONS

# 1. The program ends and an exception occurs when the user inputs something else other than a number. It also states that it could not convert string to float.

# 2. Inputing a letter or string into the prompt will crash the program. Also inputing zeros for the inputs will cause an Exception: ZeroDivisionError - float divmod(). Can't divide a number by zero when calculating the area of the garden or planting circles.

# 3. Yes, because the outputs are rounding floating numbers. This can give a different output if multiplying the output of plants for a semi-circle by two to get the amount of plants for a full-circle. Also, if the expression to calculate the total plants in a semi circle were using regular division instead of floor division, it would give a floating which could change the output. It's finding a number of plants that has a float number that rounds down, but when multiplied by two, it will be rounded to the next number up.
# example: 3.4 rounds down to 3 (semi circle plants). --- 3.4 * 2 = 6.8 rounds up to 7(full circle plants)
# it depends if the numbers used to find the total amount of plants in the full circle are rounded first or used as a floating number.