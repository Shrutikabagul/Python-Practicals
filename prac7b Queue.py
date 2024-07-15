#program for Queue and DeQue
i=1

List=[]
lst=[]
while i==1:
    print("1.Queue")
    print("2.DeQueue")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        while i==1:
            print("1.ADD element\n2.Remove element\n3.Display")
            ch=int(input("Enter your Choice"))
            if(ch==1):
                val=int(input("Enter number to add in Queue :"))
                lst.append(val)
                print(lst)
            elif(ch==2):
                if lst!=[]:
                    del(lst[0])
                print(lst)
            elif(ch==3):
                print(lst)
            else:
                print("Invalid choice")
            i=int(input("Do you want to operate on Queue then press 1..."))

    elif ch==2:
        while i==1:
            
            print("\n1.ADD element in front\n2.Add element in Rear\n3.Remove element from front\n4Remove element from rear")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                   no=int(input("Enter number to add element at front of DeQueue"))
                   List.insert(0,no)
                   print(List)
            elif(ch==2):
                    no=int(input("Enter element to add element at reae of DeQueue"))
                    List.append(no)
                    print(List)
            elif(ch==3):
                     List.pop(0)
                     print(List)
            elif(ch==4):
                    List.pop()
                    print(List)

            else:
                print("Invalid Choice")
            i=int(input("Do you want to continue on DeQueue press 1:"))
            
    else:
       print("Invalid choice")
    i=int(input("Do you want to continue press 1:")) 

                
            
             
               
           
