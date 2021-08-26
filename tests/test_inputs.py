import unittest
from unittest import mock
from controller import inputs
from mock_data import *


class TestInputs(unittest.TestCase):

    @mock.patch.object(inputs, "solve_board(board)")
    def test_solve_sudoku(self):
        board = sudoku_input
        inputs.solve_board(board)
        mock.assert_called()


if __name__ == '__main__':
    unittest.main()
