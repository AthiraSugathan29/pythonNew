#Break
l = [10,20,30,100,70,80]
for i in l:
    print(i)
    if i == 100:
        break

# Continue
for i in l:
    if i == 100:
        continue
    print(i)