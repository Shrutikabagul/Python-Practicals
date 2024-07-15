#creating a dictionary
my_dict = {'name': 'Shrutika Bagul', 'age': 18,'enroll no': 1906007}
print("Printing the Dictionary:",my_dict)
print(my_dict['name'])
print(my_dict.get('age'))

# update value
print("Updating values in Dictionary:")
my_dict['age'] = 19
print(my_dict)

# add item
print("\nAdding values in Dictionary:")
my_dict['address'] = 'Dhayri Pune'
print(my_dict)

#printing keys using key function
keys = my_dict.keys()
print("\nprinting keys using key function",keys)

# Removing elements from a dictionary
print("\nRemoving element using pop method") 
print(my_dict.pop('age'))
print("\nAfter using pop method :");      
print(my_dict)

# remove an arbitrary item, return (key,value)
print(my_dict.popitem())
print("\nRemoving element using popitem method") 
print(my_dict)


#remove all items
print("\nRemoving all elements in dictionary using clear method") 
my_dict.clear()
print(my_dict)

#deleting the dictionary
del my_dict
print(my_dict)





