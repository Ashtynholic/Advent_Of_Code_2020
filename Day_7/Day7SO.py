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
for line in RawList:
    SplitbyContain = RawList[0].split("contain")
    
print(SplitByContain)
