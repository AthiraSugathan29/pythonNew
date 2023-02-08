# Single Inheritance

class A:
    def displayA(self):
        print("Base Class Method")
class B(A):
    def displayB(self):
        print("Derive Class Method")

ob = B()
ob.displayA()
ob.displayB()