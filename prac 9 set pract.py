# Practical 9 program for set operations
i=1
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("sets are:")
print(A)
print(B)

print("After Adding elements in set A")
A.add(10)
A.add(11)
print(A)

print("After Adding elements in set B")
B.add(12)
B.add(13)
print(B)

print("After discarding elements from set A")
A.discard(1)
A.discard(5)
print(A)

print("Using pop method in set A")
A.pop()
print(A)

while i==1:
    
    
    print("\n1.Set Union\n2.Set Intersection\n3.Set Difference")
    ch=int(input("Enter your Choice :"))
    if(ch==1):
        print("\nUnion of sets :")
        print(A | B)

    elif(ch==2):
         print("\nIntersection of sets :")
         print(A & B)

    elif(ch==3):
        print("\nDifference of sets :")
        print(A - B)

    else:
        print("Invalid Choice!!")
    i=int(input("Do you want to continue on set operations then press 1..."))
    


                   

        
       
           
