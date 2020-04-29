# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

'''
# Core modules
'''
#datetime
from datetime import date

today = date.today()

print(today)
# _________________________________

#time
from time import time

timestamp = time()

print(timestamp)
# __________________________________


'''
Pip modules
'''
#Firstly run this command , pip install camelcase
import camelcase
from camelcase import CamelCase
camel = camelcase.CamelCase()

intro="vivesh codes is my username"
introNew = camel.hump(intro) 
print(introNew)


'''
 Custom modules - user defined modules
 '''

import validator
from validator import validate_email


email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Not an email')