'''
 problem 2
 program that prints a table of n, n^2, and n^3 in right-aligned columns for 1<=n<=10

'''

# TRY

for n in range(1,11):
    print(n, n**2, n**3)
    



# DEMO

for n in range(1,11):

    print(f"{n:2} {n**2:3} {n**3:4}")