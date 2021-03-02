

import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

smol_list = ['a', 'b', 'c', 'd']
text_box_input = 1

for i in range(len(smol_list)):

    smol_list[i] = ord(smol_list[i])
    # UPPER
    if 65 <= smol_list[i] <= 90:
        smol_list[i] = (smol_list[i] + text_box_input) % 90

    # LOWER
    elif 97 <= smol_list[i] <= 122:
        smol_list[i] = (smol_list[i] + text_box_input) % 122

    
    smol_list[i] = chr(smol_list[i])

print(smol_list)