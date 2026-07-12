def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=i*fact
    print("The factorial of ",num,"is ",fact) 
    

num=int(input("Enter a number to find factorial:"))
fact(num)      
    