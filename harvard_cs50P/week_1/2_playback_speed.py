# AshtynHolic 10-16-24

# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

# Hints
# Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

# Here’s how to test your code manually:

# Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output:
# This...is...CS50    
# Run your program with python playback.py. Type This is our week on functions and press Enter. Your program should output:
# This...is...our...week...on...functions
# Run your program with python playback.py. Type Let's implement a function called hello and press Enter. Your program should output
# Let's...implement...a...function...called...hello
# You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

answer = input("Tell me how you feel? ")

answer = answer.replace(' ','...')

print(answer) 