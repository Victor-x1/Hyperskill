atoms, quantity = (int(input()) for i in range(2))
# N == atoms, R == Quantity, T == half_life
half_life = 0
while quantity < atoms:
    half_life += 12
    quantity += 1
    atoms /= 2
print(half_life)
