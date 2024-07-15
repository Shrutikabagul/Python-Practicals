#program 5c :Write a program to print table of 11,12,13,14,15 with nested loop

result=0

for j in range(1,11):
    for i in range(11,16):
        
        result=i*j 
        print(result,end='\t')
    print()
    
