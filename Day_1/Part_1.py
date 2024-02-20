# print ("Hello World")
# This Is A Comment
'''this is also a comment'''
#Ashtyn 2-20-2024
#create a variable named f that points to our input file
f = open("input.txt")
#create a variable called numbers that will be a list where we store all of the lines from our input
numbers = []
numbers2 = []
 
#we are going to create a loop that reads the lines of the input file one at a time and appends them to our list named numbers
#we are interating through every line of the file, and then we are taking that line and we are adding on to the end of the list that we call numbers, and we are also setting the type of that thing to an interger
for line in f.readlines():
    numbers.append(int(line))
    numbers2.append(int(line))
#we are going to print out every line of this file as an example
# for entry in numbers:
#     print(entry)        

#go through the list line by line and for every number in the list check if it combines with any of the other numbers to the sum of 2020
for value1 in numbers:
    for value2 in numbers2:
        sum = value1 + value2
        if sum == 2020:
#if it does multiply them together and print the sum
            print (value1 * value2)            
#if it doesnt continue