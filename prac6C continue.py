# Practical 6b:program for print table using continue

n=int(input("Enter any no to print table:"))
result=0

print("The multiplication table of :",n)
for i in range(1,11):
    result=n*i
    if(i==5):
        continue
    print(result)
    
          
