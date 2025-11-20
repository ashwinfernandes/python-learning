small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99) # removes the number if it exists in the set,
# does nothing otherwise
print(small_ints)

small_ints.remove(99) # will crash the code because 99 doesn't exist in the set
print(small_ints)
