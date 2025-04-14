# Adds two numbers
def add(num1, num2):
    return num1 + num2

# Subtracts num2 from num1
def subtract(num1, num2):
    return num1 - num2

# Multiplies two numbers
def multiply(num1, num2):
    return num1 * num2

# Divides num1 by num2, checks for zero division
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed"
    return num1 / num2
    
#-----main-----

num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == '+':
    print("num1 + num2 =", add(num1, num2))
elif op == '-':
    print("num1 - num2 =", subtract(num1, num2))
elif op == '*':
    print("num1 * num2 =", multiply(num1, num2))
elif op == '/':
    print("num1 / num2 =", divide(num1, num2))
else:
    print("Invalid operator")
