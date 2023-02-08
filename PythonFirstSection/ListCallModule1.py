# import  ListModule1
from ListModule1 import *
while True:
    opt = int(input("1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice : "))
    if opt == 1:
        create()
    elif opt == 2:
        search()
    elif opt == 3:
        Remove()
    elif opt == 4:
        Replace()
    else:
        break