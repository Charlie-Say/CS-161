#! /usr/bin/env python3
# # coding=utf-8
'''
Append new values to a new_row list. After the initial 1, the values will be
the sum of two elements of old_row.

It is easiest to use a for loop that loops through indices, e.g.
for i in range(n):
so you can refer to adjacent items using indices i and i +1, but be careful
that you do not get too large an index, i.e. out of range.

Alex Nylund
Charlie Say
'''


pascal_height = int(input("how many rows bruh: "))
master_list = [[1]]

def make_new_row(old_row):

   if old_row == []:
      old_row = [1]
      print(old_row)

   elif old_row == [1]:
      old_row = [1,1]
      print(old_row)

   if len(old_row) == pascal_height:
      return

   else:

      new_row = []
      
      for i in range(len(old_row) - 1):
            new_row.append(old_row[i] + old_row[i+1])
            
      new_row.append(1)
      new_row.insert(0 , 1)
      old_row = new_row
      master_list.append(old_row)
      print(old_row)
      
      return make_new_row(old_row)

print("Printing one list at a time:")
make_new_row([])
print("\n")
print(f"The whole list of lists: \n{master_list}")
print("\n")

for i in range(len(master_list)):
   master_list[i] = str(master_list[i])
   master_list[i] = '    '.join(x for x in master_list[i] if x not in '[],').center(230)
   print(master_list[i])
   
