# The app also asks for the length of the item in centimeters. Unfortunately, the recycling service cannot recycle small plastic items like bottle caps because they get caught in the recycling equipment.

# Set waste_type to the value "trash" if a plastic item is smaller than 7.5 cm.
# You'll need to add new conditional that compares against the length value. Remember that the order you check the conditions and update waste_type matters!

# Large plastic items should go in the recycling, small plastic items should go in the trash, and all other items should go in the trash.

material = input("What material is it? ")
length = float(input("What is its length in cm? "))

waste_type = "trash"
if material == "plastic":
    waste_type = "recycling"
if length <= 7.5:
    waste_type = "trash"

print("Please deposit your item in the " + waste_type + " bin.")
