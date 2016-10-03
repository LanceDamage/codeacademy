'''
In this project, I'll create an area calculator for a number of shapes.
'''
#first, I'll import some important tools
from math import pi
from time import sleep
from datetime import datetime
#next, I'll use a function to retreive the date and time
now = datetime.now()
print 'Calculator is waking up...'
#now I'll print the day and time like MM/DD/YYYY HH:MM
print "Current time: %s/%s/%s %s:%s" % (now.month,now.day,now.year,now.hour,now.minute)
# I need to ask the program to delay a bit
sleep(1)
#this keeps users on track
hint = "Dont forget to include the right units! \nExiting..."
#now let's ask the user what shape they'd like to calculate
option = raw_input("Enter C for Circle or T for Triangle: ")
#we will force any entry to be uppercase
option = option.upper()
#create an if statement that determines what a user specified
if option == "C":
    radius = float(raw_input("Enter the radius of the circle: ")) 
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area,hint))
elif option == "T":
    base = float(raw_input("Enter the base of the triangle: "))
    height = float(raw_input("Enter the height of the triangle: "))
    area = (.5)*base*height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area,hint))
else:
    print "I didn't understand that. Try again."
