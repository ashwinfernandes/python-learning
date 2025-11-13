even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd) # extends even with elements of odd [2, 4, 6, 8, 1, 3, 5, 7, 9]
print(even)
another_even = even
print(another_even)

even.sort() # Sorts in ascending order. Mutates original list
even.sort(reverse=True) # Sorts in descending order. Mutates original list
print(even) # shows result of mutation
print(another_even) # same as even
