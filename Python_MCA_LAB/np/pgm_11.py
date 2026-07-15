i=1
while i==1:
    print("MENU\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter second number:"))
    ch=int(input("Enter your choice:"))
    match ch:
        case 1:
            result=num1+num2
            print("Result=",result)
            exit
        case 2:
            result=num1-num2
            print("Result=",result) 
            exit 
        case 3:
            result=num1*num2
            print("Result=",result)
            exit      
        case 4:
            result=num1/num2
            print("Result=",result)
            exit
        case _:
            print("Enter valid input")  
    con=input("Do you need to continue?(Y/N):")
    if con=='Y' or con=="y":
        continue
    if con=='N' or con=='n':
        print("\n\nExiting...")
        i=i+1
