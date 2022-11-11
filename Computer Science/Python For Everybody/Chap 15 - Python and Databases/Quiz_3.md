### How do we model a many-to-many relationship between two database tables?
b) We add a table with two foreign keys

### In Python, what is a database "cursor" most like?
b) A file handle

### What method do you call in an SQLIte cursor object in Python to run an SQL command?
b) execute()

### In the following SQL, 
```python
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
```
### what is the purpose of the "?"?
b) It is a placeholder for the contents of the "org" variable

### In the following Python code sequence (assuming cur is a SQLite cursor object), 
```python
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
```
### what is the value in row if no rows match the WHERE clause?
b) None

### What does the LIMIT clause in the following SQL accomplish? 
```SQL
SELECT org, count FROM Counts
   ORDER BY count DESC LIMIT 10
```
b) It only retrieves the first 10 rows from the table

### What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?
b) It allows multiple SQL statements separated by semicolons

### What is the purpose of "OR IGNORE" in the following SQL: 
```SQL
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
```
b) It makes sure that if a particular title is already in the table, there are no duplicate rows inserted

### For the following Python code to work, what must be added to the title column in the CREATE TABLE statement for the Course table: 
```python
cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', ( title, ) )
cur.execute('SELECT id FROM Course WHERE title = ? ',
    (title, ))
```
### course_id = cur.fetchone()[0]
b) A UNIQUE constraint

### What do we generally avoid in a many-to-many junction table?
[] Two foreign keys
[x] An AUTOINCREMENT primary key column
[] Data items specific to the many-to-many relationship
[x] A logical key

