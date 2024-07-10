# Course options to choose from for our recommendation.
fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"

# Collect user attributes to inform our recommendation.
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? ")

# Make a course recommendation based on the user's attributes.
rec = ""
if grade < 6:
    # Course caters to younger learners.
    rec = grammar
else:
    if favorite_subject == "computing" or favorite_subject == "art":
        rec = pixar
    else:
        # Most broadly relevant and approachable subject.
        rec = fin_lit

print("We recommend the Khan Academy course: " + rec)