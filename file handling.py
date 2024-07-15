# Python code to create a file
file = open('file.txt','w')
file.write("""Python too supports file handling and allows users to handle files i.e.,to read and write files, along with many other file handling options, to operate on files.""")
file.close()

# a file named "file", will be opened with the reading mode.
file = open('file.txt', 'r')
# This will print every line one by one in the file for each in file:
for each in file:
    print (each)
file.close()
