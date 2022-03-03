import freestyle
import os


ranking_commands_list = []
existing_commands = []
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
    freestyle.append_data_to_comamnd_list(ranking_commands_list, existing_commands, data)

print(ranking_commands_list)
def sort_ranking():


# !! <- poprzednie polecenie
