# def stud(st1,st2,st3):
#     print("First : ",st1)
#     print("Second : ", st2)
#     print("Third : ", st3)
#
# stud(st2='Anu',st3='Shilpa',st1='Athira')

# def stud(**st):
#     for i,j in st.items():
#         print("%s => %s"%(i,j))
#
# stud(st2='Anu',st3='Shilpa',st1='Athira')

def stud(x,*args,**kwargs):
    print("Simple Argument : ",x)
    print("Arbitrary Argument : ")
    for i in args:
        print(i)
    print("Keyword Arguments : ")
    for i,j in kwargs.items():
        print("%s => %s"%(i,j))

stud('Jiya','Ram','Sneha','Sanu',st2='Anu',st3='Shilpa',st1='Athira')
