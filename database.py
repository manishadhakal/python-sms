import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("CREATE TABLE student(id int,name text,roll_no int,task text) ")
conn.commit()