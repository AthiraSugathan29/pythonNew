# import pymysql
# ch = input("Do you want to update(yes/no) :")
# if ch == 'yes':
#     id = int(input("Enter the id : "))
#     name = input("Enter the name : ")
#     ag = int(input("Enter the age : "))
#     db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
#     con = db.cursor()
#     query = "update t1 set Name='%s',Age=%d where Id = %d"%(name,ag,id)
#     con.execute(query)
#     db.commit()
#     print("Updated successfully")
# else:
#     print("Exit")

import pymysql
ch = input("Do you want to update(yes/no) :")
if ch == 'yes':
    id = int(input("Enter the id : "))
    addr = input("Enter the address : ")
    em = input("Enter the email : ")
    db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
    con = db.cursor()
    query = "update t2 set Address='%s',Email='%s' where Id = %d"%(addr,em,id)
    con.execute(query)
    db.commit()
    print("Updated successfully")
else:
    print("Exit")
