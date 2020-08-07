initial = (float(input()))

year = 0
PROTECTION = 700000

while initial < PROTECTION:
    year = year + 1
    initial = initial * 1.071
print(year)

