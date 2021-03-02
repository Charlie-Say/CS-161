'''
program that will calculate how many helmets are sold for every bicycle.

The program will prompt the user for how many bikes were sold for the month and its output will be the amount of helmets sold. 1 helmet is sold for every 5 bikes. The program will also out the total expected revenue while each helmet costs $50 and each bike costs $250.

Charlie Say
Pito Libby
CS 161
10:00 AM

----- PSUEDO -----

input("how many bikes sell?")

helmets = bikes // 5
total cost bikes = 250 * bikes
total cost helmets = 250 * helmets
total cost of bikes and helmets = total_cost_bikes + total_cost_helmets

print output

'''

bikes = int(input("how many bikes did you sell?: "))

helmets = bikes // 5
revenue_a = bikes * 250
revenue_b = helmets * 50
output = revenue_a + revenue_b

print(output)
