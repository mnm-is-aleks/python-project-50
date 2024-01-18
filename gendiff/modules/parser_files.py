import json


def read_files(file1, file2):
    with open(file1) as file_1, open(file2) as file_2:
        f_1 = json.load(file_1)
        f_2 = json.load(file_2)
    return f_1, f_2
