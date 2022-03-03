# from flask import Flask, render_template
import os

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


# app = Flask(__name__)

# data structures
ranking_commands_list = []
command = {
    'name':         None,   # str
    'rank':         None,   # int
    'rank_list':    [],     # list of ints
    'description':  [],     # list of strs
}

# folders paths
data_folder_path = r'C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\data-folder'
repo_folder_path = r'C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\LinuxHot16Challenge-main'
wasze_zwrotki_folder_path = r'C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\LinuxHot16Challenge-main\wasze_zwrotki'
wasze_zwrotki_freestyle_folder_path = r'C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\LinuxHot16Challenge-main\wasze_zwrotki_freestyle'


HERE = os.getcwd()  # C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\Piaskownica 010

def load_data_from_folder(folder_path):
    files_list = os.listdir(folder_path)
    filter_list = ['README.md', 'TWOJEIMIE_linux_hot_16_challenge.txt', 'TWOJEIMIE_linux_hot_16_challenge_freestyle.txt']  # files I want to exclude from files

    for file in files_list:
        if file == 'Demetress_linux_hot_16_challenge':
            break
        if file in filter_list:
            continue
        print(file)
        # file_path = f'{wasze_zwrotki_folder_path}\{file}'
        file_path = os.path.join(wasze_zwrotki_folder_path, file)

        with open(file_path, 'r', encoding='utf-8') as file_inside:
            text_lines = file_inside.readlines()
        print(text_lines)



load_data_from_folder(wasze_zwrotki_folder_path)

