# This application will read the mainbox data (Exercise_2_Input.txt) and count the number of email messages
# per organization (i.e. domain name of the email address) using a database with the following
# schema to maintain the counts. [CREATE TABLE Counts (org TEXT, count INTEGER)]
import sqlite3

# Connect to the database
conn = sqlite3.connect('./Chap 15 - Python and Databases/Exercise_2.sqlite')
cur = conn.cursor()

# Creates table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Reads the file
fname = './Chap 15 - Python and Databases/Exercise_2_Input.txt'
fh = open(fname)
for line in fh:
    # Gets an email
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]
    org = email.split('@')[1]
    
    # Gets count from database and updates it if it exists
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    data = cur.fetchone()
    if data is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 
                    WHERE org = ?''', (org,))
# Commits the changes into database
conn.commit()

# Verifies the results
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
print(cur.fetchone())
conn.close()
        
    