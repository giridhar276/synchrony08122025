

#import pymssql      for sqlserver
#import cx_Oracle    for oracle database
import pymysql 
import csv
#step1
conn = pymysql.connect(host="localhost",port=3306,user='root',password='rps12345',)
print(conn)

#step2
cursor = conn.cursor()

#obj = open(filename, mode)
fobj = open("empinfo.csv","r") 
reader = csv.reader(fobj)
for record in reader:
    workclass = record[1]
    education = record[3]
    query = "insert into empdb.employee values('{}','{}')".format(workclass,education)
    #step3
    cursor.execute(query)

print("all the records were inserted")
#step5
fobj.close()
conn.commit()
conn.close()


# in mysql :
select count(*) from employee;