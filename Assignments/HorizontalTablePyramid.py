# 2. Horizontal Number Table Pyramid
# 1
# 2 4
# 3 6 9
# 4 8 12 16

rows = int(input("Enter the rows : "))
for i in range(1,rows+1): # Rows
    for j in range(1,i+1): # Columns
        print(i * j,end=" ")
    print()
