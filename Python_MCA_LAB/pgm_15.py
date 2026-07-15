import calc

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("MENU\n1.Addition\n2.Subtraction\n3.Multitplication\n4.Division\n")
ch=int(input("Enter your choice:"))

match ch:
    case 1:
        print("Addition =", calc.add(a, b))
    case 2:    
        print("Subtraction =", calc.sub(a, b))
    case 3:    
        print("Multiplication =", calc.mul(a, b))
    case 4:    
        print("Division =", calc.div(a, b))
    case _:
        print("Enter a valid input.")    