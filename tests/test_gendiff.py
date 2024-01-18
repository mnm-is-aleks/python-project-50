import pytest
import os
import json
from gendiff.diff_generator import generate_diff


@pytest.fixture(params=[('file1.json', 'file2.json'), ('file1.yaml', 'file2.yaml'),
                        ('file1.yml', 'file2.yml'), ('file1.json', 'file2.yaml'),
                        ('file1.json', 'file2.yml'), ('file1.yaml', 'file2.yml')])


def get_path(request):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_1 = os.path.join(current_dir, 'fixtures', request.param[0])
    file_2 = os.path.join(current_dir, 'fixtures', request.param[1])
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