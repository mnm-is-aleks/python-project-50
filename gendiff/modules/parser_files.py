import json
import yaml


def read_files(file1, file2):
    with open(file1) as file_1, open(file2) as file_2:
        if file1.endswith('yaml') or file1.endswith('yml'):
            f_1 = yaml.safe_load(file_1)
        else:
            f_1 = json.load(file_1)
        if file2.endswith('') or file2.endswith('yml'):
            f_2 = yaml.safe_load(file_2)
        else:
            f_2 = json.load(file_2)
    return f_1, f_2
