import sqlite3
import json

# Create a new SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Create the 'comments' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        kind TEXT,
        etag TEXT,
        id TEXT,
        channelId TEXT,
        textDisplay TEXT,
        textOriginal TEXT,
        parentId TEXT,
        authorDisplayName TEXT,
        authorProfileImageUrl TEXT,
        authorChannelUrl TEXT,
        authorChannelId TEXT,
        canRate INTEGER,
        viewerRating TEXT,
        likeCount INTEGER,
        publishedAt TEXT,
        updatedAt TEXT,
        negative INTEGER,
        angry INTEGER,
        spam INTEGER,
        response TEXT
    )
''')

# Load data from "comments.json" file
with open('comments.json') as file:
    data = json.load(file)

# Insert each comment as a new row in the 'comments' table
for comment in data:
    try:
        cursor.execute('''
            INSERT INTO comments (
                kind, etag, id, channelId, textDisplay, textOriginal, parentId,
                authorDisplayName, authorProfileImageUrl, authorChannelUrl,
                authorChannelId, canRate, viewerRating, likeCount, publishedAt,
                updatedAt, negative, angry, spam, response
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            comment.get('kind', ''), comment.get('etag', ''), comment.get('id', ''),
            comment['snippet'].get('channelId', ''),
            comment['snippet'].get('textDisplay', ''), comment['snippet'].get('textOriginal', ''),
            comment['snippet'].get('parentId', ''), comment['snippet'].get('authorDisplayName', ''),
            comment['snippet'].get('authorProfileImageUrl', ''), comment['snippet'].get('authorChannelUrl', ''),
            comment['snippet']['authorChannelId'].get('value', ''), comment['snippet'].get('canRate', ''),
            comment['snippet'].get('viewerRating', ''), comment['snippet'].get('likeCount', ''),
            comment['snippet'].get('publishedAt', ''), comment['snippet'].get('updatedAt', ''),
            0, 0, 0, ''
        ))
    except KeyError as e:
        print(f"KeyError: {e} occurred. Skipping this entry.")


# Commit the changes and close the connection
conn.commit()
conn.close()

