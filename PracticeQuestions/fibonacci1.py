n = int(input("Enter the limit : "))
a,b = 0,1
print("Fibonacci Series : ")
print(a)
print(b)
for i in range(2,n):
    f = a + b
    a,b = b,f
    print(f)