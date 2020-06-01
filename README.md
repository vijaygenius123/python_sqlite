# SQLite With Python

SQLite is a default python package can be be imported using the below statement

```python
import sqlite3
```
You can connect to a existing sqlite3 database or create a new one by using the connect() method. Since sqlite3 is a file you will need to pass the path of the file , incase the file does not exist the module will create a new file in the path

```
conn  = sqlite3.connect("customers")
```


## Data Types In Sqlite3

Sqlite3 only supports 5 data types. It is easy to remember
1. NULL 
2. INTEGER
3. REAL  (Decimal)
4. TEXT
5. BLOB 

```python

c = conn.cursor()
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)
""")
conn.commit()
```

To run the query you will need to run commit method on the connection.


## Inserting Data

```python
c.execute("""INSERT INTO customers 
    (first_name, last_name, email) 
    VALUES ("Vijay","S","vijaygenius123@gmail.com")
""")
conn.commit()
```

for bulk insert
```python
data = [
    ('User','1','user1@gmail.com'),
    ('User','2','user2@gmail.com'),
    ('User','3','user3gmail.com')
]

c.executemany("""INSERT INTO customers VALUES (?,?,?)""",data)

conn.commit()
```

## Retreiving Data

```python
c.execute("""SELECT *  FROM customers""")

print(c.fetchone())

```

There are three methods to fetch the data

1. fetchone() returns one row
2. fetchmany(x) returns x number of rows
3. fetchall() returns all the rows

## Formatting Results

```python
items = c.fetchall()

for item in items:
    print("First Name:{}\tLast Name:{}\tEmail:{}".format(item[0],item[1],item[2]))
```

## Retrieving Row ID

sqlite generates a row ID for every row. It automatically increments on each record inserted
```python
c.execute("""SELECT rowid, *  FROM customers""")
```

## Using Where Clause

Where can be used to select specific records by providing the condition. For example the below example we are selecting all customers with last_name as Doe

```python
c.execute("""SELECT rowid, *  FROM customers WHERE last_name='Doe' """)
```

In this example below we are selecting all customers with name starting with J

```python
c.execute("""SELECT rowid, *  FROM customers WHERE first_name LIKE 'J%' """)
```

## Update Clause

To update a specific record / multiple records you can use the update statement like below:

```python
c.execute("""UPDATE customers SET last_name = 'Sundararaman'
    WHERE rowid = 1
""")
```

## Delete Clause
Can be used to delete record(s) based on condition

```python
c.execute("""DELETE from customers WHERE rowid = 4""")
```
