n = int(input("Enter the number : "))
count = 0
if n == 1:
    print("Not defined")
else:
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")