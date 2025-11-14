empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd # concatenates 2 lists
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

number_string = "432985617"
digits = sorted(number_string) # creates a list of characters
print(digits)
print(type(digits)) # will be a list

digits = list(number_string) # using list initializer
print(digits)

# using list initializer to duplicate lists
more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers) # False. Checks whether the lists are the same (reference the same object)
print(numbers == more_numbers) # True. Checks whether the list items are the same.more_numbers = list(numbers)

# using slice to duplicate lists
more_numbers = numbers[:]
print(more_numbers)
print(numbers is more_numbers) # False. Checks whether the lists are the same (reference the same object)
print(numbers == more_numbers) # True. Checks whether the list items are the same.more_numbers = numbers[:]

# using copy method
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers) # False. Checks whether the lists are the same (reference the same object)
print(numbers == more_numbers) # True. Checks whether the list items are the same.
