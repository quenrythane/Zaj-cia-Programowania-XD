import freestyle
import os


def append_data_to_comamnd_list(pack_list):
    existing_commands = []
    for pack in pack_list:
        points = len(pack_list)+1-pack[1]
        command = {
            'name': '',  # str
            'rank': 0,  # int
            'rank_list': [],  # list of ints
            'description': [],  # list of strs
        }

        if pack[0] in existing_commands:
            for i in ranking_commands_list:
                if i['name'] == pack[0]:  # jeśli taka komenda już jest to tylko dodaj punkty
                    i['rank_list'].append(points)

        else:
            existing_commands.append(pack[0])  # dodaj ją do existing list
            command['name'] = pack[0]  # dodaj jądo listty komend
            command['rank_list'].append(points)  # dodaj punkty
            command['description'] = pack[2]  # dodaj opis
            ranking_commands_list.append(command)


ranking_commands_list = []
# folders paths
prepath = r'C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica'
data_folder_path = fr'{prepath}\data-folder'
repo_folder_path = fr'{prepath}\LinuxHot16Challenge-main'
wasze_zwrotki_folder_path = fr'{prepath}\LinuxHot16Challenge-main\wasze_zwrotki'
wasze_zwrotki_freestyle_folder_path = fr'{prepath}\LinuxHot16Challenge-main\wasze_zwrotki_freestyle'
HERE = os.getcwd()  # C:\Users\Thane Art\PycharmProjects\.Kursy\Zajęcia Programowania XD\Piaskownica\Piaskownica 010

files = freestyle.get_files_from_folder(wasze_zwrotki_folder_path)[:3]  # get file adrian88szymanski_Linux_hot_16_challenge.txt

for file in files:
    lines = freestyle.return_lines_from_file(wasze_zwrotki_folder_path, file)  # lines from adrian
    data = freestyle.get_command_data(lines)  # list of tuples
    print(data)
    append_data_to_comamnd_list(data)

print(ranking_commands_list)
