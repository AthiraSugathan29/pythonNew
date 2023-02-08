n = int(input("Enter a number : "))
num = n
arm = 0
num_len = len(str(num))
while num > 0:
    digit = num % 10
    arm = arm + digit ** num_len
    num = num // 10
if n == arm:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")