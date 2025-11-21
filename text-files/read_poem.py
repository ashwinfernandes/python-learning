# jabber = open("Jabberwocky.txt", 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

with open('Jabberwocky.txt', 'r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    lines = jabber.readlines()

print(lines)
print(lines[-1:])

for line in reversed(lines):
    print(line, end='') # do some processing in reverse order
