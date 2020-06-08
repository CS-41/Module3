"""
Program: test_average_scores.py
Author: Elizabeth Allen
Last date modified: 06/07/2020

The purpose of this program is to show the average test file.
The input is side_effect=[].
The output will be verifying the function.
"""

import unittest
import unittest.mock as mock
from format_ouput import average_scores as avg


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert avg.average() == 90


if __name__ == '__main__':
    unittest.main()
