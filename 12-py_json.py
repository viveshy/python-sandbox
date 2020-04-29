# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "vivesh", "last_name": "yadav", "age": 21}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'brand': 'Tesla', 'model': 'X', 'body-style':'5 door SUV'}

carJSON = json.dumps(car)

print(carJSON)
