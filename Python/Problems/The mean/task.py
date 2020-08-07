# Python Statistics Function
import statistics

numbers = []

while True:
    x = input()
    if x != '.':  # input x while x is not '.'
        numbers.append(int(x))  # and add x to the end of the list
    else:
        break

# Prints the Mean
print(statistics.mean(numbers))
