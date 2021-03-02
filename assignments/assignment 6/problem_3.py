'''
 write a python program to get the largest number from a list

 problem_3
'''

my_list = [1, 4, 6, 3, 8, 9]

biggest = 0
for num in my_list:
    
    if num > biggest:
        biggest = num
    
print(biggest)
        
# SOLUTION

print(max(my_list))

# 8 AM CLASS
my_list.sort()
sorted_list = sorted(my_list, reverse=True)
print(my_list[-1])
print(sorted_list)
printed(sorted[0])