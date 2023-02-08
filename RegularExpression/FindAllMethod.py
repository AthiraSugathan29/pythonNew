# Regular Expression Method - findall()
import re
str1 = 'Rose is a beautiful and colorful flower'
res = re.findall('ful',str1)
print(res)
res2 = re.findall('full',str1)
print(res2)

s = 'cat mat pat rat sat'
res3 = re.findall('[sc]',s) # Checking each string starting with s and c and returns the matching character list
print(res3)