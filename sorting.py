pangram = "The quick brown fox jumps over the lazy dog"  # pangrams are sentences/phrases that contain all letters of the english alphabet

letters = sorted(pangram)  # sorts in ascending ascii order
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)  # sorts in ascending order
print(sorted_numbers)  # new list with sorted numbers
print(numbers)  # numbers list remains unchanged

another_sorted_numbers = numbers.sort()  # most of the funtions that process objects in place, return None
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)  # you can also pass string literals to sorted because strings are iterable
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "micheal"
         ]
names.sort(key=str.casefold)
print(names)
