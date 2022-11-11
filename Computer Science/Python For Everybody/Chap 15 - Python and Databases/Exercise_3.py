# The application will read an iTunes export file in XML and produce a
# properly normalized database.
import xml.etree.ElementTree as ET
import sqlite3

# # Connects to the database
conn = sqlite3.connect('./Chap 15 - Python and Databases/Exercise_3.sqlite')
cur = conn.cursor()

# Creates the database
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

cur.execute('''CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    )''')

# Opens the xml file
tree = ET.parse('./Chap 15 - Python and Databases/Exercise_3_Input.xml')
results = tree.findall('dict/dict/dict')

# Loops through all the tracks
for result in results:
    # Setups dictionary to store the data we want
    data = {'Artist': None, 'Genre': None, 'Album': None, 
            'Name': None, 'Total Time': None, 'Rating': None,
            'Track Count': None}
    
    # Gets the data from the xml file
    key = ''
    for child in result:
        if child.tag == 'key':
            key = child.text
        else:
            if key in data:
                data[key] = child.text

    # Inserts data into the database
    album_id = None
    genre_id = None
    if data['Artist'] is not None:
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (data['Artist'], ))
        if data['Album'] is not None:
            cur.execute('SELECT id from Artist WHERE name = ?', (data['Artist'],))
            cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (data['Album'], cur.fetchone()[0]))
            
            cur.execute('SELECT id from Album WHERE title = ?', (data['Album'],))
            album_id = cur.fetchone()[0]
    
    if data['Genre'] is not None:
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (data['Genre'],))
        
        cur.execute('SELECT id from Genre WHERE name = ?', (data['Genre'],))
        genre_id = cur.fetchone()[0]
    
    if data['Name'] is not None:
        cur.execute('INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)',
                    (data['Name'], album_id, genre_id, data['Total Time'], data['Rating'], data['Track Count']))
    
# Commits the changes
conn.commit()

# Verifies the results
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
            FROM Track JOIN Genre JOIN Album JOIN Artist 
            ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
            AND Album.artist_id = Artist.id
            ORDER BY Artist.name LIMIT 3''')
for row in cur:
    print(row)

# Closes the database
conn.close()

        
    