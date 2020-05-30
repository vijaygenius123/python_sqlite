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

c.execute("""SELECT *  FROM customers""")

print(c.fetchone())
#print(c.fetchmany(2))
#print(c.fetchall())

conn.commit()