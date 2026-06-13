#dictionary 1
myself = {'name': 'Jack', 'age': 21, 'favourite player': 'Alcaraz'}

#dictionary 2
players = {'Zverev': 3, 'Shelton': 5, 'Sinner': 1, 'Alcaraz': 2, 'Felix': 4}

#loop through dictionary 
for player, rank in players.items():
    print(f'{player}, {rank}')

#Tuple 
Wimbledon_champ = (2025, 'Sinner')

print(f'The {Wimbledon_champ[0]} Wimbledon champion was {Wimbledon_champ[1]}')

#uniqueness of sets
players_2 = ['Zverev', 'Sinner', 'Sinner', 'Alcaraz']
players_unique = set(players_2)
print(players_unique)

#player ranking
print('Alcaraz\'s ranking is ', players['Alcaraz'])

#define variables
name = myself['name']
age = myself['age']
favourite_player = myself['favourite player']
ranking = players[favourite_player]

#final message
message = (
    f'Hello, my name is {name}, I am {age} years old, my favourite player is' 
    f'{favourite_player} who is ranked {ranking} in the world.'
)
print(message)