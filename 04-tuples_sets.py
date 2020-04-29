"""
A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
"""
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)

# Check if Apple is present in fruit_tuple
print('Apple' in fruit_tuple)

# Using constructor
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
# print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

'''
Deleting tuple ,
We can't delete individual element of tuple but whole tuple.
'''
del fruit_tuple_2


# Get length of tuple
print(len(fruit_tuple))
 

"""
A Set is a collection which is unordered and unindexed. No duplicate members.
"""
# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)
# Check if in set
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')   # In List , we had append()
print(fruit_set)

#Add diplicate value - it won't throw an error .However , it won't be added as well
fruit_set.add('Apple') 

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)

# Clear set - remove all elements from set
fruit_set.clear()
print(fruit_set)

# Delete set
del fruit_set

# print(fruit_set)