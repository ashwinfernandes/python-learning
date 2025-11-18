def multiply(x, y):
    """
    Multiplies two items and returns the result.
    :param x: The multiplicand.
    :param y: The multiplier.
    :return: The product after multiplying the two items.
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Verifies whether the provided string is a palindrome or not.

    A palindrome is a string that reads the same forwards as backwards.

    The function is case-insensitive.

    :param string: The string to be verified.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(sentence):
    """
    Verifies whether the provided sentence is a palindrome or not.

    The sentence can be combination of alphanumeric characters.

    The function ignores whitespace, capitalization and
    punctuation in the sentence.

    :param sentence: The sentence to be verified.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    palindrome_sentence = "".join([char if char.isalnum() else '' for char in sentence.casefold()])
    return is_palindrome(palindrome_sentence)

sentence = input("Please enter a sentence to check: ")
if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))
