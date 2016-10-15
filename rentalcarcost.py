def rental_car_cost(days):
    rental_car_cost = 40 * days
    if days >= 7:
        rental_car_cost -= 50
    elif days >= 3:
        rental_car_cost -= 20
    print rental_car_cost
rental_car_cost(1) 
