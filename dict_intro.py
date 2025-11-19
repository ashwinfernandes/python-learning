vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet and you "
                            "might afford a racing car.") # returns the default value
print(result)
plane = vehicles.pop("learjet") # returns the value from the dict
print(plane)

bike = vehicles.pop("tenere", "not present") # returns the value from the dict
print(bike)
print()

for key, value in vehicles.items():
    print(key, value, sep=", ")
