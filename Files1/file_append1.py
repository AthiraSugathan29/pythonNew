f = open('file_test1','a') # To append content at the end of the file,open the file using append mode and use write() method.
f.write("Python is a OOP")
f.close()

f = open('file_test1','r') # To display the content of file,again open the file in read mode and print the content using read() method or for loop.
print(f.read())
f.close()