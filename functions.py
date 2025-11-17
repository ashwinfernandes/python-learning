def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(string):
    palindrome_sentence = "".join([char if char.isalnum() else '' for char in string.casefold()])
    return palindrome_sentence[::-1] == palindrome_sentence


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

sentence = input("Please enter a sentence to check: ")
if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))
