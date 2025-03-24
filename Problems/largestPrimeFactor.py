number = 2#int(input("Enter Prime Number: "))

factors = [x for x in range(1, int(number/2+1)) if number % x == 0]
factors = [x for x in factors if (x % 2 != 0 and x % 3 != 0 and x % 5 != 0) or (x in [2, 3, 5])]

print("Highest Prime Factor:", max(factors))

primes = [x for x in range(1, number+1, 2) if x % 3 != 0 and x % 5 != 0 and x % 7 != 0 or (x in [3, 5, 7])]

for x in primes:
    if x != 1:
        for y in primes:
            if y % x == 0:
                primes.remove(y)

print("Highest Prime Number:", max(primes))