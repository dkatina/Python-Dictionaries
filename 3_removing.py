# Removing items from a dictionary

dogs= {'Huge': 'Great Danes', 'Large': 'German Shepard', 'Medium': 'Pitt Bull', 'Shmedium' : 'Pug', 'Small':'Dachshund'}

#-- .pop(key) : remove the kvp associated with that key, return value

new_home = dogs.pop('Samll', "Not a category") #Adding a second argument with a message to prevent KeyErrors when using bad keys
print(new_home)

new_home = dogs.pop('Small')
print(dogs)

#-- .popitem() : remove the lates kvp (the one at the end), returns a tuple with the key and value (k, v)

dog = dogs.popitem()
print(dog)
print(dogs)

#--- del dictionary[key] : deletes the kvp at that key

del dogs['Large']

print(dogs)

# del dogs['Large'] #Throws a KeyError if the key is invalid


#--- clear() : removes all kvps from the dictionary

dogs.clear()

print(dogs)

