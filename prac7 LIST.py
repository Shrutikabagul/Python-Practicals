#prac 7 :Write Python program to perform operations on list
i=1
lst=[1,2,3,4,5]
print("The list is: ",lst)

while i==1:
    print("1.insert")
    print("2.Delete")
    
    ch=int(input("Enter your Choice"))
    if(ch==1):
    
            
            p=int(input("Enter position to be insert in alist: "))
            n=int(input("Enter a no to insert in a list :"))
            lst.insert(p,n)
            print("\nList after performing Insert Operation: ")
            print(lst)
          
                

    elif(ch==2):
            
                
                p1=int(input("Enter a no to delete from list: "))
                lst.remove(p1)
                print("\nList after performing delete Operation: ")
                print(lst)

    else:
        
        print("Invalid choice!!")
                  
        i=int(input("Do you want to continue press 1:"))

        

        
        
