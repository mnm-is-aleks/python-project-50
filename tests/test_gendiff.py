import pytest
import os
import json
from gendiff.diff_generator import generate_diff


@pytest.fixture
def get_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_1 = os.path.join(current_dir, 'fixtures', 'file1.json')
    file_2 = os.path.join(current_dir, 'fixtures', 'file2.json')
    expected_output = os.path.join(current_dir, 'fixtures', 'expected_output.txt')
    return file_1, file_2, expected_output


def load_file_content(file_name):
    with open(file_name, 'r') as file:
        if file_name.endswith('.json'):
            return json.load(file)
        else:
            return file.read()


def test_generate_diff(get_path):
    file_1, file_2, expected_output = get_path

    result = generate_diff(file_1, file_2)

    expected_output = load_file_content(expected_output)
    assert result == expected_output