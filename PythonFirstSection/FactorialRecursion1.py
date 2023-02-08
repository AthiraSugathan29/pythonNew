def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
n = int(input("Enter the number : "))
f = fact(n)
print(f"Factorial of {n} : {f}")