n = int(input("Enter the number : "))
if n == 1:
    print("Not defined")
else:
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print(f"{n} is Prime")
    else:
        print(f"{n} is not Prime")