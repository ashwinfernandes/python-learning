int_string = input('Please enter three numbers separated by commas')
a = b = c = 0
numbers = []
for number in int_string.split(','):
    numbers.append(int(number))

a = numbers[0] if len(numbers) > 0 else 0
b = numbers[1] if len(numbers) > 1 else 0
c = numbers[2] if len(numbers) > 2 else 0

print("a + b - c = {}".format(a + b - c))
