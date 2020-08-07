numbers = []

while True:
    x = input()
    if x != '.':  # input x while x is not '.'
        numbers.append(float(x))  # and add x to the end of the list
    else:
        break

# Prints the Min
print(min(numbers))
