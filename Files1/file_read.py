f = open('file_test1','r')
#print(f.read())
#print(f.read(8)) # Print first 8 characters
# print(f.readline()) # Read file content line by line
#print(f.readline())
for i in f: # To read file content line by line using for loop
    print(i)
f.close()