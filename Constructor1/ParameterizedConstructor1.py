# Parameterized Constructor
class A:
    def __init__(self,name):
        print("Parameterized Constructor")
        self.na = name
    def display(self):
        print("Name : ",self.na)
obj = A("Anu")
obj.display()