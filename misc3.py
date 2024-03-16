import sqlite3
import json

with open("comments.json", 'r') as json_file:
    data = json.load(json_file)

error_entries = []

# Create a new SQLite database
conn = sqlite3.connect('comments2.db')
cursor = conn.cursor()

# Insert each comment as a new row in the 'comments' table
for comment in data:
    try:
        snippet = comment.get('snippet', {})
        author_channel_id = snippet.get('authorChannelId', {}).get('value', '') if snippet.get('authorChannelId') else ''
        cursor.execute('''
            INSERT INTO comments (
                kind, etag, id, channelId, textDisplay, textOriginal, parentId,
                authorDisplayName, authorProfileImageUrl, authorChannelUrl,
                authorChannelId, canRate, viewerRating, likeCount, publishedAt,
                updatedAt, negative, angry, spam, response
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            comment.get('kind', ''),
            comment.get('etag', ''),
            comment.get('id', ''),
            snippet.get('channelId', ''),
            snippet.get('textDisplay', ''),
            snippet.get('textOriginal', ''),
            snippet.get('parentId', ''),
            snippet.get('authorDisplayName', ''),
            snippet.get('authorProfileImageUrl', ''),
            snippet.get('authorChannelUrl', ''),
            author_channel_id,
            snippet.get('canRate', 0),
            snippet.get('viewerRating', 0),
            snippet.get('likeCount', 0),
            snippet.get('publishedAt', ''),
            snippet.get('updatedAt', ''),
            0, 0, 0, ''
        ))
    except Exception as e:
        print(f"Error: {e} occurred. Skipping this entry.")
        error_entries.append(comment)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Save error entries to "error_entries.json" file
with open('error_entries.json', 'w') as file:
    json.dump(error_entries, file)
