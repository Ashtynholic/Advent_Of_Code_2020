# AshtynHolic 10-16-24
# correct answer is 348

RawList = []

file = open("Day7Input.txt")

for line in file.readlines():
    RawList.append(str(line.replace('\n','')))
# ok, testing some methods to turn this into a dictionary

working_list = []
ValueBags1 = []
FinalDict = {}

# print(RawList[0].split()) shows we can split it into individual words.
for line in RawList:
    working_list.append(line.split("contain"))

templist2 = []

for sublist in working_list:
    # For sublist is running through the list sublist by sublist
    OuterKey = sublist[0].rstrip('s ')
        # for item is running through each element in the sublist
    Templist = sublist[1].split(",")
        
        #Now were striping the data of the white space to the left 
    for line in Templist:
        line.lstrip(' ')
        # now were striping the rest of the unwanted charaters
        templist2.append(line.lstrip(' ').rstrip('.').rstrip('s'))
        
        # intializing a temp dictionary to start nesting
    contents_dict = {}
    
    # here were running through the value list we made, and slicing it further to seperate the numbers from the bags and then updating it to that temp dictionary
    for line in templist2:
        # No other bag is a value option, so we added a condition that finds "no other bag" and adds it as the Key and the value as 0
        if line == "no other bag":
            contents_dict.update({line:0})
        else: 
            tempnumber = line[0]
            tempstring = line[2::]
            contents_dict.update({tempstring:tempnumber})
    #we reinitialize and empty templist2 so it doesnt continually append 
    templist2 = []
    # updating the final ditionary witht he created nested dictionary
    FinalDict.update({OuterKey:contents_dict})
    
# by here we have processed the entire file and created the full nested dictionary
# print(FinalDict)
    
# print(FinalDict.get("shiny gold bag"))

#first thing recursive does, is check for an ending condition which is "No other bags" or a "shiny gold bag" these are our two conditions
# if neither of the ending conditions, then we call ourselves again
#if recursive function call finds a bag, add to a counter
# if it finds no other bags, adds nothing to counter and returns
# only recursing if not doing anything else

gold_bag_count = 0

def check_for_gold_bag(bag):
    global gold_bag_count
    if bag == "shiny gold bag":
        gold_bag_count +=1
        return True
    if bag == "no other bags":
        return 
    if bag in FinalDict:
        for inner_bag in FinalDict[bag]:
            if inner_bag != "none" and check_for_gold_bag(inner_bag):
                return True
    return False           
                
for bag in FinalDict.keys():
    if bag != "shiny gold bag":
        check_for_gold_bag(bag)
        
print(gold_bag_count)
                
        

