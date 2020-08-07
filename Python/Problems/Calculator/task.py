first, second = (float(input()) for i in range(2))
operand = input()

if operand == "+":
    calc = first + second
elif operand == "-":
    calc = first - second
elif operand == "pow":
    calc = first ** second
elif operand == "*":
    calc = first * second

# Division by Zero " /, mod, div "
elif operand == "/":
    calc = "Division by 0!" if second == 0 else first / second

elif operand == "mod":
    calc = "Division by 0!" if second == 0 else first % second

elif operand == "div":
    calc = "Division by 0!" if second == 0 else first // second

print(calc)
