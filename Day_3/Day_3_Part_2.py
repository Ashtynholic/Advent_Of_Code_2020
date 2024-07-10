#Ashtyn Holic 3-13-23
# #You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

map_list = []
sled_list = []
index_right = 3
index_down = 1
tree_counter = 0
slope_list = [[1,1], [3,1], [5,1], [7,1], [1,2]]
slope = 0
final_tree_count = []

f = open("inputAoC3.txt") 
for line in f.readlines():
    map_list.append(line)
#search through everything and remove any newlines if they are present in the data
# map_list = [line.replace('\n','') for line in map_list]    
for line in map_list:
    sled_list.append(line.replace('\n',''))
#so in order to count the trees, we need to create a program that uses the 1 down three right pattern continuously until we reach the end of the list and keep track of all of trees (#'s) we cross paths with on the way
# for slope in slope_list:
#     index_down = slope_list[0], index_right = slope_list[1]
#     #you'll re assign new values to index down and index right by walking slope list
    #I understand i need to reassign the list values to the index's, but i have no idea how to do it. I know i can count the list items with values, but how do i count multiple values?
     # in multiple runs? how am i changing the variable each loop? I tried to brute force it manually, and couldnt even get the right number. I started getting emotional and walked away.

for slope in slope_list:
    
    index_down = slope[1]
    index_right = slope[0]
    movement_down = 0
    movement_right = 0
    tree_counter = 0
    end_of_file = False

    # print(slope)
    # #assign a slope fromt he list to index down and index right
    # print(slope[0])
    # print(slope[1])
    for line in sled_list:
            if end_of_file:
                #when break executes, its breaking the current for line, and moving to the next 
                break
            try: 
                if sled_list [movement_down] [movement_right] == "#":
                    tree_counter = tree_counter +1
            #were always going donw by 1, and the program stops at the end of the list.       
                movement_down += index_down
            #We can run out of width, but we know that the patterns repeat, so we fake them repeating by subtracting the length of the list if we go over.  
                movement_right += index_right 
                if movement_right > len(line)-1: 
                    movement_right = movement_right -len(line)
                if movement_down > len(sled_list):
                    #this was because we were reaching the end of the file, and needed to repeat back at top
                    end_of_file = True
                
            except IndexError:
                    # continue
                print("index down was:", movement_down, "index right was:", movement_right)        

    print("The Number of trees is:", tree_counter)    

    final_tree_count.append(tree_counter)

# print(final_tree_count)    
#This is a temporary variable number, when walking a list this will always mean the current item on that list
#every time the loop runs it will be the next item after
product = 1  
for number in final_tree_count:
    product *= number


print(product)

# If you want to avoid importing anything and avoid more complex areas of Python, you can use a simple for loop:

# nums = [1, 2, 3]

# product = 1  # Don't use 0 here, otherwise, you'll get zero because were MULTIPLYING
# for num in nums:
#     product *= num

# print("Slope 1 is 60")
# print("slope 2 is 189")
# print("Slope 3 is 75")
# print("Slope 4 is 82")
# print("Slope 5 is 37")

# print("Did this work? ", final_tree_count)

#We need to create a loop that walks the list,
#on each line, check the index down and index right
#if the item there is equal to a "#" increment a counter of how many "#" (Trees) weve found, no tree = no need to keep track of
#were going to have to increment the index for how far were going. were going to need a varible that stores the index of how far weve gone and checks if it is higher than the width of the list. if it is higher, then we need to change it by subtracting the width of the list by that number.
#two indexs here, 3 right and 1 down






