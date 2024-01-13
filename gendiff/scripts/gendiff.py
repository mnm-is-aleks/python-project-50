import argparse


parser = (
    argparse.ArgumentParser
    (description='Compares two configuration files and shows a difference.'))
parser.add_argument('-f', '--format', type=str, help='set format of output')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.print_help()


def main():
    pass


if __name__ == "__main__":
    main()
