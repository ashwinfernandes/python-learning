empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd] # creates a nested list containing lists even and odd
print(numbers)

for number_list in numbers:
    print(number_list) # prints individual lists

    for value in number_list:
        print(value) # prints individual elements of each list
