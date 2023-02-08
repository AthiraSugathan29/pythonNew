# For loop
# n = int(input("Enter a number : "))
# f = 1
# for i in range(1,n+1):
#     f = f * i
# print("Factorial : ",f)

# While Loop
# n = int(input("Enter a number : "))
# f = 1
# i = 1
# while i <= n:
#     f = f * i
#     i = i + 1
# print("Factorial : ",f)

def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n-1)
n = int(input("Enter the number :"))
print("Factorial : ",rec(n))