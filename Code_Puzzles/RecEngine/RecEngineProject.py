#AshtynHolic 4-20-24, 4-26-24, 5-3-24, 5-8-24

#SO first I'm going to pick what my engine is going to recommend. 
#I think I'm going to do an engine based on what marijuana strain is best suited for you
#That means I'll have 4 options available as Recommendation Items
# Indica
# Sativa
# Hybrid
# CBD
 
# I'll need at least 2 questions, but i'm going to try to ask 3-4 questions.
# Let me think of examples of questions:

# "Would you like to feel any sensation of high/euphoria?" this question is good because it can instantly suggest CBD if this input == no
# "Do you suffer from anxiety and/or panic attacks?" this questions is good because it rules out sativas, so this input would somehow elimnate sativa as an option? (hmmmm...) (setting a Flag boolean term)
# "Would you like to be more active, relaxed, or either?" this questions adds a different variable type, the first two are integers, this is a string? this would rule Indica

#I need to collect some information from the user

print("Welcome to Ashtyn's Cannabis Kiosk! Lets find the right strain of weed to fit YOUR Lifestyle!" )

has_high = input("Would you like to feel high? ")
energy = input("Would you like to feel sleepy? ")
panic = input("Do you suffer from Anxiety and/or Panic Attacks? ")
Level = input("Do you want a mix of mind and body highs? ")
 
Recom = "Sativa Strains."

if energy == "yes":
    Recom = "Indica Strains."
    
if Level == "yes":
    Recom = "Hybrid Strains."      

if panic == "yes":
    Recom = "Indica Strains or Inidca Heavy Hybrid Strains." 
    print("Stay away from Sativa!")   
    
if has_high == "no":
    Recom = "CBD Strains."

         
print("The Best Recommended Type Of Weed For You is " + (Recom))    


#I believe this runs correctly! Im going to test it more as well.
#5-8-24
#Im going to challenge myself to a part two of this challenge, and try to make the program continue and find out which ingestion type is best as well. 

#5-11-24
#adding consumtion reccomendations. The input above should effect the input here. lets try 3-4 questions.
#Outcomes are Smoking, Eating, Topical, *vaping and *dabs (see below) **double checked, it needs 5 options on the engine
#fuck, i forgot dabs lol, gotta add that.
#Might add a conditional to smoking where smoking = mostly private/mostly public and mostly public turns to "Vaping"


#The main default is smoking.
#Do you have asthma? = yes = instantly rule out smoking & Dabs
#Do you have a sensitive stomach? = yes = rule out eating
#are you using it for concentrated pain in areas? = yes = suggest Topical
#Do you want a long experience of euphoria (over an hour or more)?: yes = edibles
#are you consuming in a public place? = yes = suggest vaping
#Do you want the strongest high possible? = yes = dabs

print("Let's figure out which way is best for you to consume cannabis!")

asthma = input("Do you have asthma or a lung condition?: ")
stomach = input("Do you have a sensitive stomach, ulcer, or other stomach condition?:" )
