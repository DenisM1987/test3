from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json_file


@pytest.fixture
def valid_json_data():
    return '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'


def test_read_valid_json_file(valid_json_data):
    with patch('builtins.open', mock_open(read_data=valid_json_data)):
        result = read_json_file('dummy_path.json')
        assert len(result) == 2
        assert result[0]['id'] == 1


def test_read_empty_file():
    with patch('builtins.open', mock_open(read_data='')):
        result = read_json_file('empty.json')
        assert result == []


def test_read_non_list_json():
    with patch('builtins.open', mock_open(read_data='{"id": 1}')):
        result = read_json_file('not_a_list.json')
        assert result == []


def test_file_not_found():
    result = read_json_file('nonexistent.json')
    assert result == []
