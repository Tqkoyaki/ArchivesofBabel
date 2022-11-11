### What is a Database?
- A database is a file that is organized to store data. Most databases are like dictionaries in the sense they map keys to values.
- Databases are stored on permanent storage so they presist after the program ends and can store a lot of data.
- There are many different database systems. The most popular are MySQL, PostgreSQL, and SQLite.
- SQLite is designed to embedded into other applications to provide database support within the application.

### Database Concepts
- The primary data structures in a database are tables, rows, and columns. The formal terms are relations, tuples, and attributes but this is used less often.
- For Sqlite, you can use a browser to create tables, insert data, edit data, or run queries.

### Database Functions
- When we create a table we need to specify the name of each column and the type of data that will be stored in the column.
- The payoff of defining the structure ahead of time is the fast access to the data.
```python
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
```
- The connect operator makes a connection to the database with the name of the file in the database. If the file does not exist, it will be created.
- The cursor is like a file handle that is used to execute SQL statements. cursor() is very similar conceptually to the open() function.
- The execute() method is used to execute SQL statements.
- The database language used is called SQL (Structured Query Language) and is a standard language for interacting with databases.

### SQL
- The convention is to show SQL keywords in all caps and the names of tables and columns in lower case.
```SQL
-- This drops a table if it exists
DROP TABLE IF EXISTS Tracks
-- This creates a table with two columns, one is a text column and the other is an integer column
CREATE TABLE Tracks (title TEXT, plays INTEGER)
-- This inserts data into the table
INSERT INTO Tracks (title, plays) VALUES ('Thunderstruck', 20)
```
- In python we can use the `?` character to indicate a placeholder for a value. This is called a parameterized query.
```python
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
```
- Use conn.commit() to force save the changes to the database. (Only use it after a write operation)
```python
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
```
- In python after the execute() method, we can use a for loop to iterate through the rows of the result set. For efficiency, the rows are not stored in memory after execution instead they are read on demand in our for loop.
```SQL
-- Deletes all rows where plays is less than 100
DELETE FROM Tracks WHERE plays < 100
```
- `ORDER BY` is a clause that can be used during select to sort the results.
- Using * indicates all columns when used after `SELECT`.
- `WHERE` uses clauses like <, >, <=, >=, =, !=, as well as AND, OR.
- `UPDATE` is used to update a row in a table.
- The found basic SQL commands are INSERT, SELECT, UPDATE, DELETE.
- fetchone() is used to retrieve a single row from the result set. It is the first row in the result set. It returns the row as a tuple.
- `LIMIT` is used to limit the number of rows returned by a query.

### Basic Data Modeling
- Data modeling is the process of breaking up the application data into multiple tables and establishing relationships between the tables.
- Data models are the design documents that show the tables and the relationships between the tables.
- A common model used is a Relational Model. It is a model that uses tables and relationships between tables.
- One practice of database normalization is that we should never put the same string data in the database more than once. If we need the data more than once, we create a numeric key for the data and reference the actual data using this key.
```SQL
-- INTEGER PRIMARY KEY create a key value automatically
-- UNIQUE is used to ensure that the value is unique
CREATE TABLE People
    (id INTEGER PRIMARY KEY, 
    name TEXT UNIQUE, 
    retrieved INTEGER)
-- UNIQUE in this case is used to ensure that the combination of the two columns is unique
CREATE TABLE Follows
    (from_id INTEGER, 
    to_id INTEGER, 
    UNIQUE(from_id, to_id))
```
- Clauses like `UNIQUE` create set of rules that are enforced by the database which keep us from putting bad data into the database.
- `OR IGNORE` is used to ignore the command if it fails. This avoids an error if the data is already in the database.

### Types of Keys
- A logical key is a "real world" way to look up a row. For example, a person's name is an example of a logical key. A logical key doesn't have to be unique.
- A primary key is a number that is automically generated by the database. It is a unique id that has no meaning outside the program. It is the fastest way to look up a row.
- A foreign key is a number that points to a primary key in another table. It is used to establish a relationship between two tables.
- The naming convention is to use the name id for the primary key and the suffix _id for the foreign key.

### Using JOIN
```SQL
-- The join clause indicates that we are selecting fields from both tables
-- The on clause indicates how the two tables should be joined
SELECT * FROM Follows JOIN People
    ON Follows.from_id = People.id 
    WHERE Follows.from_id = 1
```
- The `JOIN` clause creates an extra-long row with fields from both coloumns.

### Debugging
- If you open SQLite database from the browser and haven't pressed saved, it locks the database file and keeps other programs from accessing it. A solution to it is use the file menu to close the database before you run your program.

### Glossary
- attribute: One of the named columns or field in a table.
- constraint: A rule that is enforced by the database.
- database browser: A program that allows you to view and edit the contents of a database.
- normalization: A process of organizing data in a database to reduce redundancy and dependency.
- relation: An area that contains tuples and attributes also known as a table.
- tuple: A single entry in a table also known as a row. It would be a set of attribute values.