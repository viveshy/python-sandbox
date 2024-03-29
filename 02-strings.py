# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

"""
*************___________CONCATENATION_______****************
"""
name = 'viveshCodes'
age = 21

# Concatenate
# We can concatenate only string.
# print('Hello I am ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
# print('My name is {name} and I am {age}'.format(name=name, age=age))

'''
The method given below is convenient for concatenation :
'''
# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')  # In JS , console.log(`My name is ${name} ans I am ${21}`);



"""
**************_______________STRING METHODS__________________*******************
"""
# String Methods

s = 'hello python Developers'

# Capitalize first letter and make all other letters small
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
t = s.replace('hello' , 'hey')
print(t)

# Count
sub = "h"
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

