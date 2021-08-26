import unittest
import os

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(os.getcwd())
    runner = unittest.TextTestRunner()
    runner.run(suite)