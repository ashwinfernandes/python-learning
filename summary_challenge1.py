# print a number of options and choose one of them, input 0 to quit
options = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed", "Drink coffee"]

INVALID_CHOICE = len(options) + 1

x = INVALID_CHOICE
while x != 0:
    if 0 < x <= len(options):
        print("Your choice is {}".format(x))
    else:
        print("Please choose an option from the list below:")
        for i in range(len(options)):
            print("{}.\t{}".format(i + 1,options[i]))
        else:
            print("0.\tExit")
    x_str = input()
    x = int(x_str) if x_str.isnumeric() else INVALID_CHOICE
