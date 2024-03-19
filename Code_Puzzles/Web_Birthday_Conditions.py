# Amy’s site has a web form for collecting a user’s birthday, but she notices that some site visitors entered nonsense month numbers like 0 or 47. She wants to add input validation to her form, so she can display an informative error message if a user enters an impossible date.

# Amy added validation for the day, but now wants to handle the month input.

# Wrap the month error in a conditional so that it only prints if the month is invalid.
# Valid month values must be between 1 and 12, where 1 represents January and 12 represents December. If the month is between 1 and 12, inclusive, the month error should not print.

# Do not change the wording of the error messages.

day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month == 0 or month > 12:
    print("Error. Month must be between 1 and 12.")

# # 
#     Amy tests her form by entering 6 for the month and 31 for the day. What bug does she find?

# June 31 should be an invalid date, because April, June, September, and November only have 30 days. She needs to validate the day and month in combination!

# Add a conditional that checks if the day is 31 for the months with only 30 days.

# If the combination is invalid, print the message: Error. Day must be within the month.

# Pay attention to your compound condition's order of operations - you may need parentheses here! You can ignore February for now.

# Make sure to print the exact error message provided.
    
    day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month == 0 or month > 12:
    print("Error. Month must be between 1 and 12.")

if day == 31 and (month == 4 or 6 or 9 or 11):
    print("Error. Day must be within the month.")

    #so this tripped me up for a while, because I didnt add the parenthesis around "month == 4...". Why does this only work with the parenthesis? 

# #  Amy wants her form to ask for birth years, as well, so she can recognize a user’s age.

# Use the input() function to ask the user to enter a year.
# Add a conditional that checks if the year is four digits long.
# If the year is not four digits long, print the message: Error. Year must have four digits.
# You can tell if an integer has four digits by checking if it's between 1000 and 9999, inclusive. Remember to print the exact error message provided!  
    
day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month == 0 or month > 12:
    print("Error. Month must be between 1 and 12.")

year = int(input("Enter a year (1000-9999): "))
if year < 1000 or year > 9999:
        print("Error. Year must have four digits.")
        
if day == 31 and (month == 4 or 6 or 9 or 11):
    print("Error. Day must be within the month.")

    # day = int(input("Enter a day (1-31): "))
# if day < 1 or day > 31:
#     print("Error. Day must be between 1 and 31.")

# month = int(input("Enter a month (1-12): "))
# if month == 0 or month > 12:
#     print("Error. Month must be between 1 and 12.")

# year = int(input("Enter a year (1000-9999): "))
# if year < 1900 or year > 2006:
#         print("Error. Year must be a valid birthdate.")
        
# if day == 31 and (month == 4 or 6 or 9 or 11) or day >= 30 and (month == 2): 
#     print("Error. Day must be within the month.")
    
    #so i added a conditional for february, and tightened up the years. but if i wanted to add a conditional to take into account leap years, how would i do that? how could i start with the
    #first leap year, and add +4 years to that year, and that equals day=29 being valid instead of just 28? year == 1904 and every 4 year interval after is <=29
    #maybe im just not smart enough for any of this :(