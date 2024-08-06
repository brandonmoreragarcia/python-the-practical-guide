import copy

original_list = [
    {
        'name': 'brandon',
        'age': 27,
        'hobbies': ['music', 'sports','videogames']
    },
    {
        'name': 'Rommel',
        'age': 22,
        'hobbies': ['anime', 'coffee','shopping']
    },
    {
        'name': 'Elias',
        'age': 27,
        'hobbies': ['reading', 'crossfit','cooking']
    },
]

name_list = [person['name'] for person in original_list]
print('names: ', name_list)

are_all_over_20 = all([person['age'] > 20 for person in original_list])

print('all over 20: ', are_all_over_20)

copied_list = copy.deepcopy(original_list)
copied_list[0]['name'] = 'Josu'

print(original_list)
print(copied_list)

person1, person2, person3 = copied_list

print(person1)
print(person2)
print(person3)