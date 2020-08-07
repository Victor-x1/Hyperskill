# Add absolute value of [(a,b,c) + modulus(a,b,c)]
# If modulus %2 is 0;even; adds 0
# If modulus % 2 is 1;odd; adds 1

# Get Input for a,b,c
a, b, c = (int(input()) for i in range(3))

# Add a,b,c
add = (a + b + c)

# Find |Modulus| of a,b,c
modulus = (abs(a % 2)) + (abs(b % 2)) + (abs(c % 2))

# Add + |Modulus| Divided by Integer Division
desks = ((add + modulus) // 2)
print(desks)
