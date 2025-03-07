name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

if age >= 18:
    print("you're old enough to vote.")
    print("Please put an X in the box")
else:
    print("Please come back in {} years.".format(18 - age))

if age < 18:
    print("Please come back in {} years.".format(18 - age))
else:
    print("you're old enough to vote.")
    print("Please put an X in the box")
