import json

# Open the JSON file
with open('comments.json') as file:
    # Load the JSON data
    data = json.load(file)

# Count the number of comment entries
total_comments = len(data)

# Print the result
print(f'Total number of comment entries: {total_comments}')

#print("Comment ID:", data[0]["id"])