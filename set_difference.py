from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print("evens", evens)
print("odds", odds)

primes = set(primes_generator(100))
print("primes", primes)
squares = set(squares_generator(100))
print("squares", squares)

print("odds - primes", odds.difference(primes))
print("odds - primes", odds - primes)

print("primes - odds", primes - odds)
