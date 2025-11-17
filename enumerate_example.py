# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"): # enumerating returns a tuple t
    index, character = t # t is unpacked into individual variables index and character
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
