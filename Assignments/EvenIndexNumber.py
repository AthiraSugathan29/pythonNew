# 1. Write a program to print characters from a string that are present at an even index number.
str1 = input("Enter the string : ")
print("Given String is",str1)
print("Characters at even index number")
for i in range(0,len(str1),2):
    print(str1[i])