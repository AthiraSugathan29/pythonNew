ls = []
def create():
    n = int(input("Enter the limit : "))
    for i in range(n):
        val = int(input())
        ls.append(val)
    print("List : ",ls)

def search():
    ele = int(input("Enter the element to be searched : "))
    if ele in ls:
        print("Element Found")
    else:
        print("Element Not Found")
def Remove():
    item = int(input("Enter the item to be removed : "))
    if item in ls:
        ls.remove(item)
        print("List after remove item : ",ls)
    else:
        print("Item not found in the list")

def Replace():
    old = int(input("Enter the item to be replaced : "))
    new = int(input("Enter the item to be added: "))
    for i in range(len(ls)):
        if ls[i] == old:
            ls[i] = new
    print("List after replace item : ", ls)

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
