import sqlite3


conn = sqlite3.connect("customers")

c = conn.cursor()

c.execute("""CREATE TABLE customers (
    first_name  text,
    last_name text,
    email  text
)
""")

conn.commit()