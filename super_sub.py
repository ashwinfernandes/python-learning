animals = {'Turtle',
           'Horse',
           'Robin',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }

birds = {'Robin', 'Swallow', 'Wren'}

print(f"birds is a subset of animals: {birds.issubset(animals)}")  # True
print(f"animals is a superset of birds: {animals.issuperset(birds)}")  # True
print(f"birds is a superset of animals: {birds.issuperset(animals)}")  # False

print(f"birds is a subset of animals: {birds <= animals}")  # True
print(f"birds is a proper-subset of animals: {birds < animals}")  # True

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)  # True
print(garden_birds <= birds)  # True
print(garden_birds < birds)  # False

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # False

# disjoint sets
pixar = {"up", "brave", "inside out"}
dream_works = {"how to train your dragon", "home", "spirit"}
directions = {"up", "down", "right", "left"}

print(f"pixar.isdisjoint(dream_works): {pixar.isdisjoint(dream_works)}")  # True
print(f"directions.isdisjoint(pixar): {directions.isdisjoint(pixar)}")  # False, 'up' is in both the sets
