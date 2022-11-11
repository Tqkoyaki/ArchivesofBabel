# This application will read roster data in JSON format, parse the file, and then
# produce an SQLite database that contains a User, Course, and Member table and
# populate the tables from the data file.
import json
import sqlite3

# Connects to the database
conn = sqlite3.connect('./Chap 15 - Python and Databases/Exercise_4.sqlite')
cur = conn.cursor()

# Creates the database
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Loads the json file
fh = open('./Chap 15 - Python and Databases/Exercise_4_Input.json')
members = json.load(fh)

# Loops through all the members
for member in members:
    name = member[0]
    course = member[1]
    role = member[2]
    
    # Inserts data into the database
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

# Commits the changes
conn.commit()

# Verifies the results
cur.execute('''SELECT User.name,Course.title, Member.role FROM 
            User JOIN Member JOIN Course 
            ON User.id = Member.user_id AND Member.course_id = Course.id
            ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')
for row in cur:
    print(row)
    
# Query data for answer
cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
            User JOIN Member JOIN Course 
            ON User.id = Member.user_id AND Member.course_id = Course.id
            ORDER BY X LIMIT 1;''')
print('Answer:', cur.fetchone()[0])

# Closes the database
conn.close()

