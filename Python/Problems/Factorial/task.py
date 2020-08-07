num = int(input())
i, factorial = 1, 1

while i <= num:
    factorial *= i
    i += 1
print(factorial)
