class Emp:
    def read(self,a,b):
        self.x = a # a is the passing variable & x is the variable in the function
        self.y = b # b is the passing variable & y is the variable in the function
    def sum(self):
        s = self.x + self.y
        print("Sum : ",s)
    def product(se):
        p = se.x * se.y
        print("Product : ",p)

obj = Emp()
obj.read(10,20)
obj.sum()
obj.product()

