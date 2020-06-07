import unittest.mock as mock

from format_output.average_scores import average as avg


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert avg.average() == 90
