import os
from string import whitespace

"""
Cel:

A. Strona www z rankingiem naj lepszych wg. was kome
1. Dane w folderze w formie plików txt.
2. Program pobierający dane do folderu z danymi.
3. Struktura danych
4. Parser - program przerzucający dane z txt do struktury danych
---- akumulowanie danych (nie nadpisywanie)
# parser - przerzucenie dany z jednego formatu do drugiego (np z tekstowego do naszej struktury danych)
5. Algorytm czyszczący dane
6. Algorytm liczący ranking
7. Zakłładka na stronie gdzie to wystawimy
"""


def get_files_from_folder(folder_path: str) -> list:
    files_list = os.listdir(folder_path)
    filter_list = ['README.md', 'TWOJEIMIE_linux_hot_16_challenge.txt', 'TWOJEIMIE_linux_hot_16_challenge_freestyle.txt']  # files I want to exclude from files
    return [file for file in files_list if file not in filter_list]


def return_lines_from_file(path, file):
    file_path = os.path.join(path, file)

    with open(file_path, 'r', encoding='utf-8') as file_inside:
        text_lines = file_inside.readlines()

    try:
        x = text_lines.index('#### ZPXD:\n')   # files end with "banner" so i find it and slice text_lines in this place
        return [line.strip() for line in text_lines[:x] if line not in whitespace]
    except:
        return [line.strip() for line in text_lines[:] if line not in whitespace]


def get_command_data(text_lines):
    result = []
    for i, line in enumerate(text_lines):
        line = line.split()
        if line[1][0].isdigit():
            name = line[2].strip()
            ranking = int(line[1][:-1])
            description = ' '.join(text_lines[i+1].split()[1:]).strip()
            result.append((name, ranking, description))
    return result
