# To find factorial of a number using class with function arguments and return.
# class Factorial:
#     def fact(self,num):
#         f = 1
#         for i in range(1,num+1):
#             f = f * i
#         return f
#
# obj = Factorial()
# n = int(input("Enter the number : "))
# print(f"Factorial of {n} : {obj.fact(n)}")

class Factorial:
    def fact(self,num):
        if num == 1:
            return 1
        else:
            #return num * self.fact(num-1)
            return num * Factorial.fact(self,num-1)

obj = Factorial()
n = int(input("Enter the number : "))
print(f"Factorial of {n} : {obj.fact(n)}")