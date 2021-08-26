from utils.play_sudoku import *
from utils.solve_sudoku import *
from utils.games import *
import time


def player_input():
    while True:
        player_choice = input("Please choose 'easy', 'medium' or 'hard'")
        if player_choice.upper() not in ['EASY', 'MEDIUM', 'HARD']:
            print("yes")
            continue
        else:
            break
    if player_choice.upper() == "EASY":
        play_board(game1)

    elif player_choice.upper() == "MEDIUM":
        play_board(game2)

    if player_choice.upper() == "HARD":
        play_board(game3)


def solve_board(board):
    sudoku_filled_count = 0
    while True:

        print_board(board)
        revert_board = board
        print("select coordinates on the board")
        row = valid_row_input()
        col = valid_column_input()
        value = valid_value_input()

        if not modify_board(row, col, value, board):
            continue
        if not isValidSudoku(board):
            print("invalid sudoku inputs, Please enter the valid inputs again")
            board = revert_board
            continue
        sudoku_filled_count += 1
        if sudoku_filled_count > 9:
            print("do you want to provide more inputs, select 'y' or 'n'")
            if valid_selection_input():
                continue
            else:
                break

    print("The Sudoku is being solved by bot")
    sudoku_solver(board)
    print_board(board)


def play_board(board):
    start_time = time.time()
    while True:
        print_board(board)
        row = valid_row_input()
        col = valid_column_input()
        value = valid_value_input()
        if modify_board(row, col, value, board):
            if isValidSudoku(board):
                pass
            else:
                print("invalid sudoku inputs, Please enter the valid inputs again")
                continue
        if board_full(board):
            end_time = time.time()
            print("you did it")
            score = caluclate_score(start_time, end_time)
            print("player score is {}".format(score))
            break
