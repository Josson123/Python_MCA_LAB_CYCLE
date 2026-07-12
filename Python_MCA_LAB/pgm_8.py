try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Result =", result)    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer values.")
except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program execution completed.")