# Method-1
# str1 = input("Enter the string : ")
# rev = str1[::-1]
# print(rev)

# Method-2
# rev = ""
# for i in str1:
#     rev = i + rev
# print(rev)

# Method-3 - Recursion
# def rev(n):
#     if len(n) == 1:
#         return n
#     else:
#         return rev(n[1:]) + n[0] # bcde + a, cde + b + a, de + c + b + a,e + d + c + b + a => edcba
# str1 = input("Enter a string : ")
# re = rev(str1)
# print("Reversed string : ",re)

# Method-4 - Using reversed()
# def rev(n):
#     r = "".join(reversed(n))
#     return r
# str1 = input("Enter a string : ")
# print(rev(str1))

# Method-5 - List Comprehension
# def rev(str1):
#     ls = [str1[i] for i in range(len(str1)-1,-1,-1)]
#     rev1 = "".join(ls)
#     return rev1
# str1 = input("Enter a string : ")
# print("Reverse of the string : ",rev(str1))

# Method-5 - Using List
def rev(str1):
    ls = list(str1)
    ls.reverse()
    return "".join(ls)
st = input("Enter a string : ")
print(rev(st))
