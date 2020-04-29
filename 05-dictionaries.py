"""
 A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
-In JS , we have OBJECT .
"""

# Simple dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}
'''
In JS ,
person = {
  first_name : 'Vivesh',  // key is not put within quotes
  last_name : 'Yadav',
  age : 21
}
'''
print(person)
# Using a constructor
# person = dict(first_name='John', last_name='Doe',age=30)

# Access value
print(person['first_name'])   
# In JS , we can do this as well as , console.log(person.first_name);
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Bangalore'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

print(person)

# List of dict
people = [
  {'name': 'Martha', 'age': 40},
  {'name': 'Bob', 'age': 20}
]
print(people[1]['name'])