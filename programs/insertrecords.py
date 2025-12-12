
#import pymssql      for sqlserver
#import cx_Oracle    for oracle database
import pymysql 
#step1
conn = pymysql.connect(host="localhost",port=3306,user='root',password='rps12345',)
print(conn)

#step2
cursor = conn.cursor()
query = "select * from empdb.employee"

#step3
cursor.execute(query)

#step4
for record in cursor.fetchall():
    print(record)

#step5
conn.close()

