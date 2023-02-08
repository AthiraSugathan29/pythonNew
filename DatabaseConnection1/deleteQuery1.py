import pymysql
id = int(input("Enter ID: "))
db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
con = db.cursor()
query = "delete from t2 where id=%d"%(id)
con.execute(query)
db.commit()
print("Delete Successfully")