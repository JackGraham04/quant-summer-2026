# import necessary modules
from random import randint as ri
from random import choice as rc

characters = []
new_character = 'y'

# create total stats and character display functions
def total_stats(*args):
    return sum(args)

def display_character(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print('Create a character - Class types: Warrior, Mage, Healer')

# user input to create characters
while new_character == 'y':
    character = {'name': input('Name:'), 'class': input('Class:')}
    character['strength'] = ri(1,10) 
    character['magic'] = ri(1,10)
    character['health'] = ri(1,10)
    characters.append(character)

    if character['class'].lower() == 'warrior':
        character['strength'] += 5
    elif character['class'].lower() == 'mage':
        character['magic'] += 3
    else:
        character['health'] += 4

    display_character(
    Name=character['name'],
    Class=character['class'],
    Strength=character['strength'],
    Magic=character['magic'],
    Health=character['health'])

    total = total_stats(character['strength'], character['magic'], character['health'])
    print(f'Total stats: {total}')

    print('Character created!')

    new_character = input('Create another character? (y/n)')

# finding strongest character
strongest = characters[0]

for character in characters:
    total = total_stats(character['strength'], character['magic'], character['health'])
    strongest_total = total_stats(strongest['strength'], strongest['magic'], strongest['health'])
    if total > strongest_total:
        strongest = character

strongest_name = strongest['name']
strongest_total = total_stats(strongest['strength'], strongest['magic'], strongest['health'])
i=1

# character displayed
print('Characters Created:')
for character in characters:
    name = character['name']
    classed = character['class']
    print(f'{i}.  {name}  ({classed})')
    i += 1

# strongest character displayed
print('Strongest Character:')
print(f'{strongest_name}  (Total power {strongest_total})')

# battle simulator
if len(characters) >= 2:

    fighter_1 = rc(characters)
    fighter_2 = rc(characters)

    while fighter_2 == fighter_1:
        fighter_2 = rc(characters)

    fighter_1_total = total_stats(fighter_1['strength'], fighter_1['magic'], fighter_1['health'])
    fighter_2_total = total_stats(fighter_2['strength'], fighter_2['magic'], fighter_2['health'])
    fighter_1_name = fighter_1['name']
    fighter_2_name = fighter_2['name']

    print(f'{fighter_1_name} vs {fighter_2_name} ... let the best fighter win')

    if fighter_1_total > fighter_2_total:
        print(f'{fighter_1_name} wins!')
    elif fighter_1_total < fighter_2_total:
        print(f'{fighter_2_name} wins!')
    else:
        print('It\'s a draw')
else:
    print('Need at least two characters for a battle')