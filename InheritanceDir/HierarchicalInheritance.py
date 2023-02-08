# Hierarchical Inheritance
class A:
    def read(self):
        self.x = int(input("Enter x : "))
        self.y = int(input("Enter y : "))


class B(A):
    def sum(self):
        print("Sum : ", self.x + self.y)


class C(A):
    def average(self):
        print("Average : ", (self.x + self.y) / 2)


class D(A):
    def product(self):
        print("Product : ", self.x * self.y)


objB = B()
objB.read()
objB.sum()

objC = C()
objC.read()
objC.average()

objD = D()
objD.read()
objD.product()
