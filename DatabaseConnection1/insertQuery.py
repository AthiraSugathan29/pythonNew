# import pymysql
# db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
# con = db.cursor()
# sqlquery = 'insert into t2 values(%s,%s,%s)'
# val = (13,'Pathanamthitta','test13@gmail.com')
# con.execute(sqlquery,val)
# db.commit()
# print("Inserted")

# Connection - Insert values using user input
import pymysql
id = int(input("Enter Id :"))
address = input("Enter Address : ")
email = input("Enter Email : ")
db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
con = db.cursor()
sqlquery = "insert into t2 values(%s,%s,%s)"
val = (id,address,email)
con.execute(sqlquery,val)
db.commit()
print("Inserted")
