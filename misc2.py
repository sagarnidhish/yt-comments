import sqlite3
import json


with open("comments.json", 'r') as json_file:
    data = json.load(json_file)

error_entries = []

# Create a new SQLite database
conn = sqlite3.connect('comments2.db')
cursor = conn.cursor()

# Set default values for columns where data does not exist
cursor.execute('''
    INSERT INTO comments (
        kind, etag, id, channelId, textDisplay, textOriginal, parentId,
        authorDisplayName, authorProfileImageUrl, authorChannelUrl,
        authorChannelId, canRate, viewerRating, likeCount, publishedAt,
        updatedAt, negative, angry, spam, response
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 0, 0, ''
))

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
        error_entries.append(comment)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Save error entries to "error_entries.json" file
with open('error_entries.json', 'w') as file:
    json.dump(error_entries, file)

