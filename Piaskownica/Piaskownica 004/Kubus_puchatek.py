import requests


link = 'https:  '
# print(requests.get(link), '\n')
kubus_text = requests.get(link).text
# requests.get(link).text.encode('utf-8')

# dziele tekst strony na linijki
kubus_lines = kubus_text.split('</p>')
sh = 'Batman'  # sh = secret herro

# każdą linijkę dodaje pojedynczo do listy
kubus_lines_list = []
for line in kubus_lines:
    kubus_lines_list.append(line[4:])

# Zapisuje tylko te linijki które mają słowo Kubuś lub Kubusiu w sobie.
# licze ile ich jest. I zamieniam Słowo kubuś na słowo Batman, a słowo Kubusie na Batmanie
number_of_lines = 0
batman_list = []
for i, line in enumerate(kubus_lines_list):
    if 'Kubus' in line:
        batman_list.append(line.replace('Kubus', sh))
        number_of_lines += 1
    elif 'Kubuś' in line:
        batman_list.append(line.replace('Kubuś', sh))
        number_of_lines += 1

print('<h2>Co by się stało, gdyby zamienić postać Kubusia, Batmanem?</h2>\n')
for line in batman_list:
    print(f'<p>{line}</p>')


print('\n', number_of_lines, 'linii zawiera słowo Batman')
