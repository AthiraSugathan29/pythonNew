# Class & Object
class Emp:
    x = 100
    def display(self):
        print("Simple function")
    def disp():
        print("Without self argument")
    def sum1(self,a,b):
        print("Sum : ",a+b)
    def product(arg,a,b):
        print("Product : ",a*b)
obj = Emp()
obj.display()
obj.sum1(30,40)
obj.product(5,10)
print("Value of x : ",obj.x)
obj2 = Emp
obj2.disp()
