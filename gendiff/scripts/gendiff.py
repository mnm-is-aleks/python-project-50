import argparse
import json


def make_low_case(data):
    result = []
    for i in data:
        if 'False' in i:
            result.append(f'{i[:-6]} false')
        elif 'True' in i:
            result.append(f'{i[:-5]} true')
        else:
            result.append(i)
    return result


def generate_diff(file1, file2):
    with open(file1) as file_1, open(file2) as file_2:
        f_1 = json.load(file_1)
        f_2 = json.load(file_2)

    result_lines = []
    for key in sorted(f_1 | f_2):
        if f_1.get(key) == f_2.get(key):
            result_lines.append(f'  {key}: {f_1[key]}')
        elif key not in f_2:
            result_lines.append(f'- {key}: {f_1[key]}')
        elif f_1.get(key) != f_2.get(key):
            if f_1.get(key):
                result_lines.append(f'- {key}: {f_1[key]}')
            result_lines.append(f'+ {key}: {f_2[key]}')

    format_lines = make_low_case(result_lines)
    result = '{\n  ' + '\n  '.join(format_lines) + '\n}'
    print(f'{result}')


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '-f', '--format', type=str, help='set format of output'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    format_arg = args.format
    file_1 = args.first_file
    file_2 = args.second_file
    return format_arg, file_1, file_2


if __name__ == "__main__":
    arguments = main()
    if arguments[1] and arguments[2]:
        generate_diff(arguments[1], arguments[2])
