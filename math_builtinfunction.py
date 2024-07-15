import math
while True:  
    print("\nMENU")  
    print("1. Calculate Factorial")  
    print("2. Calculate Log")
    print("3. Calculate Power of given no")
    print("4. Exit")  
    ch = int(input("Enter the Choice:"))  
    if ch == 1:
        n = int(input("Enter number to calculate Factorial : "))
        print("Factorial of ", n , "is : ", math.factorial(n), "\n\n")
              
    elif ch == 2:
        n=int(input("Input a number to compute the Log : "))
        print(math.log(n))
            
    elif ch == 3:
        b = int(input("Enter Base value to calculate Power : "))
        n = int(input("Enter Exponent value to calculate Power : "))
        print("Power of base ", b, " ", n, "is : ", math.pow(b, n), "\n\n")
            
    elif ch == 4:
        break  
              
    else:  
        print("Oops! Incorrect Choice.")  
      
    
