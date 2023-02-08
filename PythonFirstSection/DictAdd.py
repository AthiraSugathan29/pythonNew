#Add items to dictionary
n = int(input("Enter the limit : "))
dict1 = {}
for i in range(n):
    key = int(input("Enter the key : "))
    val = input("Enter the value : ")
    dict1.update({key:val})
print("Dictionary : ",dict1)

# dict2 = {101:'yellow',102:'red'}
# for i in dict2.values():
#     print(i)

# for i in dict2.keys():
#     print(i)

# for i,j in dict2.items():
#     print(i,j)
#
# x = dict2.get(102)
# print(x)