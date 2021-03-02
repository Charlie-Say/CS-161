'''
import has_common_element() from mytools.py
'''


from mytools import has_common_element

list1 = [43, 45, 47, 34, 65, 2]
list2 = [43, 95, 23, 63, 34, 2, 6, 87]
print('First List')
has_common_element(list1, list2)

list3 = [1, 4, 5, 6, 7, 8, 74]
list4 = [43, 95, 23, 63, 34, 3, 71, 87]
print()
print('Second List')
has_common_element(list3, list4)