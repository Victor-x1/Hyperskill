prime_numbers = [n for n in range(2, 1000)
                 if all(n % y != 0 for y in range(2, n))]
