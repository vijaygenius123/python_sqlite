# SQLite With Python

SQLite is a default python package can be be imported using the below statement

```python
import sqlite3
```
You can connect to a existing sqlite3 database or create a new one by using the connect() method. Since sqlite3 is a file you will need to pass the path of the file , incase the file does not exist the module will create a new file in the path

```
conn  = sqlite3.connect("customers")
```