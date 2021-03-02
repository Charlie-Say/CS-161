'''
program that converts input in amount of quarters, dimes, nickles, and pennies.

The program will prompt for an input from the user and convert it into the amount of change. The output will give the amount of quarters, dimes, nickles, and pennies.

Charlie Say
Pito Libby
CS 161
10:00 AM

----- PSUEDO -----

quarters = input // 25
dimes = input % 25 // 10
dime remainder = input % 25 % 10
nickles = dime remainder // 5
nickles remainder = dime remainder % 5
pennies = nickle remainders // 1

print output

'''


change = int(input("please enter change due: "))

q =  change // 25
d = change % 25 // 10
dime_rem = (change % 25) % 10
n = dime_rem // 5
n_rem = dime_rem % 5
p = n_rem // 1

print(f"Quarters: {q} Dimes: {d} Nickles: {n} Pennies: {p}")
