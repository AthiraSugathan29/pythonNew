import pymysql
db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
con = db.cursor()
query = "select * from t2"
con.execute(query)
data = con.fetchall()
for i in data:
    id = i[0]
    addr = i[1]
    em = i[2]
    print(f"Id : {id}, Address = {addr}, Email = {em}")
