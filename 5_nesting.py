#Nesting Dictionaries and Lists

#lists inside Dictionaries

pet_names ={
    'Dogs': ['Oreo', 'Bailey', 'Fido', 'Punkin', 'Baby', 'Trouble'],
    'Cats': ['Mittens', 'CatKeisha', 'Snowball', 'Cookie', 'Smokey'],
    'Hamster': ['Cheddars', 'Hamtarro', 'Lightning', 'Turbo', 'Hammie'],
    'Lizards': 'Lizzy'
}

#we can chain keys and indices one after another
print(pet_names['Cats'][3])

for pet, names in pet_names.items():
    print(f'\nCommon {pet} names:')
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)


#Dictionaries inside of lists:

books = [
    {'Title': 'Diary of a Wimpy Kid', 'Author': 'Jeff Kiney', 'Genre': 'YAF'},
    {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert Kiwaske', 'Genre': 'Self Help'},
    {'Title': 'Dune', 'Author': 'Frank Herbert', 'Genre': 'Science Fiction'}
]

#we can chain keys and indices one after another
print(books[0]['Author'])

for book in books:
    print(f'{book["Title"]} is written by {book["Author"]}')


#Dictionaries within Dictionaries


user = {
    'dk@email.com': {'username': 'dylank' , 'password': '12345', 'likes': ['tacos', 'dogs']},
    'tp@email.com': {'username': 'travisp', 'password': '67890', 'likes': ['key lime pie', 'walks on the beach']},
    'rk@dogmail.com': {'username': 'Rhiannon-Bananan', 'password':'password', 'likes': ['treats', 'walks on the beach']}
}

print(user['tp@email.com']['likes'][0])


def login(user_dict):

    while True:
        try:
            email = input('email: ')
            password = input('password: ')
            user = user_dict[email]
            if password != user['password']:
                raise ValueError
        except:
            print('invalid email or password')
        else:
            print(f'Welcome back {user["username"]}')
            break


login(user)