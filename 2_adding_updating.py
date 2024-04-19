#--- Adding and Updating KVPS

kitchen = {
    'drawer': 'silver ware', 
    "pantry": 'snacks', 
    'cabinet': 'plates',
    'drawer': 'socks'
    }


#-- add a kvp

#dictionary[new_key] = new_value

kitchen['fridge'] = 'cold stuff'

print(kitchen)

kitchen['freezer'] = 'frozen stuff'

print(kitchen)



#-- updating the value of a key

#dictionary[existing_key] = new_value

kitchen['cabinet'] = 'plates and bowls'
print(kitchen)


#-- incrementing values

stock = {'oranges': 10, 'apples': 2, 'pears':20}

#need to restock on apples need 10 more

stock['apples'] += 10

print(stock)

#-- decrementing values

#no one is buying my pears and they're rotting need to throw out 5

stock['pears'] -= 5
print(stock)


1
#---- .update({key, value}) : merges one dictionary into another, 
#updating any common keys to the new_values

car = {"year" : 1968, 'Make': 'Ford', 'Model': 'Mustang'}

car.update({"color": 'green'}) #adding kvps with .update()
print(car)

car.update({'color': 'black'}) #updating kvps with .update()
print(car)

car.update({'wheels': 4, 'engine': 'v8', 'year': 2024}) #adding and updating multiple things with .update()
print(car)