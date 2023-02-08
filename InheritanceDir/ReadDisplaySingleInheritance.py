class A:
    def read(self):
        print("Base class Method")
        self.x = int(input("Enter x : "))
        self.y = int(input("Enter y : "))
class B(A):
    def display(self):
        print("Derive class Method")
        print("Sum : ",self.x+self.y)
obj = B()
obj.read()
obj.display()