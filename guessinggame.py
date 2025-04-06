import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))

attempts = 3
guess = None
while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Game over!")
        break

    attempts -= 1
    if guess == answer:
        print("Well done, you guessed it!")
        break

    if attempts == 0:
        print("Sorry, you have run out of guesses!")
        break
    elif guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
