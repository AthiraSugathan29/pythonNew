# Palindrome
n = int(input("Enter the number : "))
rev = 0
num = n
while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num = num // 10
if n == rev:
    print(f"{n} is Palindrome")
else:
    print("%d is not Palindrome"%(n))

# str1 = input("Enter the string : ")
# str_rev = ""
# for i in str1:
#     str_rev = i + str_rev
# if str_rev == str1:
#     print(f"{str1} is Palindrome")
# else:
#     print(f"{str1} is not Palindrome")