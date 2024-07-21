# AshtynHolic 7-20-24
# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag?

# Holy Moly. This is a brain bender. Ok brain storming:
# We need to append this data to a dictionary so the values are stored in keys.
# we are most likely using line splicing to append the dictionary properly
# when we get a dictionary appended, we have to find a way to search through the dictionary and every one of its values to check for our "Shiny Gold Bag" and if it could validly be carried in that dictionary key. This will most likely take recurrsion.
# if thats true, we count all of the "trues" and that count is our puzzle answer.

RawList = []
NewDict = {} 
SplitEntryOne = []
SplitByContain = []

file = open("Day7Input.txt")

for line in file.readlines():
    RawList.append(line.replace('\n',''))

print(RawList)

# ok, testing some methods to turn this into a dictionary
print(RawList[0])

# print(RawList[0].split()) shows we can split it into individual words.

SplitEntryOne = RawList[0].split("contain")
print(SplitEntryOne)
print(SplitEntryOne[1])
# hmm, ok that splits an entry by the word contain which would equal the ":" in the dictionary equivelent of KEY:VALUE. wait is it always a three word segenment for the first bag?
# It IS. which means:
#  the KEY = SplitEntryOne [0]<~~~ That should be the first three words
#  the VALUE = SplitEntryOne [1] <~~~~ Thats the second part, or bags it can contain
# this way leaves the word "BAGS" in as well. 
#  but that would append it to a list. how do i make this a dictionary?

Keys = SplitEntryOne[0]
Values = SplitEntryOne[1]
NewDict = dict(zip(Keys, [[value] for value in Values]))

print(NewDict)







# dict = dict(RawList)

# # Loop to add key-value pair
# # to dictionary
# for i in range(len(RawList)):
#     # If the key is already 
#     # present in dictionary
#     # then append the value 
#     # to the list of values
#     if RawList[i][0] in D:
#         D[RawList[i][0]].append(RawList[i][1])
     
#     # If the key is not present
#     # in the dictionary then add
#     # the key-value pair
#     else:
#         D[RawList[i][0]]= []
#         D[RawList[i][0]].append(RawList[i][1])
         
# print(D)