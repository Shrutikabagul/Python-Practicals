class A:
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")

class B(A):
    def feature3(self):
        print("Feature3 is working")
    def feature4(self):
        print("Feature4 is working")

a1=A();
a1.feature1()
a1.feature2()


b1=B();
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

        
