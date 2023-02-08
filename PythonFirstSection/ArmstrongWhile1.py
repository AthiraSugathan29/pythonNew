# Armstrong Number
n = int(input("Enter the number : "))
num = n
num_len = len(str(n))
arm = 0
while num > 0:
    digit = num % 10
    arm = arm + digit ** num_len
    num = num // 10
if n == arm:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")


