#Ashtyn 2-27-2024
#First, I know I need to open the file in the program
f = open("D2P1Input.txt")
#I think i need to make a variable to append the data too?
Passwords = []
split_password_entry = []
delimiter_list = []
first_position = 0
second_position = 0
letter = ""
password = ""
letter_count = 0
valid_password_counter = 0
first_letter = ""
second_letter = ""
letter_found_counter = 0
#I think ill need more than one actually? I know i need to read each line in seperate parts somehow, and those parts and inspecting each other? 
#I need to understand how to create a correct/incorrect programming line as well
for line in f.readlines():
    Passwords.append(line)
#I think im missing some codes from here. Im also lost in understanding    
#each line gives the password policy and then the password
#look at the policy first, how we know its a poliy is it will be a numberhyphen number then space
#always following the space is the letter we care about
#for each line will be upper and lower value as well as the letter itself
#and then eachline will be the password that appears how many times were counting it
#We need a counter for how many valid passwords
#when we finish we will need to print out how many passwords in total     
print (Passwords[0])       
print (Passwords[0].split()) 
#split the list even further
split_password_entry = Passwords[0].split()
print (split_password_entry)
#split_password_entry now contains a line from the input file divided by white space
#we are going to split the first item in the the password entry according tot hge hyphen in order to get our 
#top and bottom values
# delimiter_list = split_password_entry [0].split("-")
# print (delimiter_list)
# first_position = delimiter_list [0]
# second_position = delimiter_list [1]
# print ("my max value is ", second_position)
# letter = split_password_entry[1][0]     
# print (letter)
for line in Passwords:
    #reset the letter_found_counter to 0 this is re intializing the variable in the loop
    letter_found_counter = 0
    split_password_entry = line.split()
    password = split_password_entry [2] 
    delimiter_list = split_password_entry [0].split("-")
    first_position = int (delimiter_list [0])
    second_position = int (delimiter_list [1])
#the letter of interest is located at index 1 but there is a colon in that line too, so we specifiy that we want to 
#grab the first charactor in position 0 of the entry in index 1
    letter = split_password_entry[1][0]
#we need to grab the character from the password from the correct position to see if its the letter
#since our inputs were not zero positioned, we subtracted 1 from them    
    first_letter = password[first_position-1] 
    second_letter = password[second_position-1]          
#check if the letter is at first_posiion
#check if the letter is at second_postion
#check if this is valid by comparing weither first_postion or second_postion is set for true,
#but not both or neither 
    if first_letter == letter:
        letter_found_counter = letter_found_counter +1
    if second_letter == letter:
        letter_found_counter = letter_found_counter +1    
        #if we only found the letter once, its a valid password    
    if letter_found_counter == 1:   
        valid_password_counter = valid_password_counter +1
print ("The number of valid passwords is", valid_password_counter)  
#Each policy actually describes two positions in the password,where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
