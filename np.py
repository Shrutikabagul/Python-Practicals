import numpy as np 
A=np.array([[1,2],[3,4]]) 
B=np.array([[4,5],[6,7]]) 
print("A matrix: \n",A)
print("B matrix: \n",B) 
 
result=[[0,0],[0,0]]
result=np.add(A,B) 
print("Addition of matrices is: \n",result) 
 
result=np.subtract(A,B)
print("Subtraction of matrices is: \n",result) 
