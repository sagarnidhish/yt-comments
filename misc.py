import json

# Load the JSON data from the file
with open("comments.json", 'r') as json_file:
    data = json.load(json_file)
i = 0
# Iterate over each entry in the JSON data
#for i in data:
print("Comment ID:", data[i]["id"])
print("Text Display:", data[i]["snippet"]["textDisplay"])
print("Author:", data[i]["snippet"]["authorDisplayName"])
print("Published At:", data[i]["snippet"]["publishedAt"])
print("Like Count:", data[i]["snippet"]["likeCount"])
print("Source:", data[i]["source"])
print()  # Add a newline for better readability
