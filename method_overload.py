class Student:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

# Create an instance
obj = Student()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Shrutika')

