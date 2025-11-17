def sum_eo(n, t):
    if n <= 0 or t not in ['e','o']:
        return -1

    if t == 'e':
        # sum of even natural numbers
        return sum([i for i in range(0, n, 2)])
    else:
        # sum of odd natural numbers
        return sum([i for i in range(1, n, 2)])


print(sum_eo(10,'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
print(sum_eo(0,'e'))
print(sum_eo(-1,'e'))
print(sum_eo(11,''))
