  ulubioneMiejsca = {
    'Kuba': ['Paryż', 'Tokio', 'Wrocław'],
    'Patrycja': ['Wrocław', 'Moskwa', 'Berlin'],
    'Karol': ['Kraków', 'Toruń', 'Wieluń'],

}

for osoba, miejsce in ulubioneMiejsca.items():
    i = 1
    print('Ulubione miejsce użytkownika ' + str(osoba) + ' to: ')
    if osoba == 'Kuba':
        for miejsce in ulubioneMiejsca['Kuba']:
            print('\t' + str(i) + ') ' + miejsce)
            i += 1
        print()
    elif osoba == 'Patrycja':
        for miejsce in ulubioneMiejsca['Patrycja']:
            print('\t' + str(i) + ') ' + miejsce)
            i += 1
        print()
    else:
        for miejsce in ulubioneMiejsca['Karol']:
            print('\t' + str(i) + ') ' + miejsce)
            i += 1

"""
ulubioneMiejsca = {
    'Kuba': ['Paryż', 'Tokio', 'Wrocław'],
    'Patrycja': ['Wrocław', 'Moskwa', 'Berlin'],
    'Karol': ['Kraków', 'Toruń', 'Wieluń'],

}

for osoba, miejsce in ulubioneMiejsca.items():
    i = 1
    print('Ulubione miejsce użytkownika ' + str(osoba) + ' to: ')
    for m in miejsce:

        print('\t' + str(i) + ') ' +str( m))
        i+=1
"""