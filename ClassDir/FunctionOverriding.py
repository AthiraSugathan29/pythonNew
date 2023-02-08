class Rectangle:
    def Area(self,l,b):
        print("Area of rectangle : ",l*b)
class Square(Rectangle):
    def Area(self,l,b):
        print("Area of square : ",l*b)
obj = Square()
obj.Area(10,20)