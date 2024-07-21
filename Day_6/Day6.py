# AshtynHolic 7-17-24

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
answer_list = []

f = open("Day_6_Input.txt")

for line in f.readlines():
    group_data_1.append(str(line))
    
for line in group_data_1:
    group_data_clean.append(line.replace('\n',''))
    
# the steps here would be to go through each item in this list, count the number of unique letters in that item, save that number, then move to the next item on the list, count the unique leters again, continue saving each number until you reach an empty string. once you reach an empty string, add the previously saved numbers so far together. save THAT number. now continue that pattern until you reach the end of the list. the numbers listed are then added together for the sum and answer. 

string_list = ' '.join(group_data_clean)

fixed_group_list = string_list.split('  ')

print(fixed_group_list)


# Lil pat on the back here, now that data is grouped correctly, each item on the list is the group of passengers.
# So the data is grouped correctly, now i need to count the unique characters in each group, count them, save that count, then add all th ecounts together at the end.


# found this Python program to count the number of distinct
# characters present in the string

for S in fixed_group_list:
    a = ""
    for i in S:
        if i == " ":
            continue
        if i not in a:
            a += i    
    number_counter.append(len(a))
print(number_counter)

print(sum(number_counter))


    
# DAY 2

# each item listed by index in the list of fixed group list ([0,1,2,etc]) is each indivdual group. the People are seperated by the white space inside of each of those items. we need to compare each line seperated by white space against each other and count if a character appears in EACH line. then append that count to another list.