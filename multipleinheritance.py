class A:
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")

class B:
    def feature3(self):
        print("Feature3 is working")
    def feature4(self):
        print("Feature4 is working")

class C(A,B):
    def feature5(self):
        print("Feature5 is working")
   
a1=A()


b1=B()


c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
