# # Add 5 to each elements of a list
# oldlist = [1,2,3,4]
# newlist = [x+5 for x in oldlist]
# print(newlist)
#
# # Even numbers upto 25
# lst = [x for x in range(25) if x%2 == 0]
# print(lst)
#
# str1 = 'programming'
# lst = [x for x in str1 if x in ['a','e','i','o','u']]
# print(lst)
#
# str2 = input("Enter a string : ")
# words = str2.split()
# print(words)
# lst = [x[0] for x in words]
# print(lst)

# # Print elements contains 'e' letter
# str1 = ['red','white','green','pink']
# lst = [x for x in str1 if 'e' in x]
# print(lst)

# # Print elements that are not 'green'
# str1 = ['red','white','green','pink']
# lst = [x for x in str1 if x != 'green']
# print(lst)
#
# # Convert elements to upper case
# str1 = ['red','white','green','pink']
# lst = [x.upper() for x in str1]
# print(lst)

# # Convert elements to upper case
# str1 = ['red','white','green','pink']
# lst = ['hello' for x in str1]
# print(lst)

# Print all elements except 'pink' and display 'blue' instead of 'pink'
str1 = ['red','white','green','pink']
lst = [x if x != 'pink' else 'blue' for x in str1]
print(lst)