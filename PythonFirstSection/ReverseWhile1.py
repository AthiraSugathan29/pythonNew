# Reverse of a number using while
n = int(input("Enter the number : "))
rev = 0
p = 1
s = 0
while n > 0:
    r = n % 10
    rev = rev*10 + r
    p = p * r
    s = s + r
    n = n // 10
print("Reverse : ",rev)
print("Product : ",p)
print("Sum : ",s)