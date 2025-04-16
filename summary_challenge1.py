# print a number of options and choose one of them, input 0 to quit
options = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed", "Drink coffee"]

x = 10
while x != 0:
    if 0 < x <= len(options):
        print("Your choice is {}".format(x))
    else:
        print("Please choose an option from the list below:")
        for i in range(0, len(options)):
            print("{}.\t{}".format(i + 1,options[i]))
        else:
            print("0.\tExit")
    x = int(input())
