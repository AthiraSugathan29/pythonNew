# Function overloading is a class containing different functions
# with same function name and different signatures(number,order and type of arguments).
# But python doesnot support function overloading because it doesnot support compile time.
# So we can use the concept indirectly by the following way.
class A:
    def display(self,name = None):
        if name is None:
            print("Hello")
        else:
            print("Hello",name)

ob = A()
ob.display()
ob.display('Anu')