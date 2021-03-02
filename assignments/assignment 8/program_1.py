'''
open simple_text.txt and display them on screen, sorted in ascending (A-Z) order, case insensitively.
repeat words will appear in the list multiple times. Additionally, calculate and display the average word length.

problem 1
'''


import codecs

infilename = open('simple_text.txt', encoding='utf-8')
read_infilename = infilename.read()
split_infilename = read_infilename.split()
split_infilename.sort()


count = 0
# letter count
for i in range(len(split_infilename)):
    count = count + len(split_infilename[i])

# word count
len_list = len(split_infilename)

print(count)
print(len_list)

print(count / len_list)
# average = total_letters / total_words



# SOLUTION

# import string

# with open("simple_text.txt", "r", encoding="utf-8") as simple_reader:
#     words = []
#     for line in simple_reader.read():
#         for word in line.split():
#             words.append(word)

# sb_list = simple_read.read().split()
# sb_list.sort(key=str.lower)

# average_len = sum(len(word) for word in sb_list) / len(sb_list)

# print(sb_list)
# print(f"{average_len:.1f}")