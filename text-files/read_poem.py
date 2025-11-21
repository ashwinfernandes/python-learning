# jabber = open("Jabberwocky.txt", 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
