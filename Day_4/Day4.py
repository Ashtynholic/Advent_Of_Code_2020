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
#NEW notes 5-5-24
#Trying new approaches myself before walking along katrinas answer.


# expected_keys = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]


# def simple_passport_validator(p):
#     return all(key in p for key in expected_keys)


#Need to pin this info TO something first, then try to figure out how to group by splitting. Can I split by new EMPTY line? hmm, that would help. I searched the interent and tried this multiple diffferent ways, most of which I didnt understand, so I couldnt figure out how to continue the code. SO I opted to keep searching for a basic solution I actually understood.

# ok, one empty line dopesnt work, because some of these passsports do that. but if i could split it by when it finds 3 consecutive empty lines, that would split it properly. but thats hard to figure out too. so i split the original list by new lines, which left a list seperated by empty new lines. then found the second code online to basically take a ll that data before it hits an empty list,"[]", and append those as lists to another list called passports.
passportData = ""
AllPassportData = []
dataList = []
Passport_Counter = 0
validfieldscount = 0

f = open("Day4.txt")

for line in f.readlines():
        AllPassportData.append(line)
        
#i found this through stackoverfow and it seems to work better than previous attempts        
Passports = []
tmp = []
for item in AllPassportData:
    if item != '\n':
        tmp.append(item.rstrip('\n'))
    else:
        #Note we aren't actually processing this item of the input list, as '\n' by itself is unwanted
        Passports.append(tmp)
        tmp = []        
            
            #We are encoutering an "Off By One" error above. the last passport is detected but not appened to the data. fixing this by adding two new lines to the Day4.txt file.
 #Ok, that gave me a much cleaner list of the individual passports. now how do I validate each passport?
#I need to check each item of the list and make sure it includes ALL the 7 listed 3-letter codes (8th is still optional at this point)
#Flatting the list from a nested list, into a single list of strings.

passport_list = []
for sublist in Passports:
    passport_list.append(' '.join(sublist))  
        
while (passport_list.find(" ") != -1):
    index = passport_list.find(" ")
    datalist.append(passport_list[:index])
    passportData = passportData[index+1:]
    
for i in dataList:
    dataField = i[:3]
    data = i[4:]      
    
    if(dataField == "byr"):
        data = int(data)
        if (data >= 1920) and (data <= 2002):
            validfieldscount += 1
    elif (dataField == "iyr"):
        data = int(data)
        if (data >= 2010) and (data <= 2020):
            validfieldscount += 1
    elif (dataField == "eyr"):
        data = int(data)
        if (data >= 2020) and (data <= 2030):
            validfieldscount += 1
    elif (dataField == "hgt"):
        if (data.find("cm") != -1):
            data = int(data[:data.find("cm")])
            if (data >= 150) and (data <= 193):
                validfieldscount += 1
        elif (data.find("in")!= -1):
            data = int(data[:data.find("in")])
            if (data >= 59) and (data <= 76):
                validfieldscount += 1
    elif (dataField == "hcl"):
        validCharacters = 0
        if (data[0] == "#"):
            data = data[1:]
            if (len(data) == 6):
                for j in data:
                    if (j.isdigit()):
                        j = int(j)
                        if (j >= 0) and (j <= 9):
                            validCharacters += 1
                    elif (j.isalpha()):
                        if (j >= 'a') and (j <= 'f'):
                            validCharacters += 1
                if (validCharacters == 6):
                    validfieldscount += 1
    elif (dataField == "ecl"):
        if (data == "amb"):
            validfieldscount += 1
        elif (data == "blu"):
            validfieldscount += 1
        elif (data == "brn"):
            validfieldscount += 1
        elif (data == "gry"):
            validfieldscount += 1
        elif (data == "grn"):
            validfieldscount += 1
        elif (data == "hzl"):
            validfieldscount += 1
        elif (data == "oth"):
            validfieldscount += 1
    elif (dataField == "pid"):
        if (len(data) == 9) and (data.isdigit()):
            validfieldscount += 1
            
if (validfieldscount == 7):
    Passport_Counter += 1
    
passportData = ""
dataList = []
validfieldscount = 0

f.close()

print ("If this worked, there are", Passport_Counter, "valid passports")    
    
        
# for passport in passport_list:
#     if simple_passport_validator(passport):
#         Passport_Counter += 1

print(passport_list[-1])
print(Passport_Counter)

#have flattened the nested list into a single list of strings
# FormatPassport = Passports.count
# byr = 'byr'
# iyr = 'iyr'
# eyr = 'eyr'
# hgt = 'hgt'
# hcl = 'hcl'
# ecl = 'ecl'
# pid = 'pid'

# I cant seem to split this list any further?


# for line in Passports:
#     if byr and iyr and eyr and hgt and hcl and ecl and pid == True:
#         Passport_Counter = Passport_Counter +1








# for sublist in Passports: 
#     for item in sublist: 
#         print(item, end=' ') 
#     print()                    
# # WOW that made it pretty, but its only printing pretty, its not actually listed that way

#Can I count how many passports total first? So i know


#Everything below here were previous attempts at creating a passport list broken into correct info chunks that didnt work as well                 
# passports = [[]]

# for ele in AllPassportData:
#     if len(ele) > 0:
#         passports[-1].append(ele)
#     else:
#         passports.append([])
        

        
# Passport_Counter = passports.count()        


# # for i in passports:
# #     x.extend(i)
# # for i in x:
# #     res.append((i,))        
        
# # if 'byr' in passports[2]:
# #     Passport_Counter = Passport_Counter +1

# # for line in passports:
# #     FormatPassport.append(list.split(0))

# # if (all(x in passports[0] for x in Key)):
# #     Passport_Counter = Passport_Counter +1

# print(passports)
# print(Passport_Counter)
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

# man nothing i try is working, i think i have to approach the list in the beginning differently