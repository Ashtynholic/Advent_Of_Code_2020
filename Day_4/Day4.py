#AshtynHolic 4-2024
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid? Valid Fields are:
#byr
#iyr
#eyr
#hgt
#hcl
#ecl
#pid
#cid - This is the only optional field missing or not doesnt matter

#So I need a program that reads all of the passports (Passports are seperated by new EMPTY lines /n) and validates the 7 particular KEY id's (passport info is written in KEY:Value) that are seperated by spaces AND new lines, randomly. if they are true to those 7 values, count the grouped info as "VALID", then use a counter to collect the amount of valid passports

#First, gotta open the data file.
file = open("Day4.txt")

#Need to pin this info TO something first, then try to figure out how to group by splitting. Can I split by new EMPTY line? hmm, that would help. I searched the interent and tried this multiple diffferent ways, most of which I didnt understand, so I couldnt figure out how to continue the code. SO I opted to keep searching for a basic solution I actually understood.

# ok, one empty line dopesnt work, because some of these passsports do that. but if i could split it by when it finds 3 consecutive empty lines, that would split it properly. but thats hard to figure out too. so i split the original list by new lines, which left a list seperated by empty new lines. then found the second code online to basically take a ll that data before it hits an empty list,"[]", and append those as lists to another list called passports.

AllPassportData = []
Key = ['byr','iyr','eyr','hgt','hcl',['ecl'],['pid']]
Passport_Counter = 0
FormatPassport = []

for line in file.readlines():
        AllPassportData.append(line.split())
        
passports = [[]]

for ele in AllPassportData:
    if len(ele) > 0:
        passports[-1].append(ele)
    else:
        passports.append([])
        

        
Passport_Counter = passports.count(1)        


# for i in passports:
#     x.extend(i)
# for i in x:
#     res.append((i,))        
        
# if 'byr' in passports[2]:
#     Passport_Counter = Passport_Counter +1

# for line in passports:
#     FormatPassport.append(list.split(0))

# if (all(x in passports[0] for x in Key)):
#     Passport_Counter = Passport_Counter +1

print(passports)
print(Passport_Counter)
# for i in passports:
#     if(i == "byr" and "iyr" and "eyr" and "hgt" and "hcl" and "ecl" and "pid"):
#         Passport_Counter = Passport_Counter +1

     
# print(passports)

# print(len(passports))

# print(Passport_Counter)
# for line in passports:
#         splitpassports = passports.slice()
        
# print(splitpassports)
     
#Ok! I have an actual list of the passports now! it's grouped to make my eyes hurt, but its #there. It's technically a List of Lists of Lists. That might come back to bite me later.

#NOW, how do i check EACH item on that list for all 7 KEYS? if statements?
# if each 2nd list of passports list contains 7 Keys == True passport, add to a counter

# Method #1 found online: Using collections.Counter() 
# #collections.Counter() provides two direct methods keys() and values() that provides the elements and its occurrences. At last, zip them together using Python zip() method. 

# Python3 program to Grouping list
# elements based on frequency
# from collections import Counter
 
# def group_list(lst):
     
#     return list(zip(Counter(lst).keys(), Counter(lst).values()))
     
# # Driver code
# lst = [1, 3, 4, 4, 1, 5, 3, 1]
# print(group_list(lst)) 