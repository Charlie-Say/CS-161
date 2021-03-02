'''
 problem 3
 accepts integer and spits out string
 
 example 5 + 55 + 555 = 615
 
'''

# TRY

for n in range(11):
    
    n = n
    n2 = n**2
    n3 = n**3
    print(str(n, n2, n3))
    print(f"{n} + {n2} + {n3}")


# DEMO

def method_2(n):
    nums = []
    for i in range(1,4):
        num = n * i
        nums.append(int(num))

    print(f"{num[0]} + {num[1]} + {num[2]} = sum(nums)}")

if __name__ == "__main__":
    n = input("Please enter a number: ")
    method_2(n)

def method_3(n):
    print(sum([int(n * i) for i in range(1,4)]))