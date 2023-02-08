# WAP to find factorial of a number using function with return type and function parameter.
def fact(num):
    fac = 1
    for i in range(1,num+1):
        fac = fac * i
    return fac
n = int(input("Enter the number : "))
f = fact(n)
print(f"Factorial of {n} : {f}")