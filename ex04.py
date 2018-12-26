cars = 100
space = 4.0
driver = 30
passenger = 90
cars_not_driven = cars - driver
cars_driven = driver
carpool_capacity = cars_driven*space
ave_passenger_per_car = passenger/cars_driven


print('there are', cars, 'cars availiable')
print('there are only', driver, 'drivers availiable')
print('there will be', cars_not_driven, 'empty cars today')
print('we can transport', carpool_capacity, 'pelple today')
print('we have ', passenger, 'to carpool today')
print('we need to put about', ave_passenger_per_car, 'in each car')
