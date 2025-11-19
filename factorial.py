def factorial(number: int) -> int:
    """
    Returns the factorial of the given number.
    """
    if number == 0:
        return 1

    product = 1
    for i in range(1, number + 1):
        product *= i

    return product

for i in range(36):
    print(i, factorial(i))
