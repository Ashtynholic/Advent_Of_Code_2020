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

f = open("inputAoC3.txt") 
for line in f.readlines():
    map_list.append(line)
#search through everything and remove any newlines if they are present in the data
# map_list = [line.replace('\n','') for line in map_list]    
for line in map_list:
    sled_list.append(line.replace('\n',''))
#so in order to count the trees, we need to create a program that uses the 1 down three right pattern continuously until we reach the end of the list and keep track of all of trees (#'s) we cross paths with on the way
for line in sled_list:
    try: 
        if sled_list [index_down] [index_right] == "#":
            tree_counter = tree_counter +1
    #were always going donw by 1, and the program stops at the end of the list.       
        index_down = index_down +1
    #We can run out of width, but we know that the patterns repeat, so we fake them repeating by subtracting the length of the list if we go over.  
        index_right = index_right +3
        if index_right > len(line)-1: 
            index_right = index_right -len(line)
    except IndexError:
        print("index down was:", index_down, "index right was:", index_right)        

print("The Number of trees is:", tree_counter)        





#We need to create a loop that walks the list,
#on each line, check the index down and index right
#if the item there is equal to a "#" increment a counter of how many "#" (Trees) weve found, no tree = no need to keep track of
#were going to have to increment the index for how far were going. were going to need a varible that stores the index of how far weve gone and checks if it is higher than the width of the list. if it is higher, then we need to change it by subtracting the width of the list by that number.
#two indexs here, 3 right and 1 down


