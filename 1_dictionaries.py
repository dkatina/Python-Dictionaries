#Dictionaries in python are a datatype to store a collection of key-value pairs

#features:
#--- Mutable : you can manipulate the data without moving it to a new location in memory
#--- Key-Value Pairs : instead of indices pointing to items in a collection, we have
# label (keys) that point to items  (values).
#--- They are unordered "technically"

#features of key-value pairs (kvp):
#-- Keys must be unique (one key -> one value)
#-- Keys are typically strings (can be other immutable datatypes)
#-- Values are Flexible, and can change (And can be just about any datatype)
#-- You can hav duplicate values


#---- Creating Dictionaries using curly braces

empty_dict = {} #use curly braces when define dictionary

#defining a populated dictionary

#syntax
#dictionary = {key: value, key2: value2}

kitchen = {
    'drawer': 'silver ware', #keys and values separated by colon, whole kvps separated by comma
    "pantry": 'snacks', 
    'cabinet': 'plates',
    'drawer': 'socks'
    }


print(kitchen)


#----- Accessing Values from Dictionaries

#syntax
#dictionary[key] return value associated with that key

utencils = kitchen['drawer']
print(utencils)


#KeyErrors - trying to use a key that doesn't exist

# kitchen['fridge']

# A way to avoid KeyErrors is to use .get()

print(kitchen.get('pantry')) #returns snack
print(kitchen.get('fridge')) #returns None since fridge is not a key in my dict

#add custom message to be displayed in the event that you use a bad key

print(kitchen.get('pant', 'BAD KEY'))

#can store keys in variables to be used

my_key = 'fridge'

print(kitchen.get(my_key, f'{my_key} is not a key in your dictionary'))

