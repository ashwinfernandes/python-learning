LOW = 1
HIGH = 1000 # needs at most x guesses to guess the right value,
# where x is the binary exponent that results in the exact high value
# or is the next higher exponent
# e.g. high value of 512 would require at most 2^9 guesses
# high value of 513 would require at most 2^10 guesses

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2

        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        elif guess == answer:
            return guesses

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times. Max {} guesses."
      .format(correct_count, max_guesses))
