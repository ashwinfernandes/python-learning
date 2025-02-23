letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

print(letters[25::-1])
print(letters[:-27:-1])
print(letters[::-1])

#create a slice that produces the characters qpo.
print(letters[16:13:-1])
print(letters[-10:-13:-1])

#slice the string to produce edcba.
print(letters[-22::-1])
print(letters[4::-1])
print(letters[-22:-27:-1])

#slice the string to produce the last 8 characters, in reverse order.
print(letters[25:17:-1])
print(letters[:17:-1])
print(letters[:-9:-1])

print(letters[-4:]) #last 4 chracters
print(letters[-1:]) #last 1 character
print(letters[:1]) #first character
print(letters[0]) #first character, but fails with index out of range if source is empty
