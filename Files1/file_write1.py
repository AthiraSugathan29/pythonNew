f = open('file_test1','w') # To write any content in file,open file using write mode and use write() method.
f.write('Hello Python') # If the file exist,overwrite the content
f.close()

f = open('file_test1','r')
for i in f:
    print(i)
f.close()