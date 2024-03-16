import sqlite3
import json

# Load JSON data from file
with open('comments.json') as f:
    data = json.load(f)

# Connect to SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE comments
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  body TEXT,
                  negative INTEGER,
                  angry INTEGER,
                  spam INTEGER,
                  response INTEGER)''')

# Insert data into table
for comment in data:
    cursor.execute('''INSERT INTO comments
                      (id, name, email, body, negative, angry, spam, response)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (comment['id'], comment['name'], comment['email'], comment['body'], 0, 0, 0, 0))

# Commit changes and close connection
conn.commit()
conn.close()