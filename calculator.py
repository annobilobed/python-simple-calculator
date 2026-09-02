num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

operator = input("enter an operator (+, -, *, /, %):")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")