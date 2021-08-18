import unittest
from utils.sudoku_solver import *
from mock_data import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_sudoku_solver(self):
        self.assertEqual(solve_sudoku(sudoku_input), sudoku_solver_response)

if __name__ == '__main__':
    unittest.main()