import json

with open("shopping_list.json") as f:
    data = json.load(f)

print(data)