"""
In this project, we will use Python to write a Mad Libs story! 
Mad Libs require input from the reader to plug into the story. 
This script will require the creation of a user prompt requiring input, 
and will then print the entire story.
"""

#This will inform the user that the program
#is running
print "In a land far away..."
name = raw_input("Name: ")
lineage = raw_input("Clan: ")
loc = raw_input("Planet: ")
power = raw_input("Ability: ")
verb1 = raw_input("Infinitive tense verb: ")
verb2= raw_input("Infinitive tense verb: ")
verb3 = raw_input("Infinitive tense verb: ")
noun1 = raw_input("Favorite math teacher: ")
noun2 = raw_input("Favorite hair product, plural: ")
noun3 = raw_input("Name of river: ")
noun4 = raw_input("Musical Instrument: ")
animal = raw_input("Animal: ")
food = raw_input("Food: ")
number = raw_input("Number: ")
nemisis= raw_input("Nemisis: ")
country = raw_input("Country: ")
dessert = raw_input("Dessert: ")
year = raw_input("Year: ")
feel = raw_input("Feeling1: ")
feel2 = raw_input("Feeling2: ")
#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally incite a bunch of %sing over the big %s of planet %s. 
On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, 
which made all of the %ss very %s. %s tried to %s into the sewers and found %s's rats %s. Needing help, %s quickly called %s. 
%s appeared and saved %s by flying to the %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, 
in a world where %ss ruled the world. %s quickly sought out everyone in the clan %s, including %s and challenge them to a war to end 
all wars. %s thought that this challenge would be no problem since he gained the super power of %s, but %s recruited all the %ss by 
offering them %s. %s brought the %s back into the fold with his %s-playing, won the victory, and all of %s was %s."
print STORY % (feel,nemisis,verb1,noun3,loc,noun3,animal,noun2,verb1,noun4,animal,feel2,noun1,verb3,nemisis,power,noun1,name,name,
country,noun3,nemisis,dessert,nemisis,year,animal,nemisis,lineage,name,name,power,nemisis,animal,food,name,animal,noun4,loc,feel2)
