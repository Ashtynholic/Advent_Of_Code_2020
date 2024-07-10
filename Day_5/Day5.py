#5-12-24 AshtynHolic oh-crap-day-5 ^_^*

#so heres the actual puzzle question material:

    # Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

# Ok so this one is interesting and going to utilize alot of splitting or what im really thinking it is, partitioning
#each of these is a boarding pass
#they are using "Binary Space Partitioning" basically creating "black and white" groups, then continuinng to partition

#first we have intialized the base information into a list

basedata = []
seat_list = []
final_seats = []
bottom_row = 0
top_row = 127
left_column = 0
right_column = 7
boarding_pass = ""

f = open('BoardingPasses.txt')

for line in f.readlines():
    basedata.append(line)
    
#we clean up the data and remove the new lines ('\n') so the data is a list of the correct inforation, and individual seats. 
    
for line in basedata:
    seat_list.append(line.replace('\n',''))
    
  # there are 127 seats in total. the letters represnt FRONT and BACK aka "f" and "b" for the first 7 letters in each seat.
#so we start by making a variable to contain unscrambled seat numbers at the end.(so i dont forget later)
#so if first letter is F == range of 0-63 and b == range of 64-127
# how do i determine and append that data, then use elif statements and partitioning to determine the range over the next 6 letters

import math
bottom_row = 0
top_row = 127
left_column = 0
right_column = 7


rows = []
columns = []
row = 0

# fixed boarding pass = BFFFBBFRRR: row 70, column 7, seat ID 567
example = seat_list[0]
# "BFFFBBFRRR"row 70, column 7, seat ID 567
# "FFFBBBFRRR"row 14, column 7, seat ID 119.
# "BBFFBBFRLL"row 102, column 4, seat ID 820.
# example need to equal the count of the seat list

rows = example[:7:1]
columns = example[7:10:1]

for character in rows:
    if character == "B":
        bottom_row = math.ceil(bottom_row + ((top_row-bottom_row)/2)) #the upper bound is 127, so this makes the      lower bound 64
        # math.ceil is rounding up the numbers to the to the highest
        row = bottom_row
    if character == "F":
        top_row = math.floor(top_row - ((top_row-bottom_row)/2)) #the upper is 127, this makes the top half of 127 (64-127)
        # math.floor is rounding numbers to the lowest
        row = top_row
        
    print(row)
        
for i in columns: 
    if i == "R":
        left_column = math.ceil(left_column + ((right_column-left_column)/2))
        column = left_column
    if i == "L":
        right_column = math.floor(right_column - ((right_column-left_column)/2))
        column = right_column
     
    print(column)
    
        
seat_id = (row * 8 + column)   
        
print(seat_id)        
# print(seat_list)
# print(rows)
# print(columns)        

    # the first run it will hit the b, and lower bound will equal 64. and the upper bound will still be 127. The second time it runs through another character, it hits the f and then the lower bound will be 64 but the upper bound will stil be 64
    # top row = top row - rang that is given to us then dived by 2       
    # top row = 127-(127-0/2) = 63
    # top row = 63-(63-0/2) = 32
    # top row = 32-(32-0/2) = 16
    # bottom row = botttom row + (top row-bottom row/2)
    # bottom row = 0+(127-0/2) = 63
    # bottom row = 63 +((127-63)/2) *equals 32 = 95
    # bottom row = 95 +((127-95)/2) = 111   
    
        

# workingdata = 0
  
# # for i in seat_list:
# #     if (seat_list[0][0] == "F"):
    
    
    
    #     workingdata = range(63)
    # else:
    #     workingdata = range(64,127)
        
        # so im not quite using the range function right here, i think. But if i was, now id start doing partioning for the next 6 letters in a row to get the rownumber
        #actually now that im looking at it, im better off slicing I think?
        # heres an example i found of slicing:
        
        # To illustrate slicing, it is:
        # [start:stop:step]
        
        # example
        # l = [1,2,3,4,5,6,7,8,9] 
        # s = l[4:8:2] 
        # print(s) #this will print [5,7]
        
        #  you can see the start step is 4th index, stop index is 8th index and the steps are in count of 2.
        #  Hence the answer is [5,7]
         #BUT i actually need to split a RANGE in half, i think its different than this
         
        #  The numpy.array_split() method in Python is used to split an array into multiple sub-arrays of equal size. 
        #  In Python, an array is a data structure that is used to store multiple items of the same type together
        
        # this sounds like what i need i think
        
        # if (seat_list[0][1] == "F"):
        #     workingdata = 
            
        
        
# print(seat_list)
# print(seat_list[0])
# print(seat_list[0][0])
# print(workingdata)