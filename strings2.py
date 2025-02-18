# Indexing
#         01234567890123
parrot = "Norwegian Blue"
print(parrot)

###### mini challenge ######
# what_i_want = "we win"
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

### my way ###
# what_i_want = "we win"
# for char in what_i_want:
#     index = parrot.find(char)
#     print(parrot[index])

print()
# what_i_want = "we win" using negative indexing
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

### my way ###
# what_i_want = "we win" using negative indexing
# what_i_want = "we win"
# for char in what_i_want:
#     index = parrot.find(char)
#     print(parrot[index-len(parrot)])

# another way
stringLen = len(parrot)
print(parrot[3 - stringLen])
print(parrot[4 - stringLen])
print(parrot[9 - stringLen])
print(parrot[3 - stringLen])
print(parrot[6 - stringLen])
print(parrot[8 - stringLen])
