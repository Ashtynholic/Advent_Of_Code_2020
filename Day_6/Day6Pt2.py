# teststring = "mswxhfpl xmhulfp jhglrxfvmp xtldhmpf"
# mylist = ["mswxhfpl","xmhulfp","jhglrxfvmp","xtldhmpf"]
# sum = 0
# alphabet = "abcdefghijklmnopqrstuvwxyz"    

# mylist = teststring.split()

# for letter in alphabet:
#     letterfound = True
#     for group in mylist:
#         if group.count(letter) == 0:
#             letterfound = False
#     if letterfound == True:
#         sum += 1

# print(sum)


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


alphabet = "abcdefghijklmnopqrstuvwxyz"    
total = 0

for String in fixed_group_list:
    mylist = String.split()
    total = 0
    for letter in alphabet:
        letterfound = True
        for group in mylist:
            if group.count(letter) == 0:
                letterfound = False
        if letterfound == True:
            total += 1
    number_counter.append(total)
    
print(number_counter)
print(sum(number_counter))