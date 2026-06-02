# Simple Calculator
import math
print("=" * 40)     # print(=======================================)
print("Python Calculator Simulator")
print("=" * 40)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("=" * 40)

ch = int(input("Enter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if ch == 1:
    print("Result =", num1 + num2)
elif ch == 2:
    print("Result =", num1 - num2)
elif ch == 3:
    print("Result =", num1 * num2)
elif ch == 4:
    print("Result =", num1 / num2)
else:
    print("Invalid choice")


