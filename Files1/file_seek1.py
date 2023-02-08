f = open('file_test1','r')
f.seek(4)
print(f.readline())
f.close()