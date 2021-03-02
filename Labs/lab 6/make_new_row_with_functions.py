pascal_height = int(input("how many rows bruh: "))



def make_new_row(old_row):

    if old_row == []:
        old_row = [1]
        print('    '.join(str(x) for x in old_row).center(230))
    
    elif old_row == [1]:
        old_row = [1,1]
        print('    '.join(str(x) for x in old_row).center(230))


    if len(old_row) == pascal_height:
        return

    else:

        new_row = []
        for i in range((len(old_row) - 1)):
            new_row.append(old_row[i] + old_row[i+1])
            
        new_row.append(1)
        new_row.insert(0 , 1)
        old_row = new_row
        
        str_list_center = ('    '.join(str(x) for x in old_row).center(230))
        print(str_list_center)
        
        return old_row , make_new_row(old_row)

make_new_row([1])
