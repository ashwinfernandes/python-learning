filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)
