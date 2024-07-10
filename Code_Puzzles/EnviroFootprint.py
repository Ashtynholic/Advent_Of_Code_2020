footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    footprint = footprint + 5
    contains = input("Does your pets food contain meat? ")
    if contains == "yes":
        footprint = footprint +10

days = int(input("How many days a week do you commute to school or work? "))
if days == 0:
    footprint = footprint + 0
else:    
    transport = input("Do you commute by foot, bike, bus, train, or car? ")    
    if transport == "car":
        footprint = footprint + (8 * days)
    if (transport == "bus") or (transport == "train"):
        footprint = footprint + (4 * days)
    # if transport == "train":
    #     footprint = footprint + (4 * days)
    if (transport == "bike") or (transport == "foot"):
        footprint = footprint + (days)
    # if transport == "foot":
    #     footprint = footprint + (days)
    

print("Your environmental footprint score is " + str(footprint) + ".")
