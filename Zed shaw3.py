cars=100 #here we declare a variable called cars we use equal sign to assign that value to or valiable 
space_in_a_car=4.0 #here we declare a variable and we use underscore to combine that words because space are not allowed during variable declaration
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven
print("there are",cars,"cars available..")
print("there are only",drivers,"drivers available")
print("there will be ",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have",passengers,"to carpool today")
print("we need to put about ",average_passengers_per_car,"in each car")

