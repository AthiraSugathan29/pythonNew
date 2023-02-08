class A:
    def read(self):
        self.x = int(input("Enter x : "))
        self.y = int(input("Enter y : "))
class B(A):
    def sum(self):
        self.sum1 = self.x + self.y
        print("Sum : ",self.sum1)
class C(B):
    def average(self):
        avg = self.sum1 / 2
        print("Average : ",avg)
obj = C()
obj.read()
obj.sum()
obj.average()