#oart 1
students = [
  {'first_name': 'Michael', 'last_name': 'Jordan'},
  {'first_name': 'John', 'last_name': 'Rosales'},
  {'first_name': 'Mark', 'last_name': 'Guillen'},
  {'first_name': 'KB', 'last_name': 'Tonel'}
]

print students


#part2
users = {
    'students' : [
        {'id':1, 'first_name': 'Michael', 'last_name': 'Jordan'},
        {'id':2, 'first_name': 'John', 'last_name': 'Rosales'},
        {'id':3, 'first_name': 'Mark', 'last_name': 'Guillen'},
        {'id':4, 'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]

}

for key, data in users.items():
    print key.title()
    for value in data:
            print value['id'], '-', value ['first_name'] + "" + value ['last_name']
