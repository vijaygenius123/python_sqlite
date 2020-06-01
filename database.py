import sqlite3


conn = sqlite3.connect("customers")

c = conn.cursor()


#c.execute("""CREATE TABLE customers (
#    first_name  text,
#    last_name text,
#    email  text
#)
#""")

#c.execute("""INSERT INTO customers 
#    (first_name, last_name, email) 
#    VALUES ("Vijay","S","vijaygenius123@gmail.com")
#""")

#data = [
#    ('Swathi','GV','swathi@gmail.com'),
#    ('John','Doe','john@gmail.com'),
#    ('Jane','Doe','jane@gmail.com')
#]

#c.executemany("""INSERT INTO customers VALUES (?,?,?)""",data)

#c.execute("""UPDATE customers SET last_name = 'Sundararaman'
#    WHERE rowid = 1
#""")
c.execute("""DELETE from customers WHERE rowid = 4""")

conn.commit()

#print(c.fetchone())
#print(c.fetchmany(2))

c.execute("""SELECT rowid, *  FROM customers""")

items = c.fetchall()

for item in items:
    print("Row ID:{}\tFirst Name:{}\tLast Name:{}\tEmail:{}".format(item[0],item[1],item[2],item[3]))
conn.commit()