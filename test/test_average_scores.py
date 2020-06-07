"""
Program: test_average_scores.py
Author: Elizabeth Allen
Last date modified: 06/07/2020

The purpose of this program is to show the average test file.
The input is side_effect=[85,90,95].
The output will be an error, per the instructions.
"""

import unittest.mock as mock

from format_output.average_scores import average as avg


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert avg.average() == 90
