import unittest
from unittest.mock import patch

import pandas as pd

from src.file_operations import read_csv_file, read_excel_file


class TestFileOperations(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        # Подготовка тестовых данных
        test_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [100, 200],
            'description': ['test1', 'test2']
        })
        mock_read_csv.return_value = test_data

        # Вызов функции
        result = read_csv_file('dummy_path.csv')

        # Проверки
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['date'], '2023-01-01')
        mock_read_csv.assert_called_once_with('dummy_path.csv')

    @patch('pandas.read_excel')
    def test_read_excel_file(self, mock_read_excel):
        # Подготовка тестовых данных
        test_data = pd.DataFrame({
            'date': ['2023-01-03', '2023-01-04'],
            'amount': [300, 400],
            'description': ['test3', 'test4']
        })
        mock_read_excel.return_value = test_data

        # Вызов функции
        result = read_excel_file('dummy_path.xlsx')

        # Проверки
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['date'], '2023-01-03')
        mock_read_excel.assert_called_once_with('dummy_path.xlsx')
