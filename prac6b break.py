# Practical 6a:program for print table using break

n=int(input("Enter any no to print table:"))
result=0

print("The multiplication table of :",n)
for i in range(1,11):
    result=n*i
    if(i==8):
        break
    print(result)
    
          
