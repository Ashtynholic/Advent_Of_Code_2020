# Ashton Hollick 11/2024

#First I need to get the camel case from the user
camel_case = input("camelCase: ")
# I need to identify when the capital letters are, split it by that location
for char in camel_case:
    if char.isupper():
        _ = camel_case.split(char)
        # insert a "_" before it and uncapitilize the letter
        _.insert(1, "_" + char.lower())
        # rejoin the string
        camel_case = "".join(_)
        # print out the snake case
print("snake_case:", camel_case.lstrip("_"))
