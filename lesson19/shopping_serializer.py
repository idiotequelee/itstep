import pickle
import json

shopping_list_example = [
    {
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "meat": 2.4
    },
    {
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "meat": 2.4,
    "eggs": 0.4,
    "fish": 2.4
     }
]

with open('shopping_list.pkl', 'wb') as f:
    f.write(pickle.dumps(shopping_list_example))

with open('shopping_list.json', 'w') as f:
    f.write(json.dumps(shopping_list_example, indent=2))