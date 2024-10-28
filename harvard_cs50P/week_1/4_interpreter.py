#Ashton Hollick 10/2024

"""Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split, which separates a str into a sequence of values, all of which can be assigned to variables at once. For instance, if expression is a str like 1 + 1, then

x, y, z = expression.split(" ")
will assign 1 to x, + to y, and 1 to z.
Here’s how to test your code manually:

Run your program with python interpreter.py. Type 1 + 1 and press Enter. Your program should output:
2.0 
Run your program with python interpreter.py. Type 2 - 3 and press Enter. Your program should output:
-1.0
Run your program with python interpreter.py. Type 2 * 2 and press Enter. Your program should output
4.0
Run your program with python interpreter.py. Type 50 / 5 and press Enter. Your program should output
10.0"""

expression = input("Please Enter Your Equation: ")
split_express = expression.split(" ")

x = split_express[0:1:]
y = split_express[1:2:]
z = split_express[2:3:]

new_x = ''.join(x)
new_z = ''.join(z)

final_x = float(new_x)
final_z = float(new_z)
final_y = ''.join(y)


if final_y == "+":
    print("{:.1f}".format(final_x + final_z))
elif final_y == "-":
    print("{:.1f}".format(final_x - final_z))
elif final_y == "*":
    print("{:.1f}".format(final_x * final_z))
elif final_y == "/":
    print("{:.1f}".format(final_x / final_z))
