from gendiff.modules import parser_files as pf
from gendiff.modules import formatter
from gendiff.modules import comparator


def generate_diff(file1, file2):
    f_1, f_2 = pf.read_files(file1, file2)
    result_lines = comparator.compare_dct(f_1, f_2)
    result = formatter.make_string(result_lines)
    return result
