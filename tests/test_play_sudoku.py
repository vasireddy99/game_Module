import unittest
from utils.play_sudoku import *
from mock_data import *


class testplaysudoku(unittest.TestCase):
    def test_isvalidsudoku(self):
        self.assertTrue(isValidSudoku(sudoku_input))

    def test_modify_board(self):
        self.assertTrue(modify_board(2, 2, 2, sudoku_input))

    def test_create_board(self):
        self.assertEqual(create_board(),create_board_output)


if __name__ == '__main__':
    unittest.main()
