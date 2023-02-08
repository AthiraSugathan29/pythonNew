# Normal string to dictionary
# str = 'cat rat mat cat pat rat cat sat cat sat'
# lst = str.split()
# dict1 = {}
# for i in lst:
#     if i in dict1:
#         dict1[i] = dict1[i]+1
#     else:
#         dict1[i] = 1
# print(dict1)


# File content to dictionary
f = open("file_test1",'r')
dict1 = {}
for i in f:
    lst = i.split()
    for j in lst:
        if j in dict1:
            dict1[j] = dict1[j]+1
        else:
            dict1[j] = 1
print(dict1)
