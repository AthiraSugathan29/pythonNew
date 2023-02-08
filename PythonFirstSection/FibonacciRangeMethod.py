# To print fibonacci series with range method in for loop.
n = int(input("Enter the limit : "))
a,b = 0,1
print("Fibonacci Series")
print(a)
print(b)
for i in range(2,n):
    fib = a + b
    print(fib)
    a,b = b,fib
