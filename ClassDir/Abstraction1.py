from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("Non-abstract Method")
class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")
t = Triangle()
t.sides()
t.display()