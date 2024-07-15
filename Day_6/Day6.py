# AshtynHolic 7-11-24

# # As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

# However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

# abcx
# abcy
# abcz
# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

# Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# This list represents answers from five groups:

# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

#so were trying to count the number of characters in each grouping, then add those counts together
group_data_1 = []
group_data_clean = []
number_counter = []

f = open("Day_6_Input.txt")

for line in f.readlines():
    group_data_1.append(str(line))
    
for line in group_data_1:
    group_data_clean.append(line.replace('\n',''))
    
# the steps here would be to go through each item in this list, count the number of unique letters in that item, save that number, then move to the next item on the list, count the unique leters again, continue saving each number until you reach an empty string. once you reach an empty string, add the previously saved numbers so far together. save THAT number. now continue that pattern until you reach the end of the list. the numbers listed are then added together for the sum and answer. 

string_list = ' '.join(group_data_clean)

fixed_group_list = string_list.split('  ')

print(fixed_group_list)

print(len(fixed_group_list))

# Lil pat on the back here, now that data is grouped correctly, each item on the list is the group of passengers.
# So the data is grouped correctly, now i need to count the unique characters in each group, count them, save that count, then add all th ecounts together at the end.

# found this Python program to count the number of distinct
# characters present in the string

S = fixed_group_list[0]
a = ""
for i in S:
    if i not in a:
        a += i
number_counter.append(len(a))

print(number_counter)

# well, this works on the first item, and any one item in the list at a time, but how do i get this to walk the rest of the items? when i leave it with no indexing i get too big a number, its counting them ALL. how can i get each number from each item and append those to the number_counter list?








# ~~~~~~~~~~Extra Working Code~~~~~~~~~~~~~
# print(groups)
# letters = group_data_clean
# unique_letters = set(letters[0])             # == set(['a', 'b', 'c'])
# unique_letter_count = len(unique_letters)




# To check if a list contains only unique values, you can compare the length of the list with the length of the set created from the list:

# def is_unique(lst):
#     return len(lst) == len(set(lst))
# # Example usage
# my_list = [1, 2, 3, 4, 5]
# print(is_unique(my_list))  # Output: True
# my_list_with_duplicates = [1, 2, 3, 3, 4, 5]
# print(is_unique(my_list_with_duplicates))  # Output: False
# What built-in Python data structure can be used to get unique values from a list?
# The set data structure is used to get unique values from a list. A set automatically removes duplicates and maintains only unique elements.

# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_values = list(set(my_list))
# print(unique_values)  # Output: [1, 2, 3, 4, 5]
# How do I count unique items in a list in Python?
# To count the number of unique items in a list, convert the list to a set and get the length of the set:

# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_count = len(set(my_list))
# print(unique_count)  # Output: 5