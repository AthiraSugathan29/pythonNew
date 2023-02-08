f = open('file_test1','r')
f.readline()
pos = f.tell()
f.close()
print("Position : ",pos)

