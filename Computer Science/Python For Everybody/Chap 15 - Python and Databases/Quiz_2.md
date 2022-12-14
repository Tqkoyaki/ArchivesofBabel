### What is the primary added value of relational databases over flat files?
d) Ability to scan large amounts of data quickly

### What is the purpose of a primary key?
a) To look up a particular row in a table very quickly

### Which of the following is NOT a good rule to follow when developing a database model?
a) Use a person's email address as their primary key

### If our user interface (i.e., like iTunes) has repeated strings on one column of the user interface, how should we model this properly in a database?
d) Make a table that maps the strings in the column to numbers and then use those numbers in the column

### Which of the following is the label we give a column that the "outside world" uses to look up a particular row?
d) Logical key

### What is the label we give to a column that is an integer and used to point to a row in a different table?
d) Foreign key

### What SQLite keyword is added to primary keys in a CREATE TABLE statement to indicate that the database is to provide a value for the column when records are inserted?
a) AUTOINCREMENT

### What is the SQL keyword that reconnects rows that have foreign keys with the corresponding data in the table that the foreign key points to?
d) JOIN

### What happens when you JOIN two tables together without an ON clause?
d) The number of rows you get is the number of rows in the first table times the number of rows in the second table

### When you are doing a SELECT with a JOIN across multiple tables with identical column names, how do you distinguish the column names?
a) tablename.columnname