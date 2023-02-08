# Destructor
class A:
    def __init__(self,name): # Constructor
        print("Constructor")
        self.na = name
    def display(self):
        print("Name : ",self.na)
    def __del__(self): # Destructor
        print("Destructor")
obj = A("Ram")
obj.display()
del obj # Destructor deletes the object