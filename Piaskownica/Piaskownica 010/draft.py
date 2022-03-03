
ranking_commands_list = []

for i in range(4):
    command = {
        'name': '',  # str
        'rank': 0,  # int
        'rank_list': [],  # list of ints
        'description': [],  # list of strs
    }

    print('początek', command)
    command['name'] = f'komenda_{i}'
    command['rank_list'] = []
    command['rank_list'].append(10+i)
    command['description'] = 'do xyz'
    ranking_commands_list.append(command)
    print('koniec', command)
    print(ranking_commands_list, '\n')

print(ranking_commands_list)
print(ranking_commands_list[0]['name'])
for el in ranking_commands_list:
    if el['name'] == 'komenda_1':
        el['name'] = 'komenda_5'

print(ranking_commands_list)
my = [1, 2, 3, 4]
print(my[:])

