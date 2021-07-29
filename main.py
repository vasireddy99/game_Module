from play_sudoku import *
from games import *
from sudoku_solver import *
from inputs import *

def user_choice():
    print("choose either play or solve")
    x = input()
    if x =='play':
        print('you chose to play, select the board')
        user_input()

        ## step1####
        ## board ##

    if x == 'solve':
        print('You chose to solve, provide the board')
        #step 2:
        ## user can provide direct board##
        board = [[0 for i in range(9)] for i in range(9)]
        solve_board(board)

if __name__ == "__main__":
    user_choice()