import unittest
from utils.play_sudoku import *
from mock_data import *


class MyTestCase(unittest.TestCase):
    def test_isvalidsudoku(self):
        self.assertTrue(isValidSudoku(sudoku_input))

    def test_modify_board(self):
        self.assertTrue(modify_board(2, 2, 2, sudoku_input))

    def

if __name__ == '__main__':
    unittest.main()
