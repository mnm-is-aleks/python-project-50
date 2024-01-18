import argparse
from gendiff.diff_generator import generate_diff


def run_gendiff(file_1, file_2):
    if file_1 and file_2:
        print(generate_diff(file_1, file_2))


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
    file_1 = args.first_file
    file_2 = args.second_file
    run_gendiff(file_1, file_2)


if __name__ == "__main__":
    main()
