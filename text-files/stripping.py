filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

# breaks after finding a non-matching character in chars
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

# breaks after finding (in reverse) a non-matching characters in chars
for character in first[::-1]: # process backwards
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
