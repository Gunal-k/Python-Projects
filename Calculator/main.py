#python calculator

operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{operator} is invalid")