#Looping over dictionaries

chips = {"Cheeto": "Flamin Hot", "Dorito": "Cool Ranch", "Takis":'Fuego', "Miss Vickies": "Spicy Dill Pickle"}

#looping keys of a dictionary

#---- .keys() : be explicit

print("Major Chip Brands")
print("-----------------")
for key in chips.keys():
    print('Key', key)
    print('Value', chips[key])


#looping over values of a dictionary

#----- .values()

print("\nFlavors")
print("--------------")
for value in chips.values():
    print(value)


#looping over both keys and value at the same time

print('\nMy favorite flavor per chip')
print("--------------")
for key, value in chips.items():
    print(f'My favorit {key} flavor is {value}!')
