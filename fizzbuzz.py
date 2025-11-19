def fizz_buzz(number: int) -> str:
    """
    Returns a string for the provided number,
    as per the fizz buzz game rules.

    :return: "fizz" if the number is divisible by 3,
        "buzz" if the number is divisible by 5,
        "fizz buzz" if the number is divisible by both 5 & 3 and
        the number itself, otherwise.
    """
    result = ""
    if number % 3 == 0:
        result = "fizz"

    if number % 5 == 0:
        result += " buzz" if len(result) > 0 else "buzz"

    return result if len(result) > 0 else str(number)


def verify_input(number: int, input_string: str) -> (bool, str):
    """
    Returns a tuple containing a bool value, indicating right or wrong
     answer and the correct answer
    :param number: The number used to calculate the fizz buzz result
    :param input_string: A number, "fizz", "buzz" or "fizz buzz"
    :return A tuple containing a bool value - True if the `input_string` is
        the correct answer and False otherwise,
        and the expected fizz buzz result
    """
    result = fizz_buzz(number)
    return input_string == result, result


input("Play Fizz Buzz. Press Enter to start")
print()

game_number = 1
while game_number < 101:
    if game_number % 2 == 1:
        # calculate computer's input
        computer_says = fizz_buzz(game_number)
        # computer says
        print("Computer says {}".format(computer_says))
    else:
        # ask user input
        user_input = input("Your turn: ")
        print()
        right, correct_answer = verify_input(game_number, user_input)
        if not right:
            print("You lose, the correct answer was {}".format(correct_answer))
            break

    game_number += 1
else:
    print("Congratulations! you've reached the end of the game.")
