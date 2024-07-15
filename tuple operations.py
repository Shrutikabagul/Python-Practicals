#prac 8a: accessing tuple elements

#1: using indexing

t1 = ('A','B','C','D','E')

print("INDEXING")
print("Given tuple1 is: " ,t1)

print("Tuple element at t1[0]: " ,t1[0]) 
print("Tuple element at t1[3]: " ,t1[3]) 

#2: using negative indexing

t2 = ('H','A','P','P','Y')

print("\n\nNEGATIVE INDEXING")
print("Given tuple2 is: " ,t2)

print("Tuple element at t1[-1]: " ,t2[-1]) 
print("Tuple element at t1[-4]: " ,t2[-4]) 

#3: using slicing

t3 = ("S","H","R","U","T","I","K","A")

print("\n\nSLICING")
print("Given tuple3 is: " ,t3)

print("Tuple elements t3[0:2]: " ,t3[0:3])
print("Tuple elements t3[:-4]: " ,t3[:-4])
print("Tuple elements t3[0:4]: " ,t3[7:])
print("Tuple elements t3[:]: " ,t3[:])

#4:Deleting tuples

t4 = ('p', 'y', 't', 'h', 'o', 'n')
del t4
print(t4)

