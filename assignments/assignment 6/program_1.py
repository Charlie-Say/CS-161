'''
 write a proram to sum a list of numbers.

 write a code to randomly generate the list of numbers, ten integers between 1 and 1337

program_1
'''

# TRY
my_list = [15, 7, 22, 37, 42]

print(f"The sum of the list is: {sum(my_list)}")

import random

for n in range(10):
    
        print(random.randrange(1338))



# SOLUTION
nums = [random.randint(1, 1337) for _ in range(10)]

print(sum(nums))