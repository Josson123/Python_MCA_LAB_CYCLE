try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Program executed.Rerun the code.")