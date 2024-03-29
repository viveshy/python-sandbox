# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['viv', 'viv-bhai', 'vivesh', 'viveshCodes']

# Simple for loop
for person in people:
  print(f'Current person:  {person}')

# Break out
for person in people:
  if person == 'Janet':
    break
  print('Current person: ', person)

# Continue
for person in people:
  if person == 'Janet':
    continue
  print('Current person: ', person)


# Range
print("RANGE")
for i in range(len(people)):
  print('Current Person: ', people[i])


for i in range(0, 11 ,2):           # (a , b ,c)  a = inclusive , b = exclusive , c = increment / decrement
  print('Number ', i)


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
  print('Count: ', count)
  count += 1