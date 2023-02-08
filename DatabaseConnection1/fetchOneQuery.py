import pymysql
id = int(input("Enter Id : "))
db = pymysql.connect(host='localhost',user='root',password='Pass123',database='nov_test')
con = db.cursor()
query = "select * from t2 where id = %d"%(id)
con.execute(query)
i = con.fetchone()
id1 = i[0]
addr = i[1]
em = i[2]
print(f"Id : {id1},Address = {addr},Email = {em}")