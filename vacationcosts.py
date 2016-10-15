#This is a function to help plan for a vacation
#The first function will help define the hotel costs
def hotel_cost(nights):
    return 140 * nights
#The second function will define the airplane costs
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        print "I don't know that city."
#Now we need to figure how much it will cost to get around
def rental_car_cost(days):
    if days < 3:
        return 40 * days
    elif days >= 3 and days < 7:
        return days * 40 - 20 
    elif days >= 7:
        return days * 40 - 50
#Next let's define a function that brings these former functions together
def trip_cost(city,days,spending_money):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city) + spending_money
#Now let's plan and print a trip
print trip_cost("Los Angeles",5,600)
