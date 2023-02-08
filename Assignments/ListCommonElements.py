# 3. Check if two lists have common elements.
l1 = [10,20,30,40,50]
l2 = [11,20,30,45,50,53]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
if len(l3) == 0:
    print("No common Elements")
else:
    print("Common Elements : ",l3)
